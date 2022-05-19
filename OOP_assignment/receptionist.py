import appointment as ap


class receptionist():

    """
    receptionist class handles the appointments using appointment class and appointment_schedule class
    and makes or deletes appointments from other classes

    """

    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    # nurse and doctor here are set to a default to make them optional in case you need one or the other
    # if appointment is already provided type parameter doesn't matter
    def make_appointment(type, patient, appointment=None, doctor=None, nurse=None):
        if appointment:
            patient.appointment = appointment
            if doctor:
                doctor.appointment = appointment
            if nurse:
                nurse.appointment = appointment
        else:
            if doctor:
                patient.appointment = ap.appointment(type, doctor, patient)
                doctor.appointment = patient.appointment
            if nurse:
                patient.appointment = ap.appointment(type, nurse, patient)
                nurse.appointment = patient.appointment

    # patient doctor and nurse should be objects
    # deleting appointments from doctor and patient
    def cancel_appointment(patient, doctor=None, nurse=None):
        patient.appointment = None
        if doctor:
            doctor.appointment = None
        if nurse:
            nurse.appointment = None
