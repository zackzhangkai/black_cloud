from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

# config = Config('OAGQAAHPBFDOGLSJHPGC', 'jt7eMkKiheCTdZ7AxswF8ykJJ5MENXXGBF3kpp9s')
config = Config('NEHJOMFLKPTUSVMXFGRN', 'roz8ErW0q0iV0ku9s5vZnQEvSv3DuH0RiirCPg8r')
qingstor = QingStor(config)

def new_bucket():
    bucket = qingstor.Bucket("hello1234", 'pek3b')
    bucket.put()
    return bucket

def put(object_name, body):
    bucket = new_bucket()
    resp = bucket.put_object(object_name, body=body)

def get(object_name):
    bucket = new_bucket()
    output = bucket.get_object(object_name)
    return output

def delete(object_name):
    bucket = new_bucket()
    bucket.delete_object(object_name)

def list():
    bucket = new_bucket()
    output = bucket.list_objects()
    return output



