
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ym = pd.read_excel('features.xlsx')
#label = ym.iloc(1:,1:2)

filler = [0,
35,
2,
5,
6,
15,
21,
34,
11,
10,
7,
19,
9,
34,
9,
41,
50,
18,
13,
23
]
#filler = (int)filler
print(filler)
index = np.arange(len(filler))
print(index)
plt.subplot(1,2,1)
plt.bar(index, filler)
plt.xlabel('Participants', fontsize=10)
plt.ylabel('No of Filler Words', fontsize=10)
plt.xticks(range(1,20))
plt.title('No of Filler Words:')

pos = [0,
5,
5,
4,
2,
1,
1,
5,
1,
1,
1,
5,
8,
10,
19,
13,
19,
17,
15,
21
]
plt.subplot(1,2,2)
plt.bar(index, pos)
plt.xlabel('Participants', fontsize=10)
plt.ylabel('Positive Emotion Representing Word count', fontsize=10)
plt.xticks(range(1,20))
plt.title('Positive Emotions')

plt.show()

#ym1 = pd.read_excel('features.xlsx')
#label = ym.iloc(1:,1:2)

frequency = [0,
330.56469727,
342.03424072,
318.94616699,
339.22833252,
348.16061401,
327.65826416,
315.9491272,
332.8465271,
321.08102417,
321.08102417,
346.58441162,
347.5960083,
346.69580078,
348.4855957,
342.89096069,
342.89096069,
342.89080811,
342.89096069,
339.72341919
]
#filler = (int)filler
print(frequency)
index = np.arange(len(frequency))
print(index)
plt.subplot(1,2,1)
plt.bar(index, filler)
plt.xlabel('Participants', fontsize=10)
plt.ylabel('Maximum of the fundamental frequency in Hz', fontsize=10)
plt.xticks(range(1,20))
plt.title('Maximum of the fundamental frequency')

pause_dur = [0,
266.2739726,
250.47058824,
212.53012048,
248.80681818,
274.0397351,
221.96581197,
169.36170213,
562.91970803,
277.87234043,
277.87234043,
188.20754717,
167.86764706,
228.35714286,
355.91280654,
286.10619469,
286.10619469,
286.10619469,
286.10619469,
197.03504043
]
plt.subplot(1,2,2)
plt.bar(index, pos)
plt.xlabel('Participants', fontsize=10)
plt.ylabel('Average duration of pauses', fontsize=10)
plt.xticks(range(1,20))
plt.title('Average Pause Duration')

plt.show()
