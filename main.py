import csv
# comma sperated value

with open("YA_Books.csv",mode="r") as bookfile:
    # mode "r"  means read 
    

    books = csv.reader(bookfile)
   #skip heder row:
    next(books)
    most_recent_published =0 # starting low so that we actually capture  the first book
    most_rated=5.0
    lowest_rated=0.0
    for book in books:
        title=book[0]
        author=book[1]
        # print all the authors that begin with the letter" M"
        # if author.startswith("M"):
        #   print(author) 

        # get most recently published book
        year = int(book[2])
        if year > most_recent_published:
            most_recent_published = year
            most_recent_book = book

        # get book with worst rating:
        rated = float(book [6])
        if rated < most_rated:
            most_rated=rated
            most_rated_book=book
   
       # what is the highest rating for any book in the data set
        rated = float(book[6])
        if rated > lowest_rated:
            lowest_rated=rated
            lowest_rated_book=book

            

    print(f"Most recently publsihed: {most_recent_book}")
    print(f"Most recently publsihed: {most_rated_book}")
    print(f"Most recently publsihed: {lowest_rated_book}")