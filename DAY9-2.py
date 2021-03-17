import paramiko

def qytang_ssh(ip, usr, passwd, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usr, password=passwd, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

def ssh_get_route(ip, usr, passwd, port=22, cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usr, password=passwd, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    gw = x.split()[x.split().index('UG') - 2]
    return gw


if __name__ == '__main__':
    print(qytang_ssh('10.156.16.51', 'root', 'Bbc#2016'))
    print(qytang_ssh('10.156.16.51', 'root', 'Bbc#2016', cmd='pwd'))
    print("网关为：")
    print(ssh_get_route('10.156.16.51', 'root', 'Bbc#2016'))