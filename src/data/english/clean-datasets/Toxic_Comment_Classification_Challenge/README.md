# Clean Toxic_Comment_Classification_Challenge Dataset

The dataset was from kaggle, and there were 3 files, train.csv, test.csv and test_labels.csv.
Eventually I merged all 3 into one dataframe
There were 8 columns, which were id, comment_text, toxic, severe_toxic, obscene, threat, insult and identity_hate.
Aside the id and comment text(which had obvious values), the rest had binary values, 1 or 0, 0 meaning that comment doesnt belong to that category and 1 meaning it belonged
After my checks, i concluded that texts that had all 0s would be put in the non risky category, texts that had toxic and insult being 1 and the rest 0 put in the potentially risk, and the rest(mostly all 1s) put in the too risky category
Digits, words containing digits, punctuations, special characters, extra spaces and links were all removed from the texts
There were no null values, and stopwords were removed and lemmatization was applied.
No emojis were present, so the column for clean_sentence_EDA and clean_sentence_training would be the same.
