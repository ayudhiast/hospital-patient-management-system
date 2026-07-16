# ==========================================
# HOSPITAL PATIENT MANAGEMENT SYSTEM
# ==========================================

# Dummy Database
patients = [
    {
        "patient_id":"P001",
        "patient_name":"Arya Saputra",
        "age":28,
        "gender":"Male",
        "diagnosis":"Diabetes",
        "insurance":"BPJS",
        "admission_status":"Outpatient"
    },
    {
        "patient_id":"P002",
        "patient_name":"Budi Santoso",
        "age":45,
        "gender":"Male",
        "diagnosis":"Hypertension",
        "insurance":"Private",
        "admission_status":"Inpatient"
    },
    {
        "patient_id":"P003",
        "patient_name":"Cindy Wijaya",
        "age":35,
        "gender":"Female",
        "diagnosis":"Asthma",
        "insurance":"BPJS",
        "admission_status":"Outpatient"
    },
    {
        "patient_id":"P004",
        "patient_name":"Dina Pratiwi",
        "age":52,
        "gender":"Female",
        "diagnosis":"Pneumonia",
        "insurance":"Uninsured",
        "admission_status":"Inpatient"
    },
    {
        "patient_id":"P005",
        "patient_name":"Eko Nugroho",
        "age":31,
        "gender":"Male",
        "diagnosis":"Dengue Fever",
        "insurance":"BPJS",
        "admission_status":"Inpatient"
    },
    {
        "patient_id":"P006",
        "patient_name":"Farah Aulia",
        "age":26,
        "gender":"Female",
        "diagnosis":"Migraine",
        "insurance":"Private",
        "admission_status":"Outpatient"
    },
    {
        "patient_id":"P007",
        "patient_name":"Gilang Ramadhan",
        "age":63,
        "gender":"Male",
        "diagnosis":"Heart Disease",
        "insurance":"Private",
        "admission_status":"Inpatient"
    },
    {
        "patient_id":"P008",
        "patient_name":"Hana Putri",
        "age":19,
        "gender":"Female",
        "diagnosis":"Gastritis",
        "insurance":"BPJS",
        "admission_status":"Outpatient"
    },
    {
        "patient_id":"P009",
        "patient_name":"Ivan Kurniawan",
        "age":41,
        "gender":"Male",
        "diagnosis":"Kidney Stone",
        "insurance":"Uninsured",
        "admission_status":"Inpatient"
    }
]

def display_header():
    print("=" * 100)
    print(
        f"{'ID':<8}"
        f"{'NAME':<20}"
        f"{'AGE':<8}"
        f"{'GENDER':<10}"
        f"{'DIAGNOSIS':<20}"
        f"{'INSURANCE':<15}"
        f"{'STATUS':<15}"
    )
    
    print("=" * 100)

def display_patient(patient):
    print(
        f"{patient['patient_id']:<8}"
        f"{patient['patient_name']:<20}"
        f"{patient['age']:<8}"
        f"{patient['gender']:<10}"
        f"{patient['diagnosis']:<20}"
        f"{patient['insurance']:<15}"
        f"{patient['admission_status']:<15}"
    )


def find_patient(patient_id):
    for patient in patients:
        if patient['patient_id'] == patient_id:
            return patient
    return None

def validate_patient_id(patient_id):
    if len(patient_id) != 4:
        return False
    if patient_id[0] != 'P':
        return False
    if not patient_id[1:].isdigit():
        return False
    return True

# Main Menu
def main_menu():
    print("=" * 45)
    print("Hospital Patient Management Systems")
    print("=" * 45)

    print("1. Read Patient Data")
    print("2. Add New Patient")
    print("3. Update Patient Data")
    print("4. Delete Patient Data")
    print("5. Statistics")
    print("6. Exit")

    print("=" * 45)

    menu = input("Choose Menu: ")

    return menu

