from prefixes_and_suffixes import prefixes, suffixes

def longest_prefix():

    max_length = 0
    max_length_string = ""

    for key in prefixes:

        if len(prefixes[key]) > max_length:
            max_length = len(prefixes[key])
            max_length_string = prefixes[key]

    return(max_length_string)

def make_longest_string():
    
    longest_string = ""
    longest_prefix = "seventy-three"
    key = 41

    while key in suffixes:
        longest_string += longest_prefix+ suffixes[key] + " "
        key -=1

    print(len(longest_string))
    print(longest_string)

make_longest_string()