import argparse

from src.main import main

parser = argparse.ArgumentParser("在这里写程序名")

group = parser.add_mutually_exclusive_group()

# 必选功能
group.add_argument('-t', '--test', action='store_true', help='test mode')
group.add_argument('--demo_func', action='store_true',
                   help='求input的乘方')

#可选功能
parser.add_argument('--input',
                    action='store',
                    type=str,
                    help='输入变量')

args = parser.parse_args()

if __name__ == '__main__':
    print(args)
    main(args)