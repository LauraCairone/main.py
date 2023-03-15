inFile = open("schieramento.txt")

tab = []
for riga in inFile:
    riga = riga.rstrip()
    n = len(riga)
    if riga != "0" * n: # abbiamo trovato la prima riga dello schieramento
        tab.append(riga)

# print(tab)
larghezza = len(tab)


# Il testo dice che non è possibile avere "buchi"/ caduti nella prima fila
m = 0
n = 0
n_zeri = 0
ind = 0
trovata = False

while n < len(tab[0]):
    while not trovata:
        if tab[0][n] != "0":
            primo_num = int(tab[0][n])

            if primo_num > int(tab[0][n + 1]): # pongo la colonna successiva come necessariamente
                                                    # esistente essendo il valore [0][n] il primo dello
                                                    # schieramento e avendo questo un minimo di due file

                nFile = int(tab[0][n]) # perchè in questo caso sono necessariamente in ordine crescente
                direzione = "E"
                trovata = True
                n = 0

            elif primo_num < int(tab[0][n + 1]):
                nFile = max(tab[0])
                direzione = "W"
                trovata = True
                n = 0


            else: # nel caso i valori fossero uguali
                if primo_num == "1":
                    nFile = int(tab[len(tab)][n])
                    direzione = "N"
                    trovata = True
                    n = 0


                else:
                    nFile = int(tab[0][n]) # ordine crescente
                    direzione = "S"
                    trovata = True
                    n = 0

        n += 1


    while m < len(tab):
        riga_zeri = 0
        if m != 0 and m != (len(tab) - 1) and tab[m][n] == "0":
            riga_zeri += 1
            posizione = int(tab[m - 1][n])

        if riga_zeri > n_zeri:
            n_zeri = riga_zeri
            ind += posizione

        m += 1
    n += 1


print("La larghezza dello schieramento è %d" %larghezza)
print("Lo schieramento ha %d file" %nFile)
print("La direzione dello schieramento è %s" %direzione)
print("La fila con maggior numero di perdite è la %d" %ind)
