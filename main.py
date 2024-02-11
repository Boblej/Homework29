class SchoolObject:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def calculate_average_grade(self, grades):
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)

class Mathematics(SchoolObject):
    def __init__(self, topic):
        super().__init__('математика', 5)
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def calculate_average_grade(self, grades):
        if len(grades) == 0:
            return 0
        weighted_sum = sum(grades * topic.difficulty for grades, topic in zip(grades, self.topics))
        total_difficulty = sum(topic.difficulty for topic in self.topics)
        return weighted_sum / total_difficulty

class Literature(SchoolObject):
    def __init__(self, difficulty):
        super().__init__('литература', 4)
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def calculate_average_grade(self, grades):
        if len(grades) == 0:
            return 0
        weighted_sum = sum(grades * book.difficulty for grades, book in zip(grades, self.books))
        total_difficulty = sum(topic.difficulty for topic in self.books)
        return weighted_sum / total_difficulty

class Topic:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

class Book:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

math = Mathematics(3)
math.add_topic(Topic("Алгебра", 2))
math.add_topic(Topic("Геометрия", 3))

lit = Literature(2)
lit.add_book(Book("Пушкин", 5))
lit.add_book(Book("Толстой", 4))

math_grades = [5, 4, 3]
lit_grades = [4, 5, 3]

print(math.calculate_average_grade(math_grades))
print(lit.calculate_average_grade(lit_grades))
