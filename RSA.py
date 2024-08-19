import sympy

def Convert_Binary_String(_int): #function to convert integer to binary
    binary_lst=[] #empty list to store binary numbers
    while _int>0: #Keeps running until _int is 0 (less than one)
        k=_int %2 #k is the modular of the _int and will be used to append the binary list. 
        binary_lst.append(str(k)) #Appending the binary list with k (mod of iteration) but also converting it to a list.
        _int=_int//2 #Updating the _int value with the quotient since that is what is left of _int after adding the mod to the binary list
    binary_lst.reverse() #Reversing the binary list to match how binary numbers should be ordered after using this method of binary expansion
    return ''.join(binary_lst) #joins the strings in the list and produces one string representing binary expansion
def FME(a, n, b):
    #def FME(a,n,b): #Fast Modular Exponation for (a^n mod b)
    result=1 #initilizing result 
    square=a #initilize a paramater that repeatadly squares a. 
    while n>0: #Loop to convert n to binary until until n=0
        k=n % 2 #extracts least signifgant bit
        if k==1: #if bit is one and not 0
            result=(result*square) % b #updates the result to reflect the latest binary number in the loop
        square=square * square % b # Updates square for the next iteration
        n = n // 2  # Updates n by dividing it by 2
    return result
def Euclidean_Alg(a, b):
    while b>0: #This will run as long as n is greater than 0
        k= a % b #k is equal to m module n
        a=b #assigning m as n to define the next largest number
        b=k #assining n as K for the next smallest number
    return a #returning the GCD.
def EEA(m, n):
    s1, t1 = 1, 0
    s2, t2 = 0, 1
    while n > 0:
        k = m % n
        q = m // n
        m, n = n, k
        s1, t1, s2, t2 = s2, t2, (s1 - q* s2), (t1 - q* t2)
    return m, s1, t1
def Find_Public_Key_e(p, q):
    if p <= 1 or q<=1:
        return False  # 0 and 1 are not prime numbers
    
    # Check for factors from 2 to sqrt(p) and sqrt(q)
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False  # Found a divisor, so p is not prime
    for i in range(2, int(q**0.5) + 1):
        if q % i == 0:
            return False  # Found a divisor, so q is not prime
    n=p*q #n is simply the product of the two prime inputs
    phi = (p - 1) * (q - 1) #phi is needed to calulate e. Euler's totient.
    for e in range(2, phi): #range from 2-phi since two is the smallest prime numer and phi is the largest e can be.
        if Euclidean_Alg(e, phi) == 1: #if e and phi are coprime, then e can be used as a public key.
            public_key_e = e
            return True,n, public_key_e
def compute_modular_inverse(a, m): #solving for modualar inverse 
    #a = a % m # Might as well compute a mod m
    m1, s1, t1 = EEA(a, m) #This assigns the values g,s,t from the Eucldian Extended algorithim above. 
    if m1 != 1: #If the modulo is not equal to one, then this is false.
        print('ERROR: ', a, ',', m, ' are not relatively prime.')
        return False
    return s1 % m #s%m would be the modular inverse of a.
def Find_Private_Key_d(e, p, q):
    #~~~~ This is copied in from above to check for primality~~~~#
    if p <= 1 or q<=1:
        return False  # 0 and 1 are not prime numbers
    
    # Check for factors from 2 to sqrt(p) and sqrt(q)
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False  # Found a divisor, so p is not prime
    for i in range(2, int(q**0.5) + 1):
        if q % i == 0:
            return False  # Found a divisor, so q is not prime
    #~~~~ This is the end of the primality check ~~~~# 
    n=p*q #n is simply the product of the two prime inputs
    phi = (p - 1) * (q - 1) #phi is needed to calulate e. Euler's totient.
    d=compute_modular_inverse(e,phi) 
    if d<0:
        while d<0:
            d+=phi         
    return d
def Convert_Text(_string):
    #integer_list = []
    integer_list = [ord(char) for char in _string]
    return integer_list
