# 🤖 Git Auto Committer

[![CI](https://github.com/lovelybugf/Auto-commit-tool/actions/workflows/ci.yml/badge.svg)](https://github.com/lovelybugf/Auto-commit-tool/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/lovelybugf/Auto-commit-tool?include_prereleases)](https://github.com/lovelybugf/Auto-commit-tool/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Công cụ CLI chuyên nghiệp tự động quét các dự án Git, cập nhật README và tạo commit theo ngày tùy chỉnh.

---

## ✨ Tính năng

- **🔍 Auto Scan** — Tự động quét ổ đĩa để tìm tất cả Git repositories
- **📝 README Update** — Tự động thêm/cập nhật Activity Log trong README
- **📅 Backdated Commits** — Tạo commit với ngày tùy chỉnh (cả `GIT_AUTHOR_DATE` & `GIT_COMMITTER_DATE`)
- **🎲 Randomized** — Giờ commit ngẫu nhiên (9h–21h), message ngẫu nhiên với emoji
- **🚀 Auto Push** — Tùy chọn tự động push lên remote
- **⚙️ Configurable** — Cài đặt linh hoạt qua `config.json`
- **🖥️ Interactive CLI** — Giao diện terminal tương tác với menu đẹp mắt

--

## 📋 Yêu Cầu

- Python 3.8+
- Git đã cài đặt và cấu hình (`git config user.name` & `git config user.email`)

---

## 🚀 Cài Đặt

### Từ source (Development)

```bash
git clone https://github.com/lovelybugf/Auto-commit-tool.git
cd Auto-commit-tool
pip install -e .
```

### Chạy trực tiếp

```bash
# Qua module
python -m auto_committer

# Qua entry point (sau khi pip install)
auto-committer

# Kiểm tra version
python -m auto_committer --version
```

---

## 📖 Sử Dụng

### Auto Mode (Không cần tương tác)

Chạy tool hoàn toàn tự động (quét repos, thêm mới, tạo commit) mà không cần xác nhận:

```bash
python -m auto_committer --auto
# Hoặc
auto-committer -a
```

### Interactive Mode (Menu tương tác)

```bash
python -m auto_committer
```

Sẽ mở menu tương tác:

```
╔══════════════════════════════════════════════════════╗
║           🤖 GIT AUTO COMMITTER v1.0.0              ║
║        Production Commit Automation Tool              ║
╚══════════════════════════════════════════════════════╝

  ┌─────────────────────────────────────┐
  │          📋 MAIN MENU               │
  ├─────────────────────────────────────┤
  │  [1] 🔍 Scan repos trên ổ đĩa       │
  │  [2] 📂 Quản lý danh sách repos      │
  │  [3] 📝 Auto commit                  │
  │  [4] 🚀 Auto commit + Push            │
  │  [5] ⚙️  Cài đặt                      │
  │  [0] ❌ Thoát                         │
  └─────────────────────────────────────┘
```

### Chức năng chính

| # | Chức năng | Mô tả |
|---|-----------|-------|
| 1 | **Scan repos** | Quét ổ đĩa tìm Git repos, thêm vào danh sách |
| 2 | **Quản lý repos** | Thêm/xóa/dọn dẹp danh sách repos |
| 3 | **Auto commit** | Tạo commit tự động theo khoảng ngày |
| 4 | **Commit + Push** | Commit và tự động push lên remote |
| 5 | **Cài đặt** | Tuỳ chỉnh scan path, depth, commits/day... |

---

## 📁 Cấu Trúc Dự Án

```
Auto-commit-tool/
├── src/
│   └── auto_committer/
│       ├── __init__.py      # Package metadata & version
│       ├── __main__.py      # Entry point (python -m)
│       ├── cli.py           # Interactive menu interface
│       ├── scanner.py       # Git repo discovery
│       ├── committer.py     # Commit creation engine
│       ├── config.py        # Configuration management
│       └── utils.py         # UI helpers & ANSI colors
├── tests/
│   ├── test_scanner.py      # Scanner unit tests
│   └── test_committer.py    # Committer unit tests
├── .github/workflows/
│   ├── ci.yml               # CI: lint + test
│   └── release.yml          # Auto release on tag
├── config.json              # Runtime configuration
├── pyproject.toml           # Python packaging
├── CHANGELOG.md             # Version history
├── COMMIT_CONVENTION.md     # Commit standards
├── CONTRIBUTING.md          # Contribution guide
├── LICENSE                  # MIT License
└── README.md                # This file
```

---

## ⚙️ Cấu Hình

File `config.json` ở root dự án:

```json
{
    "scan_path": "D:\\",
    "max_depth": 2,
    "min_commits_per_day": 1,
    "max_commits_per_day": 3,
    "auto_push": false,
    "time_range_start": "09:00",
    "time_range_end": "21:00",
    "commit_messages": [
        "📝 Update README with daily activity log",
        "🔧 Refactor and improve documentation",
        "..."
    ]
}
```

---

## 🧪 Testing

```bash
# Chạy tests
pytest

# Với coverage report
pytest --cov=auto_committer --cov-report=term-missing -v
```

---

## 🔄 Versioning

Dự án sử dụng [Semantic Versioning](https://semver.org/):

- **MAJOR** — Thay đổi không tương thích ngược
- **MINOR** — Thêm tính năng mới, tương thích ngược
- **PATCH** — Sửa lỗi, tương thích ngược

Xem [CHANGELOG.md](./CHANGELOG.md) để biết lịch sử phiên bản.

---

## 🤝 Đóng Góp

Xem [CONTRIBUTING.md](./CONTRIBUTING.md) để biết hướng dẫn chi tiết.

Quy chuẩn commit: [COMMIT_CONVENTION.md](./COMMIT_CONVENTION.md)

---

## ⚠️ Lưu Ý

- Tool sẽ **hỏi xác nhận** trước khi tạo commit
- Mỗi commit sẽ **chỉ thay đổi file README** — không ảnh hưởng source code
- Commit message được chọn **ngẫu nhiên** từ danh sách có emoji
- Giờ commit random trong khoảng **9:00–21:00** để trông tự nhiên
- Dùng auto push cẩn thận — đảm bảo bạn có quyền push lên remote

---

## 📄 License

[MIT License](./LICENSE) — Tự do sử dụng và chỉnh sửa.

<!-- auto-committer-log -->

---

## 📅 Activity Log

| Date | Status |
|------|--------|
| 2026-05-18 13:07:53 | ✅ Updated |

> 🤖 Auto-maintained by Git Auto Committer
