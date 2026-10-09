import os

def tri(uri):
    os.chdir(uri)
    children, k = os.listdir() , 0
    while k < len(children):
        for i in range(len(children) - 1):
            if i != len(children) - 1:
                if os.path.getmtime(children[i]) > os.path.getmtime(children[i+1]):
                    a, b = children[i], children[i+1]
                    children[i], children[i+1] = b, a
        k += 1
    return children

def rename(liste):
    for index, element in enumerate(liste):
        os.rename(element, f'({index+ 1})_{element}')
    print(os.listdir())

def run():
    while True:
        user_input = input('Enter l\'emplacement du dossier: ')
        try:
            os.chdir(user_input)
            print(os.listdir())
            reponse = input('Voulez-vous numeroter les fichiers dans ce dossier? [Oui(o) / Non(n)]: ').lower()
            if reponse == 'o':
                folder_path = tri(user_input)
                rename(folder_path)
            break
        except FileNotFoundError:
            print(f'{user_input} est introuvable.')

run()