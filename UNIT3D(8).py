def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Meghana", Python=90, Java=85, C=80)