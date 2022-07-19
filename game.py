from game_a import game_a
from game_b import game_b

## Start a game
#
#  @return round - it shows how many rounds has the player played in this game, int
#  @return total_score - the total score that the player has got in this game, int
def game():
	#Initialize
	round = 0
	total_score = 0
	difficulty = 1.0
	health = 3
	scene = 0

	#Print the information
	print("\nRound:", round)
	print("Score:", total_score)
	print("Difficulty: {:.1f}".format(difficulty))
	print("Health:", health)
	print()

	#Modify the variable value according to the results
	while(health):
		if(scene == 0):
			score = game_a(difficulty)
		else:
			score = game_b(difficulty)
		if(score):
			scene = 1 - scene
			total_score += score
			health += 1
			difficulty += 0.1
		else:
			health -= 1
		round += 1

		#Print the information
		print("\nRound:", round)
		print("Score:", total_score)
		print("Difficulty: {:.1f}".format(difficulty))
		print("Health:", health)
		print()

	#Game over and print the information
	print("Game over.")
	print("Round:", round)
	print("Score:", total_score)
	print()

	return round, total_score

if __name__ == "__main__":
	round, score = game()
	print(round, score)