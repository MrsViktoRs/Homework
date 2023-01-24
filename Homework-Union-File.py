name_file = '1.txt'
name_file2 = '2.txt'
name_file3 = '3.txt'
with open('1.txt', 'r', encoding='utf-8') as file_one:
    f1 = file_one.readlines()
with open('2.txt', 'r', encoding='utf-8') as file_two:
    f2 = file_two.readlines()
with open('3.txt', 'r', encoding='utf-8') as file_three:
    f3 = file_three.readlines()
with open('4.txt', 'w', encoding='utf-8') as file_four:
    if len(f1) < len(f2) and len(f3):
        file_four.write(name_file + '\n')
        file_four.write(str(len(f1)) + '\n')
        file_four.writelines(f1)
        file_four.write('\n')
        if len(f2) < len(f3):
            file_four.write(name_file2 + '\n')
            file_four.write(str(len(f2)) + '\n')
            file_four.writelines(f2)
            file_four.write('\n')
            file_four.write(name_file3 + '\n')
            file_four.write(str(len(f3)) + '\n')
        else:
            file_four.write(name_file3 + '\n')
            file_four.write(str(len(f3)) + '\n')
            file_four.writelines(f3)
            file_four.write(name_file2 + '\n')
            file_four.write(str(len(f2)) + '\n')
            file_four.writelines(f2)
    if len(f2) < len(f1) and len(f3):
        file_four.write(name_file2 + '\n')
        file_four.write(str(len(f2)) + '\n')
        file_four.writelines(f2)
        file_four.write('\n')
        if len(f1) < len(f3):
            file_four.write(name_file + '\n')
            file_four.write(str(len(f1)) + '\n')
            file_four.writelines(f1)
            file_four.write('\n')
            file_four.write(name_file3 + '\n')
            file_four.write(str(len(f3)) + '\n')
            file_four.writelines(f3)
        else:
            file_four.write(name_file3 + '\n')
            file_four.write(str(len(f3)) + '\n')
            file_four.writelines(f3)
            file_four.write('\n')
            file_four.write(name_file + '\n')
            file_four.write(str(len(f1)) + '\n')
            file_four.writelines(f1)
    if len(f3) < len(f1) and len(f2):
        file_four.write(name_file3 + '\n')
        file_four.write(str(len(f3)) + '\n')
        file_four.writelines(f3)
        file_four.write('\n')
        if len(f1) < len(f2):
            file_four.write(name_file + '\n')
            file_four.write(str(len(f1)) + '\n')
            file_four.writelines(f1)
            file_four.write('\n')
            file_four.write(name_file2 + '\n')
            file_four.write(str(len(f2)) + '\n')
            file_four.writelines(f2)
        else:
            file_four.write(name_file2 + '\n')
            file_four.write(str(len(f2)) + '\n')
            file_four.writelines(f2)
            file_four.write('\n')
            file_four.write(name_file + '\n')
            file_four.write(str(len(f1)) + '\n')
            file_four.writelines(f1)