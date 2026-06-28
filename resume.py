# -*- coding: utf-8 -*-
import streamlit as st

# 页面全局配置
st.set_page_config(
    page_title="个人技术简历 | 技术爱好者",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
# 注入样式，让badge支持自动换行，增加间距更好看
st.markdown("""
<style>
/* 文本允许自动换行 */
div[data-testid="stMarkdown"] p {
    white-space: normal !important;
}
/* 徽章改为行内块，上下左右留边，换行不挤在一起 */
span[class*="badge"] {
    display: inline-block !important;
    margin: 6px 8px 6px 0 !important;
}
</style>
""", unsafe_allow_html=True)
# ====================== 全新改版侧边栏 ======================
with st.sidebar:
    # 顶部头像占位区域
    st.markdown("## 👨‍💻 技术爱好者")
    # 个人定位标签
    st.markdown("""
    <div style="display:flex;flex-wrap:wrap;gap:6px;margin:8px 0;">
        <span style="background:#165DFF;color:white;padding:4px 10px;border-radius:12px;font-size:13px;">后端开发</span>
        <span style="background:#00B42A;color:white;padding:4px 10px;border-radius:12px;font-size:13px;">云原生运维</span>
        <span style="background:#FF7D00;color:white;padding:4px 10px;border-radius:12px;font-size:13px;">嵌入式开发</span>
        <span style="background:#F53F3F;color:white;padding:4px 10px;border-radius:12px;font-size:13px;">机器人仿真</span>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    # 个人简介卡片
    with st.container(border=True):
        st.subheader("📝 个人介绍")
        st.markdown("""
        :orange-badge[:material/star: 哈工程硕士｜5年+互联网｜高校教师]

        """)
        st.markdown("""
            `拥有Java后端、云原生运维、嵌入式单片机、ROS2机器人，可独立完成项目从开发、部署到可视化落地全流程。`
            """)
    st.divider()

    # 技术栈分类卡片 + 对应徽章
    with st.container(border=True):
        st.subheader("🧩 核心技术栈")
        # st.write("后端技术")
        # col1, col2, col3, col4 = st.columns([1, 1.5, 1.5, 1])
        # with col1: st.badge("Java", color="red")
        # with col2: st.badge("SpringBoot", color="orange")
        # with col3: st.badge("MySQL", color="blue")
        # with col4: st.badge("Redis", color="yellow") 
        st.markdown("后端技术：:red-badge[Java] :orange-badge[SpringBoot] :blue-badge[MySQL] :yellow-badge[Redis]")
        st.markdown("云原生运维：:blue-badge[Docker] :violet-badge[K8s] :green-badge[CI/CD]")
        st.markdown("嵌入式 & 机器人：:orange-badge[STM32] :yellow-badge[ESP32] :green-badge[ROS2]")
        st.markdown("脚本 & 可视化：:yellow-badge[Python] :red-badge[Streamlit] :blue-badge[QT]")


    st.divider()

    # 求职方向
    with st.container(border=True):
        st.subheader("🎯 个人爱好")
        st.success("骑行")

    st.divider()
    st.caption("✨ 基于 Streamlit 搭建的个人技能页面")

# 首页头部 + 封面大图
st.title("🚀 技能爱好全景介绍")


# 核心优势模块（优化左右宽度3:2，文字更宽松）
st.subheader("🔥 核心技术优势")
col_text, col_img = st.columns([3, 2])
with col_img:
    st.image("images/cover.png", width='stretch')
with col_text:
    st.markdown("""
<span style="font-weight:bold; color:#2E86AB;">**基础扎实：**</span>精通数据结构与算法，熟练运用各类设计模式，代码功底扎实

<span style="font-weight:bold; color:#A23B72;">**后端全能：**</span>熟练Java生态，掌握主流框架、中间件原理与业务方案设计

<span style="font-weight:bold; color:#F18F01;">**运维落地：**</span>精通容器化、CI/CD流水线搭建，具备企业级部署运维能力

<span style="font-weight:bold; color:#C73E1D;">**跨界开发：**</span>兼顾嵌入式、机器人仿真、上位机、跨端开发，技术覆盖面广

<span style="font-weight:bold; color:#009473;">**自动化能力：**</span>熟练Python脚本开发，可实现业务自动化与数据可视化
""", unsafe_allow_html=True)
st.divider()

# 1. 计算机基础 & 核心编程
st.subheader("💡 一、计算机基础 & 核心编程")
col1, col2 = st.columns(2)
with col1:
    st.success("**算法与架构基础**")
    st.markdown("- 掌握常用数据结构、经典算法\n- 熟练应用各类常见设计模式，优化代码架构")
with col2:
    st.success("**多语言开发能力**")
    st.markdown("- **Java**：熟练语法，精通JVM、JMM、JUC并发编程，掌握Spring、SpringBoot主流框架\n- **C/C++**：了解基础语法，熟练STL标准库，熟悉Boost库基础应用\n- **Python**：熟练基础开发，可独立编写自动化脚本、完成数据处理与业务逻辑开发")

st.divider()

# 2. 后端开发 & 中间件 + 配图
st.subheader("⚙️ 二、后端开发 & 中间件技术")
col_img, col_text = st.columns([1, 3])
with col_img:
    st.image("images/backend.png", width='stretch')
with col_text:
    st.success("**数据库 & 消息队列中间件**")
    st.markdown("""
    - 关系型数据库：熟练 MySQL 使用与原理，可独立设计业务数据库方案、解决业务问题
    - 缓存中间件：精通 Redis、Memcached 原理与实战应用，适配高并发业务场景
    - 消息队列：熟练主流 MQ 使用及底层原理，可基于 MQ 实现业务解耦、异步处理、流量削峰
    """)

st.divider()

# 3. Linux运维 & 云原生 + 配图
st.subheader("🛠️ 三、Linux运维 & 容器化 & CI/CD")
col_img2, col_text2 = st.columns([1, 3])
with col_img2:
    st.image("images/devops.png", width='stretch')
with col_text2:
    st.success("**运维部署 & 自动化流水线**")
    st.markdown("""
    - **Linux体系**：熟练常用Linux命令、Shell脚本编写，了解TCP/IP网络协议，掌握Nginx部署配置、Grafana、Graphite监控工具使用
    - **容器云原生**：熟练 Docker 容器搭建与使用、K8S集群部署运维，掌握 Helm 脚本编写、OpenShift、ArgoCD 持续部署工具
    - **CI/CD流水线**：熟练 Gitlab CI/CD 自动化流水线搭建，实现项目自动化构建、测试、部署
    """)

st.divider()

# 4. 嵌入式 & 机器人 & 上位机 + 配图
st.subheader("🤖 四、嵌入式开发 & 机器人仿真 & 上位机")
col_img3, col_text3 = st.columns([1, 3])
with col_img3:
    st.image("images/embedded.png", width='stretch')
with col_text3:
    st.success("**硬件开发与机器人技术**")
    st.markdown("""
    - **嵌入式开发**：熟练 STM32、ESP32 单片机软件开发，具备嵌入式固件独立开发能力
    - **机器人开发**：掌握 ROS2 机器人仿真环境搭建与仿真开发
    - **上位机开发**：可独立完成 QT 跨平台可视化上位机程序编写，实现数据交互与界面展示
    """)

st.divider()

# 5. 可视化 & 跨端开发 + 配图
st.subheader("📊 五、数据可视化 & 跨端开发")
col_img4, col_text4 = st.columns([1, 3])
with col_img4:
    st.image("images/visual.png", width='stretch')
with col_text4:
    st.success("**前端可视化 & 移动端跨端**")
    st.markdown("""
    - **Streamlit**：熟练使用框架快速搭建数据分析、可视化交互页面，实现数据自动化展示
    - **Flutter**：了解跨平台开发技术，具备移动端/桌面端跨端开发基础能力
    """)

st.divider()

# 整体能力总结
st.subheader("📋 整体能力总结")
st.markdown("""
1. **技术栈全面**：覆盖后端开发、云原生运维、嵌入式开发、机器人仿真、数据可视化多领域
2. **实战能力强**：不止掌握理论知识，可独立完成开发、部署、调试、可视化全流程工作
3. **适配场景广**：可胜任后端开发、运维开发、嵌入式开发、自动化开发等多岗位工作
""")

# 底部水印
st.divider()