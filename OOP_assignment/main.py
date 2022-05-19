import healthcare_prof
import patient
import prescription
import receptionist
import appointment

"""
This is main script to simulate a full functionality cycle
and also an easy way to see how the model works, with explained steps
that will be written in the readme as well
"""

# shorthand to create doctor and nurse objects
doctor = healthcare_prof.doctor
nurse = healthcare_prof.nurse

# initializing the objects
schedule = appointment.appointment_schedule()
doctor1 = doctor("Peter Parker", "1122")
nurse1 = nurse("Mary Jane", "1333")
patient1 = patient.patient("Bruce Wayne", "Wayne Manor", "3451189")
receptionist1 = receptionist.receptionist("Sam David", "4455")

# we start with the patient asking for an appointment
# the appointment does not exist so we'll need the receptionist

# this will print only a string since no appointment is passed
patient1.req_appointment()

# receptionist creates appointment and assigns it to patient and doctor (aggregation)
receptionist1.make_appointment(patient1, None, doctor1)

# --> verify that it is the same memory allocation so the same appointment
print(patient1.appointment, doctor1.appointment)

# assigning the appointment to a variable to handle it better
appointment1 = patient1.appointment

# now we can add the appointment to the schedule
appointment.appointment_schedule.add_app(schedule, appointment1)

# here we can see how the appointment is accessed inside the schedule
# should print the name of our doctor peter parker
print(schedule.appointments[0].staff.name)

# now the receptionists deletes the appointment
# receptionist1.cancel_appointment(schedule, appointment1, patient1, doctor1)
receptionist1.cancel_appointment(patient1, doctor1)
schedule.cancel_app(appointment1)

# should print none , none
# should print 0 to verify that now schedule is empty
print(patient1.appointment, doctor1.appointment)
print(len(schedule.appointments))

# now the scripts to issue a prescription
patient1.req_repeat(doctor1)
doctor1.issue_prescription(
    "antistress caused by too much darkness", patient1, doctor1, "55", "100ml")
# checking that the two objects are actually the same prescription assigned through aggregation
print(patient1.prescription, doctor1.prescription)

# for schedule methods hard coded doctors and staff list are used to better show the functionality
# I'll include a number of busy doctors and a free doctor
doc2 = doctor("John", "4455", "fake appointment")
doc3 = doctor("Jack", "4455", "fake appointment")
doc4 = doctor("Samuel", "4455")
doc5 = doctor("Samantha", "4455", "fake appointment")
staff_list = [doc2, doc3, doc4, doc5]

# this should check in the list since and print samuel is free
schedule.find_next_avail(None, None, staff_list)

# you can also check if for example samantha is free
schedule.find_next_avail(doc5, None, None)
# or nurse Mary Jane
schedule.find_next_avail(None, nurse1, None)
