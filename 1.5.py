# Ex01
with open('names.txt') as file:
    print(max(file, key=len).strip())

# Ex02
with open('names.txt') as file:
    print(sum(len(line.strip()) for line in file))

# Ex03
with open('names.txt') as file:
    names = [name.strip() for name in file]
    min_length = min(len(name) for name in names)
    print("\n".join(name for name in names if len(name) == min_length))

# Ex04
with open('names.txt') as file, open('name_length.txt', 'w') as out:
    lengths = [len(line.strip()) for line in file]
    out.write('\n'.join(map(str, lengths)))

# Ex05
length = int(input("Enter name length: "))
with open('names.txt') as file:
    print('\n'.join([line.strip() for line in file if len(line.strip()) == length]))
