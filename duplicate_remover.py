# Read data from file -> remove duplicates -> write unique data in new file
import os
file_path = input("Enter File path: ")
unique_data = []
if os.path.exists(file_path):
    with open(file_path, 'r') as file: # reading file and remove duplicates
        for data in file:
            if data not in unique_data:
                unique_data.append(data)

    
    with open('duplicates_removed.txt', 'a') as duplicates_removed:
        for u_data in unique_data:
            duplicates_removed.write(f"{u_data}") # writing data in  duplicates_removed.txt file
        print("File saved successfully.")



user
pass


1. Sign UP
2. Login


print('Hi')




    


