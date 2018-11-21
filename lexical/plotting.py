
import matplotlib.pyplot as plt
import pandas as pd

ym = pd.read_excel('turker_scores.xlsx')
paused =ym.iloc[1:,12:13]
print(paused)
confidence = ym.iloc[1:,13:14]
speaking_rate = ym.iloc[1:,11:12]
friendliness = ym.iloc[1:,4:5]
hiring = ym.iloc[1:,2:3]
plt.subplot(221)
plt.xticks(range(1,20))
plt.plot(confidence,label="confidence")
plt.plot(hiring,label="recommended hiring")
plt.legend()
#plt.title('confidence')
plt.subplot(222)
plt.plot(paused,label="pause rate")
plt.plot(hiring,label="recommended hiring",)
plt.legend()
plt.xticks(range(1,20))
#plt.title('paused_rate')
plt.subplot(223)
plt.plot(speaking_rate,label="speaking rate")
plt.plot(hiring,label="recommended hiring")
plt.legend()
plt.xticks(range(1,20))
#plt.title('speaking rate')
plt.subplot(224)
plt.xticks(range(1,20))
plt.plot(friendliness,label="friendliness")
plt.plot(hiring,label="recommended hiring")
plt.legend()
#plt.title('freindliness')
plt.show()
