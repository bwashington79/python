acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
acronyms.append('IMHO')

print(acronyms[3])
print(acronyms[3-1])
print(acronyms[4])

# Check if val in list

if "FOO" in acronyms:
    print('True')
else:
    print("False")

# Loop example
for acronym in acronyms:
    print(acronym)