

#Tavsiye olarak python 3 ve üst sürümünü kullanın.
#ÖNEMLİ:PYTHON EN SON SÜRÜM KULLANIYORSANIZ opencv ve mediapipe kütüphanelerinin bir alt sürümünü kullanmanızı öneririm.
#Önce opencv,mediapipe  ve pyfirmata kütüphaneleri komut satırından yazarak pip install ile yükleyin.
#aruino kartına standart firmatayı yükledikten sonra python sayfası açık kalsın diğer programların sayfasını kapatabilirsiniz.Fakat arduino karta bağlı USB kablosunu çekmeyin

#Eğer el hareketi ile görüntüdeki hareket ters yönlü ise flip kodu ekleyin



import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:3:o')#Arduinoda 3 numaralı bağlı led
led_2=board.get_pin('d:4:o')#Arduinoda 4 numaralı bağlı led 
led_3=board.get_pin('d:5:o')#Arduinoda 5 numaralı bağlı led 
led_4=board.get_pin('d:6:o')#Arduinoda 6 numaralı bağlı led 
led_5=board.get_pin('d:7:o')#Arduinoda 7 numaralı bağlı led 
led_6=board.get_pin('d:8:o')#Arduinoda 8 numaralı bağlı led 
led_7=board.get_pin('d:9:o')#Arduinoda 9 numaralı bağlı led 
led_8=board.get_pin('d:10:o')#Arduinoda 10 numaralı bağlı led 
led_9=board.get_pin('d:11:o')#Arduinoda 11 numaralı bağlı led 
led_10=board.get_pin('d:12:o')#Arduinoda 12 numaralı bağlı led 

def led(yanan_led):#yanacak led sayısına ait fonksiyon 
    if yanan_led==0:#Tüm parmak uçları kapalıyken hiç bir led yanmaz.
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==1:#1 led yanar.
        led_1.write(1)#3 numaralı pine bağlı led yanar.
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==6:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==7:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(0)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==8:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(1)
        led_9.write(0)
        led_10.write(0)
    elif yanan_led==9:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(1)
        led_9.write(1)
        led_10.write(0)
    elif yanan_led==10:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(1)
        led_9.write(1)
        led_10.write(1)


