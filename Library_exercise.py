class Item:
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

    def get_info(self):
        pass


class Book(Item):
    def __init__(self, title, publication_year, author, num_pages):
        super().__init__(title, publication_year)
        self.author = author
        self.num_pages = num_pages

    def get_info(self):
        print(
            f'The book {self.title} written by {self.author} in the year {self.publication_year} has a number of {self.num_pages} pages')


class Magazine(Item):
    def __init__(self, title, publication_year, issue, editor):
        super().__init__(title, publication_year)
        self.issue = issue
        self.editor = editor

    def get_info(self):
        print(
            f'The title of the magazine is {self.title} from editor {self.editor} from the year {self.publication_year} released in {self.issue}')


class DVD(Item):
    def __init__(self, title, director, publication_year, duration):
        super().__init__(title, publication_year)
        self.director = director
        self.duration = duration

    def get_info(self):
        print(f'The title of the DVD is {self.title} directed by {self.director} from the year {self.publication_year} has a duration of {self.duration} minutes')


book1 = Book('Find Waldo', 2020, 'Steph John', 60)
magazine1 = Magazine('Forbes', 2024, 5, 'New York Editor')
dvd1 = DVD('Godzilla', 'John Doe', 1999, 192)

items = [book1, magazine1, dvd1]

for item in items:
    item.get_info()


