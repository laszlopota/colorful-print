# Print colorful text
def cprint(text, **kwargs):
    kvPairs = {'color': 'white'}
    for key, value in kwargs.items():
        kvPairs[key] = value

    colors = {'red': '\033[91m',
              'green': '\033[92m',
              'blue': '\033[94m',
              'yellow': '\033[93m',
              'purple': '\033[95m',
              'white': '\033[0m',
              'black': '\033[90m'}

    print(colors[kvPairs['color']] + str(text) + '\033[0m')

# Print text with colorful background
def bprint(text, **kwargs):
    kvPairs = {'color': 'white'}
    for key, value in kwargs.items():
        kvPairs[key] = value

    colors = {'red': '0;30;41',
              'green': '0;30;42',
              'blue': '0;30;44',
              'yellow': '0;30;43',
              'purple': '0;30;45',
              'white': '0;30;47'}

    backgroundColor = colors[kvPairs['color']]
    print(f'\x1b[{backgroundColor}m' + str(text) + '\x1b[0m')


if __name__ == '__main__':
    cprint('This is a colored text.', color='red')
    bprint('The background of this text is colored.', color='green')
