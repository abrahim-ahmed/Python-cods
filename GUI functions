
def searchButtonPress(event=None):
    global searchEntry
   
    # Getting the input
    query = searchEntry.get()
    # Stemming
    query = ' '.join(stem_words(word_tokenize(query)))
    query_vec = vectorizer.transform([query])

    # search
    startTime = time.time()
    results = cosine_similarity(X, query_vec).reshape((-1,))
    endTime = time.time()
    
    nbresults = (results != 0).sum()

    # set info
    updateInfo(nbresults, (endTime - startTime)*10**3)

    fillList(results)


def updateInfo(numResults, time):
    global numResultsLabel
    global timeLabel

    numResultsLabel.configure(text=(str(numResults) + " Results"))
    timeLabel.configure(text=("Time: " + str(int(time)) + "ms"))


def fillList(results):
    global data
    global searchList
    global frame

    # clear list
    searchList.pack_forget()
    searchList.destroy()

    searchList = customtkinter.CTkScrollableFrame(
        master=frame, fg_color='#ebecec')
    searchList.pack(padx=10, pady=10, fill="both", expand=True)
        
    count = 0
    for i in results.argsort()[-10:][::-1]:
        temFrame = customtkinter.CTkFrame(master=searchList)
        temFrame.pack(padx=10, pady=10, fill="x")

        headline = customtkinter.CTkLabel(
            master=temFrame, text=df_news.iloc[i,0], font=("Arial", 18), wraplength=1200)
        headline.pack(padx=5, pady=2)

        if len(df_news.iloc[i,1]) != 0:
            short_description = customtkinter.CTkLabel(
                master=temFrame, text=df_news.iloc[i,1], font=("Arial", 16), wraplength=1200)
            short_description.pack(padx=5, pady=2)

        if len(df_news.iloc[i,2]) != 0:
            authors = customtkinter.CTkLabel(
                master=temFrame, text="Authors: " + df_news.iloc[i,2], wraplength=1200)
            authors.pack(padx=5, pady=2)

        count += 1
        if count >= 20:
            break

def imNotFeelingLuckyButtonPress():
    global vectorizer
    global searchEntry

    set_text(searchEntry, random.choice(list(vectorizer.vocabulary_.keys())))
    searchButtonPress()

def set_text(entry, text):
    entry.delete(0, customtkinter.END)
    entry.insert(0, text)


# ------------------------------------============================= UI =============================------------------------------------



customtkinter.set_appearance_mode("light")

root = customtkinter.CTk()

root.title("beda Search")

root.geometry("1280x720")
frame = customtkinter.CTkFrame(
    master=root, width=1280, height=720, fg_color='white')
frame.pack(fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text="beda Search", font=("Arial", 150))
label.pack(pady=12, padx=10)

searchEntry = customtkinter.CTkEntry(
    master=frame, height=50, width=550, corner_radius=50, font=("Arial", 22))
searchEntry.bind('<Return>', searchButtonPress)
searchEntry.pack(pady=12, padx=10)

# ---=== start button frame ===--- #

buttonsFrame = customtkinter.CTkFrame(
    master=frame, width=500, fg_color='white')
buttonsFrame.pack()

searchButton = customtkinter.CTkButton(
    master=buttonsFrame, text="beda Search engine", width=200, height=50, font=("Arial", 18), fg_color='#f8f9fa', hover_color='#c5c6c6', text_color='#202124', command=searchButtonPress)
searchButton.pack(pady=12, padx=10, side='left')

imNotFeelingLuckyButton = customtkinter.CTkButton(
    master=buttonsFrame, text="randem search", width=200, height=50, font=("Arial", 18), fg_color='#f8f9fa', hover_color='#c5c6c6', text_color='#202124', command=imNotFeelingLuckyButtonPress)
imNotFeelingLuckyButton.pack(pady=12, padx=10, side='left')

# ---=== end button frame ===--- #

# ---=== start info frame ===--- #

infoFrame = customtkinter.CTkFrame(master=frame, width=400, fg_color='white')
infoFrame.pack(pady=12, padx=10)

numResultsLabel = customtkinter.CTkLabel(
    master=infoFrame, text="0 Results", font=("Arial", 16))
numResultsLabel.pack(padx=50, pady=6, side='left')
# ---=== start Time results info frame ===--- #
timeLabel = customtkinter.CTkLabel(
    master=infoFrame, text="Time: 0ms", font=("Arial", 16))
timeLabel.pack(padx=50, pady=6, side='right')

# ---=== end info frame ===--- #

searchList = customtkinter.CTkScrollableFrame(master=frame, fg_color='#ebecec')
searchList.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
