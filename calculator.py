
from colorama import Style , Fore , Back , init
import time
init(autoreset=True)

print(Fore.BLACK+Back.BLUE+'Welcome to Calculator {beta version!}'.center(75))
def calc():
	list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	time.sleep(2)
	print('This style is AI generated btw , it didnt work for me well so I asked ai JUST about the style code not the code entirely')
	x = input(
    f"{Fore.CYAN}Choose:{Style.RESET_ALL}\n"
    f"{Fore.YELLOW}a-{Style.RESET_ALL} {Fore.GREEN+Style.BRIGHT}Addition\n"
    f"{Fore.YELLOW}b-{Style.RESET_ALL} {Fore.RED+Style.BRIGHT}Difference\n"
    f"{Fore.YELLOW}c-{Style.RESET_ALL} {Fore.LIGHTBLACK_EX+Style.BRIGHT+Style.BRIGHT+Style.BRIGHT}Multiplication\n"
    f"{Fore.YELLOW}d-{Style.RESET_ALL} {Fore.MAGENTA+Style.BRIGHT+Style.BRIGHT}Division\n"
    f"{Fore.YELLOW}q-{Style.RESET_ALL} {Fore.LIGHTBLUE_EX+Style.BRIGHT}Quit\n\n"
    f"{Fore.GREEN}(Write just the letter): {Style.RESET_ALL}"
    )
	


	if x =='a' :
		a = input('Choose the first number:  ')
		if a in list :
			print(f'Imposter Detected! : {'{a}'}')
			calc()
		else :
			a = float(a)
			time.sleep(1)
			b = input('Choose the second number:  ')
				
			if b in list :
				print(f'Imposter Detected! : {'{b}'}')
				calc()

			else :
				b=float(b)
				time.sleep(1.5)
				print('The result is : ', a+b)
				calc()
	elif x == 'b':
		a = input('Choose the first number:  ')
		if a in list :
			print(f'Imposter Detected! : {'{a}'}')
			calc()
		else:
			a = float(a)
			time.sleep(1)
			b = input('Choose the second number:  ')
			if b in list :
				print(f'Imposter Detected! : {'{b}'}')
				calc()
			else:
				b = float(b)
				time.sleep(1.5)
				print('The result is : ', a-b)
				calc()
	elif x == 'c':
		a = input('Choose the first number:  ')
		if a in list :
			print(f'Imposter Detected! : {'{a}'}')
			calc()
		else:
			a = float(a)
			time.sleep(1)
			b = input('Choose the second number:  ')
			if b in list :
				print(f'Imposter Detected! : {'{b}'}')
				calc()
			else:
				b = float(b)
				time.sleep(1.5)
				print('The result is : ', a*b)
				calc()
	elif x == 'd':
		a = input('Choose the first number:  ')
		if a in list :
			print(f'Imposter Detected! : {'{a}'}')
			calc()
		else:
			a = float(a)
			time.sleep(1)
			b = input('Choose the second number:  ')
			if b in list :
				print(f'Imposter Detected! : {'{b}'}')
				calc()
			else:
				b = float(b)
				if b == 0 :
					time.sleep(3)
					print('Cannot Devide by 0! stooopid')
					calc()
				else:
					time.sleep(1.5)
					print('The result is : ', a/b)
					calc()	
	elif x == 'q':
		time.sleep(.5)
		print(f'{Fore.RED+Style.BRIGHT}Hope you enjoyed!')
		
	else:
		time.sleep(1.5)
		print("That's not an option stooopid!")
		calc()
calc()	


	
