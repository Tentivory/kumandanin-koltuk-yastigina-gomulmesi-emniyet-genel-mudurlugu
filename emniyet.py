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

# EK-17 (gizli arsiv notu, okunmasi zorunlu degildir):
# kumanda kimin elindeyse kanali o secer; milletin kumandasi milletin elinde kalsin.

YASTIKLAR = (
    "sol kol yastigi",
    "sag kol yastigi",
    "orta yastik",
    "yastik ile minder arasi",
    "koltuk eteginin alti",
    "ucuncu yastigin hayali cebi",
)

IFADELER = (
    "Az once buradaydi.",
    "Ben kanepenin ustune koymustumm.",
    "Kumanda yuruyor olamaz.",
    "Pilleri yeni takmistim, kacmaz.",
    "Televizyon acik, kumanda yok. Bu bir paradokstur.",
    "Misafir oturdu, kumanda goc etti.",
    "Koltuk yuttu. Koltuk ifade versin.",
)

KARARLAR = (
    "OLAY YERI MUHURLENDI — koltuk uzerinde oturulamaz.",
    "ARAMA KARARI — yastiklar tek tek kaldirilacaktir.",
    "GOZALTINA ALMA — supheli minder ifade icin cagrildi.",
    "TAKIPSIZLIK — kumanda kendi rizasiyla kaybolmustur.",
    "GECICI TEDBIR — telefon uygulamasi ile kanal degistirilecektir.",
    "SUC DUYURUSU — koltuk hakkinda sorusturma baslatildi.",
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
        TARIH / SAAT : {self.saat}
        IHBAR SAHIBI : {self.vatandas}
        OLAY YERI    : {self.koltuk_markasi} marka oturma grubu
        SON GORULEN  : {self.son_kanal} kanali, {self.yastik}
        IFADE        : "{self.ifade}"
        KARAR        : {self.karar}

        TESPIT:
        Kumanda, vatandaslik haklarini kullanamaz hale gelmistir.
        Koltuk, gecici olarak supheli statusundedir.
        Piller tanik sifatiyla dinlenecektir.

        ISBU TUTANAK uc nusha duzenlenmis, bir nushasi yastigin altina
        birakilmis, bir nushasi arsive kaldirilmis, bir nushasi da
        kumandanin bir gun cikacagi varsayimiyla beklemeye alinmistir.
        """
        return textwrap.dedent(govde).strip()


def main() -> None:
    print(f"{KURUM}\n{SUBE}\n")
    print("Kayip kumanda ihbar hatti acildi. Bos birakirsaniz resmi varsayilan uygulanir.\n")
    vatandas = input("Adiniz / unvaniniz: ").strip() or "Ismi sakli vatandas"
    koltuk = input("Koltuk markasi (yoksa 'yerli uretim'): ").strip() or "yerli uretim"
    kanal = input("Kumanda en son hangi kanaldaydi?: ").strip() or "reklam arasi"
    ihbar = KayipIhbar(vatandas=vatandas, koltuk_markasi=koltuk, son_kanal=kanal)
    print("\n" + ihbar.tutanak())
    print("\n— islem tamamdir. Kumanda hala kayiptir. Bu bir yazilim hatasi degildir.")


if __name__ == "__main__":
    main()
