# https://curl.trillworks.com/

from bs4 import BeautifulSoup
import requests
import time
import json
from pprint import pprint
import genanki
import random
import os

cookies = {
    'php7_ta_123_session_id': '79rvlfvpn7qlejcps71kshltn2',
    'ta123_user_shared': 'EurbIFJfUXxLRdiQUcL9RQlP^%^2Fj19c^%^2B^%^2B^%^2Fnq5AlwUMlosKi0GkkyKgQv58SgrzREGebnCWZ5yo452rCnib2dG^%^2FrUxOXNBxzendwipkESBInGWZuujI4XHvbMaAJRhlj^%^2BZrnZS6cCNrzDnnHEzK02iQz8^%^2FmoXOnezpZJGOX1C9aAusdAtLSWjm9UcfSDecABya6AGZGwOApo6vKP^%^2FiKremovednF4yEsnKgAMqtJrFlkrRXdAzdZg^%^2BH^%^2FTitlSpyef9c7^%^2B4T4rZTOFSsgvA928IUfNSuBQAAAAAA',
    'ta123_member': '3w9ABxnLcmc^%^3D',
    'HIM_on_off': '0',
    'HIM_method': '0',
    'HIM_ckspell': '1',
    'HIM_daucu': '1',
    'hocphatamgvmy-2': 'false',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.tienganh123.com/tieng-anh-lop-6-sach-moi-bai-1',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
}

# deckNameFinal = "Tiếng Anh lớp 11 - Sách mới"
# URLs = ["https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-1-tu-vung-1/17378-generation-gap-su-khac-biet-giua-cac-the-he.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-1-tu-vung-2/17387-generation-gap-su-khac-biet-giua-cac-the-he-2.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-2-tu-vung-1/17595-tu-vung-chu-de-cac-moi-quan-he.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-2-tu-vung-2/17601-tu-vung-chu-de-cac-moi-quan-he-2.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-3-tu-vung-1/17920-chu-de-song-doc-lap.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-3-tu-vung-2/17926-chu-de-song-doc-lap-tu-vung-bo-sung.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-4-tu-vung-1/18315-nguoi-khuyet-tat-people-with-disabilities.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-tu-vung-2/18321-nguoi-khuyet-tat-people-with-disabilities-2.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-5-tu-vung-1/18631-tu-vung-chu-de-ASEAN.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-5-tu-vung-2/18637-tu-vung-chu-de-ASEAN-tiep.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-6-tu-vung-1/19011-tu-vung-chu-de-nong-len-toan-cau.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-6-tu-vung-2/19017-tu-vung-chu-de-nong-len-toan-cau-tiep.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-7-tu-vung-1/19423-tu-vung-chu-de-hoc-len-cao-phan-1.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-7-tu-vung-2/19429-tu-vung-chu-de-hoc-len-cao-phan-2.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-8-tu-vung-1/19721-tu-vung-cac-di-san-the-gioi-cua-chung-ta-phan-1.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-8-tu-vung-2/19728-tu-vung-cac-di-san-the-gioi-cua-chung-ta-phan-2.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-9-tu-vung-1/20080-tu-vung-cac-thanh-pho-tuong-lai-phan-1.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-9-tu-vung-2/20086-tu-vung-cac-thanh-pho-tuong-lai-phan-2.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-10-tu-vung-1/20297-tu-vung-loi-song-khoe-manh-song-lau-phan-1.html", "https://www.tienganh123.com/tieng-anh-lop-11-sach-moi-bai-10-tu-vung-2/20303-tu-vung-loi-song-khoe-manh-song-lau-phan-2.html"]

# deckNameFinal = "Tiếng anh lớp 10 - Sách mới"
# URLs = ["https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-1-tu-vung-1/17035-ly-thuyet-tu-vung-chu-de-cong-viec-nha.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-1-tu-vung-2/17043-ly-thuyet-tu-vung-chu-de-cong-viec-nha-2.html", "https://www.tienganh123.com/lop-10-moi-bai-2-vocab/17195-ly-thuyet-tu-vung-chu-de-co-the-ban.html", "https://www.tienganh123.com/lop-10-moi-bai-2-vocab-2/17202-ly-thuyet-tu-vung-chu-de-co-the-ban-1.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-3-tu-vung-1/17888-tu-vung-chu-de-am-nhac-1.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-3-tu-vung-2/17895-tu-vung-chu-de-am-nhac-2.html", "https://www.tienganh123.com/tieng-anh-lop-10-moi-bai-4-tu-vung-1/18287-tu-vung-cong-dong-1.html", "https://www.tienganh123.com/tieng-anh-lop-10-moi-bai-4-tu-vung-2/18294-tu-vung-cong-dong-2.html", "https://www.tienganh123.com/tieng-anh-lop-10-moi-bai-5-tu-vung-1/18567-tu-vung-phat-minh-1.html", "https://www.tienganh123.com/tieng-anh-lop-10-moi-bai-5-tu-vung-2/18573-tu-vung-phat-minh-2.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-6-tu-vung-1/19040-tu-vung-binh-dang-gioi-gender-equality-1.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-6-tu-vung-2/19056-tu-vung-binh-dang-gioi-gender-equality-2.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-7-tu-vung-1/19294-tu-vung-da-dang-van-hoa-cultural-diversity-1.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-7-tu-vung-2/19300-tu-vung-da-dang-van-hoa-cultural-diversity-2.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-8-tu-vung-1/19586-tu-vung-phuong-thuc-hoc-moi.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-9-tu-vung-1/20425-tu-vung-ve-moi-truong.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-9-tu-vung-2/20431-tu-vung-ve-moi-truong-2.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-10-tu-vung-1/20514-tu-vung-du-lich-sinh-thai.html", "https://www.tienganh123.com/tieng-anh-lop-10-sach-moi-bai-10-tu-vung-2/20520-tu-vung-du-lich-sinh-thai-2.html"]


