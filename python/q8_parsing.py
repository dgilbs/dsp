import csv

def find_smallest_goal_difference(file_path):
    difference = 0
    team = ""
    with open(file_path, "rb") as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(file_reader)
        for row in file_reader:
            goals_scored = row[5]
            goals_allowed = row[6]
            diff = int(goals_scored) - int(goals_allowed)
            if diff < difference:
                difference = diff
                team = row[0]
    print team


x = '/Users/danielgilberg/data_science/metis/dsp/python/football.csv'
find_smallest_goal_difference(x)


