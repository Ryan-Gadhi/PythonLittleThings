

def emojy_adder(msg):
    msg = str(msg).split(" ")
    output =''
    emojies = makeEojieDic()
    for word in msg:
        output += emojies.get(word,word)+' '
    return output


def get_emojies():
    file = open('emojies.txt','r')
    data = file.read()
    return data

def makeEojieDic():
    emojiesDic = {}
    data = get_emojies()
    data = data.split('\n')
    for line in data:
        emoji, string = line.split(' ')
        emojiesDic[string]=emoji
    return emojiesDic


def update_emoji_adder(emoji, string):
    file = open('emojies.txt','a')
    file.write('\n'+emoji+' '+string)
    pass


while(1):
    print('\nChoose a function to do:'
          '\n\n \tto write something, press (1)'
          '\n\n \tto show emoji bank, press (2)'
          '\n\n \tto add an emoji, press (3)'
          '\n\n \tto exit, press (0)')


    choice = input()
    if choice == '3':
        emoji = input('\n Ok, insert an emoji: ')
        string= input('\n nice! choose a string for that: ')
        update_emoji_adder(emoji, string)
        get_emojies()
    elif choice == '2':
        print('\n---- emoji bank:\n')
        print(get_emojies())
    elif choice == '1':
        print(emojy_adder(input()))
    elif choice == '0':
        print('\nthank you')
        exit(0)


# ---------------