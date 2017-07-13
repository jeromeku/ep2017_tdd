# TDD

I often need to manage lists of dictionaries (NoSQL-style), and I'd like to have a
structure that can contains them and allows me to perform some changes and filters on them.

I want it to behave like a list

``` python
d = dr.DictRegister()

d.append({'a': 1, 'b': 2})
```

I want to also be able to initialize it with an already existing list

``` python
d = dr.DictRegister([
    {'a': 1, 'b': 2},
    {'a': 5, 'c': 6},
    {'b': 3, 'c': 9}
])
```

I need a `find()` method that selects all the dictionaries that contain a given key

``` python
d = dr.DictRegister([
    {'a': 1, 'b': 2},
    {'a': 5, 'c': 6},
    {'b': 3, 'c': 9}
])

d.find('a') -> d = dr.DictRegister([
    {'a': 1, 'b': 2},
    {'a': 5, 'c': 6},
])
```

The `find()` method shall also be able to select all the dictionaries with a given key/value pair

``` python
d = dr.DictRegister([
    {'a': 1, 'b': 2, 'c': 4},
    {'a': 5, 'b': 6, 'c': 4},
    {'b': 3, 'c': 9}
])

d.find(c=4) -> dr.DictRegister([
    {'a': 1, 'b': 2, 'c': 4},
    {'a': 5, 'b': 6, 'c': 4}
])
```

Last, the `find()` method shall support a special syntax that allows to find all the dictionaries with a given key with a value greater than a given one.

``` python
d = dr.DictRegister([
    {'a': 1, 'b': 2, 'c': 4},
    {'a': 5, 'b': 6, 'c': 4},
    {'b': 3, 'c': 9}
])

d.find(b__gt=3) -> dr.DictRegister([     {'a': 5, 'b': 6, 'c': 4} ])
```

# Mocks

We have an external service that provides data in a JSON format. To interact with that service we wrote a helper class called `RestService` that exposes the only two endpoints of that service, namely `list()` and `get()`.

The server returns data in JSON format, so our class converts it to Python structures.

Unfortunately the server behind the service is very slow, and we cannot use it for the tests. Moreover, we want to be sure that we call the service with the right parameters.

# Refactoring

We need to quickly come up with some statistics on our data, so someone in our team wrote a very quick and mostly untested class called `DataStats`, that provides a single method `stats`. There is one test that injects some fixed data and checks the correctness of the output.

We want to refactor the class, i.e. to split the big method in smaller, tested methods preserving the functionality.