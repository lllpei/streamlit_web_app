import streamlit as st

st.title('Aアプリ')
st.caption('これはテストアプリです')

st.subheader('自己紹介')
st.text('Aです。よろしくお願いします。')

code = '''
AAAAAAAAAAAAAAA

BBBBBBBBBBBBBBBB
'''
st.code(code, language='python')


with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')


print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')


