import streamlit as st

# -----------------------------
# TFT Hero Tracker (Streamlit Web App)
# -----------------------------
# 功能：
#   - 8 个玩家，通过网页点击勾选当前持有的英雄
#   - 玩家名称：红1、红2、紫1、紫2、黄1、黄2、蓝1、蓝2
#   - 实时统计无人持有的英雄 & 每张牌被持有次数
#   - 一键清空所有勾选
# 部署：
#   streamlit run tft_hero_tracker_streamlit.py
#   或部署到 Streamlit Cloud
# -----------------------------

HEROES = [
    "安妮", "亚菲利欧", "布兰德", "科加斯", "雷欧娜", "好运姐", "妮可", "史瓦妮",
    "薇可丝", "莉雅", "劫", "婕莉", "希格斯",
]
PLAYER_NAMES = ["红1", "红2", "紫1", "紫2", "黄1", "黄2", "蓝1", "蓝2"]

st.set_page_config(page_title="TFT Hero Tracker", layout="wide")
st.title("TFT Hero Tracker")

# 初始化 Session State（可选，多余也无大碍）
for pname in PLAYER_NAMES:
    for hero in HEROES:
        key = f"{pname}-{hero}"
        if key not in st.session_state:
            st.session_state[key] = False

# 布局：8 列，每列一个玩家
cols = st.columns(len(PLAYER_NAMES))
for idx, pname in enumerate(PLAYER_NAMES):
    with cols[idx]:
        st.subheader(pname)
        for hero in HEROES:
            key = f"{pname}-{hero}"
            # 只创建 Checkbox，状态存储在 session_state 中
            st.checkbox(hero, key=key)

# 统计逻辑
counts = {hero: 0 for hero in HEROES}
for pname in PLAYER_NAMES:
    for hero in HEROES:
        if st.session_state.get(f"{pname}-{hero}", False):
            counts[hero] += 1

# 显示结果
unpicked = [h for h, c in counts.items() if c == 0]
st.markdown("**没人拿的牌：** " + ("，".join(unpicked) if unpicked else "无"))

st.markdown("---")
st.subheader("各牌被持有次数")
for hero, c in counts.items():
    st.write(f"{hero}: {c}")

# 清空按钮
if st.button("清空全部勾选"):
    for key in list(st.session_state.keys()):
        if "-" in key:
            st.session_state[key] = False
    st.experimental_rerun()
