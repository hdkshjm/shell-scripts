# display diff for pasting excel sheet...
import sys

with open(sys.argv[1]) as f:
  left = set(f.read().splitlines())
with open(sys.argv[2]) as f:
  right = set(f.read().splitlines())

only_left = left - right
only_right = right - left
common = left & right

print("line", sys.argv[1], sys.argv[2], sep="\t")

for line in common:
  print(line, "OK", "OK", sep="\t")

for line in only_left:
  print(line, "OK", "", sep="\t")

for line in only_right:
  print(line, "", "OK", sep="\t")
