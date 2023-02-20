from data import geo_logs, ids, stats
from collections import Counter


def geo_log(city):
    res = [geo_list for geo_list in geo_logs for visits, geo in geo_list.items() for country in geo if country == city]
    return res


def unique_val(some_list=ids):
    vals = [value for nums in some_list.values() for value in nums]
    return sorted(set(vals), key=vals.index)


def chanal(some_dict=stats):
    return max(some_dict, key=some_dict.get)

if __name__ == '__main__':

    print(type(*unique_val()))
