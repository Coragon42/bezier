from os import system

def main():
    '''Turns bitmap into svg (requires Potrace: https://potrace.sourceforge.net/, https://potrace.sourceforge.net/README)'''
    file = input('Enter black and white ppm file name with extension: ')
    name = file.split('.')[0]
    system(f'potrace -t 4 {file} --svg -o {name}.svg') # you can view svgs by opening them with a browser

main()