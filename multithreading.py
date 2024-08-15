
import os
import threading
import concurrent.futures
import time

class Class:
    def func(id):
        #some logic
        
def function(thread_id, obj):
    # Set a different environment variable for each thread
    
    # Call the fetch method
    obj.func(thread_id)

def main():
    number_of_threads = 5
    obj = Class()

    # Use ThreadPoolExecutor to manage the threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        # Submit tasks to the executor for each thread
        futures = [executor.submit(function, i, obj) for i in range(number_of_threads)]
        
        # Wait for all threads to complete
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
