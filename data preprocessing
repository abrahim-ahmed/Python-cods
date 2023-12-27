    # turn to lowercase

X['lowerd_text'] = [(entryH + ' ' + entryS + ' ' + entryA).lower() for entryH, entryS, entryA in zip(X['headline'], X['short_description'], X['authors'])]
X['word_tokenize'] = [word_tokenize(entry) for entry in X['lowerd_text']]

# stemming
X['word_tokenize'] = [stem_words(list(entry)) for entry in X['word_tokenize']]
