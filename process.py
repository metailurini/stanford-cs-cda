import sys, os

FILE_DATA = "data"
MONTHS = []

def read_data(file_name):
    return open(file_name).read().split('\n')


def retrieve_overal_data(data):
    global MONTHS
    MONTHS = [ i.split(',')[0] for i in data[3:] if i ]

    courses = [ [i] for i in data[2].split(',')[1:] ]

    appender = lambda datum: [
        courses[index].append(int(value))
        for index, value in enumerate(datum.split(',')[1:])
    ]

    for item in data[3:]:
        appender(item)

    data = { item[0]: item[1:] for item in courses }
    return data


def main():
    courses = {}
    [
        courses.update(
            retrieve_overal_data(
                read_data(os.path.join(FILE_DATA, name))
            )
        )
        for name in os.listdir('data')
    ]
    # print(MONTHS)
    keys = list(courses.keys())
    avgs = []

    [
        avgs.append([key, sum(courses[key]) / (len(courses[key]) + 1e-6)])
        for key in keys
    ]

    avgs.sort(key=lambda x: x[1], reverse=True)
    courses = [course[0] for course in avgs]

    print(courses[:3])


if __name__ == "__main__":
    main()
