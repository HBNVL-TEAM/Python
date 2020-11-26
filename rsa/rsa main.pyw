import subprocess
import sys
import PySimpleGUI as sg
import time

sg.theme('SandyBeach')

def main():
  layout = [
        [sg.Image(filename='rsa.png',size=(200,60))],
        [sg.Text('P:          \t\t\t'),sg.Input(key='P', do_not_clear=False),sg.Text('Private key: \t\t'), sg.Input(key='D', do_not_clear=False)],
        [sg.Text('Q:          \t\t\t'),sg.Input(key='Q', do_not_clear=False),sg.Text('Public key: \t\t'), sg.Input(key='E', do_not_clear=False)],
        [sg.Text('Plaintext: \t\t'), sg.Input(key='M', do_not_clear=False),sg.Text('Plain Encrypt: \t\t'), sg.Input(key='C', do_not_clear=False)],
        [sg.Button('Encryption', bind_return_key=True),sg.Button('Decryption', bind_return_key=True)],
        [sg.Text('Loading data '),sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
        [sg.Button('About', bind_return_key=True,button_color=('black','yellow')), sg.Button('Clear',button_color=('black','red')),sg.Button('Exit',button_color=('black','green'))],
        [sg.Output(size=(150,25), background_color='black', text_color='yellow',key='1')],
        [sg.Text('\t\t\t\t\t\tCopyright © 2020 RSA Encryption Decryption - Author: Trương Hữu Phúc')]
        
        ]           
  

  window = sg.Window('RSA Encryption Decryption', layout)

  while True:
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'Exit'):
                        break
                elif event == 'Encryption':
                  if snt(int(values['P'])) and snt(int(values['Q'])):
                    e1="rsae.py " + values['M'] +" "+values['P']+" "+values['Q']
                    runCommand(cmd=e1,window=window)
                  else:
                    sg.popup('Thông Báo','P và Q phải là số nguyên tố')
                elif event == 'Decryption':
                  if snt(int(values['P'])) and snt(int(values['Q'])):
                    e2="rsad.py " + values['C'] +" "+values['P']+" "+values['Q']+" "+values['D']+" "+values['E']
                    runCommand(cmd=e2,window=window)
                  else:
                    sg.popup('Thông Báo','P và Q phải là số nguyên tố')
                elif event=='Clear':
                  window['1'].update('')
                elif event=='About':
                  sg.popup("Thông Tin",'Tác giả:Trương Hữu Phúc\nFB:fb.com/DdosFulzac')
  window.close()

def snt(n):
    dem=0
    for i in range(1,n+1):
        if(n%i==0):
            dem+=1
    if(dem==2):
        return True
    else:
        return False
def runCommand(cmd,window):
  window['progbar'].update_bar(0)
  for i in range(1000):
    window['progbar'].update_bar(i+1)
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in p.stdout:
    line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
    print(line)
    time.sleep(1)

main()
