from cmu_112_graphics import *
import main
import random
import Button
import datetime
import csv
import recommendation

##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.timerDelay = 50
    app.message = ''
    app.timeslot = dict()

# image ###############################
#  download images from https://www.freepik.com/free-vector/profile-icons-pack-hand-drawn-style_18156023.htm#query=profile&position=29&from_view=search&track=sph
    app.image1 = app.loadImage('f.png')
    app.image1 = app.scaleImage(app.image1, 1/3)
    app.image2 = app.loadImage('m.png')
    app.image2 = app.scaleImage(app.image2, 1/3)

# button with OOP  ###############################
    app.AddButton1 = Button.Button(1400,100,120,50,'Add food')
    app.AddButton2 = Button.Button(1400,200,120,50,'Add food')
    app.AddButton3 = Button.Button(1400,300,120,50,'Add food')
    app.ViewButton = Button.smallButton(app.width/2,app.height/3,120,30,'Change View')
    app.RecButton1 = Button.smallButton(app.width/4*2.6,app.height/7*4.4,200,50,'What to eat for breakfast')
    app.RecButton2 = Button.smallButton(app.width/4*2.6,app.height/7*5.3,200,50,'What to eat for lunch')
    app.RecButton3 = Button.smallButton(app.width/4*2.6,app.height/7*6.3,200,50,'What to eat for dinner')

# textbox with OOP ############################### 
   
    app.textbox1 = Button.Textbox(1150,75,1300,150,False,'','')
    app.textbox2 = Button.Textbox(1150,175,1300,250,False,'','')
    app.textbox3 = Button.Textbox(1150,275,1300,350,False,'','')

# initial calories ###############################
    app.breakfastcal = 0
    app.lunchcal = 0
    app.dinnercal = 0
    app.takeincal = 0
    app.BasCal = 0
    app.percent = 0 

# initial intake data ###############################
    app.breakfast = ''
    app.lunch = ''
    app.dinner = ''
    app.breakfastcal = 0
    app.lunchcal = 0
    app.dinnercal = 0
    app.breakfastcalgap = 0
    app.lunchcalgap = 0
    app.dinnercalgap = 0

# Store the user information ###############################
    app.UserWarehouse = dict()
    app.dateset = []
    # set the initial view of chart as the hisogram
    app.View = True

# set the initial recommend message -- empty lists & empty strings ###############################
    app.RecommendBreList = []
    app.RecommendLunList = []
    app.RecommendDinList = []
    app.RecommendBre = ''
    app.RecommendLun = ''
    app.RecommendDin = ''
    # the existing categories of food that user has intaken
    app.exist = []

# Dataset with datetime ###############################
# create a new user profile based on user input
    x = datetime.datetime.now()
    # change the date to month/day/year
    app.time = (x.strftime("%x"))
    app.dateset.append(app.time)
    name = app.getUserInput('What is your name?')
    gender = app.getUserInput('What is your gender?')
    age = int(app.getUserInput('What is your age?'))
    weight = float(app.getUserInput('Your present weight(kg)'))
    height = float(app.getUserInput('Your present height(cm)'))
    goalweight = float(app.getUserInput('What is your target weight(kg)'))
    BMI = float('%.2f' % (main.bmiCal(height,weight)))
    # check whether the input is legal
    if (not isinstance(age,int)):
        app.showMessage('Please check your answer')
    
    # create the user profile
    app.user = main.User_Profile(name,age,height,weight,gender)
    app.user.addweight(weight)
    app.BMI = BMI
    app.BasCal = int(main.basmetaCal(gender,weight,height,age))
    app.breakfastcalgap = app.BasCal * 0.3
    app.lunchcalgap = app.BasCal * 0.4
    app.dinnercalgap = app.BasCal * 0.3
    app.state = main.state(app.BMI)
    app.target = goalweight

    # update the user info local file 
    app.timeslot = dict()
    app.UserWarehouse[name] = app.UserWarehouse.get(name,app.timeslot)
    app.timeslot[app.time] = app.timeslot.get(app.time,app.user.getAll())

    app.message = f'{app.user.getname()}\nBMI: {BMI}\nBasic metabolism: {app.BasCal}\n{app.state}'
    app.info = app.UserWarehouse[name][app.time]
    
    # wirte user input into the local csv file
    #  cite from https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20your%20CSV%20file%20in,row%20to%20the%20CSV%20file).
    from csv import writer
    with open('User_information.csv','a',newline = '') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([name,app.time,app.info])

    # check the gender and load profile image accordingly
    if app.user.getgender() == 'female':
        app.image = app.image1
    elif app.user.getgender() == 'male':
        app.image = app.image2

