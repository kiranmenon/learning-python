ex1.py : Write a generator which computes the running average.

ex2.py : Write a generator frange, which behaves like range but accepts float values.

ex3.py : Write a generator trange, which generates a sequence of time tuples from start to stop incremented by step. A time tuple is a 3-tuple of integers: (hours, minutes, seconds) So a call to trange might look like this: trange((10, 10, 10), (13, 50, 15), (0, 15, 12) )

ex4.py : Write a version "rtrange" of the previous generator, which can receive messages to reset the start value.

ex5.py : Write a program, using the newly written generator "trange", to create a file "times_and_temperatures.txt". The lines of this file contain a time in the format hh::mm::ss and random temperatures between 10.0 and 25.0 degrees. The times should be ascending in steps of 90 seconds starting with 6:00:00. For example:

06:00:00 20.1
06:01:30 16.1
06:03:00 16.9
06:04:30 13.4
06:06:00 23.7
06:07:30 23.6
06:09:00 17.5
06:10:30 11.0

ex6.py :  Write a generator with the name "random_ones_and_zeroes", which returns a bitstream, i.e. a zero or a one in every iteration. The probability p for returning a 1 is defined in a variable p. The generator will initialize this value to 0.5. In other words, zeroes and ones will be returned with the same probability.

ex7.py : Implement below using generator

countries = ["Germany", "Switzerland", "Austria"]
country_iterator = cycle(countries)
for i in range(7):
    print(next(country_iterator))

o/p:
Germany
Switzerland
Austria
Germany
Switzerland
Austria
Germany


