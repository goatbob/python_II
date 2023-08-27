"""
program: insurance_quote_assignment.py
author: kyle godwin
last date modified: 27 august 2023
"""


def ins_rate_calc(age, coverage):

    if int(age) < 25:
        if coverage == "state minimum":
            cost = 2593
        elif coverage == "liability":
            cost = 2957
        elif coverage == "full":
            cost = 6930
    elif int(age) < 35:
        if coverage == "state minimum":
            cost = 608
        elif coverage == "liability":
            cost = 691
        elif coverage == "full":
            cost = 1745
    elif int(age) < 45:
        if coverage == "state minimum":
            cost = 552
        elif coverage == "liability":
            cost = 627
        elif coverage == "full":
            cost = 1564
    elif int(age) < 55:
        if coverage == "state minimum":
            cost = 525
        elif coverage == "liability":
            cost = 596
        elif coverage == "full":
            cost = 1469
    elif int(age) < 65:
        if coverage == "state minimum":
            cost = 494
        elif coverage == "liability":
            cost = 560
        elif coverage == "full":
            cost = 1363
    else:
        if coverage == "state minimum":
            cost = 515
        elif coverage == "liability":
            cost = 585
        elif coverage == "full":
            cost = 1402

    return cost


if __name__ == "__main__":
    n = input("Enter name: ")
    a = input("Enter age: ")
    c = input("Enter coverage level (state minimum, liability, full): ")\

    cust = {"Name": n, "Age": a, "Coverage": c}

    rate = ins_rate_calc(a, c)
    cust["Coverage Cost"] = rate

    acc = input("Have you ever been in an accident (y/n): ")
    if acc == "y":
        cust["Coverage Cost"] = cust["Coverage Cost"] * 1.41

    disc = input("Would you like to pay now for a 10% discount (y/n): ")
    if acc == "y":
        cust["Coverage Cost"] = cust["Coverage Cost"] * 0.90
    
    print(f"${cust['Coverage Cost']:.2f}")
