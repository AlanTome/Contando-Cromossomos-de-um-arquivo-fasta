def ler_fasta(arquivo):
    sequencia = ''
    lista = []
    with open(arquivo, 'r') as fasta:
            sequencia = ''
            for linha in fasta:
                if not linha.startswith('>'):
                    sequencia += linha
            lista.append(sequencia)

    return lista

lista = ler_fasta("sequence.fasta")

for i in lista:
    print("A quantidade de cromossomos A é: ",i.count("A"))
    print("A quantidade de cromossomos C é: ",i.count("C"))
    print("A quantidade de cromossomos T é: ",i.count("T"))
    print("A quantidade de cromossomos G é: ",i.count("G"))
    print()
    
soma1 = i.count("A")
soma2 = i.count("C")
soma3 = i.count("T")
soma4 = i.count("G")

total = soma1+soma2+soma3+soma4

print("A média dos cromossomos A é: {:.3f}%".format((soma1/total)*100))
print("A média dos cromossomos C é: {:.3f}%".format((soma2/total)*100))
print("A média dos cromossomos T é: {:.3f}%".format((soma3/total)*100))
print("A média dos cromossomos G é: {:.3f}%".format((soma4/total)*100))




    