##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    canvas.create_text(400, 70, text='(Press U to update)', font='Arial 14 bold', fill='black')
    app.AddButton1.drawRectangleButton(app, canvas)
    app.AddButton2.drawRectangleButton(app, canvas)
    app.AddButton3.drawRectangleButton(app, canvas)
    app.ViewButton.drawRectangleButton(app, canvas)
    app.RecButton1.drawRectangleButton(app, canvas)
    app.RecButton2.drawRectangleButton(app, canvas)
    app.RecButton3.drawRectangleButton(app, canvas)
    splashScreenMode_Drawtitle(app,canvas)
    splashScreenMode_DrawUserInput1(app,canvas)
    splashScreenMode_DrawUserInput2(app,canvas)
    splashScreenMode_DrawUserInput3(app,canvas)
    splashScreenMode_DrawAllintake(app,canvas)
    splashScreenMode_DrawPercent(app,canvas)
    app.textbox1.drawtextbox(app,canvas)
    app.textbox2.drawtextbox(app,canvas)
    app.textbox3.drawtextbox(app,canvas)

    # splashScreenMode_DrawTextboxInput1(app, canvas)
    # draw the user profile only after the user input their information
    # avoid to invoke the draw function before there is a user so check first
    if app.message:
        splashScreenMode_drawmessage(app,canvas)
        if app.View:
            splashScreenMode_drawWeightHisto(app,canvas)
        else:
            splashScreenMode_drawBMIline(app,canvas)
    # draw the recommendation only after the user click the rec buttons__there is app.reco
    if app.RecommendBre:
        splashScreenMode_drawBreakfast(app,canvas)
    if app.RecommendLun:
        splashScreenMode_drawLunch(app,canvas)
    if app.RecommendDin:
        splashScreenMode_drawDinner(app,canvas)

# calculate the intake in total timely #############################
def splashScreenMode_DrawAllintake(app,canvas):
    canvas.create_text(1050,400,text = str(app.takeincal) + 'calories', font = 'Arial 18',fill = 'aquamarine4')

# draw the user_profile with the information user input #############################
def splashScreenMode_drawmessage(app,canvas):
    canvas.create_text(app.width/5,  app.height/6,text= app.message, font='Arial 16 bold', fill='black')
    canvas.create_image(app.width/12, app.height/6, image=ImageTk.PhotoImage(app.image))

# draw the fixed titles #############################
def splashScreenMode_Drawtitle(app,canvas):
    canvas.create_text(900,100,text = 'Breakfast', font = 'Arial 18 bold',fill = 'aquamarine4')
    canvas.create_text(900,200,text = 'Lunch', font = 'Arial 18 bold',fill = 'aquamarine4')
    canvas.create_text(900,300,text = 'Dinner', font = 'Arial 18 bold',fill = 'aquamarine4')
    canvas.create_text(900,400,text = 'Total', font = 'Arial 18 bold',fill = 'aquamarine4')
    canvas.create_text(app.width/4*1.1,40,text= 'Profile', font='Arial 22 bold', fill='turquoise4')
    canvas.create_text(app.width/4*1.1,app.height/3,text= 'Data', font='Arial 22 bold', fill='turquoise4')
    canvas.create_text(app.width/4*3.1,40,text= 'Daily Input', font='Arial 22 bold', fill='turquoise4')
    canvas.create_text(app.width/4*3.1,app.height/7*3.8,text= 'Recommendation', font='Arial 22 bold', fill='turquoise4')


