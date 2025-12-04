
# & 'd:\01.project\CodeIt\.venv\Scripts\python.exe' -m streamlit run "d:\01.project\CodeIt\streamit\test_steamit.py"

import streamlit as st


image_dir=r"D:\01.project\CodeIt\data\catanddog\cats"



# ════════════════════════════════════════
# 1. 페이지 설정 (브라우저 탭 제목 등)
# ════════════════════════════════════════
st.set_page_config(
    page_title="시각화 데모",  # 브라우저 탭 제목
    page_icon="📊",                   # 브라우저 탭 아이콘
    layout="wide",                    # 레이아웃 (wide 또는 centered)
    initial_sidebar_state="expanded"  # 사이드바 초기 상태
)

# ════════════════════════════════════════
# 2. 앱 제목 설정
# ════════════════════════════════════════
st.title("간단한 Streamlit 데이터 시각화 데모")

# ════════════════════════════════════════
# 3. 사용자 입력 받기 (사이드바)
# ════════════════════════════════════════
st.sidebar.header("이미지 목록")
# Image_dir의 목록을 불러와서 사이드바에 표시
import os

simage_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# 페이지네이션 (20개씩 표시)
items_per_page = 20
total_pages = (len(simage_files) - 1) // items_per_page + 1

if total_pages > 1:
    page = st.sidebar.slider("페이지", 1, total_pages, 1)
else:
    page = 1

start_idx = (page - 1) * items_per_page
end_idx = min(start_idx + items_per_page, len(simage_files))
current_page_files = simage_files[start_idx:end_idx]

# ════════════════════════════════════════
# 4. 라디오 버튼으로 이미지 선택
# ════════════════════════════════════════
selected_image = st.sidebar.radio(
    f"이미지 선택 ({start_idx + 1}-{end_idx} / 총 {len(simage_files)}개)",
    current_page_files,
    index=0
)

# 디버깅: 선택한 파일 출력
print(f"[DEBUG] 선택된 이미지: {selected_image}")
print(f"[DEBUG] 현재 페이지: {page}, 인덱스 범위: {start_idx}-{end_idx}")

# ════════════════════════════════════════
# 5. 이미지 표시
# ════════════════════════════════════════
image_path = os.path.join(image_dir, selected_image)
st.image(image_path, caption=selected_image)

# ════════════════════════════════════════
# 6. 이미지 정보 표시
# ════════════════════════════════════════
from PIL import Image
image = Image.open(image_path)
st.write("이미지 크기:", image.size)
st.write("이미지 모드:", image.mode)
st.write("이미지 포맷:", image.format)  
st.write("파일 크기 (바이트):", os.path.getsize(image_path))
st.write("파일 경로:", image_path)
st.write("파일 이름:", selected_image)
st.write("파일 확장자:", os.path.splitext(selected_image)[1])
