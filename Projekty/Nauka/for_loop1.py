napis = ['dupa', 'kon', 'pies', 'kot']
napis1 = ['jaja', 'kura', 'kaczka', 'misio']

i=10
[print(x, z)for x, z in zip(napis, napis1)if x != 'kon' and x != 'kot']