# draw histogram chart #############################
def splashScreenMode_drawWeightHisto(app,canvas):
    basewidth = 800
    basehi = 550
    axis_x1 = 80
    axis_y1 = 260
    axis_x2 = 840
    axis_y2 = 770
    basegap = 50
    # read data from app.dateset and app.user.getweightSet
    for index in range(len(app.dateset)):
        if len(app.user.getweightset()) == len(app.dateset):
            weight = app.user.getweightset()[index]
            rec_x1 = axis_x1 + basegap * index 
            rec_y1 = axis_y2 -  weight / 100 * basehi
            rec_x2 = axis_x1 + basegap * (index+1 )
            rec_y2 = 770
            text_centerX = (rec_x1 + rec_x2) / 2
            text_centerY = rec_y2 + 20
            date = app.dateset[index]
            # draw axis
            canvas.create_line(axis_x1,axis_y2,axis_x1,axis_y1,width = 2)
            canvas.create_line(axis_x1,axis_y2,axis_x2,axis_y2,width = 2)
            # draw unit
            canvas.create_text(axis_x2,axis_y2,text = 'Date')
            canvas.create_text(axis_x1,axis_y1,text = 'Weight')
            # draw rectangle
            canvas.create_rectangle(rec_x1,rec_y1,rec_x2,rec_y2,fill = 'aquamarine3')
            # draw x coornidate
            canvas.create_text(text_centerX,text_centerY,text = date, font = "Arial 9")


# draw line chart#############################
# draw BMI line charts with the target and ranges as reference ###############################
def splashScreenMode_drawBMIline(app,canvas):
    #  draw lines with endpoints of next two BMI dots
    basewidth = 800
    basehi = 550
    axis_x1 = 80
    axis_y1 = 260
    axis_x2 = 840
    axis_y2 = 770
    basegap = 50
    dailyBMI = 0
    pastBMI = 0

    # draw x and y axis of the chart
    canvas.create_line(axis_x1,axis_y2,axis_x1,axis_y1,width = 2)
    canvas.create_line(axis_x1,axis_y2,axis_x2,axis_y2,width = 2)
    # draw unit
    canvas.create_text(axis_x2,axis_y2,text = 'Date',font = "Arial 14" )
    canvas.create_text(axis_x1,axis_y1,text = 'Weight', font = "Arial 14" )
    
    # draw the dots and lines conneting them
    for index in range(len(app.dateset)):
        if len(app.user.getweightset()) == len(app.dateset) and index > 0:
            date = app.dateset[index-1]
            height = app.user.getheight()
            initBMI = app.BMI
            targetBMI = float('%.2f' % (main.bmiCal(height,app.target)))
            dailyweight = app.user.getweightset()[index]
            dailyBMI = float('%.2f' % (main.bmiCal(height,dailyweight)))
            # the center of dots are at the center of each rectangle in histogram
            rec_x1 = axis_x1 + basegap * index 
            rec_x2 = axis_x1 + basegap * (index + 1)
            rec_x0 = axis_x1 + basegap * (index - 1)
            dot1x = (rec_x1 + rec_x2) / 2
            dot1y = axis_y2 -  dailyBMI / 45 * basehi
            dot0x = (rec_x1 + rec_x0) / 2
            if index == 1:
                dot0y = axis_y2 - initBMI / 45 * basehi
            else:
                dot0y = axis_y2 -  pastBMI / 45 * basehi
            # draw target line
            TargetY = axis_y2 -  targetBMI / 45 * basehi
            TargetX1 = axis_x1
            TargetX2 = axis_x2
            canvas.create_line(TargetX1,TargetY,TargetX2,TargetY,fill = 'aquamarine1')
            canvas.create_text(TargetX1-20,TargetY,text = 'Target \nBMI',font = 'Arial 10')
            # draw reference lines --- Overweight
            ReferY1 = axis_y2 -  30 / 45 * basehi
            ReferX1 = axis_x1
            ReferX2 = axis_x2
            canvas.create_line(ReferX1,ReferY1,ReferX2,ReferY1,fill = 'aquamarine1')
            canvas.create_text(ReferX1-30,ReferY1,text = 'Overweight',font = 'Arial 10')
            # draw reference lines --- Overweight
            ReferY2 = axis_y2 -  25 / 45 * basehi
            canvas.create_line(ReferX1,ReferY2,ReferX2,ReferY2,fill = 'aquamarine1')
            canvas.create_text(ReferX1-30,ReferY2,text = 'Healthy',font = 'Arial 10') 
            # draw reference lines --- Underweight
            ReferY3 = axis_y2 -  18.5 / 45 * basehi
            canvas.create_line(ReferX1,ReferY3,ReferX2,ReferY3,fill = 'aquamarine1')
            canvas.create_text(ReferX1-30,ReferY3,text = 'Underweight',font = 'Arial 10')          
            # draw the line chart
            canvas.create_line(dot1x,dot1y,dot0x,dot0y,fill = 'grey',width = 2)
            # draw x coornidate
            text_centerX = dot0x
            text_centerY = axis_y2 + 20
            canvas.create_text(text_centerX,text_centerY,text = date, font = "Arial 9") 
            pastBMI = dailyBMI


