import paramiko

def qytang_ssh(ip, usr, passwd, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usr, password=passwd, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    print(qytang_ssh('10.156.16.51', 'root', 'Bbc#2016'))
    print(qytang_ssh('10.156.16.51', 'root', 'Bbc#2016', cmd='pwd'))