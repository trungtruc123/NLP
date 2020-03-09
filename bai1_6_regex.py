import re

# s = re.split('\s+','Tran Trung Truc')
# print(s)
doc = "For more details please mail us at: xyz@abc.com, pqr@mno.com"
s= re.findall(r'[\w\.-]+@[\w\.-]+',doc)
print(s)
# replace dia chi email thanh tieuthu.anninh@gmail.com
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)',r'tieuhtu.anninh@gmail.com', doc)
print(new_email_address)
