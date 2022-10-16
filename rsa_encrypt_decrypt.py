#This program generates rsa public and private keys
#Use public key to encrypt the message
#and private key to decrypt the message

import rsa
import os.path

global rsa_public_key, rsa_private_key
global path_to_keys_directory
global secret_message

#Location to the python program
path_to_keys_directory = "C:/Users/Desktop/PythonProjects/"

#Set the message
secret_message = "Lets change the secret message"

#Function generates public and private keys
def rsaKeyGenerator():
    #Generate a key pair
    rsa_public_key, rsa_private_key = rsa.newkeys(1024)
    
    #Open a file in writebytes mode, and save the public key
    with open("rsa_public_key.pem", "wb") as file:
        file.write(rsa_public_key.save_pkcs1("PEM"))
    
    #Open a file in writebytes mode, and save the private key
    with open("rsa_private_key.pem", "wb") as file:
        file.write(rsa_private_key.save_pkcs1("PEM"))
    
def rsaPrivateKey():
    #Open the private key file in read bytes mode
    with open("rsa_private_key.pem", "rb") as file:
        return rsa.PrivateKey.load_pkcs1(file.read())

def rsaPublicKey():
    #Open the public key file in read bytes mode
    with open("rsa_public_key.pem", "rb") as file:
        return rsa.PublicKey.load_pkcs1(file.read())

def rsaEncryption():
    #Check if private key exist
    rsa_private_key_file_exist = os.path.exists(path_to_keys_directory + 'rsa_private_key.pem')
    #Check if public key exist
    rsa_public_key_file_exist = os.path.exists(path_to_keys_directory + 'rsa_public_key.pem')
    
    #if both private and public keys exist  
    if rsa_private_key_file_exist and rsa_public_key_file_exist:
        #Get the public key 
        rsa_public_key = rsaPublicKey()
    else:
        #If either public or private key doesn't exist, generate a new key
        rsaKeyGenerator()
    
    #Encrypt the message with the public key 
    encrypted_message = rsa.encrypt(secret_message.encode(), rsa_public_key)
    
    #Write the encrypted message
    with open("encrypted_message_file", "wb") as file:
        file.write(encrypted_message)
   
def rsaDecryption():
    #Get the private key
    rsa_private_key = rsaPrivateKey()
    
    #Open the file in read mode
    encrypted_message = open("encrypted_message_file", "rb").read()
    
    #Decrypt the Encrypted message with the private key
    plain_message = rsa.decrypt(encrypted_message, rsa_private_key)
    
    #Print the plain message 
    print(plain_message)
    
rsaEncryption()
rsaDecryption()