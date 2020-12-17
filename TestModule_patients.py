import unittest
import hospital.patient.patients as p
class TestPatients(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start testing in general patients.")

    def setUp(self):
        self.p1 = p.GeneralPatient("Emma Jones", 25, "11/23/2020",1.66, 60, ['vomit'])

    def test_init(self):
        self.assertEqual(self.p1.name, "Emma Jones")
        self.assertEqual(self.p1.age, 25)
        self.assertEqual(self.p1.date, "11/23/2020")
        self.assertEqual(self.p1.doc_approve, False)
        self.assertEqual(self.p1.weight, 60)
        self.assertEqual(self.p1.height, 1.66)
        self.assertEqual(self.p1.symptom, ['vomit'])
    
    def test_display(self):
        self.assertEqual(self.p1.display(), 
                         "Patient name: Emma Jones\nPatient age: 25\nIn hospital date: 11/23/2020\nSymptoms: ['vomit']")
    
    def test_bmi(self):
        bmi = 60/1.66**2
        self.assertEqual(self.p1.bmi(), "Patient BMI is {}".format(bmi))
        self.p2 = p.GeneralPatient("Tom Dwan", 29, "11/16/2020",1.82, '72', 'headache')
        self.assertEqual(self.p2.bmi(), "Cannot apply since one or both of weight and height is not a number.")
        
    def test_fullrecovered(self):
        self.assertEqual(self.p1.full_recovered(), "No, this patient is not ready to leave the hospital.")
        self.p1.doc_approve = True
        self.assertEqual(self.p1.full_recovered(), "Yes, this patient is ready to leave the hospital.")
        
    def test_additionsymp(self):
        self.p1.addition_symptom(['back pain', 'headache'])
        self.assertEqual(self.p1.addition_symptom(2), "Please enter a list or string.")
        self.p1.addition_symptom('cough')
        self.assertEqual(self.p1.symptom, ['vomit', 'back pain', 'headache', 'cough'])
        
    def test_recoveredsymp(self):
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
        
    def tearDown(self):
        self.p1 = None

    @classmethod
    def tearDownClass(cls):
        print("Finish tests in general patients.")

