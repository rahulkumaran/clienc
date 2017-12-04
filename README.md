# CLIEnc

A  program that allows you to encrypt and decrypt data using the CLI.

This program best runs on Ubuntu (Tested and executed)
To run this program follow the given steps:

(1) Download virtualenv in the same folder as that of the clienc repository programs.(if you already have this then skip this and go to the next step)

    sudo apt install virtualenv
    
    
(2) Then run the virutal environment in the same folder.

    virtualenv venv
    
(3) Then to make sure you enter your virtual environment, enter the following command.

    . venv/bin/activate
    
(4) Then type the command below, in order to make sure that the changes you do in your file are directly reflected in your virtual environment.

    pip install --editable .
    
    
(5) Finally type the below command to make sure that you get a list of the functionalities available in the following program

    clienc --help
    

Lastly, <b>please follow the order in which the options are given</b>.
For example if you want encrypt the word "KILLBILL" by a key value of 4, and store the encrypted data result in a new file "test.txt", then you need to execute the following command:

    clienc --string KILLBILL --key 4 test.txt --encrypt
    
If you want to encrypt or decrypt a sentence with spaces then put the sentence in "". For example, if you want to encrypt the sentence "CLIENC IS A CLI APPLICATION", execute the following command:

    clienc --string "CLIENC IS A CLI APPLICATION" --key 4 test.txt --encrypt
    

    
# IMPORTANT NOTE
(1) Currently encrypts and decrypts only capital letters.

(2) Make sure to follow order.

(3) --encrypt or --decrypt should always be used in the end only.
