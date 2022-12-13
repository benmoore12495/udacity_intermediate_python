import datetime
from models import * 

def cd_to_datetime(calendar_date):
    return datetime.datetime.strptime(calendar_date, "%Y-%b-%d %H:%M")

def datetime_to_str(dt):
    return datetime.datetime.strftime(dt, "%Y-%m-%d")

def create_neo_db(neos,cads):

    neo_db = []
    i = 1
    for k,v in neos.items():
        if i > 1 and i < 4:
            class_inst = NearEarthObject(v[2]# pdes
                                        ,v[1]# name
                                        ,v[15]# diameter
                                        )
            neo_db.append(class_inst)
        else:
            pass
        i += 1

    print(neo_db)

    for i in range(len(cads['data'])):
        approach = cads['data'][i]
        approach_inst = CloseApproach(approach[0]# pdes
                                     ,datetime_to_str(cd_to_datetime(approach[3]))# time
                                     ,approach[4]# dist
                                     ,approach[7]# velocity
                                     )
        pdes_of_approach = approach[0]
        for neo in neo_db:
            if neo.pdes == pdes_of_approach:
                neo.add_approach(approach_inst)
            else:
                pass

    return neo_db
