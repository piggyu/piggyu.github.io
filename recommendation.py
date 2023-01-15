import main

# the recommendation rule:
# 1. recommend three food for each meal
# 2. three food belong to differenct categories
# 3. avoid to recommend food that belongs to the same category with the food that the user has taken in
# 4. the sum of calories of recommeneded food are within the target calories of each meal and no less than 50 calories

def recommendation(gap,existCate):
    solution = []
    categories = []
    if gap < 0 or gap == 0 :
        return ('No more food')
    else:
        return sol(gap,solution,categories,3,existCate)

def sol(gap,solution,categories,type,existCate):
    # when finish: the gap between the sum of food calories and the target calories is less than 50, and the types of food are 3
    if gap < 50 and type == 0:
        return solution
    else:
        for Foodname in main.FoodWarehouse:
            # Foodwarehourse dictionary:
                # key : Foodname, value: a list of [different kinds of nutrients, calories and category the food belongs to]
                # calories is at the 1st column of the list,category at in the 8th
            Category = main.FoodWarehouse[Foodname][7]
            Calories = int(main.FoodWarehouse[Foodname][1])
            Grams = main.FoodWarehouse[Foodname][0]
            solution.append(Foodname+' '+Grams+'g')
            if isLegal(gap, Foodname, Category, categories,existCate):
                categories.append(Category)
                gap -= Calories
                nextsol = sol(gap,solution,categories,type-1,existCate)
                if nextsol != None:
                    return nextsol
            # if the way does not work, go back to the previous step
            solution.pop(-1)
        return None

# check if the way works
def isLegal(gap, Foodname,Category,categories,existCate):
    Calories = int(main.FoodWarehouse[Foodname][1])
    if gap > Calories and Category not in categories and Category not in existCate:
        return True
    return False
