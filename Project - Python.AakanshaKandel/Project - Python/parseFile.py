"""" 
Code is building a data cleaning and data standardization pipeline for employee records that come from messy sources (JSON).
A machine that takes raw, inconsistent employee data and turns it into clean, validated, formatted, standardized employee profiles.
"""

import json
import os

def getJSONContent(file):
    """This reads the json content and returns the data as Python 
    data structures."""

    with open(file, "r", encoding = "utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "employees" in data: 
        return data["employees"]
    return data 


def generateEmail(firstname, lastname): 
    """Generates and formats the email of the employee."""

    firstname = firstname.strip()
    lastname = lastname.strip()
    return firstname[0].lower() + lastname.lower() + "@comp.com"

def generateFormattedFile(empList, ogPath): 
    """Creates a new JSON file to store cleaned employee data
    gets the base name from the original file and adds _formatted.json
    at the end of the name, giving it a new filename"""

    folder = os.path.dirname(ogPath)
    base = os.path.splitext(os.path.basename(ogPath))[0]
    newName = base +"_formatted.json"
    newPath = os.path.join(folder, newName)

    with open(newPath, "w", encoding = "utf-8") as f: 
        json.dump(empList, f, indent = 4)
    
    return newPath

def generateSalary(jobId, state): 
    """Generates the base salaries, formula for manager bonus, 
    high_cost_states and returns the data accordingly """

    base_salaries = {
        "SA": 60000,
        "IT": 80000,
        "HR": 70000,
    }
    #extracting department prefix
    jobId = str(jobId).strip()
    state = str(state).strip().upper()

    dept = jobId.split("_")[0]
    base = base_salaries.get(dept,0)

    manager_bonus = 0 
    if jobId.endswith("_MNG"): 
        manager_bonus = base * 0.05
    
    if state in {"NY", "CA", "OR", 
                        "WA", "VT"}:
        state_bonus = (base + manager_bonus) * 0.015
    else: 
        state_bonus = 0 

    return base + manager_bonus + state_bonus

def validatePhoneNumber(phoneNumber):
    """Validates the phone number to have 10 digits length and 
    returns it as an integer and if the phone number does not meet
    this criteria it returns 1."""

    phoneNumber = str(phoneNumber or "").replace(" ", "" )
    if phoneNumber.isdigit() and len(phoneNumber) == 10:
        return int(phoneNumber)
    elif phoneNumber == "":
        return 1 
    else: 
        return 1

def validateZips(zipCode): 
    """Validates the zipCode to have a length of 5, and returns 
    it as an integer and if the zipCode 
    does not meet this criteria it returns 1."""

    zipCode = str(zipCode or "")
    if zipCode.isdigit() and len(zipCode) == 5:
        return int(zipCode)
    else: 
        return 1

def proper_case(s):
    """This function definies propercase for use in 
    processEachEmp function."""

    return str(s or "").title().strip()

def processEachEmp(empList):
    """Adds each employees to the formatted json, ensuring the 
    phone number, zipcode, first_name, last_name, address, salary and job title 
    are returned in the desired format. If phone number, zipcode invalid, entry will be skipped."""

    processed_employees = []


    for emp in empList: 
        
        #emp = emp.copy()
        phone = validatePhoneNumber(emp.get("Phone Number", "")) 
        zip_code = validateZips(emp.get("Zip Code", ""))

        if phone == 1 or zip_code == 1: 
            continue #skips invalid entries

        emp["Phone Number"] = phone
        emp["Zip Code"] = zip_code


        #Remove Last entry(extra data)
        #emp_keys = list(emp.keys())
        #emp.pop(emp_keys[-1])
        for key in list(emp.keys()): 
            if key.strip() == "I declare that the above information is accurate.": 
                emp.pop(key)

        #formatting the names, and address to captital first letter
        emp["First Name"] = proper_case(emp.get("First Name", ""))
        emp["Last Name"] = proper_case(emp.get("Last Name", ""))
        emp["Address Line 1"] = proper_case(emp.get("Address Line 1", ""))
        emp["Address Line 2"] = proper_case(emp.get("Address Line 2", "" ))
        emp["City"] = proper_case(emp.get("City", ""))
        emp["Job Title"] = proper_case(emp.get("Job Title", ""))

        
        # Adding email 
        emp["Email"] = generateEmail(
            emp["First Name"],
            emp["Last Name"]
        )

        #Add salary 
        emp["Salary"] = generateSalary(
            emp.get("Job ID", ""), 
            emp.get("State", "")
        )
        
        #Add cleaned employee to list 

        processed_employees.append(emp)
  

    return processed_employees


    

