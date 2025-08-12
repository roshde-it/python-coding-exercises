# WEEK 6
# binary conversion table

start = int(input('Start: '))
stop = int(input('Stop: '))



# Create the binary conversion table, saving it to table.txt.

with open('table.txt', 'w') as table_file:
    for i in range(start, stop):
        table_file.write('{:08b} is {}\n'.format(i, i))



# Read and display the contents of the file.
table_file_readonly = open('table.txt', 'r')
print(table_file_readonly.read(), end='')