select = ""
crypt_message = ""
result = ""
key = ""
pos_neg = ""

while select != False:
  select = int(input(" select 1 to encrypt \n select 2 to decrypt \n select 0 to quit program"))

  if select == 1:
    crypt_message = input("enter the message you want to encrypt")
    key = int(input("enter the key to encrypt message"))

    if pos_neg != False:
      pos_neg = input(" select + to enter a positive number \n select - to enter a negative number")
      if pos_neg == "-":
        for x in range(0, len(crypt_message)):
          result += chr(ord(crypt_message[x])-key)
          print(result)
          result = ""
      elif pos_neg == "+":
        for x in range(0, len(crypt_message)):
          result += chr(ord(crypt_message[x])+key)
          print(result)
          result = ""

  elif select == 2:
    crypt_message = input("enter the message you want to decrypt")
    key = int(input("enter the key to encrypt message"))

    if pos_neg != False:
      pos_neg = input(" select + to enter a positive number \n select - to enter a negative number")
      if pos_neg == "-":
        for x in range(0, len(crypt_message)):
          result += chr(ord(crypt_message[x]) - key)
          print(result)
          result = ""
      elif pos_neg == "+":
        for x in range(0, len(crypt_message)):
          result += chr(ord(crypt_message[x]) + key)
          print(result)
          result = ""

  elif select ==0:
    print("you have just quitted this program")
    quit()