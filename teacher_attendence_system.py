import json

# STEP 1: Load existing attendance data from the JSON file (if it exists)
with open("teacher_attendance.json", "r") as f:
    data = json.load(f)   # reads the file content and converts it into a Python dictionary


# STEP 2: Ask which teacher to mark attendance for
teacher_atten = input("enter the name of the teacher:")

# STEP 3: Update the attendance count in memory (in the 'data' dictionary)
if teacher_atten in data:
    data[teacher_atten] += 1
    print(data[teacher_atten])

# STEP 4: Save the updated data back into the JSON file
with open("teacher_attendance.json", "w") as f:
    json.dump(data, f)   # writes the updated dictionary back into the file as JSON
