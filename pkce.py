import random
import hashlib
import base64

# generates a PKCE code verifier for PKCE authorization
def generate_code_verifier():
    # types of characters that can be possible: ASCII uppercase/lowercase, digits, underscores, periods, hyphens, tildes
    all_possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprqstuvwxyz0123456789-._~'

    # determines the length of the token, between 43 and 128 characters
    length = random.randrange(43, 128)

    # creates the token from the possible characters and a random length between 43 and 128 characters
    code_verifier = ''.join(random.choices(all_possible_chars, k=length))

    return code_verifier

# generates a code challenge for PKCE authorization
def generate_code_challenge():
    # generate a code verifier
    code_verifier = generate_code_verifier()

    # hash and encode the code verifier
    code_challenge = base64.b64encode(hashlib.sha256(code_verifier.encode('utf-8')).digest())

    return code_challenge