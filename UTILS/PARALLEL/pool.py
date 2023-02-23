import glob
import sys

from functools import reduce

def count_lines_in_file(filename):
    """
    Function that returns the number of lines
    of text in the file 'filename'
    """
    with open(filename) as f:
        return len(f.readlines())

# get all of the names of the plays from the command line
filenames = sorted(glob.glob(f"{sys.argv[1]}/*"))

# map the count_lines function against all of the
# files listed in "filenames"
play_line_count = list(map(count_lines_in_file, filenames))

# Now print out all of the totals
string_results = map(lambda x, y: "%s contains %s lines" % (x, y), filenames, play_line_count)

# Join the list of strings using a newline character
# and print to screen.
print("\n".join(string_results))

total = reduce(lambda x,y: x+y, play_line_count)

print("The total number of lines is %s." % total)