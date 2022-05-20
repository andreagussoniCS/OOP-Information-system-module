# OOP system implementation

This project is developed using modules that are imported in each
script when needed for better understandability.
`prescription and appointment`
Starting from the easiest classes, prescription and appointment don't have any
particular method, they just have the init method to assign them the attributes described in the system design, but they use other objects as attributes, like patient and staff/doctor. Appointment method is then a part of the appointment schedule class through composition in the sense that every appointment is included in the appointments list.
`appointment schedule`
The appointment schedule class in the appointment module operates on its single attribute which is a list containing all the appointments, it has add, delete methods and a find next available. I interpreted the latter in multiple scenarios, to find the first staff available in the default case, using a list of all the staff created in the main file, or it is possible passing in a specific doctor/nurse to check if he/she is available. In the case that nothing is passed a part from the list of appointments it prints out what is the customer's position in the waiting line.
`healthcare professional`
Healthcare professionale is the parent class that has the init method and a consulting method that returns a string.
Doctor class is the first class that inherits from healthcare professional and overwrites the init method to include some attributes required by the aggregation of prescription and appointment. It also has an issue prescription method that creates a prescription object and assigns it to himself and the patient passed to not call patient method again.
Nurse class inherits from the parent class without adding anything.
`patient`
Patient has the init method, that includes appointment and prescription through aggregation and two other methods. Request repeat method asks for a repeat and gets it from doctor class that is the only that can issue one (if it is already provided, otherwise doctor method will assign it). The second method asks for an appointment and if provided it is assigned to patient object through aggregation, otherwise a method in receptionist will assign it or create it.
`receptionist`
Receptionist is initialized with the attributes name and employee number, then it has two methods. The first method assigns an appointment to the passed objects (doctor/nurse, patient) if provided or creates it if not passed in. The second method eliminates an appointment passed as a parameter from the objects indicated when calling the method.
`main`
Main file is used to demonstrate the functionality of the system in an easy way, the file has all the comments to describe what is happening and the results can be seen in the console as evrything is printed out. The approach used aims to comprehend two scenarios, one that an appointment is a separarted entity created outside of other methods but the system works also with the appointments created through the receptionist method and assigned to the respective objects, every attribute set to None makes this possible leaving more freedom for the system user to manage it.
The file demonstrates the most comprehensive cycle with logic in it but others can be performed.
`testing`
For every module there is a test present. I used unittest object orienrted testing features with hard coded data. To run the tests it's possible to just run the single file without any installation.

Throughout the project everything is commented as clearly as possible to show the thought process, the main file is a good way to see it a bit more visualized.
