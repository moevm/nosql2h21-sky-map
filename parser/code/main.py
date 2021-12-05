import json

filename = 'data.txt'
out_file = open("test2.json", "w")
dict1 = {}

# fields_orig = ['pgc', 'objname', 'objtype', 'modbest', 'l2', 'b2', 'bar', 'multiple', 'ring', 'compactness', 'logdc',
#           'brief', 'v']

fields = ['pgc', 'name', 'type', 'distance', 'galactic_longitude', 'galactic_latitude', 'barred', 'multiple',
          'rings', 'compact', 'diameter_log', 'brightness', 'radial_speed']

coords = ['distance', 'galactic_longitude', 'galactic_latitude']

galactic_info = ['barred', 'multiple', 'rings', 'compact', 'diameter_log']

out_file.write("[")  # i'm not sure if it's ok

with open(filename) as fh:
    l = 1

    for line in fh:
        description = list(line.strip("\n").replace(" ", "").split(";"))
        if len(description) != len(fields):
            continue
        sno = 'emp' + str(l)
        i = 0
        dict2 = {}
        dict3 = {}
        dict4 = {}
        while i < len(fields):
            if i == 3:
                for j in range(len(coords)):
                    dict3[coords[j]] = description[i]
                    i = i + 1
                dict2['coords'] = dict3
            elif i == 6:
                for j in range(len(galactic_info)):
                    if galactic_info[j] == 'diameter_log':
                        dict4[galactic_info[j]] = description[i]
                    elif description[i] != "":
                        dict4[galactic_info[j]] = True
                    else:
                        dict4[galactic_info[j]] = False
                    i = i + 1
                dict2['galactic_info'] = dict4
            else:
                dict2[fields[i]] = description[i]
                i = i + 1

        #print("wtf")
        #dict1[sno] = dict2
        json.dump(dict2, out_file)
        l = l + 1
        if l % 100000 == 0:
            print(l)

        # if l > 1000:
        #     break
        if l == 5300000:
            break
        out_file.write(",")  # i'm not sure if it's ok


#json.dump(dict1, out_file, indent=2)
out_file.write("]")  # i'm not sure if it's ok
out_file.close()
