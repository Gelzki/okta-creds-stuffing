# okta-creds-stuffing
python3 script that reads usernames from a file of usernames and passwords against the specified domain's okta page.

First: pip3 install requests
Usage: python3 okta-sprayer.py -u [usernames.txt] -p [passwords.txt] -d [domain.com] -w [wait_time_in_seconds]

The script will perform a brute force credential stuffing based on the given usernames and passwords file. Make sure that the usernames and passwords on the file matches each line as this script will iterate on both files at the same time.

If performing this test for a large number of users, you may want to consider breaking the user list into smaller groups and running each group from a different source host.

Note: if the script is having trouble parsing the password, surround it in single quotes (').
Note: This is forked from [okta-s](https://github.com/cedowens/okta-sprayer)https://github.com/cedowens/okta-sprayer
