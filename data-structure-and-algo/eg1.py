p = (4, 5)
x, y = p


data = ['ACME', 50, 20, 3, (34, 4, 5)]
name, share, price, other = data


s = 'Hello'
a, b, c, d, e = s


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('dave', 'dave@example.com', '86765444', '8765555')
name, email, *phone_number = user_record

*trailing, current = [9, 8, 8, 75, 6, 643, 3, 6]

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


