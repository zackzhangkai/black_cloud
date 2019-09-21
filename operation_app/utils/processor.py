import hashlib


def get_hashed_name(upload_file):
    """获得上传的文件的一个唯一名称"""
    # generate the md5 code for the uploaded file
    md5 = hashlib.md5()
    # to deal with larger file, use file chunks to update the md5 code
    for chunk in upload_file.chunks():
        md5.update(chunk)
    hashed_name = md5.hexdigest()
    return hashed_name
