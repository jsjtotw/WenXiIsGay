tandas = input('What is your name')
if tandas == 'joshua':
    print('Error')
elif tandas == 'Joshua':
    print('Error')
else:
    gen = input('What is your gender? (m/f)')
    if gen == 'm':
        par = "girlfriend"
    elif gen == 'f':
        par = "boyfriend"
    else:
        print('Error')
    
    jamban = input(f'Who is your {par} (This will not be recorded.)')
    if jamban == 'joshua':
        print('Error')
    elif jamban == 'Joshua':
        print('Error')
    else:
        print(f'{tandas} is gay.')
        print(f'{jamban} is also gay and is as retarded as you are currently are!')
