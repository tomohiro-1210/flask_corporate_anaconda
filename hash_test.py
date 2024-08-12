from werkzeug.security import generate_password_hash, check_password_hash

pw = "pikachu"
pw_hash = generate_password_hash(pw)
print(pw_hash)

pw_input = "mimikyu"
pw_check = check_password_hash(pw_hash, pw_input)
print(pw_check)