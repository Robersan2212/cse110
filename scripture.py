max_chapter = -1
with open ( 'books_and_chapters.txt' ) as book_file:
    for line in book_file: 
        parts = line.strip().split(":")
        book = parts[0]
        chapter = int(parts [1])
        scripture = parts[2].strip()
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
        if chapter > max_chapter:
            max_chapter = chapter
            book_max = book

print(f'The book with more chapters is: {book_max} ')
print (f'It contains {max_chapter} chapters in the book.')