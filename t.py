Thresholds = [73 ,109 ,136 ,160 ,188]  #Thresholds
Thresholds.append(256)
Thresholds.insert(0, 0)

hist = []               
for i in range(256):
    hist.append(int(input()))             #Taking histogram input from a text file
s = sum(hist)
for i in range(len(hist)):
    hist[i] = hist[i] / s

cumulative_sum = []   #declaractions
cumulative_mean = []
global_mean = 0
Sigma = 0

for i in range(len(Thresholds)-1):
    cumulative_sum.append(sum(hist[Thresholds[i]:Thresholds[i + 1]])) # Cumulative sum of each Class 
    
    cumulative = 0
    for j in range(Thresholds[i], Thresholds[i + 1]):
        cumulative = cumulative + j * hist[j]
    
    cumulative_mean.append(cumulative / cumulative_sum[-1])           # Cumulative mean of each Class
     
    global_mean = global_mean + cumulative                            # Global Intensity Mean
    
for i in range(len(cumulative_mean)):                                 # Computing Sigma
    Sigma = Sigma + (cumulative_sum[i] * ((cumulative_mean[i] - global_mean)** 2))
    
print(Sigma)

