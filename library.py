class Book:
    """定义一个书本类"""

    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    """定义一个图书馆类"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """向图书馆添加书本"""
        self.books.append(book)

    def find_book(self, title):
        """在图书馆中查找书本"""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def save_to_file(self, filename):
        """将图书馆中的书本信息保存到文件"""
        try:
            with open(filename, 'w') as f:
                for book in self.books:
                    f.write(f'{book.title},{book.author}\n')
        except Exception as e:
            print(f"Unable to save books to file: {e}")

    def load_from_file(self, filename):
        """从文件中加载书本信息到图书馆"""
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    title, author = line.strip().split(',')
                    self.add_book(Book(title, author))
        except Exception as e:
            print(f"Unable to load books from file: {e}")


# 创建一个图书馆实例
my_library = Library()

# 添加书本
my_library.add_book(Book('The Great Gatsby', 'F. Scott Fitzgerald'))
my_library.add_book(Book('To Kill a Mockingbird', 'Harper Lee'))

# 查找书本
book = my_library.find_book('The Great Gatsby')
if book:
    print(f"Found book: {book.title} by {book.author}")
else:
    print("Book not found")

# 保存到文件
my_library.save_to_file('books.txt')

# 从文件加载书本
my_library.load_from_file('books.txt')
