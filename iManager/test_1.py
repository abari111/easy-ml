from utils import check_executable, check_file_ext, check_files_ext




if __name__=="__main__":
    dir_path_1 = 'test/folder_1'
    dir_path_2 = 'test/folder_2'
    file_path = 'test/folder_1/names.txt'

    assert check_file_ext(file_path) == 'txt'
    assert check_executable(dir_path_2)
    assert not check_executable(dir_path_1)

    output = check_files_ext(dir_path_2)
    print(output)
    