# _____________________ Tạo Model Field Cho deck Anki ___________

wd = os.path.join(os.getcwd(), 'assets')
with open(os.path.join(wd, 'front.html'), encoding='utf-8') as f:
    frontHtml = f.read()
    f.close()
with open(os.path.join(wd, 'back.html'), encoding='utf-8') as f:
    backHtml = f.read()
    f.close()
with open(os.path.join(wd, 'style.css'), encoding='utf-8') as f:
    cssLoaded = f.read()
    f.close()

my_model = genanki.Model(
    112252933,
    'TiengAnh123.com (vuongcris4)',
    model_type=genanki.Model.FRONT_BACK,
    fields=[
        {'name': 'Word'},
        {'name': 'IPA'},
        {'name': 'Type'},
        {'name': 'MeaningOfWord'},
        {'name': 'Example'},
        {'name': 'MeaningOfExample'},
        {'name': 'Image'},
        {'name': 'AudioOfWord'},
        {'name': 'AudioOfExample'},
        {'name': 'Video'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': frontHtml,
            'afmt': backHtml,
        },
    ],
    css=cssLoaded
)

my_deck = []


def createDeck(deckName):
    my_deck.append(
        genanki.Deck(
            deck_id=int(str(int.from_bytes(deckName.encode(), 'little'))[:18]),
            name=deckName,
            description="From Trần Duy Vương with love <3"
        )
    )


def addNote(fields):
    my_note = genanki.Note(
        model=my_model,
        fields=fields, guid=(random.randrange(1 << 30, 1 << 31)))
    my_deck[-1].add_note(my_note)


def saveAnkiPackage(packageName):
    genanki.Package(my_deck).write_to_file(packageName + '.apkg')

# ____________________________________ Process _____________________________________


for URL in URLs:
    page = requests.get(URL, headers=headers, cookies=cookies)

    print(page.status_code)
    time.sleep(0.3)
    soup = BeautifulSoup(page.content, 'lxml')

    # ___________ Title _________
    title = deckNameFinal
    unit = soup.find_all("span", itemprop='name')[
        2].text  # 'Unit 1: My new school'
    title += "::" + unit + "::"

    # _______ Lấy Json file của tienganh123.com
    lesson_main = soup.find("div", class_="lesson_main")

    urlJson = lesson_main['file']
    response = requests.get(urlJson)
    data = BeautifulSoup(response.content, 'lxml')  # Data thô của file Json
    main_lession_json = data.p.text
    """
    Xử lí chuỗi trước khi parse
    """
    main_lession_formated = main_lession_json

    # [ \t\n\r\f\v] re.sub("\s","",str)
    for ch in ['\t', '\n', '\r', '\f', '\v']:
        main_lession_formated = main_lession_formated.replace(ch, "")
    # Xóa ngoặc tròn và ; cuối câu
    main_lession_formated = main_lession_formated[1:-2]
    main_lession_formated = main_lession_formated.replace(
        ',},"words":', '},"words":')   # Xóa , chỗ "img" trong "video"

    main_lession_formated = main_lession_formated.replace(',"note":"','}') # Lỗi bất ngờ
    main_lession_formated = main_lession_formated.replace(',"note"','}') # Lỗi bất ngờ

    # ĐÃ CÓ DATABASE, BẮT ĐẦU XỬ LÍ
    main_lession = json.loads(main_lession_formated)

    sub_title = main_lession['title']   # School things and activities

    title += sub_title  # 'Tiếng Anh lớp 6::Unit 1: My new school::School things and activities'
    print(title)
    createDeck(deckName=title)

    url = urlJson.rsplit('/', 2)[0]+"/"   # Lấy base url để nối Image, Audio

    try:
        video = main_lession['video']['mp4']+"_VIP.mp4"
    except:
        video=""

    listWords = main_lession['words']
    for word in listWords:
        Word = word['word']
        ipa = word['phonetic']
        type = word['type']
        meaningOfWord = word['mean']
        example = word['ex'][0][0]
        meaningOfExample = word['ex'][0][1]
        image = url+word['img']
        audioOfWord = url+word['audio']
        audioOfExample = url+word['ex'][0][2]

        addNote([Word, ipa, type, meaningOfWord, example,
                meaningOfExample, image, audioOfWord, audioOfExample, video])

saveAnkiPackage(deckNameFinal)