# draw the BREAKFAST recommendation message to the canvas
def splashScreenMode_drawBreakfast(app,canvas):
    canvas.create_text(app.width/4*3.5,app.height/4*2.5,font = 'Arial 16',text = app.RecommendBre)
# draw the LUNCH recommendation message to the canvas
def splashScreenMode_drawLunch(app,canvas):
    canvas.create_text(app.width/4*3.5,app.height/4*3,font = 'Arial 16',text = app.RecommendLun)
# draw the DINNER recommendation message to the canvas
def splashScreenMode_drawDinner(app,canvas):
    canvas.create_text(app.width/4*3.5,app.height/4*3.5,font = 'Arial 16',text = app.RecommendDin)


# Update user information #######################
def splashScreenMode_keyPressed(app, event):
    # when textbox1 is activated
    if app.textbox1.getchecked() == True:
        if event.key == 'Space':
            app.textbox1.addtext(' ')
        elif event.key == 'BackSpace':
            app.textbox1.deletetext()
        elif event.key == 'Return':
            app.textbox1.addtext('\n')
        else:
            app.textbox1.addtext(event.key)
    # when textbox2 is activated
    elif app.textbox2.getchecked() == True:
        if event.key == 'Space':
            app.textbox2.addtext(' ')
        elif event.key == 'BackSpace':
            app.textbox2.deletetext()
        elif event.key == 'Return':
            app.textbox2.addtext('\n')
        else:
            app.textbox2.addtext(event.key)
    # when textbox3 is activated
    elif app.textbox3.getchecked() == True:
        if event.key == 'Space':
            app.textbox3.addtext(' ')
        elif event.key == 'BackSpace':
            app.textbox3.deletetext()
        elif event.key == 'Return':
            app.textbox3.addtext('\n')
        else:
            app.textbox3.addtext(event.key)
    else:
    # when press 'u' for updating data proactively
        if event.key == 'u':
            date = app.getUserInput('What is the date?(mm/dd/yy)')
            app.dateset.append(date)
            weight = float(app.getUserInput('Your present weight(kg)'))
            app.user.addweight(weight)
            gender = app.user.getgender()
            height = app.user.getheight()
            age = app.user.getage()
            BMI = float('%.2f' % (main.bmiCal(height,weight)))
            BasCal = int(main.basmetaCal(gender,weight,height,age))
            state = main.state(BMI)
            app.message = f'{app.user.getname()}\nBMI: {BMI}\nBasic metabolism: {BasCal}\n{state}'


####################################################################
# Buttons to -- Add food / Ask for recommendation ###########
def splashScreenMode_mousePressed(app, event):
    x = event.x
    y = event.y

# activate textbox1
    if app.textbox1.isActivated(x,y):
        app.textbox1.activate()
        app.textbox2.inactivate()
        app.textbox3.inactivate()
        app.lunch += Calculateoutput2(app)
        app.dinner += Calculateoutput3(app)
        app.textbox2.changetext('')
        app.textbox3.changetext('')
# activate textbox2
    elif app.textbox2.isActivated(x,y):
        app.textbox2.activate()
        app.textbox1.inactivate()
        app.textbox3.inactivate()
        app.breakfast += Calculateoutput1(app)
        app.dinner += Calculateoutput3(app)
        app.textbox1.changetext('')
        app.textbox3.changetext('')
