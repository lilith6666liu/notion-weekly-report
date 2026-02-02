# 📦 项目文件说明

## 文件结构

```
notion-weekly-report/
├── README.md                      # 项目说明文档
├── QUICKSTART.md                  # 快速开始指南
├── LICENSE                        # MIT 开源协议
├── requirements.txt               # Python 依赖包
├── .gitignore                     # Git 忽略文件
└── weekly_report_to_notion.py     # 主程序脚本
```

## 给同事的部署指南

### 方法 1：下载 ZIP（推荐给不熟悉 Git 的同事）

1. 点击 GitHub 页面右上角绿色的 **"Code"** 按钮
2. 选择 **"Download ZIP"**
3. 解压到任意文件夹
4. 按照 `QUICKSTART.md` 的步骤配置

### 方法 2：使用 Git Clone

```bash
git clone https://github.com/你的用户名/notion-weekly-report.git
cd notion-weekly-report
```

然后按照 `QUICKSTART.md` 配置。

## 核心文件说明

### weekly_report_to_notion.py

主程序脚本，包含：
- 剪贴板内容读取
- Notion API 调用
- 自动解析标题和正文
- 错误处理和提示

**需要配置的地方：**
```python
NOTION_TOKEN = "your_notion_token_here"  # 第 17 行
DATABASE_ID = "your_database_id_here"    # 第 20 行
```

### requirements.txt

Python 依赖包列表：
- `notion-client`: Notion 官方 Python SDK

安装命令：
```bash
pip3 install -r requirements.txt
```

### README.md

完整的项目文档，包括：
- 功能介绍
- 详细配置步骤
- 使用方法
- 进阶配置（快捷键）
- 故障排查

### QUICKSTART.md

3 分钟快速上手指南，适合第一次使用的同事。

## 发布到 GitHub 的步骤

1. 在 GitHub 创建新仓库（Repository）
2. 仓库名称建议：`notion-weekly-report`
3. 不要勾选 "Initialize with README"（我们已经有了）
4. 创建后，按照 GitHub 提示运行：

```bash
cd /Users/liuliu.lilith/Documents/notion-weekly-report
git remote add origin https://github.com/你的用户名/notion-weekly-report.git
git branch -M main
git push -u origin main
```

## 分享给同事

发布后，把 GitHub 仓库链接发给同事，告诉他们：

1. 打开链接
2. 点击 "Download ZIP" 下载
3. 解压后打开 `QUICKSTART.md` 跟着做
4. 3 分钟搞定！

---

**提示**：建议在 README.md 中添加截图，让同事更容易理解配置步骤。
