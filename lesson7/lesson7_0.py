while True:
    name=str(input('請輸入姓名:'))
    try:
        height=float(input('請輸入身高(cm):'))
        weight=float(input('請輸入體重(kg):'))
    except ValueError:
        print('格式錯誤')
    else:
        BMI=round(weight/((height*0.01)**2),ndigits=2)

        print(f'{name}您好')
        print(f'您的BMI值是:{BMI}')

        if BMI>=35:
            grade='重度肥胖'
        elif BMI>=30:
            grade='中度肥胖'
        elif BMI>=27:
            grade='輕度肥胖'
        elif BMI>=24:
            grade='過重'
        elif BMI>=18:
            grade='正常'
        else:
            grade='過輕'
        print(f'體重:{grade}')
    
    leave = input("是否要繼續計算?['q':離開,enter:繼續]:")
    if leave == 'q':
        break
print('應用程式結束!')