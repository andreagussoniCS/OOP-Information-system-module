import healthcare_prof
import unittest
import prescription
import patient

# pre initialized objects used for testing
pat = patient.patient("name", "address", "phone",
                              "appointment", "prescription")

presc = prescription.prescription(
    "type", "patient", "doctor", "quantity", "dosage")


class testHealthcare(unittest.TestCase):

    # default init method testing valid for both doctor and nurse
    def test_init(self):
        obj = healthcare_prof.healthcare_professional("name", "3333")
        print("testing init method")
        self.assertEqual("name", obj.name)
        self.assertEqual("3333", obj.employee_number)

    # testing doctor specific method
    def test_doctor(self):
        obj = healthcare_prof.doctor(
            "name", "4444")

        obj.issue_prescription(
            "type", pat, "doctor", "quantity", "dosage")
        print(obj.prescription)
        self.assertEqual("type", obj.prescription.type)

    # test if method works with provided object
    def test_doctor_presc(self):
        obj = healthcare_prof.doctor(
            "name", "4444", None, presc)

        self.assertEqual("type", obj.prescription.type)


if __name__ == '__main__':
    unittest.main()
