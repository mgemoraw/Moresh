"""
Public key Cipher
"""
import sys
import math
import os


SYMBOLS = r"""
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.?!@#$%^&*()_-+=[]{}|\;:""''<>/`~
"""
AMHARIC = r"""
ሀሁሂሃሄህሆ
ለሉሊላሌልሎ
ሐሑሒሐሔሕሖ
መሙሚማሜምሞ
ሠሡሢሣሤሥሦ
ረሩሪራሬርሮ
ሰሱሲሳሴስሶ
ሸሹሺሽሻሼሽሾ
ቀቁቂቃቄቅቆ
በቡቢባቤብቦ
ተቱቲታቴትቶ
ቸቹቺቻቼችቾ
ኀኁኂኃኄኅኆ
ነኑኒናኔንኖ
ኘኙኚኛኜኝኞ
አኡኢኣኤእኦ
ከኩኪካኬክኮ
ኸኹኺኻኼኽኾ
ወዉዊዋዌውዎ
ዐዑዒዓዔዕዖ
ዘዙዚዛዜዝዞ
ዠዡዢዣዤዥዦ
የዩዪያዬይዮ
ደዱዲዳዴድዶ
ጀጁጂጃጄጅጆ
ገጉጊጋጌግጎ
ጠጡጢጣጤጥጦ
ጨጩጪጫጬጭጮ
ጵጱጲጳጴጵጶ
ጸጹጺጻጼጽጾ
ፀፁፂፃፄፅፆ
ፈፉፊፋፌፍፎ
ፐፑፒፓፔፕፖ
ኋሏሗሟሧሯሷሿቋቧቷቿኇኗኟኧኳዃዟዧዷጇጓጧጯጷጿፇፏፗ
"""

# The public and private keys for this program are created by
# the keygen.py progam
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main(mode=None):
	# Reuns a test taht encrypts a message from a file or decrypts a message
	# from a file.
	filename = 'encrypted_file.txt'
	# mode = 'encrypt' # Set to either 'encrypt' or 'decrypt' mode

	if (mode == 'encrypt'):
		message = "JJournalists belong in the gutter because that is where the ruling classes throw their guilty secrets. Gerald Priestland. The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people. Hugo Black"
		publicKeyFilename = 'moresh_pubkey.txt'
		print("Enrypting and writing to {}...".format(filename))
		encryptedText = encryptAndWriteToFile(filename, publicKeyFilename, message)

		print("Encrypted text:")
		print(encryptedText)

	elif mode == 'decrypt':
		privKeyFilename = 'moresh_privkey.txt'
		print("Reading from {} and decrypting...".format(filename))

		decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
		print("Decrypted text:")
		print(decryptedText)
	else:
		print()

def getBlocksFromText(message, blockSize):
	# Converts a string message to block text
	for character in message:
		if character not in symbols:
			print("ERROR: The symbol set does not have the character {}".format(character))
			sys.exit()
	blockInts = []
	for blockStart in range(0, len(message), blockSize):
		# Calclate teh block integer for this block of text
		blockInt = 0
		for i in range(blockStart, min(blockStart + blockSize, len(message))):
			blockInt += (symbols.index(message[i])) * (len(symbols)**(i % blockSize))
		blockInts.append(blockInt)
	return blockInts

def getTextFromBlocks(blockInts, messageLength, blockSize):
	# Converts a list of block integers to the original message string
	# The original message length is needed to properly convert the last
	# block integer.
	message = []
	for blockInt in blockInts:
		blockMessage = []
		for i in range(blockSize - 1, -1, -1):
			if len(message) + i < messageLength:
				# Decode the message string for 128 or (whatever
				# blockSize is set to) characters from this block integer
				charIndex = blockInt // (len(symbols)**i)
				blockInt = blockInt % (len(symbols)**i)
				# print(charIndex)
				blockMessage.insert(0, symbols[charIndex])
		message.extend(blockMessage)
	return ''.join(message)

def encryptMessage(message, key, blockSize):
	# Converts the message string into a list of block integers, and then
	# encrypts each block integer.
	encryptedBlocks = []
	n,e = key
	for block in getBlocksFromText(message, blockSize):
		# ciphertext plaintext ^ e mod n
		encryptedBlocks.append(pow(block, e, n))
	return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
	# Decrypts a list of encrypted block ints to the original message
	# string. The original message length is required to properly decrypt
	# the last block. Be sure to pass the PRIVATE key to decrypt.
	decryptedBlocks = []
	n, d = key
	for block in encryptedBlocks:
		# plaintext = ciphertext ^ e mod n
		decryptedBlocks.append(pow(block, d, n))
	return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
	# Given the filename of a file that contains a public or private key
	# return the key as a (n,e) or (n,d) tuple value
	with open(keyFilename, 'r') as fo:
		content = fo.read()

	keySize, n, EorD = content.split(",")
	return (int(keySize), int(n), int(EorD))

def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=None):
	# Using a key from a key file, encrypt the message and save and save it to
	# file. Returns the encrypted message string.
	keySize, n, e = readKeyFile(keyFilename)

	if blockSize == None:
		# If blockSize isn't given, set it to the largest size allowed by the key size and symbol set size.
		blockSize = int(math.log(2** keySize, len(symbols)))

	# Check that key size is large enough for the block size
	if not (math.log(2 ** keySize, len(symbols)) >=blockSize):
		sys.exit("ERROR: Blosk size is too large for the key and symbol set size. Did you specify the correct key file and encrypted file?")

	# Encrypt the message
	encryptedBlocks = encryptMessage(message, (n, e), blockSize)

	# Convert the large int values to one string value
	for i in range(len(encryptedBlocks)):
		encryptedBlocks[i] = str(encryptedBlocks[i])
	encryptedContent = ','.join(encryptedBlocks)

	# Write out the encrypted string to the output file
	encryptedContent = '{}_{}_{}'.format(len(message), blockSize, encryptedContent)
	fo = open(messageFilename, 'w')
	fo.write(encryptedContent)
	fo.close()

	# Also return the encrypted string:
	return encryptedContent

def readFromFileAndDecrypt(messageFilename, keyFilename):
	# Using a key from a key file, read and encrypt message from  a file
	# and then decrypt it. Returns the decrypted message string
	keySize, n, d = readKeyFile(keyFilename)


	# Read in the message length and the encrypted message from the file
	fo = open(messageFilename, 'r')
	content = fo.read()
	fo.close()

	messageLength, blockSize, encryptedMessage = content.split("_")
	messageLength = int(messageLength)
	blockSize = int(blockSize)


	# Check that key size is large enough for the block size

	if not (math.log(2 ** keySize, len(symbols)) >= blockSize):
		sys.exit("ERROR: Blosk size is too large for the key and symbol set size. Did you specify the correct key file and encrypted file?")

	# Convert the encryped message into large int values
	encryptedBlocks = []
	for block in encryptedMessage.split(','):
		encryptedBlocks.append(int(block))


	# Decrypt the large int values
	return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)



# If criptify.py is run (instead of imported as a module), call
# the main() function.
# if __name__ == "__main__":
# 	main(mode='decrypt')


from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Hello World")

print(token)

print(f.decrypt(token))

def encrypt(text):
	
	try:
		current_path = os.getcwd()
		with open(f"{current_path}\\modules\\moresh_privkey.txt", "r")  as pubkey:
			text = pubkey.read()
		
	except:
		text =os.getcwd()
	return text

def decrypt(text):
	try:
		path = os.getcwd()
		with open(f"{path}\\modules\\moresh_privkey.txt", "r")  as pubkey:
			text = pubkey.read()
	except:
		text =os.getcwd()

	return text



