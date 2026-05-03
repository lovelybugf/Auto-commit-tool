# 📋 Quy Chuẩn Commit Code (Commit Convention)

> **Phiên bản:** 1.0.0  
> **Cập nhật lần cuối:** 2026-05-03  
> **Áp dụng cho:** Toàn bộ thành viên trong team phát triển sản phẩm

---

## Mục Lục

- [1. Tổng Quan](#1-tổng-quan)
- [2. Cấu Trúc Commit Message](#2-cấu-trúc-commit-message)
- [3. Các Loại Commit (Type)](#3-các-loại-commit-type)
- [4. Scope (Phạm Vi)](#4-scope-phạm-vi)
- [5. Quy Tắc Viết Subject](#5-quy-tắc-viết-subject)
- [6. Body (Nội Dung Chi Tiết)](#6-body-nội-dung-chi-tiết)
- [7. Footer (Chân Commit)](#7-footer-chân-commit)
- [8. Breaking Changes](#8-breaking-changes)
- [9. Ví Dụ Thực Tế](#9-ví-dụ-thực-tế)
- [10. Quy Trình Làm Việc Với Git](#10-quy-trình-làm-việc-với-git)
- [11. Quy Tắc Branch](#11-quy-tắc-branch)
- [12. Code Review & Merge Request](#12-code-review--merge-request)
- [13. Những Điều KHÔNG Được Làm](#13-những-điều-không-được-làm)
- [14. Công Cụ Hỗ Trợ](#14-công-cụ-hỗ-trợ)

---

## 1. Tổng Quan

Tài liệu này định nghĩa quy chuẩn commit code cho toàn bộ dự án, dựa trên tiêu chuẩn [Conventional Commits](https://www.conventionalcommits.org/) và được tùy chỉnh phù hợp với quy trình phát triển sản phẩm chuyên nghiệp.

### Mục tiêu

- ✅ Đảm bảo **lịch sử commit rõ ràng**, dễ đọc và dễ truy vết
- ✅ Hỗ trợ **tự động hóa** changelog, semantic versioning
- ✅ Tăng hiệu quả **code review** và **collaboration**
- ✅ Đảm bảo **chất lượng code** và tính nhất quán trong team

---

## 2. Cấu Trúc Commit Message

Mỗi commit message **BẮT BUỘC** tuân theo cấu trúc sau:

```
<type>(<scope>): <subject>

[body]

[footer]
```

### Quy tắc chung

| Thành phần | Bắt buộc | Mô tả |
|------------|----------|-------|
| `type` | ✅ Có | Loại thay đổi |
| `scope` | ⚠️ Khuyến khích | Phạm vi ảnh hưởng |
| `subject` | ✅ Có | Mô tả ngắn gọn (tối đa 72 ký tự) |
| `body` | ❌ Tùy chọn | Giải thích chi tiết lý do thay đổi |
| `footer` | ❌ Tùy chọn | Tham chiếu issue, breaking changes |

---

## 3. Các Loại Commit (Type)

### Loại chính (Primary Types)

| Type | Emoji | Mô tả | Ví dụ |
|------|-------|--------|-------|
| `feat` | ✨ | Thêm tính năng mới | Thêm chức năng đăng nhập bằng Google |
| `fix` | 🐛 | Sửa lỗi (bug fix) | Sửa lỗi crash khi mở app trên Android 12 |
| `hotfix` | 🚑 | Sửa lỗi khẩn cấp trên production | Sửa lỗi bảo mật SQL injection |

### Loại bổ sung (Secondary Types)

| Type | Emoji | Mô tả | Ví dụ |
|------|-------|--------|-------|
| `docs` | 📝 | Thay đổi documentation | Cập nhật README, API docs |
| `style` | 💄 | Thay đổi format code (không ảnh hưởng logic) | Sửa indentation, thêm dấu phẩy |
| `refactor` | ♻️ | Tái cấu trúc code (không thêm tính năng, không sửa lỗi) | Tách function, đổi tên biến |
| `perf` | ⚡ | Cải thiện hiệu năng | Tối ưu query database |
| `test` | ✅ | Thêm hoặc sửa test | Thêm unit test cho module auth |
| `build` | 🏗️ | Thay đổi build system, dependencies | Upgrade Gradle, thêm thư viện |
| `ci` | 👷 | Thay đổi CI/CD configuration | Cập nhật GitHub Actions workflow |
| `chore` | 🔧 | Công việc maintenance khác | Cập nhật .gitignore, config files |
| `revert` | ⏪ | Hoàn tác commit trước đó | Revert commit abc1234 |
| `release` | 🚀 | Đánh dấu phiên bản release | Release version 2.1.0 |
| `security` | 🔒 | Sửa lỗi bảo mật | Vá lỗ hổng XSS |
| `i18n` | 🌐 | Thay đổi liên quan đến đa ngôn ngữ | Thêm bản dịch tiếng Nhật |
| `a11y` | ♿ | Cải thiện accessibility | Thêm aria-label cho button |
| `ux` | 🎨 | Cải thiện UI/UX | Đổi màu nút CTA, cải thiện animation |

---

## 4. Scope (Phạm Vi)

Scope xác định **module/component** bị ảnh hưởng bởi commit. Sử dụng tên module hoặc feature area.

### Ví dụ scope theo dự án

```
feat(auth): thêm xác thực 2 yếu tố
fix(payment): sửa lỗi tính thuế VAT
refactor(database): tối ưu connection pool
docs(api): cập nhật tài liệu endpoint v2
test(cart): thêm integration test cho giỏ hàng
```

### Danh sách scope gợi ý

| Scope | Mô tả |
|-------|--------|
| `auth` | Module xác thực, đăng nhập |
| `user` | Quản lý người dùng |
| `payment` | Thanh toán |
| `order` | Đơn hàng |
| `product` | Sản phẩm |
| `cart` | Giỏ hàng |
| `notification` | Thông báo |
| `search` | Tìm kiếm |
| `admin` | Trang quản trị |
| `api` | API endpoints |
| `database` | Cơ sở dữ liệu |
| `config` | Cấu hình hệ thống |
| `ui` | Giao diện người dùng |
| `core` | Logic nghiệp vụ chính |
| `infra` | Hạ tầng, DevOps |

> [!TIP]
> Team nên thống nhất danh sách scope cụ thể cho dự án và cập nhật khi có module mới.

---

## 5. Quy Tắc Viết Subject

### ✅ Nên

- Viết bằng **tiếng Anh** (ưu tiên) hoặc **tiếng Việt không dấu** nhất quán
- Bắt đầu bằng **động từ nguyên thể** (add, fix, update, remove, refactor...)
- Giới hạn tối đa **72 ký tự**
- Viết **chữ thường** ở ký tự đầu tiên
- Không kết thúc bằng dấu chấm (`.`)
- Mô tả **cái gì đã thay đổi**, không phải cách thay đổi

### ❌ Không nên

- ❌ `Fix bug` → quá chung chung
- ❌ `Updated the login page to fix the issue with...` → quá dài
- ❌ `feat: Add new feature.` → không kết thúc bằng dấu chấm
- ❌ `FEAT: add login` → type không viết hoa

### Ví dụ tốt vs xấu

| ❌ Xấu | ✅ Tốt |
|---------|--------|
| `fix bug` | `fix(auth): resolve token expiration on refresh` |
| `update code` | `refactor(user): extract validation logic to service` |
| `add stuff` | `feat(cart): add quantity adjustment for cart items` |
| `WIP` | `feat(search): add autocomplete suggestions (WIP)` |
| `asdfgh` | `fix(payment): correct VAT calculation for EU region` |

---

## 6. Body (Nội Dung Chi Tiết)

Body cung cấp **ngữ cảnh và lý do** cho sự thay đổi. Sử dụng khi commit phức tạp hoặc cần giải thích.

### Quy tắc

- Cách dòng trống sau subject
- Mỗi dòng tối đa **100 ký tự**
- Giải thích **tại sao** thay đổi, không phải **thay đổi gì** (code đã thể hiện)
- Có thể dùng bullet points (`-` hoặc `*`)

### Ví dụ

```
fix(auth): resolve session timeout on mobile devices

The session was expiring after 5 minutes on mobile browsers due to
a misconfigured cookie SameSite attribute. This caused users to be
logged out unexpectedly during checkout flow.

- Changed SameSite from 'Strict' to 'Lax' for session cookies
- Added session heartbeat mechanism every 2 minutes
- Updated session config to extend timeout to 30 minutes
```

---

## 7. Footer (Chân Commit)

Footer chứa thông tin bổ sung như **tham chiếu issue**, **breaking changes**, hoặc **co-author**.

### Tham chiếu Issue/Task

```
fix(payment): correct discount calculation logic

Closes #142
Refs #138, #140
```

### Ký hiệu tham chiếu

| Từ khóa | Hành động |
|---------|-----------|
| `Closes #<id>` | Tự động đóng issue khi merge |
| `Fixes #<id>` | Tự động đóng issue (đánh dấu là fixed) |
| `Refs #<id>` | Tham chiếu liên quan (không đóng) |
| `Resolves #<id>` | Tự động đóng issue |
| `Related to #<id>` | Liên quan nhưng không đóng |

### Co-authored

```
feat(dashboard): add real-time analytics widget

Co-authored-by: Nguyen Van A <a.nguyen@company.com>
Co-authored-by: Tran Thi B <b.tran@company.com>
```

---

## 8. Breaking Changes

Khi commit chứa **thay đổi không tương thích ngược** (breaking change):

### Cách 1: Thêm `!` sau type/scope

```
feat(api)!: change authentication endpoint response format
```

### Cách 2: Dùng `BREAKING CHANGE` trong footer

```
feat(api): migrate to v2 authentication endpoints

BREAKING CHANGE: The /api/v1/auth/login endpoint has been removed.
All clients must migrate to /api/v2/auth/login which now returns
a JWT token instead of a session ID.

Migration guide: https://docs.company.com/migration/auth-v2
```

> [!CAUTION]
> Breaking changes **BẮT BUỘC** phải được thông báo cho toàn team trước khi merge và phải có migration guide đi kèm.

---

## 9. Ví Dụ Thực Tế

### Commit đơn giản

```
feat(user): add email verification on registration
```

```
fix(ui): correct button alignment on mobile landscape
```

```
docs(readme): update installation instructions for Windows
```

### Commit có body

```
perf(search): optimize full-text search query performance

Replaced LIKE queries with PostgreSQL's tsvector full-text search.
Query execution time reduced from ~800ms to ~45ms on 1M records.

- Created GIN index on searchable columns
- Added search_vector column with trigger for auto-update
- Implemented query caching with 5-minute TTL
```

### Commit có breaking change

```
feat(api)!: restructure API response envelope

BREAKING CHANGE: API response format has changed.

Before:
{
  "data": [...],
  "error": null
}

After:
{
  "status": "success",
  "data": [...],
  "meta": { "page": 1, "total": 100 },
  "errors": []
}

Fixes #256
Refs #200, #234
```

### Commit revert

```
revert: feat(cart): add bulk delete functionality

This reverts commit 3a5c8d2.

Reason: Bulk delete was causing cascade deletion of saved-for-later
items. Rolling back until the issue is properly investigated.

Refs #301
```

---

## 10. Quy Trình Làm Việc Với Git

### 10.1. Workflow tổng quan

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Working   │────▶│   Staging   │────▶│    Local     │
│  Directory  │     │    Area     │     │  Repository  │
└─────────────┘     └─────────────┘     └──────┬───────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │   Remote     │
                                        │  Repository  │
                                        └─────────────┘
```

### 10.2. Trước khi commit

```bash
# 1. Pull code mới nhất
git pull origin <branch> --rebase

# 2. Kiểm tra thay đổi
git status
git diff

# 3. Stage files có chọn lọc (KHÔNG dùng git add .)
git add src/auth/login.service.ts
git add src/auth/login.controller.ts

# 4. Kiểm tra lại staged changes
git diff --staged

# 5. Commit
git commit -m "feat(auth): add OAuth2 login with Google provider"
```

### 10.3. Nguyên tắc commit

| Nguyên tắc | Mô tả |
|------------|--------|
| **Atomic Commits** | Mỗi commit chỉ chứa **một thay đổi logic duy nhất** |
| **Compilable** | Code sau mỗi commit **phải build được** |
| **Testable** | Code sau mỗi commit **phải pass tất cả tests** |
| **No WIP on main** | Không commit code dang dở lên `main`/`develop` |
| **Frequent commits** | Commit thường xuyên, tránh commit lớn |

> [!IMPORTANT]
> **Quy tắc vàng**: Nếu bạn không thể mô tả commit trong 72 ký tự, có thể bạn đang commit quá nhiều thay đổi cùng lúc. Hãy tách ra thành nhiều commit nhỏ hơn.

---

## 11. Quy Tắc Branch

### 11.1. Mô hình branching

```
main (production)
 │
 ├── develop (development)
 │    │
 │    ├── feature/AUTH-123-google-login
 │    ├── feature/CART-456-bulk-operations
 │    │
 │    ├── bugfix/PAY-789-vat-calculation
 │    │
 │    └── release/v2.1.0
 │
 ├── hotfix/SEC-001-sql-injection-fix
 │
 └── support/v1.x
```

### 11.2. Quy tắc đặt tên branch

| Loại | Format | Ví dụ |
|------|--------|-------|
| Feature | `feature/<TICKET>-<short-desc>` | `feature/AUTH-123-google-login` |
| Bugfix | `bugfix/<TICKET>-<short-desc>` | `bugfix/PAY-789-vat-calc` |
| Hotfix | `hotfix/<TICKET>-<short-desc>` | `hotfix/SEC-001-xss-fix` |
| Release | `release/v<version>` | `release/v2.1.0` |
| Experiment | `experiment/<desc>` | `experiment/new-search-algo` |

### 11.3. Quy tắc bảo vệ branch

| Branch | Push trực tiếp | Merge qua MR/PR | Approval cần | Auto tests |
|--------|---------------|-----------------|--------------|------------|
| `main` | ❌ Cấm | ✅ Bắt buộc | ≥ 2 người | ✅ Bắt buộc |
| `develop` | ❌ Cấm | ✅ Bắt buộc | ≥ 1 người | ✅ Bắt buộc |
| `release/*` | ❌ Cấm | ✅ Bắt buộc | ≥ 2 người | ✅ Bắt buộc |
| `feature/*` | ✅ Cho phép | ✅ Khi merge | ≥ 1 người | ✅ Khuyến khích |
| `hotfix/*` | ✅ Cho phép | ✅ Khi merge | ≥ 1 người | ✅ Bắt buộc |

---

## 12. Code Review & Merge Request

### 12.1. Checklist trước khi tạo MR/PR

- [ ] Code đã build thành công (no errors)
- [ ] Tất cả tests đã pass
- [ ] Không có conflict với target branch
- [ ] Đã self-review code
- [ ] Commit messages tuân thủ convention
- [ ] Đã cập nhật documentation (nếu cần)
- [ ] Đã thêm/cập nhật tests cho thay đổi
- [ ] Không chứa credentials, secrets, hoặc dữ liệu nhạy cảm
- [ ] Performance không bị ảnh hưởng tiêu cực

### 12.2. Template Merge Request

```markdown
## 📋 Mô tả
<!-- Mô tả ngắn gọn thay đổi -->

## 🔗 Ticket liên quan
<!-- Link đến Jira/Trello/Linear ticket -->
- Closes #<issue_number>

## 📸 Screenshots (nếu có UI changes)
<!-- Đính kèm ảnh before/after -->

## ✅ Loại thay đổi
- [ ] 🐛 Bug fix (thay đổi không breaking, sửa issue)
- [ ] ✨ New feature (thay đổi không breaking, thêm tính năng)
- [ ] 💥 Breaking change (thay đổi gây ảnh hưởng tính năng hiện tại)
- [ ] 📝 Documentation update
- [ ] ♻️ Refactoring
- [ ] ⚡ Performance improvement

## 🧪 Đã test như thế nào?
<!-- Mô tả các test đã thực hiện -->
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## 📝 Checklist
- [ ] Code tuân thủ coding standards
- [ ] Self-review đã hoàn thành
- [ ] Comments đã được thêm cho code phức tạp
- [ ] Documentation đã cập nhật
- [ ] Không có warning mới
- [ ] Tests đã được thêm và pass
```

### 12.3. Quy tắc review

| Vai trò | Trách nhiệm |
|---------|-------------|
| **Author** | Mô tả rõ ràng, self-review, respond feedback kịp thời |
| **Reviewer** | Review trong 24h, comment constructive, approve/request changes |
| **Approver** | Đảm bảo chất lượng tổng thể, merge khi đủ điều kiện |

---

## 13. Những Điều KHÔNG Được Làm

> [!WARNING]
> Vi phạm các quy tắc sau có thể dẫn đến rollback commit và yêu cầu sửa lại.

### ❌ TUYỆT ĐỐI KHÔNG

| # | Quy tắc | Lý do |
|---|---------|-------|
| 1 | **Commit trực tiếp lên `main`** | Bypass review, gây rủi ro production |
| 2 | **Force push lên shared branches** | Mất lịch sử, conflict cho team |
| 3 | **Commit credentials/secrets** | Lỗ hổng bảo mật nghiêm trọng |
| 4 | **Commit node_modules, build artifacts** | Tăng kích thước repo, không cần thiết |
| 5 | **Commit file có conflict markers** | Code không chạy được |
| 6 | **Squash tất cả thành 1 commit** | Mất lịch sử chi tiết |
| 7 | **Commit code không compile** | Chặn workflow của team |
| 8 | **Dùng `git add .` mà không kiểm tra** | Có thể stage file không mong muốn |
| 9 | **Commit message chung chung** | Không truy vết được khi có lỗi |
| 10 | **Sửa nhiều bug trong 1 commit** | Khó revert từng bug riêng lẻ |

---

## 14. Công Cụ Hỗ Trợ

### 14.1. commitlint

Cài đặt để tự động kiểm tra commit message:

```bash
# Cài đặt
npm install --save-dev @commitlint/{cli,config-conventional}

# Tạo file config commitlint.config.js
echo "module.exports = { extends: ['@commitlint/config-conventional'] };" > commitlint.config.js
```

### 14.2. Husky (Git Hooks)

```bash
# Cài đặt
npm install --save-dev husky
npx husky init

# Thêm commit-msg hook
echo "npx --no -- commitlint --edit \$1" > .husky/commit-msg
```

### 14.3. Commitizen

Interactive commit message builder:

```bash
# Cài đặt
npm install --save-dev commitizen cz-conventional-changelog

# Cấu hình trong package.json
# "config": { "commitizen": { "path": "cz-conventional-changelog" } }

# Sử dụng
npx cz
```

### 14.4. Standard Version / Release Please

Tự động tạo changelog và bump version:

```bash
# Standard Version
npm install --save-dev standard-version
npx standard-version

# Hoặc sử dụng Google Release Please (GitHub Action)
# Xem: https://github.com/google-github-actions/release-please-action
```

### 14.5. .gitignore cơ bản

```gitignore
# Dependencies
node_modules/
vendor/
venv/

# Build
dist/
build/
*.pyc
__pycache__/

# IDE
.idea/
.vscode/
*.swp

# Environment
.env
.env.local
.env.*.local

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Coverage
coverage/
.nyc_output/
```

---

## Phụ Lục: Quick Reference Card

```
┌──────────────────────────────────────────────────────────┐
│                  COMMIT MESSAGE FORMAT                    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  <type>(<scope>): <subject>     ← Dòng 1: Tối đa 72 ký │
│                                                          │
│  <body>                         ← Giải thích WHY        │
│                                                          │
│  <footer>                       ← Issues, breaking      │
│                                                          │
├──────────────────────────────────────────────────────────┤
│  TYPES:                                                  │
│  feat ✨  fix 🐛  docs 📝  style 💄  refactor ♻️        │
│  perf ⚡  test ✅  build 🏗️  ci 👷  chore 🔧            │
│  revert ⏪  hotfix 🚑  security 🔒  release 🚀          │
├──────────────────────────────────────────────────────────┤
│  EXAMPLES:                                               │
│  feat(auth): add biometric login support                 │
│  fix(cart): resolve quantity update race condition        │
│  docs(api): add OpenAPI spec for v2 endpoints            │
│  perf(search): implement elasticsearch indexing          │
│  feat(api)!: migrate to GraphQL (BREAKING)               │
└──────────────────────────────────────────────────────────┘
```

---

> **Ghi nhớ:** Một commit message tốt là câu trả lời cho câu hỏi:  
> *"Nếu áp dụng commit này, nó sẽ **[subject]**"*
>
> Ví dụ: *"Nếu áp dụng commit này, nó sẽ **add biometric login support**"* ✅

---

*📌 Tài liệu này được review và cập nhật mỗi quý bởi Tech Lead team.*  
*💬 Mọi đề xuất thay đổi vui lòng tạo issue hoặc liên hệ Tech Lead.*
