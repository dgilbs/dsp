[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Around 34% fit in this demographic.

import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
dist.cdf(mu-sigma)
low = dist.cdf(177.8)
high = dist.cdf(185.4)
print(low, high, high-low, dist)