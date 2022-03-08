login = ['javohir.coder', 'azizcik77', 'javohir77', 'kotta.bolla', 'abbos_98', 'massa_38']
search = input("\nIltimos login kiriting:\n>>> ")
search = search.lower()
password = 'kiritilmagan'
if len(search) >= 6:
    if search not in login:
        password = password = input('\nparol kiriting:\n>>> ')
        if len(password) >= 8 and len(password) < 15:
            print('Ok.')
        else:
            print('\nParol minimum 8ta maximum 15ta belgidan iborat bo\'lishi kerak.')
            password = password = input('\nparol kiriting:\n>>> ')
    elif search in login:
        print('bu login band, iltimos boshqa login tanlang.')
else:
    print('Login 6ta belgidan ko\'p bo\'lishi kerak.')
    search = 'Xato'

if True:
    print(f'\nSizning loginingiz:\n>>> {search}\n\nSizning parolingiz:\n>>> {password}')