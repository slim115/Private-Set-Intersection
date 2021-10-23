import secrets, hashlib

# Extended Euclidean Algorithm
def xgcd(a,b):
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x  
        y, prevy = prevy - q*y, y
        a, b = b, r
    return a, prevx, prevy

# Encrypt m using key e in modulo p
def enc(e,m,p):
    return pow(m, e, p)

# Key Generation for Grab and Gojek 
def keygen(p):
    while True: 
        e = secrets.randbelow(p) 
        gcd, x, y = xgcd(e, p-1) 
        if gcd != 1: continue
        d = x % (p-1) 
        break
    return e,d

# Encrypt over a list
def enc_list(k, messages, p):
    result = set()
    for msg in messages:
        result.add(enc(k, msg, p))
    return result

# Hash of the given string of messages
def sha256(messages):
    result = set()
    for msg in messages:
        t= hashlib.sha256(msg.encode('utf-8')).hexdigest()
        result.add(int(t,base=16))
    return result

# Modulo p is public, Hexadecimal representation
p = 0xFFFFFFFFFFFFFFFFADF85458A2BB4A9AAFDC5620273D3CF1D8B9C583CE2D3695A9E13641146433FBCC939DCE249B3EF97D2FE363630C75D8F681B202AEC4617AD3DF1ED5D5FD65612433F51F5F066ED0856365553DED1AF3B557135E7F57C935984F0C70E0E68B77E2A689DAF3EFE8721DF158A136ADE73530ACCA4F483A797ABC0AB182B324FB61D108A94BB2C8E3FBB96ADAB760D7F4681D4F42A3DE394DF4AE56EDE76372BB190B07A7C8EE0A6D709E02FCE1CDF7E2ECC03404CD28342F619172FE9CE98583FF8E4F1232EEF28183C3FE3B1B4C6FAD733BB5FCBC2EC22005C58EF1837D1683B2C6F34A26C1B2EFFA886B423861285C97FFFFFFFFFFFFFFFF

# Start of code
grab_messages = {"91234567", "12345678","40000000", "52134567", "11112222", "98765432", "95678000"}
grab_messages_digest = sha256(grab_messages)

gojek_messages = {"95678000", "40000000", "68991111" "32123212", "52134567", "98765432"}
gojek_messages_digest = sha256(gojek_messages)

# Private to Grab
x = keygen(p)[0] 
grab_ciphertexts = enc_list(x, grab_messages_digest, p)

# Private to Gojek
y = keygen(p)[0] 
gojek_ciphertexts = enc_list(y, gojek_messages_digest, p)

# Encrypt with own private key
grab_double_enc = enc_list(x, gojek_ciphertexts, p)
gojek_double_enc = enc_list(y, grab_ciphertexts, p)

num = len(gojek_double_enc.intersection(grab_double_enc))
print("Number of intersections:", num)
doubledip = gojek_double_enc.intersection(grab_double_enc)

# Getting the plaintext which has intersection
def intersect(messages, centre):
    result = set()  
    for msg in messages:
        t = hashlib.sha256(msg.encode('utf-8')).hexdigest()
        u = int(t,base=16)
        v = enc(x, u, p)
        w = enc(y, v, p)
        if ( str(w) in str(centre)):
            result.add(msg)
    return result

double_dipper = intersect(grab_messages, doubledip)
print("\nPhone numbers:", double_dipper)
