[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The distribution seems to be uniform for the CDF and not for the PMF.

random_nums = np.random.random(1000)
pmf = thinkstats2.Pmf(random_nums)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='Random var
cdf = thinkstats2.Cdf(random_nums)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random variate', ylabel='PMF')