import re
import csv

def count_degrees(csv_file_name):
    degree_dict = dict()
    with open(csv_file_name, "rb") as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(file_reader)
        for row in file_reader:
            standard_name= re.sub('[.]', '', row[1])
            if standard_name[0] == " ":
                standard_name = standard_name[1:]
            degrees = standard_name.split(" ")
            for degree in degrees:
                if degree not in degree_dict:
                    degree_dict[degree] = 1
                else:
                    degree_dict[degree] += 1
        if '0' in degree_dict:
            del degree_dict['0']
    return degree_dict



print count_degrees('faculty.csv')