# 복호화: 암호화와 같은 키를 사용하되, 반대 방향(왼쪽)으로 이동한다.
ciphertext = input("암호문을 입력하세요: ")
key = int(input("암호화 키를 입력하세요: "))

plaintext = ""
for char in ciphertext:
    code = ord(char)
    if 65 <= code <= 90:      # 대문자
        # 키만큼 빼서 원래 위치로 되돌린다. 음수가 되어도 % 26이 0~25로 맞춰준다.
        plaintext += chr((code - 65 - key) % 26 + 65)
    elif 97 <= code <= 122:   # 소문자
        plaintext += chr((code - 97 - key) % 26 + 97)
    else:                     # 공백 등은 그대로
        plaintext += char

print("평문:", plaintext)