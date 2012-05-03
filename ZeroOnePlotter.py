from Tkinter import *

class Plotter:

	def __init__(self, sequence, width = 1000, height = 400, boundariesSizeQuotient = 0.06):
		self.values = sequence
		self.valuesCount = len(self.values)

		self.sizeQuotient = boundariesSizeQuotient

		self.DeterminePlotBoundaries(width, height)
		self.CreateCanvas(width, height)
		self.DrawGrid()
		self.DrawLabels()
		self.DrawData()

		self.canvas.pack()
		self.root.mainloop()

	def CreateCanvas(self, width, height):
		self.root = Tk()
		self.canvas = Canvas(self.root, width = width, height = height)

	def DeterminePlotBoundaries(self, width, height):
		self.upper = height * self.sizeQuotient
		self.lower = height * (1.0 - self.sizeQuotient)
		self.left = width * self.sizeQuotient
		self.right = width * (1.0 - self.sizeQuotient)


	def DrawGrid(self):
		gridColor = "green"

		self.canvas.create_line(self.left, self.upper, self.right, self.upper, fill = gridColor)
		self.canvas.create_line(self.right, self.upper, self.right, self.lower, fill = gridColor)
		self.canvas.create_line(self.left, self.lower, self.right, self.lower, fill = gridColor)
		self.canvas.create_line(self.left, self.upper, self.left, self.lower, fill = gridColor)

		dashPattern = [4,4]

		yStep = (self.lower - self.upper)/10.0
		for i in range(1,10):
			self.canvas.create_line(self.left, self.upper + yStep*i, self.right, self.upper + yStep*i, fill = gridColor, dash = dashPattern)
		
		xStep = self.XStep()
		for i in range(1, self.valuesCount-1):
			self.canvas.create_line(self.left + xStep*i, self.upper, self.left + xStep*i, self.lower, fill = gridColor, dash = dashPattern)


	def XStep(self):
		return (self.right - self.left)/float(self.valuesCount-1)

	def DrawLabels(self):
		#string = "Min = " + str(min(self.values)) + "; Max = " + str(max(self.values))
		string = "Min = {0}; Max = {1}.".format(min(self.values), max(self.values))
		self.canvas.create_text((0.4 * self.right, 0.5 * self.upper), text = string)

	def DrawData(self):
		dataColor = "black"
		xStep = self.XStep()

		for i in range(1, self.valuesCount):
			self.canvas.create_line(self.left + xStep*(i-1), self.Transform(self.values[i-1]), self.left + xStep*i, self.Transform(self.values[i]), fill = dataColor)

	def Transform(self, y):
		return self.lower - y*(self.lower - self.upper)



	