# my-web-home · 崔嘉洋的个人小站

计算机网络课程 **实验一：静态网页制作** 的成品站点（纯 HTML5 + CSS3 手写，不使用任何前端框架）。

- 在线地址：<https://a1exthegreat.github.io/my-web-home/>
- 页面：首页(自我简介) / 科大印象 / 研究分享 / 博客 / HTTP 观察
- 部署：GitHub Pages（仓库根目录，`main` 分支）

## 目录结构

```
├── index.html      首页 / 自我简介
├── ustc.html       科大印象
├── research.html   研究分享
├── blog.html       博客（实验过程中新发布的一篇博文）
├── http.html       该站点的 HTTP 版本观测记录
├── css/style.css   全站样式表（CSS 变量 + Grid + 响应式）
├── img/            自制 SVG 插画 + PIL 生成的 PNG
└── tools/          生成雷达图的 Python 脚本
```

## 本地预览

```bash
python3 -m http.server 8099   # 然后访问 http://127.0.0.1:8099
```
