import os

def toon_aantal_kluizen_vrij():
	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()
	aantal_vrij_kluizen = 12 - len(kluizen)
	print(" - Er zijn: {} vrije kluizen." .format(aantal_vrij_kluizen))
#eind def toon_aantal_kluizen_vrij

def nieuwe_kluis():
	lijst_totaal_kluisnummers = ['1','2','3','4','5','6','7','8','9','10','11','12']
	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()

	for kluis in kluizen:
		nummer_code_splits = kluis.split(";")
		for kluisnummer in nummer_code_splits:
			if kluisnummer in lijst_totaal_kluisnummers:
				lijst_totaal_kluisnummers.remove(kluisnummer)

	if lijst_totaal_kluisnummers != "":
		code = input("Voer uw kluiscode in: ")
		code_confirm = input("Voer uw kluiscode nog een keer in: ")
		while code != code_confirm:
			code = input("Voer uw kluiscode in: ")
			code_confirm = input("Voer uw kluiscode nog een keer in: ")
		
		if code == code_confirm:
			kluisnummer = lijst_totaal_kluisnummers[0]
			save_kluis = open('kluizen.txt', 'a')
			save_kluis.write('{};{}\n'.format(kluisnummer, code))
			save_kluis.close()
			print("\nKluis succesvol opgeslagen.\nUw kluisnummer is: {} vergeet aub uw kluiscode niet." .format(kluisnummer))
# eind def nieuwe_kluis

def kluis_openen():
	message = 0
	kluisnummer = input("Kies uw kluisnummer: ")
	kluiscode = input("Voer aub uw kluiscode in: ")
	invoer_kluis = kluisnummer + ";" + kluiscode
	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()

	for kluis in kluizen:
		kluis = kluis.strip()
		if invoer_kluis == kluis:
			message = "Dat is een goede combinatie de kluis is open."
			break
		else:
			message = "Dat is een foutieve combinatie."
	print(message)
# eind def kluis_openen

def kluis_teruggeven():
	message = 0
	kluisnummer = input("Kies uw kluisnummer: ")
	kluiscode = input("Voer aub uw kluiscode in: ")	
	invoer_kluis = kluisnummer + ";" + kluiscode
	to_remove_kluis = kluisnummer + ";" + kluiscode + "\n"

	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()
	infile.close()
	
	outfile = open('kluizen.txt', 'w')
	for kluis in kluizen:
		kluis = kluis.strip()
		if invoer_kluis == kluis:
			kluizen.remove(to_remove_kluis)
			message = "Dat is een goede combinatie, kluis verwijderd."
			break
		else:
			message = "Dat is een foutieve combinatie."

	for kluis in kluizen:
		outfile.write(kluis)
	outfile.close()
	print(message)
# eind def kluis_teruggeven


def hoofdprogramma():
	while True:
		print("\nWelkom bij de NS bagagekluis kies in van de 5 menu opties door het bijhorden getal in te voeren.")
		print("1: Ik wil weten hoeveel kluizen no vrij zijn.")
		print("2: Ik wil een nieuwe kluis.")
		print("3: Ik wil even iets uit mijn kluis halen.")
		print("4: Ik geef mijn kluis terug.")
		print("5: Ik wil stoppen.")

		try:
			optie = eval(input("Optie: "))
			if optie == 1:
				print("\nAantal vrije kluizen:")
				toon_aantal_kluizen_vrij()
			elif optie == 2:
				print("\nNieuwe kluis:")
				nieuwe_kluis()
			elif optie == 3:
				print("\nKluis openen:")
				kluis_openen()
			elif optie == 4:
				print("\nKluis terug geven:")
				kluis_teruggeven()
			elif optie == 5:
				clear = lambda: os.system('cls')
				clear()
				print("Totziens")
				break
			else:
				print("Oops het ingevoerd getal is geen menu optie")
		except NameError:
			print("Oops u moet alleen het getal van de menu optie invoeren.")
		except SyntaxError:
			print("Oops u heeft niets ingevoerd.")
# eind def hoofdprogramma
hoofdprogramma()
