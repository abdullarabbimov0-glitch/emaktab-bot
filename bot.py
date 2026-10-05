import httpx
import asyncio
from datetime import datetime

TOKEN = "BOT_TOKEN_BU_YERGA_RENDERDA_BERILADI"
GROUP_ID = 635586802

HAFTA_KUNLARI = {
    0: "dushanba",
    1: "seshanba",
    2: "chorshanba",
    3: "payshanba",
    4: "juma",
    5: "shanba",
    6: "yakshanba"
}

async def yuborish():
    while True:
        hozir = datetime.now()

        kun = HAFTA_KUNLARI[hozir.weekday()]
        sana = hozir.strftime("%d.%m.%Y")
        vaqt = hozir.strftime("%H:%M")

        xabar = (
            f"🔔 Eslatma\n\n"
            f"📅 Bugun: {kun}, {sana}\n"
            f"🕐 Vaqt: {vaqt}\n\n"
            f"📚 eMaktabga kirishni unutmang!"
        )

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        try:
            r = httpx.post(
                url,
                data={"chat_id": GROUP_ID, "text": xabar},
                timeout=30
            )
            print(r.status_code)
            print(r.text)

        except Exception as e:
            print("Xato:", e)

        await asyncio.sleep(3600)

asyncio.run(yuborish())
