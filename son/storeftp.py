from ftplib import FTP
from decouple import config
import base64,os

class store_ftp:
    @staticmethod
    def base_64(encode,code,folder='images'):
        try:
            decode=base64.b64decode(encode)
            if not os.path.exists(folder):
                os.makedirs(folder)

            file_path=os.path.join(f'{code}.jpg')
            with open(file_path,'wb')as file:
                file.write(decode)
            return {"Message":"Success","File_path":file_path}
        except  Exception as err:
            return {
                "Message":"Error",
                "Error":str(err)
            }
    @staticmethod
    def ftp_method(local_path):
        try:
            ftp_host=config('FTP_HOST')
            ftp_user=config('FTP_USER')
            ftp_pass=config('FTP_PASS')
            rem_dir='/TEST/Images_Db/'

            ftp=FTP(ftp_host)
            ftp.login(ftp_user,ftp_pass)
            ftp.cwd(rem_dir)

            with open (local_path,'rb')as file:
                ftp.storbinary(f'STOR {os.path.basename(local_path)}',file)

            ftp.quit()
            ftp_path=os.path.join(ftp_host,rem_dir,os.path.basename(local_path))
            return ftp_path
        except Exception as err:
            return {
                "Message":"Error",
                "Error":str(err)
            }
        finally:
            if os.path.exists(local_path):
                os.remove(local_path)
                print("Removed!")
