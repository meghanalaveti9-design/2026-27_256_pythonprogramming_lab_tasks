class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

except InvalidMarksError as e:
    print("Error:", e)

finally:
    print("Program finished")