from collections import namedtuple, deque


Marks = namedtuple('Marks', ['Algebra', 'Geometry', 'History', 'Informatics', 'Geography'])

marks = deque([
    Marks(9, 10, 9, 11, 11),
    Marks(6, 7, 7, 6, 12),
    Marks(10, 10, 11, 10, 11),
    Marks(5, 6, 5, 5, 4)
])

for mark in marks:
    print(mark)