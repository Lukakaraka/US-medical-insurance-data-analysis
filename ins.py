import csv

ins_file = r"C:\Users\Korisnik\PycharmProject\konvertori\medicalinscost\insurance.csv"
#converts the file to a dictionary (which we won't use because we don't need it)
with open(ins_file, newline = '') as csv_file:
    csv_file.readline()
    reader = csv.reader(csv_file)
    my_list = []
    for row in reader:
        my_list.append(row)
    main_dict = {}
    for i in range(len(my_list)):
        main_dict[i] = {"age": int(my_list[i][0]), "sex": my_list[i][1], "bmi": float(my_list[i][2]), "children": int(my_list[i][3]), "smoker": my_list[i][4], "region": my_list[i][5], "charges": float(my_list[i][6])}
    
#lists which we will use because I like lists
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

for i in range(len(my_list)):
    age.append(int(my_list[i][0]))
    sex.append(my_list[i][1])
    bmi.append(float(my_list[i][2]))
    children.append(int(my_list[i][3]))
    smoker.append(my_list[i][4])
    region.append(my_list[i][5])
    charges.append(float(my_list[i][6]))

#average value in a list with integers or floats
def avg(list):
    all = 0
    for i in list:
        all += i
    return all / len(list)

#median value in a list with integers or floats
def median(list):
    list.sort()
    half_len = len(list) / 2
    return list[int(half_len)]

smoker_non_smoker_charges = [list(i) for i in zip(smoker, charges)]

#smoker and non-smoker charges (can be used to compare the avg cost for both)
smoker_charges = []
non_smoker_charges = []

for i in smoker_non_smoker_charges:
    if i[0] == "no":
        non_smoker_charges.append(i[1])
    else:
        smoker_charges.append(i[1])

smoker_bmi_age_sex_children = [list(i) for i in zip(smoker, bmi, age, sex, children)]

#random lists whcich can be used
smoker_bmi = []
non_smoker_bmi = []
smoker_age = []
non_smoker_age = []
smoker_sex = []
smoker_children = []
non_smoker_children = []

for i in smoker_bmi_age_sex_children:
    if i[0] == "no":
        non_smoker_bmi.append(i[1])
        non_smoker_age.append(i[2])
        non_smoker_children.append(i[4])
    else:
        smoker_bmi.append(i[1])
        smoker_age.append(i[2])
        smoker_sex.append(i[3])
        smoker_children.append(i[4])

male_smokers = []
female_smokers = []

for i in smoker_sex:
    if i == 'male':
        male_smokers.append(i)
    else:
        female_smokers.append(i)

bmi_charges = [list(i) for i in zip(bmi, charges)]

underweight = []
healthy = []
overweight = []
obese = []

for i in bmi_charges:
    if i[0] < 18.5:
        underweight.append(i[1])
    elif i[0] >= 18.5 and i[0] < 25.0:
        healthy.append(i[1])
    elif i[0] >= 25.0 and i[0] < 30.0:
        overweight.append(i[1])
    elif i[0] >= 30.0:
        obese.append(i[1])

#example how you could use the lists to see the differences between groups of people

print(avg(healthy)) #prints 10409.34 (that's the cost)
print(avg(obese)) #prints 15552.33 (that's the cost)

#I could make analytics all day with this so i decided to stop here