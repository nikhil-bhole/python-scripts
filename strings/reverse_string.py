def reverse_string_with_loop(str):
    reverse = ""
    for i in str:
        reverse = i + reverse
    return reverse

#print(reverse_string_with_loop("banana"))

def reverse_string(str):
    return str[::-1]

print(reverse_string("python is awesome"))
