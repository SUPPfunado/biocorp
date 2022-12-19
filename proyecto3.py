
import pandas as pd
from graphviz import Digraph
from graphviz import Graph
def secuencia(secuencia_nueva):
    codones = []
    sequence = []
    clean_sequence = []
    j = 0
    while j != len(secuencia_nueva):
        sequence.append(secuencia_nueva[j])
        if sequence[j] == "T":
            sequence[j] = "U"
        j+=1
    
    i = 0
    largo = len(sequence)
    while i < largo:
        if sequence[i] == "I":
           
            while sequence[i]!= "F":
            
                i = i + 1
           
        else:
            clean_sequence.append(sequence[i])
        i+=1
        
       

    secuencia_nueva = "".join(clean_sequence)

    start = ["AUG"]
    stop = ["UAG","UGA","UAA"]
    i = 0
    
    while i < len(secuencia_nueva)-2:
            if start[0] == secuencia_nueva[i:i+3]:
                i+=3
                while (i+3)<=len(secuencia_nueva):
                    if stop[0] == secuencia_nueva[i:i+3] or stop[1] == secuencia_nueva[i:i+3] or stop[2] == secuencia_nueva[i:i+3]:   
                        i+=len(secuencia_nueva)

                    else:
                        codones.append(secuencia_nueva[i:i+3])
                        i+=3
            i+=1 
    return (codones)


