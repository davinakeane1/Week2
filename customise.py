life_exp = [1,6,2,4,6,2,6,8]
gdp_cap = [974, 12779, 34435, 36126, 29796, 1391, 33692, 334292]

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
#plt.xlabel('GDP per Capita [in USD]')
#plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']


plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

