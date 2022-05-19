import appointment as ap


class patient():

    """
    patient class, initialized with name address and phone attributes
    request methods don't actually produce appointments or prescriptions 
    because that's limited to doctor and receptionist classes
    """

    # aggregation with prescription class
    # prescription starts as none when creating patient object since
    # patient can't issue himself a prescription, instead you should call doctor method
    # then pass it with patient method, same as appointment
    def __init__(self, name, address, phone, appointment=None, prescription=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.appointment = appointment
        self.prescription = prescription

    # here the doctor needs to issue a prescription before the patient can get it
    # the method can be called anyway but the prescription will be set to none again since doctor
    # default prescription value is None
    def req_repeat(self, doctor):
        print(f"I need a medicine Doctor {doctor.name}")
        self.prescription = doctor.prescription
        print("------")

    # assigning appointment to patient using aggregration (appointment needs to be initialized before)
    def req_appointment(self, appointment=None):
        print(f"Good morning, I don't feel good, could I book an appointment?")
        if appointment:
            self.appointment = appointment
            return
        print("------")
