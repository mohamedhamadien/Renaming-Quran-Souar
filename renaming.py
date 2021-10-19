import os
import pathlib
from pathlib import Path

# List of Sower names
names_sower = ['الفاتحة', 'البقرة', 'آل عمران', ' النساء', 'المائدة', ' الأنعام', ' الأعراف', ' الأنفال', ' التوبة',
               ' يونس', ' هود', 'يوسف', ' الرعد', 'ابراهيم', ' الحجر', ' النحل', 'الإسراء', 'الكهف', ' مريم', ' طه', ' الأنبياء',
               ' الحج', ' المؤمنون', ' النور', ' الفرقان', ' الشعراء', ' النمل', ' القصص', ' العنكبوت', ' الروم', ' لقمان', ' السجدة', ' الأحزاب', 'سبأ', ' فاطر', ' يس', ' الصافات', ' ص', ' الزمر', ' غافر', ' فصلت', ' الشوري', ' الزخرف', ' الدخان', ' الجاثية', ' الأحقاف', ' محمد', ' الفتح', ' الحجرات', ' ق', ' الذاريات', ' الطور', ' النجم', ' القمر', ' الرحمن', '  الواقعة', ' الحديد', ' المجادلة', ' الحشر', ' الممتحنة', ' الصف', ' الجمعة', ' المنافقون', ' التغابن', ' الطلاق', ' التحريم', ' الملك', ' القلم',
               'الحاقة', ' المعارج', ' نوح', ' الجن', ' المزمل', ' المدثر', ' القيامة', ' الإنسان', ' المرسلات', ' النبأ', ' النازعات',
               'عبس', ' التكوير', ' الإنفطار', ' المطففين', ' الانشقاق', ' البروج', ' الطارق', ' الأعلى', ' الغاشية', ' الفجر',
               'البلد', ' الشمس', ' الليل', ' الضحى', ' الشرح', ' التين', ' العلق', ' القدر', ' البينة', ' الزلزلة', ' العاديات',
               'القارعة', ' التكاثر', ' العصر', ' الهمزة', ' الفيل', ' قريش', ' الماعون', ' الكوثر', ' الكافرون', ' النصر', ' المسد', ' الإخلاص',
               ' الفلق', ' الناس']

# Loop to get path for every sourah
for i in range(1, 115, 1):
    # add 00 at start of count to be like 001 002 ..
    formating = format(i, "03d")
    # path of every sourah
    file_path = Path(F'{formating}.mp3')
    #get currntly path
    current_path = pathlib.Path().resolve()
    # get files name in current path
    files_names = os.listdir(current_path)
    
    #looping in files to check if files missing 
    for x in files_names[:-1]:
         myFile = x
         #convert myFile to path to use it in condition
         myFile_path = Path(myFile)
         if myFile_path == file_path :
               os.rename(file_path, f'{i}-{names_sower[i-1]}.mp3')

print('Done All Souar Renamed.')