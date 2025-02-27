# models/sentiment_analysis.py

from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes sentiment of the given text using TextBlob.
    Returns a dictionary with polarity and subjectivity scores.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    }

if __name__ == "__main__":
    sample_text = "The market is showing promising growth with new opportunities emerging."
    result = analyze_sentiment(sample_text)
    print("Sentiment Analysis:", result)
