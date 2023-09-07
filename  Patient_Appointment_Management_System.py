# Import necessary libraries
def draw_script_name():
    print("      _  _              _                 _       _   _   _   _   _   _   _ ")
    print("   |_||_| _ _    | |   _  _  (_) __  | |_| |_| |_| |_| |_| |_| |_ ")
    print("  / _`⠟⠟⠺'_| \\ V / | '_ \\/ _` |/ -_) | |/ _| |  _|  _|  _|  _|  _|  _|  _|")
    print("  \\__,_||_||_|    \\_/  |_.__/\\__,_|\\___| |_||___|  \\__| \\__| \\__| \\__| \\__| \\__|")

# Call the function to draw the script name
draw_script_name()
print(' ')
print('created by Trapzzy')
print ('==============================')
import datetime

# Create a class to represent patients
class Patient:
    def __init__(self, name, dob, phone):
        self.name = name
        self.dob = dob
        self.phone = phone

# Create a class to represent appointments
class Appointment:
    def __init__(self, patient, date, time, status):
        self.patient = patient
        self.date = date
        self.time = time
        self.status = status

# Create a class to manage appointments
class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def list_appointments(self):
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient.name}")
            print(f"Date: {appointment.date}")
            print(f"Time: {appointment.time}")
            print(f"Status: {appointment.status}")
            print("-------------------------")

# Function to update appointment details
def update_appointment(manager, appointment_id):
    for appointment in manager.appointments:
        if appointment.id == appointment_id:
            print("Current appointment details:")
            print(f"Patient: {appointment.patient.name}")
            print(f"Date: {appointment.date}")
            print(f"Time: {appointment.time}")
            print(f"Status: {appointment.status}")

            print("Enter new details (leave empty to keep current value):")
            name = input(f"Enter new patient's name [{appointment.patient.name}]: ") or appointment.patient.name
            dob = input(f"Enter new patient's date of birth [{appointment.patient.dob}]: ") or appointment.patient.dob
            phone = input(f"Enter new patient's phone number [{appointment.patient.phone}]: ") or appointment.patient.phone
            date = input(f"Enter new appointment date [{appointment.date}]: ") or appointment.date
            time = input(f"Enter new appointment time [{appointment.time}]: ") or appointment.time
            status = input(f"Enter new status [{appointment.status}]: ") or appointment.status

            appointment.patient.name = name
            appointment.patient.dob = dob
            appointment.patient.phone = phone
            appointment.date = date
            appointment.time = time
            appointment.status = status

            print("Appointment updated successfully.")
            return
    print(f"No appointment found with ID {appointment_id}.")

# Function to cancel an appointment
def cancel_appointment(manager, appointment_id):
    for appointment in manager.appointments:
        if appointment.id == appointment_id:
            print(f"Cancelling appointment with ID {appointment_id}:")
            print(f"Patient: {appointment.patient.name}")
            print(f"Date: {appointment.date}")
            print(f"Time: {appointment.time}")
            print(f"Status: {appointment.status}")
            manager.appointments.remove(appointment)
            print("Appointment cancelled successfully.")
            return
    print(f"No appointment found with ID {appointment_id}.")

# Function to save appointment data to a file
def save_appointment_data(manager, filename):
    try:
        with open(filename, 'w') as file:
            for appointment in manager.appointments:
                file.write(f"{appointment.patient.name},{appointment.patient.dob},{appointment.patient.phone},"
                           f"{appointment.date},{appointment.time},{appointment.status}\n")
        print("Appointment data saved to", filename)
    except Exception as e:
        print("Error saving appointment data:", str(e))

# Function to handle conflicts when scheduling or updating appointments
def handle_conflicts(manager, appointment):
    conflicts = [appt for appt in manager.appointments if appt.date == appointment.date and appt.time == appointment.time]
    return conflicts

# Main function to interact with the program
def main():
    manager = AppointmentManager()
    appointment_id_counter = 1

    while True:
        print("\nOptions:")
        print("1. Schedule Appointment")
        print("2. List Appointments")
        print("3. Update Appointment")
        print("4. Cancel Appointment")
        print("5. Save Appointment Data to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            dob = input("Enter patient's date of birth (YYYY-MM-DD): ")
            phone = input("Enter patient's phone number: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time: ")
            status = "Scheduled"

            appointment = Appointment(Patient(name, dob, phone), date, time, status)
            conflicts = handle_conflicts(manager, appointment)

            if not conflicts:
                appointment.id = appointment_id_counter
                appointment_id_counter += 1
                manager.add_appointment(appointment)
                print("Appointment scheduled successfully.")
            else:
                print("Scheduling conflict detected! Cannot schedule.")

        elif choice == '2':
            manager.list_appointments()

        elif choice == '3':
            appointment_id = int(input("Enter the appointment ID to update: "))
            update_appointment(manager, appointment_id)

        elif choice == '4':
            appointment_id = int(input("Enter the appointment ID to cancel: "))
            cancel_appointment(manager, appointment_id)

        elif choice == '5':
            filename = input("Enter the filename to save appointment data: ")
            save_appointment_data(manager, filename)

        elif choice == '6':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()