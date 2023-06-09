from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from .models import enrolled_device
import qrcode
import json
import time
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    print ("hello")
    data_all=enrolled_device.objects.all()
    return render(request,'device_enrollment.html',{'dt':data_all})

def add_device(request):
        try:
            if request.method=="POST":
                    enterprise_name='enterprises/LC03u79ru8'
                    creds = Credentials.from_service_account_file('C:/Users/centiago/Desktop/project_django/emilocker/api_playgroud.json')
                    androidmanagement = build('androidmanagement', 'v1', credentials=creds)

                    policy_name = enterprise_name + '/policies/mayur_policy1'+str(request.POST.get('device_id'))
                    androidmanagement.enterprises().policies().patch(
                                                                        name=policy_name,
                                                                        body={
                                                                    "applications": [
                                                                        {
                                                                        "packageName": "com.google.samples.apps.iosched",
                                                                        "installType": "FORCE_INSTALLED"
                                                                        }
                                                                    ],
                                                                    "advancedSecurityOverrides": {
                                                                        "developerSettings": "DEVELOPER_SETTINGS_ALLOWED"
                                                                    },
                                                                    "safeBootDisabled": True,
                                                                    "screenCaptureDisabled": True,
                                                                    "factoryResetDisabled": True,
                                                                    "statusBarDisabled": True,
                                                                    "cameraDisabled": True,
                                                                    # "disableTouchscreen": False
                                                                    }
                                                                    ).execute()

                    enrollment_token = androidmanagement.enterprises().enrollmentTokens().create(
                        parent=enterprise_name,
                        body={"policyName": policy_name}
                    ).execute()

                    inst=qrcode.make(enrollment_token['qrCode'])
                    qrcode_destination='static/database_files/qrcodes/QRcode-'+time.strftime("%y_%m_%d_%H_%M_%S")+'mayur.png'
                    inst.save(qrcode_destination)
                    
                    
                    
                    if request.method == 'POST':   
                        data_inst=enrolled_device()
                        data_inst.customer_name=request.POST.get('name')
                        data_inst.device_brand=request.POST.get('device_brand')
                        data_inst.device_id=request.POST.get('device_id')
                        data_inst.policy_name=policy_name
                        data_inst.qrcode=qrcode_destination
                        data_inst.save()
            
            return redirect('home')
        except :
              return redirect('home')
              
        
                    
