#6) მომხარებელს შემოატანინე სტრინგი. შეამოწმე — სულ დიდი ასოებით არის თუ არა. თუ არის დაპრინტე "string  is uppercase", სხვა შემთხვევაში "string is lowercase"

text = input("enter some text: ")
if text.isupper():
    print("string is uppercase")
else:
    print("string is lowercase")