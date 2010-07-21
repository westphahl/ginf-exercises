"""
    Author: Simon Westphahl <westphahl@gmail.com>
    Description: Brute-force implementation for solving the TSP.
    http://en.wikipedia.org/wiki/Travelling_salesman_problem
    License: Public Domain
"""

routes = []


def find_paths(node, cities, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(cities) == len(path)) and (cities[path[-1]].has_key(path[0])):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print path, distance
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (cities[city].has_key(node)):
            find_paths(city, dict(cities), list(path), distance)


if __name__ == '__main__':
    cities = {
        'SR': {'R': 15, 'SF': 18},
        'R': {'SR': 15, 'O': 15},
        'SF': {'SR': 18, 'O': 12, 'SM': 20, 'P': 15},
        'O': {'R': 15, 'SF': 12, 'H': 20},
        'P': {'SF': 15, 'HMB': 15},
        'HMB': {'P': 15, 'SCR': 50, 'SM': 25},
        'SCR': {'HMB': 50, 'SV': 10, 'W': 70},
        'W': {'SCR': 70, 'SJ': 60},
        'SV': {'SCR': 10, 'SCL': 35},
        'SCL': {'SV': 35, 'SJ': 15, 'PA': 10},
        'SJ': {'SCL': 15, 'W': 60, 'F': 20},
        'F': {'SJ': 20, 'PA': 15, 'H': 14},
        'PA': {'SCL': 10, 'F': 15, 'SM': 18},
        'SM': {'HMB': 25, 'SF': 20, 'H': 20, 'PA': 18},
        'H': {'F': 14, 'SM': 20, 'O': 20},
    }

    print "Start: San Francisco"
    find_paths('SF', cities, [], 0)
    print "\n"
    routes.sort()
    if len(routes) != 0:
        print "Shortest route: %s" % routes[0]
    else:
        print "FAIL!"
