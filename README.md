# 🤖 Git Auto Committer

Công cụ tự động quét các dự án Git trên ổ đĩa, cập nhật README và tạo commit theo ngày tùy chỉnh.

---

## ✨ Tính năng

- **🔍 Auto Scan** — Tự động quét ổ D (hoặc đường dẫn bất kỳ) để tìm tất cả Git repositories
- **📝 README Update** — Tự động thêm/cập nhật phần Activity Log trong README của từng dự án
- **📅 Backdated Commits** — Tạo commit với ngày trong quá khứ (hỗ trợ cả `GIT_AUTHOR_DATE` và `GIT_COMMITTER_DATE`)
- **🎲 Randomized** — Giờ commit ngẫu nhiên (9h–21h), commit message ngẫu nhiên với emoji
- **🚀 Auto Push** — Tùy chọn tự động push lên remote sau khi commit
- **⚙️ Linh hoạt** — Hỗ trợ commit theo số ngày, khoảng ngày cụ thể, hoặc chỉ định từng repo

---

## 📋 Yêu cầu

- Python 3.8+
- Git đã cài đặt và cấu hình (`git config user.name` & `git config user.email`)

---

## 🚀 Sử dụng

### 1. Quét tất cả repos trên ổ D

```powershell
python main.py scan
```

Kết quả:

```
🔍 Scanning D:\ for git repositories...

  ✅ D:\my-project
     Branch: main | Remote: https://github.com/user/my-project.git | README: 📖
  ✅ D:\another-repo
     Branch: dev | Remote: https://gitlab.com/user/another-repo.git | README: ❌

📊 Found 2 repositories.
```

### 2. Tạo commit cho 30 ngày gần nhất

```powershell
python main.py commit --days 30
```

### 3. Tạo commit theo khoảng thời gian cụ thể

```powershell
python main.py commit --from 2026-01-01 --to 2026-04-30
```

### 4. Chỉ commit cho 1 repo cụ thể

```powershell
python main.py commit --repo "D:\my-project" --days 7
```

### 5. Commit và tự động push lên remote

```powershell
python main.py commit --days 7 --push
```

### 6. Nhiều commit mỗi ngày, bỏ qua xác nhận

```powershell
python main.py commit --days 30 --min-commits 1 --max-commits 3 -y
```

---

## 📖 Tham số đầy đủ

### Lệnh `scan`

```powershell
python main.py scan [--path PATH] [--depth DEPTH]
```

| Tham số     | Mặc định | Mô tả                          |
|-------------|----------|---------------------------------|
| `--path`    | `D:\`    | Đường dẫn gốc để quét          |
| `--depth`   | `2`      | Độ sâu quét tối đa             |

### Lệnh `commit`

```powershell
python main.py commit [options]
```

| Tham số           | Mặc định | Mô tả                                  |
|-------------------|----------|-----------------------------------------|
| `--days`          | `30`     | Số ngày tính từ hôm nay về quá khứ     |
| `--from`          | —        | Ngày bắt đầu (YYYY-MM-DD)              |
| `--to`            | —        | Ngày kết thúc (YYYY-MM-DD)             |
| `--repo`          | —        | Đường dẫn repo cụ thể (bỏ qua scan)   |
| `--min-commits`   | `1`      | Số commit tối thiểu mỗi ngày           |
| `--max-commits`   | `1`      | Số commit tối đa mỗi ngày              |
| `--push`          | `false`  | Tự động push sau khi commit            |
| `-y`, `--yes`     | `false`  | Bỏ qua bước xác nhận                   |

---

## 📁 Cấu trúc dự án

```
git-auto-committer/
├── main.py          # CLI chính — điều phối scan và commit
├── scanner.py       # Module quét tìm git repositories
├── committer.py     # Module tạo commit và cập nhật README
├── config.json      # File cấu hình tham khảo
└── README.md        # Tài liệu hướng dẫn
```

---

## ⚠️ Lưu ý

- Tool sẽ **hỏi xác nhận** trước khi tạo commit (dùng `-y` để bỏ qua)
- Mỗi commit sẽ **chỉ thay đổi file README** — không ảnh hưởng source code
- Commit message được chọn **ngẫu nhiên** từ danh sách có emoji
- Giờ commit được random trong khoảng **9:00–21:00** để trông tự nhiên
- Dùng `--push` cẩn thận — đảm bảo bạn có quyền push lên remote

---

## 📄 License

MIT License — Tự do sử dụng và chỉnh sửa.
