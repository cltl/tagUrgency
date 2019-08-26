# TagUrgency

This repository provides a basic tagger which identifies words and expressions of urgency in text . The 
version: 0.1

Dependencies:

- Python3

Usage:

- python cnt_urgency.py input_directory
- some variables are hard-coded (see cnt_urgency.py "variables")

Input:

- Directory of text files; filenames ending in '.txt'

Output:

- screendump with information about number of processed files and total number urgency expressions
- csv file (_countUrgencyResults.csv) with number of urgency expressions per file

Expressions of urgency:

time=["binnenkort", "urgentie","meerdere malen","laatste","op tijd"," eerder "," gauw","dringend","meteen ","onmiddellijk", " snel ",  " spoedig ", "terstond" ,   "zojuist", " dadelijk" ," op dit moment " , "eenmalig ", "eenmalige "]
deon=[" moet","verplicht"," dient", " dienen", " moeten","genoodzaakt"]
lost=["vervelende consequenties", "geen toegang meer","geen betalingsregeling meer","betalingsachterstand","aanmaning","ongelezen","opheffen","afgekeurd","geen geld meer","schuld","naheffing","gerechtsdeurwaarder","beslag ","ongeldig", "verlopen", " vervalt", " verval ","schorsing", "erger", "verloopt", " verouderd","nadelig","geblokkeerd" ,"blokkade","blokkeren","blokkering","beperkt","gijzeling", "verouderd"]
action=["[hier]","let op","heraanvraag","voorkomen", "voorkom "," voorkomt ","klikken"," klik ", "[klik" , "opsturen","direct betalen","verifieer", "verifieert", "verifieren","voldoen", "voldoet", "start"]
gain=["kosteloos","deblokkeren","vervangen","beter beveiligd","gratis","vernieuwd","verbeterd" ,"toegang herstellen"]


Features Coming up:

Options:
- apply to single file instead of directory
- only string match or only lemma match
- option to set pointer to resource or to retrieve it from the resource itself


For questions contact:

isa.maks@vu.nl
