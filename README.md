# fourequalsfour
When does six equal three, three equal five, five equal four, and four equal four? When `len('six') == 3`, `len('three') == 5`, `len('five') == 4`, and so on. Through this function, everything ultimately decomposes to `len('four') == 4`.

My question is, what spelled-out number is the greatest number of decompositions from `len('four') == 4`? Mathematically, is there a theoretical limit to the number of decompositions? I have no idea. However, it's been a fun coding challenge and I'm looking forward to optimizing my code.

## how it works

With five functions, and two dictionaries.

### functions

`delim(int)` takes an integer and parses it into chunks ready to be appended with the appropriate mathematical suffix.

`textnum(arr)` takes a list of integers converted to strings and first substitutes the appropriate spelled-out number for each chunk and then concatenates the correct mathematical suffix.

`num_count(str)` is a simple program that takes the spelled-out number and counts the total letters within, returning an integer. Useful for iterating through the previous steps.

`decay_num(int)` takes an integer and, using the above three functions, returns a list containing `[input, input spelled out, total decay cycles]`. This can be used on it's own to determine the number of decay cycles it takes a particular integer to decay to `len('four') == 4`.

`print_decay(int)` clearly formats and prints the decay cycle of an integer.

`max_decay(x,y,z=1,pass_through=False)` brute-forces through a range of numbers and returns which one has the highest decay cycles, and then returns the first number along with its decay cycle. All numbers with the max decay cycle are appended to `max_list`. if `pass_through` remains `False`, the function will only print out the first integer and it's full decay cycle, along with a count (but not values) of other values that share the same cycle. If `pass_through=True`, the function returns `max_iter`,`max_list` as a tuple.

### dictionaries

At first I was interested in using [inflect](https://pypi.org/project/inflect/), but figured that I wanted as many possible word combinations as possible. `inflect` can translate only numbers up to 32 digits long; this meant that some suffixes were being left on the table! Techically there are infinite mathemtacial suffixes, but [Wikipedia's page on names of large numbers](https://en.wikipedia.org/wiki/Names_of_large_numbers) offers conescutive suffixes up to quadragintillion, which allows consecutive spelled-out integers to a maximum of 126 positions. 

`suffixes` contains all of those said suffixes, and `prefixes` contains every number < 1000 that those suffixes may append to. Both are found in the aptly named `prefixes_and_suffixes.py`.

### examples

    max_decay(0,1000000)
    
      Range:(0 : 1000000)
      Maximum iterations: 6
      Origin(s): 323

      three hundred twenty-three equals 23
      twenty-three equals 11
      eleven equals 6
      six equals 3
      three equals 5
      five equals 4
      four equals 4
    
    print(max_decay(0,50, pass_through=True))   
    
      (5, [23, 27, 28, 33, 37, 38])

and the numbers can get pretty big. Maybe unreasonably big.


      Range:(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 : 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
      Maximum iterations: 6
      Origin: 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

      nine duotrigintillion nine hundred ninety-nine untrigintillion nine hundred ninety-nine trigintillion nine hundred ninety-nine novemvigintillion nine hundred ninety-nine octovigintillion nine hundred ninety-nine septemvigintillion nine hundred ninety-nine sesvigintillion nine hundred ninety-nine quinvigintillion nine hundred ninety-nine quattuorvigintillion nine hundred ninety-nine tresvigintillion nine hundred ninety-nine duovigintillion nine hundred ninety-nine unvigintillion nine hundred ninety-nine vigintillion nine hundred ninety-nine novemdecillion nine hundred ninety-nine octodecillion nine hundred ninety-nine septendecillion nine hundred ninety-nine sexdecillion nine hundred ninety-nine quindecillion nine hundred ninety-nine quattuordecillion nine hundred ninety-nine tredecillion nine hundred ninety-nine duodecillion nine hundred ninety-nine undecillion nine hundred ninety-nine decillion nine hundred ninety-nine nonillion nine hundred ninety-nine octillion nine hundred ninety-nine septillion nine hundred ninety-nine sextillion nine hundred ninety-nine quintillon nine hundred ninety-nine quadrillion nine hundred ninety-nine trillion nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine equals 1117
      one thousand one hundred seventeen equals 30
      thirty equals 6
      six equals 3
      three equals 5
      five equals 4
      four equals 4
