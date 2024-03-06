import os, sys
from config import DB_DETAILS


def main():
    """Program takes at least one argument"""
    env = sys.argv[0].strip(".py")
    db_details = DB_DETAILS[env]


if __name__ == '__main__':
    main()
