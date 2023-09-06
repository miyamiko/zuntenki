import streamlit as st
# import streamlit.components.v1 as stc
import base64
import time
import requests 
import urllib.request
import tenki

st.title('ずんだもんの声で天気を教えてくれるよ！')
#改行は半角スペース２個と\n
st.write('入力欄に漢字の県名（栃木より西）を含んだ文を入力してください  \n例、神奈川県の天気を教えて')
st.caption('天気予報の詳細からヘッドラインの冒頭22文字抽出して回答します。読み始めるまで数秒かかります。')
prompt=st.chat_input("例、神奈川県の天気を教えて（注意：栃木より西の都道府県のみ対応）")
if prompt:
    message1 = st.chat_message("user")
    message1.write(prompt)
    saved=0
    resten=tenki.tenki(prompt)
    print(resten)
    message = st.chat_message("assistant")
    message.write(f"{resten}（読み上げるからちょっと待ってね！）")
    if resten=='エラー発生した':
        saved=2
    else:
        situmon=resten
        # situmon=prompt
        url=r'https://api.tts.quest/v1/voicevox/?text='+urllib.parse.quote(situmon)+r'&speaker=1'
        res = requests.get(url)
        time.sleep(2.5)
        d=res.json()
        song=d["mp3DownloadUrl"]
        print('urlは'+url)
        print('songは'+song)
        res = requests.get(song)
        print('response_codeは'+str(res.status_code))
        print('savedは'+str(saved))
        if (res.status_code == 200) and (saved==0):
            saved=1
            with open("sample.mp3", "wb") as file:
                file.write(res.content)
                print("ファイルを保存しました。")
        elif res.status_code == 404:
            time.sleep(5)
            res = requests.get(song)
            print('response_codeは'+str(res.status_code))
            print('savedは'+str(saved))
            if (res.status_code == 200) and (saved==0):
                saved=1
                with open("sample.mp3", "wb") as file:
                    file.write(res.content)
                    print("ファイルを保存しました。")
            else:
                    saved=2
                    print("ファイルをダウンロードできませんでした。")
        else:
            saved=2
            print("ファイルをダウンロードできませんでした。")



    if saved:
        if saved==1:
            audio_path1 = 'sample.mp3' #答えの音声ファイル
        else:
            audio_path1 = 'failed.mp3' #失敗音声ファイル
        saved=0
        audio_placeholder = st.empty()

        file_ = open(audio_path1, "rb")
        contents = file_.read()
        file_.close()

        audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
        audio_html = """
                        <audio autoplay=True>
                        <source src="%s" type="audio/ogg" autoplay=True>
                        Your browser does not support the audio element.
                        </audio>
                    """ %audio_str

        audio_placeholder.empty()
        time.sleep(0.5) #これがないと上手く再生されません
        audio_placeholder.markdown(audio_html, unsafe_allow_html=True)
st.markdown('###### Streamelitやこのサイトの関連情報は')
link = '[イチゲブログ](https://kikuichige.com/17180/)'
st.markdown(link, unsafe_allow_html=True)
st.write('<a href="https://voicevox.hiroshiba.jp/" target="_blank">VOICEVOX:ずんだもん</a>', unsafe_allow_html=True)
st.write('<a data-v-730ae480="" href="https://anko.education/apps/weather_api" target="_blank">天気予報の参考：気象庁の天気予報JSONファイルをWebAPI的に利用したサンプルアプリ</a>', unsafe_allow_html=True)
st.write('<a data-v-730ae480="" href="https://www.jma.go.jp/jma/kishou/info/coment.html" target="_blank">気象庁利用規約</a>', unsafe_allow_html=True)
