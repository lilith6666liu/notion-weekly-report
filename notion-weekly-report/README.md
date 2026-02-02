# 周报自动归档到 Notion

一键将 JoySpace 周报自动归档到 Notion，告别手动复制粘贴！

## ✨ 功能特点

- 📋 **一键归档**：复制周报内容后运行脚本，自动创建到 Notion
- 🎯 **保持格式**：标题和正文自动解析，保留段落结构
- ⚡ **快速高效**：2秒完成归档，比手动操作快10倍
- 🔧 **简单配置**：只需配置一次，永久使用

## 🚀 快速开始

### 1. 安装依赖

```bash
pip3 install notion-client
```

### 2. 配置 Notion

#### 2.1 创建 Notion Integration

1. 访问 [Notion Integrations](https://www.notion.so/my-integrations)
2. 点击 **"+ New integration"**
3. 填写信息：
   - **Name（名称）**：周报自动归档
   - **Associated workspace**：选择你的工作区
   - **Type**：Internal
4. 提交后复制 **Internal Integration Token**（以 `secret_` 开头）

#### 2.2 获取 Database ID

1. 打开你的 Notion 周报归档页面
2. 复制浏览器地址栏的 URL
3. URL 格式：`https://www.notion.so/xxxxx?v=yyyy`
4. 其中 `xxxxx` 就是 Database ID

#### 2.3 授权 Integration

1. 在 Notion 周报页面，点击右上角 `···`
2. 点击 **"集成"** 或 **"Integrations"**
3. 选择你刚创建的 **"周报自动归档"** Integration
4. 确认添加

### 3. 配置脚本

编辑 `weekly_report_to_notion.py`，修改以下配置：

```python
# Notion 配置
NOTION_TOKEN = "your_notion_token_here"  # 替换为你的 Token
DATABASE_ID = "your_database_id_here"    # 替换为你的 Database ID
```

### 4. 使用方法

1. 在 JoySpace 中复制周报内容（包括标题）
2. 运行脚本：
   ```bash
   python3 weekly_report_to_notion.py
   ```
3. 完成！查看 Notion 确认归档成功

## 💡 进阶配置：设置快捷键（可选）

### macOS 用户

创建一个快捷命令，按快捷键即可运行：

1. 打开 **"自动操作"（Automator）**
2. 新建 **"快速操作"**
3. 添加 **"运行 Shell 脚本"**
4. 输入：
   ```bash
   cd /path/to/your/script && python3 weekly_report_to_notion.py
   ```
5. 保存为 "归档周报"
6. 在 **系统设置 > 键盘 > 快捷键 > 服务** 中设置快捷键（如 `Cmd+Shift+W`）

### 使用 Alfred/Raycast

如果你使用 Alfred 或 Raycast，可以创建一个 Workflow/Script Command：

```bash
#!/bin/bash
cd /path/to/your/script
python3 weekly_report_to_notion.py
```

## 📝 周报格式要求

脚本会自动解析剪贴板内容：
- **第一行**：作为 Notion 页面标题
- **其余内容**：作为页面正文，保留段落结构

示例：
```
2026年第5周周报

本周工作总结：
1. 完成了用户增长模块的开发
2. 修复了3个线上bug

下周计划：
1. 开始新功能的设计
```

## 🔧 故障排查

### 问题1：提示"剪贴板为空"
- **原因**：未复制内容或复制失败
- **解决**：重新在 JoySpace 中选中内容并复制（Cmd+C）

### 问题2：提示"Could not find page/database"
- **原因**：未授权 Integration 访问 Database
- **解决**：在 Notion 页面的"集成"菜单中添加你的 Integration

### 问题3：提示"属性不存在"
- **原因**：Database 结构与脚本不匹配
- **解决**：运行 `check_notion_db.py` 查看 Database 属性，或联系开发者

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📮 联系方式

如有问题或建议，欢迎通过 GitHub Issues 联系。

---

**享受自动化带来的效率提升！** 🚀
