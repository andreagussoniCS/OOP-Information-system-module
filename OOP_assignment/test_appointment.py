import unittest
import appointment as ap
import healthcare_prof as hp

doc1 = hp.doctor("jack", "3333", "appointment")
doc2 = hp.doctor("jhon", "4444")

schedule = ap.appointment_schedule()

# list for testing last method
staffl = [doc1, doc2]


class test_appointment(unittest.TestCase):

    def test_init(self):
        obj = ap.appointment("type", "staff", "patient")
        self.assertEqual("type", obj.type)
        self.assertEqual("staff", obj.staff)
        self.assertEqual("patient", obj.patient)
        print("Init ok")
        print("------")

    def test_add_cancel(self):
        obj = ap.appointment("type", "staff", "patient")
        ap.appointment_schedule.add_app(schedule, obj)
        print("------")
        print("add is ok")
        print("------")
        ap.appointment_schedule.cancel_app(schedule, obj)
        print("cancel is ok")

    def test_find_next(self):
        obj = ap.appointment("type", "staff", "patient")
        # testing list part of method
        print("------")
        ap.appointment_schedule.find_next_avail(
            schedule, doc1, None, staffl)  # should print jhon is free
        print("------")
        # testing specific doctor method
        # should print Dr. Jack is not available
        ap.appointment_schedule.find_next_avail(schedule, doc1)
        print("------")
        # testing schedule only
        ap.appointment_schedule.add_app(schedule, obj)
        print("------")
        # should print you are number 2 on the list
        ap.appointment_schedule.find_next_avail(schedule)


if __name__ == '__main__':
    unittest.main()
