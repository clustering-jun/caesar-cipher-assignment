# 1. 사용자로부터 평문과 암호화 키를 입력받는다.
plaintext = input("평문을 입력하세요: ")

# 암호화 키는 알파벳을 몇 칸 이동할지 결정하는 정수이다.
key = int(input("암호화 키(이동할 칸 수)를 입력하세요: "))


# 2. 암호화 결과를 저장할 빈 문자열을 생성한다.
# 반복문에서 변환된 문자를 하나씩 추가할 예정이다.
ciphertext = ""


# 3. 평문을 한 글자씩 읽으면서 암호화를 수행한다.
for char in plaintext:

    # ord() 함수는 문자를 ASCII 코드 값으로 변환한다.
    ascii_code = ord(char)

    # 3-1. 대문자 알파벳 처리
    # ASCII 코드에서 대문자 A~Z는 65~90에 해당한다.
    if 65 <= ascii_code <= 90:

        # 대문자 A의 ASCII 코드인 65를 빼면
        # A~Z를 0~25 사이의 숫자로 표현할 수 있다.

        position = ascii_code - 65

        # 현재 알파벳 위치에 암호화 키를 더한다.
        # % 26은 26으로 나눈 나머지를 계산하는 연산이다.

        # 알파벳은 총 26개이므로 % 26을 사용하면
        # Z를 넘어가더라도 다시 A부터 시작할 수 있다.

        new_position = (position + key) % 26

        # 변환된 위치에 65를 더해 대문자 ASCII 코드로 복원한다.
        # chr() 함수는 숫자 코드를 문자로 변환한다.
        encrypted_char = chr(new_position + 65)

    # 3-2. 소문자 알파벳 처리
    # ASCII 코드에서 소문자 a~z는 97~122에 해당한다.
    elif 97 <= ascii_code <= 122:

        # 소문자 a의 ASCII 코드인 97을 빼서
        # 알파벳 위치를 0~25 사이의 숫자로 변환한다.
        position = ascii_code - 97

        # 암호화 키만큼 이동한다.
        # % 26을 사용하여 z 다음에는 a로 돌아가도록 한다.
        new_position = (position + key) % 26

        # 소문자 ASCII 코드로 변환한 뒤 문자로 복원한다.
        encrypted_char = chr(new_position + 97)

    # 3-3. 공백 및 기타 문자 처리
    else:

        # 공백은 알파벳이 아니므로 변경하지 않는다.
        # 숫자, 특수문자 등도 원래 문자 그대로 유지한다.
        encrypted_char = char

    # 3-4. 암호화 결과 저장
    # 변환된 문자를 기존 암호문 문자열의 끝에 추가한다.
    ciphertext += encrypted_char


# 4. 최종 암호화 결과를 화면에 출력한다.
print("\n===== 암호화 결과 =====")
print("평문:", plaintext)
print("암호화 키:", key)
print("암호문:", ciphertext)