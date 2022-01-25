amigos = ["Sam", "Samantha", "Saurabh"]

starts = [amigo for amigo in amigos if amigo.startswith("S")]

print(amigos)
print(starts)
print(amigos is starts)
print("Amigos:  ", id(amigos), "starts: ", id(starts))
