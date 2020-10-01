import requests
import hashlib
# import sys


def request_api_data(chars):
    url = f"https://api.pwnedpasswords.com/range/{chars}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"error code: {response.status_code}")
    return response


def get_pword_leak_count(hash, hash_to_check):
    lis = (line.split(':') for line in hash.text.splitlines())
    for h, count in lis:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_hash = (hashlib.sha1(password.encode('utf-8'))).hexdigest().upper()
    first5_char, rest = sha1_hash[:5], sha1_hash[5:]
    res = request_api_data(first5_char)
    return get_pword_leak_count(res, rest)


psword = input('password: ')
count = pwned_api_check(psword)
if count:
    print(f'''{psword} has occured {count} times...
you should consider to change it''')
else:
    print('its too safe😊')
print('done')

"""def main(args):
    for i in args:
        count = pwned_api_check(i)
        if count:
            print(f'''{i} has occured {count} times...
you should consider to change it''')
        else:
            print('All good broii')
        print('done')


main(sys.argv[1:])
"""
