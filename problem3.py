def problem3_1(txtfilename):
    f = open(txtfilename)
    sum = 0
    for line in f:
        print(line, end = "")
        sum = sum + len(line)
    print ("\n",end = "")
    print(sum)
    
nlis = [23,64,23,46,12,24]          # list
atup = ("c","e","a","d","b")        # tuple
str1 = "Rumplestilskin"             # string

def problem3_2(collection):
    for i in collection:
        print(i)

def problem3_3(month, day, year):
    months = ("January", "February", "March","April","May","June","July","August","September","October","November","December")
    print(months[int(month)-1],str(day) + ", " + str(year))
    
dic = {"January":1 , "February":2 , "March":3 ,"April" : 4,"May" : 5,"June" : 6,"July":7,"August":8,"September":9,
       "October":10,"November":11,"December":12}
def problem3_4(mon, day, year):
    print(str(dic[mon])+"/"+str(day)+"/"+str(year))

def problem3_5(name):  
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241","james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    print(phone_numbers[name])
    
def problem3_7(csv_pricefile, flower):
    import sys 
    import csv
    infile = open(csv_pricefile)
    for row in csv.reader(infile):
        if flower == row[0] :
            print(row[1])
    infile.close()    
    

