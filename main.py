import csv

# User_profile class ###############################
class User_Profile:
    def __init__(self,name,age,height,weight,gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.BMI = float('%.2f' % (bmiCal(self.height,self.weight)))
        self.state = state(self.BMI)
        self.gender = gender
        self.weightSet = []
        self.basalMetabolism = int(basmetaCal(self.gender,self.weight,self.height,self.age))

        self.breakfast=''
        self.lunch = ''
        self.dinner = ''
        self.intake = dict()

    def __repr__(self):
        return [self.name,self.age,self.height,self.weight,self.gender,self.BMI,self.state,self.basalMetabolism]

    def getgender(self):
        return self.gender

    def addweight(self,newweight):
        self.weightSet.append(newweight)

    def getname(self):
        return self.name

    def getweight(self):
        return self.weight

    def getheight(self):
        return self.height
    
    def getBMI(self):
        return self.BMI

    def getbasalMetabolism(self,gender,weight,height,age):
        return basmetaCal(gender,weight,height,age)

    def getage(self):
        return self.age

    def getAll(self):
        return [self.age,self.height,self.weight,self.gender,self.BMI,self.state,self.basalMetabolism]

    def getweightset(self):
        return self.weightSet

# FOod class ###############################
class Food:
    def __init__(self,name,Measure,Grams,Calories,Protein,Fat,Sat_Fat,Fiber,Carbs,Category):
        self.name = name
        self.Measure = Measure
        self.Grams = Grams
        self.Calories = Calories
        self.Protein = Protein
        self.Fat = Fat
        self.Sat_Fat = Sat_Fat
        self.Fiber = Fiber
        self.Carbs = Carbs
        self.Category = Category
    
    def addfood(self,name):
        self.Database.get(name,dict())

    def __repr__(self):
        return {self.name}

    def getFoodname(self):
        return self.name

    def getCalories(self):
        return self.Calories
    
    def getcategory(self):
        return self.Category

# meal class ###############################
class meal:
    def __init__(self,name):
        self.name = name
        self.food = dict()
        self.calories = 0 
        self.nutrients = dict()
    def getcalories(self):
        return self.calories
    def getnutrients(self):
        return self.nutrients
    def addfood(self,foodname,grams):
        self.food[foodname] = self.food.get(foodname,0) + grams
    def addcalories(self,calories):
        self.calories += calories
    def addnutrient(self,nutrient,grams):
        self.nutrients[nutrient] = self.nutrients.get(nutrient,0) + grams


##########################################        
# food dataset
# download the file on Kaggle: https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods
##########################################
with open('nutrients.csv') as csvfile:
    food_reader = csv.reader(csvfile, delimiter=',')
# Foodwarehourse dictionary:
# keys : Foodname, values: a list of [different kinds of nutrients, calories and category the food belongs to]
    FoodWarehouse = dict()
    line_count = 1
    for row in food_reader:
        # add food to Food class
        if line_count == 1:
            line_count += 1
        Name = row[0]
        # 0:Grams,1:Calories,2:Protein,3:Fat,4:Sat_Fat,5:Fiber,6:Carbs,7:Category
        FoodWarehouse[Name] = [row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
        line_count += 1


# functions to calculate BMI ################################
# from Wikipedia
# "basal metablic rate formula: 
# Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years) 
# Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)""
    
def bmiCal(height,weight):
    if weight and height:
        return weight / height ** 2 * 10000
    return('Oops, you seem to input wrong!')

def state(BMI):
    if BMI < 16: state = 'Underweight (Severe thinness)'
    elif 16 < BMI < 16.99: state = 'Underweight (Moderate thinness)'
    elif 17 < BMI < 18.49: state = 'Underweight (Mild thinness)'
    elif 18.5 < BMI < 24.99: state = 'Healthy'
    elif 25 < BMI < 29.99: state = 'Overweight (Pre-obese)'
    elif BMI > 30: state = 'Obese'
    return state

def basmetaCal(gender,weight,height,age):
    if gender == "male":
        return 88.362 + (13.397*weight) + (4.799*height)-(5.677*age)
    elif gender == 'female':
        return 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)

def Gap(goal,present):
    if goal > present:
        return "+" + goal - present
    else:
        return "-" + present - goal

        
from csv import writer
from csv import reader

# cite from https://thispointer.com/python-add-a-column-to-an-existing-csv-file/
def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)



