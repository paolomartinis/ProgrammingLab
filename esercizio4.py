# ProgrammingLab Idrostudi
# Lezione 4
# Paolo Martinis - 16.03.2022

class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        # apri il file in sola lettura
        my_file = open(self.name, 'r')
        # inizializza la lista generale
        overall_list = []
        # cicla sulle righe
        for line in my_file:
            # strippo la linea per rimuovere la newline
            line = line.strip()
            # spezzetta la riga in elementi in base al separatore (,)
            # nb: implicitamente crea una lista
            line_elements = line.split(',')
            # salta la riga di intestazione
            if not line_elements[0].startswith('Date'):
                # appendi alla lista generale
                overall_list.append(line_elements)
        return(overall_list)

# controlliamo se funziona (a video)
csv_file = CSVFile('shampoo_sales.csv')
print(csv_file.get_data())