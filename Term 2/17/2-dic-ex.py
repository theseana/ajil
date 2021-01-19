en_pe = {
    'i': 'من',
    'am': 'هستم',
    'a': 'یک',
    'student': 'دانش آموز'
}

txt = 'i am a student'
txt_list = txt.split()
txt_pe = ""

for i in txt_list:
    txt_pe = txt_pe + en_pe[i] + " "
    
print(txt_pe)
