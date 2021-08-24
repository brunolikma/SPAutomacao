import os
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def instalar_fms_service():
    os.chdir(4 * '../')
    os.chdir('/Myfms Briefcase')
    os.popen('fms_service /install')


def desinstalar_fms_service():
    os.chdir(4 * '../')
    os.chdir('/Myfms Briefcase')
    os.popen('fms_service /uninstall')


def iniciar_fms_service():
    os.system('net start fms_mgr')


def parar_fms_service():
    os.system('net stop fms_mgr')


def codigo_install():
    if is_admin():
        instalar_fms_service()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def codigo_uninstall():
    if is_admin():
        desinstalar_fms_service()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def codigo_iniciar():
    if is_admin():
        iniciar_fms_service()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def codigo_parar():
    if is_admin():
        parar_fms_service()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def codigo_iniciar():
    if is_admin():
        iniciar_fms_service()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def codigo_parar():
    if is_admin():
        parar_fms_service()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def bt_instalar():
    codigo_install()


def bt_desinstalar():
    codigo_uninstall()


def bt_iniciar():
    codigo_iniciar()


def bt_parar():
    codigo_parar()
