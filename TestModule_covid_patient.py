import unittest
import hospital.patient.covid_patient as cp
import hospital.patient.patients as p

class TestCovidPatients(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start testing in covid-19 patients.")

    def setUp(self):
        self.p1 = p.GeneralPatient("Emma Jones", 25, "11/23/2020",1.66, 60, ['vomit'])
        self.p3 = cp.CovidPatient("Joe Mason", 43, "12/01/2020", 1.90, 100, "fever")
        
    def test_init(self):
        self.assertEqual(self.p3.name, "Joe Mason")
        self.assertEqual(self.p3.age, 43)
        self.assertEqual(self.p3.date, "12/01/2020")
        self.assertEqual(self.p3.doc_approve, False)
        self.assertEqual(self.p3.weight, 100)
        self.assertEqual(self.p3.height, 1.90)
        self.assertEqual(self.p3.symptom, ['fever'])
        
    def test_display(self):
        self.assertEqual(self.p3.display(), 
                         "Patient name: Joe Mason\nPatient age: 43\nIn hospital date: 12/01/2020\nSymptoms: ['fever']\nTest result: positive")
        self.p3.covid_test = False
        self.assertEqual(self.p3.display(), 
                         "Patient name: Joe Mason\nPatient age: 43\nIn hospital date: 12/01/2020\nSymptoms: ['fever']\nTest result: negative")
        
    def test_bmi(self):
        bmi = 100/1.90**2
        self.assertEqual(self.p3.bmi(), "Patient BMI is {}".format(bmi))
        self.p4 = cp.CovidPatient("Tom Dwan", 29, "11/16/2020",1.82, '72', 'headache')
        self.assertEqual(self.p4.bmi(), "Cannot apply since one or both of weight and height is not a number.")
        
    def test_fullrecovered(self):
        self.assertEqual(self.p3.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.p3.doc_approve = True
        self.p3.covid_test = False
        self.assertEqual(self.p3.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        self.assertEqual(self.p1.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.p1.doc_approve = True
        self.assertEqual(self.p1.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        
    def test_additionsymp(self):
        self.p3.addition_symptom(['back pain', 'headache'])
        self.assertEqual(self.p3.addition_symptom(2), "Please enter a list or string.")
        self.p3.addition_symptom('cough')
        self.assertEqual(self.p3.symptom, ['fever', 'back pain', 'headache', 'cough'])
        
    def test_recoveredsymp(self):
        self.p3.addition_symptom(['back pain', 'headache'])
        self.p3.addition_symptom('cough')
        self.p3.recovered_symptom(['back pain', 'headache', 'cough'])
        self.assertEqual(self.p3.recovered_symptom(2), "Please enter a list or string.")
        self.assertEqual(self.p3.recovered_symptom('headache'), 
                         "Symptom is not in the list, please provide symptoms from existed list.")
        self.assertEqual(self.p3.recovered_symptom('fever'),
                         "This patient has been recorvered already, please check test result.")
        self.assertEqual(self.p3.doc_approve, True)
        self.p1.addition_symptom(['back pain', 'headache'])
        self.p1.addition_symptom('cough')
        self.p1.recovered_symptom(['back pain', 'headache', 'cough'])
        self.assertEqual(self.p1.recovered_symptom(2), "Please enter a list or string.")
        self.assertEqual(self.p1.recovered_symptom('headache'), 
                         "Symptom is not in the list, please provide symptoms from existed list.")
        self.assertEqual(self.p1.recovered_symptom('vomit'),
                         "This patient has been recorvered already, please check condition to leave.")
        self.assertEqual(self.p1.doc_approve, True)
        self.assertEqual(self.p1.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        
    def test_testresult(self):
        self.assertEqual(self.p3.recovered_symptom('fever'),
                         "This patient has been recorvered already, please check test result.")
        self.assertEqual(self.p3.doc_approve, True)
        self.assertEqual(self.p3.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.assertEqual(self.p3.test_result('positive'), "Test not passed")
        self.assertEqual(self.p3.test_result(2), "Please provide valid test input.")
        self.assertEqual(self.p3.test_result('negative'), "Test passed, please check condition to leave.")
        self.assertEqual(self.p3.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        
    def tearDown(self):
        self.p3 = None

    @classmethod
    def tearDownClass(cls):
        print("Finish tests in covid-19 patients.")
