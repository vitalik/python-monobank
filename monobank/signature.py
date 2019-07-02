
import os
import ecdsa
import base64
import hashlib
import binascii


class SignKey(object):
    def __init__(self, priv_key):
        self.priv_key = priv_key
        self.sk = self._load()
    
    def key_id(self):
        "Returns monobank X-Key-Id"
        publicKey = self.sk.get_verifying_key()
        publicKeyB64 = base64.b64encode(publicKey.to_der())

        uncompressedPublicKey = bytearray([0x04]) + (bytearray(publicKey.to_string()))
        digests = hashlib.sha1()
        digests.update(uncompressedPublicKey)
        return binascii.hexlify(digests.digest())
    
    def sign(self, str_to_sign):
        "Signs string str_to_sign with private key, and hash sha256"
        sign = self.sk.sign(str_to_sign.encode(), hashfunc=hashlib.sha256)
        return base64.b64encode(sign)

    def _load(self):
        if 'PRIVATE KEY-----' in self.priv_key:
            raw = self.priv_key
        elif os.path.exists(self.priv_key):
            with open(self.priv_key) as f:
                raw = f.read()
        else:
            raise Exception('Cannot load private key')
        return ecdsa.SigningKey.from_pem(raw)
