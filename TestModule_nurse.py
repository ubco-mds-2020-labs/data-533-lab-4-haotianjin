import unittest
import hospital.employee.nurse as n

class TestNurse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing nurse')
    
    def setUp(self):
        self.n1 = n.Nurse('Tess',18,"5436890982",3200,25)
        self.n2 = n.Nurse('Melissa',40,"8920953924",9000,5)

    def test_init(self):
        self.assertEqual(self.n1.name,"Tess")
        self.assertEqual(self.n1.age,18)
        self.assertEqual(self.n1.phone_num,"5436890982")
        self.assertEqual(self.n1.salary,3200)
        self.assertEqual(self.n1.number_treated,25)

    def test_display(self):
        self.assertEqual(self.n1.display(),"Nurse {} is {} years old. \nThe best number to reach out is {}. \nThe nurse's salary is {}. \nThe nurse has treated {} patients.\n".format('Tess',18,"5436890982",3200,25))

    def test_change_in_phone_num(self):
        self.n1.change_in_phone_num("1234567890")
        self.n2.change_in_phone_num("0987654321")
        self.assertEqual(self.n1.phone_num,"1234567890")
        self.assertEqual(self.n2.phone_num,"0987654321")
        self.n1.change_in_phone_num("3254678313")
        self.n2.change_in_phone_num("0928495820")
        self.assertEqual(self.n1.phone_num,"3254678313")
        self.assertEqual(self.n2.phone_num,"0928495820")

    def test_change_in_salary(self):
        self.n1.change_in_salary(9000)
        self.n2.change_in_salary(10000)
        self.assertEqual(self.n1.salary,9000)
        self.assertEqual(self.n1.change_in_salary(-50),"Invalid salary.")
        self.assertEqual(self.n2.salary,10000)
        self.n1.change_in_salary(20)
        self.assertEqual(self.n1.salary,20)

    def test_bonus(self):
        self.n1.bonus()
        self.n2.bonus()
        self.assertEqual(self.n1.salary,3450)
        self.assertEqual(self.n2.salary,9050)
        

    def tearDown(self):
        self.n1 = None
        self.n2 = None
    
    @classmethod
    def tearDownClass(cls):
        print("Finish test nurse")

unittest.main(argv=[''], verbosity=2, exit=False)
