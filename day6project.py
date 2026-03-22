print("\n🔢 Welcome to Number Analyzer 🚀")
while True:
    print("\n📋 ----------- Number Analyzer -----------")
    print(" 1️⃣  Reverse a Number")
    print(" 2️⃣  Sum of Digits")
    print(" 3️⃣  Prime Check")
    print(" 4️⃣  Multiplication Table")
    print(" 5️⃣  Star Pattern")
    print(" 6️⃣  Exit ❌")
    print("------------------------------------------")

    choice=int(input("👉 Enter Your choice(1-6): "))

    if choice==1:
        n=input("enter num : ")
        rev=""
        for i in n:
            rev=i+rev
        print("Reverse of the given number is : " ,rev)

    elif choice==2:
        n=input("enter num : ")
        total=0
        for i in n:
            total+=int(i)
        print("Total sum of digits of the number is : ",total)
    
    elif choice==3:
        n=int(input("enter num : "))
        is_prime=True
        if n<=1:
            is_prime=False
        else:
            i=2
            while i*i<=n:
                if n%i==0:
                    is_prime=False
                    break
                i+=1
        if is_prime:
            print(f"{n} is a Prime Num")
        else:
            print(f"{n} is Not prime Num")        
      
    elif choice==4:
        n=int(input("enter num for table : "))
        print("Multiplication Table for ",n)
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}") 

    elif choice==5:
        pattern=input("which type of pattern(even/odd) : ").lower()
        if pattern =='even':
            n=int(input("enter no of rows "))
            for i in range(1,n+1):
                for j in range(i):
                    print("*",end="")
                print() 
        elif pattern =='odd':
            n=int(input("enter no of rows "))
            for i in range(1,n+1):
                for j in range(i*2-1):
                    print("*",end="")
                print()
        else:
            print("Invalid pattern type ❌ ")
    
    elif choice==6:
        print("👋 Exiting Program")
        break

    else:
        print("❌ Invalid choice ❌ ")
        continue
