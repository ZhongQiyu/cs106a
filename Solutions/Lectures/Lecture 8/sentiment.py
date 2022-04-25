import nltk.sentiment
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
# this is a structure called directory-subdirectory-class in the subdirectory.
# in this case, 'nltk' is the directory that contains the subdirectory 'sentiment',
# and SentimentIntensityAnalyzer is a class in the subdirectory. A class is an
# organic set of functions that represents a certain type of object's behaviors.
# I am happy to go over this more if you find interesting and convenient to learn!


def main():
    while True:
        # it is better to extract the text as a variable
        prompt = 'How do you feel? '
        user_text = input(prompt)
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        print(f"I guess your reaction is {reaction}.")
        print(f"Roughly your score of mentality is {score}.")
        print('')


def get_reaction(score):
    """
    Parameter score: a float between -1 and +1
    Return: An emoji as a string!
    """
    # be careful about using if-elif-else chain
    if score > 0.5:
        return "🥰"
    elif score > 0:
        return "🙂"
    elif score == 0:
        return "😶"
    elif score < -0.5:
        return "😢"
    else:  # elif score < 0:
        # be careful that for lower bounds we start conditioning on values
        # that are large in absolute values, so that the 'else' part in
        # conditioning can exert its function
        return "😟"


def get_sentiment(user_text):
    """
    Parameter user_text: any text (string)
    Return: a sentiment score between -1 and +1 (float)
    """
    # 1. pass the text into the analyzer.polarity_scores function, part of the nltk package
    scores = analyzer.polarity_scores(user_text)
    # 2. extract the sentiment score. Scores is a "dictionary" (covered on May 17th)
    sentiment_score = scores['compound']

    return sentiment_score


if __name__ == '__main__':
    main()
