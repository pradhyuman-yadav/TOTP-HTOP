import pyotp as ttotp
import hashlib


root = "https://api.challenge.hennge.com/challenges/003"
content_type = "application/json"
userid = "pradhyuman999@gmail.com"
secret_suffix = "HENNGECHALLENGE003"
shared_secret = userid+secret_suffix
base32Str = "OBZGCZDIPF2W2YLOHE4TSQDHNVQWS3BOMNXW2SCFJZHEORKDJBAUYTCFJZDUKMBQGM======"


p = ttotp.TOTP(s=base32Str, digits=10, digest=hashlib.sha512, interval=30)

print("JS1 " +p.now())