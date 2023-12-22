# Calculate the sum of squares of given integers, excluding any negatives.
# The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
# Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
# For each test case, calculate the sum of squares of the integers, excluding any negatives, and print the calculated sum in the output.
# Note: There should be no output until all the input has been received.
# Note 2: Do not put blank lines between test cases solutions.
# Note 3: Take input from standard input, and output to standard output.

# Do not use any for loop, while loop, or any list / set / dictionary comprehension

def process_string(input_string):
    lines = input_string.split('\n')
    lines.pop(0)
    new_string = '\n'.join(lines)
    return new_string

def sum_of_squares(iter, input):
  iter_count = int(iter)
  if iter_count == 0:
    return 0
  
  index = iter_count - 1
  elements = input.split(" ")
  square = int(elements[index]) * int(elements[index])
  return square + sum_of_squares(iter_count-1, input) 

def recursive_wrapper(iter, input):
  if int(iter) == 0:
    return 0

  input_length = input.split("\n")[0]

  # Process the string and remove the entry for input length
  raw_string = process_string(input)
  
  sum = sum_of_squares(input_length, raw_string)
  print('sum of squares: ', sum)

  # Process the string again to remove the entry
  raw_string = process_string(input)

  return sum + recursive_wrapper(int(iter) - 1, raw_string)

def main():
  string = "1\n3\n3 1 4"
  input_elements = string.split("\n")[0]

  # Process the string and remove the entry for number of inputs
  raw_input = process_string(string)
  return recursive_wrapper(input_elements, raw_input)

if __name__ == "__main__":
  ans = main()
  print('final ans: ', ans)