def Convert_Num(_list):
    _string = ''
    for i in _list:
        _string += chr(i)
    return _string
def Encode(e, n, message):
    num_lst=Convert_Text(message)
    cipher_text = []
    for num in num_lst:
        char_enc=FME(num,e,n)
        cipher_text.append(char_enc)
    return cipher_text
def Decode(n, d, cipher_text):
    message = ''
    letter_num_lst=[]
    for num in cipher_text:
        letter_num=FME(num,d,n)
        letter_num_lst.append(letter_num)
    message=Convert_Num(letter_num_lst)   
    return message

#creates a dictionry of users and passwords and can be apended with new users
User_and_pass={"Faisal":"Shahin", "Rachel":"Cox","Ben":"Someone"} 

#Function that genorates primes based on number of bits if the user doesnt have primes.
def generate_random_prime(bits):
    #Computes a range from 2^(bits-1) to 2^bits (from smallest bit number to bit number specified.
    #Therefore the user doesnt need to know an integer number range.
    return sympy.randprime(2**(bits-1), 2**bits)

#Function uses the dictornary above to make sure the user and password match
def authenticate_user():     
    attempts = 5 #Only get 5 log in attempts
    #function runs as long as you havent run out of attempts
    while attempts > 0:
        #asks for uername
        entered_user =input ("To log in Enter Username: ")
        #asks for password
        entered_password = input("Enter password: ") 
        #if user and password are the keys and values in the dictionary, then you can log in.
        if User_and_pass.get(entered_user) == entered_password:
            print("Welcome back, ",entered_user)
            #exits the loop
            return True
        else:
            #if user and pass dont match, then attemps is reduced by 1.
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.")
    print("Access denied.")
    #if running out of attempts, it exits the main function.
    return False

def log_in():
    #prompt to log in, create an account, or leave.
    account=input ("Sign in (press 1) or create an account Press (2) or exit (3): ")
    #if choice is 1, checks to see the user and pass using the athenticate user.
    if account == "1":
        if authenticate_user():
            return True
    #if choice is 2, you can make a user, a password,and those are addded to the dictionary.
    # Once the account is made, then a user can be redirected to athenticate user function.
    elif account == "2":
        user= input("Create a Username: ")
        while user in User_and_pass.keys() and user != "3":
            user=input ("Username already in use, please select a different one or press Q to exit")
            password= input ("Create a Password: ")
        User_and_pass[user]=password
        authenticate_user()
        return True
    #if 3 is elected the main function is exited.
    elif account == "3":
        return False
    return False

