import base64, os
from colorama import Fore

fg = Fore.GREEN
fr = Fore.RED
fy = Fore.YELLOW
fw = Fore.WHITE

os.system("clear")
print(f"""
                                                                          
{fr} ______  _     _    ___    _____  _     _  _____  _______  _____   _____  
(______)(_)   (_) _(___)_ (_____)(_)   (_)(_____)(__ _ __)(_____) (_____) 
(_)__   (__)_ (_)(_)   (_)(_)__(_)(_)_(_) (_)__(_)  (_)  (_)   (_)(_)__(_)
(____)  (_)(_)(_)(_)    _ (_____)   (_)   (_____)   (_)  (_)   (_)(_____) 
(_)____ (_)  (__)(_)___(_)( ) ( )   (_)   (_)       (_)  (_)___(_)( ) ( ) 
(______)(_)   (_)  (___)  (_)  (_)  (_)   (_)       (_)   (_____) (_)  (_)
[ EASY ENCRYPT WITH base64 WITH CUSTOM VARIABEL ]
Coded By LyxCodex
Project all ( t.me/tpnetofc ){fw}
                                                                          """)
def encode_file(file_path, output_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    encoded_content = base64.b64encode(file_content)
    
    with open(output_path, 'wb') as encoded_file:
        encoded_file.write(encoded_content)

python_script_path = input("root@enc~ Input# ")
encoded_script_path = input("root@enc~ Output# ")
encode_file(python_script_path, encoded_script_path)
with open(encoded_script_path, 'rb') as encoded_file:
    encoded_content = encoded_file.read()

# variable texts ( can custom )
variable_text = '[ENC-BOT]:[LyxCodex;https://github.com/lyxcodex];[By:TpnetCyber]'
variable_texts = "\n".join([variable_text for _ in range(1000)])
vartex = '[ENCRYPTOR-BOT]:[LyxCodex;https://github.com/lyxcodex]:[ThanksFor;ReyNode;MrBronx]'
vartex2 = "\n".join([vartex for _ in range(1000)])

decode_and_execute_code = f"""\
#!/usr/bin/env python3
import base64
# 1k Variabel
jkk = '''{variable_texts}'''
def decrypt_script(encoded_content):
    decoded_content = base64.b64decode(encoded_content)
    return decoded_content.decode()

# 2k Variabel
mmk = '''{vartex2}'''

lyxcodex = "{encoded_content.decode('utf-8')}"
decodex = decrypt_script(lyxcodex.encode('utf-8'))
exec(decodex) #dont delete it bitch
"""

with open(encoded_script_path, 'wb') as encoded_file:
    encoded_file.write(decode_and_execute_code.encode() + encoded_content)
