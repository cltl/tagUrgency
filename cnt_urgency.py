# Detecting expresssions of urgency in text per urgency category (i.e. time, deon, lost, action, gain)
# Counting expressions of urgency per document per urgency category
# Classifying the documents (e.g. emails) as phishing or non phishing
# The program can be run with 1 argument (srcdir)


import os
import sys
from nltk.tokenize import sent_tokenize, word_tokenize
import collections


versionnr = '0.1'


# input and output
## documents in srcdir with filenames ending in ".txt" will be processed
## output will be directed at the console and outputfile
srcdir=sys.argv[1]
outputfile=srcdir+"_countUrgencyResults.csv"

# variables
threshold = 1          # used for classification , refers to number of urgency_expressions per text; n>=threshold is phishing, n< threshold = non-phishing
max_files=400000       # max. number of files that is processed
min_fsz = 200          # files smaller than min_fsz kb will be discarded
max_fsz = 5000         # files larger than max`_fsz kb will be discarded

# lists with urgency expressions
time=["binnenkort", "urgentie","meerdere malen","laatste","op tijd"," eerder "," gauw","dringend","meteen ","onmiddellijk", " snel ",  " spoedig ", "terstond" ,   "zojuist", " dadelijk" ," op dit moment " , "eenmalig ", "eenmalige "]
deon=[" moet","verplicht"," dient", " dienen", " moeten","genoodzaakt"]
lost=["vervelende consequenties", "geen toegang meer","geen betalingsregeling meer","betalingsachterstand","aanmaning","ongelezen","opheffen","afgekeurd","geen geld meer","schuld","naheffing","gerechtsdeurwaarder","beslag ","ongeldig", "verlopen", " vervalt", " verval ","schorsing", "erger", "verloopt", " verouderd","nadelig","geblokkeerd" ,"blokkade","blokkeren","blokkering","beperkt","gijzeling", "verouderd"]
action=["[hier]","let op","heraanvraag","voorkomen", "voorkom "," voorkomt ","klikken"," klik ", "[klik" , "opsturen","direct betalen","verifieer", "verifieert", "verifieren","voldoen", "voldoet", "start"]
gain=["kosteloos","deblokkeren","vervangen","beter beveiligd","gratis","vernieuwd","verbeterd" ,"toegang herstellen"]
urgDict = {}
urgDict["time"] = time
urgDict["lost"] = lost
urgDict["deon"] = deon
urgDict["action"] = action
urgDict["gain"] = gain





def process_file(f,cnt):
    # read email
    f = open(f, 'r')
    lines = f.readlines()

    # initialize counters for urgency expressions
    for ucat in urgDict:
        cnt[ucat] = 0

    # count occurrences of urgency words per category in mail (per line)
    for l in lines:
        snt=sent_tokenize(l)
        for s in snt:
            for ucat in urgDict:
                for e in urgDict[ucat]:
                    if e in s:
                        cnt[ucat]+=1
    return(cnt)



def classify(fdict,threshold):
    cnt=collections.Counter()
    for f in fdict:
        total=sum(fdict[f].values())
        if total >= threshold:
            cnt['phish']+=1
        else:
            cnt['nonphish']+=1
    outline= "\nclassified as phishing\t\t: {} docs".format(cnt['phish'])
    outline=outline+"\nclassified as non-phishing\t\t: {} docs".format(cnt['nonphish'])
    outline=outline+"\ntotal documents:{}; threshold:>={}".format(len(fdict), threshold)
    print(outline)


def stats_per_file_specs(fdict, outputcsv):
    # report extra statistics per file (mail) such as filename and number of urgency expressions
    sep = ";"
    header = "fn" + sep + "totals" + sep
    for uc in urgDict:
        header = header + uc + sep
    outfile = open(outputcsv, 'w+', encoding='utf-8')  # Trying to create a new file or open one
    outfile.write(header)

    for f in fdict:
        fline = "\n"+f + sep + str(sum(fdict[f].values()))
        for key in fdict[f]:
            fline = fline + sep + str(fdict[f][key])

        outfile.write(fline)
    outfile.close()
    print("\nDetails can be found in {}".format(outputcsv))





def process_dir(srcdir):
    # Initialize counters for words in categories (per folder)
    cntFolder = collections.Counter()
    fcounter = 0
    fdict = {}
    fdictsize={}
    print(srcdir)
    cf=0
    # Collect stats per file
    for (dir, _, files) in os.walk(srcdir):
        for f in files:
            cf+=1
            if f.endswith(".txt"):
                fsz = os.stat(dir + f).st_size
                fdictsize[f] = fsz
                if min_fsz <= fsz <= max_fsz:
                    fcounter += 1
                    cnt = collections.Counter()
                    fdict[f] = process_file(dir + "/" + f, cnt)
                    cntFolder.update(cnt)
        print("total number of files = {} \ntotal number of processed files = {} \nnumber of  discarded files = {} (with minsize={}kb or maxsize={}kb)".format(cf,fcounter,cf-fcounter,min_fsz,max_fsz))


    # Calculate and print stats per srcdir
    print("\nnr of files processed", len(fdict))
    print("total number of urgency expressions", sum(cntFolder.values()))
    for c in cntFolder:
        print("{}\ttotal number of occurrences: {}".format(c, cntFolder[c]))


    # Classify a document as phishing or non-phishing
    classify(fdict, threshold)
    # print other stats per file
    stats_per_file_specs(fdict, outputfile)





def main():
    if len(sys.argv) < 1:
        print('Error: please provide the input folder with documents to be processed')
    else:
        process_dir(sys.argv[1])



if __name__ == "__main__":
        main();

