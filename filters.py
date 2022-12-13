def pull_on_dates(start_date,end_date,db):
    small_approaches = []
    for neo in db:
        for approach in neo.approaches:
            if approach.time >= start_date and approach.time < end_date:
                small_approaches.append(approach)
    return small_approaches


def pull_on_distance(min_d,max_d,db):
    small_approaches = []
    for neo in db:
        for approach in neo.approaches:
            if float(approach.distance) > float(min_d) and float(approach.distance) < float(max_d):
                small_approaches.append(approach)
    return small_approaches

def pull_on_velocity(min_v,max_v,db):
    small_approaches = []
    for neo in db:
        for approach in neo.approaches:
            if float(approach.velocity) > float(min_v) and float(approach.velocity) < float(max_v):
                small_approaches.append(approach)
    return small_approaches
