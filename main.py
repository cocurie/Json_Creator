import json
import openpyxl
import glob

import cv2 #画像表示デバック用




#画像を表示（デバック用）
#image = cv2.imread('/Users/tsurutashuichi/PycharmProjects/pythonProject2/image_strage/dog.犬.1-1.jpg')
#cv2.imshow('image_test',image)
#cv2.waitKey(0)
#cv2.destroyWindow('image_test')
#print(cv2.__version__)


#imageファイルをフォルダから抽出
imageFileName = "dog.犬.1-1.jpg"
imagePath = glob.glob("/Users/tsurutashuichi/PycharmProjects/pythonProject2/image_strage/"+ imageFileName)
print(imageFileName)
print(imagePath)



#JSONファイルを作成
tuningSet = {
    'prompt':'竣工年次1972年の単純PCプレテンT桁橋の主桁の写真です。この橋は精密な点検を必要としますか？',

    'additionalInfo':'主桁の下フランジ側面に鉄筋露出(150×200×20mm)が見られる',

    'answer':'この橋梁は精密検査を必要としていません。この損傷は、縦目地からの路面水の影響により、かぶり不足の鉄筋が腐食・膨張 し、露出したと推定されます。前回の点検に記録はなく、縦目地からの漏水が継続するため、損傷が進行する可能性は高いが、局所的な鉄筋露出であることから直ちに部材の耐荷力が低下する状況ではない。'
}
out = json.dumps(tuningSet, indent=2, ensure_ascii=False)
with open('sample.json', 'wt', encoding='utf-8') as fout:
    fout.write(out)


#excelファイルをオープン
wb = openpyxl.load_workbook('forTest.xlsx')
#シートを選択
sheet = wb['Sheet1']
#セルの値を取得
for i in range(1,8):
    prompt = sheet.cell(row=i, column=1).value \
                +'と' \
                    + sheet.cell(row=i, column=2).value
    print(prompt)

#新たに追加するデータ
add_data = {
    'ddd':{
        'e':'eee'
    }
}
#JSONファイルに追加する辞書データをupdateで追加する
with open('sample.json','r')as file:
    data = json.load(file)
    data.update(add_data)

#JSONファイルにデータを追加(write)する
with open('sample.json', 'w')as file:
    json.dump(data, file, indent=2, ensure_ascii=False)









#####################
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



#testSet = {
#    'test1':{
#        'hours':'7:30',
#        'menus':['pan','bacon']
#    },
#
#    'test2': {
#        '時間': '7:30',
#        'メニュー': ['トースト', 'ベーコン']
#    }
#}





