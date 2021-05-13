from ncclient import manager
import requests
import json

# Access token change every 12 hrs
access_token = 'ZTEzNzg0NTctZjc0Yi00YTYzLWFhZWMtMmYzMjA5MWQwODg3NWExOWQ3NTAtMWVk_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f'

url = 'https://webexapis.com/v1/messages'
url_room = 'https://webexapis.com/v1/rooms'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
# params={'max': '100'}

def createMsg(msg):
    params_createMsg = {
    'roomId': room_id,
    "text": msg
    }
    requests.post(url, headers=headers, json=params_createMsg)

def getMsg():
    params = {
        'roomId': room_id
    }
    res = requests.get(url, headers=headers, params=params)
    current_msg = res.json()['items'][0]['text']
    return current_msg

while True:
    try:
        current_msg = getMsg()
        print("Current Message: %s"%current_msg)

        if current_msg == "61070023":
            m = manager.connect(
            host = "10.0.15.106",
            port = 830,
            username = "admin",
            password = "cisco",
            hostkey_verify = False
            )

            status = ""
            # Get config need to use filter
            netconf_filter = """
            <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
            <Loopback>
            </Loopback>
            </interface>
            </native>
            </filter>
            """
            netconf_reply = m.get(netconf_filter)
            print(netconf_reply)
            lst = str(netconf_reply).split("</name>")
            if "<shutdown/>" in lst[1]:
                status = "Loopback61070023 - Operational status is down"
                print("Shutdown!")
            else:
                status = "Loopback61070023 - Operational status is up"
                print("no shut")
            headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
            }
            createMsg(status)
        else:
            print("Not my ID")
        

    except KeyboardInterrupt:
        print("\n\nExit . . .")
        break
    except:
        print("Not a message format.")




