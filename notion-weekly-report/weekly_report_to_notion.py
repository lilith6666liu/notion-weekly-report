#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周报自动归档到 Notion 脚本
使用方法：
1. 在 JoySpace 中复制周报内容（包括标题）
2. 运行此脚本：python3 weekly_report_to_notion.py
3. 脚本会自动创建页面到 Notion
"""

from notion_client import Client
import subprocess
import sys

# ==================== 配置区域 ====================
# 请在这里填入你的 Notion 配置信息

# Notion Integration Token（从 https://www.notion.so/my-integrations 获取）
NOTION_TOKEN = "your_notion_token_here"

# Notion Database ID（从你的 Notion 页面 URL 中获取）
DATABASE_ID = "your_database_id_here"

# ==================== 配置区域结束 ====================


def parse_clipboard_content():
    """从剪贴板读取并解析内容"""
    try:
        result = subprocess.run(['pbpaste'], capture_output=True, text=True, check=True)
        content = result.stdout
        
        if not content or content.strip() == "":
            print("❌ 剪贴板为空，请先复制周报内容")
            print("💡 提示：请在 JoySpace 中选中周报内容（包括标题），按 Cmd+C 复制后再运行脚本")
            return None, None
        
        lines = content.strip().split('\n')
        title = lines[0].strip()
        body = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
        
        return title, body
    except Exception as e:
        print(f"❌ 读取剪贴板失败: {e}")
        return None, None


def create_notion_page(title, body):
    """创建 Notion 页面到 Database"""
    try:
        notion = Client(auth=NOTION_TOKEN)
        
        # 获取 Database 信息
        db_info = notion.databases.retrieve(database_id=DATABASE_ID)
        properties = db_info.get('properties', {})
        
        # 构建页面内容
        children = []
        if body:
            paragraphs = body.split('\n')
            for para in paragraphs:
                para = para.strip()
                if para:
                    children.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{
                                "type": "text",
                                "text": {"content": para}
                            }]
                        }
                    })
        
        # 构建属性 - 查找标题属性
        page_properties = {}
        title_property = None
        
        for prop_name, prop_info in properties.items():
            if prop_info.get('type') == 'title':
                title_property = prop_name
                break
        
        if title_property:
            page_properties[title_property] = {
                "title": [{
                    "text": {"content": title}
                }]
            }
        else:
            # 对于空 Database，使用默认方式
            page_properties = {
                "title": {
                    "title": [{
                        "text": {"content": title}
                    }]
                }
            }
        
        # 创建页面
        new_page = notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties=page_properties,
            children=children if children else []
        )
        
        page_url = new_page.get("url", "")
        print(f"✅ 周报已成功归档到 Notion！")
        print(f"📄 标题: {title}")
        print(f"🔗 链接: {page_url}")
        
        return True
    except Exception as e:
        print(f"❌ 创建 Notion 页面失败: {e}")
        print("\n💡 故障排查：")
        print("1. 确认已在 Notion 页面的「集成」菜单中添加了你的 Integration")
        print("2. 确认 NOTION_TOKEN 和 DATABASE_ID 配置正确")
        print("3. 查看详细错误信息：")
        import traceback
        traceback.print_exc()
        return False


def main():
    # 检查配置
    if NOTION_TOKEN == "your_notion_token_here" or DATABASE_ID == "your_database_id_here":
        print("❌ 请先配置 NOTION_TOKEN 和 DATABASE_ID")
        print("📖 配置方法请查看 README.md")
        sys.exit(1)
    
    print("=" * 50)
    print("📝 周报自动归档到 Notion")
    print("=" * 50)
    
    print("\n⏳ 正在读取剪贴板内容...")
    title, body = parse_clipboard_content()
    
    if not title:
        sys.exit(1)
    
    print(f"✓ 已读取标题: {title}")
    print(f"✓ 正文长度: {len(body)} 字符")
    
    print("\n⏳ 正在创建 Notion 页面...")
    success = create_notion_page(title, body)
    
    if success:
        print("\n🎉 完成！")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
