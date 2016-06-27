from email.header import decode_header

# http://stackoverflow.com/questions/7331351/python-email-header-decoding-utf-8
# http://stackoverflow.com/questions/5259601/how-convert-email-subject-from-utf-8-to-readable-string
print(decode_header("""=?UTF-8?B?IERyZWltb25hdHNmcmlzdCBmw7xyIFZlcnBmbGVndW5nc21laHJhdWZ3ZW5kdW4=?="""))
r = decode_header("=?utf-8?B?6JGh6JCE572R56uZ6YKA6K+35Ye9?=")
print(r)
print(r[0])
print(r[0][0].decode(r[0][1]))  # 葡萄网站邀请函
