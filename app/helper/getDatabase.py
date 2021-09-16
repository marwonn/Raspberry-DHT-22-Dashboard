import os
import paramiko
from helper.config import Config

def get_database():
    script_dir = os.path.dirname(__file__)
    rel_path = Config.PATH_2_DB_TARGET_LOCATION
    abs_file_path = os.path.join(script_dir, rel_path)

    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=Config.HOSTNAME, username=Config.USERNAME, password=Config.PASSWORD)

    ftp_client=ssh_client.open_sftp()
    ftp_client.get(Config.PATH_2_DB, abs_file_path)
    ftp_client.close()