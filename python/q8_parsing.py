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


path = '/Users/danielgilberg/data_science/metis/dsp/python/football.csv'
find_smallest_goal_difference(path)


def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values.
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    team_list = []
    with open(filename, "rb") as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(file_reader)
        for row in file_reader:
            team_list.append(",".join(row))
    return team_list


def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    current_low = 0
    current_low_index = 0
    for team in goals:
        current_diff = int(team.split(",")[5]) - int(team.split(",")[6])

        if abs(current_diff) < abs(current_low) or goals.index(team) == 0:
            current_low = current_diff
            current_low_index = goals.index(team)
    return current_low_index


def get_team(index_value, parsed_data):
    """Returns the team name at a given index.

    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above

    Returns: the team name
    """
    team_data = parsed_data[index_value]
    return team_data.split(",")[0]


footballTable = read_data('football.csv')
print footballTable
minRow = get_index_with_min_abs_score_difference(footballTable)
print minRow
print(str(get_team(minRow, footballTable)))