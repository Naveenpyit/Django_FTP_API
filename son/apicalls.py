from .dbconnect import Api_methods
from .serializer import serialize

class Api_calls:
    @staticmethod
    def get_api(query):
        try:
            get_data=Api_methods.get_commmon(query)

            ser_data=serialize.serial_data(get_data)
            if "Error" in ser_data:
                return {
                    "Result":0,
                    "Message":"Fails",
                    "Api-result":""
                }
            return {
                "Result":1,
                "Message":"Success",
                "Api-result":ser_data
            }
        except Exception as err:
            return {
                "Result":0,
                "Message":str(err),
                "Api-result":""
            }
    @staticmethod
    def  post_api(query):
        try:
            post_data=Api_methods.post_common(query)

            if "Error" in post_data:
                return {
                    "Result":0,
                    "Message":"Fails",
                    "Api-result":""
                }
            succes_data= {
                "Result":1,
                "Message":"Success",
                "Api-result":post_data
            }
            return succes_data
        except Exception as err:
            return{
                "Result":0,
                "Message":str(err),
                "Api-result":""
            }
    @staticmethod
    def put_api(query):
        try:
            put_data=Api_methods.put_common(query)

            if put_data.get("Message")=="Row doesn't Exist, Need to Insert!":
                return {
                    "Result":0,
                    "Message":"Fails to put",
                    "Api-result":""
                }
            success_data={
                "Result":1,
                "Message":"Success",
                "Api-result":put_data
            }
            return success_data
        except Exception as err:
            return{
                "Result":0,
                "Message":str(err),
                "Api-result":""
            }

