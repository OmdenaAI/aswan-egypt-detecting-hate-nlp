# Clean Datasets

This folder will contain all clean datasets. 

Please create a folder for each clean dataset and name it following the repository's naming conventions. Name the dataset file with their name as indicated in the raw datasets' table. Feel free to add a README.md with details on the dataset and yourself. 

Those unsure about how to use GitHub and/or unwilling to modify the repository structure can simply send their clean datasets to @CaterinaBi on Slack.

## Pre-processing guidelines

### File structure

The output of the pre-processing has to be a .cvs file. Please create one file for each dataset.

The file will be organised in 5 columns as follows:

 | corpus_name | raw_sentence | label | clean_sentence_EDA | clean_sentence_training |
  |-|-|-|-|-|
 | | | | | |
 | | | | | |
  
 Please respect the column order and naming.
 
 ### Labels
 
 The labels will be:
 - '1' for hateful sentences;
 - '2' for non hateful sentences.

If your dataset contains labels diffent from 'hateful' and 'non hateful' (e.g., 'abusive'), please *keep the original labels*.

### Preprocessing

