# Remove Duplicates From List

def remove_duplicates(input_list):
    return list(set(input_list))


# Example usage
input_list = input("Enter elements of the list separated by spaces: ")
input_list = input_list.split()
print("List after removing duplicates:", remove_duplicates(input_list))