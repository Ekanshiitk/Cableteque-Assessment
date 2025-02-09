# Cableteque Assessment

## bicycle_generator.py 
The Bicycle Generator is a Python script that processes an Excel file (.xlsx) containing bicycle specifications and generates all possible bicycle modifications based on the provided data. The output is a JSON file that lists all bicycle configurations.
        The Excel file should have the following sheets:
    	1.	ID – Contains designators that define unique bicycle IDs.
    	2.	GENERAL – Contains common attributes for all bicycles.
    	3.	Other Sheets – Contain attributes specific to certain designators.
    
The script reads the Excel file, combines designators, applies modifications, and produces a JSON-formatted output.

### Working
  1.	The script parses the Excel file and extracts data from different sheets.
  2.	It converts sheet data into dictionaries for easy manipulation.
  3.    The designators in the “ID” sheet are converted into tuples.
  4.    The script then computes the Cartesian product of these tuples to generate all possible unique bicycle IDs.
  5.	Each generated bicycle configuration is enriched with additional specifications from the “GENERAL” sheet and other modification sheets.
  6.	The final result is a structured JSON output containing all possible bicycle variations.

### Usage 
 To generate the configurations, run the on terminal 
	    +------------------------------------------------------------+
	    | python bicycle_generator.py /absolute/path/to/Bicycle.xlsx |
	    +------------------------------------------------------------+

## Automated test 
The automated test is used for verifying the functionality of the Bicycle Generator (bicycle_generator.py). It ensures that the script correctly processes Excel files, generates all possible bicycle configurations, and outputs the expected JSON format.

### What the Test Does
1.	Creates a temporary Excel file with sample data.
2.	Runs the generate_bicycles function from bicycle_generator.py.
3.	Compares the actual output JSON with the expected results.
4.	Deletes the temporary test file after execution.

### Downlaoding dependencies 
 To generate excel files for testing, download
    +------------------------+
    | pip install xlsxwriter |
    +------------------------+

### Running the tests
To execute the tests, run 
    +-----------------------------------------------+
    | python -m unittest test_bicycle_generator.py  |
    +-----------------------------------------------+

If all the tests pass, we shall se an output

   +----------------------------------------------+
   |----------------------------------------------|
   | Ran 1 test in 0.345s                         |
   |                                              |
   | OK                                           |
   +----------------------------------------------+

     If there are errors, unittest will display a detailed report.
