def analyze_text_sentiment(text):
    Positive_words={
        "good","great","happy","excellent","amazing","perfect","love","better",
        "well","intentional","caring","positive","pure","sharp","appreciate"
    }
    Negative_words={
        "bad","negative","poor","disappointed","angry","awful","sad","terrible","mad",
        "worst","broken","non-chalant","evil","dull","complicated"
    }
    vowels=set("aeiouAEIOU")
    puntuation=".,!?:;\"'(){}[]-_"

    positive_count=0
    negative_count=0
    words=text.lower().split()
    for word in words:
        cleaned=word.strip(puntuation)
        if cleaned in Positive_words:
            positive_count+=1
        elif cleaned in Negative_words:
            negative_count+=1
    vowel_count=0
    consonant_count=0
    for char in text:
        if char.isalpha():
            if char.lower() in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    vowel_run_count=0
    current_run=0
    for char in text:
        if char.isalpha()and char.lower() in vowels:
            current_run+=1
        else:
            if current_run>=3:
                vowel_run_count+=1
            current_run=0
    if current_run>=3:
        vowel_run_count+=1
    has_vowelruns=vowel_run_count>0

    Sentiment_score=positive_count-negative_count
    if Sentiment_score>0:
        Sentiment_label="Positive"
    elif Sentiment_score<0:
        Sentiment_label="Negative"
    else:
        Sentiment_label="Neutral"
    return{
        "Positive_words":positive_count,
        "Negative_words":negative_count,
        "vowels":        vowel_count,
        "consonants":   consonant_count,
        "vowel_runs":   vowel_count,
        "has_vowelruns":has_vowelruns,
        "Sentiment_score":Sentiment_score,
        "Sentiment_label":Sentiment_label
    }
def print_stats(label,stats):
    print(f"\n{label}")
    print(f"Positive words: {stats['Positive_words']}")
    print(f"Negative words: {stats['Negative_words']}")
    print(f"Vowels: {stats['vowels']}")
    print(f"Consonants: {stats['consonants']}")
    print(f"Vowel runs (3+ in a row): {stats['vowel_runs']}")
    print(f"Sentiment score: {stats['Sentiment_score']}")
    print(f"Sentiment label: {stats['Sentiment_label']}")
def compare_texts(text1,text2):
    stats1=analyze_text_sentiment(text1)
    stats2=analyze_text_sentiment(text2)
    print_stats("Text 1",stats1)
    print_stats("Text 2",stats2)
    print("\nComparison")
    if stats1["Sentiment_score"] > stats2["Sentiment_score"]:
        print("Text 1 is more positive.")
    elif stats2["Sentiment_score"] > stats1["Sentiment_score"]:
        print("Text 2 is more positive.")
    else:
        print("Both texts have equal sentiment.")
if __name__=="__main__":
    favouritesong_lyric=(
        """Should I confiscate your cellphone Are you done with typing,"
        I don't appreciate comments Where you talk about me Said it's complicated
        honey I can't phoking shout it A-little drummer girl
        Beating my drum for you Pum pum pum pum. I don't want a piece of you
        I want it all I want it all Can't have just a piece of you It breaks my heart,
        It breaks my heart First off So it ain't enough So when they ask me 
        What's my status I think for about 5 minutes And I say it's complicated.""")
    motivational_quote=("""You might not be perfect, but you are capable of great things.
                        Most importantly,love yourrself.""")
    complaint_message=("""I'm giving a negative review because the delivery service was 
                       terrible.This is the worst thing I have experienced yet.""")
    
    print("ANALYZING: Favourite Song Lyrics")
    print_stats(f"\nFavourite Song Lyrics", analyze_text_sentiment(favouritesong_lyric))

    print(f"\nANALYZING: Motivational Quote")
    print_stats("Motivational Quote", analyze_text_sentiment(motivational_quote))

    print("\nANALYZING: Complaint Message")
    print_stats("Complaint Message", analyze_text_sentiment(complaint_message))

    print("\nCOMPARING: Motivational Quote vs Complaint Message")
    compare_texts(motivational_quote, complaint_message)

    print("\nCOMPARING: Favourite Song Lyric vs Motivational Quote")
    compare_texts(favouritesong_lyric,motivational_quote)

    print("\nCOMPARING: Favourite Song Lyric vs Complaint Message")
    compare_texts(favouritesong_lyric, complaint_message)