#This is the user interface the user uses after logging in decode or encode.
def messaging_interface():
    #prompt to see if the user wants a program to generate priem numbers
    answ=input("Do you know the prime numbers you want to use to code/decode? (Y/N)")
    #While loop running as long as the user doesnt exit (hits 4)
    while True:
        #intializes an x value to be used to break the loop for invalid inputs.
        x=1
        # if the user knows the prime numbers then two input messeges are outputted to get p and q.
        if "Y" in answ or "y" in answ:
            p = int(input("Enter a large prime number (p): "))
            q = int(input("Enter another  large prime number (q): "))
            # if p and q are prime then the find public key function is run (if is used to validate p and q are prime)
            # d is also computed using the new found e and the user inputs p and q.
            if Find_Public_Key_e(p, q):
                t,n, e = Find_Public_Key_e(p, q)
                d = Find_Private_Key_d(e, p, q)
                print( f"Your public key (e) is {e}, and your n is {n}. Don't forget them! With large enough primes they dont need to be kept safe")
            else:
                #if find public key is unable to run, then p and q are not prime and 
                print("\n!!!--------------------ERROR--------------------!!!\n P and Q are not prime. You will be logged out. Try again\n!!!--------------------ERROR--------------------!!!! ")
                # sets x to 100 to break the loop for an error.
                x=100
                return x
            break
        #if the user doesnt know primes this else if statement is initalized
        elif "N" in answ or "n" in answ:
            #promotes the user to generate primes if desired by the generate_random_prime funtcion
            do_primes= input("Would you like to us to generate some for you? (Y/N)")
            if "Y" in do_primes or "y" in do_primes:
                #if the user wants primes, then p and q are generated composed of 15 bit numbers.
                # p and q should be larger but figured this is large enough for this project.
                p= generate_random_prime(15)
                q= generate_random_prime(15)
                # a public key e is generated with the random p and q.
                t,n, e = Find_Public_Key_e(p, q)
                # a private key d is generated with the computed e and random p and q
                d = Find_Private_Key_d(e, p, q)
                print( f"Your public key (e) is {e}, and your n is {n}. Don't forget them! With large enough primes they dont need to be kept safe")
            else:
                # warns the user that they cant decode without primes.
                # prompts the user to enter the public key and n.
                print("if you dont know your  primes, you can only Encode messages(option 1 in the menu)\nplease select 1 or 4 from the menu")
                e = int(input("Enter the public key e (the smaller number of the two numbers you have): "))
                n = int(input("Enter n (the larger number of the two numbers you have): "))
                #Genrated an incorrect d to not allow the user to decode 
                d=1
            break
        else:
            print ("Error: not a valid input-try again later")
            #assigning x=100 to log out for invalid input
            x=100
            break
    # intializes a length and message list to decrypt the last encrypted message.        
    previous_encrypted_message = []
    leng = None
    #This runs until a false or break is found
    while True:
        #Prompts to ask a user that they wish to accomplish
        print("\n       Menu \n1. Send Message\n2. Receive Message\n3. Do You want to Decode the previously encoded message?\n4. Exit ")
        choice = int(input("Enter your choice: "))
        # if choice is 1, then the user can encode a message using previously calcuted or inputted e and n.
        if choice == 1:
            message = input("Enter the message to send: ")
            encrypted_message = Encode(e, n, message)
            #These two lines store the encoded message in a list and calcualtes length for option 3.
            previous_encrypted_message.extend(encrypted_message)
            leng=len(encrypted_message)
            #prints out the encoded messages
            print(f"\n Encrypted message: {encrypted_message}")
        
        elif choice == 2:
            #if choice 2, the user can decode a message
            # d==1 was initialized earlier if the user did not provide primes to stop this from running and generating an error.
            if d==1:
                print("\nError you did not provide primes!")
                return False
            #prompts the user to enter an encrypted message
            encrypted_message = input("Enter the encrypted message to decrypt (comma-separated): ")
            # converts the message from one long string to a list of strings.
            string_list = [s.strip() for s in encrypted_message.split(',')]
            integer_lst=[]
            #next lines identify characters to remove. 
            char_remove="["
            char_remove_2="]"
            #This loop removes brackets and converts each integer string to an integer, if it can't then the charchater is skipped
            #as it is most likely not an integer.
            for s in string_list:
                if char_remove in s:
                    s=s.replace(char_remove,"")
                if char_remove_2 in s:
                    s=s.replace(char_remove_2,"")
                try:
                    num=int(s)
                    integer_lst.append(num)
                except:
                    pass
                
            #Decodes the proccessed user input using the inegter list , n (calculated) and d(calculated)
            decrypted_message = Decode(n, d, integer_lst)
            print(f"\n Decrypted message: {decrypted_message}")

        elif choice == 3:
            #if choice 2, the user can decode a message
            # d==1 was initialized earlier if the user did not provide primes to stop this from running and generating an error.
            if d==1:
                print("\nError you did not provide primes!")
                return False
            #checks to see if there was a message provided and leng was updated.
            #if it was, then it decryptes the previously stored message
            elif leng  != None:
                decrypted_message = Decode(n, d, previous_encrypted_message[-leng:])
                print(f"\n Decrypted message: {decrypted_message}")
            else:
                print("\n Error, no previous message to decode")
        
        #if user wishes to leave, 4 will be inputted to exit the loop. Otherwise, it will exit based on invalid inputs
        elif choice == 4 or x==100:
            break
                 
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if log_in():
        messaging_interface()