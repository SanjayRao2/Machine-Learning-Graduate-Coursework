import csv

def loadInvestments(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        data = []
        for row in reader:
            name = row[1]
            jan_2020 = int(row[-1])
            increase = jan_2020-int(row[276])
            data.append([name, jan_2020, increase])
    return data

def optimizeInvestments(data, budget, smallest_increment):
    n = len(data)
    num_increments = budget // smallest_increment
    dp = [[0] * (num_increments + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, price, profit = data[i - 1]
        for j in range(1, num_increments + 1):
            if price // smallest_increment > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - price // smallest_increment] + profit)

    max_profit = dp[n][num_increments]
    cities = []
    j = num_increments
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            name, _, _ = data[i - 1]
            cities.append(name)
            j -= data[i - 1][1] // smallest_increment

    return max_profit, cities





data = loadInvestments("metro.csv")
profit, cities = optimizeInvestments(data, 1000000, 1000)
print("Maximum Profit:", profit)
print("cities:", cities)



#ans
# Maximum Profit: 102203
# Selected Names: ['Baraboo, WI',
#                   'Idaho Falls, ID',
#                   'Joplin, MO',
#                   'Tyler, TX',
                    #'Yakima, WA']