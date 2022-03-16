# ProgrammingLab Idrostudi
# Paolo Martinis - 16.03.2022

def sum_csv(file_name):
    # apri il file in sola lettura
    my_file = open(file_name, 'r')
    # inizializza la variabile di somma
    overall_sum = 0.0
    # cicla sulle righe
    for line in my_file:
        # spezzetta la riga in elementi in base al separatore (,)
        line_elements = line.split(',')
        # salta la riga di intestazione
        if line_elements[0] != 'Date':
            # leggi il valore della data (qui non serve, commentato...)
            #date = line_elements[0]
            # leggi il valore numerico in formato testo
            txt_value = line_elements[1]
            # converti a reale
            real_value = float(txt_value)
            # aggiungi alla somma totale
            overall_sum += real_value
    return overall_sum

# controlliamo se funziona (a video)
#nome_file = 'shampoo_sales.csv'
#print(sum_csv(nome_file))
