import logging
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

APP_PATH = os.path.dirname(os.path.abspath(__file__))

PARENT_PATH = Path(APP_PATH).parent
APP_PATH = Path(APP_PATH)

# Load environment variables from .env file
ENV_FILE = PARENT_PATH / ".env"

load_dotenv(ENV_FILE)

log_level = getattr(logging, os.environ["LOG_LEVEL"], logging.DEBUG)
log_to_console = os.environ["LOG_TO_CONSOLE"] == "true"

today = datetime.now().strftime("%Y-%m-%d")
log_filename = PARENT_PATH / f"logs/{today}.log"

handlers = [logging.FileHandler(log_filename)]

if log_to_console:
    handlers.append(logging.StreamHandler())

logging.basicConfig(
    level=log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=handlers,
)


def get_logger(name: str):
    return logging.getLogger(name)


danish_thai_dict = {
    "Sund og rask": "สุขภาพดี",
    "Kostråd": "คำแนะนำด้านโภชนาการ",
    "På forskud": "ล่วงหน้า",
    "Sidegevinst": "ผลประโยชน์เพิ่มเติม",
    "Vedvarende": "ถาวร",
    "Hyppigt": "บ่อยครั้ง",
    "Uoplagt": "ไม่อยากทำ",
    "Viljestyrke": "ความเข้มแข็งของจิตใจ",
    "Evig": "ชั่วนิรันดร์",
    "Værdier": "คุณค่า",
    "Sygemeldt": "ลาป่วย",
    "Jævnaldrene": "เพื่อนรุ่นเดียวกัน",
    "Alvorlig": "จริงจัง",
    "Ligestilling": "ความเสมอภาค",
    "Lønforskelle": "ความแตกต่างของค่าจ้าง",
    "Faggrupper": "กลุ่มวิชาชีพ",
    "Værdien": "ค่า",
    "Øremærket barsel": "การลาคลอดเฉพาะเจาะจง",
    "uanset": "ไม่ว่า",
    "Oprindelse": "แหล่งกำเนิด",
    "Forskelsbehandlet": "ถูกเลือกปฏิบัติ",
    "Saglig": "ตามข้อเท็จจริง",
    "Straffet": "ลงโทษ",
    "Hudfarve": "สีผิว",
    "Politisk anskuelse": "ความคิดเห็นทางการเมือง",
    "Seksuel orientering": "รสนิยมทางเพศ",
    "Udgangspunkt": "จุดเริ่มต้น",
    "Afvise": "ปฏิเสธ",
    "I særlige": "ในกรณีพิเศษ",
    "Undlade": "ละเว้น",
    "Forfremme": "เลื่อนตำแหน่ง",
    "Bestemt": "เฉพาะเจาะจง",
    "Optagelse": "การรับเข้า",
    "Nægte": "ปฏิเสธ",
    "I strid med": "ขัดแย้งกับ",
    "Forhindres": "ถูกขัดขวาง",
    "Forfatning": "รัฐธรรมนูญ",
    "Stille op": "ลงสมัคร",
    "Skilles": "แยกทาง",
    "Forældremyndighed": "การปกครองบุตร",
    "Lovgivning": "การออกกฎหมาย",
    "Barselsorlov": "การลาคลอด",
    "Ulighed": "ความไม่เสมอภาค",
    "Løngab": "ช่องว่างค่าจ้าง",
    "Tilbøjelige": "มีแนวโน้ม",
    "Lederstilling": "ตำแหน่งผู้นำ",
    "Miljømærke": "ตราสัญลักษณ์สิ่งแวดล้อม",
    "Advare": "เตือน",
    "Afskaffe": "ยกเลิก",
    "Udfordring": "ความท้าทาย",
    "Pligt": "หน้าที่",
    "Omkostning": "ค่าใช้จ่าย",
    "Gevinst": "ผลกำไร",
    "Overskud af": "กำไรของ",
    "Mangel på": "การขาดแคลน",
    "Tilstrømning af": "การหลั่งไหลของ",
    "Masser af": "จำนวนมากของ",
    "Tillid til": "ความไว้วางใจต่อ",
    "Vejledning": "คำแนะนำ",
    "Hvorvidt": "ว่า",
    "Erkender": "ยอมรับ",
    "Det skyldes": "เนื่องจาก",
    "Formentlig": "เป็นไปได้",
    "Regelmæssig": "ปกติ",
    "Beføjelse": "อำนาจ",
    "Adfærd": "พฤติกรรม",
    "Tilstand": "สถานะ",
    "Vedtaget": "ประกาศใช้",
    "Forskere": "นักวิจัย",
    "Hvoraf": "ที่ซึ่ง",
    "Bør": "ควร",
    "Burde": "ควรจะ",
    "Trivsel": "ความเป็นอยู่ที่ดี",
    "Gælder": "มีผลบังคับใช้",
    "Adskiller": "แยก",
    "Mistede": "สูญเสีย",
    "Hvile": "พักผ่อน",
    "Enkelte": "บางคน",
    "Kønsmæssigt": "ตามเพศ",
    "Overset": "มองข้าม",
    "Udsagn": "คำกล่าว",
    "Træffe valg": "ตัดสินใจ",
    "Understrege": "เน้นย้ำ",
    "Drøfte": "อภิปราย",
    "Række": "ช่วง",
    "Sænke": "ลดลง",
    "Altså": "ดังนั้น",
    "Netop": "ทันทีที่",
    "Forståeligt": "เข้าใจได้",
    "Uforståeligt": "ไม่เข้าใจ",
    "Enig": "เห็นด้วย",
    "Uenig": "ไม่เห็นด้วย",
    "Alligevel": "ยังคง",
    "Desuden": "นอกจากนี้",
    "Imidlertid": "อย่างไรก็ตาม",
    "Forventeligt": "คาดว่า",
    "Som nævnt": "ตามที่กล่าว",
    "Dog": "อย่างไรก็ตาม",
    "Fravælge": "เลือกออก",
    "Tilvælge": "เลือกเข้า",
    "Vanskeligt": "ยาก",
    "Almindeligt": "ปกติ",
    "Derimod": "ในทางตรงกันข้าม",
    "Til gengæld": "ตอบแทน",
    "Derudover": "นอกจากนี้",
    "I stedet": "แทนที่",
    "Forudsætning": "ข้อกำหนดเบื้องต้น",
    "Hensigt": "เจตนา",
    "Sikre": "ทำให้แน่ใจ",
    "Forklaring": "คำอธิบาย",
    "Betyder": "หมายความว่า",
    "Forudsætte": "สมมติฐาน",
    "Beliggenhed": "ทำเลที่ตั้ง",
    "Overraskende": "น่าประหลาดใจ",
    "Størrelser": "ขนาด",
    "Afvist": "ถูกปฏิเสธ",
    "Ligeledes": "เช่นเดียวกัน",
    "På trods af": "แม้ว่า",
    "Omvendt": "กลับกัน",
    "Sjældent": "ไม่บ่อย",
    "Derfor": "ดังนั้น",
    "Følger": "ผลที่ตามมา",
    "Overholder": "ปฏิบัติตาม",
    "Strammer": "ทำให้เข้มงวดขึ้น",
    "Ændrer": "เปลี่ยนแปลง",
    "Foreslår": "เสนอ",
    "Tværtimod": "ในทางตรงกันข้าม",
    "Øger": "เพิ่ม",
    "Svækker": "ทำให้อ่อนแอ",
    "Forstyrrer": "รบกวน",
    "Således": "ดังนั้น",
    "Derefter": "หลังจากนั้น",
    "Muligvis": "อาจจะ",
    "Formål": "เป้าหมาย",
    "Målsætning": "วัตถุประสงค์",
    "Nemlig": "เช่น",
    "Indtil": "จนกระทั่ง",
    "Bortset fra": "นอกจาก",
    "Tilbyde": "เสนอ",
    "Acceptere": "ยอมรับ",
    "Hermed": "ด้วยเหตุนี้",
    "Med andre ord": "พูดง่าย ๆ",
    "Eksempelvis": "เช่น",
    "Heldigvis": "โชคดี",
    "Grunde til": "เหตุผลสำหรับ",
    "Former for": "รูปแบบของ",
    "Holdning til": "ทัศนคติต่อ",
    "Årsag til": "เหตุผลสำหรับ",
    "Fællesskabet": "ชุมชน",
    "Forebygge": "ป้องกัน",
    "Vurdere": "ประเมิน",
    "Faglige": "ทางวิชาการ",
    "Spare på": "ประหยัด",
    "Foretrækker": "ชอบมากกว่า",
    "Overvejer": "พิจารณา",
    "Vanskeligt": "ยาก",
    "Frivilligt": "สมัครใจ",
    "Trygt": "ปลอดภัย",
    "Samtidig": "พร้อมกัน",
    "Nødvendighed": "ความจำเป็น",
    "Rettidig": "ตรงเวลา",
    "Rettighed": "สิทธิ",
    "Sandsynlighed": "ความน่าจะเป็น",
    "Tilfældighed": "ความบังเอิญ",
    "Allerførst": "ก่อนอื่น",
    "Vant til": "เคยชินกับ",
    "Opmærksom på": "ตระหนักถึง",
    "Skeptisk overfor": "สงสัยเกี่ยวกับ",
    "Behandlet for": "ได้รับการรักษา",
    "Eksponeret for": "สัมผัสกับ",
    "Beskyttet mod": "ได้รับการคุ้มครองจาก",
    "Blandt andet (bl.a.)": "รวมถึง",
    "Det vil sige (dvs.)": "นั่นคือ",
    "Krav": "ความต้องการ",
    "Forbud": "การห้าม",
    "Opfordring": "คำแนะนำ",
    "Undersøgelse": "การตรวจสอบ",
    "Modsat": "ตรงกันข้าม",
    "Løsning på": "การแก้ปัญหา",
}
