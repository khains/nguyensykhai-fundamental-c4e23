print("Answer the following algebra question:")
ques = ["If x=8, then what is the value of 4(x + 3) ?",
"Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? "]
d = {
    "1" :[35, "about 55"],
    "2" :[36, "about 65"],
    "3" :[40, "about 75"],
    "4" :[44, "about 85"],
}
corr = ["4", "2"]
s = 0
for i in range(len(ques)):
    print(ques[i])
    for k,v in d.items():
        print(k,".", v[i])
    x = input("Your choice: ")
    if x in corr:
        print("Bingo")
        s+=1
    else:
        print(":(")
print("You correctly answer",s,"out of",len(ques),"questions")