# Read Function
def read_patient():
    while True:
        print("=" * 45)
        print("Read Patient Data")
        print("=" * 45)

        print("1. Display All Patients")
        print("2. Search Patient by ID")
        print("3. Search Patient by Diagnosis")
        print("4. Search Patient by Insurance")
        print("5. Back to Main Menu")

        print("=" * 45)

        menu = input("Choose Menu: ")

        if menu == "1":
            if len(patients) == 0:
                print("No patient data available.")

            else:
                print("\nLIST OF PATIENT DATA")
                display_header()
                for patient in patients:
                    display_patient(patient)
                print("-" * 100)

        elif menu == "2":
            patient_id = input("Enter Patient ID: ").upper()
            patient = find_patient(patient_id)
            if patient:
                print("\nPATIENT DATA")
                display_header()
                display_patient(patient)
                print("-" * 100)
            else:
                print("Patient Not Found")

        elif menu == "3":
            diagnosis = input("Input Diagnosis: ").title()
            found = False
            print("\nPATIENT DATA")
            display_header()
            for patient in patients:
                if patient['diagnosis'] == diagnosis:
                    display_patient(patient)
                    found = True
            if not found:
                print("Patient Not Found.")
            print("-" * 100)

        elif menu == "4":
            insurance = input("Input Insurance: ").title()
            found = False
            print("\nPATIENT DATA")
            display_header()
            for patient in patients:
                if patient['insurance'] == insurance:
                    display_patient(patient)
                    found = True
            if not found:
                print("Patient Not Found.")
            print("-" * 100)

        elif menu == "5":
            break

        else:
            print("Invalid Menu")

# Create Function
def create_patient():
    while True:
        print("=" *45)
        print("ADD NEW PATIENT")
        print("=" *45)

        print("1. Create Patient Data")
        print("2. Back to Main Menu")
        
        choice = input("Choose Menu: ")
        
        if choice == "1":
            # Input Patient ID
            patient_id = input("Enter Patient ID (e.g. P001): ").upper()
            if not validate_patient_id(patient_id):
                print("Invalid Patient ID Format!")
                continue

            if find_patient(patient_id):
                print("Patient ID already exists!")
                continue

            # Input Patient Name
            while True:
                patient_name = input("Enter Patient Name: ").title()
                if patient_name != "":
                    break
                print("Patient Name cannot be empty!")

            # Input Age
            while True:
                age = input("Input Age: ")
                if age.isdigit() and int(age) > 0:
                    age = int(age)
                    break
                else:
                    print("Age must be a number!")

            # Input Gender
            while True:
                gender = input("Input Gender (Male/Female): ").title()
                if gender in ["Male", "Female"]:
                    break
                else:
                    print("Input only Male or Female!")

            # Input Diagnosis
            diagnosis = input("Input Diagnosis: ").title()

            # Input Insurance
            while True:
                insurance = input(
                    "Input Insurance (BPJS/Private/Uninsured): ").upper()
                if insurance in ["BPJS", "PRIVATE", "UNINSURED"]:
                    insurance = insurance.title()
                    if insurance == "Bpjs":
                        insurance = "BPJS"
                    break
                else:
                    print("Invalid Insurance Input!")

            # Input Admission Status
            while True:
                admission_status = input(
                    "Input Admission Status (Inpatient/Outpatient): ").title()
                if admission_status in ["Inpatient", "Outpatient"]:
                    break
                else:
                    print("Invalid Admission Status Input!")

            # Confirm save
            save = input("Save Patient Data? (Y/N): ").upper()
            if save == "Y":
                new_patient = {
                    "patient_id": patient_id,
                    "patient_name": patient_name,
                    "age": age,
                    "gender": gender,
                    "diagnosis": diagnosis,
                    "insurance": insurance,
                    "admission_status": admission_status
                }
                patients.append(new_patient)
                print("Patient Data Successfully Saved!")
            else:
                print("Add Patient Data Cancelled!")
            break  
        
        elif choice == "2":
            break
            
        else:
            print("Invalid Menu!")      

# Update Function
def update_patient():
    while True:
        print("=" * 45)
        print("UPDATE PATIENT DATA")
        print("=" * 45)

        print("1. Update Patient Data")
        print("2. Back to Main Menu")
        
        choice = input("Choose Menu: ")
        
        if choice == "1":
            patient_id = input("Input Patient ID: ").upper()
            patient = find_patient(patient_id)
            if not patient:
                print("Patient Not Found!")
                back = input("Back to Update Menu? (Y/N): ").upper()
                if back == "Y":
                    continue
                else:
                    break

            print("\nCURRENTPATIENT DATA")
            display_header()
            display_patient(patient)
            print("-" * 100)

            print("Choose Data to Update:")
            print("1. Patient Name")
            print("2. Age")
            print("3. Gender")
            print("4. Diagnosis")
            print("5. Insurance")
            print("6. Admission Status")
            print("7. Cancel Update")

            choice = input("Choose Menu: ")
            if choice == "1":
                new_value = input("Input New Patient Name: ").title()
                field = "patient_name"
            elif choice == "2":
                while True:
                    age = input("Input New Age: ")
                    if age.isdigit():
                        new_value = int(age)
                        break
                    else:
                        print("Age must be a number!")
                field = "age"
            elif choice == "3":
                while True:
                    gender = input("Input Gender (Male/Female): ").title()
                    if gender in ["Male", "Female"]:
                        new_value = gender
                        break
                    else:
                        print("Invalid Gender!")
                field = "gender"
            elif choice == "4":
                new_value = input("Input New Diagnosis: ").title()
                field = "diagnosis"
            elif choice == "5":
                while True:
                    insurance = input(
                        "Input Insurance (BPJS/Private/Uninsured): ").upper()
                    if insurance in ["BPJS", "PRIVATE", "UNINSURED"]:
                        new_value = insurance.title()
                        if insurance == "Bpjs":
                            insurance = "BPJS"
                        new_value = insurance
                        break
                    else:
                        print("Invalid Insurance Input!")
                field = "insurance"
            elif choice == "6":
                while True:
                    status = input(
                        "Input Admission Status (Inpatient/Outpatient): ").title()
                    if status in ["Inpatient", "Outpatient"]:
                        new_value = status
                        break
                    else:
                        print("Invalid Admission Status Input!")
                field = "admission_status"
            elif choice == "7":
                break
            else:
                print("Invalid Menu!")
                continue
            print()
            print("Current Value: ", patient[field])
            print("New Value: ", new_value)
            if confirm == "Y":
                patient[field] = new_value
                print("Patient Successfully Updated!")
            else:
                print("Update Cancelled!")
            back = input("Back to Update Menu? (Y/N): ").upper()
            if back == "Y":
                continue
            else:
                break
        
        elif choice == "2":
            break
            
        else:
            print("Invalid Menu!")

# Delete Function
def delete_patient():
    while True:
        print("=" * 45)
        print("DELETE PATIENT DATA")
        print("=" * 45)
        
        print("1. Delete Patient by ID")
        print("2. Back to Main Menu")
        
        choice = input("Choose Menu: ")
        
        if choice == "1":
            patient_id = input("Input Patient ID: ").upper()
            patient = find_patient(patient_id)
            
            if not patient:
                print("Data Not Found!")
            else:
                print("\nPATIENT DATA TO DELETE")
                display_header()
                display_patient(patient)
                print("-" * 100)
                
                confirm = input("Confirm Delete? (Y/N): ").upper()
                if confirm == "Y":
                    patients.remove(patient)
                    print("Success! Patient data has been deleted.")
                else:
                    print("Delete Cancelled.")
                    
        elif choice == "2":
            break
            
        else:
            print("Invalid Menu!")

# Statistics Function
def show_statistics():
    while True:
        print("=" * 45)
        print("STATISTICS MENU")
        print("=" * 45)
        
        print("1. Display Total Patient")
        print("2. Display Perbandingan Male vs Female")
        print("3. Display Insurance Sum")
        print("4. Display Admission Sum")
        print("5. Back to Main Menu")
        
        print("=" * 45)
        
        choice = input("Choose Menu: ")
        
        if choice == "1":
            # Display Total Patient
            total_patients = len(patients)
            print(f"\n=> Total Patient(s): {total_patients}")
            
        elif choice == "2":
            # Display Perbandingan Male vs Female
            male_count = sum(1 for p in patients if p["gender"] == "Male")
            female_count = sum(1 for p in patients if p["gender"] == "Female")
            print("\n=> Perbandingan Gender:")
            print(f"   Male   : {male_count}")
            print(f"   Female : {female_count}")
            
        elif choice == "3":
            # Display Insurance Sum
            insurance_counts = {}
            for p in patients:
                ins = p["insurance"]
                insurance_counts[ins] = insurance_counts.get(ins, 0) + 1
            
            print("\n=> Insurance Sum:")
            for ins, count in insurance_counts.items():
                print(f"   {ins:<10}: {count}")
                
        elif choice == "4":
            # Display Admission Sum
            inpatient = sum(1 for p in patients if p["admission_status"] == "Inpatient")
            outpatient = sum(1 for p in patients if p["admission_status"] == "Outpatient")
            

            
            print("\n=> Admission Sum:")
            print(f"   Inpatient  : {inpatient}")
            print(f"   Outpatient : {outpatient}")
            
        elif choice == "5":
            # Kembali ke Main Menu
            break
            
        else:
            # Peringatan Invalid Menu
            print("\nInvalid menu")

# Main Program
while True:
    menu = main_menu()

    if menu == "1":
        read_patient()

    elif menu == "2":
        create_patient()

    elif menu == "3":
        update_patient()

    elif menu == "4":
        delete_patient()

    elif menu == "5":
        show_statistics()

    elif menu == "6":
        print("Thank you for using Hospital Patient Management System")
        break
    
    else:
        print("Invalid Menu")