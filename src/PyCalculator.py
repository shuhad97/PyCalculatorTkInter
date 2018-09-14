from tkinter import * 

class CalculatorMain:

	StringNumber1= "" 
	StringNumber2 = ""
	equalsPressed = None
	plusOperation = False
	minusOperation  = False
	divideOperation  = False
	multiplicationOperation  = False
	operationPressed = False

	def __init__(self, master):

		frame = Frame(master)
		frame.pack
		
		equalsPressed = False
		display = "0"
		# lamda function allows a function to become one expression, as
		display = Label(root, text = display)
		c = Button(root, text = "C", command = lambda: self.resetC(display))
		equals = Button(root, text = "=", command = lambda: self.completeOperation(display))
		one = Button(root, text = "1", command = lambda: self.appendnumbers(display, "1"))
		two = Button(root, text = "2", command = lambda: self.appendnumbers(display, "2"))
		three = Button(root, text = "3", command = lambda: self.appendnumbers(display, "3")) 
		four = Button(root, text = "4", command = lambda: self.appendnumbers(display, "4"))
		five = Button(root, text = "5", command = lambda: self.appendnumbers(display, "5"))
		six  = Button(root, text = "6", command = lambda: self.appendnumbers(display, "6"))
		seven = Button(root, text = "7", command = lambda: self.appendnumbers(display, "7"))
		eight = Button(root, text = "8", command = lambda: self.appendnumbers(display, "8"))
		nine = Button(root, text = "9", command = lambda: self.appendnumbers(display, "9"))
		zero = Button(root, text = "0", command = lambda: self.appendnumbers(display, "0"))
		minus = Button(root, text = " - ", command = lambda: self.Operation("-"))
		plus = Button(root, text = " + ", command = lambda: self.Operation("+")) 
		divide = Button(root, text = " / ", command = lambda: self.Operation("/"))  
		multiplication = Button(root, text = " * ", command = lambda: self.Operation("*")) 

		equals.pack()
		display.pack()
		minus.pack()
		plus.pack()
		divide.pack()
		multiplication.pack()
		c.pack()
		zero.pack()
		one.pack()
		two.pack()
		three.pack()
		four.pack()
		five.pack()
		six.pack()
		seven.pack()
		eight.pack()
		nine.pack()
		zero.pack()
	
	def completeOperation(self, display):

		if self.plusOperation:
			Answer = float(self.StringNumber1) + float(self.StringNumber2)
			display['text'] = str(Answer)
			self.plusOperation = False
		if self.minusOperation:
			Answer = float(self.StringNumber1) - float(self.StringNumber2)
			display['text'] = str(Answer)
			self.minusOperation = False
		if self.multiplicationOperation:
			Answer = float(self.StringNumber1) * float(self.StringNumber2)
			display['text'] = str(Answer)
			self.multiplicationOperation= False
		if self.plusOperation:
			Answer = float(self.StringNumber1) / float(self.StringNumber2)
			display['text'] = str(Answer)
			self.plusOperation=False

		self.StringNumber1 = ""
		self.StringNumber2 = ""
		self.operationPressed = False


	def appendnumbers(self,display, number):
			
		if self.StringNumber1 != "" and not self.equalsPressed and not self.operationPressed:
			self.StringNumber1 += number 
			display['text'] = self.StringNumber1

			
		if self.StringNumber1 == "" and not self.equalsPressed and not self.operationPressed:
			self.StringNumber1 = number
			display['text'] = self.StringNumber1
				

		if self.StringNumber2 != "" and not self.equalsPressed and self.operationPressed:
			self.StringNumber2 += number 
			display['text'] = self.StringNumber2

		if self.StringNumber2 == "" and not self.equalsPressed and self.operationPressed:
			self.StringNumber2 = number
			display['text'] = self.StringNumber2
		
	def Operation(self,operationString):

		self.operationPressed = True

		if operationString == "+":
			self.plusOperation = True
		if operationString == "-":
			self.minusOperation = True
		if operationString == "*":
			self.multiplicationOperation = True
		if operationString == "/":
			self.divideOperation = True
	
	def resetC(self, display):
		
		display['text'] = ""
		self.StringNumber1=""
		self.StringNumber2=""
		self.operationPressed = False



root = Tk()
calc = CalculatorMain(root)
root.mainloop() 

	


