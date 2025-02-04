from .serializer import serialize
from .dbconnect import Api_methods
from .models import Master_Tables
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
import os,json

class master_api:
    @staticmethod
    def get_for_master(query,table_name):
        try:
            mas_obj,created=Master_Tables.objects.get_or_create(Table_name=table_name)

            current_time=timezone.now()
            local_time=timezone.localtime(current_time)

            duration=int(mas_obj.Duration)
            if not duration:
                duration=2
            
            file_path=os.path.join(settings.BASE_DIR,'Datas_files',f'{table_name}.txt')
            
            if created or (local_time - mas_obj.Last_update > timedelta(hours=duration)):
                data=Api_methods.get_commmon(query)

                if data:
                    ser_data=serialize.serial_data(data)

                    mas_obj.Last_update=local_time
                    mas_obj.New_update="Yes"
                    mas_obj.save()

                    if not os.path.exists(os.path.dirname(file_path)):
                        os.makedirs(os.path.dirname(file_path))
                    
                    with open(file_path, 'w')as file:
                        json.dump(ser_data,file,indent=4)
                    
                    success_data={
                        "Result":1,
                        "Message":"Success",
                        "Api-result":ser_data
                    }
                    return success_data
            elif os.path.exists(file_path) and os.path.getsize(file_path) >0 :
                mas_obj.New_update="No"
                mas_obj.save()

                with open(file_path, 'r')as file:
                    data=json.load(file)

                success_data={
                    "Result":1,
                    "Message":"Success",
                    "Api-result":data
                }
                return success_data
            
            else:
                return {
                    "Result":0,
                    "Message":"Fails",
                    "Api-result":""
                }
            
        except Exception as err:
            return {
                "Result":0,
                "Message":str(err),
                "Api-result":""
            }


                