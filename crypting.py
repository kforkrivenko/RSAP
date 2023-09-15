import rsa


def get_keys():
    (pub, priv) = rsa.newkeys(512)
    return pub, priv


def crypt(message, e, n):
    crypted = rsa.encrypt(message.encode('utf8'), rsa.PublicKey(e=int(e), n=int(n)))
    return crypted


def decrypt(crypted, d, e, p, n, q):
    message = rsa.decrypt(crypted, rsa.PrivateKey(d=int(d), e=int(e), p=int(p), n=int(n), q=int(q)))
    return message.decode('utf8')
