# ============================================================
#  EduMS — Cấu hình MySQL
#  Chỉnh sửa thông tin kết nối trước khi chạy
# ============================================================

import os

DB_HOST     = os.getenv('DB_HOST', 'localhost')
DB_PORT     = int(os.getenv('DB_PORT', 3306))
DB_USER     = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME     = os.getenv('DB_NAME', 'edums')

SECRET_KEY  = os.getenv('SECRET_KEY', 'edums_jwt_secret_2024')
DEBUG       = os.getenv('DEBUG', 'True').lower() == 'true'
PORT        = int(os.getenv('PORT', 5000))
