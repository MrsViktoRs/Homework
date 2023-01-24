with open('1.txt', 'r', encoding='utf-8') as file1:
    f1 = file1.readlines()
with open('2.txt', 'r', encoding='utf-8') as file2:
    f2 = file2.readlines()
with open('3.txt', 'r', encoding='utf-8') as file3:
    f3 = file3.readlines()
dict_ = {'1.txt': len(f1), '2.txt': len(f2), '3.txt': len(f3)}
dict_values = sorted(dict_.values())
dict_files = {}
for i in dict_values:
    for w in dict_.keys():
        if dict_[w] == i:
            dict_files[w] = dict_[w]
            break
with open('4.txt', 'w', encoding='utf-8') as file4:
    for name_file in dict_files:
        with open(name_file, 'r', encoding='utf-8') as file:
            f = file.readlines()
            file4.write(name_file + '\n')
            file4.write(str(len(f)) + '\n')
            file4.writelines(f)
            file4.write('\n')
print(dict_files)