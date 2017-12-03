import click


@click.command()

@click.option('--string',default='-',help='Text to be encrypted.')

@click.option('--key',default=3,help='Value by which key should be adjusted for Encryption decryption.')

@click.argument('out',type=click.File('a'),required=False)

@click.option('--encrypt',is_flag=True,help='Enables us to encrypt your data.')

@click.option('--decrypt',is_flag=True,help='Enables us to decrypt your data.')

def cli(string,key,out,encrypt,decrypt):
	"""Given string is encrypted and decrypted and stored in a file of your choice"""

	if(encrypt):
		ascii_vals_enc=[ord(c) for c in string]
		
		for i in range(0,len(ascii_vals_enc)):
			if(ascii_vals_enc[i]>=65 and ascii_vals_enc[i]<=90):
				ascii_vals_enc[i] = 65 + (ascii_vals_enc[i] + key - 91)%26
		
		encrypt_string = ''.join(chr(i) for i in ascii_vals_enc)
		print "Message encrypted! Please check the file you saved it in!"
		click.echo("The message has been encrypted to %s"% encrypt_string,file=out)

	elif(decrypt):
		
		ascii_vals_dec=[ord(c) for c in string]
		for i in range(0,len(ascii_vals_dec)):
			if(ascii_vals_dec[i]>=65 and ascii_vals_dec[i]<=90):
				ascii_vals_dec[i] = 90 - (90 - ascii_vals_dec[i] + key )%26
		decrypt_string = ''.join(chr(i) for i in ascii_vals_dec)
		print "Message decrypted! Please check the file you saved it in!"
		click.echo("The message has been decrypted to %s" % decrypt_string,file=out)
		
	
