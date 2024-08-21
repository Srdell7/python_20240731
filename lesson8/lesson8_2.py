from widget import tools

while True:
    try:
        name = str(input("請輸入姓名:"))
        height = float(input('請輸入身高(cm):'))
        weight = float(input('請輸入體重(kg):'))
        bmi = round(weight/((height*0.01)**2),ndigits=2)
    except ValueError:
        print("格式錯誤")
        continue
    grade = tools.get_status_message(bmi)
    print(f'親愛的{name}您好\n您的BMI值是:{bmi}\n體重:{grade}')
    leave = input("請問是否繼續輸入資料 ('q':離開,任意鍵:繼續)?")
    if leave == 'q':
        break
print("應用程式結束")