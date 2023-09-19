import time

def focus_timer(minutes):
    seconds = minutes * 60

    while seconds > 0:
        minutes_remaining = seconds // 60
        seconds_remaining = seconds % 60

        print(f"剩余时间：{minutes_remaining}分钟 {seconds_remaining}秒")
        time.sleep(1)
        seconds -= 1

    print("专注时间结束！")

# 设置专注时间为25分钟（可以根据需要进行调整）
focus_timer(25)
