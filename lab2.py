import string
import random

str_a ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
str_b=""
for i in range(0,32):
    str_b+="0"
str_1="день"
str_1_2="утро"
str_2="вечер"
str_3="добрый"
str_3_2 ="доброе"
str_4="здравствуйте"
print(len(str_b))


def wild(str_n,l,word):
    global str_b
    for i in range(0,l):
        index=str_a.index(str_n[i])
        if(index!=len(str_b)-1):
            str_b=str_b[:index]+word[i]+str_b[index+1:]
        else:
            if(index!=0):
                str_b=str_b[:index]+word[i]
            else:
                str_b=word[i]+str_b[index+1:]
    return 

def decrypt(text,max_n=2):
    
    
    str_result=""
    word="" 
    n=0
    
    for c in text:
        if(c in str_a):
            word+=c
        else:
            #print(word)
            if(n<max_n and word!=""):
                l=len(word)
                if(l==4):
                    wild(str_1,l,word)
                    n+=1
                if(l==5):
                    wild(str_2,l,word)
                    n+=1
                if(l==6):
                    wild(str_3,l,word)
                    n+=1
                if(l==12):
                    wild(str_4,l,word)
                    n+=1
            if(max_n==-1 and word!=""):
                if(n<2):
                    l=len(word)
                    if(l==4):
                        wild(str_1_2,l,word)
                        n+=1
                    if(l==6):
                        wild(str_3_2,l,word)
                        n+=1
            word=""
            
    print(str_a)        
    print(str_b)
    print(text)
    for shift in range (0,33):
        for c in text:
            if(c in str_a):
                if(c in str_b):
                    word+=str_a[str_b.index(c)]
                else:
                    word+= str_a[(str_a.index(c) + shift)%(len(str_a))]
            else:
                str_result+= word    
                str_result+= c
                word=""
                #word_1=""
        print("shift = ",shift)
        print(str_result)
        str_result=""
    return 0







text = "блюншж явфвн, бйёпнёж яиэбёйёнляёф! оплизкриоь о еэбэфвж,злабэ кэ яштлбв квжнлккэь овпщ блидкэ яшбэяэпщ кв плищзл зиэоо(зиэооёсёзэуёь) ё кв мнлопл фёоил (нванвооёь). кэ яштлбв крдкл ялеянэцэпщ x,y, width, height ё зиэоо люкэнрдвкклал кэ зэнпёкзв лючвзпэ (ёиё зллнбёкэпшплфвз злкпрнля ъплал лючвзпэ, э-иь овайвкпэуёь)."
#decrypt(text) #3
text = "эзъйфг эюжх. зйьщжвбщлзйф дмйкзы ийюэезавев люёф ийзюдлзы из дмйкм ai, зжв ы щллщрю. цлз жюзъшбщлюехжфю люёф, ыф ёзаюлюыфъйщлх ечъмч кызч."
#decrypt(text) #7
text = "зрмцфмн ёпдзмрмфтёмы, зиса зтефян. ря х ёдрм еихизтёдпм ут очфхч фтхд отедпац. утпстъисстн уфтжфдрря рси сднцм си чздптха, пмьа цтпаот офдцомн упдс очфхд: "
#decrypt(text) #29
text = "зтефян зиса. ёт ёпткисмм сдьи отррифыихоти уфизпткисми ут утотумнстрч техпчкмёдсмв. д цдоки хумхто уфизтхцдёпгирящ сдрм чхпчж. ечзир фдзя здпасиньирч уптзтцётфстрч хтцфчзсмыихцёч!"
#decrypt(text) #29
text = "сьоюьт баюь. обсйат сьоюи этютшцыбай каьа внчщ ын ятюптю. каь сщм ныыи п кщтшаюцшб ьэцяныцт ыьътышщнабюи ынсь хнамыбай."
#decrypt(text,-1) #19
text = "упьлнэюняхюр, пшфюьфх! шрщк уъняю щлюлчзк эрьоррнщл. к кнчкйэз ъафвфлчзщжш ыьрпэюлнфюрчршцьяыщъх ыьъфунъпэюнрщщъчъофэюфгрэцъх цъшылщфф. улщфшлршэк ыъэюлнцлшфыъ йоя ьъээфф"
#decrypt(text,1) #21
text = "тэпяйш туьк. рэ юуярйд samsung ai юяэрэтчб тън ьо 10сэ ыоабуя щъоаа р ысв."
#decrypt(text) #18
text = "ощлыёф мпвпы, очуэыуф мцкоучуыщмув! ъщоьхксуэп, хщнок ю шкь люопэ ьцпоюидпп ткшйэуп?"
#decrypt(text) #22
text = "ощлыёф опшж. мкг ъщвэщмёф йдух кхэумуыщмкцу."
#decrypt(text) #22
text = "чвфдоэ чшбп, жхуъушаоэ юяьшбё ! х гдвчвяъшбьш булшцв е хуаь чьуявцу- бугдухятс булш гдшчявъшбьш гв гвчюяскшбьс ьбёшдбшёу чят хулшэ вдцубьыуйьь!"
decrypt(text) #13
