from cmu_112_graphics import *

class button:
    def __init__(self,text):
        self.text = text
        self.visible = True

    

# class ChangeView(button):

class Button:
    def __init__(self, CenterX, CenterY, lenX, lenY, text,
                 bgColor = "aquamarine4", outlineColor = "aquamarine1", outlineWidth = 3):
        self.CenterX = CenterX
        self.CenterY = CenterY
        self.lenX = lenX
        self.lenY = lenY
        self.bgColor = bgColor
        self.outlineColor = outlineColor
        self.outlineWidth = outlineWidth
        self.text = text
        self.isPressed = False

    def drawRectangleButton(self, app, canvas):
        canvas.create_rectangle(self.CenterX - self.lenX / 2,
                                self.CenterY - self.lenY / 2,
                                self.CenterX + self.lenX / 2,
                                self.CenterY + self.lenY / 2,
                                fill = self.bgColor, outline = self.outlineColor,
                                width = self.outlineWidth)

        canvas.create_text(self.CenterX, self.CenterY, text = self.text, fill = 'aquamarine1',
                           font = "Arial 16 bold", anchor = "c")
    
    def getCenterX(self):
        return self.CenterX
    def getlenX(self):
        return self.lenX
    def getCenterY(self):
        return self.CenterY
    def getlenY(self):
        return self.lenY

class smallButton(Button):
    def drawRectangleButton(self, app, canvas):
        canvas.create_rectangle(self.CenterX - self.lenX / 2,
                                self.CenterY - self.lenY / 2,
                                self.CenterX + self.lenX / 2,
                                self.CenterY + self.lenY / 2,
                                fill = 'light grey', outline = '',
                                width = 2)

        canvas.create_text(self.CenterX, self.CenterY, text = self.text, fill = 'black',
                           font = "Arial 14", anchor = "c")


class Textbox:
    def __init__(self,x1,y1,x2,y2,state,fill,text):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.state = state
        self.text = ''
        self.fill = fill
    
    def activate(self):
        self.state = True

    def inactivate(self):
        self.state = False

    def changestate(self):
        self.state = not self.state

    def isActivated(self,x,y):
        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            return True
        else:
            return False

    def addtext(self,newtext):
        self.text += newtext

    def deletetext(self):
        self.text = self.text[:-1]

    def drawtextbox(self,app,canvas):
        canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill = self.fill)

    def gettext(self):
        return self.text

    def getchecked(self):
        return self.state

    def changetext(self,newtext):
        self.text = newtext


