"""
This Test1.py will work for only for units/capacity of 160 units-3200units perfectly.
As of now this program wont work below 160 and above 3200
Test cases i did
    resourealloc(1150, 1)
    resourealloc(1110, 12)
    resourealloc(3200, 5)
    resourealloc(160, 12)

"""


def resourealloc(num, hours):
    NewYork = {'Large': (10, 120), 'XLarge': (20, 230), '2XLarge': (40, 450), '4XLarge': (80, 774),
               '8XLarge': (160, 1400),
               '10XLarge': (320, 2820)}
    India = {'Large': (10, 140), '2XLarge': (40, 413), '4XLarge': (80, 890), '8XLarge': (160, 1300),
             '10XLarge': (320, 2970)}
    China = {'Large': (10, 110), 'XLarge': (20, 200), '4XLarge': (80, 670), '8XLarge': (160, 1180)}

    def costeffec(NewYork, region):
        global t2name, t3name, t2cost, t3cost
        high = NewYork[list(NewYork.keys())[-1]][0]  # highest element in dic ie 320 here
        high2 = NewYork[list(NewYork.keys())[-2]][0]  # second highest element in dic ie 320 here
        # comparing cost effectiveness
        x = high // high2
        high2_cmp = (high2 * x) * NewYork[list(NewYork.keys())[-2]][1]
        high_cmp = high2 * NewYork[list(NewYork.keys())[-1]][1]
        if high2_cmp < high_cmp:
            t = high2
            tcost = NewYork[list(NewYork.keys())[-2]][1]
            tname = list(NewYork.keys())[-2]
        else:
            t = high
            tcost = NewYork[list(NewYork.keys())[-1]][1]
            tname = list(NewYork.keys())[-1]
        nunits_part1 = num // t
        machine = {}
        machine[tname] = nunits_part1
        reminder_part1 = num % t
        # the remaining
        if reminder_part1 != 0:
            n = len(NewYork)
            sumo = reminder_part1
            cnt = 0
            for i in range(0, n):
                for j in range(i + 1, n):
                    if NewYork[list(NewYork.keys())[i]][0] + NewYork[list(NewYork.keys())[j]][0] == sumo:
                        cnt += 1
                        t2name = list(NewYork.keys())[i]
                        t2cost = NewYork[list(NewYork.keys())[i]][1]
                        t3name = list(NewYork.keys())[j]
                        t3cost = NewYork[list(NewYork.keys())[j]][1]
                    machine[t2name] = 1
                    machine[t3name] = 1
            else:
                t2cost = 1
                t3name = list(NewYork.keys())[j]
                t3cost = 1

        # To find cost
        totalcost = (nunits_part1 * tcost * hours) + (t2cost * hours) + (t3cost * hours)
        outputNy = {}
        outputNy['region'] = region
        outputNy['totalcost'] = totalcost
        outputNy['machine'] = machine
        return outputNy

    output = [costeffec(NewYork, "Newyork"), costeffec(India, "India"), costeffec(China, "China")]
    result = {}
    result['output'] = output
    print(result)


# calling the function
resourealloc(1150, 1)
# Expected output {'output': [{'region': 'Newyork', 'totalcost': 9802, 'machine': {'8XLarge': 7, 'Large': 1,
# 'XLarge': 1}}, {'region': 'India', 'totalcost': 9102, 'machine': {'8XLarge': 7, 'Large': 1, '10XLarge': 1}},
# {'region': 'China', 'totalcost': 8262, 'machine': {'8XLarge': 7, 'Large': 1, 'XLarge': 1}}]}
