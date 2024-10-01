import unittest
import app

class TestApp(unittest.TestCase):

    def test_true_when_x_is_17(self):
        response = app.prime(17)
        self.assertEqual(response, "true")

    def test_false_when_x_is_36(self):
        response = app.prime(36)
        self.assertEqual(response, "false")

    def test_true_when_x_is_13219(self):
        response = app.prime(13219)
        self.assertEqual(response, "true")

    def test_hello_simple_api(self):
        response = app.hello("simple api")
        self.assertEqual(response, "Hello simple api")

    def test_hello_123(self):
        response = app.hello("123")
        self.assertEqual(response, "Hello 123") 

    def test_minus_1_2(self):
        response = app.minus(1, 2)
        self.assertEqual(response, "-1") 
    
    def test_avg_4_5(self):
        response = app.avg(4, 5)
        self.assertEqual(response,"4.5")
    def test_power_2_0(self):
        response = app.power(2,0)
        self.assertEqual(response,"1")
    def test_power_3_2(self):
        response = app.power(3,2)
        self.assertEqual(response,"9")
    def test_power_2_n2(self):
        response = app.power(2,-2)
        self.assertEqual(response,"0.25")
    def test_multiply_5_5(self):
        response = app.multiply(5,5)
        self.assertEqual(response,"25")
    def test_multiply_2_9(self):
        response = app.multiply(2,9)
        self.assertEqual(response,"18")


if __name__ == "__main__":
    unittest.main()