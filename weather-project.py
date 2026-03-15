import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('weatherAUS.csv')
print("数据形状:",data.shape)
print(data.head(3))
temps = data['Temp3pm'].dropna().values
print(f"\n温度数据:{temps[:10]}")
print(f"平均:{np.mean(temps):.2f}")
plt.figure(figsize=(10,6))
plt.hist(temps, bins=30,color='skyblue',edgecolor='black')
plt.title('afternoon temperature distribution(3pm)',fontsize=14)
plt.xlabel('temperature',fontsize=12)
plt.ylabel('frequency',fontsize=12)
plt.grid(axis='y',alpha=0.75)
plt.savefig('temp_distribution.png',dpi=150)
plt.show()
print(f"\n统计分析:")
print(f"样本数:{len(temps)}")
print(f"平均值:{np.mean(temps):.2f}")
print(f"标准差:{np.std(temps):.2f}")
print(f"最高温:{np.max(temps):.2f}")
print(f"最低温:{np.min(temps):.2f}")