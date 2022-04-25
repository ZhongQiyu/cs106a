# Data comes from Johns Hopkins University
# https://github.com/CSSEGISandData/COVID-19
# Thanks to them for making this data set public.
# You can find data beyond cumulative cases there!

'''
Test your code by analysing total confirmed cases over time.
Each line in the file represents one day. The first value is
confirmed cases on January 22nd. The number of confirmed cases
is "cumulative" meaning that it is the total number of cases up
until the current day. It will never go down! 
'''

COUNTRY_PATH = 'countries/Italy.txt'

def main():
    # load the file
    country_data = open(COUNTRY_PATH)
    # Challenge #1
    data_list = []
    for line in country_data:
        data_point = int(line.strip())
        data_list.append(data_point)
    print("The list of data points is:", data_list)
    print()
    # Challenge #2
    non_zero_count = 0
    for data_point in data_list:
        if data_point != 0:
            non_zero_count += 1
    print("There are %d data points in the list." % len(data_list))
    print("There are %d data points that are non-zero." % non_zero_count)
    print()
    # Challenge #3
    new_cases = []
    iter_count = len(data_list) - 1  # guess why?
    for i in range(iter_count):
        new_cases.append(data_list[i+1] - data_list[i])
    print("The list of new cases is:", new_cases)

if __name__ == '__main__':
    main()
