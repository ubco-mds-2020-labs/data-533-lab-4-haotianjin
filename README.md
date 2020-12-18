# ubc-mds-data533

## Package name: hospital

[![Build Status](https://travis-ci.com/haotianjin/ubco-mds-data533-lab4-group.svg?token=2Spxnw3MTzR9CEHNUBzV&branch=main)](https://travis-ci.com/haotianjin/ubco-mds-data533-lab4-group)

https://pypi.org/project/HospitalManagement/0.1/

- Manage employees and patients in the hospital.

- Sub-package 1: employee: manage nurses and doctors
  - doctor `\hospital.employee.doctor.Doctor(name, age, phone_num, salary, number_treated)`
    - `display()`: display all information about the doctor.
    - `change_in_phone_num(phone_num=str)`: change the doctor’s phone number into imported number.
    - `change_in_salary(salary=int or float)`: change the doctor’s salary into imported number.
    - `bonus()`: print out the bonus amount based on number of patients treated and print the total salary.
  - nurse `\hospital.employee.nurse.Nurse(name, age, phone_num, salary, number_treated)`
    - `display()`: display all information about the nurse.
    - `change_in_phone_num(phone_num=str)`: change the nurse’s phone number into imported number.
    - `change_in_salary(salary=int or float)`: change the nurse’s salary into imported number.
    - `bonus()`: print out the bonus amount based on number of patients treated and print the total salary.

- Sub-package 2: patient: manage general patients and COVID-19 patients
  - patients `\hospital.patient.patients.GeneralPatient(name, age, doc_approve=False, data, symptom_list)`
    - `display()`: display all patient's information
    - `bmi()`: calculate and display patient's bmi by deviding weight by squared height.
    - `full_recovered()`: print the result that if the patient is able to leave the hospital.
    - `addition_symptom(new_symptoms=list or str)`: append imported list or string of symptoms into symptom list and warn the user if the input value is not list or string.
    - `recovered_symptom(rec_symptoms=list or str)`: delete imported list or string of symptoms from symptom list (warning if not exist). And this function will also remind the user if patient does not have any symptoms and change doctor approve status from False to True. 
  - covid_patient `\hospital.patient.covid_patient.CovidPatient(inherit args from GeneralPatient, cov_result=True)`
    - `display()`: inherit from GeneralPatient, display all patient's information. In addition, print out covid test result.
    - `bmi()`: inherit from GeneralPatient, calculate and display patient's bmi by deviding weight by squared height.
    - `full_recovered()`: print the result that if the patient is able to leave the hospital.
    - `addition_symptom(new_symp=list or str)`: inherit from GeneralPatient, append imported list or string of symptoms into symptom list and warn the user if the input value is not list or string.
    - `recovered_symptom(rec_symptoms)`: delete imported list or string of symptoms from symptom list (warning if not exist). And this function will also remind the user if patient does not have any symptoms (change doctor approve status from False to True and recommand user to do covid test for the patient). 
    - `test_result(test)`: print out new test result, and will change cov_result=False if test shows negative.
