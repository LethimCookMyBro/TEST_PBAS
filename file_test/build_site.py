import os, json

folder = r"c:\Users\User\Downloads\PBAS\file_test"
img_base = os.path.join(folder, "images")

chapters = [
    ("ch9", "CH9: InterVLAN Routing & L3 Switch", "computer_network_ch9", 13),
    ("ch10", "CH10: Spanning Tree Protocol (STP)", "computer_network_ch10", 48),
    ("ch10new", "CH10 (ACL): Access Control Lists", "computer_network_ch10_new", 55),
    ("ch11", "CH11: EtherChannel", "computer_network_ch11", 24),
    ("ch13", "CH13: IPv6", "computer_network_ch13", 24),
]

labs = [
    ("lab9", "LAB-09: InterVLAN Route", "67160003_Chutiphon Jitrungraungsuk - LAB-09 Intervlan route", 7),
    ("lab10", "LAB-10: ACL + VLAN", "Chutiphon Jitrungraungsuk - LAB_10_new", 8),
    ("lab12", "LAB-12: EtherChannel", "Chutiphon Jitrungraungsuk - LAB_12", 4),
]

# List actual lab image files
for lid, title, img_dir, cnt in labs:
    d = os.path.join(img_base, img_dir)
    if os.path.exists(d):
        print(f"{lid}: {sorted(os.listdir(d))}")

# Build HTML parts
parts = []

# --- HEADER ---
parts.append("""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Computer Network - Exam Summary</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0f0f1a;--sf:#1a1a2e;--sf2:#16213e;--cd:#1e2746;--ac:#00d2ff;--ac2:#7b2ff7;--tx:#e0e0ff;--tx2:#8892b0;--bd:#2d3561;--gn:#00e676;--yw:#ffd740;--rd:#ff5252}
body{font-family:'Noto Sans Thai',sans-serif;background:var(--bg);color:var(--tx);display:flex;min-height:100vh}
.sb{width:300px;background:var(--sf);border-right:1px solid var(--bd);position:fixed;height:100vh;overflow-y:auto;z-index:100;transition:transform .3s}
.sb-h{padding:20px;background:linear-gradient(135deg,var(--ac2),var(--ac));-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center}
.sb-h h1{font-size:1.3em;font-weight:700}.sb-h p{font-size:.85em;-webkit-text-fill-color:var(--tx2)}
.nd{padding:12px 20px 6px;font-size:.75em;font-weight:600;color:var(--ac);text-transform:uppercase;letter-spacing:2px}
.ni{display:flex;align-items:center;gap:10px;padding:12px 20px;color:var(--tx2);text-decoration:none;font-size:.9em;transition:all .2s;border-left:3px solid transparent;cursor:pointer}
.ni:hover,.ni.act{background:rgba(0,210,255,.08);color:var(--ac);border-left-color:var(--ac)}
.mn{margin-left:300px;flex:1;padding:30px;max-width:1200px}
.cs{display:none}.cs.act{display:block}
.cs h2{font-size:1.8em;margin-bottom:24px;background:linear-gradient(90deg,var(--ac),var(--ac2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;padding-bottom:12px;border-bottom:2px solid var(--bd)}
.st{font-size:1.2em;margin:24px 0 16px;color:var(--yw)}
.sc{background:var(--cd);border-radius:12px;padding:20px;margin-bottom:16px;border:1px solid var(--bd);transition:transform .2s}
.sc:hover{transform:translateY(-2px);border-color:var(--ac)}
.sc h3{color:var(--ac);font-size:1.15em;margin-bottom:12px}
.sc h4{color:var(--yw);font-size:1em;margin:14px 0 8px}
.sc p{line-height:1.8;color:var(--tx2)}.sc ul,.sc ol{padding-left:20px;color:var(--tx2);line-height:2}
.sc li{margin-bottom:4px}.sc b{color:var(--tx)}
.sc code{background:rgba(0,210,255,.15);padding:2px 6px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:.85em;color:var(--ac)}
.cb{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:14px 18px;font-family:'JetBrains Mono',monospace;font-size:.85em;line-height:1.8;color:var(--gn);margin:8px 0;overflow-x:auto;white-space:pre-wrap}
.cb .cm{color:#6a737d}.hl{color:var(--yw);font-weight:600}
table{width:100%;border-collapse:collapse;margin:10px 0;font-size:.9em}
th{background:var(--ac2);color:white;padding:10px 14px;text-align:left;font-weight:500}
td{padding:8px 14px;border-bottom:1px solid var(--bd);color:var(--tx2)}
tr:hover td{background:rgba(0,210,255,.05)}
.tm{background:var(--rd);color:white;padding:2px 8px;border-radius:10px;font-size:.8em;font-weight:500}
.sg{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
.sl{background:var(--cd);border-radius:10px;overflow:hidden;border:1px solid var(--bd);transition:all .3s;cursor:pointer}
.sl:hover{border-color:var(--ac);transform:scale(1.02)}
.sl img{width:100%;display:block}
.sn{text-align:center;padding:8px;font-size:.8em;color:var(--tx2);background:var(--sf2)}
.mo{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.92);z-index:1000;justify-content:center;align-items:center;cursor:zoom-out}
.mo.act{display:flex}.mo img{max-width:95vw;max-height:95vh;object-fit:contain;border-radius:8px}
.mb{display:none;position:fixed;top:15px;left:15px;z-index:200;background:var(--ac);color:var(--bg);border:none;padding:10px 14px;border-radius:8px;font-size:1.2em;cursor:pointer}
@media(max-width:768px){.sb{transform:translateX(-100%)}.sb.op{transform:translateX(0)}.mn{margin-left:0;padding:15px;padding-top:60px}.mb{display:block}.sg{grid-template-columns:1fr}}
</style>
</head>
<body>
<button class="mb" onclick="document.querySelector('.sb').classList.toggle('op')">&#9776;</button>
<nav class="sb">
<div class="sb-h"><h1>Computer Network</h1><p>Summary for Exam</p></div>
<div class="nd">Chapters</div>
""")

# Nav items
parts.append('<a class="ni" onclick="go(\'concept\')" style="color:#ff8a00;font-weight:bold;"><span>💡</span>สรุปเปรียบเทียบ (ก่อนสอบ)</a>\n')
parts.append('<a class="ni" onclick="go(\'allcmd\')" style="color:#4CAF50;font-weight:bold;"><span>💻</span>เจาะลึกทุกคำสั่ง CLI (รวม Config + Show)</a>\n')
parts.append('<a class="ni" onclick="go(\'mock\')" style="color:#00e5ff;font-weight:bold;"><span>📝</span>ข้อสอบจำลอง 30 ข้อ</a>\n')
parts.append('<a class="ni" onclick="go(\'leak\')" style="color:var(--yw);font-weight:bold;"><span>&#127919;</span>เก็งข้อสอบ (จากโพย)</a>\n')
for cid, title, _, _ in chapters:
    parts.append(f'<a class="ni" onclick="go(\'{cid}\')"><span>&#128214;</span>{title}</a>\n')
parts.append('<div class="nd">Labs</div>\n')
for lid, title, _, _ in labs:
    parts.append(f'<a class="ni" onclick="go(\'{lid}\')"><span>&#128300;</span>{title}</a>\n')

parts.append('</nav>\n<main class="mn">\n')

# Read summary HTML files
summary_files = {
    "ch9": "summary_ch9.html",
    "ch10": "summary_ch10.html",
    "ch10new": "summary_ch10new.html",
    "ch11": "summary_ch11.html",
    "ch13": "summary_ch13.html",
    "lab9": "summary_lab9.html",
    "lab10": "summary_lab10.html",
    "lab12": "summary_lab12.html",
}

# Write each summary to a temp file, then read back
summaries = {}

summaries["allcmd"] = '<div class="sc" style="border-color:#4CAF50; background:rgba(76, 175, 80, 0.05)"><h3 style="color:#4CAF50; font-size:1.3em;">💻 เจาะลึกทุกคำสั่ง CLI (Configuration & Verification)</h3>'
summaries["allcmd"] += '<p style="margin-bottom:15px; font-size:1.1em; color:var(--tx);">สรุปคำสั่งที่ใช้ในการตั้งค่า (Config) และตรวจสอบ (Show) ของทุกหัวข้อสำคัญในครึ่งเทอมหลัง:</p>'

