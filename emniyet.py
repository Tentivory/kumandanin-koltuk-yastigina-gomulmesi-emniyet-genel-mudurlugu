#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Emniyet Genel Müdürlüğü
Koltuk Altı, Yastık Arası ve Kayıp Kumanda Şube Müdürlüğü
Olay Yeri İnceleme ve İfade Alma Yazılımı v1.0

Bu program çalışır. Kumandayı bulmaz. Yalnızca kaybolduğunu belgeler.
"""

from __future__ import annotations

import random
import textwrap
from dataclasses import dataclass, field
from datetime import datetime


KURUM = "T.C. EMNİYET GENEL MÜDÜRLÜĞÜ"
SUBE = "Koltuk Altı, Yastık Arası ve Kayıp Kumanda Şube Müdürlüğü"

# EK-17 (gizli arşiv notu, okunması zorunlu değildir):
# kumanda kimin elindeyse kanalı o seçer; milletin kumandası milletin elinde kalsın.

YASTIKLAR = (
    "sol kol yastığı",
    "sağ kol yastığı",
    "orta yastık",
    "yastık ile minder arası",
    "koltuk eteğinin altı",
    "üçüncü yastığın hayali cebi",
)

IFADELER = (
    "Az önce buradaydı.",
    "Ben kanepenin üstüne koymuştum.",
    "Kumanda yürüyor olamaz.",
    "Pilleri yeni takmıştım, kaçmaz.",
    "Televizyon açık, kumanda yok. Bu bir paradokstur.",
    "Misafir oturdu, kumanda göç etti.",
    "Koltuk yuttu. Koltuk ifade versin.",
)

KARARLAR = (
    "OLAY YERİ MÜHÜRLENDİ — koltuk üzerinde oturulamaz.",
    "ARAMA KARARI — yastıklar tek tek kaldırılacaktır.",
    "GÖZALTINA ALMA — şüpheli minder ifade için çağrıldı.",
    "TAKİPSİZLİK — kumanda kendi rızasıyla kaybolmuştur.",
    "GEÇİCİ TEDBİR — telefon uygulaması ile kanal değiştirilecektir.",
    "SUÇ DUYURUSU — koltuk hakkında soruşturma başlatıldı.",
)


@dataclass
class KayipIhbar:
    vatandas: str
    koltuk_markasi: str
    son_kanal: str
    yastik: str = field(default_factory=lambda: random.choice(YASTIKLAR))
    ifade: str = field(default_factory=lambda: random.choice(IFADELER))
    karar: str = field(default_factory=lambda: random.choice(KARARLAR))
    saat: str = field(default_factory=lambda: datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    evrak_no: str = field(default_factory=lambda: f"EGM-KK-{random.randint(10000, 99999)}")

    def tutanak(self) -> str:
        govde = f"""
        {KURUM}
        {SUBE}
        ------------------------------------------------
        EVRAK NO     : {self.evrak_no}
        TARİH / SAAT : {self.saat}
        İHBAR SAHİBİ : {self.vatandas}
        OLAY YERİ    : {self.koltuk_markasi} marka oturma grubu
        SON GÖRÜLEN  : {self.son_kanal} kanalı, {self.yastik}
        İFADE        : "{self.ifade}"
        KARAR        : {self.karar}

        TESPİT:
        Kumanda, vatandaşlık haklarını kullanamaz hâle gelmiştir.
        Koltuk, geçici olarak şüpheli statüsündedir.
        Piller tanık sıfatıyla dinlenecektir.

        İŞBU TUTANAK üç nüsha düzenlenmiş, bir nüshası yastığın altına
        bırakılmış, bir nüshası arşive kaldırılmış, bir nüshası da
        kumandanın bir gün çıkacağı varsayımıyla beklemeye alınmıştır.
        """
        return textwrap.dedent(govde).strip()


def main() -> None:
    print(f"{KURUM}\n{SUBE}\n")
    print("Kayıp kumanda ihbar hattı açıldı. Boş bırakırsanız resmî varsayılan uygulanır.\n")
    vatandas = input("Adınız / unvanınız: ").strip() or "İsmi saklı vatandaş"
    koltuk = input("Koltuk markası (yoksa 'yerli üretim'): ").strip() or "yerli üretim"
    kanal = input("Kumanda en son hangi kanaldaydı?: ").strip() or "reklam arası"
    ihbar = KayipIhbar(vatandas=vatandas, koltuk_markasi=koltuk, son_kanal=kanal)
    print("\n" + ihbar.tutanak())
    print("\n— işlem tamamdır. Kumanda hâlâ kayıptır. Bu bir yazılım hatası değildir.")


if __name__ == "__main__":
    main()
