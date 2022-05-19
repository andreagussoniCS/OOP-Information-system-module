import receptionist
import unittest
import appointment as ap
import healthcare_prof as hp
import patient

schedule = ap.appointment_schedule()

pat = patient.patient("name", "address", "phone", None)

doc = hp.doctor("name", "3333", None)

app = ap.appointment("type", doc, pat)

ap.appointment_schedule.add_app(schedule, app)


class test_receptionist(unittest.TestCase):

    def test_init(self):
        obj = receptionist.receptionist("jack", "3356747")
        self.assertEqual("jack", obj.name)
        self.assertEqual("3356747", obj.employee_number)

    # checking if receptionist creates appointment
    def test_make_appointment(self):
        receptionist.receptionist.make_appointment("type", pat, app, doc)
        self.assertEqual(app, doc.appointment)
        self.assertEqual(app, pat.appointment)
        # checking if receptionist creates appointment otherwise
        receptionist.receptionist.make_appointment("type", pat, None, doc)
        self.assertEqual(pat.appointment, doc.appointment)

    # creating an appointment and then deleting it
    def test_cancel_appointment(self):
        receptionist.receptionist.make_appointment("appointment", pat, doc)
        receptionist.receptionist.cancel_appointment(pat, doc)
        self.assertEqual(None, pat.appointment)
        self.assertEqual(None, doc.appointment)


if __name__ == '__main__':
    unittest.main()
