
while True:
    figura = input(f'Scegli figura tra quadrato, cerchio, rettangolo, oppure scrivi esci per terminare il programma: ')
    if figura == 'quadrato':
        lato = int (input(f'inserisci lunghezza lato: '))
        perimetro_quadrato= lato * 4
        print(f'il perimetro corrisponde a: ' , perimetro_quadrato)
    elif figura == 'rettangolo':
        base = int (input(f'inserisci lunghezza base: '))
        altezza = int (input(f'inserisci lunghezza altezza: '))
        perimetro_rettangolo = base * 2 + altezza * 2
        print(f'il perimetro corrisponde a: ' , perimetro_rettangolo)
    elif figura == 'cerchio':
        raggio = int(input(f'inserisci lunghezza raggio: '))
        circonferenza = 2 * 3.14 * raggio
        print(f'La circoferenza corrisponde a: ' , circonferenza)
    elif figura == 'esci':
        break
    else:
        print('Puoi inserire solo: quadrato, rettangolo o cerchio')