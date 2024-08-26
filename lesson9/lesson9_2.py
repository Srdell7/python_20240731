class BMI():  #attribute(實體)
    def __init__(self,name:str,height:float,weight:float):
        self.__name = name
        self.height = height
        self.weight = weight

    @property  #
    def name(self)->str:
        return self.__name

    def bmi(self)->float:
        return round((self.weight/(self.height*0.01)**2),ndigits=2)
    
    def grade(self)->str:
        self.grade = self.bmi()

        if self.grade<18.5:
            return "體重過輕"
        elif self.grade<24:
            return "正常範圍"
        elif self.grade<27:
            return "過重"
        elif self.grade<30:
            return "輕度肥胖"
        elif self.grade<35:
            return "中度肥胖"
        elif self.grade>=35:
            return "重度肥胖"

    def description(self)->str:
        return f'您的名字:{self.__name}\nBMI為:{self.bmi()}\n體重為:{self.grade()}'

while True:
    try:
        name = input("請輸入姓名: ")
        height = float(input('請輸入身高(cm): '))
        weight = float(input('請輸入體重(kg): '))
        yoursbmi = BMI(name=name,height=height,weight=weight)
        #yoursbmi.name = "xxxxx" 在實體外寫入會強制更改輸入值(去掉#來試用)
        print(yoursbmi.description())

    except ValueError:
        print("格式錯誤，請重新輸入數據")
        continue

    stuff = input("請問是否繼續輸入資料 ('q': 離開, 任意鍵: 繼續)? ")
    if stuff == 'q':
        break
print("應用程式結束")