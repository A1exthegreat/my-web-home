#!/usr/bin/env python3
"""生成首页能力雷达图 skill-radar.png（自评，纯 PIL 绘制，无第三方绘图库）"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 560
C = W // 2
R = 185
LABELS = ["计算机网络", "操作系统", "编程实现", "工具链", "科研阅读"]
VALUES = [0.78, 0.86, 0.82, 0.74, 0.66]          # 自评 0~1
N = len(LABELS)

img = Image.new("RGBA", (W, H), (255, 255, 255, 0))
d = ImageDraw.Draw(img)


def font(size, bold=False):
    paths = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-%s.ttc" % ("Bold" if bold else "Regular"),
        "/usr/share/fonts/truetype/arphic/uming.ttc",
    ]
    for p in paths:
        for idx in range(6):
            try:
                return ImageFont.truetype(p, size, index=idx)
            except Exception:
                continue
    return ImageFont.load_default()


def pt(i, ratio):
    ang = -math.pi / 2 + i * 2 * math.pi / N
    return C + R * ratio * math.cos(ang), C + R * ratio * math.sin(ang)


# 网格
for lv in (0.25, 0.5, 0.75, 1.0):
    d.polygon([pt(i, lv) for i in range(N)], outline=(186, 205, 220, 255))
for i in range(N):
    d.line([pt(i, 0), pt(i, 1.0)], fill=(186, 205, 220, 255), width=1)

# 数据多边形
poly = [pt(i, v) for i, v in enumerate(VALUES)]
d.polygon(poly, fill=(20, 184, 196, 74), outline=(18, 111, 181, 255))
d.line(poly + poly[:1], fill=(18, 111, 181, 255), width=3)
for x, y in poly:
    d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(244, 185, 66, 255), outline=(120, 84, 12, 255))

# 标签
f = font(24, bold=True)
for i, lab in enumerate(LABELS):
    x, y = pt(i, 1.22)
    box = d.textbbox((0, 0), lab, font=f)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text((x - w / 2 - box[0], y - h / 2 - box[1]), lab, font=f, fill=(31, 41, 51, 255))

img.save("/home/alex/network/lab1/site/img/skill-radar.png")
print("saved skill-radar.png")
