# FizzBuzz Microservice Edition

A scalable, containerised, microservice implementation of the prestigious [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) problem.

Inspired by [Kevlin Henney's "Get Kata" talk](https://www.youtube.com/watch?v=_M4o0ExLQCs).

## Why?

Because this:

```python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
            return 'Fizz'
     elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
```

Is _clearly_ a **naive** solution, which certainly does not _scale_ to a million users - which is of course necessary.

## Usage

After starting up the services (see below), perform a `GET` request to `localhost:5000/n` to receive the FizzBuzz of `n`:

```bash
$ curl -X GET http://localhost:5000/1
1
$ curl -X GET http://localhost:5000/3
Fizz
$ curl -X GET http://localhost:5000/5
Buzz
$ curl -X GET http://localhost:5000/15
FizzBuzz
```
### Local Development

Start up all services using Flask development server with hot reloading:

```bash
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

### Production

Start up all services using `gunicorn`:

```bash
$ docker-compose -f docker-compose.yml
```