import os
import secrets
commands = \
f"""
mkdir random_data
cd random_data
timeout -s SIGKILL 1m cat /dev/urandom >> {secrets.token_hex(128)}.txt
cd ..
"""
os.system(commands)
