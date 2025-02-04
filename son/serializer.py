from datetime import date

class serialize:
    @staticmethod
    def serial_data(data):
        if isinstance(data,list):
            return  [serialize.serial_data(item)for item in data]
        elif isinstance(data,dict):
            return {key:serialize.serial_data(value)for key,value in data.items()}
        elif isinstance(data,date):
            return data.isoformat()
        return data