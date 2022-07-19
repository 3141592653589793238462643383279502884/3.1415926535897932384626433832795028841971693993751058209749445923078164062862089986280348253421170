import matplotlib.pyplot as plt
from random import uniform, randrange
from shoot import shoot
from scene import b_barrier, draw_scene, Target, Line
from get_input import get_x0, get_v0, get_theta

## Start a round of game in the scene B
#
#  @param difficulty - the difficulty of the game, float
#
#  @return score - the score that the player has got in this round, int
def game_b(difficulty = 1):
	#Initialize
	i0 = 0
	i1 = 0
	score = 0
	case = 0
	ptr = 0

	#Create the scene and show it
	barrier = b_barrier(difficulty ** 2 * 35, difficulty ** 2 * 70, difficulty * 5, difficulty * 8, difficulty * 8, difficulty * 12, difficulty ** 2 * 10, difficulty ** 2 * 90)
	scene = barrier.copy()
	select = randrange(len(barrier))
	length = uniform(10, 20)
	target = Target(barrier[select].x_mid, barrier[select].y_down - length, 5, 1)
	line = Line(barrier[select].x_mid, barrier[select].y_down - length, length)
	scene.append(target)
	scene.append(line)
	draw_scene(scene, difficulty ** 2)
	plt.show()

	#Get v0 and theta from user input and calculate the trajectory
	x0 = get_x0(difficulty ** 2)
	v0 = get_v0(difficulty)
	theta = get_theta(1)
	x, y = shoot(v0, theta, x0)

	#If theta <= 90, collision detection will be from left to right.
	#If theta > 90, collision detection will be from right to left.
	if(theta > 90):
		case = 1
		ptr = len(barrier) - 1
	
	#Collision detection of the barriers
	for i in range(len(x)):
		if(ptr == select):
			i0 = i
			break
		if(barrier[ptr].collide(x[i], y[i])):
			plt.plot(x[:i + 1], y[:i + 1])
			draw_scene(scene, difficulty ** 2)
			print("Failed.\n")
			plt.show()
			return 0
		if(barrier[ptr].passed(x[i], case)):
			if(case):
				ptr -= 1
			else:
				ptr += 1

	#Collision detection of the target
	for i in range(i0, len(x)):
		if(target.collide(x[i], y[i], score)):
			score += 1
			i1 = i
		if(score == 5 or target.passed(x[i], score, case)):
			if(score == 0):
				break
			plt.plot(x[:i1 + 1], y[:i1 + 1])
			draw_scene(scene, difficulty ** 2)
			print("Succeeded, you've got {} points in this round.\n".format(score))
			plt.show()
			return score
		if(score == 0):
			if(line.collide(x[i], y[i])):
				plt.plot(x[:i + 1], y[:i + 1])
				draw_scene(scene, difficulty ** 2)
				print("Succeeded, you've got 1 points in this round.\n")
				plt.show()
				return 1
			if(barrier[select].collide(x[i], y[i])):
				plt.plot(x[:i + 1], y[:i + 1])
				draw_scene(scene, difficulty ** 2)
				print("Failed.\n")
				plt.show()
				return 0

	#Draw the scene
	plt.plot(x, y)
	draw_scene(scene, difficulty ** 2)
	if(score):
		print("Succeeded, you've got {} points in this round.\n".format(score))
	else:
		print("Failed.\n")
	plt.show()
	return score

if __name__ == "__main__":
	score = game_b()
	print(score)