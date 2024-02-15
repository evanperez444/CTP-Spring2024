from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I hate how pickles taste.")

print(res)