# activate textbox3
    elif app.textbox3.isActivated(x,y):
        app.textbox3.activate()
        app.textbox1.inactivate()
        app.textbox2.inactivate()
        app.breakfast += Calculateoutput1(app)
        app.lunch += Calculateoutput2(app)
        app.textbox1.changetext('')
        app.textbox2.changetext('')

# inactivate all textboxes
    else:
        app.textbox1.inactivate()
        app.textbox2.inactivate()
        app.textbox3.inactivate()
        app.breakfast += Calculateoutput1(app)
        app.lunch += Calculateoutput2(app)
        app.dinner += Calculateoutput3(app)
        app.textbox1.changetext('')
        app.textbox2.changetext('')
        app.textbox3.changetext('')

# add food to breakfast
    if isAddButton1Pressed(app, x, y):
        splashScreenMode_GetInput1(app)
# add food to lunch
    if isAddButton2Pressed(app, x, y):
        splashScreenMode_GetInput2(app)
# add food to dinner
    if isAddButton3Pressed(app, x, y):
        splashScreenMode_GetInput3(app)
# change the view of chart
    if isViewButtonPressed(app, x, y):
        app.View = not app.View

# recommend breakfast
    if isRecButton1Pressed(app, x, y):
        app.RecommendBreList = recommendation.recommendation(app.breakfastcalgap,app.exist)
        app.RecommendBre = '\n'.join(app.RecommendBreList)

# recommend lunch
    if isRecButton2Pressed(app, x, y):
        app.RecommendLunList = recommendation.recommendation(app.lunchcalgap,app.exist)
        app.RecommendLun = '\n'.join(app.RecommendLunList)

# recommend dinner
    if isRecButton3Pressed(app, x, y):
        app.RecommendDinList = recommendation.recommendation(app.dinnercalgap,app.exist)
        app.RecommendDin = '\n'.join(app.RecommendDinList)

# Add food with the button clicking method ###############################
def splashScreenMode_GetInput1(app):
    Breakfast = main.meal('Breakfast')
    Foodname = app.getUserInput('The name of food?')
    if Foodname in main.FoodWarehouse:
        Calories = main.FoodWarehouse[Foodname][1]
        Grams = main.FoodWarehouse[Foodname][0]
        CaloriesPersevring = float(Calories) / float(Grams)
        FoodGrams = int(app.getUserInput('The amount of food(g)?'))
        FoodCalories = int(FoodGrams * CaloriesPersevring) 
        Breakfast.addfood(Foodname,FoodGrams)
        Breakfast.addcalories(FoodCalories)
        app.breakfast += f'{Foodname}, {FoodGrams}g, {FoodCalories}' + '\n'
        app.breakfastcal = Breakfast.getcalories()
        app.takeincal += FoodCalories
        app.exist.append(main.FoodWarehouse[Foodname][7])
 
# Draw user input food&amounts&calories with button clicking method or textbox method ###############################
#  BREAKFAST ###############################
def splashScreenMode_DrawUserInput1(app,canvas):
    # draw from textbox
    if app.textbox1.getchecked() == True:
        canvas.create_text(1225,113,text = app.textbox1.gettext(),font = 'Arial 13')
    # draw from inputbox 
    canvas.create_text(1040,100,text = app.breakfast, font = 'Arial 15',fill = 'darkslategray')

# LUNCH ###############################
def splashScreenMode_GetInput2(app):
    Lunch = main.meal('Lunch')
    Foodname = app.getUserInput('The name of food?')
    if Foodname in main.FoodWarehouse:
        Calories = main.FoodWarehouse[Foodname][1]
        Grams = main.FoodWarehouse[Foodname][0]
        CaloriesPersevring = float(Calories) / float(Grams)
        FoodGrams = int(app.getUserInput('The amount of food(g)?'))
        FoodCalories = int(FoodGrams * CaloriesPersevring) 
        Lunch.addfood(Foodname,FoodGrams)
        Lunch.addcalories(FoodCalories)
        app.lunch += f'{Foodname}, {FoodGrams}g, {FoodCalories}' + '\n'
        app.lunchcal = Lunch.getcalories()
        app.takeincal += FoodCalories
        app.exist.append(main.FoodWarehouse[Foodname][7])

