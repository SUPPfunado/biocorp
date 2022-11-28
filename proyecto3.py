from io import open

def secuencia(secuencia_nueva):
    start = ["AUG"]
    stop = ["UAG","UGA","UAA"]
    i = 0
    terminar = True
    
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
diccionario = {"GCU":"A","GCC":"A", "GCA":"A","GCC":"A", "CGU":"R", "GCG":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", "AAU":"N", "AAC":"N", "GAU":"D", "GAC":"D", "UGU":"C", "UGC":"C", "CAA":"Q","CAG":"Q", "GAA":"E", "GAC":"E", "GGU":"G","GGC":"G","GGA":"G","GGG":"G", "GAU":"H", "CAC":"H",  "AUU":"I", "AUG":"I", "AUA":"I", "UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L", "AAA":"K","AAG":"K", "AUG":"M", "UUU":"F","UUC":"F", "CCU":"P","CCC":"P","CCA":"P","CCG":"P", "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S", "ACU":"T","ACC":"T","ACA":"T","ACG":"T", "UGG":"W", "UAU":"Y","UAC":"Y"  ,"UGG":"W","GUU":"V","GUC":"V","GUA":"V","GUG":"V"}
codones=[]
datos = open(input("ingrese el nombre del archivo junto a su extencion(.txt): ")) # write or read
#nombre=datos.readline()
secuencia_nueva = datos.read()
sequence = []

j = 0
while j != len(secuencia_nueva):
    sequence.append(secuencia_nueva[j])
    if sequence[j] == "T":
        sequence[j] = "U"
    j+=1
stop = True
i = 0
largo = len(sequence)
while stop:
    if sequence[i] == "I":
        sequence.remove(sequence[i])
        largo-=1
        while sequence[i] != "F":
            sequence.remove(sequence[i])
            largo-=1
        sequence.remove(sequence[i])
        largo-=1
    i+=1
    if i >= largo:
        stop =False  


secuencia_nueva = "".join(sequence)
secuencia_ = secuencia(secuencia_nueva)
final = []
i = 0
while i != len(codones):
    if codones[i] in diccionario:
        encontrar = diccionario.get(codones[i])
        i+=1
        final.append(encontrar)


codones="".join(final)
secuencianueva = open("secuencianueva.fasta","w")
secuencianueva.write(str(codones))  

