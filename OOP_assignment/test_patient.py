import unittest
import patient


class TestPatient(unittest.TestCase):

    # test for the initializing method
    def test_init(self):
        obj = patient.patient("name", "address", "phone",
                              "appointment", "prescription")
        print(" testing init method")
        self.assertEqual("name", obj.name)
        print("name ok")
        self.assertEqual("address", obj.address)
        print("addr ok")
        self.assertEqual("phone", obj.phone)
        print("phone ok")
        self.assertEqual("appointment", obj.appointment)
        print("appointment ok")
        self.assertEqual("prescription", obj.prescription)
        print("presc ok")

    # test for the prescription assigning method with dot notation
    def test_req_repeat(self):
        print("testing prescription assigning method")
        obj2 = patient.patient("name", "address", "phone")
        obj2.prescription = "prescription"
        self.assertEqual("prescription", obj2.prescription)

    # test for the appointment assigning method with dot notation
    def test_req_appointment(self):
        print("testing appointment assigning method")
        obj3 = patient.patient("name", "address", "phone")
        obj3.appointment = "appointment"
        self.assertEqual("appointment", obj3.appointment)


if __name__ == '__main__':
    unittest.main()
