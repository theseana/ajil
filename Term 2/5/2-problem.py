# اندازه دو ضلع کنار هم از یک چهار ضلعی رو بگیریم
# بعد اگر مربع بود چاپ کنه مربع اگر مستطیل بود چاپ کنه مستطیل
# RECTANGLE                     SQUARE
# SHAPE

side_1 = input('Enter Side 1: ')
side_2 = input('Enter Side 2: ')

if side_1 == side_2:
    print('Your Shape is Square')
else:
    print('Your Shape is Rectangle')