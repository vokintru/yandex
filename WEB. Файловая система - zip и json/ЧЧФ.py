def human_read_format(size):
    if size <= 1023:
        return f'{size}Б'
    size /= 1024
    if size <= 1023:
        return f'{round(size)}КБ'
    size /= 1024
    if size <= 1023:
        return f'{round(size)}МБ'
    size /= 1024
    if size <= 1023:
        return f'{round(size)}ГБ'


print(human_read_format(1023))
print(human_read_format(15000))
