# Python_Project
# Python File Processing and Data Transformation

## Project Overview

This project involved developing a Python-based ETL application to automate the processing and transformation of employee data stored in JSON files.

The program was designed to locate raw JSON files, validate employee records, clean and standardise information, perform data transformations and generate new formatted JSON files. It also handled invalid records to ensure the output contained properly structured data.

## Project Structure and Workflow

### 1. main.py – Main Program

This file served as the entry point for the application, coordinating the different stages of the ETL workflow.

- Called the modules responsible for locating and processing files.
- Managed the overall execution of the application.
- Reported the number of files processed and valid employee records.

### 2. usrInput.py – File Discovery and Input Validation

This module handled the extraction stage of the process.

- Accepted and validated user-provided file or directory paths.
- Searched directories and subdirectories for raw JSON files.
- Identified files that needed to be processed.
- Passed the relevant file paths to the transformation module.

### 3. parseFile.py – Data Validation and Transformation

This module was responsible for processing the employee records.

- Read and parsed the raw JSON data.
- Validated employee records and skipped invalid entries.
- Standardised employee names and addresses.
- Generated employee email addresses.
- Performed salary calculations.
- Created new JSON files containing the transformed records, using the `_formatted.json` filename suffix.

## Project Outcome

The project automated a previously manual data-processing workflow by combining file discovery, validation, transformation and output generation into a single Python application.

It strengthened my understanding of modular Python programming, JSON data handling, data validation, error handling and ETL principles.

**Technologies Used:** Python, JSON, File Handling, Data Validation, ETL.
