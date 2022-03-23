# ProgrammingLab Idrostudi
# Lezione 5
# Paolo Martinis - 23.03.2022

class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        # variante 1
        file_leggibile = True
        # apri il file in sola lettura
        try:
            my_file = open(self.name, 'r')
        except:
            print('Errore: Non riesco a leggere il file...')
            file_leggibile = False
            # variante 2
            #return []
        else:
        #variante 1
        #if file_leggibile:
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
#csv_file = CSVFile('shampoo_sales_2.csv')
#print(csv_file.get_data())


class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        numerical_list = []
        # chiamo la get_data del padre 
        string_list = super().get_data()
        
        for line in string_list:
            convertable = True
            row_elems = []
            row_elems.append(line[0])
            for element in line[1:]:
                try:
                    n_element = float(element)
                except:
                    print('Errore: non riesco a convertire a numero...\nSalto la riga "{}" perchè non posso convertire il valore "{}"'.format(line,element))
                    convertable = False
                row_elems.append(n_element)
            if convertable:
                numerical_list.append(row_elems)
        return(numerical_list)

# controlliamo se funziona (a video)
#csv_file = NumericalCSVFile('shampoo_sales.csv')
#print(csv_file.get_data())