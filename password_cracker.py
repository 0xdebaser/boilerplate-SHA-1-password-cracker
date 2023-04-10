import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt") as file:
        common_passwords = file.read().split("\n")

    if use_salts:
        with open("known-salts.txt") as file:
            salts = file.read().split("\n")
        for password in common_passwords:
            for salt in salts:
                for i in range(2):
                    sha_1 = hashlib.sha1()
                    if i == 0:
                        salted_password = salt + password
                    else:
                        salted_password = password + salt
                    sha_1.update(salted_password.encode("utf-8"))
                    if sha_1.hexdigest() == hash:
                        return password  

    else:
        for password in common_passwords:
            sha_1 = hashlib.sha1()
            sha_1.update(password.encode("utf-8"))
            if sha_1.hexdigest() == hash:
                return password

    return "PASSWORD NOT IN DATABASE"
    