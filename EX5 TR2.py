odef=int(input("enter the odef you want to get:"))
o100=odef//100
odef-=odef//100*100
o50=odef//50
odef-=odef//50*50
o20=odef//20
odef-=odef//20*20
o10=odef//10
odef-=odef//10*10
o5=odef//5
odef-=odef//5*5
o1=odef//1
print("Change is composed of :", o100 ,"X 100 bills", o50 ,"X 50 bills",o10,"X 10 coins",o5,"X 5 coins",o1,"X 1 coins")
