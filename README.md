# TagUrgency

This repository provides a basic tagger which identifies words and expressions of urgency in text. The expressions are classified in 5 different categories: Time, Loss, Gain, Deontic, Action.

The tagger has been developed to detect phishing mails. More information can be found here: https://github.com/cltl/tagUrgency/blob/master/Phishingmails.pdf


Version: 0.1

Dependencies:

- Python3

Usage:

- python cnt_urgency.py input_directory

Variables:

Some variables can be modified (see cnt_urgency.py "variables")
- threshold = 1          (used for classification , refers to number of urgency_expressions per text; n>=threshold is --phishing, n< threshold = non-phishing)
- min_fsz = 200          (files smaller than min_fsz kb will be discarded)
- max_fsz = 5000         (files larger than max`_fsz kb will be discarded)

Input:

- Directory of text files; filenames ending in '.txt'

Output:

- screendump with information about number of processed files and total number urgency expressions
- csv file (_countUrgencyResults.csv) with number of urgency expressions per file


For questions contact:

isa.maks@vu.nl
