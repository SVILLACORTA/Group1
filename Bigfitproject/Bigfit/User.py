# Team Big Fit
# Created by: Serena Villacorta
# Big Fit User Class


class User(object):

    def __init__(self, first_name, last_name, start_weight, target_weight, feet, inches, date_of_birth, gender, zip_code, email, start_date, end_date, password):
        self.first_name = first_name
        self.last_name = last_name
        self.start_weight = start_weight
        self.target_weight = target_weight
        self.feet = feet
        self.inches = inches
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.zip_code = zip_code
        self.email = email
        self.start_date = start_date
        self.end_date = end_date
        self.password = password

    def print_user(self):
        print("First Name ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Start Weight: ", self.start_weight)
        print("Target Weight: ", self.target_weight)
        print("Feet: ", self.feet)
        print("Inches: ", self.inches)
        print("Date of Birth: ", self.date_of_birth)
        print("Gender: ", self.gender)
        print("Zip Code: ", self.zip_code)
        print("Email: ", self.email)
        print("Start Date: ", self.start_date)
        print("End Date: ", self.end_date)
        print("Password: ", self.password)