diccionario = {"CAU":"H","CGC":"R","GCU":"A","GCC":"A", "GCA":"A","GCC":"A", "CGU":"R", "GCG":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", "AAU":"N", "AAC":"N", "GAU":"D", "GAC":"D", "UGU":"C", "UGC":"C", "CAA":"Q","CAG":"Q", "GAA":"E", "GAC":"E", "GGU":"G","GGC":"G","GGA":"G","GGG":"G", "GAU":"H", "CAC":"H",  "AUU":"I", "AUG":"I", "AUA":"I", "UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L", "AAA":"K","AAG":"K", "AUG":"M", "UUU":"F","UUC":"F", "CCU":"P","CCC":"P","CCA":"P","CCG":"P", "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S", "ACU":"T","ACC":"T","ACA":"T","ACG":"T", "UGG":"W", "UAU":"Y","UAC":"Y"  ,"GUU":"V","GUC":"V","GUA":"V","GUG":"V"}

diccionario2 = {"CAU":"His","CGC":"Arg","GCU":"Ala","GCC":"Ala", "GCA":"Ala","GCC":"Ala", "CGU":"Arg", "GCG":"Arg", "CGA":"Arg", "CGG":"Arg", "AGA":"Arg", "AGG":"Arg", "AAU":"Asn", "AAC":"Asn", "GAU":"Asp", "GAC":"Asp", "UGU":"Cys", "UGC":"Cys", "CAA":"Gln","CAG":"Gln", "GAA":"Glu", "GAC":"Glu", "GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly", "GAU":"His", "CAC":"His",  "AUU":"He", "AUG":"He", "AUA":"He", "UUA":"Leu","UUG":"Leu","CUU":"Leu","CUC":"Leu","CUA":"Leu","CUG":"Leu", "AAA":"Lys","AAG":"Lys", "AUG":"Met", "UUU":"Phe","UUC":"Phe", "CCU":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro", "UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser","AGU":"Ser","AGC":"Ser", "ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr", "UGG":"Trp", "UAU":"Tyr","UAC":"Tyr","GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val", "UAG":"STOP", "UGA":"STOP", "UAA":"STOP"}
codones=[]
final = []

print("-------------------Menu-------------------")
menu = int(input("ingrese 1 para obtener la proteina \ningrese 2 para obtener las estadisticas de la secuencia \ningrese 3 para generar un diagrama de relacion aa \ningrese 4 para terminar el programa \nseleccione una opcion: "))
while menu != 4:
    
    if menu == 1:
        datos = open(input("ingrese el nombre del archivo junto a su extencion(.fasta): ")) # write or read
        nombre = datos.readline()
        secuencia_nueva = datos.read()
        datos.close()
        codones = secuencia(secuencia_nueva)
        porcentaje = "".join(codones)

        codones2 = codones
        i = 0
        while i != len(codones):
            if codones[i] in diccionario:
                encontrar = diccionario.get(codones[i])
                final.append(encontrar) 
            i+=1
        codones="".join(final)
        secuencianueva = open("secuencianueva.fasta","w")
        secuencianueva.write(nombre) 
        secuencianueva.write(str(codones))  
        secuencianueva.close()
        print("-------------------Menu-------------------")
        menu = int(input("ingrese 1 para obtener la proteina \ningrese 2 para obtener las estadisticas de la secuencia \ningrese 3 para generar un diagrama de relacion aa \ningrese 4 para terminar el programa \nseleccione una opcion: "))
    
    if menu == 2:
        A = 0 
        C = 0
        U = 0
        G = 0
#-------------------------------------------------------------------
        polares_sin_carga = 0
        apolares = 0
        polares_con_carga_positiva = 0
        polares_con_carga_negativa = 0
#-------------------------------------------------------------------
        i = 0
#-------------------------------------------------------------------
        while i != len(porcentaje):
            if porcentaje[i] == "A":
                A += 1
            if porcentaje[i] == "C":
                C += 1            
            if porcentaje[i] == "U":
                U += 1
            if porcentaje[i] == "G":
                G += 1
            i +=1
#-------------------------------------------------------------------
#polares sin carga
        i = 0
        while i != len(final):
            if final[i] == "S" or final[i] == "Y" or final[i] == "Q" or final[i] == "T" or final[i] == "C" or final[i] == "N":   
                polares_sin_carga +=1
#apolares
            if final[i] == "G" or final[i] == "A" or final[i] == "V" or final[i] == "L" or final[i] == "I" or final[i] == "F" or final[i] == "W" or final[i] == "M" or final[i] == "C" or final[i] == "P":
               apolares +=1
#polares con carga positiva
            if final[i] == "D" or final[i] == "E" or final[i] == "K" or final[i] == "R" or final[i] == "H":
                polares_con_carga_positiva +=1
#polares con carga negativa
            if final[i] == "D" or final[i] == "E":
                polares_con_carga_negativa +=1
            i +=1
#-------------------------------------------------------------------
       
        print("el total de codones es de ", len(codones2))
        codones2 = pd.Series(codones2)
        x= codones2.value_counts()
        print("a contiuancion se muestra el tipo de codon, cuantos hay y luego su porcentaje")
        print(x,"\n ", x/len(codones2*100))
                
#-------------------------------------------------------------------

        print("el numero de nucleotidos A es de", A, "y el porcentaje es", A*100/len(porcentaje))
        print("el numero de nucleotidos C es de", C, "y el porcentaje es", C*100/len(porcentaje))
        print("el numero de nucleotidos U es de", U, "y el porcentaje es", U*100/len(porcentaje))
        print("el numero de nucleotidos U es de", G, "y el porcentaje es", G*100/len(porcentaje))

#-------------------------------------------------------------------
        print("la cantidad de polares sin carga es", polares_sin_carga,"y su porcentaje es de",polares_sin_carga*100/len(final))
        print("la cantidad de polares con carga positiva es", polares_con_carga_positiva,"y su porcentaje es de",polares_con_carga_positiva*100/len(final))
        print("la cantidad de polares con carga negativa es", polares_con_carga_negativa,"y su porcentaje es de",polares_con_carga_negativa*100/len(final))
        print("la cantidad de apolares es", apolares,"y su porcentaje es de",apolares*100/len(final))
        
#-------------------------------------------------------------------

        print("-------------------Menu-------------------")
        menu = int(input("ingrese 1 para obtener la proteina \ningrese 2 para obtener las estadisticas de la secuencia \ningrese 3 para generar un diagrama de relacion aa \ningrese 4 para terminar el programa \nseleccione una opcion: "))
    
    if menu == 3:
        print(codones2)
        g = Digraph('G', filename='grafico.gv',format='png')
        g.attr('node', shape='circle')
        g.edge("AUG", codones2[0])
        for i in range (len(codones2)-1):
            g.attr('node', shape='circle')
            g.edge(codones2[i], codones2[i+1])

        for i in range (len(codones2)):
            g.attr('node', shape=('rectangle'))
            g.edge(codones2[i], str(diccionario2.get(codones2[i])), color='red')


        g.attr('node', shape='circle')
        g.edge(codones2[len(codones2)-1], "STOP")
        g.view()

        print("-------------------Menu-------------------")
        menu = int(input("ingrese 1 para obtener la proteina \ningrese 2 para obtener las estadisticas de la secuencia \ningrese 3 para generar un diagrama de relacion aa \ningrese 4 para terminar el programa \nseleccione una opcion: "))
