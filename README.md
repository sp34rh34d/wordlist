# wordlist
custom password list creator  and custom username list creator (I use this with kerbrute)

this is for me, because i always lose this code and then i have to write it over and over 😪... btw, if anyone finds it useful feel free to use it too. (pentesting task)

# passwd.py
just edit the 'words' array with your target name, you can use l33t speak too.
```
python3 passwd
```
# username.py
I usually use this with kerbrute, the companies often create AD username with formats like 'username.lastname','u.lastname','usernamelastname','ulastname', so you can use a custom name list and lastname list to create a list of possible usernames used in AD, then with passwd.py you can create your custom password list to use with a bruteforce attack.

```
use:
python3 username.py

args:
-x, --format : select the following formats
                1 = [flastname]
                2 = [firstnamelastname]
                3 = [f.lastname]
                4 = [firstname.lastname]

-l, --lastname       : set a single lastname
-L, --lastname-file  : set a lastname wordlist
-f, --firstname      : set a single firstname
-F, --firstname-file : set a firstname wordlist
-c, --chars          : when you use formats like 1 and 3, maybe you only want to get username with letter 'a'.

examples:
python3 username.py -x 1 -f test1 -L lastname_wordlist.txt

python3 username.py -x 4 -F firstname_wordlist.txt -L lastname_wordlist.txt
```

