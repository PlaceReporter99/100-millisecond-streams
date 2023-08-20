import os
import secrets
commands = \
f"""
mkdir random_data
cd random_data
timeout -s SIGKILL 0.1s cat /dev/urandom >> {secrets.token_hex(64)}.txt
cd ..
"""
os.system(commands)
