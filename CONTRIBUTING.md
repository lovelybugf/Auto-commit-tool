# Contributing to Git Auto Committer

Cảm ơn bạn đã quan tâm đến việc đóng góp cho dự án! Dưới đây là hướng dẫn chi tiết.

---

## 🔀 Quy Trình Đóng Góp

### 1. Fork & Clone

```bash
git clone https://github.com/<your-username>/Auto-commit-tool.git
cd Auto-commit-tool
```

### 2. Tạo Branch

Luôn tạo branch mới từ `develop`:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/<short-description>
```

**Quy tắc đặt tên branch:**

| Loại | Format | Ví dụ |
|------|--------|-------|
| Feature | `feature/<desc>` | `feature/add-scheduler` |
| Bugfix | `bugfix/<desc>` | `bugfix/fix-encoding` |
| Hotfix | `hotfix/<desc>` | `hotfix/crash-on-scan` |

### 3. Commit

Tuân thủ [Conventional Commits](./COMMIT_CONVENTION.md):

```bash
git commit -m "feat(scanner): add recursive depth configuration"
```

### 4. Push & Pull Request

```bash
git push origin feature/<short-description>
```

Tạo Pull Request vào branch `develop` (không phải `main`).

---

## 🧪 Chạy Tests

```bash
# Cài đặt development dependencies
pip install pytest

# Chạy tests
pytest

# Chạy với coverage
pip install pytest-cov
pytest --cov=auto_committer
```

---

## 📐 Code Style

- **Python 3.8+** compatible
- **Max line length:** 120 characters
- **Docstrings:** Google style
- **Encoding:** UTF-8 with emoji support

---

## 📋 Checklist Trước Khi Tạo PR

- [ ] Code chạy được (`python -m auto_committer --version`)
- [ ] Tests pass (`pytest`)
- [ ] Commit messages theo convention
- [ ] Đã cập nhật CHANGELOG.md (nếu thêm feature)
- [ ] Không commit file nhạy cảm (repos.txt, .env)

---

## 📝 Quy Trình Release

Chỉ maintainer mới được thực hiện release:

1. Merge `develop` → `main`
2. Cập nhật version trong `src/auto_committer/__init__.py` và `pyproject.toml`
3. Cập nhật `CHANGELOG.md`
4. Tạo tag: `git tag -a v<version> -m "release: v<version>"`
5. Push: `git push origin main --tags`
6. GitHub Actions sẽ tự động tạo release

---

## ❓ Câu Hỏi?

Tạo issue trên [GitHub Issues](https://github.com/lovelybugf/Auto-commit-tool/issues).
