def dups(input_list):
    seen={}
    duplicates=[]

    for item in input_list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen[item]=True
    return duplicates

def main():
    num=[]
    print("Enter elements (press Enter without input to finish):")
    while True:
        user_input=input("Enter an element: ")
        if user_input == "":
            break
        num.append(user_input)
    if not num:
        print("No elements were entered!")
        return
    duplicate_list = dups(num)

    print("\nOriginal list:", num)
    if duplicate_list:
        print("Duplicates found:", duplicate_list)
    else:
        print("No duplicates found!")

if __name__ == "__main__":
    main()