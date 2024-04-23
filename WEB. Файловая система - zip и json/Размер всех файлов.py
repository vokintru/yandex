import os


def cff(file, size):
    out = file + " "
    if size <= 1023:
        out += f'{size}Б'
        return out
    size /= 1024
    if size <= 1023:
        out += f'{round(size)}КБ\n'
        return out
    size /= 1024
    if size <= 1023:
        out += f'{round(size)}МБ\n'
        return out
    size /= 1024
    if size <= 1023:
        out += f'{round(size)}ГБ\n'
        return out


def get_files_sizes():
    files = os.listdir()
    out = ''
    for file in files:
        size = os.path.getsize(file)
        out += cff(file, size) + "\n"
    return out

# print(get_files_sizes())
