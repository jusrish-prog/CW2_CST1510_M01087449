import bcrypt

def generate_hash(psw):
    byte_psw = psw.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(byte_psw, salt)
    return hash.decode("utf-8")


def is_valid_hash(psw, hash):
    hash_psw = hash.encode("utf-8")
    byte_psw = psw.encode("utf-8")
    is_valid = bcrypt.checkpw(byte_psw, hash_psw)
    return is_valid



# username = str(input("Enter a Username : "))
# found_lower = False
# found_upper = False
# found_digit = False
# found_spc = False
# special_characters = {"!","@","#","$","%","&"}

# for char in username:
#     if char.islower() == True:
#         found_lower = True

#     elif char.isupper() == True:
#         found_upper = True
    
#     elif char.isdigit() == True:
#         found_digit = True
    
#     elif char in special_characters:
#         found_spc = True


# if len(username) == 0:
#     print("Username cannot be empty")
# elif len(username) < 6:
#     print("Username is too short, must be at least 5 characters")
# else:
#     print("Length is okay")

   
# if found_lower == False:
#     print("Username must contain at least 1 lowercase character")

# if found_upper == False:
#     print("Username must contain at least 1 uppercase character")

# if found_digit == False:
#     print("Username must contain at least 1 digit")

# if found_spc == False:
#     print("Username must contain at least 1 special character")

# if found_lower and found_upper and found_digit and found_spc == True:
#     print("Username meets all requirements!")