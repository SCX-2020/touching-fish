# 假Windows桌面演示程序

一个模拟Windows 10桌面 + Word自动打字效果的演示程序。

## 🎬 效果预览

1. 显示一个模拟的Windows 10桌面（带任务栏、桌面图标）
2. 自动打开Word文档窗口
3. 自动打字，内容为"百度文心一言"介绍
4. 打字效果带有闪烁光标，模拟真实打字体验

## 🚀 快速启动

### 方法一：直接运行HTML文件

双击打开 `fake_windows_desktop.html` 文件，浏览器会自动显示演示效果。

### 方法二：Python脚本启动

```bash
python fake_desktop_launcher.py
```

## 📦 打包成EXE可执行文件

如果你想把程序打包成可以分发的 `.exe` 文件：

### 步骤1：安装PyInstaller

```bash
pip install pyinstaller
```

### 步骤2：打包

```bash
pyinstaller --onefile --noconsole --name "Windows演示" fake_desktop_launcher.py
```

参数说明：
- `--onefile`: 打包成单个exe文件
- `--noconsole`: 运行时不显示控制台窗口
- `--name`: 指定输出文件名

### 步骤3：获取EXE

打包完成后，exe文件在 `dist/Windows演示.exe`

## ✨ 功能特点

| 功能 | 描述 |
|------|------|
| 🖥️ 模拟桌面 | Windows 10风格桌面背景、图标、任务栏 |
| 📝 Word窗口 | 完整的Word界面模拟（标题栏、功能区、状态栏） |
| ⌨️ 自动打字 | 带闪烁光标的打字效果，速度随机模拟真实输入 |
| 🕐 实时时钟 | 任务栏显示实时时间 |
| 📊 字数统计 | 状态栏实时显示打字字数 |

## 📝 自定义内容

如果你想修改打字内容，编辑 `fake_desktop_launcher.py` 文件中的 `documentText` 变量：

```python
const documentText = `你的自定义内容...`;
```

## ⚠️ 注意事项

- 这是一个演示/娱乐程序，不是真实的Windows系统
- 建议使用Chrome/Edge等现代浏览器获得最佳效果
- 打包后的EXE可能会被杀毒软件误报（PyInstaller常见问题）

## 📂 文件结构

```
.
├── fake_windows_desktop.html    # HTML版本（直接双击运行）
├── fake_desktop_launcher.py     # Python启动器
└── README.md                    # 本说明文件
```

---

**祝使用愉快！** 🎉
