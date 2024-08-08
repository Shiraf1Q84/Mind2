import streamlit as st
import requests
import json

# タイトル
st.title('MindSearch - インテリジェント検索アシスタント')

# 入力欄
query = st.text_input('質問を入力してください:')

# 実行ボタン
if st.button('実行'):
    if query:
        # APIリクエスト
        response = requests.post('http://localhost:8002/solve', json={'inputs': query})

        # レスポンス処理
        if response.status_code == 200:
            # EventSourceResponseを処理
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        json_data = json.loads(decoded_line[5:])
                        response_data = json_data['response']
                        # ここにレスポンスを表示する処理を追加
                        st.write(response_data['response'])
        else:
            st.error('エラーが発生しました。')
    else:
        st.warning('質問を入力してください。')