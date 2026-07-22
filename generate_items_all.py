import os
import uuid
import urllib.parse
from email.utils import formatdate

# ==============================
# 配置区域（需要修改）
# ==============================
AUDIO_DIR = r"\\ipfs\download\茶话会"   # 注意：不要以 \ 结尾
BASE_URL = "https://67373.chatcyf.com/%E8%8C%B6%E8%AF%9D%E4%BC%9A/"   # 末尾务必加 /
OUTPUT_FILE = "items.xml"

# ==============================
# 工具函数：安全拼接 URL 路径
# ==============================
def build_url(base_url, relative_path):
    """
    将本地相对路径转换为 URL 路径，并逐段进行 URL 编码
    """
    parts = relative_path.replace("\\", "/").split("/")
    encoded_parts = [urllib.parse.quote(p) for p in parts]
    return base_url + "/".join(encoded_parts)

# ==============================
# 生成 item 列表
# ==============================
items_output = ""

for root, dirs, files in os.walk(AUDIO_DIR):
    for filename in files:
        if not filename.lower().endswith(".mp3"):
            continue

        full_path = os.path.join(root, filename)

        # 计算相对 AUDIO_DIR 的路径（包含子目录）
        relative_path = os.path.relpath(full_path, AUDIO_DIR)

        # 生成完整 URL（自动带子目录）
        file_url = build_url(BASE_URL, relative_path)

        # 文件大小
        length = os.path.getsize(full_path)

        # GUID
        guid = str(uuid.uuid4())

        # pubDate 使用文件修改时间
        timestamp = os.path.getmtime(full_path)
        pub_date = formatdate(timestamp, usegmt=True)

        # 标题为文件名（去后缀）
        title = os.path.splitext(filename)[0]

        item = f"""
    <item>
        <title>{title}</title>
        <description><![CDATA[{title}]]></description>
        <enclosure url="{file_url}" length="{length}" type="audio/mpeg" />
        <guid>{guid}</guid>
        <pubDate>{pub_date}</pubDate>
        <itunes:explicit>no</itunes:explicit>
    </item>
    """

        items_output += item

# ==============================
# 保存结果
# ==============================
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(items_output)

print(f"音频 item 已生成：{OUTPUT_FILE}")
