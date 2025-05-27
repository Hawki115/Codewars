def abbrev_name(name):
     
    parts1 = name.split()
    first_inital = parts1[0][0].upper()
    second_inital=parts1[1][0].upper()
    return first_inital + '.' + second_inital