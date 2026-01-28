def binary_to_decimal_builtin(binary_string):
  """
  Converts a binary string to its decimal integer equivalent using the int() function.
  """
  try:
    decimal_number = int(binary_string, 2)
    return decimal_number
  except ValueError:
    return "Invalid binary input"

# Example usage:
binary_input = "1101"
decimal_output = binary_to_decimal_builtin(binary_input)
print(f"The decimal equivalent of {binary_input} is {decimal_output}")

binary_input_2 = "101001"
decimal_output_2 = binary_to_decimal_builtin(binary_input_2)
print(f"The decimal equivalent of {binary_input_2} is {decimal_output_2}")
