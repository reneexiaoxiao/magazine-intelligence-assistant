# 📌 重要说明：如何使用这个工具

## 这个工具是做什么的？

这是一个**杂志智能助手工具包**，包含两个部分：

### 1. Python工具（本地运行）
```bash
python tools/setup_wizard.py      # 配置你的偏好
python tools/split_magazine.py    # 切分PDF文章
```

### 2. AI Prompt模板（配合任何AI使用）
```
复制 template/magazine_recommender_skill.md 的内容
↓
粘贴到 Claude / ChatGPT / 其他AI平台
↓
获得个性化的文章推荐
```

---

## 🎯 使用流程

### 方式A：完全本地（不推荐）
只运行Python工具，手动整理文章

### 方式B：AI辅助（推荐）⭐
1. 运行 `setup_wizard.py` 配置偏好
2. 复制 AI Prompt 模板到 Claude/ChatGPT
3. 获得智能推荐和分类

### 方式C：Claude Code集成（高级）⭐⭐⭐
1. 在Claude Code中使用这个skill
2. 自动切分+分类+整理
3. 完全自动化工作流

---

## 🔑 关键区别

| 特性 | GitHub版本 | 你原本的版本 |
|------|-----------|-------------|
| 用户偏好 | 通用，需要配置 | Rene定制 |
| 使用场景 | 任何人 | 个人专用 |
| AI平台 | Claude/ChatGPT等 | Claude专用 |
| 文档位置 | `~/Desktop/杂志精读/` | GitHub仓库 |

---

## 💡 推荐使用方式

**你的工作流：**
```
Deskto p/杂志精读/
├── tools/           ← 从GitHub复制过来的工具
├── template/        ← AI Prompt模板
└── WIRED_2026-03/   ← 你的杂志

使用时：
1. 运行 setup_wizard.py
2. 复制 prompt 到 Claude
3. 获得推荐
```

**别人使用时：**
```
下载GitHub项目
↓
运行 setup_wizard.py
↓
配置自己的偏好
↓
使用任何AI平台
```

---

## ❓ 常见问题

**Q: 必须用Claude Code吗？**
A: 不必须！可以用Claude网页版、ChatGPT、或其他AI平台。

**Q: 这个工具能在手机上用吗？**
A: 配置需要在电脑上，但AI推荐部分可以在手机上用（复制prompt到手机上的AI）。

**Q: 能配合Notion/Obsidian用吗？**
A: 可以！JSON输出可以转换为任何格式。

---

这个说明清楚了吗？我需要把它加到主README里。
