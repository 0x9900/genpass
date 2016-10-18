# genpass
Generate Internet Password

Generate a passworg base on the domain name of a website, your userid
on this website and a key.

This tool we generate the same password for a given use and domain
name as long as you use the same key.

The first time you use this program it will as you a key. This key
will be stored in your Mac keychain.

_Examples:_

```
]$ genpassword fred www.twitter.com
Encryption key:
Site: twitter.com: Password: vk61-borA-wlIu-BYSK

]$ genpassword fred twitter.com
twitter.com: Password: vk61-borA-wlIu-BYSK

]$ genpassword fred twitter.com
twitter.com: Password: vk61-borA-wlIu-BYSK
```
