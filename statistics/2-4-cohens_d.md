[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

This gave a Cohen's D of -.08, which indicates to me that there is not a sizable difference in the standard variation in the two groups. Code is below.

def cohens_d_birthorder():
    data = nsfg.ReadFemPreg()

    first_borns = data[data.birthord == 1]
    non_firsts = data[data.birthord != 1]

    first_born_avg_weight = first_borns.totalwgt_lb.mean()
    non_firsts_avg_weight = non_firsts.totalwgt_lb.mean()
    diff = first_born_avg_weight - non_firsts_avg_weight

    first_borns_var = first_borns.totalwgt_lb.var()
    non_firsts_var = non_firsts.totalwgt_lb.var()

    first_borns_count = len(first_borns)
    non_firsts_count = len(non_firsts)

    total_var = (first_borns_count * first_borns_var + non_firsts_count * non_firsts_var)/(first_borns_count + non_firsts_count)

    final = diff/math.sqrt(total_var)
    return final

print(cohens_d_birthorder())