# 1. Inter-VLAN Routing Commands
summaries["allcmd"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #ff8a00;">'
summaries["allcmd"] += '<h4 style="color:#ff8a00; margin-top:0; font-size:1.1em;">1. คำสั่งสร้าง Inter-VLAN Routing (ROAS & SVI)</h4>'
summaries["allcmd"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b><u>แบบ Router-on-a-stick (ทำบน Router)</u></b><br>'
summaries["allcmd"] += '<code>interface g0/0.10</code> → สร้าง Sub-interface<br>'
summaries["allcmd"] += '<code>encapsulation dot1Q 10</code> → <b>(ห้ามลืม!)</b> กำหนดว่าพอร์ตย่อยนี้ใช้รับข้อมูลของ VLAN 10<br>'
summaries["allcmd"] += '<code>ip address 192.168.10.1 255.255.255.0</code> → จ่าย IP ให้เป็น Gateway ของวง VLAN 10</li>'
summaries["allcmd"] += '<li><b><u>แบบ SVI (ทำบน L3 Switch)</u></b><br>'
summaries["allcmd"] += '<code>ip routing</code> → <b>(ห้ามลืม!)</b> เปิดหัวใจการ Routing ของ Switch ไม่งั้นคุยข้ามวงไม่ได้<br>'
summaries["allcmd"] += '<code>interface vlan 10</code> → สร้าง Interface เสมือนสำหรับ VLAN นั้น<br>'
summaries["allcmd"] += '<code>ip address 192.168.10.1 255.255.255.0</code> → จ่าย IP เพื่อให้เป็น Gateway ของก้อน VLAN 10<br>'
summaries["allcmd"] += '<code>no shutdown</code> → เปิดใช้งานพอร์ตเสมือน</li>'
summaries["allcmd"] += '</ul></div>'

# 2. Spanning Tree (STP) Configs
summaries["allcmd"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #4CAF50;">'
summaries["allcmd"] += '<h4 style="color:#4CAF50; margin-top:0; font-size:1.1em;">2. คำสั่งจัดการ Spanning Tree (STP)</h4>'
summaries["allcmd"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>การบังคับตั้งให้เป็น Root Bridge (บอส):</b><br>'
summaries["allcmd"] += '<code>spanning-tree vlan 1 root primary</code> → คำสั่งลัด ให้สวิตช์ตัวนี้พยายามรับบทเป็นบอสหลักของ VLAN 1 (มันจะไปปรับค่า Priority ให้ต่ำๆ อัตโนมัติ)<br>'
summaries["allcmd"] += '<code>spanning-tree vlan 1 root secondary</code> → ตั้งเป็นบอสสำรอง (รอเสียบแทนถ้าตัวหลักตาย)</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>การแก้ค่า Priority ดิบๆ ด้วยตัวเอง:</b><br>'
summaries["allcmd"] += '<code>spanning-tree vlan 1 priority 4096</code> → ยิ่งค่าน้อยยิ่งมีสิทธิ์เป็น Root Bridge (ต้องเพิ่มลดทีละ 4096 เท่านั้น)</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>คำสั่งตรวจสอบ (Show Command):</b><br>'
summaries["allcmd"] += '<code>show spanning-tree</code> → ดูว่าใครคือ <span style="color:var(--yw);">Root ID</span> (บอส) / <span style="color:var(--yw);">Bridge ID</span> (ตัวเราเอง) / และดูสถานะพอร์ตว่าเป็น <code>FWD</code> (ผ่านได้) หรือ <code>BLK</code> (ถูกบล็อกกัน Loop)</li>'
summaries["allcmd"] += '</ul></div>'

# 3. EtherChannel Configs
summaries["allcmd"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #2196F3;">'
summaries["allcmd"] += '<h4 style="color:#2196F3; margin-top:0; font-size:1.1em;">3. คำสั่งมัดสาย EtherChannel (LACP & PAgP)</h4>'
summaries["allcmd"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>สร้างกลุ่มพอร์ต (เช่น เอาพอร์ต 1-2 มารวมกันรัน PAgP):</b><br>'
summaries["allcmd"] += '<code>interface range f0/1 - 2</code> → ครอบพอร์ตที่จะมัดรวม<br>'
summaries["allcmd"] += '<code>channel-group 1 mode desirable</code> → สั่งมัดเข้ากลุ่มที่ 1 และใช้โหมด desirable (PAgP แบบบุกทักก่อน)</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>โหมดจับคู่ที่ต้องจำ:</b><br>'
summaries["allcmd"] += '- <b>LACP (สากล):</b> <code>active</code> คู่กับ <code>active</code> (หรือ passive)<br>'
summaries["allcmd"] += '- <b>PAgP (Cisco):</b> <code>desirable</code> คู่กับ <code>desirable</code> (หรือ auto)<br>'
summaries["allcmd"] += '- <b>มัดดื้อๆ (ไม่ใช้ Protocol):</b> <code>on</code> คู่กับ <code>on</code> เท่านั้น</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>คำสั่งตรวจสอบ (Show Command):</b><br>'
summaries["allcmd"] += '<code>show etherchannel summary</code> → ดูบรรทัดที่มีพอร์ตกรุ๊ป <code>Po1 (SU)</code> แปลว่า <span style="color:var(--yw);">S = Layer2</span> และ <span style="color:var(--yw);">U = In Use (ใช้งานสำเร็จ)</span> หากขึ้น (SD) คือพัง/ตั้งค่าผิด</li>'
summaries["allcmd"] += '</ul></div>'

# 4. Access Control List (ACL) Configs
summaries["allcmd"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #f44336;">'
summaries["allcmd"] += '<h4 style="color:#f44336; margin-top:0; font-size:1.1em;">4. คำสั่งตั้งกฎกรองข้อมูล ACL</h4>'
summaries["allcmd"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>Standard ACL (บล็อกแค่ IP ต้นทาง / ใช้เลข 1-99):</b><br>'
summaries["allcmd"] += '<code>access-list 10 deny 192.168.10.5 0.0.0.0</code> → บล็อกไม่ให้เครื่อง .5 นี้ผ่าน (Host เดียวใช้หน้ากาก 0.0.0.0)<br>'
summaries["allcmd"] += '<code>access-list 10 permit 192.168.10.0 0.0.0.255</code> → อนุญาตให้ทั้งวง .10.x นี้ผ่านได้<br>'
summaries["allcmd"] += '<code>access-list 10 permit any</code> → <b>(ห้ามลืม!)</b> อนุญาตคนที่เหลือทั้งหมดให้ผ่าน (เพื่อลบล้าง Implicit Deny)</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>Extended ACL (ล็อกเป้าหมายและชนิดพอร์ตได้ / ใช้เลข 100-199):</b><br>'
summaries["allcmd"] += '<code>access-list 100 deny tcp 192.168.10.0 0.0.0.255 host 10.10.1.50 eq 80</code> → สั่งแบน (deny) วง 10 ห้ามคุย tcp ผ่านพอร์ต 80 (เว็บ HTTP) ไปที่เซิร์ฟเวอร์ไอพี .50</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>การนำกฎไปแขวนที่ประตู (Interface):</b><br>'
summaries["allcmd"] += '<code>interface g0/0</code> → เข้าไปที่พอร์ตทางออกหรือทางเข้า<br>'
summaries["allcmd"] += '<code>ip access-group 10 out</code> → เอากฎหมายเลข 10 ไปดักตรวจ<span style="color:var(--yw);">ขาออก (out)</span> หรือ <span style="color:var(--yw);">ขาเข้า (in)</span></li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>คำสั่งตรวจสอบ (Show Command):</b><br>'
summaries["allcmd"] += '<code>show access-lists</code> → ตรวจดูว่ามีใครเข้าข่ายบ้าง (ดูตัวเลขหลังคำว่า <code>matches</code>) และเช็คว่าลำดับข้อ (Sequence Number) เรียงถูกต้องไหม (คำสั่ง Deny ควรอยู่บนๆ เสมอ)</li>'
summaries["allcmd"] += '</ul></div>'

# 5. Routing Tools (Static Route)
summaries["allcmd"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:0; border-left:4px solid #9c27b0;">'
summaries["allcmd"] += '<h4 style="color:#9c27b0; margin-top:0; font-size:1.1em;">5. คำสั่ง Routing พื้นฐาน</h4>'
summaries["allcmd"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>การชี้เป้า Static Route เบสิค:</b><br>'
summaries["allcmd"] += '<code>ip route [เครือข่ายปลายทาง] [Subnet Mask] [IP ด่านหน้าของฝั่งตรงข้าม (Next-Hop)]</code><br>'
summaries["allcmd"] += 'เช่น <code>ip route 192.168.50.0 255.255.255.0 10.0.0.2</code></li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>Default Route (ทางออกสุดท้าย):</b><br>'
summaries["allcmd"] += '<code>ip route 0.0.0.0 0.0.0.0 10.0.0.2</code> → ส่งข้อมูลอะไรก็ตามที่ไม่รู้จักในตาราง ไปที่ทางออก 10.0.0.2 ทั้งหมด</li>'
summaries["allcmd"] += '<li style="margin-bottom:8px;"><b>คำสั่งตรวจสอบ (Show Command):</b><br>'
summaries["allcmd"] += '<code>show ip route</code> → ดูแผนที่เข็มทิศของ Router <br>มองหาตัว <code>C</code> = วงตรงข้ามที่เสียบสายตรงไว้ <br>ตัว <code>S</code> = วง Static ที่แอดมินใช้คำสั่ง ip route มาร์คไว้ให้ <br>ถ้าขึ้น <code>Gateway of last resort</code> แปลว่ามีการตั้งค่า Default Route เตะส่งไว้แล้ว</li>'
summaries["allcmd"] += '</ul></div>'

summaries["allcmd"] += '</div>'

summaries["concept"] = '<div class="sc" style="border-color:#ff8a00; background:rgba(255, 138, 0, 0.05)"><h3 style="color:#ff8a00; font-size:1.3em;">💡 สรุปเปรียบเทียบ (7 จุดสำคัญที่ต้องแยกให้ออก)</h3>'

# 1. ISP vs IANA
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #ff8a00;">'
summaries["concept"] += '<h4 style="color:#ff8a00; margin-top:0; font-size:1.1em;">1. ใครเป็นคนจ่าย IP ให้เน็ตบ้าน?</h4>'
summaries["concept"] += '<p style="color:var(--tx); margin-bottom:5px;"><b>คำตอบ: <span style="color:var(--yw);">ISP (Internet Service Provider)</span></b> หรือผู้ให้บริการอินเทอร์เน็ต เช่น AIS, True, Dtac</p>'
summaries["concept"] += '<p style="color:#ff4444; font-size:0.9em; margin-bottom:0;"><b>⚠️ ข้อควรระวัง:</b> อย่าสับสนกับ <b>IANA</b> (องค์กรที่จัดสรรหมายเลข IP ระดับโลก ไม่ได้แจก IP ตรงให้ผู้ใช้บ้านๆ)</p>'
summaries["concept"] += '</div>'

# 2. Hub vs Switch
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #00e5ff;">'
summaries["concept"] += '<h4 style="color:#00e5ff; margin-top:0; font-size:1.1em;">2. ความแตกต่างระหว่าง Hub กับ Switch</h4>'
summaries["concept"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["concept"] += '<li style="margin-bottom:5px;"><b>Hub (Layer 1):</b> ทำงานแบบ <b>Broadcast</b> คือได้รับข้อมูลมา จะส่งกระจายออกไปทุกพอร์ตพร้อมกัน ทำให้เกิดการชนกันของข้อมูล (Collision) ได้ง่าย</li>'
summaries["concept"] += '<li><b>Switch (Layer 2):</b> ฉลาดกว่า Hub เพราะจะจำ <b>MAC Address</b> ของอุปกรณ์แต่ละเครื่อง และส่งข้อมูลตรงไปยังพอร์ตปลายทางที่ถูกต้องเท่านั้น ทำให้ข้อมูลไม่ชนกันและเครือข่ายเร็วกว่า</li>'
summaries["concept"] += '</ul>'
summaries["concept"] += '</div>'

# 3. VLAN
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #4CAF50;">'
summaries["concept"] += '<h4 style="color:#4CAF50; margin-top:0; font-size:1.1em;">3. หน้าที่หลักของ VLAN (Virtual LAN)</h4>'
summaries["concept"] += '<p style="color:var(--tx); margin-bottom:0;"><b>คำตอบ:</b> ใช้แบ่งเครือข่ายวงใหญ่ (Physical) ออกเป็นเครือข่ายย่อยๆ (Logical) เพื่อลดการกระจายข้อมูล (Broadcast Domain) ที่ไม่จำเป็น ช่วยให้เครือข่ายทำงานได้เร็วขึ้น และเพิ่มความปลอดภัยเพราะแต่ละ VLAN จะคุยกันข้ามวงไม่ได้ถ้าไม่มีการทำ Routing</p>'
summaries["concept"] += '</div>'

# 4. Inter-VLAN
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #9c27b0;">'
summaries["concept"] += '<h4 style="color:#9c27b0; margin-top:0; font-size:1.1em;">4. Inter-VLAN Routing 2 รูปแบบใช้อุปกรณ์ต่างกันอย่างไร?</h4>'
summaries["concept"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["concept"] += '<li style="margin-bottom:5px;"><b>Router on a stick:</b> ใช้ <b>Router</b> ทำงานร่วมกับ Switch โดยเชื่อมต่อสายเพียงเส้นเดียว (Trunk port) เพื่อเป็นทางผ่านให้ VLAN ต่างๆ คุยกันได้</li>'
summaries["concept"] += '<li><b>SVI (Switch Virtual Interface):</b> ใช้ <b>Layer 3 Switch (Multilayer Switch)</b> ตัวเดียวจบ โดยสร้าง Interface เสมือนขึ้นมาเพื่อทำหน้าที่ Routing ภายในตัว Switch เองเลย ไม่ต้องพึ่ง Router ภายนอก</li>'
summaries["concept"] += '</ul>'
summaries["concept"] += '</div>'

# 5. STP Cost
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #e91e63;">'
summaries["concept"] += '<h4 style="color:#e91e63; margin-top:0; font-size:1.1em;">5. ค่า Cost ของ Spanning Tree Protocol (STP)</h4>'
summaries["concept"] += '<p style="color:var(--tx); margin-bottom:5px;">ค่า Cost จะแปรผกผันกับความเร็วของสายแลน (Bandwidth) <b>ยิ่งเน็ตเร็ว ค่า Cost ยิ่งต่ำ:</b></p>'
summaries["concept"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["concept"] += '<li style="margin-bottom:5px;">ความเร็ว <b>1 Gbps</b> = ค่า Cost <span style="color:var(--yw);"><b>4</b></span></li>'
summaries["concept"] += '<li>ความเร็ว <b>100 Mbps</b> (Fast Ethernet) = ค่า Cost <span style="color:var(--yw);"><b>19</b></span></li>'
summaries["concept"] += '</ul>'
summaries["concept"] += '</div>'

# 6. EtherChannel
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:15px; border-left:4px solid #2196F3;">'
summaries["concept"] += '<h4 style="color:#2196F3; margin-top:0; font-size:1.1em;">6. EtherChannel 2 รูปแบบ (โปรโตคอลและโหมด)</h4>'
summaries["concept"] += '<ul style="color:var(--tx); margin-bottom:0; padding-left:20px;">'
summaries["concept"] += '<li style="margin-bottom:5px;"><b>PAgP (ของ Cisco):</b> โหมดที่ใช้จับคู่กันคือ <b>Desirable</b> (ฝ่ายเริ่มทักก่อน) และ <b>Auto</b> (ฝ่ายรอรับการทัก)</li>'
summaries["concept"] += '<li><b>LACP (มาตรฐานสากล IEEE):</b> โหมดที่ใช้จับคู่กันคือ <b>Active</b> (ฝ่ายเริ่มทักก่อน) และ <b>Passive</b> (ฝ่ายรอรับการทัก)</li>'
summaries["concept"] += '</ul>'
summaries["concept"] += '</div>'

# 7. ACL Orders
summaries["concept"] += '<div style="background:#222; padding:15px; border-radius:8px; margin-bottom:0; border-left:4px solid #f44336;">'
summaries["concept"] += '<h4 style="color:#f44336; margin-top:0; font-size:1.1em;">7. ลำดับของ ACL (Access Control List) ที่ต้องระวัง!</h4>'
summaries["concept"] += '<p style="color:var(--tx); margin-bottom:5px;"><b>คำตอบ:</b> Router จะอ่านกฎ ACL จาก <b>"บนลงล่าง" (Top-down)</b> เสมอ</p>'
summaries["concept"] += '<p style="color:#ff4444; font-size:0.9em; margin-bottom:5px;"><b>⚠️ ปัญหาที่เจอบ่อย:</b> ถ้าคุณใส่กฎ <code>Deny Any Any</code> (บล็อกทุกอย่าง) ไว้บรรทัดล่างสุด แล้ววันหลังมากดเพิ่มกฎ (เช่น อนุญาตให้บางเครื่องเข้าได้) กฎใหม่มันจะไปต่อท้าย <code>Deny Any Any</code> ทำให้กฎใหม่ไม่ทำงานเพราะถูกบล็อกไปตั้งแต่บรรทัดก่อนหน้าแล้ว</p>'
summaries["concept"] += '<p style="color:#4CAF50; font-size:0.9em; margin-bottom:0;"><b>✅ วิธีแก้รันกฎ:</b> ต้องลบ <code>Deny Any Any</code> อันเก่าทิ้งก่อน -> ใส่กฎใหม่ที่ต้องการเข้าไป -> แล้วค่อยพิมพ์ <code>Deny Any Any</code> ปิดท้ายระบบอีกครั้งครับ</p>'
summaries["concept"] += '</div>'

summaries["concept"] += '</div>'

summaries["mock"] = '<div class="sc" style="border-color:#00e5ff; background:rgba(0, 229, 255, 0.05)"><h3 style="color:#00e5ff; font-size:1.3em;">📝 ข้อสอบจำลอง 30 ข้อ (ยึดตามคลิปเสียงอาจารย์เป๊ะๆ + ภาพประกอบ)</h3>'
summaries["mock"] += '<p style="margin-bottom:15px; font-size:1.1em; color:var(--tx);">อ้างอิง: ออก 25-30 ข้อ / ครึ่งเทอมหลัง / เน้นหลักการการทำงาน / มีคำนวณและ CLI เบาๆ</p>'
summaries["mock"] += '<ol style="line-height:1.6; padding-left:20px; color:var(--tx);">'

# Hub vs Switch / ISP (อาจารย์ใบ้ตรงๆ)
summaries["mock"] += '<li style="margin-bottom:15px"><b>(ข้อสอบชัวร์ 100%) เวลาเราเช่าเน็ตบ้าน ใครเป็นคนจ่าย IP ให้เรา?</b><br><span style="color:var(--yw)">ตอบ:</span> Internet Service Provider (ISP) เช่น AIS, True, Dtac</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>องค์กร IANA มีหน้าที่หลักเกี่ยวกับอะไร (ที่อาจารย์บอกว่าอย่าคิดเยอะ)?</b><br><span style="color:var(--yw)">ตอบ:</span> เป็นสมาคมที่กำหนดว่าหมายเลข IP ไหนเป็น Public และ IP ไหนใช้ในภูมิภาคใด (ไม่ได้เป็นคนแจก IP แจกเน็ตบ้าน)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>หลักการทำงานของ Hub แตกต่างจาก Switch อย่างไรในแง่ของการส่งข้อมูล?</b><br><span style="color:var(--yw)">ตอบ:</span> Hub ส่งแบบ Broadcast (ส่งออกทุกพอร์ต) แต่ Switch ทำงานฉลาดกว่า ส่งหาปลายทางที่เจาะจงได้โดยดูจาก MAC Address</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><div style="margin:10px 0"><img src="images/computer_network_ch10/page_09.png" style="max-height:150px; border-radius:4px" alt="broadcast"></div><b>ปัญหา Broadcast Storm มักเกิดขึ้นในอุปกรณ์ใดเมื่อไม่มีการป้องกันลูปสายแลน?</b><br><span style="color:var(--yw)">ตอบ:</span> Switch (ต้องแก้ด้วยการเปิดใช้โหมด Spanning-Tree)</li>'

# Inter-VLAN Routing Concepts
summaries["mock"] += '<li style="margin-bottom:15px"><b>หลักการทำ Inter-VLAN Route (การเชื่อม VLAN ต่างกันเข้าด้วยกัน) ทำไปเพื่ออะไร?</b><br><span style="color:var(--yw)">ตอบ:</span> เพื่อให้คอมพิวเตอร์ที่อยู่คนละวง VLAN (ซึ่งปกติคุยกันไม่เห็น) สามารถติดต่อและส่งข้อมูลข้ามวงหากันได้ผ่าน Layer 3</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>ลักษณะของการทำ Inter-VLAN Route แบบ Router-on-a-stick แตกต่างจาก SVI อย่างไร?</b><br><span style="color:var(--yw)">ตอบ:</span> Router-on-a-stick ใช้ Router ภายนอกเชื่อมสายเดียว (Trunk) แล้วซอยเป็น interface ย่อย ส่วน SVI ใช้ Switch Layer 3 จัดการเบ็ดเสร็จในตัวมันเองไม่ต้องพึ่งพา Router ตัวอื่น</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>อุปกรณ์ชนิดใดที่เหมาะสมและคุ้มค่าที่สุดในการทำรูปแบบ SVI (Switch Virtual Interface)?</b><br><span style="color:var(--yw)">ตอบ:</span> Layer 3 Switch (Multilayer Switch)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>คำสั่งใดที่ "สำคัญมาก" และห้ามลืมเด็ดขาด หากต้องการเปิดการทำงาน Routing บน Switch Layer 3?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">ip routing</code> (พิมพ์ใน Global Config)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>ในการเรียงลำดับคำสั่งเพื่อสร้าง Static Route (<code class="hl">ip route</code>) ลำดับพารามิเตอร์ที่ถูกต้องคืออะไร?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">ip route [Network ปลายทาง] [Subnet Mask] [IP ภายนอกที่จะต้องโยนข้อมูลไปให้ (Next-Hop)]</code></li>'
summaries["mock"] += '<li style="margin-bottom:15px"><div style="margin:10px 0"><img src="images/computer_network_ch9/page_12.png" style="max-height:150px; border-radius:4px" alt="roas"></div><b>จากภาพของการทำ Inter-VLAN คำสั่งใดต้องพิมพ์บน interface ย่อย (เช่น 0/0/0.10) ของ Router เสมอ?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">encapsulation dot1Q [VLAN-ID]</code></li>'

# Spanning-Tree (STP)
summaries["mock"] += '<li style="margin-bottom:15px"><b>(อาจารย์เน้น) โปรโตคอล Spanning Tree (STP) ทำงานเพื่อจุดประสงค์อะไร?</b><br><span style="color:var(--yw)">ตอบ:</span> ป้องกันปัญหา Loop ทางตรรกะ (Logical Loop) และ Broadcast Storm เมื่อมีการต่อสายแลนสำรองเชื่อมสวิตช์ชนกันเป็นวงแหวน</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>ในระบบ Spanning Tree ค่า Cost หมายเลข 4 หมายถึงพอร์ตสายแลนความเร็วเท่าใด?</b><br><span style="color:var(--yw)">ตอบ:</span> 1 Gbps (Gigabit Ethernet)<br><div style="background:#222; padding:10px; border-radius:5px; margin-top:5px; font-size:0.9em; border-left:3px solid #00e5ff;"><b>🧠 วิธีจำตารางค่า Cost สำหรับหาเส้นทาง STP ที่ดีที่สุด:</b><br>ความเร็วพอร์ตยิ่งสูง ค่าใช้จ่าย (Cost) มักจะยิ่งถูก (ดีกว่า)<br>• 10 Mbps = Cost 100<br>• <b>100 Mbps (FastEthernet) = Cost 19</b><br>• <b>1 Gbps (GigabitEthernet) = Cost 4</b><br>• 10 Gbps = Cost 2<br><i>*อาจารย์จะให้จำแค่ FastEthernet = 19 และ Gigabit = 4 ครับ</i></div></li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>(เก็งข้อสอบ) ในระบบ Spanning Tree ค่า Cost หมายเลข 19 หมายถึงพอร์ตสายแลนความเร็วเท่าใด?</b><br><span style="color:var(--yw)">ตอบ:</span> 100 Mbps (Fast Ethernet)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>คำสั่งใดที่ใช้ตรวจสอบสถานะการทำงานว่าเป็น Root Bridge หรือไม่ หรือค่า Cost เป็นเท่าไร?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">show spanning-tree</code></li>'
summaries["mock"] += '<li style="margin-bottom:15px"><div style="margin:10px 0"><img src="images/computer_network_ch10/page_17.png" style="max-height:150px; border-radius:4px" alt="stp"></div><b>สวิตช์ที่เป็นดั่ง "หัวใจหลัก" (Root) ของเครือข่าย STP จะถูกคัดเลือกจากค่าใดให้เป็นศูนย์กลาง?</b><br><span style="color:var(--yw)">ตอบ:</span> ตำแหน่ง Root Bridge คัดจากสวิตช์ที่มี Bridge ID ต่ำที่สุด (Priority + MAC Address ต่ำสุด)</li>'

# EtherChannel
summaries["mock"] += '<li style="margin-bottom:15px"><b>การทำ EtherChannel มี "ประโยชน์" หลักๆ อย่างไรต่อองค์กร?</b><br><span style="color:var(--yw)">ตอบ:</span> เพิ่ม Bandwidth ด้วยการนำสายมารวมท่อกันเหมือนถนนหลายเลน และทำ Redundancy (ถ้าสายมัดนึงขาด ที่เหลือยังช่วยกันรับส่งต่อได้ ไม่ดาวน์)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>(อาจารย์ใบ้โหมด) การทำ EtherChannel ด้วยโปรโตคอล PAgP ของ Cisco ต้องจับคู่โหมด (Mode) ใดเข้าด้วยกันจึงจะเชื่อมต่อสำเร็จ?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">desirable</code> คู่กับ <code class="hl">desirable</code> (หรือคู่กับ auto ก็ได้)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>หากใช้อุปกรณ์ต่างยี่ห้อ (ไม่ใช่ Cisco) ต้องเลือกทำ EtherChannel ด้วยโปรโตคอลใด?</b><br><span style="color:var(--yw)">ตอบ:</span> โปรโตคอล LACP (Link Aggregation Control Protocol) เป็นมาตรฐาน IEEE 802.3ad</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><div style="margin:10px 0"><img src="images/computer_network_ch11/page_09.png" style="max-height:150px; border-radius:4px" alt="lacp"></div><b>(อาจารย์ใบ้โหมด) การทำ EtherChannel รูปแบบ LACP ต้องใช้การตั้งค่าโหมดลิงก์ว่าอย่างไร?</b><br><span style="color:var(--yw)">ตอบ:</span> ใช้การจับคู่แบบ <code class="hl">active</code> คู่กับ <code class="hl">active</code> (หรือคู่กับ passive)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>คำสั่งใดเป็นพระเอกหลักที่ใช้ตรวจดูว่า EtherChannel ผูกสายลิงก์สองเส้นเข้าหากัน (Logical Port) สำเร็จขึ้นสถานะ (SU) แล้วหรือยัง?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">show etherchannel summary</code></li>'

# ACL
summaries["mock"] += '<li style="margin-bottom:15px"><b>(อาจารย์ถามการเรียงลำดับ) "รูปแบบ" ของ Access Control List (ACL) มีกี่ประเภทหลักๆ?</b><br><span style="color:var(--yw)">ตอบ:</span> 2 ประเภท คือ Standard (กรองแค่ต้นทาง) และ Extended (กรองละเอียดยิบถึงประเภท Port/Protocol TCP/UDP)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>ในการคอนฟิกและการทำงานของตรรกะ ACL ลำดับบรรทัดใดจะถูกนำมาพิจารณาประมวลผลก่อน?</b><br><span style="color:var(--yw)">ตอบ:</span> ประมวลผลแบบ Top-Down (หรือจากบนลงล่างตาม Sequence Number) และหากพบกฎที่แมตช์บรรทัดบนแล้ว จะกระโดดออกจากกลไกกรองทันทีโดยไม่สนบรรทัดล่างอีกเลย</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>ด้วยเหตุใดในการสร้าง Extended ACL จึงต้องจัด "ลำดับ" โดยนำเงื่อนไขแบบ Deny เจาะจงวางไว้ข้างบน และนำ Permit กว้างๆ วางไว้บรรทัดล่างๆ?</b><br><span style="color:var(--yw)">ตอบ:</span> เพราะกฎทำงานแบบจากบนลงล่าง ถ้าเอา Permit All ขึ้นบนสุด ทุกคนก็จะผ่านหมดโดยที่คำสั่ง Deny แบน IP ไม่ถูกอ่านเลย</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><div style="margin:10px 0"><img src="images/computer_network_ch10_new/page_12.png" style="max-height:150px; border-radius:4px" alt="acl mask"></div><b>(คำนวณ 1 ข้อ) หากต้องการกำหนดช่วง Network 10.10.10.0/24 ในคำสั่ง ACL จะต้องเว้นวรรคและตามด้วย Wildcard Mask ค่าเลขใด?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">0.0.0.255</code><br><div style="background:#222; padding:10px; border-radius:5px; margin-top:5px; font-size:0.9em; border-left:3px solid #00e5ff;"><b>🧠 หลักการคำนวณ Wildcard Mask:</b><br>1. ให้เอาค่าสูงสุดคือ <code>255.255.255.255</code> เป็นตัวตั้งเสมอ<br>2. นำ Subnet Mask ของโจทย์ไปลบออก (โจทย์ /24 คือ <code>255.255.255.0</code>)<br>3. จะได้: <code>255.255.255.255 - 255.255.255.0 = 0.0.0.255</code><br><i>*เผื่อเจอโจทย์อื่น: ถ้าโจทย์เปลี่ยนเป็น /25 (Subnet 255.255.255.128) เอาไปลบจะได้คำตอบคือ <code>0.0.0.127</code></i></div></li>'

# IPv6 & Miscellaneous (to hit exactly 30 Qs based on broad hints of chapter scope)
summaries["mock"] += '<li style="margin-bottom:15px"><b>(IPv6) หากต้องการเขียนย่อเลขหมาย <code class="hl">2001:0db8:0000:0000:0000:0000:0000:0001</code> ควรย่ออย่างไร?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">2001:db8::1</code><br><div style="background:#222; padding:10px; border-radius:5px; margin-top:5px; font-size:0.9em; border-left:3px solid #00e5ff;"><b>🧠 หลักการย่อ IPv6 แบบเจอกับตัวไหนก็ทำได้:</b><br>1. <b>ตัดเลข 0 ข้างหน้าสุดทิ้งได้เสมอ:</b> <code>0db8</code> เหลือแค่ <code>db8</code> (ถ้า <code>0000</code> จะเหลือ <code>0</code> ตัวเดียว)<br>2. <b>ยุบกลุ่ม 0 ติดกันยาวๆ:</b> ให้แทนก้อนนั้นด้วย <code>::</code> ไปเลย แต่อย่าลืมกฎเหล็กว่า <b>"ใช้ :: ได้แค่จุดเดียวเท่านั้นใน 1 ไอพี"</b><br><i>*เผื่อเจอโจทย์อื่น: <code>2001:0000:0000:1234:0000:0000:0000:abcd</code> ควรย่อเป็น <code>2001:0:0:1234::abcd</code> (ให้เลือกยุบก้อน 0 ที่ยาวที่สุดก่อนเสมอ)</i></div></li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>(IPv6) ชนิดที่อยู่ใดใน IPv6 ที่เทียบเท่าได้กับฟังก์ชัน APIPA (IP เด้งอัตโนมัติ 169.254.x.x) ของระบบ IPv4?</b><br><span style="color:var(--yw)">ตอบ:</span> Link-Local (โดยส่วนใหญ่จะเริ่มต้นด้วยโค้ด FE80)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>ในการใส่กฎ ACL ไปยัง Interface (เช่น port G0/0) คำว่า in และ out มีความหมายต่างกันอย่างไร?</b><br><span style="color:var(--yw)">ตอบ:</span> in = กรองแพ็กเก็ตจังหวะที่ "ไหลเข้าสู่เร้าเตอร์" | out = กรองจังหวะที่ "เร้าเตอร์เตรียมฉีดข้อมูลพ่นออกไป"</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>การกำหนดหมายเลข ACL แบบตัวเลข (Numbered ACL) หากเราใส่เลข 110 หมายความว่ากำลังสร้าง ACL ชนิดใด?</b><br><span style="color:var(--yw)">ตอบ:</span> Extended ACL (ช่วงเลข 100-199)</li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>(คำนวณ) ในระบบ PVST+ หากสวิตช์ใช้ Priority ค่าเริ่มต้น (32768) และตั้งให้อยู่ใน VLAN 20 ค่า Bridge Priority จะแสดงผลเป็นเท่าไร?</b><br><span style="color:var(--yw)">ตอบ:</span> <code class="hl">32788</code><br><div style="background:#222; padding:10px; border-radius:5px; margin-top:5px; font-size:0.9em; border-left:3px solid #00e5ff;"><b>🧠 หลักการคำนวณ Bridge Priority / Bridge ID:</b><br>1. โครงสร้างการประกาศตัวคือ = <b>ค่า Priority + หมายเลข VLAN ID</b><br>2. สวิตช์ Cisco ทุกตัวมีค่า <b>Priority Default = 32768</b> เสมอ<br>3. เอาค่า Default + VLAN ตัวนั้นๆ (<code>32768 + 20 = 32788</code>)<br><i>*เผื่อเจอโจทย์อื่น: ถ้าโจทย์สมมติเป็น VLAN 10 ค่านั้นก็จะเป็น <code>32768 + 10 = 32778</code></i></div></li>'
summaries["mock"] += '<li style="margin-bottom:15px"><b>จากคำใบ้ทั้งหมดข้างต้น หากอาจารย์ถามคำถามข้อสอบข้อใดว่า "โปรโตคอลเปิดที่เป็นมาตรฐานกลางสำหรับมัดเทคโนโลยีสายลิงก์" คือโปรโตคอลใด?</b><br><span style="color:var(--yw)">ตอบ:</span> ย้ำอีกครั้งว่าคำตอบคือ LACP (Active/Passive) เท่านั้น</li>'
summaries["mock"] += '</ol></div>'

summaries["leak"] = '<div class="sc" style="border-color:var(--yw); background:rgba(255, 215, 64, 0.05)"><h3 style="color:var(--yw); font-size:1.3em;">🔥 เก็งข้อสอบ 100% (คำอธิบายแบบเอาไปจดเข้าห้องสอบ)</h3>'

# Add professor's hints
summaries["leak"] += '<div style="background-color:rgba(255, 68, 68, 0.1); border-left:4px solid #ff4444; padding:15px; margin-bottom:20px; border-radius:4px;">'
summaries["leak"] += '<h4 style="color:#ff4444; margin-top:0; font-size:1.1em;">🚨 คำใบ้สโคปข้อสอบจากอาจารย์ (อัปเดตล่าสุด!)</h4>'
summaries["leak"] += '<ul style="margin-bottom:0; color:var(--tx);">'
summaries["leak"] += '<li style="margin-bottom:5px"><b>จำนวนข้อสอบ:</b> แบบกากบาท (Multiple Choice) ประมาณ <b>25 - 30 ข้อ</b></li>'
summaries["leak"] += '<li style="margin-bottom:5px"><b>ขอบเขต (Scope):</b> ออกสอบเฉพาะ <b>"เนื้อหาครึ่งเทอมหลัง"</b> เท่านั้น! (ให้อ่านเฉพาะบทที่ 9 ถึง 13 พอ ไม่ต้องอ่านครึ่งแรก)</li>'
summaries["leak"] += '<li style="margin-bottom:5px"><b>แนวทฤษฎี:</b> ข้อสอบเน้นถาม <b>"หลักการการทำงาน (Concept)"</b> ให้อ่านทำความเข้าใจว่าแต่ละโปรโตคอลมีหน้าที่อะไร (เช่น ROAS vs SVI ต่างกันยังไง, STP มีไว้ทำไม)</li>'
summaries["leak"] += '<li style="margin-bottom:0"><b>แนวคำนวณ / คำสั่ง Cisco:</b> จะมีโผล่มาประมาณ <b>3 ข้อ</b> (เก็งว่าหนีไม่พ้นเรื่อง ย่อเลข IPv6, คิด Wildcard Mask ใน ACL, หรือหาค่า Cost ของ STP)</li>'
summaries["leak"] += '</ul></div>'

summaries["leak"] += '<p style="margin-bottom:15px; font-size:1.1em; color:var(--tx);">สรุปเนื้อหาแบบเนื้อๆ เน้นๆ พร้อมคำสั่ง (Command) ที่ต้องใช้จริง สั้น กระชับ จำง่าย:</p>'
summaries["leak"] += '<div style="margin-bottom:20px;"><h4>1. Hub vs Switch ต่างกันยังไง</h4>'
summaries["leak"] += '<p><b>Hub (Layer 1):</b> ทำงานแบบ <u>Broadcast</u> คือส่งข้อมูลออกไปทุกช่องจิ๋วๆ เสี่ยงชนกัน (Collision) ทำงานแบบสลับกันส่ง (Half-Duplex)</p>'
summaries["leak"] += '<p><b>Switch (Layer 2):</b> ฉลาดกว่า จำ <u>MAC Address</u> ได้ ส่งข้อมูลหาปลายทางได้ตรงเครื่องเป๊ะๆ (Unicast) ทำงานพร้อมกันได้ (Full-Duplex) ไวกว่าเยอะ</p></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>2. การทำ Broadcast CLI</h4>'
summaries["leak"] += '<p>ปกติ <b>Router ทั่วไปจะมีหน้าที่กั้น Broadcast Domain อยู่แล้ว</b> (ไม่ให้วงแลนซ้ายส่ง Broadcast ไปกวนวงแลนขวา) แต่ถ้าเจอคำถามว่าแก้อาการ Broadcast Storm ใน Switch ยังไง คำตอบคือเปิด <b>STP</b>:</p>'
summaries["leak"] += '<div class="cb">Switch(config)# spanning-tree vlan 1</div></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>3. Encapsulation CLI</h4>'
summaries["leak"] += '<p>คำสั่งสำคัญมาก <b>ใช้บน Router ตอนทำวิธี Router-on-a-Stick (ROAS)</b> เพื่อบอกว่า Sub-interface นี้ (เช่น .10) จะรับผิดชอบ VLAN หมายเลขอะไร (เช่น VLAN 10)</p>'
summaries["leak"] += '<div class="cb">Router(config)# interface gigabitEthernet 0/0/0.10\n<span class="hl">Router(config-subif)# encapsulation dot1Q 10</span></div></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>4. Route CLI</h4>'
summaries["leak"] += '<p>ถ้าข้อสอบออกเรื่อง <b>L3 Switch</b> (Switch ที่ทำ Routing ได้) กฎเหล็กคือต้องพิมพ์คำสั่งเปิดโหมด Route ก่อน ไม่งั้น Ping ข้าม VLAN ไม่ได้เด็ดขาด!</p>'
summaries["leak"] += '<div class="cb">Switch(config)# <span class="hl">ip routing</span></div></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>5. InterVLAN Route concept (ลักษณะ 2 แบบ)</h4>'
summaries["leak"] += '<table style="margin-top:10px"><tr><th>วิธีที่ 1: Router-on-a-Stick (ROAS)</th><th>วิธีที่ 2: Switch Virtual Interface (SVI)</th></tr>'
summaries["leak"] += '<tr><td>ใช้ Router แยกประกอบกับ Switch<br>ต่อสาย Trunk 1 เส้นหา Router<br><b>ข้อเสีย:</b> โหลดไปกองที่ Router (เป็นคอขวด)</td><td>ใช้ Layer 3 Switch ตัวเดียวจบ<br>สร้าง Virtual Interface ตัวแทนแต่ละ VLAN<br><b>ข้อดี:</b> ประสิทธิภาพสูงมาก ประมวลผลในฮาร์ดแวร์</td></tr></table></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>6. Protocol Spanning-Tree (cost etc. 4, 19)</h4>'
summaries["leak"] += '<p>ค่า Cost ใช้เป็น "คะแนน" หาเส้นทางที่สั้นที่สุด (Root Port) <b>จำเลข 2 ตัวนี้ไปตอบ:</b></p>'
summaries["leak"] += '<ul><li>พอร์ตความเร็ว <b>1 Gbps</b> (GigabitEthernet) = <b><span class="hl">Cost 4</span></b></li>'
summaries["leak"] += '<li>พอร์ตความเร็ว <b>100 Mbps</b> (FastEthernet) = <b><span class="hl">Cost 19</span></b></li></ul></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>7. Etherchannel ประโยชน์ / การทำ 2 แบบ</h4>'
summaries["leak"] += '<p><b>ประโยชน์:</b> เอาสาย LAN หลายเส้นมัดรวมกันเพื่อ 1. เพิ่ม Bandwidth 2. ทำ Redundancy (เส้นนึงขาด อีกเส้นสำรองไม่เน็ตหลุด)</p>'
summaries["leak"] += '<ul><li><b>แบบที่ 1 PAgP:</b> ของ Cisco ผูกขาด <br><u>Command โหมด</u>: <code class="hl">desirable</code> (เริ่มขอ) หรือ <code class="hl">auto</code> (รอเขาขอ)</li>'
summaries["leak"] += '<li><b>แบบที่ 2 LACP:</b> มาตรฐานกลาง IEEE ยี่ห้อไหนก็ใช้ได้ <br><u>Command โหมด</u>: <code class="hl">active</code> (เริ่มขอ) หรือ <code class="hl">passive</code> (รอเขาขอ)</li></ul></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>8. วิธีเขียน IPv6</h4>'
summaries["leak"] += '<p>กฎการย่อ (จำง่ายๆ):</p>'
summaries["leak"] += '<ol><li>ตัด 0 ข้างหน้าสุดทิ้งได้ <code>0202</code> &rarr; <code>202</code></li>'
summaries["leak"] += '<li>ถ้ากลุ่มนั้นมีแต่ 0000 ให้เขียน <code>0</code> ตัวเดียวพอ</li>'
summaries["leak"] += '<li>ถ้าเจอกลุ่มตัวเลข 0 รวดติดกันยาวๆ ยุบรวมเป็น <code>::</code> <span class="hl">(ห้ามทำเกิน 1 ครั้งใน IP เดียว!)</span></li></ol></div>'

summaries["leak"] += '<div style="margin-bottom:20px;"><h4>9. ACL รูปแบบ ลำดับ (deny any latest)</h4>'
summaries["leak"] += '<p>ACL จะเช็คเงื่อนไขทีละบรรทัดจากบนลงล่าง (Top-Down)</p>'
summaries["leak"] += '<p><b>กฎสำคัญ:</b> บรรทัดสุดท้ายล่างสุดของ ACL จะมีคำสั่งผี <b>"Implicit Deny Any"</b> (บล็อกทุกการเชื่อมต่อ) ซ่อนอยู่เสมอ! ดังนั้นก่อนจบ ACL มักจะต้องพิมพ์อนุญาตทุกคนที่เหลือด้วยคำสั่งนี้ด้านล่างสุด (latest):</p>'
summaries["leak"] += '<div class="cb">Router(config-ext-nacl)# <span class="hl">permit ip any any</span></div></div>'

summaries["leak"] += '</div>'

summaries["ch9"] = '<div class="sc"><h3>InterVLAN Routing</h3><p>คือการทำให้ Host ที่อยู่ <b>ต่าง VLAN กัน</b> ติดต่อกันได้ โดยต้องมีอุปกรณ์ Layer 3 มาช่วย</p></div>'
summaries["ch9"] += '<div class="sc"><h3>วิธีที่ 1: Router-on-a-Stick (ROAS)</h3><ul><li>ใช้ Router ต่อกับ Switch ผ่าน <b>Trunk link 1 เส้น</b></li><li>Router มี <b>Sub-interfaces</b> แต่ละตัวแทน VLAN</li><li>ข้อมูลถูกส่งไป Router แล้ว Route กลับไปยัง VLAN ปลายทาง</li></ul>'
summaries["ch9"] += '<h4>Config Router (ROAS)</h4><div class="cb">Router(config)# interface GigabitEthernet 0/0/0.10\nRouter(config-if)# encapsulation dot1q 10\nRouter(config-if)# ip address 192.168.10.1 255.255.255.0\n\nRouter(config)# interface GigabitEthernet 0/0/0.20\nRouter(config-if)# encapsulation dot1q 20\nRouter(config-if)# ip address 192.168.20.1 255.255.255.0</div>'
summaries["ch9"] += '<h4>การทำงาน ROAS</h4><ol><li>192.168.10.10 ส่งข้อมูลให้ 192.168.20.10</li><li>Router รับเฟรม Tag VLAN 10 บน sub-interface</li><li>Router ถอด Frame Header หาเส้นทางไปวง 192.168.20.0/24</li><li>ส่งไป sub-interface ที่ติด Tag VLAN 20 กลับไป Switch ผ่าน Trunk</li></ol></div>'

summaries["ch9"] += '<div class="sc"><h3>วิธีที่ 2: Switch Virtual Interface (SVI)</h3><ul><li>ใช้ <b>L3 Switch</b> ที่รองรับ Routing โดยไม่ต้องใช้ Router เพิ่ม</li><li>SVI = Virtual Interface ของแต่ละ VLAN</li><li>ใช้คำสั่ง <code>ip routing</code> เปิดใช้งาน</li></ul>'
summaries["ch9"] += '<h4>Config L3 Switch (SVI)</h4><div class="cb">Switch(config)# vlan 10\nSwitch(config)# exit\nSwitch(config)# vlan 20\nSwitch(config)# exit\nSwitch(config)# interface vlan 10\nSwitch(config-if)# ip address 192.168.10.1 255.255.255.0\nSwitch(config)# interface vlan 20\nSwitch(config-if)# ip address 192.168.20.1 255.255.255.0\n\n<span class="hl">Switch(config)# ip routing</span>\nSwitch(config)# interface gigabit 0/1\nSwitch(config-if)# switchport trunk encapsulation dot1q\nSwitch(config-if)# switchport mode trunk</div></div>'

summaries["ch9"] += '<div class="sc"><h3>ROAS vs SVI</h3><table><tr><th>หัวข้อ</th><th>ROAS</th><th>SVI</th></tr><tr><td>อุปกรณ์</td><td>Router + Switch</td><td>L3 Switch ตัวเดียว</td></tr><tr><td>คำสั่ง</td><td>encapsulation dot1q</td><td>interface vlan + ip routing</td></tr><tr><td>ประสิทธิภาพ</td><td>ต่ำกว่า (คอขวดที่ Router)</td><td>สูงกว่า</td></tr></table></div>'

# CH10 STP
summaries["ch10"] = '<div class="sc"><h3>ปัญหาของ Network Redundancy</h3><ol><li><b>Broadcast Storm</b> - Switch ส่ง broadcast ต่อกันไม่สิ้นสุด เครือข่ายล่ม</li><li><b>Multiple Frame Transmission</b> - เครื่องปลายทางรับ Frame ซ้ำ เสีย bandwidth</li><li><b>MAC Database Instability</b> - MAC table สับสน ส่งกลับไม่ถูก</li></ol></div>'
summaries["ch10"] += '<div class="sc"><h3>STP (Spanning Tree Protocol)</h3><p>โปรโตคอล Layer 2 ป้องกัน Loop ในเครือข่าย Ethernet</p><h4>หลักการทำงาน</h4><ol><li>เลือก <b>Root Bridge</b></li><li>คำนวณเส้นทางดีสุด (<b>Root Path Cost</b>)</li><li>เลือก Port ที่จะ <b>Block</b></li><li>ส่ง <b>BPDU</b></li></ol></div>'
summaries["ch10"] += '<div class="sc"><h3>BPDU (Bridge Protocol Data Units)</h3><p>เฟรมพิเศษที่ส่งระหว่าง Switch</p><ul><li>Root Bridge ID</li><li>Cost to Root Bridge</li><li>Sender Bridge ID</li><li>Port ID</li><li>STP timers</li></ul></div>'
summaries["ch10"] += '<div class="sc"><h3>การเลือก Root Bridge</h3><ul><li><b>Bridge ID = Priority + MAC Address</b></li><li>ค่าเริ่มต้น Priority = <b>32768</b></li><li>ช่วง: 0-61440 (หาร 4096 ลงตัว)</li><li>Bridge ID <b>ต่ำสุด</b> = Root Bridge</li><li>Priority เท่ากัน → เทียบ MAC Address</li></ul><div class="cb">VLAN 1: 32768 + 1 = 32769\nVLAN 10: 32768 + 10 = 32778\nVLAN 100: 32768 + 100 = 32868</div></div>'
summaries["ch10"] += '<div class="sc"><h3>STP Port Costs</h3><table><tr><th>ความเร็ว</th><th>Cost</th></tr><tr><td>10 Gbps</td><td>2</td></tr><tr><td>1 Gbps</td><td>4</td></tr><tr><td>100 Mbps (FastEthernet)</td><td>19</td></tr><tr><td>10 Mbps</td><td>100</td></tr></table>'
summaries["ch10"] += '<h4>ประเภท Port</h4><table><tr><th>Port</th><th>คำอธิบาย</th></tr><tr><td><b>Root Port (RP)</b></td><td>เส้นทางดีสุดไป Root Bridge (ทุก Non-Root Switch มี 1 RP)</td></tr><tr><td><b>Designated Port (DP)</b></td><td>ตัวแทนในแต่ละ segment รับ-ส่ง frame (ไม่ซ้ำ RP)</td></tr><tr><td><b>Non-Designated (NDP)</b></td><td>ถูก Block เพื่อหยุด Loop (cost มากสุด)</td></tr></table></div>'
summaries["ch10"] += '<div class="sc"><h3>STP Process & Timers</h3><h4>Normal (เสียบสายใหม่)</h4><ol><li>BLOCKING</li><li>LISTENING (15s) - ส่ง/รับ BPDU</li><li>LEARNING (15s) - เรียนรู้ MAC</li><li>FORWARDING - ส่งข้อมูลได้</li></ol><h4>Switch Link Down</h4><ol><li>BLOCKING (20s)</li><li>LISTENING (15s)</li><li>LEARNING (15s)</li><li>FORWARDING</li></ol><p><b class="hl">รวม = 20+15+15 = 50 วินาที</b></p>'
summaries["ch10"] += '<h4>คำสั่ง STP</h4><div class="cb"><span class="cm">! ปิด STP</span>\nSwitch(config)# no spanning-tree vlan 1\n<span class="cm">! เปิด STP</span>\nSwitch(config)# spanning-tree vlan 1\n<span class="cm">! ดูสถานะ</span>\nSwitch# show spanning-tree</div></div>'

# CH10new ACL
summaries["ch10new"] = '<div class="sc"><h3>ACL (Access Control List)</h3><p>กลไก<b>ควบคุมการเข้าถึงเครือข่าย</b>โดยกรองแพ็กเก็ตที่เข้า/ออกจาก Router</p></div>'
summaries["ch10new"] += '<div class="sc"><h3>ประเภท ACL</h3><table><tr><th>ประเภท</th><th>หมายเลข</th><th>กรองตาม</th></tr><tr><td><b>Standard</b></td><td>1-99, 1300-1999</td><td>Source IP <b>เท่านั้น</b></td></tr><tr><td><b>Extended</b></td><td>100-199, 2000-2699</td><td>Source/Dest IP, Protocol, Port</td></tr></table><h4>รูปแบบ</h4><table><tr><th>แบบ</th><th>ตัวอย่าง</th></tr><tr><td>Number</td><td>Standard 1-99, Extended 100-199</td></tr><tr><td>Named</td><td>ใช้ชื่อแทนตัวเลข</td></tr></table></div>'
summaries["ch10new"] += '<div class="sc"><h3>ขั้นตอนตั้งค่า ACL</h3><ol><li><b>สร้าง ACL</b></li><li><b>ประกาศใช้ ACL</b> (ผูกกับ Interface)</li></ol><h4>Standard ACL Named</h4><div class="cb"><span class="cm">! สร้าง ACL</span>\nRouter(config)# ip access-list standard TEST\nRouter(config-std-nacl)# permit host 10.0.0.10\n\n<span class="cm">! ประกาศใช้ ACL</span>\nRouter(config)# interface F0/0\nRouter(config-if)# ip access-group TEST in\n<span class="cm">! หรือ</span>\nRouter(config-if)# ip access-group TEST out</div></div>'
summaries["ch10new"] += '<div class="sc"><h3>Wildcard Mask</h3><p>คำนวณ: <b>255.255.255.255 - Subnet Mask</b></p><table><tr><th>Subnet Mask</th><th>Wildcard</th><th>ความหมาย</th></tr><tr><td>255.255.255.255</td><td><b>0.0.0.0</b></td><td>ตรง host เดียว</td></tr><tr><td>255.255.255.0</td><td><b>0.0.0.255</b></td><td>Network /24</td></tr><tr><td>255.255.0.0</td><td><b>0.0.255.255</b></td><td>Network /16</td></tr><tr><td>0.0.0.0</td><td><b>255.255.255.255</b></td><td>ทุก IP (any)</td></tr></table><p><b>0</b> = ต้องตรง | <b>255</b> = ไม่สนใจ</p></div>'
summaries["ch10new"] += '<div class="sc"><h3>การเลือกจุดใช้ ACL</h3><ul><li><b>Standard ACL</b> วางใกล้ <b>Destination</b> (ปลายทาง)</li><li><b>Extended ACL</b> วางใกล้ <b>Source</b> (ต้นทาง)</li><li><b>in</b> = กรองแพ็กเก็ตที่เข้า interface</li><li><b>out</b> = กรองแพ็กเก็ตที่ออก interface</li></ul></div>'
summaries["ch10new"] += '<div class="sc"><h3>Extended ACL</h3><div class="cb">Router(config)# ip access-list extended [NAME]\nRouter(config-ext-nacl)# [permit/deny] [protocol] [source] [wildcard] [dest] [wildcard] eq [port]\n\n<span class="cm">! ตัวอย่าง: บล็อก 10.0.0.10 ไม่ให้เข้าเว็บ 192.168.10.10</span>\naccess-list 100 deny tcp host 10.0.0.10 host 192.168.10.10 eq 80\naccess-list 100 permit ip any any</div><p class="hl">ท้าย ACL มี implicit deny any เสมอ - ต้องใส่ permit ip any any</p></div>'

# CH11 EtherChannel
summaries["ch11"] = '<div class="sc"><h3>EtherChannel คืออะไร?</h3><p>รวม link หลายเส้นเข้าด้วยกัน เพิ่ม bandwidth+ความทนทาน สูงสุด <b>8 พอร์ต</b>/channel</p><ul><li><b>Bandwidth</b>: 2x1Gbps = 2Gbps, 4x1Gbps = 4Gbps</li><li><b>Redundancy</b>: link หนึ่งล้ม ที่เหลือยังทำงาน</li><li><b>ลดภาระ STP</b>: มองเป็น link เดียว</li></ul></div>'
summaries["ch11"] += '<div class="sc"><h3>ข้อจำกัด</h3><ul><li>Port ต้อง<b>ความเร็วเท่ากัน</b></li><li>Port ต้อง<b>โหมดเดียวกัน</b></li><li>สูงสุด <b>8 links</b>/channel</li><li>ต้องรวม<b>ทั้งสองฝั่ง</b></li></ul></div>'
summaries["ch11"] += '<div class="sc"><h3>โหมด EtherChannel</h3><table><tr><th>โหมด</th><th>Protocol</th><th>คำอธิบาย</th><th>ใช้ร่วมกับ</th></tr><tr><td><b>on</b></td><td>Manual</td><td>กำหนดเอง ไม่เจรจา</td><td>on</td></tr><tr><td><b>desirable</b></td><td>PAgP (Cisco)</td><td>เริ่มร้องขอ</td><td>auto, desirable</td></tr><tr><td><b>auto</b></td><td>PAgP (Cisco)</td><td>รอฝั่งตรงข้าม</td><td>desirable</td></tr><tr><td><b>active</b></td><td>LACP (IEEE)</td><td>เริ่มร้องขอ</td><td>passive, active</td></tr><tr><td><b>passive</b></td><td>LACP (IEEE)</td><td>รอฝั่งตรงข้าม</td><td>active</td></tr></table><p class="hl">PAgP = Cisco | LACP = IEEE 802.3ad ทุกยี่ห้อ</p></div>'
summaries["ch11"] += '<div class="sc"><h3>คำสั่ง Config</h3><h4>Static (on)</h4><div class="cb">Switch(config)# interface range Gi1/0/1 - 2\nSwitch(config-if-range)# channel-group 1 mode on</div><h4>PAgP</h4><div class="cb">Switch(config-if-range)# channel-group 1 mode desirable\n<span class="cm">! หรือ mode auto</span></div><h4>LACP</h4><div class="cb">Switch(config-if-range)# channel-group 1 mode active\n<span class="cm">! หรือ mode passive</span></div><h4>ดูการตั้งค่า</h4><div class="cb">Switch# show etherchannel summary</div></div>'

# CH13 IPv6
summaries["ch13"] = '<div class="sc"><h3>IPv6 คืออะไร?</h3><ul><li>IPv4 = 32-bit ~ 4.3 พันล้าน</li><li>IPv6 = <b>128-bit</b> ~ 3.4 x 10<sup>38</sup> addresses</li></ul></div>'
summaries["ch13"] += '<div class="sc"><h3>IPv4 vs IPv6</h3><table><tr><th>หัวข้อ</th><th>IPv4</th><th>IPv6</th></tr><tr><td>Address</td><td>32-bit</td><td>128-bit</td></tr><tr><td>Header Fields</td><td>13</td><td>7 (เร็วขึ้น)</td></tr><tr><td>Header Size</td><td>ไม่แน่นอน</td><td>คงที่ 40 bytes</td></tr><tr><td>Checksum</td><td>มี</td><td>ไม่มี</td></tr><tr><td>Options</td><td>ใน Header</td><td>Extended Header</td></tr><tr><td>Auto Config</td><td>DHCP</td><td>Stateless+DHCP</td></tr><tr><td>Security</td><td>IPsec optional</td><td>IPsec mandated</td></tr><tr><td>Broadcast</td><td>มี</td><td><b>ไม่มี</b></td></tr><tr><td>Min MTU</td><td>576B</td><td>1280B</td></tr><tr><td>Fragment</td><td>Router ระหว่างทาง</td><td>Source เท่านั้น</td></tr><tr><td>TTL</td><td>Time-To-Live (วินาที)</td><td>Hop Limit (hops)</td></tr></table></div>'
summaries["ch13"] += '<div class="sc"><h3>การเขียน IPv6</h3><p>8 กลุ่ม x 16-bit เขียนเลขฐาน 16 คั่นด้วย <code>:</code></p><h4>กฎย่อ</h4><ol><li>ตัดเลข 0 นำหน้า: 0dcb &rarr; dcb</li><li>0000 เขียนเป็น 0</li><li>กลุ่ม 0000 ติดกัน แทนด้วย <code>::</code> (ทำได้ 1 ครั้ง)</li></ol><h4>ตัวอย่าง</h4><table><tr><th>เต็ม</th><th>ย่อ</th></tr><tr><td>fe80:0000:0000:0000:0202:b3ff:fe1e:8329</td><td><b>fe80::202:b3ff:fe1e:8329</b></td></tr><tr><td>2001:0000:0000:34fe:0000:0000:00ff:0321</td><td><b>2001::34fe:0:0:ff:321</b></td></tr><tr><td>0000:...:0001</td><td><b>::1</b></td></tr></table></div>'
summaries["ch13"] += '<div class="sc"><h3>ประเภท IPv6 Address</h3><table><tr><th>ประเภท</th><th>รูปแบบ</th><th>คำอธิบาย</th></tr><tr><td><b>Unicast</b></td><td>one-to-one</td><td>เครื่องหนึ่งไปอีกเครื่อง</td></tr><tr><td><b>Multicast</b></td><td>one-to-many</td><td>ส่งไปกลุ่ม Group</td></tr><tr><td><b>Anycast</b></td><td>one-to-one-of-many</td><td>ส่งไปเครื่องที่ใกล้สุดใน set</td></tr></table><p class="hl">IPv6 ไม่มี Broadcast!</p><h4>Unicast Types</h4><table><tr><th>ชนิด</th><th>Prefix</th><th>เทียบ IPv4</th></tr><tr><td>Global Unicast</td><td>2000::/3</td><td>Public IP</td></tr><tr><td>Link-Local</td><td>FE80::/10</td><td>169.254.x.x</td></tr><tr><td>Unique Local</td><td>FC00::/7</td><td>Private IP</td></tr></table></div>'
summaries["ch13"] += '<div class="sc"><h3>Extended Header</h3><ol><li><b>Hop-by-Hop</b> - ทุก Router ต้องอ่าน (Jumbogram max 2<sup>32</sup>B)</li><li><b>Destination Options</b></li><li><b>Routing</b> - Source Routing (Strict/Loose)</li><li><b>Fragment</b> - ที่ Source เท่านั้น (PMTUD)</li><li><b>Authentication</b> - IPsec</li><li><b>ESP</b> - Encryption</li></ol></div>'
summaries["ch13"] += '<div class="sc"><h3>Backward Compatibility</h3><ul><li><b>Dual Stack</b> - ใช้ IPv4+IPv6 พร้อมกัน</li><li><b>Tunneling</b> - ห่อ IPv6 ด้วย IPv4 Header</li><li><b>Translation</b> - แปลง IPv6&#8596;IPv4</li><li><b>IPv4-mapped</b>: 222.1.41.90 &rarr; <code>::FFFF:222.1.41.90</code></li></ul></div>'

# Labs
summaries["lab9"] = '<div class="sc"><h3>LAB-09: InterVLAN Routing</h3><h4>Part 1: Router on a Stick</h4><div class="cb">enable\nconfigure terminal\ninterface gigabitEthernet 0/0/0\nno shutdown\nexit\ninterface gigabitEthernet 0/0/0.10\nencapsulation dot1Q 10\nip address 192.168.10.1 255.255.255.0\nexit\ninterface gigabitEthernet 0/0/0.20\nencapsulation dot1Q 20\nip address 192.168.20.1 255.255.255.0\nexit\nend</div><h4>Part 2: SVI (L3 Switch)</h4><div class="cb">enable\nconfigure terminal\nvlan 10\nexit\nvlan 20\nexit\ninterface vlan 10\nip address 192.168.10.1 255.255.255.0\nno shutdown\nexit\ninterface vlan 20\nip address 192.168.20.1 255.255.255.0\nno shutdown\nexit\n<span class="hl">ip routing</span>\nend</div></div>'

summaries["lab10"] = '<div class="sc"><h3>LAB-10: ACL + VLAN</h3><table><tr><th>กลุ่ม</th><th>VLAN</th><th>Network</th></tr><tr><td>Teacher</td><td>10</td><td>192.168.10.0/24</td></tr><tr><td>Student</td><td>20</td><td>192.168.20.0/24</td></tr><tr><td>Staff</td><td>30</td><td>192.168.30.0/24</td></tr><tr><td>Server</td><td>1</td><td>10.80.1.0/24</td></tr></table><h4>เงื่อนไข ACL</h4><ol><li>ทุก VLAN เข้าเว็บได้ (10.80.1.16)</li><li>Student ping Teacher ไม่ได้</li><li>Student ping Staff ไม่ได้</li><li>Teacher+Staff ping กันได้</li></ol>'
summaries["lab10"] += '<h4>แนวทางการ Config ACL (จากโจทย์)</h4><p>ใน Lab นี้ใช้ <b>Extended ACL</b> เบอร์ 100 ผูกไว้ที่ Interface ของ Student (VLAN 20) แบบ <b>in</b> (กันตั้งแต่ด่านแรก)</p>'
summaries["lab10"] += '<div class="cb">Router(config)# access-list 100 permit tcp 192.168.20.0 0.0.0.255 host 10.80.1.16 eq 80\n'
summaries["lab10"] += '<span class="cm">! อนุญาตให้ Student เข้าเว็บ (TCP port 80) ของ Server ได้</span>\n\n'
summaries["lab10"] += 'Router(config)# access-list 100 deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255\n'
summaries["lab10"] += '<span class="cm">! บล็อกไม่ให้ Student ping หา Teacher</span>\n\n'
summaries["lab10"] += 'Router(config)# access-list 100 deny ip 192.168.20.0 0.0.0.255 192.168.30.0 0.0.0.255\n'
summaries["lab10"] += '<span class="cm">! บล็อกไม่ให้ Student ping หา Staff</span>\n\n'
summaries["lab10"] += 'Router(config)# access-list 100 permit ip any any\n'
summaries["lab10"] += '<span class="cm">! อนุญาตให้คำขออื่นๆ (เช่น Teacher/Staff ping กัน) ทำงานได้ปกติ</span>\n\n'
summaries["lab10"] += 'Router(config)# interface gigabitEthernet 0/0/0.20\n'
summaries["lab10"] += 'Router(config-subif)# ip access-group 100 in\n'
summaries["lab10"] += '<span class="cm">! นำ ACL เบอร์ 100 ไปบังคับใช้กับทางเข้าของ VLAN 20</span></div></div>'

summaries["lab12"] = '<div class="sc"><h3>LAB-12: EtherChannel</h3><p>ตั้งค่า EtherChannel รวมหลายลิงก์เป็น 1 logical link แล้ว Ping ทดสอบ</p>'
summaries["lab12"] += '<h4>ตัวอย่างคำสั่งใน Lab</h4>'
summaries["lab12"] += '<div class="cb"><span class="cm">! ฝั่ง Switch A</span>\n'
summaries["lab12"] += 'SwitchA(config)# interface range FastEthernet0/1 - 2\n'
summaries["lab12"] += 'SwitchA(config-if-range)# switchport mode trunk\n'
summaries["lab12"] += 'SwitchA(config-if-range)# channel-group 1 mode desirable\n\n'
summaries["lab12"] += '<span class="cm">! ฝั่ง Switch B</span>\n'
summaries["lab12"] += 'SwitchB(config)# interface range FastEthernet0/1 - 2\n'
summaries["lab12"] += 'SwitchB(config-if-range)# switchport mode trunk\n'
summaries["lab12"] += 'SwitchB(config-if-range)# channel-group 1 mode auto\n\n'
summaries["lab12"] += '<span class="cm">! ตรวจสอบผล</span>\n'
summaries["lab12"] += 'SwitchA# show etherchannel summary</div></div>'

# Add leak section
parts.append(f'<section id="mock" class="cs">\n<h2>📝 ข้อสอบจำลอง 30 ข้อ (แนวอาจารย์)</h2>\n{summaries["mock"]}\n</section>\n')
parts.append(f'<section id="leak" class="cs">\n<h2>🎯 เก็งข้อสอบ 100% (จากโพย)</h2>\n{summaries["leak"]}\n</section>\n')

# Build chapter sections with images
for cid, title, img_dir, page_count in chapters:
    parts.append(f'<section id="{cid}" class="cs">\n<h2>{title}</h2>\n')
    parts.append(f'<h3 class="st">Summary</h3>\n{summaries[cid]}\n')
    parts.append(f'<h3 class="st">Slides ({page_count} pages)</h3>\n<div class="sg">\n')
    for p in range(1, page_count+1):
        parts.append(f'<div class="sl"><img src="images/{img_dir}/page_{p:02d}.png" alt="p{p}" loading="lazy"><div class="sn">Slide {p}/{page_count}</div></div>\n')
    parts.append('</div>\n</section>\n')

# Build lab sections with images
for lid, title, img_dir, _ in labs:
    real_dir = os.path.join(img_base, img_dir)
    img_files = sorted(os.listdir(real_dir)) if os.path.exists(real_dir) else []
    parts.append(f'<section id="{lid}" class="cs">\n<h2>{title}</h2>\n')
    parts.append(f'{summaries[lid]}\n')
    if img_files:
        parts.append(f'<h3 class="st">Images ({len(img_files)})</h3>\n<div class="sg">\n')
        for imf in img_files:
            parts.append(f'<div class="sl"><img src="images/{img_dir}/{imf}" alt="{imf}" loading="lazy"><div class="sn">{imf}</div></div>\n')
        parts.append('</div>\n')
    parts.append('</section>\n')

# Close and script
parts.append("""</main>
<div class="mo" onclick="this.classList.remove('act')"><img src="" alt="zoom"></div>
<script>
function go(id){
document.querySelectorAll('.cs').forEach(s=>s.classList.remove('act'));
document.querySelectorAll('.ni').forEach(n=>n.classList.remove('act'));
var s=document.getElementById(id);if(s)s.classList.add('act');
document.querySelectorAll('.ni').forEach(n=>{if(n.getAttribute('onclick').indexOf(id)>-1)n.classList.add('act')});
document.querySelector('.sb').classList.remove('op');
window.scrollTo(0,0);
}
document.addEventListener('click',function(e){
if(e.target.closest('.sl img')){
e.stopPropagation();
var m=document.querySelector('.mo');
m.querySelector('img').src=e.target.src;
m.classList.add('act');
}
});
go('mock');
</script>
</body></html>""")

html = ''.join(parts)
out_path = os.path.join(folder, "exam_summary.html")
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Created: {out_path}")
print(f"Size: {len(html)} chars")
