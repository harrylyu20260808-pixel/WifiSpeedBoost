# -*- coding: utf-8 -*-
"""生成 WiFi优化提速工具箱.bat (UTF-8 编码, MAS 风格菜单, 中英双语可选)"""

bat = r'''@echo off
chcp 65001 >nul
rem ==========================================================
rem  WiFi 优化提速工具箱 / WiFi Optimizer Toolbox v1.0
rem  Copyright (C) 2026  Harry Lyu
rem
rem  This program is free software: you can redistribute it
rem  and/or modify it under the terms of the GNU General Public
rem  License as published by the Free Software Foundation,
rem  either version 3 of the License, or (at your option) any
rem  later version.
rem
rem  This program is distributed in the hope that it will be
rem  useful, but WITHOUT ANY WARRANTY; without even the implied
rem  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
rem  PURPOSE.  See the GNU General Public License for more
rem  details.
rem
rem  You should have received a copy of the GNU General Public
rem  License along with this program.  If not, see
rem  <https://www.gnu.org/licenses/>.
rem ==========================================================
title WiFi Optimizer Toolbox v1.0
setlocal enabledelayedexpansion
color 0B
cd /d "%~dp0"

:language
cls
echo.
echo  ==================================================
echo     WiFi Optimizer Toolbox  /  WiFi 优化提速工具箱
echo  ==================================================
echo.
echo     1. 中文
echo     2. English
echo.
set /p lang=请选择语言 / Select language: 
if "%lang%"=="2" goto set_en
if "%lang%"=="1" goto set_zh
goto language

:set_zh
set L_TITLE=WiFi 优化提速工具箱 v1.0
set L_SUB=诊断WiFi问题、清理网络缓存、优化提速
set L_M1=[1] WiFi 网络体检（信号/速率诊断+建议）
set L_M2=[2] 查看当前 WiFi 连接详情
set L_M3=[3] 附近 WiFi 扫描 + 信道分析
set L_M4=[4] 网络延迟测试（Ping）
set L_M5=[5] 一键优化加速（清理缓存/TCP优化）[需管理员]
set L_M6=[6] WiFi 优化建议指南
set L_M7=[7] HTTPS 链接测速（多站点）
set L_M8=[8] 断点续传下载器
set L_M9=[9] CLI 小游戏
set L_M0=[0] 退出
set L_CHOOSE=请输入选项后按回车:
set L_BACK=按回车返回主菜单...
set L_HC=WiFi 网络体检 / Health Check
set L_HD=当前 WiFi 连接详情 / WiFi Details
set L_HCH=附近 WiFi 扫描 + 信道分析 / Channel Analysis
set L_HP=网络延迟测试 / Latency Test
set L_HO=一键优化加速 / Optimize
set L_HG=WiFi 优化建议指南 / Optimization Guide
set L_HH=HTTPS 链接测速 / HTTPS Speed Test
set L_HR=断点续传下载器 / Resume Download
set L_HGAME=CLI 小游戏大厅 / Mini Game Hall
set L_G1=[1] 猜数字 (1-100)
set L_G2=[2] 石头剪刀布
set L_G3=[3] 掷骰子
set L_G4=[4] 猜硬币
set L_G0=[0] 返回主菜单
set L_GCHOOSE=请选择游戏:
set G1_TITLE=[猜数字] 我想了一个 1-100 的数, 你来猜
set G1_PROMPT=你猜的数字:
set G1_LOW=太小了, 继续
set G1_HIGH=太大了, 继续
set G1_AGAIN=再玩一次? (y/n):
set G2_TITLE=[石头剪刀布] 电脑已经出好了
set G2_RULE=1=石头 2=剪刀 3=布
set G2_PROMPT=你出拳 (1石头 2剪刀 3布):
set G2_INVALID=输入无效
set G2_AGAIN=再来一局? (y/n):
set G2_W0=石头
set G2_W1=剪刀
set G2_W2=布
set G2_YOU=你出:
set G2_CPU=电脑出:
set G2_DRAW=平局!
set G2_WIN=你赢了!
set G2_LOSE=电脑赢了!
set G3_TITLE=[掷骰子]
set G3_D1=第一颗
set G3_D2=第二颗
set G3_TOTAL=点数合计
set G3_HIGH=不小哦, 手气不错!
set G3_LOW=嗯... 下次再试
set G3_AGAIN=再掷一次? (y/n):
set G4_TITLE=[猜硬币] 我抛了一枚硬币
set G4_PROMPT=猜正面还是反面 (1=正 2=反):
set G4_RIGHT=猜中了!
set G4_WRONG=猜错了, 其实硬币是
set G4_AGAIN=再猜一次? (y/n):
goto menu

:set_en
set L_TITLE=WiFi Optimizer Toolbox v1.0
set L_SUB=Diagnose WiFi issues, clean cache, boost speed
set L_M1=[1] WiFi Health Check (signal/rate + advice)
set L_M2=[2] View current WiFi details
set L_M3=[3] Scan nearby WiFi + channel analysis
set L_M4=[4] Network latency test (Ping)
set L_M5=[5] One-click optimize (cache/TCP) [Admin]
set L_M6=[6] WiFi optimization guide
set L_M7=[7] HTTPS speed test (multi-site)
set L_M8=[8] Resume downloader
set L_M9=[9] CLI mini games
set L_M0=[0] Exit
set L_CHOOSE=Enter option and press Enter:
set L_BACK=Press Enter to return to main menu...
set L_HC=WiFi Health Check
set L_HD=Current WiFi Details
set L_HCH=Nearby WiFi Scan + Channel Analysis
set L_HP=Network Latency Test
set L_HO=One-click Optimize
set L_HG=WiFi Optimization Guide
set L_HH=HTTPS Speed Test
set L_HR=Resume Downloader
set L_HGAME=CLI Mini Game Hall
set L_G1=[1] Guess Number (1-100)
set L_G2=[2] Rock-Paper-Scissors
set L_G3=[3] Roll Dice
set L_G4=[4] Coin Flip
set L_G0=[0] Back
set L_GCHOOSE=Choose game:
set G1_TITLE=[Guess Number] I picked 1-100
set G1_PROMPT=Your guess:
set G1_LOW=Too low, try again
set G1_HIGH=Too high, try again
set G1_AGAIN=Play again? (y/n):
set G2_TITLE=[Rock-Paper-Scissors] Computer chose already
set G2_RULE=1=Rock 2=Scissors 3=Paper
set G2_PROMPT=Your move (1Rock 2Scissors 3Paper):
set G2_INVALID=Invalid
set G2_AGAIN=Again? (y/n):
set G2_W0=Rock
set G2_W1=Scissors
set G2_W2=Paper
set G2_YOU=You:
set G2_CPU=CPU:
set G2_DRAW=Draw!
set G2_WIN=You win!
set G2_LOSE=CPU wins
set G3_TITLE=[Roll Dice]
set G3_D1=Die1
set G3_D2=Die2
set G3_TOTAL=Total
set G3_HIGH=Nice roll!
set G3_LOW=Try again...
set G3_AGAIN=Roll again? (y/n):
set G4_TITLE=[Coin Flip] I flipped a coin
set G4_PROMPT=Heads or tails (1=H 2=T):
set G4_RIGHT=Correct!
set G4_WRONG=Wrong, it was
set G4_AGAIN=Again? (y/n):
goto menu

:menu
cls
echo.
echo  ==================================================
echo        !L_TITLE!
echo       !L_SUB!
echo  ==================================================
echo.
echo     !L_M1!
echo     !L_M2!
echo     !L_M3!
echo     !L_M4!
echo     !L_M5!
echo     !L_M6!
echo     !L_M7!
echo     !L_M8!
echo     !L_M9!
echo     !L_M0!
echo.
set /p opt=!L_CHOOSE!

if "%opt%"=="1" goto check
if "%opt%"=="2" goto detail
if "%opt%"=="3" goto channel
if "%opt%"=="4" goto ping
if "%opt%"=="5" goto optimize
if "%opt%"=="6" goto guide
if "%opt%"=="7" goto https
if "%opt%"=="8" goto resume
if "%opt%"=="9" goto games
if "%opt%"=="0" exit /b
goto menu

:check
cls
echo.
echo  [!L_HC!]
echo  ------------------------------------------
netsh wlan show interfaces > "%temp%\wifi.txt" 2>&1
findstr /c:"Signal" /c:"信号" "%temp%\wifi.txt" >nul 2>&1
if errorlevel 1 (
    echo.
    if "!lang!"=="2" (
        echo   [!] Cannot read WiFi signal info.
        echo       Enable Windows Location service, then rerun:
        echo        Settings - Privacy ^& security - Location - ON
        echo       Or use menu [5] to enable it automatically.
    ) else (
        echo   [!] 无法读取WiFi信号信息。
        echo       请先开启 Windows 的"位置服务"再运行：
        echo        设置 → 隐私和安全性 → 位置 → 打开
        echo       或在本工具菜单 [5] 一键开启。
    )
    echo.
    echo  ------------------------------------------
    if "!lang!"=="2" (echo  Network config overview:) else (echo  网络配置概览:)
    ipconfig | findstr /c:"IPv4" /c:"IPv4 地址" /c:"IP 地址" /c:"默认网关" /c:"Default Gateway"
    goto back
)
for /f "tokens=2 delims=:" %%a in ('type "%temp%\wifi.txt" ^| findstr /c:"信号"') do set "SIGNAL=%%a"
for /f "tokens=2 delims=:" %%a in ('type "%temp%\wifi.txt" ^| findstr /c:"信道"') do set "CH=%%a"
for /f "tokens=2 delims=:" %%a in ('type "%temp%\wifi.txt" ^| findstr /c:"接收速率"') do set "RATE=%%a"
for /f "tokens=2 delims=:" %%a in ('type "%temp%\wifi.txt" ^| findstr /c:"链路质量"') do set "LINK=%%a"
for /f "tokens=2 delims=:" %%a in ('type "%temp%\wifi.txt" ^| findstr /c:"SSID"') do set "SSID=%%a"
set "SIGNAL=!SIGNAL: =!" & set "SIGNAL=!SIGNAL:%%=!"
set "LINK=!LINK: =!" & set "LINK=!LINK:%%=!"
echo  ------------------------------------------
if "!lang!"=="2" (
    echo  SSID      : !SSID!
    echo  Signal    : !SIGNAL!%%
    echo  Link qual : !LINK!%%
    echo  Channel   : !CH!
    echo  Rx rate   : !RATE!
    echo  ------------------------------------------
    echo.
    echo  [Signal rating]
    if !SIGNAL! GEQ 70 (
        echo    Signal excellent: !SIGNAL!%% - WiFi is healthy.
    ) else if !SIGNAL! GEQ 40 (
        echo    Signal fair: !SIGNAL!%% - may slow down.
        echo    Tip: move closer to router, or use menu [5].
    ) else (
        echo    Signal weak: !SIGNAL!%% - lag/drops likely.
        echo    Tip: move closer, avoid walls, or change channel.
    )
    echo.
    echo  Hint: use channel 1/6/11 on 2.4GHz. See menu [3].
) else (
    echo  WiFi名称 : !SSID!
    echo  信号强度 : !SIGNAL!%%
    echo  链路质量 : !LINK!%%
    echo  当前信道 : !CH!
    echo  接收速率 : !RATE!
    echo  ------------------------------------------
    echo.
    echo  [信号评价]
    if !SIGNAL! GEQ 70 (
        echo   信号很好: !SIGNAL!%%，WiFi 连接健康。
    ) else if !SIGNAL! GEQ 40 (
        echo   信号一般: !SIGNAL!%%，可能掉速。
        echo   建议: 靠近路由器、避开遮挡，或在菜单[5]优化。
    ) else (
        echo   信号较弱: !SIGNAL!%%，容易卡顿掉线。
        echo   建议: 靠近路由器、减少遮挡，或换信道。
    )
    echo.
    echo  提示: 2.4GHz 建议用信道 1/6/11。可在菜单[3]查看拥堵。
)
goto back

:detail
cls
echo.
echo  [!L_HD!]
echo  ==================================================
netsh wlan show interfaces
echo.
echo  ==================================================
ipconfig
goto back

:channel
cls
echo.
echo  [!L_HCH!]
echo  ==================================================
netsh wlan show networks mode=bssid
echo.
echo  ------------------------------------------
if "!lang!"=="2" (
    echo  * 2.4GHz: only use channels 1 / 6 / 11 - no overlap
    echo  * Check which of these is most crowded above
    echo  * Pick the emptiest channel in your router settings
    echo  * Prefer 5GHz if devices support it - less crowded, faster
) else (
    echo  * 2.4GHz 只推荐信道 1 / 6 / 11（三信道互不重叠）
    echo  * 查看上面扫描结果中这些信道上拥挤的网络数量
    echo  * 选最空的那个信道到路由器后台切换
    echo  * 设备支持5GHz时，优先用5GHz - 信道更空、更快
)
goto back

:ping
cls
echo.
echo  [!L_HP!]
echo  ==================================================
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"默认网关" /c:"Default Gateway"') do set "GW=%%a"
set "GW=!GW: =!"
if "!GW!"=="" set "GW=192.168.0.1"
if "!lang!"=="2" (echo  Ping gateway  !GW!  - LAN latency) else (echo  测试网关  !GW!  （局域网延迟）)
ping -n 4 !GW!
echo.
if "!lang!"=="2" (echo  Ping internet 223.5.5.5) else (echo  测试外网 223.5.5.5  （互联网延迟）)
ping -n 4 223.5.5.5
echo.
if "!lang!"=="2" (echo  Ping DNS 114.114.114.114) else (echo  测试 DNS 114.114.114.114)
ping -n 4 114.114.114.114
echo  ==================================================
if "!lang!"=="2" (
    echo  Normal: LAN 1-5ms, Internet 10-60ms
    echo  High ping or loss = unstable network, see menu [6]
) else (
    echo  * 局域网 ping 1-5ms 正常; 高于20ms 检查网卡/驱动
    echo  * 外网   ping 10-60ms 正常; 高于100ms 或丢包=网络差
    echo  * 有"请求超时/丢失"说明不稳定, 见菜单[6]
)
goto back

:optimize
cls
echo.
echo  [!L_HO!]
echo  ==================================================
net session >nul 2>&1
if errorlevel 1 (
    if "!lang!"=="2" (echo  Not admin, relaunching as admin...) else (echo  当前不是管理员权限，正在重新以管理员运行...)
    echo  UAC...
    powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /b
)
if "!lang!"=="2" (echo  [1/4] Flush DNS cache...) else (echo  [1/4] 清理 DNS 解析缓存...)
ipconfig /flushdns >nul 2>&1 && echo       OK
if "!lang!"=="2" (echo  [2/4] Enable TCP auto-tuning...) else (echo  [2/4] 启用 TCP 自动调优...)
netsh int tcp set global autotuninglevel=normal >nul 2>&1 && echo       OK
if "!lang!"=="2" (echo  [3/4] Disable network throttling...) else (echo  [3/4] 关闭 Windows 网络节流...)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v PschedDisable /t REG_DWORD /d 1 /f >nul 2>&1 && echo       OK
if "!lang!"=="2" (echo  [4/4] Enable Location service...) else (echo  [4/4] 开启位置服务...)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" /v Value /t REG_SZ /d Allow /f >nul 2>&1 && echo       OK
echo.
echo  ==================================================
if "!lang!"=="2" (
    echo   Done! Restart network or PC to apply fully.
    echo   Advanced - optional: netsh winsock reset ^+ reboot
) else (
    echo   优化完成！建议重启一次网络或电脑让部分设置生效。
    echo   高级操作 - 可选: netsh winsock reset  然后重启电脑
)
goto back

:guide
cls
echo.
echo  [!L_HG!]
echo  ==================================================
if "!lang!"=="2" (
    echo  1. Placement: router high ^& central, away from
    echo     microwave/fridge/aquarium interference
    echo  2. Channels: 2.4GHz use 1/6/11; 5GHz less crowded
    echo  3. Band: enable dual-band or connect 5GHz when close
    echo  4. Security: WPA2/WPA3 to avoid freeloaders
    echo  5. Driver: update NIC driver; high-performance power
    echo  6. Background: stop heavy uploads/downloads
    echo  7. Hardware: upgrade old/100M router if capped
) else (
    echo  1. 摆放位置: 路由器放高处、房屋中央
    echo     远离微波炉/冰箱/鱼缸等干扰源
    echo  2. 信道选择: 2.4GHz 用 1/6/11; 5GHz 信道更空更快
    echo  3. 频段优先: 开"双频合一"或短距离连5GHz
    echo  4. 加密: 用 WPA2/WPA3, 避免被蹭网拖慢
    echo  5. 驱动: 更新网卡驱动; 电源设为"高性能"
    echo  6. 后台: 关闭云同步/下载器等大流量
    echo  7. 硬件: 老旧/百兆路由会封顶网速, 升级千兆
)
echo  ==================================================
if "!lang!"=="2" (echo  Suggested: [1]Health [4]Ping [3]Channel [5]Optimize) else (echo  建议按: [1]体检 → [4]测延迟 → [3]看信道 → [5]优化)
goto back

:https
cls
echo.
echo  [!L_HH!]
echo  ==================================================
if "!lang!"=="2" (echo  Testing HTTPS download speed from multiple sites...) else (echo  正在从多个 HTTPS 站点下载测试文件测速...)
echo  bytes/s -> /1000000 = MB/s, /125000 = Mbps
echo.
echo  --- 1: Cloudflare CDN (25MB) ---
curl --max-time 30 -s -o NUL -L -w "    speed: %%{speed_download} B/s  time: %%{time_total} s\n" "https://speed.cloudflare.com/__down?bytes=25000000"
echo.
echo  --- 2: OVH (10MB) ---
curl --max-time 30 -s -o NUL -L -w "    speed: %%{speed_download} B/s  time: %%{time_total} s\n" "https://proof.ovh.net/files/10Mb.dat"
echo.
echo  --- 3: OVH (100MB) ---
curl --max-time 30 -s -o NUL -L -w "    speed: %%{speed_download} B/s  time: %%{time_total} s\n" "https://proof.ovh.net/files/100Mb.dat"
echo  ==================================================
if "!lang!"=="2" (
    echo  * All slow = your network problem
    echo  * Only one slow = that site's CDN, not your speed
) else (
    echo  * 所有源都慢  = 你宽带/网络本身的问题
    echo  * 仅个别源慢  = 那个网站CDN的问题, 与你网速无关
)
goto back

:resume
cls
echo.
echo  [!L_HR!]
echo  ==================================================
if "!lang!"=="2" (set /p durl=Download URL: ) else (set /p durl=请输入下载链接(URL): )
if "!durl!"=="" (if "!lang!"=="2" (echo  No URL, back) else (echo  未输入链接, 返回菜单) & goto back)
if "!lang!"=="2" (set /p fname=Save as (blank=download.bin): ) else (set /p fname=保存为(文件名, 留空默认 download.bin): )
if "!fname!"=="" set fname=download.bin
echo.
if "!lang!"=="2" (echo  Downloading... Ctrl+C to pause, rerun same URL+name to resume) else (echo  开始下载... （支持断点续传: 中断后再运行本项输入相同链接和文件名可续传）)
echo  ==================================================
curl -L -C - -o "!fname!" "!durl!" -w "    done! avg speed: %%{speed_download} B/s  time: %%{time_total} s\n"
echo.
if "!lang!"=="2" (echo  Saved: !fname!  - rerun same URL+name to resume) else (echo  文件已保存: !fname!  - 再运行本项输入相同链接+文件名即可续传)
goto back

:games
cls
echo.
echo  [!L_HGAME!]
echo  ==================================================
echo     !L_G1!
echo     !L_G2!
echo     !L_G3!
echo     !L_G4!
echo     !L_G0!
echo.
set /p gopt=!L_GCHOOSE!
if "%gopt%"=="1" goto g_guess
if "%gopt%"=="2" goto g_rps
if "%gopt%"=="3" goto g_dice
if "%gopt%"=="4" goto g_coin
if "%gopt%"=="0" goto menu
goto games

:g_guess
cls
echo.
echo  [!G1_TITLE!]
set /a target=!random! %% 100 + 1
set tries=0
:g_guess_loop
set /p gnum=!G1_PROMPT! 
set /a tries+=1
if !gnum! LSS !target! (echo    !G1_LOW!) else if !gnum! GTR !target! (echo    !G1_HIGH!) else (
    echo.
    echo    Bingo! It was !target! in !tries! tries!  /  猜中了! 用了 !tries! 次
    set /p ag=!G1_AGAIN! 
    if /i "!ag!"=="y" goto g_guess
    goto games
)
goto g_guess_loop

:g_rps
cls
echo.
echo  [!G2_TITLE!]
echo   !G2_RULE!
set /a cpu=!random! %% 3 + 1
set /p hand=!G2_PROMPT! 
if "!hand!"=="1" (set my=!G2_W0!) else if "!hand!"=="2" (set my=!G2_W1!) else if "!hand!"=="3" (set my=!G2_W2!) else (echo   !G2_INVALID! & goto g_rps)
if !cpu!==1 (set cp=!G2_W0!) else if !cpu!==2 (set cp=!G2_W1!) else (set cp=!G2_W2!)
echo.
echo    !G2_YOU! !my!     !G2_CPU! !cp!
if !hand!==!cpu! (echo    !G2_DRAW!)
if !hand!==1 if !cpu!==2 (echo    !G2_WIN!)
if !hand!==2 if !cpu!==3 (echo    !G2_WIN!)
if !hand!==3 if !cpu!==1 (echo    !G2_WIN!)
if !hand!==1 if !cpu!==3 (echo    !G2_LOSE!)
if !hand!==2 if !cpu!==1 (echo    !G2_LOSE!)
if !hand!==3 if !cpu!==2 (echo    !G2_LOSE!)
set /p ar=!G2_AGAIN! 
if /i "!ar!"=="y" goto g_rps
goto games

:g_dice
cls
echo.
echo  [!G3_TITLE!]
set /a d1=!random! %% 6 + 1
set /a d2=!random! %% 6 + 1
set /a sum=!d1!+!d2!
echo.
echo    !G3_D1!: !d1!    !G3_D2!: !d2!
echo    !G3_TOTAL! = !sum!
if !sum! GEQ 7 (echo    !G3_HIGH!) else (echo    !G3_LOW!)
set /p ad=!G3_AGAIN! 
if /i "!ad!"=="y" goto g_dice
goto games

:g_coin
cls
echo.
echo  [!G4_TITLE!]
set /a c=!random! %% 2 + 1
set /p cc=!G4_PROMPT! 
if !cc!==!c! (echo    !G4_RIGHT!  !c!) else (echo    !G4_WRONG!  !c!)
set /p ac=!G4_AGAIN! 
if /i "!ac!"=="y" goto g_coin
goto games

:back
echo.
set /p x=!L_BACK!
goto menu
'''

import os
base = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(base, 'WiFi优化提速工具箱.bat')
with open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(bat)
print('已生成双语 bat (UTF-8):', p)
print('大小:', len(bat.encode('utf-8')), 'bytes')
