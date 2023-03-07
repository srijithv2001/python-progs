while True:
	print("1.List operation\n2.Sets opration\n3.Exit")
    ch1=int(input("Enter choice: "))
    if(ch1==1):
		n=int(input("Enter Length:"))
        l=[]
        ele=input("Enter elements")
        for i in range(0,n):
            	l.append(input())
        		print("List is:",l)
 	while True:
		print("1.append\n 2.insert\n 3.pop\n 4.remove\n 5.length\n 6.count\n 7.min \n8.sort\n 9.reverse \n10.clear")
        	ch=int(input("Enter the choice"))
		if ch==1:
                	e=input("Enter element")
                	l.append(e)
                	print("Element",e,"is appended successsfully")
                	print(l)
            	elif ch==2:
                	e=input("Enter element")
                	p=int(input("Enter position"))
                	l.insert(p,e)
                	print(e,"is inserted at ",p)
                	print(l)
            	elif ch==3:
               		print("popped element",l.pop())
            	elif ch==4:
                 	v=input("Enter value to remove")
                 	l.remove(v)
                 	print(l)
            	elif ch==5:
                	print(len(l))
            	elif ch==6:
                	e=input("Enter ele")
                	print(l.count(e))
            	elif ch==7:
                	print(min(l))
            	elif ch==8:
                	l.sort()
                	print(l)
            	elif ch==9:
                	l.reverse()
                	print(l)
            	elif ch==10:
                	l.clear()
                	print("list is: ",l)
            	else:
                	break
    elif(ch1==2):
        print("Menu")
        print("1.size of set")
        print("2.length of set")
        print("3.add of set")
        print("4.intersection of set")
        print("5.diffrence of set")
        print("6.symmetric difference of set")
        print("7.check for a element of set")
        print("8.pop of set")
        print("9.clearing of set")
        print("10.deletion of set")
        print("0.exit")
        while True:
            ch=int(input("Enter your choice"))
            if ch==1:
                set1=set(input("enter the set"))
                print(set1._sizeof_())
            elif ch==2:
                set1=set(input("Enter the set"))
                print(len(set1))
            elif ch==3:
                set1=set(input("enter the set"))
                set1.add(7)
                print(set1)
            elif ch==4:
                set1=set(input("enter the set1").split())
                set2=set(input("enter the set2").split())
                z=set1.intersection(set2)
                print("z=",z)
            elif ch==5:
                set1=set(input("enter the set1"))
                set2=set(input("enter the set2"))
                print(set1-set2)
            elif ch==6:
                set1=set(input("enter the set1"))
                set2=set(input("enter the set2"))
                print(set1^set2)
            elif ch==7:
                set1=set(input("enter the set"))
                x=input("enter the value to check")
               
                print(set1._contains_(x))
            elif ch==8:
                set1=set(input("enter the set"))
                set1.pop()
            elif ch==9:
                set1=set(input("enter the set"))
                set1.clear()
            elif ch==10:
                set1=set(input("enter the set"))
                del(set1)
                print(set1)
            else:
                break
    else:
        break
