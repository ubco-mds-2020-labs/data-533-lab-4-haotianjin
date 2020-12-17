import unittest
import hospital.employee.doctor as d

class TestDoctor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing doctor')
    
    def setUp(self):
        self.d1 = d.Doctor('Alex',23,"3132334567",3200,25)
        self.d2 = d.Doctor('Andrew',40,"6547381029",9000,5)
    
    def test_init(self):
        self.assertEqual(self.d1.name,"Alex")
        self.assertEqual(self.d1.age,23)
        self.assertEqual(self.d1.phone_num,"3132334567")
        self.assertEqual(self.d1.salary,3200)
        self.assertEqual(self.d1.number_treated,25)

    def test_display(self):
        self.assertEqual(self.d1.display(),"Dr.{} is {} years old. The best number to reach out is {}. \nThe doctor's base salary is {}. \nThe doctor has treated {} patients.\n".format("Alex",23,"3132334567",3200,25))
    
    def test_change_in_phone_num(self):
        self.d1.change_in_phone_num("1234567890")
        self.d2.change_in_phone_num("0987654321")
        self.assertEqual(self.d1.phone_num,"1234567890")
        self.assertEqual(self.d2.phone_num,"0987654321")
        self.d1.change_in_phone_num("3132334567")
        self.d2.change_in_phone_num("6547381029")
        self.assertEqual(self.d1.phone_num,"3132334567")
        self.assertEqual(self.d2.phone_num,"6547381029")

    def test_change_in_salary(self):
        self.d1.change_in_salary(9000)
        self.d2.change_in_salary(10000)
        self.assertEqual(self.d1.salary,9000)
        self.assertEqual(self.d2.salary,10000)
        self.assertEqual(self.d1.change_in_salary(-50),"Invalid salary.")
        self.d1.change_in_salary(80)
        self.d2.change_in_salary(100)
        self.assertEqual(self.d1.salary,80)
        self.assertEqual(self.d2.salary,100)

    def test_bonus(self):
        self.d1.bonus()
        self.d2.bonus()
        self.assertEqual(self.d1.salary,3700)
        self.assertEqual(self.d2.salary,9100)
    
    def tearDown(self):
        self.d1 = None
        self.d2 = None
    
    @classmethod
    def tearDownClass(cls):
        print("Finish test doctor")

unittest.main(argv=[''], verbosity=2, exit=False)
