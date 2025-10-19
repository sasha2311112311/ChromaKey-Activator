import subprocess
import sys
import os
import ctypes

def check_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if sys.platform.startswith('win'):
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit()
        except:
            print("error неизвестная ошибка")
            sys.exit()


if not check_admin():
    print("⚠️  Для активации Windows требуются права администратора")
    response = input("Запустить программу от имени администратора? (y/n): ")
    if response.lower() in ['y', 'yes', 'д', 'да']:
        run_as_admin()
    else:
        print("я не могу активировать windows без прав администратора")
        input("Нажмите Enter для выхода...")
        sys.exit()

def windows_activate():
    try:
        subprocess.run(["powershell", "-Command", "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX"], check=True)
        subprocess.run(["powershell", "-Command", "slmgr /skms kms8.msguides.com"], check=True)
        subprocess.run(["powershell", "-Command", "slmgr /ato"], check=True)
        check_activation_result()
    except subprocess.CalledProcessError as e:
        print(f"error activeted {e}")

def windows_home():
    try:
        subprocess.run(["powershell", "-Command", "slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"], check=True)
        subprocess.run(["powershell", "-Command", "slmgr /skms kms8.msguides.com"], check=True)
        subprocess.run(["powershell", "-Command", "slmgr /ato"], check=True)
        check_activation_result()
    except subprocess.CalledProcessError as e:
        print(f"error activeted {e}")

def windows_vosem():
    try:
        subprocess.run(["powershell", "-Command", "slmgr /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9"], check=True)
        subprocess.run(["powershell", "-Command", "slmgr /skms kms8.msguides.com"], check=True)
        subprocess.run(["powershell", "-Command", "slmgr /ato"], check=True)
        check_activation_result()
    except subprocess.CalledProcessError as e:
        print(f"error acvited{e}")

def check_activation_result():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "slmgr /xpr"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )
        
        output = result.stdout.lower()
        print(f"DEBUG: {output}") 
        
        if any(phrase in output for phrase in ["активирована навсегда", "permanently activated", "активирована", "activated", "successfully"]):
            print("Windows активирована")
        elif "expiration" in output or "истекает" in output:
            print("Активированно но не на всегда")
        else:
            print("не активированно")
        
        print(result.stdout)
        
    except Exception as e:
        print(f'Ошибка проверки: {e}')

def main():
    while True:
        try:
            print("\n" + "="*50)
            print("Активатор Windows")
            print("="*50)
            num = int(input('Для проверки активации--0\nWindows 10/11 Pro--1\nWindows 10/11 Home--2\nWindows 8.1 Pro--3\nВыход--4\n\nВыберите вариант: '))
            
            if num == 1:
                windows_activate()
            elif num == 2:
                windows_home()
            elif num == 3:
                windows_vosem()
            elif num == 0:
                check_activation()
            elif num == 4:
                print("услышал")
                break
            else:
                print("введить коректное число")
        except ValueError:
            print("введите коректное число")
        
        input("\nнажми enter чтобы продолжить:)")

if __name__ == "__main__":
    main()