from unittest import TestCase
from your_models_file import YourModel

class TestModelValidators(TestCase):

    def test_validate_data_captain_team_valid(self):
        """Test successful validation of data_captain_team."""
        data = {"package_id": 123, "data_captain_team": "dz-captains-123"}
        model = YourModel(**data)
        assert model.data_captain_team == data["data_captain_team"]

    def test_validate_data_captain_team_invalid_format(self):
        """Test validation error for data_captain_team with incorrect format."""
        data = {"package_id": 123, "data_captain_team": "invalid_format"}
        with self.assertRaises(ValidationError) as excinfo:
            YourModel(**data)
        assert "data_captain_team should be of the format:" in str(excinfo.value)

    def test_validate_data_captain_team_missing_package_id(self):
        """Test validation error for data_captain_team with missing package_id."""
        data = {"data_captain_team": "dz-captains-123"}
        with self.assertRaises(ValidationError) as excinfo:
            YourModel(**data)
        assert "package_id is required" in str(excinfo.value)  # Adapt the message if different

    # Similar tests for other validators (data_marshall_team & data_developer_team)

    def test_validate_data_marshall_team_valid(self):
        # ... (similar structure as the first test)

    def test_validate_data_marshall_team_invalid_format(self):
        # ... (similar structure as the second test)

    def test_validate_data_marshall_team_missing_provider_id(self):
        # ... (similar structure as the third test)

    def test_validate_data_developer_team_valid(self):
        # ... (similar structure as the first test)

    def test_validate_data_developer_team_invalid_format(self):
        # ... (similar structure as the second test)

    def test_validate_data_developer_team_missing_package_id(self):
        # ... (similar structure as the third test)

