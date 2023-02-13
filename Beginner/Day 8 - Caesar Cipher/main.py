#DAY 8
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1','2','3','4','5','6','7','8','9',' ']

direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("\nType your message: ").lower()
shift = int(input("\nType the encryption/description number: "))

def caesar(key, data, direction):
	final_text = ""
	position = 0
	for letter in data:
		ref = alphabet.index(letter)
		if direction == 'encode':
			final_text += alphabet[(ref+key)-len(alphabet)]
		elif direction == 'decode':
			if ref-key < 0:
				position = len(alphabet)+(ref-key)
			else:
				position = (ref-key)
			final_text += alphabet[position]
		else:
			print("Wrong comand!")
			return
			
	print(f"The {direction}d message is {final_text}")

caesar(shift, text, direction)

#cdefghijklmnopqrstuvwxyz ab
#abcdefghijklmnopqrstuvwxyz 