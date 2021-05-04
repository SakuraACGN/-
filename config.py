class Config:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://live.bilibili.com',
        'Referer': 'https://live.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    }

    data = {
        'roomid': '7734200',
        'csrf_token': 'fa56950667934cf5a3479ca94abc1f9a',
        'csrf': 'fa56950667934cf5a3479ca94abc1f9a',
        'visit_id': '',
    }

    url = 'https://api.live.bilibili.com/ajax/msg'

    font = "等线"
    font_size = 20
    font_color = (100, 120, 255)
    screen_size = (500, 500)
    background_color = (20, 124, 47)
    barrage_remain_num = 8
    frame_rate = 30
    end_frame = 600

