# 快速开始指南

## 第一次使用？跟着这个指南 3 分钟完成配置！

### 步骤 1：安装依赖（30秒）

打开终端，运行：

```bash
pip3 install -r requirements.txt
```

### 步骤 2：配置 Notion（2分钟）

#### 2.1 创建 Integration

1. 打开 https://www.notion.so/my-integrations
2. 点击 **"+ New integration"**
3. 名称填：`周报自动归档`
4. 选择你的工作区
5. 点击提交
6. **复制显示的 Token**（以 `secret_` 开头）

#### 2.2 获取 Database ID

1. 打开你的 Notion 周报页面
2. 复制浏览器地址栏的 URL
3. URL 格式：`https://www.notion.so/xxxxx?v=yyyy`
4. **复制 `xxxxx` 部分**（这就是 Database ID）

#### 2.3 授权 Integration

1. 在 Notion 周报页面，点击右上角 `···`
2. 点击 **"集成"**
3. 选择 **"周报自动归档"**
4. 确认添加

### 步骤 3：配置脚本（30秒）

编辑 `weekly_report_to_notion.py` 文件，找到这两行：

```python
NOTION_TOKEN = "your_notion_token_here"  # 替换为步骤 2.1 的 Token
DATABASE_ID = "your_database_id_here"    # 替换为步骤 2.2 的 Database ID
```

把刚才复制的 Token 和 Database ID 填进去，保存。

### 步骤 4：测试（30秒）

1. 复制下面这段测试内容：

```
测试周报

这是一个测试
看看能否成功归档
```

2. 运行脚本：

```bash
python3 weekly_report_to_notion.py
```

3. 看到 ✅ 成功提示，打开 Notion 确认！

---

## 日常使用

以后每次写完周报：

1. 在 JoySpace 复制周报内容（Cmd+C）
2. 运行 `python3 weekly_report_to_notion.py`
3. 完成！

---

## 遇到问题？

查看 [README.md](README.md) 的「故障排查」部分，或提交 Issue。
