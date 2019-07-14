# Variáveis
contacts = [
	{'name': 'Bob', 'surname': '', 'phone': '555-1407', 'email': 'example@python.com'},
	{'name': 'Alice', 'surname': 'Johnson', 'phone': '555-1607', 'email': ''},
]

options = {
	'add':    1,
	'remove': 2,
	'sort':   3,
	'print':  4,
	'save':   5,
	'exit':   9
}

def print_menu(length = 30):
	print('Menu'.upper().center(30))
	print(('-'*25).center(30))
	
	for k,v in options.items():
		print(('{}:'.format(k.title()).ljust(20) + str(v)).center(30))
		
	print(('-'*25).center(30))

def create_contact():
	contact = {
		'name': '',
		'surname': '',
		'phone': '',
		'email': ''
	}
	
	# Name & Surname
	while contact['name'] == '':
		name = input('Nome ').split()
		
		if len(name) > 0:
			contact['name'] = name[0]
			
			if len(name) > 1:
				contact['surname'] = ' '.join(name[1:])
			else:
				contact['surname'] = input('Sobrenome: ')
				
	# Phone || Email
	while contact['phone'] == contact['email'] == '':
		print('Preencha o numero e/ou email')
		
		contact['phone'] = input('Telefone: ')
		contact['email'] = input('Email: ')
		
	return contact

def add_contact(contacts):
	contact = create_contact()
	contacts.append(contact)

def remove_contact(contacts):
	name = input('Digite o nome do contato: ')
	sel = []
	
	# Montando lista de contatos
	for i in range(len(contacts)):
		c = contacts[i]
		
		if c['name'].find(name) != -1:
			sel.append(c)
			
	if len(sel) == 0:
		print('Nenhum contato encontrado')
	else:
		print('Contatos'.upper())
		print('-'*25)
		
		# Print: Lista de contatos
		for i in range(len(sel)):
			print((str(i + 1) + '.').ljust(5), sel[i]['name'], sel[i]['surname'])
		
		print('Selecione um contato ou digite 0 para cancelar: ')
		
		opt = -1
		while opt < 0 or opt > len(sel):
			opt = int(input('	> '))
			
		if n == 0:
			print('Nenhum contato selecionado')
		else:
			x = sel[n - 1][0]
			contacts.pop(x)
			

def print_contacts(contacts):
	for c in contacts:
		print('Name:', c['name'], c['surname'])
		print('Contacts:')
		
		if c['phone'] != '': print(' > Phone:'.rjust(10), c['phone'])
		if c['email'] != '': print(' > Email:'.rjust(10), c['email'])
			
		print()

def sort_contacts(contacts):
	contacts.sort(key = lambda x: (x['name'], x['surname']))

def save_contacts(contacts, file = '../../res/tmp.txt'):
	with open(file, 'w') as handler:
		for c in contacts:
			handler.write(';'.join(map(str, c.values())))
			handler.write('\n')

# Main
if __name__ == '__main__':
	while True:
		# Menu
		print_menu()
			
		# Choosing Option
		opt = 0
		while opt not in options.values():
			opt = int(input('	> '))
			
		# Action
		if opt == 9:
			break
		elif opt == 1:
			print('Add'.upper().center(30))
			add_contact(contacts)
		elif opt == 2:
			print('Remove'.upper().center(30))
			remove_contact(contacts)
		elif opt == 3:
			print('Sort'.upper().center(30))
			sort_contacts(contacts)
		elif opt == 4:
			print('Print'.upper().center(30))
			print_contacts(contacts)
		elif opt == 5:
			print('Save'.upper().center(30))
			sort_contacts(contacts)
			save_contacts(contacts)
			
	print('Program ended'.upper().center(30))