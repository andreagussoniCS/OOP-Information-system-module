import unittest
import prescription


class TestPrescription(unittest.TestCase):

    # printing out every stage because of many asserts
    def test_init(self):
        obj = prescription.prescription(
            "type", "patient", "doctor", "quantity", "dosage")
        print("-- testing init method --")
        self.assertEqual("type",  obj.type)
        print("type is ok")
        self.assertEqual("patient",  obj.patient)
        print("patient is ok")
        self.assertEqual("doctor",  obj.doctor)
        print("doctor is ok")
        self.assertEqual("quantity",  obj.quantity)
        print("quantity is ok")
        self.assertEqual("dosage",  obj.dosage)
        print("dosage is okay")


if __name__ == '__main__':
    unittest.main()
