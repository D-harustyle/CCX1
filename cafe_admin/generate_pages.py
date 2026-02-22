import os
import re

dir_path = "/Users/user/Desktop/@@@@AiDesign/CCX1/cafe_admin"
template_path = os.path.join(dir_path, "member-management.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

pages = [
    {"file": "post.html", "title": "게시글 관리"},
    {"file": "reward.html", "title": "보상 관리"},
    {"file": "settings.html", "title": "운영권한 및 설정"},
    {"file": "comm.html", "title": "커뮤니케이션"},
    {"file": "report.html", "title": "성장 리포트"},
    {"file": "decor.html", "title": "카페 꾸미기"},
    {"file": "biz.html", "title": "카페 비즈센터"},
]

def make_page(page_info):
    html = template_html
    target_file = page_info["file"]
    target_title = page_info["title"]
    
    # 1. Remove active state from member-management
    html = re.sub(r'class="menu-item menu-item--active"', 'class="menu-item"', html)
    html = re.sub(r'class="mobile-nav__item mobile-nav__item--active"', 'class="mobile-nav__item"', html)
    html = html.replace('assets/sidebar-member-active.svg', 'assets/sidebar-member-outlined.svg')
    
    # 2. Add active state to target page
    # Sidebar
    html = re.sub(f'href="{target_file}" class="menu-item(?: menu-item--grey)?"', f'href="{target_file}" class="menu-item menu-item--active"', html)
    # Mobile Nav
    html = re.sub(f'href="{target_file}" class="mobile-nav__item(?: mobile-nav__item--grey)?"', f'href="{target_file}" class="mobile-nav__item mobile-nav__item--active"', html)
    
    # Mobile Icons active state
    icon_map = {
        "post.html": ("sidebar-post-outlined.svg", "sidebar-post-active.svg"),
        "reward.html": ("sidebar-reward-outlined.svg", "sidebar-reward-active.svg"),
        "settings.html": ("sidebar-settings-outlined.svg", "sidebar-settings-active.svg"),
        "comm.html": ("sidebar-comm-outlined.svg", "sidebar-comm-active.svg"),
        "report.html": ("sidebar-report-outlined.svg", "sidebar-report-active.svg"),
        "decor.html": ("sidebar-decor-outlined.svg", "sidebar-decor-active.svg"),
        "biz.html": ("sidebar-biz-outlined.svg", "sidebar-biz-active.svg")
    }
    
    if target_file in icon_map:
        out_svg, act_svg = icon_map[target_file]
        # We need to replace the specific icon inside the active element
        # It's safer to just replace out_svg with act_svg overall if it's inside mobile-nav__item--active
        # But wait, python regex is easier:
        pattern = f'(class="mobile-nav__item mobile-nav__item--active"[^>]*>\\s*<span class="mobile-nav__item-icon"><img src="assets/){out_svg}(")'
        html = re.sub(pattern, f'\\g<1>{act_svg}\\g<2>', html)
    
    # 3. Update breadcrumb
    html = re.sub(f'<span class="breadcrumb__item breadcrumb__item--current">[^<]+</span>', f'<span class="breadcrumb__item breadcrumb__item--current">{target_title}</span>', html)
    
    # 4. Replace main content
    main_start = html.find('<main class="main">')
    main_end = html.find('</main>', main_start)
    
    before_main = html[:main_start]
    after_main = html[main_end:]
    
    new_main = f'''<main class="main">
          <!-- Title -->
          <div class="main__title">
            <h1>{target_title}</h1>
          </div>
          
          <div style="width: 100%; height: 1px; background: rgba(0,0,0,0.06); margin-top: -10px; margin-bottom: 30px;"></div>
          
          <div class="placeholder-content" style="color: #666666; font-size: 14px; line-height: 1.6; letter-spacing: -0.3px;">
            · 카페 관리도구인 'Cafe Studio'의 공간입니다.<br>
            · 빈 페이지 예시이며, 하단은 콘텐츠로 채워질 예정입니다.
          </div>
        '''
        
    final_html = before_main + new_main + after_main
    
    out_path = os.path.join(dir_path, target_file)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

for page in pages:
    make_page(page)

print("Pages created.")
