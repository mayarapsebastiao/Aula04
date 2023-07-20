minha_string = "qualquer texto"
print(type(minha_string))
print(minha_string)
print(f"concatenar {minha_string} em string")
print(minha_string.upper())
print(minha_string.lower())
print(minha_string.capitalize())
print(minha_string.isupper())
print(minha_string.islower())
print(minha_string.strip())
print(minha_string.replace("qualquer","meu"))
print(minha_string.replace("u","U"))
print(minha_string.replace("u","U",1))
print(len(minha_string))
print(minha_string[0])
print(minha_string[2:5])
print(minha_string[-4:-1])
print(minha_string.index("u"))
print(minha_string.index("texto"))

x= "texto" in minha_string

print(x)

minha_string2 = """linha 1,
linha 2,
linha 3.
"""
print(minha_string2)

minha_string3 = "linha 1,\nlinha 2,\nlinha 3."
print(minha_string3)

minha_string4 = "adiciona entre \"aspas\" no texto"
print(minha_string4)