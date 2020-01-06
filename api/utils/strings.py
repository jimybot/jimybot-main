from base64 import b64decode, b64encode


def encode_url(url):
    return b64encode(url.encode('UTF-8')).decode('UTF-8')

def decode_url(encoded_url):
    return b64decode(encoded_url)
