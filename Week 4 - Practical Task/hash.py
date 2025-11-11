import bcrypt

password = "AlbertWesker".encode("utf-8")

hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds = 12))
print("Hashed:", hashed.decode())