def splashScreenMode_DrawUserInput2(app,canvas):
    # draw from textbox
    if app.textbox2.getchecked() == True:
        canvas.create_text(1225,213,text = app.textbox2.gettext(),font = 'Arial 13')
    # draw from inputbox 
    canvas.create_text(1040,200,text = app.lunch, font = 'Arial 15',fill = 'darkslategray')

# DINNER ###############################
def splashScreenMode_GetInput3(app):
    Dinner = main.meal('Dinner')
    Foodname = app.getUserInput('The name of food?')
    if Foodname in main.FoodWarehouse:
        Calories = main.FoodWarehouse[Foodname][1]
        Grams = main.FoodWarehouse[Foodname][0]
        CaloriesPersevring = float(Calories) / float(Grams)
        FoodGrams = int(app.getUserInput('The amount of food(g)?'))
        FoodCalories = int(FoodGrams * CaloriesPersevring) 
        Dinner.addfood(Foodname,FoodGrams)
        Dinner.addcalories(FoodCalories)
        app.dinner += f'{Foodname}, {FoodGrams}g, {FoodCalories}' + '\n'
        app.dinnercal = Dinner.getcalories()
        app.takeincal += FoodCalories
        app.exist.append(main.FoodWarehouse[Foodname][7])

def splashScreenMode_DrawUserInput3(app,canvas):
    # draw from textbox
    if app.textbox3.getchecked() == True:
        canvas.create_text(1225,313,text = app.textbox3.gettext(),font = 'Arial 13')
    # draw from inputbox 
    canvas.create_text(1040,300,text = app.dinner, font = 'Arial 15',fill = 'darkslategray')

# Draw the progress of the intake(the percent of daily intake)
def splashScreenMode_DrawPercent(app,canvas):
    if app.BasCal:
        app.percent = app.takeincal / app.BasCal
        canvas.create_rectangle(490,120,490 + app.percent * 250,150,fill = 'aquamarine3')
        canvas.create_rectangle(490,170,740,200,fill = 'gray')
        canvas.create_line(490,110,490,210,fill = 'aquamarine3',width = 2)
        canvas.create_text(450,185,text = 'Target', font = 'Arial 15 bold',fill = 'darkslategray')
        canvas.create_text(450,135,text = 'Progress', font = 'Arial 15 bold',fill = 'darkslategray')


##########################################
# State Fuctions
##########################################

# check whether the mouse press the buttons
def isAddButton1Pressed(app, x, y):
    row1 = app.AddButton1.getCenterX() - app.AddButton1.getlenX()/2
    col1 = app.AddButton1.getCenterY() - app.AddButton1.getlenY()/2
    row2 = app.AddButton1.getCenterX() + app.AddButton1.getlenX()/2
    col2 = app.AddButton1.getCenterY() + app.AddButton1.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False
def isAddButton2Pressed(app, x, y):
    row1 = app.AddButton2.getCenterX() - app.AddButton2.getlenX()/2
    col1 = app.AddButton2.getCenterY() - app.AddButton2.getlenY()/2
    row2 = app.AddButton2.getCenterX() + app.AddButton2.getlenX()/2
    col2 = app.AddButton2.getCenterY() + app.AddButton2.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False
def isAddButton3Pressed(app, x, y):
    row1 = app.AddButton3.getCenterX() - app.AddButton3.getlenX()/2
    col1 = app.AddButton3.getCenterY() - app.AddButton3.getlenY()/2
    row2 = app.AddButton3.getCenterX() + app.AddButton3.getlenX()/2
    col2 = app.AddButton3.getCenterY() + app.AddButton3.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False

def isViewButtonPressed(app, x, y):
    row1 = app.ViewButton.getCenterX() - app.ViewButton.getlenX()/2
    col1 = app.ViewButton.getCenterY() - app.ViewButton.getlenY()/2
    row2 = app.ViewButton.getCenterX() + app.ViewButton.getlenX()/2
    col2 = app.ViewButton.getCenterY() + app.ViewButton.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False

