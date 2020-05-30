import numpy as np
from PIL import Image

def Otsu(Thresholds,image):
    Thresholds.append(256)
    Thresholds.insert(0, 0)
    Thresholds.sort()
    img = Image.open(image).convert("L")
    img=np.asarray(img)

    hist = [0] * 256               
    for i in range(len(img)):
        for j in range(len(img[0])):
            hist[int(img[i][j])] += 1

    Total_Pixels = len(img)*len(img[0])

    for i in range(len(hist)):                                              # Probabilities
        hist[i] = hist[i] / Total_Pixels

    cumulative_sum = []                                                     # declaractions
    cumulative_mean = []
    global_mean = 0
    Sigma = 0

    for i in range(len(Thresholds)-1):
        cumulative_sum.append(sum(hist[Thresholds[i]:Thresholds[i + 1]]))   # Cumulative sum of each Class

        cumulative = 0
        for j in range(Thresholds[i], Thresholds[i + 1]):
            cumulative = cumulative + (j + 1) * hist[j]
           
        cumulative_mean.append(cumulative / cumulative_sum[-1])             # Cumulative mean of each Class

        global_mean = global_mean + cumulative                              # Global Intensity Mean

    for i in range(len(cumulative_mean)):                                   # Computing Sigma
        Sigma = Sigma + (cumulative_sum[i] *
                        ((cumulative_mean[i] - global_mean) ** 2))

    return(Sigma)
