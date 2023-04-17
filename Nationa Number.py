National_number=input("please, Enter your National number \n")
if len(National_number)==14:
    print(National_number[5:7],end='/')
    print(National_number[3:5],end="/")
    if National_number[0]=='2':
        print("19",end=(""))
        print(National_number[1:3],end="")
    elif National_number[0]=='3':
        print("20",end="")
        print(National_number[1:3],end="")
    else:
        print("please, Enter date from 1900 to 2100")
else:
    print("please, Enter Valid id composed from 14 number")



