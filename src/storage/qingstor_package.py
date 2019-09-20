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


def gen_view_url(qy_access_key_id='NEHJOMFLKPTUSVMXFGRN',
                 secret_access_key='roz8ErW0q0iV0ku9s5vZnQEvSv3DuH0RiirCPg8r',
                 object_name=''):
    # qy_access_key_id = "NOVKGXOSNCUTIWNVIMMQ"
    # secret_access_key = "PYXp8uBp9K5l0H2t6dTy1yRQoKF0Dtpqeq2NVknc"

    verb = "GET"
    md5 = ""
    content_type = ""  # 请求头没有这个参数，保留空白行
    expire_second = 300  # 设置五分钟过期
    now = int(time.time())
    expire = str(now + expire_second)
    resource = "/hello1234/" + object_name  # testes.pek3b.qingstor.com 是 virtual-host 风格，所以 Canonicalized Resource 是 /bucketname 开头的
    print('im res %s' % resource)
    # host = "https://testes.pek3b.qingstor.com/1.jpg"
    host = "https://hello1234.pek3b.qingstor.com/" + object_name

    string_to_sign = verb + "\n" + md5 + "\n" + content_type + "\n" + expire + "\n" + resource
    # h = hmac.new(secret_access_key, digestmod=sha256)
    # h.update(string_to_sign)

    # python3
    h = hmac.new(secret_access_key.encode("utf-8"), digestmod=sha256)
    h.update(string_to_sign.encode("utf-8"))

    # signature = urllib.quote(base64.b64encode(h.digest()).strip())
    signature = urllib.request.quote(base64.b64encode(h.digest()).strip())

    uri = "?expires=" + expire + "&signature=" + signature + "&access_key_id=" + qy_access_key_id

    print(host + uri)
    return host + uri




