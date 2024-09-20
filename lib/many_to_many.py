
class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        self._contracts = [] 
        Author.all_authors.append(self)

    def add_contract(self,contract): 
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise Exception("must be an instance of Contract Class")
    def contracts(self):
        return self._contracts 
    def books(self):
        return[contract.book for contract in self._contracts]
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.title = title
        self._contracts = []
        Book.all_books.append(self)
    def add_contract(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise Exception("must be an instance of Contract class")
    def contracts(self):
        return self._contracts
    def authors(self):
        return[contract.author for contract in self.contracts()]

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book Class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance (royalties, int):
            raise Exception("Royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.author.add_contract(self)
        self.book.add_contract(self)
        Contract.all_contracts.append(self)
    @classmethod
    def contracts_by_date(cls, date):
        newlist = [] 
        for contract in cls.all_contracts:
            if contract.date == date:
                newlist.append(contract)
        print(newlist)
        return newlist
        