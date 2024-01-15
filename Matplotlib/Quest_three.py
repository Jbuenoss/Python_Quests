import numpy as np
import matplotlib.pyplot as plt

lang = ["Go", "Java", "Python", "C#", "JS"]
vot = [52, 120, 157, 109, 201]

plt.bar(lang, vot, color='c', edgecolor="g", lw=2, width=0.6)
plt.title("Languages survey")
plt.xlabel("Languages")
plt.ylabel("Votes")

plt.show()