from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes
from rest_framework import status
from .authentication import apikeycheck
from .master_tables_api import master_api
from .storeftp import store_ftp
from django.http.response import JsonResponse
from .apicalls import Api_calls


@api_view(['GET'])
@authentication_classes([apikeycheck])
def get_ph_business(request,table_name):
    try:
        query=f'Select * from {table_name}'

        data=master_api.get_for_master(query,table_name)
        if isinstance(data,dict) and data.get("Result")==1:
            return JsonResponse(data,safe=False,status=status.HTTP_200_OK)
        return JsonResponse(data,safe=False,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return JsonResponse({
            "Result":0,
            "Message":str(err),
            "Api-result":""
        },safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  
@api_view(['POST'])    
@authentication_classes([apikeycheck])
def post_group_product_detail(request):
    try:
        code=request.data.get('grpcode')
        ngname=request.data.get('ngrpname')
        mcode=request.data.get('mtrlcode')
        mdesc=request.data.get('mtrldesc')
        tags=request.data.get('tags')
        sgrp=request.data.get('secgroup')
        libry=request.data.get('libry')
        season=request.data.get('season')
        mtype=request.data.get('mtrltype')
        comp=request.data.get('composition')
        weight=request.data.get('weight')
        brand=request.data.get('brand')
        finish=request.data.get('finish')
        img=request.data.get('imagepath')

        image=store_ftp.ftp_img(img,code)
        if image.get("Message")=="Success":
            imagepath=image.get("Ftp-path")
        
        check_query=f"Select * from group_product_detail where grpcode={code}"
        check=Api_calls.get_api(check_query)
        # print(check)

        if isinstance(check,dict) and check["Api-result"]=="Row doesn't Exist!,Need to Insert!":
            insert_query=f""" Insert into group_product_detail(grpcode,ngrpname,mtrlcode,mtrldesc,tags,
                        secgroup,libry,season,mtrltype,composition,weight,brand,finish,imagepath,adduser,adddate,deleted)
                        values({code},'{ngname}',{mcode},'{mdesc}','{tags}','{sgrp}','{libry}',
                        '{season}','{mtype}','{comp}','{weight}','{brand}','{finish}','{imagepath}',7661288,current_date,'N') """
            insert=Api_calls.post_api(insert_query)
            # print(insert)
            if isinstance(insert,dict)and insert.get('Result')==1:
                return JsonResponse(insert,safe=False,status=status.HTTP_201_CREATED)
            return JsonResponse({"Result":0,"Message":"Not Possible to Insert!","Api-result":""},safe=False,status=status.HTTP_400_BAD_REQUEST)
        else:
            update_query=f"""Update  group_product_detail set ngrpname='{ngname}',mtrlcode={mcode},mtrldesc='{mdesc}',tags='{tags}',secgroup='{sgrp}',
                        libry='{libry}',season='{season}',mtrltype='{mtype}',composition='{comp}',weight='{weight}',brand='{brand}',finish='{finish}',
                        imagepath='{imagepath}',edtuser=1849188,edtdate=current_date where grpcode={code} """
            update=Api_calls.put_api(update_query)

            if isinstance(update,dict) and update.get('Message')=="Success":
                return JsonResponse(update,safe=False,status=status.HTTP_202_ACCEPTED)
            return JsonResponse({"Result":0,"Message":"Check the Parameter!","Api-result":""},safe=False,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as err:
        return JsonResponse({
            "Result":0,
            "Message":str(err),
            "Api-result":""
        }) 

                        




