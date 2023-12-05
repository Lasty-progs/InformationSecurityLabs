from random import randint as rand

# var 16 == 1
def read_id() -> str:
    id = input()
    return id


def create_pass(id:str) -> str:
    SPECIAL = "!”#$%&’()*"
    out = ""
    out += chr(rand(65, 90))
    out += chr(rand(65, 90))
    out += str(len(id)**2%10)
    out += chr(rand(48, 57))
    out += SPECIAL[rand(0,9)]
    out += chr(rand(97, 121))
    return out


def generate():
    print("Enter the ID:")
    id = read_id()
    print("Generated password:")
    print(create_pass(id))


generate()