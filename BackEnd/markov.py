import random, re 

# freqDict is a dict of dict containing frequencies
def addToDict(fileName, freqDict):
	f = open(fileName, 'r')
	words = re.sub("\n", " \n", f.read()).lower().split(' ')
	#Hidden markov model constructed below
	# count frequencies curr -> succ
	for curr, succ in zip(words[1:], words[:-1]):
		# check if curr is already in the dict of dicts
		if curr not in freqDict:
			freqDict[curr] = {succ: 1}
		else:
			# check if the dict associated with curr already has succ
			if succ not in freqDict[curr]:
				freqDict[curr][succ] = 1
			else:
				freqDict[curr][succ] += 1

	# compute percentages
	probDict = {}
	for curr, currDict in freqDict.items():
		probDict[curr] = {}
		currTotal = sum(currDict.values())
		for succ in currDict:
			probDict[curr][succ] = currDict[succ] / currTotal
	return probDict

#choosing which ingredient to come next based on the probabilities
def markov_next(curr, probDict):
	if curr not in probDict:
		return random.choice(list(probDict.keys()))
	else:
		succProbs = probDict[curr]
		randProb = random.random()
		currProb = 0.0
		for succ in succProbs:
			currProb += succProbs[succ]
			if randProb <= currProb:
				return succ
		return random.choice(list(probDict.keys()))

#function responsible for actually creating a cocktail
def makeCocktail(curr, probDict, T = 4):
	cocktail = [curr]
	for t in range(T):
		cocktail.append(markov_next(cocktail[-1], probDict))
	return " ".join(cocktail)

if __name__ == '__main__':
	cocktailFreqDict = {}
	cocktailProbDict = addToDict('./Data/cocktails.txt', cocktailFreqDict)

	startWord = input("What do you want your cocktail to contain?\n > ")
	print("Alright, here's your cocktail:")
	print(makeCocktail(startWord, cocktailProbDict))