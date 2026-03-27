from pwdlib import PasswordHash

def hashpassword(password:str)->str:
    pwd=PasswordHash.recommended()
    return pwd.hash(password)