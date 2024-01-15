import numpy as np
import matplotlib.pyplot as plt

profit = np.random.normal(1.2, 0.2, 60)
profit_ticks = np.arange(0.0, 2.2, 0.2)
x = np.arange(1, 61, 1)     

plt.plot(x, profit, c='green', linestyle='--', lw=1.5)
plt.yticks(profit_ticks, [f"${x:.1f} million" for x in profit_ticks])   #definir para evitar sobreposições
plt.title("Company profit")
plt.xlabel("Months")
plt.ylabel("Profit")


plt.show()