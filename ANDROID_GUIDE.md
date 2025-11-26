# 安卓手机运行指南

## 📱 可行性分析

**结论：可以在安卓手机上运行！**

本项目 `XMU-Rollcall-Bot v3` 是一个纯 Python 项目，依赖项包括：
- `pycryptodome` - 加密库
- `requests` - HTTP 请求库
- `aiohttp` - 异步 HTTP 请求库
- `xmulogin` - 厦门大学登录库

这些依赖都是纯 Python 或有安卓兼容版本的库，因此可以在安卓设备上运行。

---

## 🚀 运行方案

### 方案一：Termux（推荐）⭐

[Termux](https://termux.dev/) 是一个强大的安卓终端模拟器，可以运行完整的 Linux 环境和 Python。

#### 安装步骤

1. **安装 Termux**
   - 从 [F-Droid](https://f-droid.org/packages/com.termux/) 下载安装（推荐）
   - 或从 [GitHub Releases](https://github.com/termux/termux-app/releases) 下载
   - ⚠️ **不推荐** 从 Google Play 安装，版本可能过旧

2. **更新 Termux 包管理器**
   ```bash
   pkg update && pkg upgrade
   ```

3. **安装 Python**
   ```bash
   pkg install python
   ```

4. **安装 Git（可选，用于克隆仓库）**
   ```bash
   pkg install git
   ```

5. **克隆项目或下载源码**
   ```bash
   git clone https://github.com/KrsMt-0113/XMU-Rollcall-Bot.git
   cd "XMU-Rollcall-Bot/XMU-Rollcall-Bot-CLI(v3)"
   ```
   
   或者手动下载源码并使用 Termux 的文件访问功能。

6. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

7. **配置信息**
   
   编辑 `info.txt` 文件，按以下格式填写（每行一个信息）：
   ```
   你的学号
   你的密码
   纬度（如 24.4378）
   经度（如 118.0965）
   ```
   
   可以使用 `nano` 或 `vim` 编辑：
   ```bash
   nano info.txt
   ```

8. **运行程序**
   ```bash
   python main.py
   ```

#### Termux 使用技巧

- **保持后台运行**：使用 `termux-wake-lock` 防止系统休眠杀死进程
  ```bash
  pkg install termux-api
  termux-wake-lock
  python main.py
  ```

- **访问手机存储**：运行 `termux-setup-storage` 获取存储权限

- **复制粘贴**：长按屏幕调出菜单

---

### 方案二：Pydroid 3

[Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) 是一个安卓上的 Python IDE，使用更简单但功能相对有限。

#### 安装步骤

1. **安装 Pydroid 3**
   - 从 Google Play 商店搜索 "Pydroid 3" 并安装

2. **安装依赖**
   - 打开 Pydroid 3
   - 点击菜单 → Pip → 输入包名安装：
     - `pycryptodome`
     - `requests`
     - `aiohttp`
     - `xmulogin`

3. **导入项目文件**
   - 下载 `XMU-Rollcall-Bot-CLI(v3)` 目录下的所有文件
   - 通过 Pydroid 3 打开 `main.py`

4. **配置 `info.txt`**
   - 使用文本编辑器修改 `info.txt`

5. **运行**
   - 在 Pydroid 3 中点击运行按钮

#### 注意事项

- Pydroid 3 的免费版可能有广告
- 部分功能需要付费解锁
- 后台运行可能受限

---

### 方案三：QPython

[QPython](https://www.qpython.com/) 是另一个安卓 Python 环境。

#### 安装步骤

1. 从应用商店安装 QPython 或 QPython 3L
2. 使用 QPYPI 安装依赖
3. 导入并运行项目

---

## 📍 获取经纬度

在手机上获取当前位置的经纬度：

### 方法一：手机自带地图应用
1. 打开地图应用（如高德地图、百度地图）
2. 长按目标位置
3. 查看显示的坐标信息

### 方法二：使用坐标拾取工具
- [高德坐标拾取](https://lbs.amap.com/tools/picker)
- [百度坐标拾取](https://api.map.baidu.com/lbsapi/getpoint/index.html)

### 方法三：Termux 获取 GPS
```bash
pkg install termux-api
termux-location
```

> ⚠️ **注意**：请确保使用 **WGS84** 坐标系（GPS 原始坐标），不要使用 GCJ-02 或 BD-09 坐标系。

---

## ⚠️ 注意事项

1. **网络环境**
   - 建议连接校园网或使用校园 VPN
   - 部分功能可能需要特定网络环境

2. **电池优化**
   - 建议将 Termux/Pydroid 加入电池优化白名单
   - 否则系统可能会在后台杀死应用

3. **登录安全**
   - 如遇登录失败，**不要** 频繁重试
   - 频繁失败可能导致账号临时冻结
   - 详见项目 [README.md](README.md) 中的警告部分

4. **持续运行**
   - 程序需要持续运行才能监控签到
   - 建议使用 Termux + `termux-wake-lock`
   - 或配合 Tasker 等自动化工具定时启动

---

## 🔧 常见问题

### Q: 安装依赖时报错怎么办？

**A:** 尝试以下方法：

```bash
# 更新 pip
pip install --upgrade pip

# 安装编译工具（Termux）
pkg install python-dev clang

# 单独安装有问题的包
pip install pycryptodome --no-cache-dir
```

### Q: 提示 `xmulogin` 安装失败？

**A:** `xmulogin` 是作者开发的包，确保网络正常后重试：

```bash
pip install xmulogin --no-cache-dir
```

### Q: 程序运行一段时间后自动退出？

**A:** 这通常是安卓系统的后台管理导致的。解决方法：

1. 将应用加入电池优化白名单
2. 在 Termux 中使用 `termux-wake-lock`
3. 考虑使用 `nohup` 命令：
   ```bash
   nohup python main.py &
   ```

### Q: 如何让程序开机自启？

**A:** 可以配合 Tasker 或 Termux:Boot 插件实现：

1. 安装 [Termux:Boot](https://f-droid.org/packages/com.termux.boot/)
2. 在 `~/.termux/boot/` 目录创建启动脚本

---

## 📚 相关链接

- [Termux 官网](https://termux.dev/)
- [Termux Wiki](https://wiki.termux.com/)
- [项目主页](https://github.com/KrsMt-0113/XMU-Rollcall-Bot)
- [问题反馈](https://github.com/KrsMt-0113/XMU-Rollcall-Bot/issues)

---

## 🤝 贡献

如果你在安卓上成功运行了本项目，或者发现了其他可行的运行方案，欢迎：

1. 提交 Issue 分享你的经验
2. 提交 Pull Request 完善本文档

感谢你的贡献！
