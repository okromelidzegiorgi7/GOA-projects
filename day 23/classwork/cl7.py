#7) მომხარებელს შემოატანინე სტრინგი. შეამოწმე — სულ პატარა ასოებით არის თუ არა. თუ არის დაპრინტე "string is lowercase", სხვა შემთხვევაში "string is uppercase"


text = input("enter some text: ")
if text.islower():
   print("string is lowercase")
else:
    print("string is uppercase")