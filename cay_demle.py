#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleme Simülatörü
Çay asla demlenmez. Bu bir özelliktir.
"""

import time
import random
import sys

def sonsuz_cay_demle():
    print("Çay demleme işlemi başlatılıyor...")
    print("Lütfen bekleyin. Evren genişliyor, çay demleniyor (demlenmiyor).")
    
    sikayetler = [
        "Bu çay ne zaman demlenecek yahu?",
        "Annem bile daha hızlı demlerdi.",
        "Kuantum çay bekliyorum, dalga çökmesi bekleniyor.",
        "Mahkeme kararı bekleniyor, çay için.",
        "Çaydanlık ısınıyor ama kalbi soğuk.",
        "Belki çay uzayda daha iyi demlenir.",
        "Bu kadar bekledikten sonra çay şekerli mi olacak acaba?",
        "GitHub'a commit atsam daha hızlı olur.",
        "Çay demlenene kadar evlenirim belki.",
        "Sonsuzluk bu kadar mı kısa sürerdi?"
    ]
    
    sayac = 0
    while True:  # Sonsuz döngü, çünkü çay asla bitmez
        time.sleep(2)  # Her 2 saniyede bir şikayet
        print(f"[{sayac}] {random.choice(sikayetler)}")
        sayac += 1
        if sayac % 10 == 0:
            print("--- Çay hâlâ demleniyor. Sabır taşınızı yutun. ---")
            # Gizli mesaj: bürokrasi çayı bile bekletir
            sys.stdout.flush()

if __name__ == "__main__":
    try:
        sonsuz_cay_demle()
    except KeyboardInterrupt:
        print("\nÇay demleme durduruldu. Ama çay hâlâ demlenmedi. Mahkeme kararı bekleniyor.")
        sys.exit(0)
