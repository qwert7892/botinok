def get_tgAPI():
    sf = open('settings.txt', 'r')
    setfile = sf.readlines()
    return setfile[0].split()[1]


def get_channels():
    sf = open('settings.txt').readlines()
    links = list(map(lambda x: 'https://t.me/' + x.split()[1].strip(), sf[2:]))
    return links


def add_channel(link):
    string = len(open('settings.txt').readlines()) - 1
    sf = open('settings.txt', '+a')
    sf.write(f'\nChannel_{string}: {link}')
    sf.close()


def delete_channel(link):
    index = ''
    sf = open('settings.txt').readlines()
    for i in sf:
        if link in i:
            index = sf.index(i)
    sf = open('settings.txt').readlines()
    if index != '':
        sf.pop(index)
    sf[-1] = sf[-1].strip()
    with open('settings.txt', 'w') as F:
        F.writelines(sf)



delete_channel('botinok_test3')