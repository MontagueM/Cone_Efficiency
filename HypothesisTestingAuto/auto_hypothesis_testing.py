import math

# Defining vars
hyp_sided = ""
hyp_null_prob = ""
drv = ""
trials = ""
sig_level = ""
# Defining functions''-['''''''''


def ncr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def binomial(n,r):
    b = ncr(n, r)*(hyp_null_prob**r)*((1-hyp_null_prob)**(trials-r))
    return b

def binomial_cumulative(n, r):
    sum = 0
    for i in range(0, r+1):
        sum += binomial(n, i)
    return sum


def start(sided):
    print("Let X be the DRV that represents", drv + ".")
    print("\nX ~ B(" + str(trials) + ",", str(hyp_null_prob) + ")")
    print("\nH0: p =", str(hyp_null_prob) + "                        H1: p", sided, str(hyp_null_prob))
    print("\nLet c be the critical value.\n")


def lower_side():
    print("P(X<=c) <", sig_level_dec)

    critical_value = 0
    for i in range(0, trials+1):
        b = binomial_cumulative(trials, i)
        if b > sig_level_dec:
            critical_value = i-1
            critical_value_above = i
            break
    print("P(X<=" + str(critical_value) + ") =", str(format(binomial_cumulative(trials, critical_value), '.4f')))
    print("P(X<=" + str(critical_value_above) + ") =", str(format(binomial_cumulative(trials, critical_value_above), '.4f')))
    print("\nc =", str(critical_value))


def upper_side():
    print("P(X>=c) <", sig_level_dec)
    print("1-P(X<=c-1) <", sig_level_dec)
    print("P(X<=c-1) >", 1-sig_level_dec)

    critical_value = 0
    for i in range(0, trials+1):
        b = binomial_cumulative(trials, i)
        if b > (1-sig_level_dec):
            critical_value = i
            critical_value_below = i-1
            break
    print("P(X<=" + str(critical_value) + ") =", str(ncr(trials, critical_value)*(hyp_null_prob**critical_value)*((1-hyp_null_prob)**(trials-critical_value))))
    print("P(X<=" + str(critical_value_below) + ") =", str(ncr(trials, critical_value_below)*(hyp_null_prob**(critical_value_below))*((1-hyp_null_prob)**(trials-critical_value_below))))
    print("\nc-1 =", str(critical_value))
    print("c =", str(critical_value+1))



easy_mode_enabled = input("Easy or complex mode? (e/c, new users select e): ")


if easy_mode_enabled == 'e':
    hyp_sided = input("\nLower/Upper/Two Sided test? (l/u/t): ")
    hyp_null_prob = float(input("\nNull hypothesis prob (e.g. 0.5) = "))
    drv = input("\nWhat is the variable (e.g. number of heads thrown): ")
    trials = int(input("\nHow many trials? "))
    sig_level = float(input("\nWhat is the level of significance in %? "))

    sig_level_dec = sig_level/100

    print("\n--------------------------------------------------------------------------------\n")

    if hyp_sided == "l":
        start("<")
        lower_side()
    elif hyp_sided == "u":
        start(">")
        upper_side()
    elif hyp_sided == "t":
        start("!=")
        sig_level_dec = sig_level_dec / 2
        print("\nLower:\n")
        lower_side()
        print("\nUpper:\n")
        upper_side()
