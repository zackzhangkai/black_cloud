# import calendar
import time
import hmac
import base64
# import urllib
import urllib.request
from hashlib import sha256
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

# config = Config('OAGQAAHPBFDOGLSJHPGC', 'jt7eMkKiheCTdZ7AxswF8ykJJ5MENXXGBF3kpp9s')
config = Config('NEHJOMFLKPTUSVMXFGRN', 'roz8ErW0q0iV0ku9s5vZnQEvSv3DuH0RiirCPg8r')
qingstor = QingStor(config)

def new_bucket():
    bucket = qingstor.Bucket("hello1234", 'pek3b')
    bucket.put()
    return bucket

def qs_put(object_name, body):
    bucket = new_bucket()
    resp = bucket.put_object(object_name, body=body)

def qs_get(object_name):
    bucket = new_bucket()
    print(object_name)
    qlist = bucket.list_objects()
    print(qlist)
    output = bucket.get_object(object_name)
    print(output.status_code)
    print('hi-im-output')
    print(output)
    return output.content

def qs_delete(object_name):
    bucket = new_bucket()
    bucket.delete_object(object_name)

def qs_list():
    bucket = new_bucket()
    output = bucket.list_objects()
    return output

def gen_view_url(object_name=''):
    bucket = new_bucket()
    expire_second = 300
    now = int(time.time())
    prepared = bucket.get_object_request(object_name).sign_query(
        now + expire_second
    )
    return prepared.url




