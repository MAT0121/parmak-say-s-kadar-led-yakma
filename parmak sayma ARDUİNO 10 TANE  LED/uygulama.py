import cv2
import mediapipe as mp
import led_ayar as knt

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#kamera
camera_video = cv2.VideoCapture(0)#harici kamera kullanıyorsanız parantezin içini 1 yapınız.
camera_video.set(3, 1280)#kamera penceresinde yatay uzunluk
camera_video.set(4, 720)#kamera penceresinde dikey uzunluk

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
 while camera_video.isOpened():
     success, image = camera_video.read()#görüntü algılama tanımlaması
     image=cv2.flip(image,2)#ekrandaki el ile kendi elinizin aynı yönlü olması için flip kodu eklendi.
     if not success:
         print("Görüntü algılanamadı, görüntü yansıtılmayacak.")
         continue

     image.flags.writeable = False
     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     results = hands.process(image)

     image.flags.writeable = True
     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

     fingerCount = 0
     if results.multi_hand_landmarks:#

         for hand_landmarks in results.multi_hand_landmarks:
             handIndex = results.multi_hand_landmarks.index(hand_landmarks)
             handLabel = results.multi_handedness[handIndex].classification[0].label

             handLandmarks = []

             for landmarks in hand_landmarks.landmark:
                 handLandmarks.append([landmarks.x, landmarks.y])


             if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                 fingerCount = fingerCount+1

             if handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                 fingerCount = fingerCount+1


             if handLandmarks[8][1] < handLandmarks[6][1]:
                 fingerCount = fingerCount+1

             if handLandmarks [12][1] < handLandmarks[10][1]:
                 fingerCount = fingerCount+1

             if handLandmarks [16][1] < handLandmarks[14][1]:
                 fingerCount = fingerCount+1

             if handLandmarks [20][1] < handLandmarks[18][1]:
                 fingerCount = fingerCount+1


             #led sayımı
             yanan_led = fingerCount
             knt.led(yanan_led)
             if yanan_led == 0:
                 cv2.putText(image,'YANAN LED SAYISI:', (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 1:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 2:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 3:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 4:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 5:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 6:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 7:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 8:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 9:
                 cv2.putText(image, "YANAN LED SAYISI:", (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                             2, (255, 0, 0), 5)
             elif yanan_led == 10:
                 cv2.putText(image, "MATEMATIK ve YAPAY ZEKA", (260, 100), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255), 8)



             #el işaretlerini gösterme
                 mp_drawing.draw_landmarks(image, hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),
                 mp_drawing_styles.get_default_hand_connections_style())


     #Parmak Sayısını Görüntüye Yansıtma
     cv2.putText(image, str(fingerCount), (630,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

     cv2.imshow('EL TAKiBi İLE PARMAK SAYMA UYGULAMASI', image)#Kameranın açılacığı pencere adı
     if cv2.waitKey(5) & 0xFF==27:
         break
















