# select two small prime numbers print
# n = p * q
# find 0(n) = p-1 * q-1
# find a private key i.e. the range of  1 < e < 0(n)
# CT = PT ^ e * mod(n)
# DT = CT ^ d * mod(n)

def inputt():
  prime1, prime2 = input("Enter two prime numbers here: ").split(' ')
  prime1= int(prime1) 
  prime2= int(prime2)
  if (test_prime(prime1) and test_prime(prime2)) == True:
    return prime1,prime2
  else:
    print('Enter the values again:')
    prime1,prime2 = inputt()
    if (test_prime(prime1) and test_prime(prime2)) == True:
      return prime1,prime2

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))

def gcd(x,y):
   while(y):
       x, y = y, x % y
 
   return x

def userinput():
  plaintext = int(input('Enter your credit/debit/netbanking card number to be secured:'))
  return plaintext

def cipher(phi,e_key,plaintext):
  cipher = (plaintext**e_key)
  cipher = cipher%num
  print('Cipher Text '+ str(cipher))
  return cipher

def decipher(num,d_key,ciphertext):
  dec = (ciphertext**d_key)%num
  print('Deciphered Text ',dec)
  return dec

def calc_d_key(phi,e_key,plaintext):
  for val in range(2,phi):
    if (e_key*val)%phi==1:
      d_key = val
      print('Decryption Key '+ str(d_key))
      return d_key

msg = 'Welcome to RSA ALGORITHM'
print(msg)
print('1.___________________________________________________________________________')
prime1, prime2 = inputt()
num = prime1*prime2
phi = (prime1-1)*(prime2-1)
print('2.___________________________________________________________________________')
for x in range(2,phi):
  if (gcd(x,phi) == 1):
    e_key = x
    print('Encryption key ' + str(e_key))
    break
print('3.___________________________________________________________________________')
plaintext = userinput()
print('4.___________________________________________________________________________')
ciphertext = cipher(num,e_key,plaintext)
print('5.___________________________________________________________________________')
d_key = calc_d_key(phi,e_key,plaintext)
print('6.___________________________________________________________________________')
decrypted_text = decipher(num,d_key,ciphertext)