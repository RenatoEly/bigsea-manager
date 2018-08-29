import paramiko

def _get_ssh_connection(ip, key_path):
    print
    "Getting ssh key"
    keypair = paramiko.RSAKey.from_private_key_file(key_path)
    print
    "Getting paramiko client"
    conn = paramiko.SSHClient()
    print
    "Setting policy"
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print
    "Connecting to the host"
    conn.connect(hostname=ip, username="ubuntu", pkey=keypair)
    return conn


conn = _get_ssh_connection("10.5.0.46","/home/ubuntu/Asperathos/.ssh/asperathos_key")
conn.exec_command("mkdir zueira")