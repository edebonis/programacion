import bcrypt


def encriptar(password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    print(type(hashed))
    return hashed

def chechPas(password, hashed):
    check = password.encode('utf-8')
    if bcrypt.checkpw(check, hashed):
        return True
    else:
        return False

