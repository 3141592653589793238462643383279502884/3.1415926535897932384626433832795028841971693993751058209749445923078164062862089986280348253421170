import matplotlib.pyplot as plt
from numpy import sin, cos, tan, pi

## Compute the expected (exact) trajectory of an thrown object, based on analytical method.
#
#  @param v0 - initial velocity (in meter/second), float
#  @param theta - initial velocity angle (in radian), float
#  @param x - initial position (in meter), float
#
#  @return x - an array of x-coordinates of the trajectory, list[int]
#  @return y - an array of y-coordinates of the trajectory, list[int]
def shoot(v0, theta, x0 = 0):
	t = 0
	g = 9.81
	x = []
	y = []
	s_x = 0
	s_y = 0
	radian = theta * pi / 180
	v0_x = v0 * cos(radian)
	v0_y = v0 * sin(radian)
	a_y = -g
	while(s_y > -0.01):
		s_x = x0 + v0_x * t
		s_y = v0_y * t + 0.5 * a_y * t ** 2
		x.append(s_x)
		y.append(s_y)
		t += 0.001
	return x, y

if __name__ == "__main__":
	x, y = shoot(35, 120, 50)
	plt.plot(x, y)
	plt.axis([0, 100, 0, 75])
	plt.show()