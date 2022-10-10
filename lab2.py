import string
import random

str_a ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
str_b=""
for i in range(0,32):
    str_b+="0"
str_1="день"
str_2="вечер"
str_3="добрый"
print(len(str_b))
n=0
word_1=""

def wild(str_n,l):
    global word_1,n,str_b
    for i in range(0,l):
        index=str_a.index(str_n[i])
        #print(word[i])
        if(index!=len(str_b)-1):
            str_b=str_b[:index]+word_1[i]+str_b[index+1:]
        else:
            if(index!=0):
                str_b=str_b[:index]+word_1[i]
            else:
                str_b=word_1[i]+str_b[index+1:]
        print(str_n)
        print(str_b)
        print(word_1)
    n+=1
    word_1=str_n
    return

def decrypt(text):
    global word_1,n
    str_result=""
    word=""
    word_1=""
    n=0
    for shift in range(0,33):
        for c in text:
            if(c>='а' and c<='я'):
                if(c in str_b):
                    word+=str_a[str_b.index(c)]
                    word_1+=c
                else:
                    word+= str_a[((ord(c) - shift)-ord('а'))%(len(str_a))]
                    word_1+=c
            else:
                if(n<2 and word!=""):
                    l=len(word_1)
                    if(l==4):
                        wild(str_1,l)
                    if(l==5):
                        wild(str_2,l)
                    if(l==6):
                        wild(str_3,l)
                str_result+= word    
                str_result+= c
                word=""
                word_1=""
        print("shift = ",shift)
        print(str_result)
        str_result=""
    return 0

  
text = "блюншж явфвн, бйёпнёж яиэбёйёнляёф! оплизкриоь о еэбэфвж,злабэ кэ яштлбв квжнлккэь овпщ блидкэ яшбэяэпщ кв плищзл зиэоо(зиэооёсёзэуёь) ё кв мнлопл фёоил (нванвооёь). кэ яштлбв крдкл ялеянэцэпщ x,y, width, height ё зиэоо люкэнрдвкклал кэ зэнпёкзв лючвзпэ (ёиё зллнбёкэпшплфвз злкпрнля ъплал лючвзпэ, э-иь овайвкпэуёь)."
#decrypt(text) #29
text = "эзъйфг эюжх. зйьщжвбщлзйф дмйкзы ийюэезавев люёф ийзюдлзы из дмйкм ai, зжв ы щллщрю. цлз жюзъшбщлюехжфю люёф, ыф ёзаюлюыфъйщлх ечъмч кызч."
#decrypt(text) #25
text = "зрмцфмн ёпдзмрмфтёмы, зиса зтефян. ря х ёдрм еихизтёдпм ут очфхч фтхд отедпац. утпстъисстн уфтжфдрря рси сднцм си чздптха, пмьа цтпаот офдцомн упдс очфхд: "
#decrypt(text) #3
text = "зтефян зиса. ёт ёпткисмм сдьи отррифыихоти уфизпткисми ут утотумнстрч техпчкмёдсмв. д цдоки хумхто уфизтхцдёпгирящ сдрм чхпчж. ечзир фдзя здпасиньирч уптзтцётфстрч хтцфчзсмыихцёч!"
#decrypt(text)
text = "сьоюьт баюь. обсйат сьоюи этютшцыбай каьа внчщ ын ятюптю. каь сщм ныыи п кщтшаюцшб ьэцяныцт ыьътышщнабюи ынсь хнамыбай."
#decrypt(text)
text = "упьлнэюняхюр, пшфюьфх! шрщк уъняю щлюлчзк эрьоррнщл. к кнчкйэз ъафвфлчзщжш ыьрпэюлнфюрчршцьяыщъх ыьъфунъпэюнрщщъчъофэюфгрэцъх цъшылщфф. улщфшлршэк ыъэюлнцлшфыъ йоя ьъээфф"
#decrypt(text)
text = "тэпяйш туьк. рэ юуярйд samsung ai юяэрэтчб тън ьо 10сэ ыоабуя щъоаа р ысв."
#decrypt(text)
text = "ощлыёф мпвпы, очуэыуф мцкоучуыщмув! ъщоьхксуэп, хщнок ю шкь люопэ ьцпоюидпп ткшйэуп?"
#decrypt(text)
text = "ощлыёф опшж. мкг ъщвэщмёф йдух кхэумуыщмкцу."
#decrypt(text)
text = "чвфдоэ чшбп, жхуъушаоэ юяьшбё ! х гдвчвяъшбьш булшцв е хуаь чьуявцу- бугдухятс булш гдшчявъшбьш гв гвчюяскшбьс ьбёшдбшёу чят хулшэ вдцубьыуйьь!"
#decrypt(text)
