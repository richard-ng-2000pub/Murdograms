# KDP Puzzle SVG Solutions — GitHub Pages Repo

Repo tĩnh dành cho sách KDP có 80 puzzle. Mỗi puzzle có URL ổn định:

- `/p/001/`
- `/p/002/`
- ...
- `/p/080/`

Mỗi trang hiển thị một SVG tại `solutions/solution_XXX.svg`.

## 1. Thay 80 SVG thật

Cách đơn giản nhất: đổi tên file của bạn thành:

`001.svg, 002.svg, ... 080.svg`

Sau đó chạy:

```bash
python tools/replace_solutions.py "DUONG_DAN_DEN_FOLDER_SVG"
```

Hoặc tự copy đè trực tiếp vào thư mục `solutions/` theo tên:

`solution_001.svg ... solution_080.svg`

Kiểm tra repo:

```bash
python tools/check_repo.py
```

## 2. Upload lên GitHub

1. Tạo một repository mới trên GitHub, ví dụ `book-solutions`.
2. Chọn Public nếu muốn dùng GitHub Pages miễn phí theo cách đơn giản nhất.
3. Upload toàn bộ nội dung của repo này vào **root** của repository.
4. Vào **Settings → Pages**.
5. Ở **Build and deployment**, chọn **Deploy from a branch**.
6. Branch: `main`, folder: `/ (root)`, rồi Save.
7. GitHub sẽ cấp URL dạng:
   `https://USERNAME.github.io/book-solutions/`

Lưu ý: Nếu chưa dùng custom domain, QR phải bao gồm `/book-solutions`, ví dụ:
`https://USERNAME.github.io/book-solutions/p/001/`

## 3. Khuyến nghị dùng custom domain

Ví dụ:

`https://answers.yourdomain.com/p/001/`

Trong GitHub Pages → Custom domain, nhập `answers.yourdomain.com`.

Sau khi GitHub xác nhận domain, bật **Enforce HTTPS**.

File `CNAME.example` chỉ là mẫu. Khi đã quyết định domain, đổi tên nó thành `CNAME` và sửa nội dung thành domain thật, hoặc để GitHub tự tạo file khi cấu hình Pages.

## 4. Tạo 80 QR code

Cài thư viện:

```bash
pip install -r requirements.txt
```

Nếu dùng custom domain:

```bash
python tools/generate_qr.py --base-url https://answers.yourdomain.com
```

Nếu dùng GitHub Pages project URL:

```bash
python tools/generate_qr.py --base-url https://USERNAME.github.io/book-solutions
```

QR sẽ nằm trong thư mục `qr/` với tên:

`qr_001.png ... qr_080.png`

## 5. Quan trọng về bảo mật

GitHub Pages là website công khai. `robots.txt` và `noindex` trong repo này giúp giảm khả năng công cụ tìm kiếm lập chỉ mục, nhưng **không phải cơ chế bảo mật**.

Nếu một người biết URL chính xác, họ vẫn có thể mở trang đáp án. Nếu bạn cần chỉ người mua sách mới truy cập được, cần dùng hệ thống có xác thực/token thay vì GitHub Pages thuần.

## 6. Khuyến nghị in trong sách

Nên in cả QR và URL chữ nhỏ phía dưới, ví dụ:

`answers.yourdomain.com/p/037/`

Như vậy nếu QR bị bẩn hoặc camera không quét được, độc giả vẫn truy cập được bằng tay.
