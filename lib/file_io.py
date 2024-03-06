def write_file(file_name, file_content):
    file_name_extension = f'{file_name}.txt'
    with open(file_name_extension, mode='w', encoding='utf-8') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    file_name_extension = f'{file_name}.txt'

    with open(file_name_extension, mode='a', encoding='utf-8') as file:
        file.write(append_content)


def read_file(file_name):
    file_name_extension = f'{file_name}.txt'

    with open(file_name_extension, encoding='utf-8') as file:
        return file.read()
