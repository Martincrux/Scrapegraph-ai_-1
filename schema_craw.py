# ==============================================================================
#  This code was written by himmeow the coder.
#  Contact: himmeow.thecoder@gmail.com
#  Discord server: https://discord.gg/deua7trgXc
#
#  Feel free to use and modify this code as you see fit. 
#  If you find it helpful, I'd appreciate a coffee!
#  - Momo: 0374525177
#  - Vietcombank (VCB): 1014622635
# ==============================================================================

from typing import List
from pydantic import BaseModel, Field
from scrapegraphai.utils import prettify_exec_info
from scrapegraphai.graphs import SmartScraperGraph

# Khóa API của Gemini Pro
gemini_key = "GOOGLE_APIKEY"

# Định nghĩa cấu trúc dữ liệu cho tin tức
class News(BaseModel):
    title: str = Field(description="Tiêu đề của tin tức")
    public_time: str = Field(description="Thời gian tin tức được đăng tải")
    description: str = Field(description="Tóm tắt ngắn gọn của tin tức")

# Định nghĩa cấu trúc dữ liệu cho danh sách tin tức
class NewsList(BaseModel):
    news: List[News]

# Cấu hình cho LLM
graph_config = {
    "llm": {
        "api_key": gemini_key,
        "model": "gemini-pro",
    },
}

# Tạo một đối tượng SmartScraperGraph
smart_scraper_graph = SmartScraperGraph(
    prompt="Hãy liệt kê các tin tức mới nhất",
    source="https://vtv.vn/vtv-news.html",
    schema=NewsList,  # Định dạng dữ liệu đầu ra
    config=graph_config
)

# Thực thi đồ thị và lưu kết quả vào biến result
result = smart_scraper_graph.run()
print(result)

# In thông tin về quá trình thực thi đồ thị
graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))