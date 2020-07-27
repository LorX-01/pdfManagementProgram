#Scrivere un programma che gestisca i pdf


import PyPDF2
import os
import shutil

#----------------  OGGETTI  CON VALORE DI RITORNO LE FOLDERS ---------------- 

cartellainputmerge = os.path.join(os.getcwd(), "inputfile/daunire/")
cartellainputsplit = os.path.join(os.getcwd(), 'inputfile/dadividere/')

cartellaoutputmerge = os.path.join(os.getcwd(), 'outputfile/uniti/')
cartellaoutputsplit = os.path.join(os.getcwd(),'outputfile/divisi/')

#----------------  OGGETTI  CON VALORE DI RITORNO LE FOLDERS ---------------- 



#-------------------------------------- FUNZIONI --------------------------------------
def unionepdf(nomefiles):
        listafiles = os.listdir("./inputfile/daunire/")
        print(listafiles)
        pdfoutput = open((cartellaoutputmerge + nomefiles),"wb")
        merger = PyPDF2.PdfFileMerger()

        for nomeFile in listafiles:
            if nomeFile.endswith(".pdf"):
                PdfFile = open((cartellainputmerge + nomeFile),"rb")
                readerPDF = PyPDF2.PdfFileReader(PdfFile)
                merger.append(readerPDF)
                PdfFile.close()
        merger.write(pdfoutput)
        merger.close()
        
        print("Unione completata con successo!")



def  divisionepdf():
    listafiles = os.listdir("./inputfile/dadividere/")
    print(listafiles)
    for nomeFile in listafiles:
        if nomeFile.endswith(".pdf"):
            filebase = nomeFile.replace(".pdf","")
            letturapdf = PyPDF2.PdfFileReader((cartellainputsplit + nomeFile))
            for numeropagine in range(letturapdf.numPages):
                writer = PyPDF2.PdfFileWriter()
                writer.addPage(letturapdf.getPage(numeropagine))
                if not os.path.exists(cartellaoutputsplit + filebase):
                    os.makedirs(cartellaoutputsplit + filebase)
                with open(os.path.join(cartellaoutputsplit + filebase, "{0}_Pagina{1}.pdf".format(filebase,numeropagine + 1)),'wb') as f:
                    writer.write(f)
                    f.close()
    print("Divisione PDF completata con successo!!!")
                
#-------------------------------------- FUNZIONI --------------------------------------


#-------------------------------------- CONTROLLO CARTELLE --------------------------------------

if os.path.exists(cartellainputmerge):
    print("Cartella input esistente")
    checkcartellainput = True
elif os.path.exists(cartellainputmerge) == False:
    print("Cartella input non esistente")
    checkcartellainput = False
    if checkcartellainput == False:
        os.makedirs(cartellainputmerge)
        print("Cartella input creata con successo")
        checkcartellainput = True

if os.path.exists(cartellaoutputmerge):
    print("Cartella output esistente")
    checkcartellaoutput = True
elif os.path.exists(cartellaoutputmerge) == False:
    print("Cartella output non esistente")
    checkcartellaoutput = False
    if checkcartellaoutput == False:
        os.makedirs(cartellaoutputmerge)
        print("Cartella output creata con successo")
        checkcartellaoutput = True

if os.path.exists(cartellainputsplit):
    print("Cartella input split esistente")
    checkcartellasplitinput = True
elif os.path.exists(cartellainputsplit) == False:
    print("Cartella input split non esistente")
    checkcartellasplitinput = False
    if checkcartellasplitinput == False:
        os.makedirs(cartellainputsplit)
        print("Cartella input split creata con successo")
        checkcartellasplitinput= True

if os.path.exists(cartellaoutputsplit):
    print("Cartella output split esistente")
    checkcartellasplitoutput = True
elif os.path.exists(cartellaoutputsplit) == False:
    print("Cartella output split non esistente")
    checkcartellasplitoutput = False
    if checkcartellasplitoutput == False:
        os.makedirs(cartellaoutputsplit)
        print("Cartella output split creata con successo")
        checkcartellasplitoutput= True

#-------------------------------------- CONTROLLO CARTELLE --------------------------------------


#-------------------------------------- MAIN PROGRAM--------------------------------------

if os.path.exists(cartellainputmerge) and os.path.exists(cartellaoutputmerge):
    print("Tutte le cartelle  sono presenti. Non sono necessarie apportare ulteriori modifiche ")
    while True:
        scelta = int(input("Scegli la modalita': \n \
            1: Unire due o piu' PDF \n \
            2:Splittare un PDF in tanti file quante sono le pagine  \n \
            3 o superiore: Esci dal programma \n \
            Fai la tua scelta: "))
            
    
        if scelta == 1:
            file = str(input("Inserisci i file all'interno della cartella 'inputfile' (y,n):  "))
            if file == "y"or file == "Y":
                if os.listdir("./inputfile/daunire/") == []:
                    print("Non e' presente nessun file compatibile... Riprova!")
                    continue
                else:   
                    varnome = str(input("Scrivi il nome con cui vorresti salvare il file: "))
                    unionepdf((varnome + ".pdf"))
                    scelta2 = int(input("Vuoi utilizzare ancora il programma o vuoi uscire? (1 o 2): "))
                    if scelta2 == 1:
                        continue

        elif scelta == 2:
            file1 =  str(input("Inserisci i file all'interno della cartella 'inputfile' (y,n):  "))
            if file1 == "y" or file1 =="Y":
                if os.listdir("./inputfile/dadividere/") == []:
                    print("Non e' presente nessun file compatibile... Riprova!")
                    continue
                print("Bene")
                divisionepdf()

            elif file1 == "n" or file1 == "N":
                    continue
    


        if scelta >= 3:
            break 


#-------------------------------------- MAIN PROGRAM--------------------------------------