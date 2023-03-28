def get_tgAPI():
    sf = open('settings.txt', 'r')
    setfile = sf.readlines()
    return setfile[0].split()[1]


def get_channels():
    sf = open('settings.txt').readlines()
    links = list(map(lambda x: x.split()[1].strip(), sf[3:]))
    return links


def add_channel(link):
    string = len(open('settings.txt').readlines()) - 2
    sf = open('settings.txt', '+a')
    sf.write(f'\nChannel_{string}: {link}')
    sf.close()


def change_gpt_key(new_key: str):
    sf = open('settings.txt').readlines()
    sf[1] = f'ChatGPT_API: {new_key}\n'
    with open('settings.txt', 'w') as F:
        F.writelines(sf)


def delete_channel(link):
    index = ''
    sf = open('settings.txt').readlines()
    for i in sf:
        if link == i.split()[1]:
            index = sf.index(i)
    sf = open('settings.txt').readlines()
    if index != '':
        sf.pop(index)
    sf[-1] = sf[-1].strip()
    with open('settings.txt', 'w', encoding='utf-8') as F:
        F.writelines(sf)


def get_admin_password():
    sf = open('settings.txt').readlines()
    data = sf[2].split()[1]
    return data


def change_admin_password(new):
    sf = open('settings.txt').readlines()
    sf[2] = f'AdminPassword: {new}\n'
    with open('settings.txt', 'w') as F:
        F.writelines(sf)