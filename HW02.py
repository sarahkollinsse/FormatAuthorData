#Sarah Kollins, Jared Hofer, Michael Supeck, Zack Leytze
#CSE 211 B Group 17
#2-26-18
#Purpose: take in information from a text file and put that info in a dictionary
#Homework 02
#Python 3

#Problems with homework:
#There is an issue with adding different types of library reference(ex: book, journal,and conference)
#I know why I have the error but didn't have time to fix it

#Opens files
step1=open("Step1Data.txt",'r')
step2=open("Step2Data.txt",'r')
step3=open("Step3Data.txt",'r')

#Creates dictionary
dict= {}

#loops through first file
def addToDict(file):
    for line in file:
        info_title=line.strip()
        print(info_title)
        if(info_title=='Book'):
            book(file)
        elif(info_title=='Journal'):
            journal(file)
        elif(info_title=='Conference'):
            conference(file)


#adds keys and values of book library reference
def book(file):
    for line in file:
        category=line.split(":")[0].strip()
        if(category!='Book'):
            info = line.split(":")[1]
            if (category == "Key"):
                key = info.strip()
            elif (category == "Author"):
                author = info.strip()
            # last_first=author.split()
            # author=last_first[1]+", "+last_first[0]
            elif (category == "Title"):
                title = info.strip()
            elif (category == "Publisher"):
                publisher = info.strip()
            elif (category == "Date"):
                date = info.strip()
        else:
            referenceBook = "{}, {}, {}, {}.".format(author, title, publisher, date)
            dict[key] = referenceBook
#adds keys and values of journal library reference
def journal(file,type):
    for line in file:
        c = line.split()
        category=line.split(":")[0].strip()
        if(":"in c[0]):
            info = line.split(":")[1]
            if (category == "Key"):
                key = info.strip()
            elif (category == "Author"):
                author = info.strip()
            # last_first=author.split()
            # author=last_first[1]+", "+last_first[0]
            elif (category == "Title"):
                title = info.strip()
            elif (category == "Publisher"):
                publisher = info.strip()
            elif (category == "Date"):
                date = info.strip()
            elif (category == "Journal"):
                journal = info.strip()
            elif (category == "Volume"):
                volume = info.strip()
            elif (category == "Number"):
                number = info.strip()
        else:
            referenceJournal = "{}, {}, {}, {}:{}({}), {}.".format(author, title, journal, publisher,volume,number,date)
            dict[key] = referenceJournal

#adds keys and values of conference library reference
def conference(file):
    for line in file:
        c=line.split()
        category = line.split(":")[0].strip()
        if(":" in c[0]):
            info = line.split(":")[1]
            if (category == "Key"):
                key = info.strip()
            elif (category == "Author"):
                author = info.strip()
            # last_first=author.split()
            # author=last_first[1]+", "+last_first[0]
            elif (category == "Title"):
                title = info.strip()
            elif (category == "Date"):
                date = info.strip()
            elif (category == "Conference"):
                conference = info.strip()
            elif (category == "Location"):
                location = info.strip()
            elif (category == "Pages"):
                pages = info.strip()
        else:
            referenceConference = "{}, {}, {}, {}, {}, {}.".format(author, title, conference, date,location,pages)
            dict[key] = referenceConference

#add file input to dictionary
#addToDict(step1)
#addToDict(step2)
addToDict(step3)

#User input
reference=input("Lookup a library reference with key: ")
print(dict.get(reference,""))

