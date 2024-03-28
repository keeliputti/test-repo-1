from typing import Optional
from pydantic import BaseModel

class Class1(BaseModel):
    flag: str

class Class2(BaseModel):
    data1: str
    data2: int
    data3: Optional[str] = None


from typing import Union

class CombinedSchema(BaseModel):
    class1: Class1
    class2: Union[Class2, None]

    @classmethod
    def __get_validators__(cls):
        yield from super().__get_validators__()
        yield cls.validate_flag

    @classmethod
    def validate_flag(cls, value):
        if value == "internal":
            yield {"class2": {"__config__": {"validate_all": True}}}
        else:
            yield value



schema = CombinedSchema(class1=Class1(flag="internal"), class2=Class2(data1="abc", data2="xyz"))
# Valid, no validation for Class2 fields

schema = CombinedSchema(class1=Class1(flag="external"), class2=Class2(data1="123", data2="invalid"))  # Validation error for data2




import org.apache.arrow.memory.BufferAllocator;
import org.apache.arrow.memory.RootAllocator;
import org.apache.arrow.vector.*; // Import all vector types
import org.apache.arrow.vector.ipc.ArrowFileWriter;
import java.io.ByteArrayOutputStream;
import java.util.ArrayList;
import java.util.List;

public class ArrowSerialization {

  public static byte[] serializeListObjects(List<Object> dataList) throws IOException {
    // Allocate memory
    BufferAllocator allocator = new RootAllocator(Long.MAX_VALUE);

    // Define Field Vectors based on data types in dataList
    List<FieldVector> vectors = new ArrayList<>();
    List<Field> fields = new ArrayList<>();

    for (Object obj : dataList) {
      FieldVector vector = null;
      String fieldName = "field_" + vectors.size(); // Generate unique field names

      if (obj instanceof Integer) {
        vector = new IntVector(fieldName, allocator);
      } else if (obj instanceof Long) {
        vector = new BigIntVector(fieldName, allocator);
      } else if (obj instanceof Float) {
        vector = new Float4Vector(fieldName, allocator);
      } else if (obj instanceof Double) {
        vector = new Float8Vector(fieldName, allocator);
      } else if (obj instanceof String) {
        vector = newVarCharVector(fieldName, allocator);
      } else {
        // Handle other data types or throw an exception
        throw new IllegalArgumentException("Unsupported data type: " + obj.getClass().getName());
      }

      vector.allocateNew();

      // Add elements to the vector based on data type
      if (vector instanceof IntVector) {
        ((IntVector) vector).setSafe(0, (Integer) obj);
      } else if (vector instanceof BigIntVector) {
        ((BigIntVector) vector).setSafe(0, (Long) obj);
      } else if (vector instanceof Float4Vector) {
        ((Float4Vector) vector).setSafe(0, (Float) obj);
      } else if (vector instanceof Float8Vector) {
        ((Float8Vector) vector).setSafe(0, (Double) obj);
      } else if (vector instanceof VarCharVector) {
        ((VarCharVector) vector).setValueLength(0, ((String) obj).getBytes().length);
        ((VarCharVector) vector).setSafe(0, ((String) obj).getBytes());
      }

      vector.close();
      vectors.add(vector);
      fields.add(new Field(fieldName, vector.getField().getFieldType(), null)); // Add field metadata
    }

    // Create VectorSchemaRoot with fields and vectors
    VectorSchemaRoot root = new VectorSchemaRoot(new org.apache.arrow.vector.Schema.Builder().build(fields), vectors);

    // Serialize using ArrowFileWriter
    try (ByteArrayOutputStream bos = new ByteArrayOutputStream();
         ArrowFileWriter writer = new ArrowFileWriter(bos, allocator)) {
      writer.write(root);
      return bos.toByteArray();
    } finally {
      root.close();
      for (FieldVector vector : vectors) {
        vector.close();
      }
      allocator.close();
    }
  }

  // Example usage (assuming data contains a mix of Integer, String, and Double)
  public static void main(String[] args) throws IOException {
    List<Object> dataList = new ArrayList<>();
    dataList.add(10);
    dataList.add("Hello");
    dataList.add(3.14);

    byte[] serializedBytes = serializeListObjects(dataList);

    // Send serializedBytes to the server
  }
}

