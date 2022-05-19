class appointment():

    """
    class used only to create an appointment, in order to 
    make the appointment unique use
    staff and patient objects as parameters when creating 
    an appointment
    """

    def __init__(self, type, staff, patient):
        self.type = type
        self.staff = staff
        self.patient = patient


class appointment_schedule():

    # initializing a schedule instance is needed or positional argument error will raise
    # schedule should be only one, appointments is initialized as list
    def __init__(self, appointments=[]):
        self.appointments = appointments

    # method to add provided appointment
    def add_app(self, appointment):
        self.appointments.append(appointment)

    # simple method to del an appointment from schedule
    def cancel_app(self, appointment):
        self.appointments.remove(appointment)

    def find_next_avail(self, doctor=None, nurse=None, staff_list=None):

        # default behaviour, iterate through staff list created in main to check if anyone is free
        # if user needs to check a particular staff just input that staff
        if staff_list:
            for staff in staff_list:
                if staff.appointment == None:
                    print(f"{staff.name} is free")
                    return

        # special cases
        if doctor and nurse:
            print("choose only one staff")
            return

        # this checks if a doctor object is provided and checks if he/she is free
        if not nurse and doctor:
            if doctor.appointment == None:
                print(f"Dr. {doctor.name} is free")
                print("------")
                return
            else:
                print(f"Dr. {doctor.name} is not available")
                return

        if not doctor and nurse:
            if nurse.appointment == None:
                print(f"Nurse {nurse.name} is free")
                print("------")
                return
            else:
                print(f"Nurse {nurse.name} is not available")
                return

    # if no doctor or nurse is passed this finds when patient appointment could be,
    # given that there is no date attribute
        i = 0
        for app in self.appointments:
            i += 1

        print(f"you are number {i+1} on the waiting list")
