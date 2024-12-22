def write_passing(file_path):
    with open (file_path,"r") as file:

        passing = []

        lines = file.readlines()

        for line in lines[1:]:
            if int(line.split(",")[2]) >= 50:
                passing.append(line)
    
    with open ("passing_students.txt","w") as file:
        for line in passing:
            file.write(line)

