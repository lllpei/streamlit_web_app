import streamlit as st
import time

st.title('Aアプリ')
st.caption('これはテストアプリです')
st.subheader('自己紹介')
code = '''
AAAAAAAAAAAAAAA
BBBBBBBBBBBBBBBB
'''
st.code(code, language='python')

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    # テキストエリア
    text_area = st.text_area('Text Area', 'Input some text here.')

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        with st.spinner('processiong...'):
            time.sleep(3)
            st.write('end!')

    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！テキストエリアに「{text_area}」について、入力されました。')

print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')


