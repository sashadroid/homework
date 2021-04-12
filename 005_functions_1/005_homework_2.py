

def palindrom(p):
	if wwrite == "".join(reversed(wwrite)):
		return True
	return False
write = str(input("Введите любую фразу: "))
wwrite = write.replace(" ", "").replace(",", "")
print(palindrom(write))


