import click


@click.command()

@click.option('--string',default='-',help='Text to be encrypted.')			#Mention the string which you want to encrypt

@click.option('--key',default=3,help='Determines how to encrypt or decrypt.')		#Value by which encryption and decryption should take place

@click.argument('out',type=click.File('a'),required=False)				#Mention file to store encrypted or decrypted results. File opened in append mode

@click.option('--encrypt',is_flag=True,help='Enables us to encrypt your data.')		#Does not take any arguments after option is given

@click.option('--decrypt',is_flag=True,help='Enables us to decrypt your data.')		#Does not take any arguments after option is given

def cli(string,key,out,encrypt,decrypt):
	"""Given string is encrypted and decrypted and stored in a file of your choice"""

	if(encrypt):			#To encrypt the string when cli gets '--encrypt' option
		ascii_vals_enc=[ord(c) for c in string]
		
		for i in range(0,len(ascii_vals_enc)):
			if(ascii_vals_enc[i]>=65 and ascii_vals_enc[i]<=90):
				ascii_vals_enc[i] = 65 + (ascii_vals_enc[i] + key - 91)%26

			elif(ascii_vals_enc[i]>=97 and ascii_vals_enc[i]<=122):
				ascii_vals_enc[i] = 97 + (ascii_vals_enc[i] + key - 122)%26
		
		encrypt_string = ''.join(chr(i) for i in ascii_vals_enc)
		print "Message encrypted! Please check the file you saved it in!"
		click.echo("The message has been encrypted to %s"% encrypt_string,file=out)

	elif(decrypt):			#To decrypt the string when cli gets '--decrypt' option
		
		ascii_vals_dec=[ord(c) for c in string]
		for i in range(0,len(ascii_vals_dec)):
			if(ascii_vals_dec[i]>=65 and ascii_vals_dec[i]<=90):
				ascii_vals_dec[i] = 90 - (90 - ascii_vals_dec[i] + key )%26

			elif(ascii_vals_dec[i]>=97 and ascii_vals_dec[i]<=122):
				ascii_vals_dec[i] -= (key+1)

		decrypt_string = ''.join(chr(i) for i in ascii_vals_dec)
		print "Message decrypted! Please check the file you saved it in!"
		click.echo("The message has been decrypted to %s" % decrypt_string,file=out)


