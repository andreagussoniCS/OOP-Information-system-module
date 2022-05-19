class prescription():

    """
    prescription class initializing, only doctor class can call this method
    """

    def __init__(self, type, patient, doctor, quantity, dosage):
        self.type = type
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage
