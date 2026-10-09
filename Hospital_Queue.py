'''
Question 6: Hospital Patient Queue 
A hospital maintains a list of patients waiting for consultation. 
Write a function that removes the first patient after consultation, 
adds a new patient to the queue, and displays the updated queue. 
'''
patients=['Ramesh','Suresh','Subhas','Jadu','Madhu']
def patient_queue(patients:list):
    while(True):
            choice = int(input(('Enter Choice-\n1. Add Patient\n2. Remove Consulted Patient\n3. Dispaly Queue\n4. Exit:\n')))
            if choice== 1:
                patients.append(input('Enter patient name: '))
                print('Patient Added!')
            elif choice == 2:
                if patients.pop(0):
                    print('First Patient Removed!')
                else:
                    print('No Patient in the queue')
            elif choice == 3:
                print('Available patients:')
                for i in patients:
                    print(i)
            elif choice == 4:
                break
            else:
                print('Invalid Choice')
                
patient_queue(patients)