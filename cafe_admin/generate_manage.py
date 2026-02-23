import os
import re

dir_path = "/Users/user/Desktop/@@@@AiDesign/CCX1/cafe_admin"
template_path = os.path.join(dir_path, "member-management.html")
target_path = os.path.join(dir_path, "cafe_manage.html")

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update active state from member-management to cafe_manage
html = re.sub(r'class="menu-item menu-item--active"', 'class="menu-item"', html)
html = re.sub(r'class="mobile-nav__item mobile-nav__item--active"', 'class="mobile-nav__item"', html)
html = html.replace('assets/sidebar-member-active.svg', 'assets/sidebar-member-outlined.svg')

html = re.sub(r'href="cafe_manage.html" class="menu-item(?: menu-item--grey)?"', 'href="cafe_manage.html" class="menu-item menu-item--active"', html)
html = re.sub(r'href="cafe_manage.html" class="mobile-nav__item(?: mobile-nav__item--grey)?"', 'href="cafe_manage.html" class="mobile-nav__item mobile-nav__item--active"', html)
# Switch mobile icon
pattern = r'(class="mobile-nav__item mobile-nav__item--active"[^>]*>\s*<span class="mobile-nav__item-icon"><img src="assets/)sidebar-cafe-outlined\.svg(")'
html = re.sub(pattern, r'\g<1>sidebar-cafe-active.svg\g<2>', html)

# 2. Update breadcrumb
html = re.sub(r'<span class="breadcrumb__item breadcrumb__item--current">[^<]+</span>', r'<span class="breadcrumb__item breadcrumb__item--current">카페 운영</span>', html)

# 3. Main content replacement
main_start = html.find('<main class="main">')
main_end = html.find('</main>', main_start)

before_main = html[:main_start]
after_main = html[main_end:]

new_main = '''<main class="main">
          <!-- Title -->
          <div class="main__title">
            <h1>카페 운영</h1>
          </div>
          
          <!-- Keep the line, drop the tabs -->
          <div style="width: 100%; height: 1px; background: rgba(0,0,0,0.06); margin-top: -10px; margin-bottom: 30px;"></div>
          
          <div class="placeholder-content" style="flex: 1; display: flex; flex-direction: column;">
            <div style="color: #666666; font-size: 14px; line-height: 1.6; letter-spacing: -0.3px;">
              · 카페 관리도구인 'Cafe Studio'의 공간입니다.<br>
              · 하단은 콘텐츠로 채워질 예정입니다.
            </div>
            <div style="flex: 1;"></div> <!-- spacer to push footer down -->
          </div>
          
          <!-- Footer -->
          <footer class="footer" style="margin-top: auto; padding-top: 32px;">
            <span class="footer__copyright">Since 2023.10.10. &copy;&nbsp;감스트</span>
            <div class="footer__links">
              <a href="#" class="footer__link">네이버 이용약관</a>
              <span class="footer__link-divider"></span>
              <a href="#" class="footer__link">카페 비즈센터 이용약관</a>
              <span class="footer__link-divider"></span>
              <a href="#" class="footer__link">카페 비즈센터 운영정책</a>
              <span class="footer__link-divider"></span>
              <a href="#" class="footer__link">개인정보 처리 방침</a>
              <span class="footer__link-divider"></span>
              <a href="#" class="footer__link">고객센터</a>
            </div>
          </footer>
'''

# To ensure the footer sticks to bottom if `.main` is a flex container, let's inject a fix into body or content if needed.
# Since `.content` is `flex: 1` and `.main` isn't `flex: 1` by default, let's explicitly add style to `.main` via regex or inline.
final_main = new_main.replace('<main class="main">', '<main class="main" style="display: flex; flex-direction: column; flex: 1; min-height: 0;">')

html = before_main + final_main + after_main

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("cafe_manage.html created/updated successfully.")
