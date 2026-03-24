#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
假Windows桌面演示程序启动器
Fake Windows Desktop Demo Launcher

功能：
- 启动假的Windows 10桌面
- 自动打开Word文档并演示打字效果
- 展示百度原生全模态大模型文心5.0介绍
"""

import os
import sys
import webbrowser
import tempfile
import shutil
from pathlib import Path


def get_html_content():
    """获取HTML内容 - 从同目录下的HTML文件读取"""
    # 获取脚本所在目录
    script_dir = Path(__file__).parent.absolute()
    html_file = script_dir / "fake_windows_desktop.html"
    
    if html_file.exists():
        with open(html_file, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # 如果HTML文件不存在，使用内嵌的简化版本
        return get_embedded_html()


def get_embedded_html():
    """内嵌的简化HTML版本（备用）"""
    return r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Windows 10</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; }
        body { font-family: "Segoe UI", "Microsoft YaHei UI", sans-serif; overflow: hidden; background: #000; }
        .desktop {
            width: 100vw; height: 100vh;
            background: url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&q=80') center/cover no-repeat;
            position: relative;
        }
        .desktop::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, rgba(0,20,40,0.3) 0%, rgba(0,40,80,0.2) 50%, rgba(0,20,40,0.3) 100%);
            pointer-events: none;
        }
        .word-window {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 960px; height: 640px; background: #f3f3f3; border-radius: 6px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.35); display: none; flex-direction: column; overflow: hidden; z-index: 100;
        }
        .word-window.show { display: flex; animation: windowOpen 0.25s ease-out; }
        @keyframes windowOpen { from { opacity: 0; transform: translate(-50%,-48%) scale(0.96); } to { opacity: 1; transform: translate(-50%,-50%) scale(1); } }
        .word-titlebar { height: 32px; background: linear-gradient(180deg, #2b579a 0%, #28508e 100%); display: flex; align-items: center; justify-content: center; }
        .word-titlebar span { color: white; font-size: 12px; }
        .word-document-area { flex: 1; background: #e8e8e8; display: flex; justify-content: center; overflow: auto; padding: 16px 0; }
        .word-page { width: 816px; min-height: 1056px; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.12); padding: 72px; }
        .document-title { font-size: 22px; font-weight: bold; color: #1a1a1a; margin-bottom: 20px; text-align: center; font-family: "Microsoft YaHei", sans-serif; }
        .document-content { font-size: 12pt; line-height: 2; color: #1a1a1a; white-space: pre-wrap; font-family: "Microsoft YaHei", sans-serif; }
        .cursor { display: inline-block; width: 2px; height: 16px; background: #000; animation: blink 0.6s steps(1) infinite; vertical-align: text-bottom; margin-left: 1px; }
        @keyframes blink { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }
        .taskbar { position: absolute; bottom: 0; left: 0; right: 0; height: 48px; background: rgba(32,32,32,0.85); display: flex; align-items: center; backdrop-filter: blur(30px); }
        .start-button { width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; cursor: pointer; }
        .start-button:hover { background: rgba(255,255,255,0.1); }
        .start-button svg { width: 18px; height: 18px; fill: white; }
        .datetime { margin-left: auto; display: flex; flex-direction: column; align-items: flex-end; padding: 0 14px; height: 100%; justify-content: center; }
        .datetime-time { color: white; font-size: 12px; }
        .datetime-date { color: white; font-size: 12px; }
    </style>
</head>
<body>
    <div class="desktop">
        <div class="word-window show" id="wordWindow">
            <div class="word-titlebar"><span>百度原生全模态大模型文心5.0介绍.docx - Word</span></div>
            <div class="word-document-area">
                <div class="word-page">
                    <div class="document-title" id="docTitle"></div>
                    <div class="document-content" id="docContent"><span class="cursor"></span></div>
                </div>
            </div>
        </div>
        <div class="taskbar">
            <div class="start-button"><svg viewBox="0 0 24 24"><path d="M3 3h8v8H3V3zm10 0h8v8h-8V3zM3 13h8v8H3v-8zm10 0h8v8h-8v-8z"/></svg></div>
            <div class="datetime">
                <span class="datetime-time" id="time">12:00</span>
                <span class="datetime-date" id="date">2024/1/1</span>
            </div>
        </div>
    </div>
    <script>
        const documentText = `文心5.0基础能力全面升级，在多模态理解、指令遵循、创意写作、事实性、智能体规划与工具应用等方面表现突出，拥有强大的理解、逻辑、记忆和说服力。在40余项权威基准的综合评测中，其语言与多模态理解能力与 Gemini-2.5-Pro、GPT-5-High 等模型持平，图像与视频生成能力与垂直领域专精模型相当，达到全球领先水平，验证了原生全模态大模型的能力和潜力。

文心5.0在多模态理解、指令遵循、创意写作、事实性、智能体规划与工具应用等方面表现突出。

百度创始人李彦宏会上表示，大模型技术在快速迭代，其智能水平不断突破极限，模型思考时间变长，原生全模态统一，将自我学习和迭代，具备创新能力。"智能本身是最大的应用，而技术迭代速度是唯一护城河。百度会持续投入、研发更前沿的模型，推高智能天花板。"

百度首席技术官王海峰介绍，文心大模型5.0是新一代原生全模态大模型。不同于业界多数的多模态模型采用后期融合的方式，文心5.0的技术路线是采用统一的自回归架构进行原生全模态建模，理解与生成一体化。从训练开始便融合语言、图像、视频、音频等多模态数据，使得多模态特征在统一架构下充分融合并协同优化，实现原生的全模态统一理解与生成。

依托飞桨深度学习框架，文心5.0采用了超稀疏混合专家架构，进行庞大的全模态训练，总参数规模超过2.4万亿，激活参数比例低于3%，在保持模型强大能力的同时有效提升推理效率。同时，基于大规模工具环境，合成长程任务轨迹数据，并采用基于思维链和行动链的端到端多轮强化学习训练，显著提升了模型的智能体和工具调用能力。

目前，文心大模型5.0 Preview 已同步上线文心 App，用户可直接体验；开发者和企业用户也可通过百度千帆大模型平台调用 API 服务。

此前在11月8日，LMArena 大模型竞技场最新排名显示，文心模型 ERNIE-5.0-Preview-1022在文本任务评测中位列全球并列第二、中国第一，尤其在创意写作、复杂问题理解等方面表现突出。`;
        let charIndex = 0, isTyping = false;
        const titleText = "百度原生全模态大模型文心5.0介绍";
        function updateClock() {
            const now = new Date();
            document.getElementById('time').textContent = now.getHours().toString().padStart(2, '0') + ':' + now.getMinutes().toString().padStart(2, '0');
            document.getElementById('date').textContent = now.getFullYear() + '/' + (now.getMonth() + 1).toString().padStart(2, '0') + '/' + now.getDate().toString().padStart(2, '0');
        }
        function startTyping() {
            isTyping = true; charIndex = 0;
            const titleEl = document.getElementById('docTitle');
            const contentEl = document.getElementById('docContent');
            titleEl.textContent = '';
            let titleIndex = 0;
            function typeTitle() {
                if (titleIndex < titleText.length) { titleEl.textContent += titleText[titleIndex++]; setTimeout(typeTitle, 60); }
                else setTimeout(typeContent, 400);
            }
            function typeContent() {
                if (charIndex < documentText.length) {
                    contentEl.innerHTML = documentText.substring(0, ++charIndex) + '<span class="cursor"></span>';
                    setTimeout(typeContent, documentText[charIndex-1] === '\n' ? 100 : Math.random() * 25 + 15);
                } else { isTyping = false; contentEl.innerHTML = documentText; }
            }
            typeTitle();
        }
        updateClock(); setInterval(updateClock, 1000);
        window.onload = () => setTimeout(startTyping, 800);
    </script>
</body>
</html>'''


def run_demo():
    """启动演示程序"""
    print("=" * 60)
    print("  假 Windows 10 桌面演示程序")
    print("  Fake Windows 10 Desktop Demo")
    print("=" * 60)
    print()
    print("正在启动...")
    print()
    
    temp_dir = tempfile.mkdtemp(prefix="fake_windows_")
    html_file = os.path.join(temp_dir, "desktop.html")
    
    try:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(get_html_content())
        
        print("演示说明:")
        print("  1. 程序将在浏览器中打开模拟的 Windows 10 桌面")
        print("  2. 页面加载后自动打开 Word 文档")
        print("  3. Word 自动打字，介绍百度原生全模态大模型文心5.0")
        print()
        print("-" * 60)
        
        webbrowser.open('file://' + html_file)
        
        input("\n按回车键退出...")
        
    except KeyboardInterrupt:
        print("\n程序已退出")
    finally:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass


def main():
    """主函数"""
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
        print("用法:")
        print("  python fake_desktop_launcher.py        启动演示程序")
        print("  python fake_desktop_launcher.py --help 显示帮助信息")
        print()
        print("打包成 EXE:")
        print("  pip install pyinstaller")
        print("  pyinstaller --onefile --noconsole --name 'Windows演示' fake_desktop_launcher.py")
        print()
        print("注意: 打包时请确保 fake_windows_desktop.html 文件在同一目录")
        return
    
    run_demo()


if __name__ == "__main__":
    main()
