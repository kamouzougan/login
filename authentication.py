import time
def main() :
    print("==========Welcome=========")
    access = False
    while access == False :
         print("Please lest's check your identity ")
         time.sleep(1)
         password = input("please enter your password ")
         if password == 'open123':
            access = True
            print("access is granted ")
         else :
               print("access denied")
         main()

main()
