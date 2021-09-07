# https://curl.trillworks.com/

from bs4 import BeautifulSoup
import requests
import time
import json
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

deckNameFinal = "Tiếng Anh lớp 9 - Sách mới"
URLs = ["https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-1-tu-vung-1/18851-tu-vung-ve-cac-san-pham-thu-cong-lang-nghe-truyen-thong.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-1-tu-vung-2/18862-tu-vung-ve-cac-san-pham-thu-cong-lang-nghe-truyen-thong-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-2-tu-vung-1/18917-tu-vung-ve-cac-net-dac-trung-cua-cuoc-song-thanh-pho.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-2-tu-vung-2/18925-tu-vung-ve-doi-song-o-thanh-pho-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-3-tu-vung-1/18935-tu-vung-ve-nhung-cang-thang-va-ap-luc-trong-giai-doan-vi-thanh-nien.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-3-tu-vung-2/18938-tu-vung-ve-nhung-cang-thang-va-ap-luc-trong-giai-doan-vi-thanh-nien-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-4-tu-vung-1/19062-tu-vung-ve-cuoc-song-thoi-xua.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-4-tu-vung-2/19066-tu-vung-ve-cuoc-song-thoi-xua-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-5-tu-vung-1/19175-tu-vung-ve-cac-ky-quan-o-viet-nam.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-5-tu-vung-2/19179-tu-vung-ve-cac-ky-quan-o-viet-nam-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-6-tu-vung-1/19226-tu-vung-ve-viet-nam-thoi-xua-va-nay.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-6-tu-vung-2/19251-tu-vung-ve-viet-nam-thoi-xua-va-nay-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-7-tu-vung-1/19313-tu-vung-ve-cac-mon-an-va-cac-cach-che-bien-thuc-an.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-7-tu-vung-2/19319-tu-vung-ve-cac-mon-an-va-cac-cach-che-bien-thuc-an-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-8-tu-vung-1/19372-tu-vung-ve-du-lich.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-8-tu-vung-2/19400-tu-vung-ve-du-lich-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-9-tu-vung-1/19419-tu-vung-ve-ngon-ngu-cach-hoc-va-su-dung-ngon-ngu.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-9-tu-vung-2/19451-tu-vung-ve-ngon-ngu-cach-hoc-va-su-dung-ngon-ngu-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-10-tu-vung-1/19502-tu-vung-ve-thien-van-hoc-va-du-hanh-vu-tru.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-10-tu-vung-2/19506-tu-vung-ve-thien-van-hoc-va-du-hanh-vu-tru-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-11-tu-vung-1/19543-tu-vung-ve-nhung-thay-doi-vai-tro-trong-xa-hoi.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-11-tu-vung-2/19612-tu-vung-ve-nhung-thay-doi-vai-tro-trong-xa-hoi-tiep.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-12-tu-vung-1/19619-tu-vung-ve-lua-chon-nghe-nghiep-cho-tuong-lai.html","https://www.tienganh123.com/tieng-anh-lop-9-sach-moi-bai-12-tu-vung-2/19624-tu-vung-ve-lua-chon-nghe-nghiep-cho-tuong-lai-tiep.html"]

