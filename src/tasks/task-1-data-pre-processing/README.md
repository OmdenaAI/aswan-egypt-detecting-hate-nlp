# Task 1: Data Pre-Processing

## Task Guidelines

### File structure

The output of the pre-processing has to be a .cvs file. Please create one file for each dataset.

The file will be organised in 5 columns as follows:

 | corpus_name | raw_sentence | label | clean_sentence_training | clean_sentence_EDA |
  |-|-|-|-|-|
 | | | | | |
 | | | | | |
  
 Please respect the column order and naming. For the corpus name, please use the same label you use as a name for your directory (e.g., HateXplain).
 
 ### Labels
 
 > Please note that the labels have changed!
 
 The labels will be:
 - '2' for RISKY sentences (eg., 'hateful' or 'abusive');
 - '1' for POTENTIALLY RISKY sentences (e.g., 'offensive)';
 - '0' for NON RISKY sentences.

We leave to the collaborators the task to determine how to fit the original labels in the three classes above. Please contact the task leaders if unsure about the classification. We'll be most happy to help you decide how to re-label your dataset.

### Preprocessing

The pre-processing for the 'clean_sentence_training' column will involve the following steps:

1- delete all rows containing null values;

2- stopwords removal;

3- removal of digits and words containing digits, punctuation and special characters, extra spaces, links;

4- lemmatization (no NOT perform stemming at it can yield undesirable results).

Please do NOT change the case of your sentences as the distinction between lowercase and uppercase can be meaningful in this context.

The pre-processing for the 'clean_sentence_EDA' will involve all the steps above, *plus the deletion of all emojis* (if present).

## Task Table

Please modify the table below to register all activity within the task folder. Use your GitHub pseudo in the 'author name' field whenever possible.

Add rows if necessary.

| Activity | Activity Name | Author Name | Details |
|-|-|-|-|
|1| pre-processing | Vishu Kalier | completed (1 dataset) |
|2| file integration | Caterina Bonan | in progress |
|3| pre-processing | Caterina Bonan | in progress (3 datasets) |
|4| pre-processing | Hyacinth Ampadu | completed (1 dataset) |
|5| pre-processing | Ameya Chaudhari | completed (3 datasets) |
|6| script sharing | Ameya Chaudhari | completed |
|7| script sharing | Hyacinth Ampadu | completed |
|8|         |         |         |
|9|         |         |         |
|10|        |         |         |
