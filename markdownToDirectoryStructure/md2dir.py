import os
import shutil
# dir = os.path.dirname(__file__)
dir = '/Users/tanvirkhan/Desktop/notes/note'

dir2 = '/Users/tanvirkhan/Desktop/notes/note/md-files2dir'

all_files = os.listdir(dir)
print(all_files)

total_dir_list = []
for file in all_files:
    if file.endswith('.md'):
        print(file)
        original_file_path = os.path.join(dir, file)
        file_name = file.split('.')[0]
        print(file_name)
        if '-' in file_name:
            file_name = file_name.split('-')
            print(file_name)
            # file_path = os.path.join(dir2, file_name[0])
            # print(file_path)
            for i in range(len(file_name)-1):
                if i == 0:
                    file_path = os.path.join(dir2, file_name[i])
                    print(file_path)

                    total_dir_list.append(file_path)

                    if not os.path.exists(file_path):
                        os.mkdir(file_path)
                        total_dir_list.append(file_path)
                else:
                    file_path = os.path.join(file_path, file_name[i])
                    print(file_path)

                    total_dir_list.append(file_path)

                    if not os.path.exists(file_path):
                        os.mkdir(file_path)
            print(f'------------------')
            print(f'copying {original_file_path} to {file_path}')
            shutil.copy2(original_file_path, file_path)
        else:
            print(file_name)
            file_path = os.path.join(dir2, file_name)
            total_dir_list.append(file_path)
            print(file_path)
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            print(f'------------------')
            shutil.copy2(original_file_path, file_path)
