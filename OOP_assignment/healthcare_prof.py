import prescription


class healthcare_professional():

    """
    parent class for nurse and doctor classes, 
    initializing and consulting method to inherit
    """

    def __init__(self, name, employee_number, appointment=None):
        self.name = name
        self.employee_number = employee_number
        self.appointment = appointment

    def consultation(self, patient):

        print(f"{healthcare_professional.name} visited {patient.name}")
        print("------")


class doctor(healthcare_professional):

    """
    Health care professional child class that adds methods to the class.
    doctors can issue prescription using prescription class through aggregation
    """

    # init method overwriting to implement aggregation
    def __init__(self, name, employee_number, appointment=None, prescription=None):
        self.name = name
        self.employee_number = employee_number
        self.appointment = appointment
        self.prescription = prescription

    # method used to create prescription object from doctor class
    # (if existing prescription is not passed in the init method)

    def issue_prescription(self, type, patient, doctor, quantity, dosage):
        self.prescription = prescription.prescription(
            type, patient, doctor, quantity, dosage)
        patient.prescription = self.prescription
        print(
            f"prescription created by {self.name} for {self.prescription.patient.name}")
        print("------")


class nurse(healthcare_professional):
    # no methods or attributes
    pass
