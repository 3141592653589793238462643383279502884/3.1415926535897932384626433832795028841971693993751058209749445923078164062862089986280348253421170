import matplotlib.pyplot as plt
from shoot import shoot
from scene import a_barrier, draw_scene, Target
from get_input import get_v0, get_theta

## Start a round of game in the scene A
#
#  @param difficulty - the difficulty of the game, float
#
#  @return score - the score that the player has got in this round, int
def game_a(difficulty = 1):
	#Initialize
	ptr = 0
	i0 = 0
	i1 = 0
	score = 0

	#Create the scene and show it
	barrier = a_barrier(difficulty ** 2 * 2, difficulty ** 2 * 32, difficulty * 5, difficulty * 15, difficulty ** 2 * 20, difficulty ** 2 * 72)
	scene = barrier.copy()
	target = Target(difficulty ** 2 * 90, 10, 5)
	scene.append(target)
	draw_scene(scene, difficulty ** 2)
	plt.show()

	#Get v0 and theta from user input and calculate the trajectory
	v0 = get_v0(difficulty)
	theta = get_theta()
	x, y = shoot(v0, theta)

	#Collision detection of the barriers
	for i in range(len(x)):
		if(ptr == len(barrier)):
			i0 = i
			break
		if(barrier[ptr].collide(x[i], y[i])):
			plt.plot(x[:i + 1], y[:i + 1])
			draw_scene(scene, difficulty ** 2)
			print("Failed.\n")
			plt.show()
			return 0
		if(barrier[ptr].passed(x[i])):
			ptr += 1

	#Collision detection of the target
	for i in range(i0, len(x)):
		if(target.collide(x[i], y[i], score)):
			score += 1
			i1 = i
		if(target.passed(x[i], score)):
			break

	draw_scene(scene, difficulty ** 2)

	#Determine whether it has succeeded
	if(score):
		plt.plot(x[:i1 + 1], y[:i1 + 1])
		print("Succeeded, you've got {} points in this round.\n".format(score))
	else:
		plt.plot(x, y)
		print("Failed.\n")
	plt.show()

	return score

if __name__ == "__main__":
	score = game_a()
	print(score)