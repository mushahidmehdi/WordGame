from ps4a import *
from ps4b import *


wordList = loadWords()
# frequencyDict = getFrequencyDict(sequence)

# def getWordScore(word, n):
# 	word = word.lower()
# 	wordScore = 0
# 	for i in word:
# 		wordScore += SCRABBLE_LETTER_VALUES.get(i)
# 	wordScore *= len(word)
# 	if len(word) == n:
# 		wordScore += 50
# 
# 	return wordScore
# n = 4
# print(getWordScore(word, n))
# 

# def updateHand(hand, word):
# 
# 	word = word.lower()
# 	hand = hand.copy()
# 
# 	for char in word:
# 		hand[char] -= 1
# 	return hand


#def isValidWord(word, hand, wordList):
# 
# 	# Gurded Statement! 
# 	if not word in wordList:
# 		return False
# 
# 	wordFreq = getFrequencyDict(word)
# 	print(wordFreq)
# 	for char in wordFreq:
# 		if wordFreq[char] > hand.get(char, 0):
# 			return False
## 	
## 	return True
#
#
#def play(hand, wordList, n):
#
#	totalScore = 0
#	handLength = calculateHandlen(hand)
#	print(handLength)
#
#	while handLength > 0:
#		# Display the hand
#		print("Current Hand:", end= ' ')
#		displayHand(hand)
#
#		playerInput = input("Enter word, or a '.' to indicate that you are #finished: ").lower()
#
#		if playerInput == '.':
#			break
#
#		else:
#			if not isValidWord(playerInput, hand, wordList):
#				print("Invalid word, please try again.")
#
#			else:
#				scoreEarned = getWordScore(playerInput, n)
#				totalScore += scoreEarned
#				print(str(playerInput) + " earned " + str(scoreEarned) + " #points.", end=" ")
#				print("Total: " + str(totalScore) + " points")
#				hand = updateHand(hand, playerInput)
#				handLength = calculateHandlen(hand)
#
#	if playerInput == '.' or handLength == 0:
#		return ("Total score: " + str(totalScore))
#
#
#

#
#print(play(hand, wordList, n))
##
#
#def play(wordList):
#	"""
#    Allow the user to play an arbitrary number of hands.
#
#    1) Asks the user to input 'n' or 'r' or 'e'.
#      * If the user inputs 'n', let the user play a new (random) hand.
#      * If the user inputs 'r', let the user play the last hand again.
#      * If the user inputs 'e', exit the game.
#      * If the user inputs anything else, tell them their input was invalid.
# 
#    2) When done playing the hand, repeat from step 1   
#    """
#
#	finished = False
#	lastHand = {}	
#	while not finished:
#		playerInput = input("Enter n to deal a new hand, r to replay the last #and, or e to end game: ")
#		if playerInput == 'n':
#			hand = dealHand(HAND_SIZE)
#			lastHand = hand.copy()
#			playHand(hand, wordList, HAND_SIZE)
#			
#
#		elif playerInput == 'r':
#			if lastHand == {}:
#				print ("You have not played a hand yet. Please play a new hand #first!")
#			else:
#				playHand(lastHand, wordList, HAND_SIZE)
#
#		elif playerInput == 'e':
#			finished = True
#
#		else:
#			print("Invalid command.")
#
#print(play(wordList))
#

def play(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

def play(wordList):
	playing = False
	lastHand = {}
	while not playing:
		playerInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

		if playerInput == 'e':
			playing = True

		elif playerInput == 'r':
			if lastHand == {}:
				print ("You have not played a hand yet. Please play a new hand first!")
			else:
				choosePlayer = input("Enter u to have yourself play, c to have the computer play: ")
				if choosePlayer == 'u':
					playHand(lastHand, wordList, HAND_SIZE)

				elif choosePlayer == 'c':
					compPlayHand(lastHand, wordList, HAND_SIZE)

				else:
					print('Invalid command.')

		elif playerInput == 'n':
			breakLoop = False
			while not breakLoop:
				choosePlayer = input("Enter u to have yourself play, c to have the computer play: ")

				if choosePlayer == 'u':
					hand = dealHand(HAND_SIZE)
					lastHand = hand.copy()
					playHand(hand, wordList, HAND_SIZE)
					break
				elif choosePlayer == 'c':
					hand = dealHand(HAND_SIZE)
					lastHand = hand.copy()
					compPlayHand(hand, wordList, HAND_SIZE)
					break
				else:
					print('Invalid command.')
		else:
			print("Invalid command.")


print(play(wordList))