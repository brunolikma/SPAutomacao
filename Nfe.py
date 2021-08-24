import os


def instalar_Nfe():
    os.chdir(4 * '../')
    os.chdir('/Myfms Briefcase')
    os.popen("C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\regasm  fmsutil.dll")

def desinstalar_Nfe():
    os.chdir(4 * '../')
    os.chdir('/Myfms Briefcase')
    os.popen("C:\WINDOWS\Microsoft.NET\Framework\\v4.0.30319\\regasm /u fmsutil.dll /tlb:fmsutil.tlb")

