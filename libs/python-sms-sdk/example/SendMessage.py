from ronglian_sms_sdk import SmsSDK

accId = '8a216da87b4e71e1017b5271e45800de'
accToken = 'e1d736b0be9b4cde9a89feb414b4d06a'
appId = '8a216da87b4e71e1017b5271e56e00e5'

def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '18081961426'
    datas = ("1234","10")
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

send_message()
