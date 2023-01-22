print ('welcom to my calcouter mohammad amiri ')

work = input ('whate do you want:=> ')
if work == '*':
     name =input('number:=> ')
     name2 =input('number: ')
     name = float(name)
     name2 =float(name2)
     print (name * name2)

elif work =='/' :
  name =input('number: ')
  name2 =input('number: ')
  name = float(name)
  name2 =float(name2)
  print (name / name2)

elif work =='+':
  name =input('number: ')
  name2 =input('number: ')
  name = float(name)
  name2 =float(name2)
  print (name + name2) 
elif work =='-':
  name =input('number: ')
  name2 =input('number: ')
  name = float(name)
  name2 =float(name2)
  print (name - name2) 

elif work=='%':
   name =input('enter number :=>   ')
   name2 = input('enter nuber2:=>  ')
   name = float(name)
   name2 =float(name2)     
   print(name%name2) 

else:
    print( 'لطفا گزینه درست انتخاب کنید ')