def isRecButton1Pressed(app, x, y):
    row1 = app.RecButton1.getCenterX() - app.RecButton1.getlenX()/2
    col1 = app.RecButton1.getCenterY() - app.RecButton1.getlenY()/2
    row2 = app.RecButton1.getCenterX() + app.RecButton1.getlenX()/2
    col2 = app.RecButton1.getCenterY() + app.RecButton1.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False

def isRecButton2Pressed(app, x, y):
    row1 = app.RecButton2.getCenterX() - app.RecButton2.getlenX()/2
    col1 = app.RecButton2.getCenterY() - app.RecButton2.getlenY()/2
    row2 = app.RecButton2.getCenterX() + app.RecButton2.getlenX()/2
    col2 = app.RecButton2.getCenterY() + app.RecButton2.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False

def isRecButton3Pressed(app, x, y):
    row1 = app.RecButton3.getCenterX() - app.RecButton3.getlenX()/2
    col1 = app.RecButton3.getCenterY() - app.RecButton3.getlenY()/2
    row2 = app.RecButton3.getCenterX() + app.RecButton3.getlenX()/2
    col2 = app.RecButton3.getCenterY() + app.RecButton3.getlenY()/2
    if  row1 <= x <= row2 and col1 <= y <= col2:
       return True
    return False

# Calculate the caloires from the user input textbox
# BREAKFAST ###############################
def Calculateoutput1(app):
    Breakfast = main.meal('Breakfast')
    output = ''
    for item in app.textbox1.gettext().split('\n'):
        Foodname = item.split(',')[0]
        if Foodname in main.FoodWarehouse:
            FoodGrams = int(item.split(',')[1])
            Calories = main.FoodWarehouse[Foodname][1]
            Grams = main.FoodWarehouse[Foodname][0]
            CaloriesPersevring = float(Calories) / float(Grams)
            FoodCalories = int(FoodGrams * CaloriesPersevring)
            output += Foodname + ', ' + str(FoodGrams) + 'g' + ', ' + str(FoodCalories) +'\n'
            Breakfast.addfood(Foodname,FoodGrams)
            Breakfast.addcalories(FoodCalories)
            app.breakfastcal = Breakfast.getcalories()
            app.takeincal += FoodCalories
            app.exist.append(main.FoodWarehouse[Foodname][7])
    return output

# LUNCH ###############################
def Calculateoutput2(app):
    Lunch = main.meal('Lunch')
    output = ''
    for item in app.textbox2.gettext().split('\n'):
        Foodname = item.split(',')[0]
        if Foodname in main.FoodWarehouse:
            FoodGrams = int(item.split(',')[1])
            Calories = main.FoodWarehouse[Foodname][1]
            Grams = main.FoodWarehouse[Foodname][0]
            CaloriesPersevring = float(Calories) / float(Grams)
            FoodCalories = int(FoodGrams * CaloriesPersevring)
            output += Foodname + ', ' + str(FoodGrams) + 'g' + ', ' + str(FoodCalories) +'\n'
            Lunch.addfood(Foodname,FoodGrams)
            Lunch.addcalories(FoodCalories)
            app.lunchcal = Lunch.getcalories()
            app.takeincal += FoodCalories
            app.exist.append(main.FoodWarehouse[Foodname][7])
    return output

# DINNER ###############################
def Calculateoutput3(app):
    Dinner = main.meal('Dinner')
    output = ''
    for item in app.textbox3.gettext().split('\n'):
        Foodname = item.split(',')[0]
        if Foodname in main.FoodWarehouse:
            FoodGrams = int(item.split(',')[1])
            Calories = main.FoodWarehouse[Foodname][1]
            Grams = main.FoodWarehouse[Foodname][0]
            CaloriesPersevring = float(Calories) / float(Grams)
            FoodCalories = int(FoodGrams * CaloriesPersevring)
            output += Foodname + ', ' + str(FoodGrams) + 'g' + ', ' + str(FoodCalories) +'\n'
            Dinner.addfood(Foodname,FoodGrams)
            Dinner.addcalories(FoodCalories)
            app.breakfastcal = Dinner.getcalories()
            app.takeincal += FoodCalories
            app.exist.append(main.FoodWarehouse[Foodname][7])
    return output


runApp(width=1500, height=850)
