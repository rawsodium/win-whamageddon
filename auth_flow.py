import random
import hashlib


# generates a PKCE code verifier for PKCE authorization
def generate_code_verifier():
    # determine the range
    length = random.randrange(43, 128)



# generates a code challenge for PKCE authorization
def generate_code_challenge():
    code_verifier = generate_code_verifier()
    
    hashlib.sha256(code_verifier)