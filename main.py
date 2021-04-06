# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from spider import spider_jjwxc_novel, spider_zhxsw_novel, spider_52shuku_novel


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def saveJjwxc():
    spider_jjwxc_novel.save()
def saveZhxsw():
    spider_zhxsw_novel.save()
def save52sk():
    spider_52shuku_novel.save()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    save52sk()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
