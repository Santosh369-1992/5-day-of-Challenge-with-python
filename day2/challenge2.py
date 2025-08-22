attendence = input("Were you present in all days or day gap was there? ")

if attendence == "all days":
    assignment = input("Assignment completed? (yes/no): ")
    attended   = input("Attended live class? (yes/no): ")
    camera     = input("Camera was ON? (yes/no): ")

    if assignment == "yes" and attended == "yes" and camera == "yes":
        print("Eligible for certificate")
    else:
        print("Not Eligible for certificate")

elif attendence == "day gap":
    print("Not Eligible for certificate")

else:
    print("out of options")
