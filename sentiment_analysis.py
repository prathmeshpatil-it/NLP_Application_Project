from textblob import TextBlob

text = input("Enter text: ")
analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    print("Positive")
elif analysis.sentiment.polarity < 0:
    print("Negative")
else:
    print("Neutral")
