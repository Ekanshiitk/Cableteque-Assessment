import unittest
import pandas as pd
import json
import tempfile
import os
from bicycle_generator import generate_bicycles 

class TestBicycleGenerator(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        writer = pd.ExcelWriter(self.test_file.name, engine='xlsxwriter')

        id_data = pd.DataFrame({
            "Type": ["CITY", "MOUNTAIN"],
            "Wheels": [26, 27]
        })
        id_data.to_excel(writer, sheet_name="ID", index=False)

        general_data = pd.DataFrame([{
            "Manufacturer": "Bikes INC",
            "Brake warranty": "2 years",
            "Has suspension": False,
            "Logo": True
        }])
        general_data.to_excel(writer, sheet_name="GENERAL", index=False)

        wheels_data = pd.DataFrame({
            "Wheels": [26, 27],
            "Suspension travel": ["Not applicable", "80 mm"]
        })
        wheels_data.to_excel(writer, sheet_name="Wheels", index=False)

        writer.close()
        self.test_file.close()

    def test_generate_bicycles(self):
        output_json = generate_bicycles(self.test_file.name)
        bicycles = json.loads(output_json) 

        expected_output = [
            {
                "ID": "CITY26",
                "Manufacturer": "Bikes INC",
                "Brake warranty": "2 years",
                "Has suspension": False,
                "Logo": True,
                "Suspension travel": "Not applicable"
            },
            {
                "ID": "CITY27",
                "Manufacturer": "Bikes INC",
                "Brake warranty": "2 years",
                "Has suspension": False,
                "Logo": True,
                "Suspension travel": "80 mm"
            },
            {
                "ID": "MOUNTAIN26",
                "Manufacturer": "Bikes INC",
                "Brake warranty": "2 years",
                "Has suspension": False,
                "Logo": True,
                "Suspension travel": "Not applicable"
            },
            {
                "ID": "MOUNTAIN27",
                "Manufacturer": "Bikes INC",
                "Brake warranty": "2 years",
                "Has suspension": False,
                "Logo": True,
                "Suspension travel": "80 mm"
            }
        ]

        self.assertEqual(bicycles, expected_output)

    def tearDown(self):
        os.remove(self.test_file.name)

if __name__ == "__main__":
    unittest.main()