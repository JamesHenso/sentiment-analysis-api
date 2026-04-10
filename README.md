# Phân Tích Cảm Xúc Đa Ngôn Ngữ với FastAPI và Hugging Face

## 1. Thông tin sinh viên

- **Họ và tên:** Nguyễn Hữu Khánh
- **MSSV:** 24120340
- **Môn học:** Tư duy tính toán
- **LAB - 1:** API

## 2. Tên mô hình và liên kết Hugging Face

- **Tên mô hình:** `tabularisai/multilingual-sentiment-analysis`
- **Liên kết mô hình:** https://huggingface.co/tabularisai/multilingual-sentiment-analysis

## 3. Mô tả ngắn về chức năng hệ thống

Hệ thống cung cấp API phân tích cảm xúc cho văn bản đa ngôn ngữ (ví dụ: tiếng Việt, tiếng Anh).
Người dùng gửi câu văn bản qua endpoint `/predict`, hệ thống trả về:

- Nhãn cảm xúc dự đoán (label)
- Độ tin cậy của dự đoán (confidence score)

Ngoài ra còn có endpoint kiểm tra trạng thái hoạt động (`/health`) và endpoint mô tả nhanh dịch vụ (`/`).

## 4. Hướng dẫn cài đặt thư viện

### Yêu cầu

- Python 3.8 trở lên
- Kết nối internet khi tải mô hình từ Hugging Face lần đầu

### Cài đặt

1. Tạo môi trường ảo:

```bash
python -m venv .venv
```

2. Kích hoạt môi trường ảo:

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

- Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

3. Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

## 5. Hướng dẫn chạy chương trình

### Chạy bằng uvicorn

```bash
uvicorn main:app --reload
```

Sau khi chạy thành công, chờ: `INFO: Application startup complete`
Mở API mặc định tại: `http://127.0.0.1:8000`

## 6. Hướng dẫn gọi API và ví dụ request/response

> **Lưu ý quan trọng khi dùng Windows PowerShell:**
> Trong PowerShell, `curl` thường là alias của `Invoke-WebRequest` (không phải curl chuẩn), nên có thể lỗi khi dùng cú pháp `-X`, `-H`, `-d` như trên Linux/macOS.
> Để tránh lỗi, hãy dùng `curl.exe` hoặc `Invoke-RestMethod` như ví dụ bên dưới.

### Danh sách endpoint

| Method | Endpoint   | Mô tả                               |
| ------ | ---------- | ----------------------------------- |
| GET    | `/`        | Thông tin tổng quan dịch vụ         |
| GET    | `/health`  | Kiểm tra trạng thái API             |
| POST   | `/predict` | Dự đoán cảm xúc cho văn bản đầu vào |

### 6.1. GET `/`

Ví dụ:

macOS/Linux (curl):

```bash
curl http://127.0.0.1:8000/
```

Windows PowerShell (curl.exe):

```powershell
curl.exe http://127.0.0.1:8000/
```

Response mẫu:

```json
{
	"name": "Multilingual Sentiment Analysis API",
	"model": "tabularisai/multilingual-sentiment-analysis",
	"description": "Gui POST request chua van ban toi /predict de phan tich cam xuc (Positive, Negative, Neutral,...)."
}
```

### 6.2. GET `/health`

Ví dụ:

macOS/Linux (curl):

```bash
curl http://127.0.0.1:8000/health
```

Windows PowerShell (curl.exe):

```powershell
curl.exe http://127.0.0.1:8000/health
```

Response mẫu:

```json
{
	"status": "ok",
	"message": "API is up and running!"
}
```

### 6.3. POST `/predict`

#### Request body

```json
{
	"text": "Món ăn rất giòn"
}
```

#### Gọi bằng cURL

macOS/Linux (curl):

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
	-H "Content-Type: application/json" \
	-d '{"text":"Món ăn rất giòn"}'
```

Windows PowerShell (curl.exe):

```powershell
curl.exe -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"text\":\"Món ăn rất giòn\"}"
```

Windows PowerShell (Invoke-RestMethod):

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/predict" -Method Post -ContentType "application/json" -Body '{"text":"Món ăn rất giòn"}'
```

#### Response thành công (mẫu)

```json
{
	"success": true,
	"input_text": "Món ăn rất giòn",
	"prediction": "POSITIVE",
	"confidence_score": 0.9876
}
```

Lưu ý: `prediction` và `confidence_score` thay đổi theo nội dung đầu vào.

#### Response lỗi khi text rỗng

Request:

```json
{
	"text": "   "
}
```

Response:

```json
{
	"detail": "Văn bản đầu vào không được để trống."
}
```

### 6.4. Chạy file test mẫu

Repository có sẵn file `test.py` để thử nhanh các endpoint:

```bash
python test.py
```

### 7. Video demo



https://github.com/user-attachments/assets/c1e9e4a0-237d-4407-867d-41f9978a1c89


