#Select one of the N bins uniformly at random, and place the current ball in it
import random 
import numpy as np 
import matplotlib.pyplot as plt




def plot_histogram(bins, filename = None):
  """
  This function wraps a number of hairy matplotlib calls to smooth the plotting 
  part of this assignment.

  Inputs:
  - bins:   numpy array of shape max_bin_population X num_strategies numpy array. For this 
        assignment this must be 200000 X 4. 
        WATCH YOUR INDEXING! The element bins[i,j] represents the number of times the most 
        populated bin has i+1 balls for strategy j+1. 
  
  - filename: Optional argument, if set 'filename'.png will be saved to the current 
        directory. THIS WILL OVERWRITE 'filename'.png
  """
  assert bins.shape == (200000,4), "Input bins must be a numpy array of shape (max_bin_population, num_strategies)"
  assert np.array_equal(np.sum(bins, axis = 0),(np.array([30,30,30,30]))), "There must be 30 runs for each strategy"

  thresh =  max(np.nonzero(bins)[0])+3
  n_bins = thresh
  bins = bins[:thresh,:]
  print "\nPLOTTING: Removed empty tail. Only the first non-zero bins will be plotted\n"

  ind = np.arange(n_bins) 
  width = 1.0/6.0

  fig, ax = plt.subplots()
  rects_strat_1 = ax.bar(ind + width, bins[:,0], width, color='yellow')
  rects_strat_2 = ax.bar(ind + width*2, bins[:,1], width, color='orange')
  rects_strat_3 = ax.bar(ind + width*3, bins[:,2], width, color='red')
  rects_strat_4 = ax.bar(ind + width*4, bins[:,3], width, color='k')

  ax.set_ylabel('Number Occurrences in 30 Runs')
  ax.set_xlabel('Number of Balls In The Most Populated Bin')
  ax.set_title('Histogram: Load on Most Populated Bin For Each Strategy')

  ax.set_xticks(ind)
  ax.set_xticks(ind+width*3, minor = True)
  ax.set_xticklabels([str(i+1) for i in range(0,n_bins)], minor = True)
  ax.tick_params(axis=u'x', which=u'minor',length=0)

  ax.legend((rects_strat_1[0], rects_strat_2[0], rects_strat_3[0], rects_strat_4[0]), ('Strategy 1', 'Strategy 2', 'Strategy 3', 'Strategy 4'))
  plt.setp(ax.get_xmajorticklabels(), visible=False)
  
  if filename is not None: plt.savefig(filename+'.png', bbox_inches='tight')

  plt.show()
#input:
#output: number of balls in the most populated bin
def strategy_one(N):
	#initialize bins as list of zeros 
  bins = [0] * N
  #for N balls, generate random bin # to place it into and increment count of bin 
  for i in range(N):
    randomBin = random.randint(0, N-1) #inclusive 
    bins[randomBin] += 1
  #find number of balls in most populated bin
  return max(bins)
  
  
  
  
'''
Select two of the N bins uniformly at random (either with or without replacement), and look at how
many balls are already in each. If one bin has strictly fewer balls than the other, place the current ball
in that bin. If both bins have the same number of balls, pick one of the two at random and place the
current ball in it.
'''

def strategy_two(N):
  bins = [0] * N
  
  for i in range(N):
    #select two bins at random
    firstRandomBin = random.randint(0, N-1)
    secondRandomBin = random.randint(0, N-1)
    #find if one of them has a strictly lower count
    firstBinCount = bins[firstRandomBin]
    secondBinCount = bins[secondRandomBin]
    if (firstBinCount < secondBinCount):
      bins[firstRandomBin] += 1
    if (secondBinCount < firstBinCount):
      bins[secondRandomBin] += 1
      
    #if both bins have the same count, select one randomly 
    else:
      randBin = random.randint(0, 1)
      if randBin == 0:
        bins[firstRandomBin] += 1
      else:
        bins[secondRandomBin] += 1
        
  return max(bins)


'''
Same as the previous strategy, except choosing three bins at random rather than two.
'''
def strategy_three(N):
  bins = [0] * N
  
  for i in range(N):
	  #select three bins at random
	  firstRandomBin = random.randint(0, N-1)
	  secondRandomBin = random.randint(0, N-1)
	  thirdRandomBin = random.randint(0, N-1)


	  firstBinCount = bins[firstRandomBin]
	  secondBinCount = bins[secondRandomBin]
	  thirdBinCount = bins[thirdRandomBin]
	  
	  if(firstBinCount < secondBinCount and firstBinCount < thirdBinCount):
	    bins[firstRandomBin] += 1
	  elif(secondBinCount < firstBinCount and secondBinCount < thirdBinCount):
	    bins[secondRandomBin] += 1
	  elif(thirdBinCount < firstBinCount and thirdBinCount < secondBinCount):
	  	bins[thirdRandomBin] += 1
	  else:
	    options = []
	    if(firstBinCount == secondBinCount):
	      if(firstBinCount == thirdBinCount):
	        options.append(firstRandomBin)
	        options.append(secondRandomBin)
	        options.append(thirdRandomBin)
	      else:
	        options.append(firstRandomBin)
	        options.append(secondRandomBin)
	    elif(firstBinCount == thirdBinCount):
	      options.append(firstBinCount)
	      options.append(thirdBinCount)
	    elif(secondBinCount == thirdBinCount):
	      options.append(secondBinCount)
	      options.append(thirdBinCount)
	      
	      
	    numOptions = len(options)
	    randomPick = random.randint(0, numOptions-1)
	    if(randomPick == 0):
	      bins[firstRandomBin] += 1
	    elif(randomPick == 1):
	      bins[secondRandomBin] += 1
	    else:
	      bins[thirdRandomBin] += 1
  return max(bins)
        
    
    

    
def strategy_four(N):
  bins = [0] * N 
  boundary = N/2
  
  for i in range(N):
	#select 2 random bins from appropriate ranges 
	firstRandomBin = random.randint(0, N/2 - 1)
	secondRandomBin = random.randint(N/2, N - 1)
	#increment first bin if equal or has fewer balls 
	if (bins[firstRandomBin] <= bins[secondRandomBin]):
		bins[firstRandomBin] += 1
	else:	
		bins[secondRandomBin] += 1
    

  return max(bins)




#HMMM can we get a double check on whether our indexing is correct?
#WATCH YOUR INDEXING! The element bins[i,j] represents the number of times the most populated bin has i+1 balls for strategy j+1. 
histogramArray = np.zeros((200000, 4))
for i in range(30):
  firstStrategyIndex = strategy_one(200000)
  secondStrategyIndex = strategy_two(200000)
  thirdStrategyIndex = strategy_three(200000)
  fourthStrategyIndex = strategy_four(200000)

  histogramArray[firstStrategyIndex - 1][0] += 1
  histogramArray[secondStrategyIndex - 1][1] += 1
  histogramArray[thirdStrategyIndex - 1][2] += 1
  histogramArray[fourthStrategyIndex - 1][3] += 1



plot_histogram(histogramArray)
