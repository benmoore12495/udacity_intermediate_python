# ==================================
# Step 1:
# ==================================

def data_discovery(neos,cads):

    # - How many NEOs are in the `neos.csv` data set? DONE
    print('1a answer: ' + str(len(neos)))

    # - What is the primary designation of the first Near Earth Object in the `neos.csv` data set?
    print('1b answer: ' + str(neos[1][2]))

    # - What is the diameter of the NEO whose name is "Apollo"?
    for k,v in neos.items():
        if v[3] == 'Apollo':
            print('1c Apollo diameter: '+ str(v[15]))
        else:
            pass

    # - How many NEOs have IAU names in the data set?
    num = 0
    for k,v in neos.items():
        if len(v[3]) > 0:
            num += 1
        else:
            pass
    print('1d number of neos with a non null name: ' + str(num))

    # - How many NEOs have diameters in the data set?
    num = 0
    for k,v in neos.items():
        if len(v[15]) > 0:
            num += 1
        else:
            pass
    print('1e number of neos with a non null diameter: ' + str(num))

    # - How many close approaches are in the `cad.json` data set?
    print('1f number of cads: ' + str(cads['count']))

    # - On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?
    data = cads['data']
    for d in data:
        date = d[3]
        pdes = d[0]
        dist = d[4]
        if date.startswith('2000-Jan-01') and pdes == '2015 CL':
            print('1g Distance from earth of 2015 CL Jan 1, 2000: ' + str(dist))
        else:
            pass

    # - On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?
    for d in data:
        date = d[3]
        pdes = d[0]
        speed = d[7]
        if date.startswith('2000-Jan-01') and pdes == '2002 PB':
            print('1h Speed of 2002 PB Jan 1, 2000: ' + str(speed))
        else:
            pass
