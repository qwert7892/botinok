def count_user(id):
    db = open('db.txt', 'r+')
    file = db.readlines()
    if len(file) != 0:
        for i in file:
            if i.split()[0] == id:
                index = file.index(i)
                line = i
                break
    db.close()
    line_ls = line.split()
    new = [line_ls[0], str(int(line_ls[1]) + 1), line_ls[2], line_ls[3]]
    f = open('db.txt').readlines()
    f.pop(index)
    f[-1] = f[-1].strip()
    with open('db.txt', 'w') as F:
        F.writelines(f)
    add_user(new[0], new[1], new[2], new[3])


def change_status(id):
    db = open('db.txt', 'r+')
    file = db.readlines()
    if len(file) != 0:
        for i in file:
            if i.split()[0] == id:
                index = file.index(i)
                line = i
                break
    db.close()
    line_ls = line.split()
    new = [line_ls[0], line_ls[1], 'yes', line_ls[3]]
    f = open('db.txt').readlines()
    f.pop(index)
    f[-1] = f[-1].strip()
    with open('db.txt', 'w') as F:
        F.writelines(f)
    add_user(new[0], new[1], new[2], new[3])


def change_status_2(id):
    db = open('db.txt', 'r+')
    file = db.readlines()
    if len(file) != 0:
        for i in file:
            if i.split()[0] == id:
                index = file.index(i)
                line = i
                break
    db.close()
    line_ls = line.split()
    new = [line_ls[0], line_ls[1], line_ls[2], 'yes']
    f = open('db.txt').readlines()
    f.pop(index)
    f[-1] = f[-1].strip()
    with open('db.txt', 'w') as F:
        F.writelines(f)
    add_user(new[0], new[1], new[2], new[3])


def get_count(id):
    db = open('db.txt', 'r+')
    file = db.readlines()
    for i in file:
        if i.split()[0] == id:
            return i.split()[1]


def get_status(id):
    db = open('db.txt', 'r+')
    file = db.readlines()
    for i in file:
        if i.split()[0] == id:
            return i.split()[2]


def get_status_2(id):
    db = open('db.txt', 'r+')
    file = db.readlines()
    for i in file:
        if i.split()[0] == id:
            return i.split()[3]


def add_user(id, count=0, status='no', status_2='no'):
    db = open('db.txt', 'r+')
    file = db.readlines()
    for i in file:
        if i.split()[0] == id:
            return False
    db.write(f'\n{id} {count} {status} {status_2}')
    db.close()
    return True
