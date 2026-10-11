# WiFi 优化提速工具箱 · WiFi Optimizer Toolbox

**[English](README_EN.md) | 中文**

![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6.svg)
![Language](https://img.shields.io/badge/Language-Batch-4EAA25.svg)
![Encoding](https://img.shields.io/badge/Encoding-UTF--8-brightgreen.svg)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-orange.svg)

一个纯 `.bat` 实现的 Windows 命令行 WiFi 工具箱：**网络诊断 · 信道分析 · 延迟测试 · 一键优化 · HTTPS 测速 · 断点续传下载 · CLI 小游戏**。双击即用，无需安装任何依赖，内置中英双语界面。

![WiFi 优化提速工具箱 Banner](docs/banner.jpg)

## 🎬 宣传短片

<video src="https://aka.doubaocdn.com/s/ulm59gOLmt" controls width="640"></video>

## ✨ 特性

- ⚡ **一键优化提速**：清理 DNS 缓存、开启 TCP 自动调优、关闭网络节流，释放被系统限制的带宽
- 🔍 **WiFi 网络体检**：读取信号强度 / 速率 / 信道 / 链路质量，自动评级并给出针对性建议
- 📡 **信道分析**：扫描附近 WiFi 占用情况，教你在 2.4GHz 避开拥堵信道（推荐 1 / 6 / 11）
- ⏱️ **多站点 HTTPS 测速**：Cloudflare + OVH 多源下载测速，一眼区分"宽带本身慢"还是"某个网站 CDN 慢"
- ⬇️ **断点续传下载器**：基于 curl `-C -` 断点续传，下载中断了可以接着下
- 🎮 **CLI 小游戏**：猜数字 / 石头剪刀布 / 掷骰子 / 猜硬币，等测速的时候不无聊
- 🌍 **中英双语**：首次运行自由切换 中文 / English，全界面即时切换
- 📄 **零依赖**：纯 .bat + Windows 自带命令（netsh / ipconfig / ping / curl），不装任何东西

## 🚀 快速开始

1. 下载 [`WiFi优化提速工具箱.bat`](WiFi优化提速工具箱.bat)
2. **双击运行**（Windows 7 / 10 / 11 均可）
3. 首次运行选择语言，然后按菜单数字操作即可

> [!NOTE]
> - 读取 WiFi 信号 / 信道需要开启系统**位置服务**（菜单 5 可一键开启，或手动：设置 → 隐私和安全性 → 位置）
> - 菜单 5「一键优化」需要**管理员权限**，首次会弹出 UAC，点"是"即可
> - 文件为 **UTF-8 编码**（内置 `chcp 65001`），在任何语言版本的 Windows 下菜单显示都正常

## 📸 界面预览

| 主菜单 | HTTPS 多站点测速 |
| --- | --- |
| ![主菜单界面](docs/menu-zh.jpg) | ![HTTPS 测速界面](docs/speedtest-zh.jpg) |

| CLI 小游戏 | 项目艺术海报 |
| --- | --- |
| ![CLI 小游戏界面](docs/game-zh.jpg) | ![Zine 风格艺术海报](docs/zine-poster.jpg) |

## 🧩 功能详解

| 菜单 | 功能 | 说明 |
| --- | --- | --- |
| 1 | WiFi 网络体检 | 读取信号/速率/信道，自动评价并给优化建议 |
| 2 | WiFi 连接详情 | 显示网卡连接信息 + IP 配置 |
| 3 | 附近 WiFi 扫描 + 信道分析 | 看 2.4G 信道拥挤度，指导换不重叠信道 |
| 4 | 网络延迟测试 | Ping 网关 / 外网 / DNS，判断是否卡顿掉包 |
| 5 | 一键优化加速 | 清 DNS 缓存、TCP 自动调优、释放带宽、自动开启位置服务（需管理员） |
| 6 | 优化建议指南 | 路由器摆放、信道选择、5G 优先等建议清单 |
| 7 | HTTPS 链接测速 | Cloudflare 25MB + OVH 10MB / 100MB 多源下载测速 |
| 8 | 断点续传下载器 | curl `-C -` 断点续传下载任意 HTTPS 文件 |
| 9 | CLI 小游戏 | 猜数字 / 石头剪刀布 / 掷骰子 / 猜硬币 |

## 🛠️ 从源码构建

项目核心由 `make_wifi_bat.py` 生成（以 UTF-8 编码 + CRLF 输出双语 bat，保证中文菜单在任何语言 Windows 下正常显示）：

```bat
python make_wifi_bat.py
```

## 📁 目录结构

```
WiFi优化提速工具箱.bat   # 可执行工具箱（双击即用）
make_wifi_bat.py         # bat 生成脚本（源码）
docs/                    # README 配图
LICENSE                  # GPL-3.0 许可证
README.md                # 中文说明
README_EN.md             # English README
```

## 🤝 贡献

欢迎任何形式的贡献：提 Issue 报告问题、提交 PR 改进功能、翻译界面、完善文档。

1. **Fork** 本仓库
2. 创建你的分支：`git checkout -b feature/your-feature`
3. 提交你的修改：`git commit -m "feat: xxx"`
4. 推送并创建 **Pull Request**

## ⭐ 支持

如果这个工具对你有用，欢迎点个 **Star** ⭐，让更多人看到它～

## 📄 许可证

本项目基于 **GNU General Public License v3.0（GPL-3.0）** 发布。
你可以自由使用、修改、分发，但修改后的版本也必须以 GPL-3.0 许可发布，并保留版权声明。
完整条款见 [LICENSE](./LICENSE)。

---

**WiFi Optimizer Toolbox** — Diagnose. Test. Optimize. Boost. 🚀
