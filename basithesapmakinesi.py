def hesap_makinesi():
    İlkSayi = int(input("İlk sayiyi giriniz: "))
    İkinciSayi = int(input("İkinci sayiyi giriniz: "))

    islem = input("Yapmak istediğiniz işlemi seçiniz (toplama: + , cikarma: - ,carpma: * , bölme: /): ")



    if islem == "+":
        print("Sonuç: " + str(İlkSayi + İkinciSayi))
    elif islem == "-":
        print("Sonuç: " + str(İlkSayi - İkinciSayi))
    elif islem == "*":
        print("Sonuç: " + str(İlkSayi * İkinciSayi))
    elif islem == "/":


        if İkinciSayi == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
     
     
            print("Sonuç: " + str(İlkSayi / İkinciSayi))
    else:
        print("Geçersiz işlem türü!")

hesap_makinesi()

