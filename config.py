class Config:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://live.bilibili.com',
        'Referer': 'https://live.bilibili.com/5225369?spm_id_from=333.334.b_62696c695f6c697665.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.119 Safari/537.36'
    }

    data = {
        'room_id': '未配置',
        'csrf_token': 'fa56950667934cf5a3479ca94abc1f9a',
        'csrf': 'fa56950667934cf5a3479ca94abc1f9a',
        'visit_id': ''
    }

    url = 'https://api.live.bilibili.com/ajax/msg'

    font = "等线"
    font_size = 20
    font_color = (255, 255, 255)
    screen_size = (500, 500)
    background_color = (255, 255, 255)
    barrage_remain_num = 8
    frame_rate = 30
    end_frame = 600