# deckNameFinal = "Tiếng Anh lớp 8 - Sách mới"
# URLs = ["https://www.tienganh123.com/tieng-anh-lop8-sach-moi-bai-1-tu-vung-1/18579-tu-vung-ve-hoat-dong-trong-thoi-gian-ranh-roi.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-1-tu-vung-2/18589-tu-vung-ve-hoat-dong-trong-thoi-gian-ranh-roi-tiep-theo.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-2-tu-vung-1/18773-tu-vung-ve-phong-canh-hoat-dong-o-cac-vung-que.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-2-tu-vung-2/18778-tu-vung-ve-phong-canh-hoat-dong-o-cac-vung-que-2.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-3-tu-vung-1/19233-tu-vung-ve-cac-dan-toc-o-viet-nam.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-3-tu-vung-2/19247-tu-vung-ve-cac-dan-toc-o-viet-nam-tiep-theo.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-4-tu-vung-/19758-tu-vung-ve-cac-phong-tuc-va-truyen-thong.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-5-tu-vung-1/19956-tu-vung-ve-cac-le-hoi-o-viet-nam.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-5-tu-vung-2/19959-tu-vung-ve-cac-le-hoi-o-viet-nam-2.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-6-tu-vung/20048-tu-vung-xuat-hien-trong-cac-truyen-co-tich-dan-gian-ngu-ngon-truyen-thuyet.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-7-tu-vung-1/20875-tu-vung-ve-cac-loai-o-nhiem-moi-truong.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-8-tu-vung/21011-tu-vung-ve-cac-nuoc-noi-tieng-anh.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-9-tu-vung-1-cac-loai-tham-hoa-thien-nhien/21249-tu-vung-ve-cac-loai-tham-hoa-thien-nhien-dong-tu-cum-dong-tu-mieu-ta.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-9-tu-vung-2-tu-mieu-ta-va-cau-cam-than-ve-tham-hoa-thien-nhien/21417-tu-vung-ve-tham-hoa-thien-nhien-2.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-10-tu-vung-hinh-thuc-va-cong-nghe-giao-tiep/22466-tu-vung-ve-cac-hinh-thuc-giao-tiep-va-cong-nghe-giao-tiep.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-11-tu-vung/22802-tu-vung-ve-khoa-hoc-va-cong-nghe.html","https://www.tienganh123.com/tieng-anh-lop-8-sach-moi-bai-12-tu-vung/23066-tu-vung-ve-su-song-tren-cac-hanh-tinh-khac.html"]


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
        {'name': 'TypeWord'},
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

def ch(x):    # chuẩn hóa xâu
    return str(x).strip()

# ____________________________________ Process _____________________________________

for URL in URLs:
    page = requests.get(URL, headers=headers, cookies=cookies)
    print(page.status_code)
    time.sleep(0.3)
    soup = BeautifulSoup(page.content, 'lxml')

    # Xử lí Title
    title = deckNameFinal
    unit = soup.find_all("span", itemprop='name')[1].text  # 'Unit 1: My new school'

    number = unit[unit.find(" ")+1:unit.find(":")]
    numberZero=number.zfill(2)
    unit = unit.replace(number, numberZero)

    title += "::" + unit + "::"

    sub_title = soup.find('h1',class_='v3_lesson_title').text
    title+=sub_title

    createDeck(title)
    print(title)

    # Get list từ vựng
    list_vocab = soup.find_all('li', class_='vocab_box')

    video = json.loads(soup.find('div', {"id": "video_show_0"}).text)['mp4']

    for vocab in list_vocab:
        vocab_word = vocab.find('div', class_="vocab_word")
        vocab_mean = vocab.find('div', class_="vocab_mean")
        vocab_exam = vocab.find('div', class_="vocab_exam")

        Word = vocab_word.span.text  # artisan
        ipa = vocab_word.span.next_sibling.next_sibling.text    # /ˌɑːtɪˈzæn/
        typeWord = vocab_mean.div.text.strip().replace('(','').replace(')','')  # n.
        meaningOfWord = vocab_mean.div.next_sibling  # thợ làm nghề thủ công
        example = vocab_exam.span.text  # Lan's father is a skillful artisan.
        # Bố của Lan là một thợ thủ công lành nghề.
        meaningOfExample = vocab_exam.div.text
        # https://www.tienganh123.com/file/phothong/lop9/bai1/lesson1/ly-thuyet/img/1.jpg
        image = vocab.find('div', class_='vocab_img').img['src']
        # https://www.tienganh123.com/file/phothong/lop9/bai1/lesson1/ly-thuyet/audio/1.mp3
        audioOfWord = vocab_word.find(
            'span', class_='uba_audioButton')['media-url']
        audioOfExample = vocab_exam.find(
            'span', class_='uba_audioButton')['media-url']

        addNote([ch(Word), ch(ipa), ch(typeWord), ch(meaningOfWord), ch(example),
                ch(meaningOfExample), ch(image), ch(audioOfWord), ch(audioOfExample), ch(video)])

saveAnkiPackage(deckNameFinal)

