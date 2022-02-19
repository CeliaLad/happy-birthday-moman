import cv2
import numpy as np

# image demo
demo = cv2.imread("assets/image__source.png", 0)
demo = cv2.flip(demo, 1)
cv2.imwrite("assets/image__source_key_demo.png", demo)   # Save key image
# demo shape and make a key
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
cv2.imwrite("assets/image__source_key.png", key)   # Save key image

encryption = cv2.bitwise_xor(demo, key)  # encryption
cv2.imwrite("assets/image__source_encrypted.png", encryption)     # Save the encrypted image
decryption = cv2.bitwise_xor(encryption, key)  # decrypt
cv2.imwrite("assets/image__source_decrypted.png", decryption) # Save the decrypted image

cv2.imshow("encryption", encryption)  # Display ciphertext image
cv2.imshow("decryption", decryption)  # Displays the decrypted image

# https://realpython.com/python-bitwise-operators/
