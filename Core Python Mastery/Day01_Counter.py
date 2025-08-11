# 🧠 Objective:
# Develop a Python script that reads a given text  and analyzes word frequency using the `collections.Counter` class.
# This is a fundamental task in text processing and forms the basis for more advanced applications like search engines,
# chatbots, and natural language processing (NLP) systems.
from collections import Counter
import re
text = """
In the age of information, data is everywhere.
But raw data alone is meaningless — it’s the patterns, the insights, the questions we ask of the data that give it value.
Python, being a versatile and powerful language, enables us to extract this value efficiently.

Can you count how often each word appears in this paragraph?
Let’s find out — and remember: case, punctuation, and repetition all matter!
"""
# Lets start with normilization of input
new_text = text.lower()
new_text = re.sub(r'([^\w\s])', r' \1 ', text)
new_text = re.sub(r'\s+', ' ', new_text)
new_text = new_text.strip()
new_text= new_text.split(sep=' ')

counting = Counter(new_text)
print(counting)


