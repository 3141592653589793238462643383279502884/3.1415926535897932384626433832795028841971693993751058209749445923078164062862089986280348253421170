import numpy as np
import matplotlib.pyplot as plt
from random import uniform, randrange

class Line(object):
	def __init__(self, x = 0, y_down = 0, height = 0):
		self.x = x
		self.y_down = y_down
		self.height = height
		self.y_up = y_down + height
		self.y = [y_down, self.y_up]
	
	def draw(self):
		plt.plot([self.x, self.x], self.y, color = "deepskyblue")

	def collide(self, x, y):
		return abs(x - self.x) <= 1 and y >= self.y_down and y <= self.y_up

	def passed(self, x):
		return x >= self.x

class Rectangle(object):
	def __init__(self, x_left = 0, y_down = 0, width = 0, height = 0):
		self.x_left = x_left
		self.y_down = y_down
		self.width = width
		self.height = height
		self.x_right = x_left + width
		self.x_mid = x_left + width / 2
		self.y_up = y_down + height
		self.x = [x_left, x_left, self.x_right, self.x_right]
		self.y = [y_down, self.y_up, self.y_up, y_down]
	
	def draw(self):
		plt.plot(self.x, self.y, color = "deepskyblue")
		plt.plot([self.x_left, self.x_right], [self.y_down, self.y_down], color = "deepskyblue")

	def collide(self, x, y):
		return x >= self.x_left and x <= self.x_right and y >= self.y_down and y <= self.y_up

	def passed(self, x, case = 0):
		if(case):
			if(x <= self.x_left):
				return True
		else:
			if(x >= self.x_right):
				return True
		return False

class Triangle(object):
	def __init__(self, x_left = 0, y_down = 0, width = 0, height = 0):
		self.x_left = x_left
		self.y_down = y_down
		self.width = width
		self.height = height
		self.halfwidth = width / 2
		self.x_right = x_left + width
		self.x_mid = x_left + self.halfwidth
		self.y_up = y_down + height
		self.x = [x_left, self.x_mid, self.x_right]
		self.y = [y_down, self.y_up, y_down]
	
	def draw(self):
		plt.plot(self.x, self.y, color = "deepskyblue")
		plt.plot([self.x_left, self.x_right], [self.y_down, self.y_down], color = "deepskyblue")

	def collide(self, x, y):
		if(x < self.x_left or x > self.x_right or y < self.y_down or y > self.y_up):
			return False
		return self.y_up - y >= abs(x - self.x_mid) * self.height / self.halfwidth

	def passed(self, x):
		return x >= self.x_right

class Circle(object):
	def __init__(self, x_mid = 0, y_mid = 0, r = 0):
		self.x_mid = x_mid
		self.y_mid = y_mid
		self.r = r
		self.x = np.linspace(x_mid - r, x_mid + r, 1000)
		self.y = np.sqrt(abs(np.power(r, 2) - np.power((self.x - x_mid), 2)))
	
	def draw(self):
		plt.plot(self.x, self.y_mid + self.y, color = "deepskyblue")
		plt.plot(self.x, self.y_mid - self.y, color = "deepskyblue")

	def collide(self, x, y):
		return (x - self.x_mid) ** 2 + (y - self.y_mid) ** 2 <= self.r ** 2

	def passed(self, x, case = 0):
		if(case):
			if(x <= self.x_mid - self.r):
				return True
		else:
			if(x >= self.x_mid + self.r):
				return True
		return False

class Target(object):
	def __init__(self, x_mid = 0, y_mid = 0, r = 0, case = 0):
		self.circle = []
		self.x_mid = x_mid
		self.y_mid = y_mid
		self.case = case
		for i in range(5):
			self.circle.append(Circle(x_mid, y_mid, r * (1 - i * 0.2)))
	
	def draw(self):
		for i in range(5):
			self.circle[i].draw()
		if(self.case == 0):
			plt.plot([self.x_mid, self.x_mid], [0, self.y_mid], color = "deepskyblue")

	def collide(self, x, y, score):
		return self.circle[score].collide(x, y)
			
	def passed(self, x, score, case = 0):
		return score == 5 or self.circle[score].passed(x, case)


## Generate the barrier in scene A
#
#  @param min_height, max_height - the random range of the height of barriers, float
#  @param min_width, max_width - the random range of the width of barriers, float
#  @param x_start, x_end - the range of the barriers, float
#  @param min_interval, max_interval - the random range of the interval of barriers, float
#
#  @return barrier - a list of the barriers, list[[Line, Rectangle, Triangle]]
def a_barrier(min_height = 2, max_height = 32, min_width = 5, max_width = 15, x_start = 20, x_end = 72, min_interval = 10, max_interval = 30):
	barrier = []
	x = x_start
	while(x < x_end):
		height = uniform(min_height, max_height)
		interval = uniform(min_interval, max_interval)
		case = randrange(3)
		if(case == 0):
			new = Line(x, 0, height)
		else:
			width = uniform(min_width, max_width)
			if(width > x_end - x):
				width = x_end - x
			if(case == 1):
				new = Rectangle(x, 0, width, height)
			if(case == 2):
				new = Triangle(x, 0, width, height)
			x += width
		barrier.append(new)
		x += interval
	return barrier

## Generate the barrier in scene B
#
#  @param min_y, max_y - the random range of the y position of barriers, float
#  @param min_height, max_height - the random range of the height of barriers, float
#  @param min_width, max_width - the random range of the width of barriers, float
#  @param x_start, x_end - the range of the barriers, float
#  @param min_interval, max_interval - the random range of the interval of barriers, float
#
#  @return barrier - a list of the barriers, list[Rectangle]
def b_barrier(min_y = 35, max_y = 70, min_height = 5, max_height = 8, min_width = 8, max_width = 12, x_start = 10, x_end = 90, min_interval = 5, max_interval = 15):
	barrier = []
	x = x_start
	while(x < x_end):
		y = uniform(min_y, max_y)
		interval = uniform(min_interval, max_interval)
		height = uniform(min_height, max_height)
		width = uniform(min_width, max_width)
		if(width > x_end - x):
			width = x_end - x
			if(width < min_width):
				return barrier
		new = Rectangle(x, y, width, height)
		x += width
		barrier.append(new)
		x += interval
	return barrier

## Draw the scene from a list
#
#  @param list - the list of the objects that will be drawn, list[[Line, Rectangle, Triangle]]
#  @param difficulty - it will decide the display range
def draw_scene(list, size = 1):
	for i in range(len(list)):
		list[i].draw()
	plt.axis([0, size * 100, 0, size * 75])
	plt.xlabel("x(m)")
	plt.ylabel("y(m)")

if __name__ == "__main__":
	def test_collide():
		#obj = Line(50, 10, 50)
		#obj = Rectangle(25, 10, 50, 50)
		obj = Triangle(25, 10, 50, 50)
		print(obj.collide(30, 40))
		obj.draw()
	
	def test_barrier():
		#bar = a_barrier()
		bar = b_barrier()
		draw_scene(bar)
		
	#test_collide()
	test_barrier()
	plt.axis([0, 100, 0, 75])
	plt.show()