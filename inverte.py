texto = "palavra"
letterGrabber = []

for i in range(len(texto) - 1, -1, -1):
    letterGrabber.append(texto[i])

reversedText = "".join(letterGrabber)
print(reversedText)
