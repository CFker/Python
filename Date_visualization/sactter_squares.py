import matplotlib.pyplot as plt

x_value = list(range(1, 50))
print(x_value)
y_value = [x**3 for x in x_value]
print(y_value)
plt.scatter(x_value, y_value, c=y_value, edgecolors='none', s=20)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
# plt.axis([0, 5000, 0, 11000000])

plt.savefig('squares_plot.png', bbox_inches='tight')
