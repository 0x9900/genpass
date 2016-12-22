#! /usr/bin/env python
#
# Dependency:
# pip install keyring
#
# Fred C. http://github.com/0x9900/
#
"""
Generate a passworg base on the domain name of a website, your
userid on this website and a key.

The first time you use this program it will as you a key. This key
will be stored in your Mac keychain.

Examples:

]$ ./genpassword fred www.yahoo.com
yahoo.com: Password: vk61-borA-wlIu-BYSK
]$ ./genpassword fred yahoo.com
yahoo.com: Password: vk61-borA-wlIu-BYSK
]$ ./genpassword fred YAHOO.COM
yahoo.com: Password: vk61-borA-wlIu-BYSK

"""
from __future__ import print_function
import getpass
import os
import random
import sys

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from hashlib import sha256
from urlparse import urlparse

import keyring

PASSWD_LEN = 19
ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'

def normalize_url(url):
  """Extract the domain name from the url, remove the leading www and
  return the domain name in lower case"""
  url = urlparse(url)
  url = url.netloc or url.path
  url = url.lower().replace('www.', '')
  return url

def get_key(program, token='Password Generator'):
  """Try to find the encryption key for that token in the keyring. If
  the key cannot be found prompt the user.

  """
  key = keyring.get_password(program, token)

  # the key hasn't been found in the keyring. Request for a new one.
  if not key:
    key = getpass.getpass('Encryption key: ')
    try:
      keyring.set_password(program, token, key)
    except keyring.errors.PasswordSetError as exp:
      print(exp, file=sys.stderr)

  return str(key)

def parse_arguments():
  """Parse the command arguments"""
  parser = ArgumentParser(
    description="Password generator",
    epilog=globals()['__doc__'],
    formatter_class=RawDescriptionHelpFormatter
  )
  parser.add_argument('-i', '--interactive', action="store_true",
                      default=False,
                      help="Do not use key stored in the keychain")
  parser.add_argument('username', nargs=1,
                      help="Site username")
  parser.add_argument('url', nargs=1,
                      help="Site's domain name http://example.com/")
  opts = parser.parse_args()
  opts.username = opts.username.pop()
  opts.url = normalize_url(opts.url.pop())


  return opts

def main():
  """This is where everything happens"""
  opts = parse_arguments()
  if opts.interactive:
    key = getpass.getpass('Encryption key: ')
  else:
    program_name = os.path.basename(sys.argv[0])
    key = get_key(program_name)
  seed = sha256(opts.url + key + opts.username).hexdigest()
  random.seed(seed)
  charlist = [c for c in ALPHABET]
  random.shuffle(charlist)
  password = ''.join([c if i%5 else '-' for i, c in
                      enumerate(charlist[:PASSWD_LEN], 1)])
  if os.isatty(sys.stdout.fileno()):
    print("Site: {}: Password: {}".format(opts.url, password))
  else:
    sys.stdout.write(password)
    sys.stdout.flush()


if __name__ == '__main__':
  main()
