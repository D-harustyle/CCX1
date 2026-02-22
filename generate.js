const fs = require('fs');
const path = require('path');
const rootDir = '/Users/user/Desktop/@@@@AiDesign/CCX1';

function walkDir(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        if (file === '.git' || file === 'node_modules' || file === '.cursor' || file === 'generate.js') continue;
        const filePath = path.join(dir, file);
        if (fs.statSync(filePath).isDirectory()) {
            walkDir(filePath, fileList);
        } else {
            if (file.endsWith('.html') && file !== 'index.html') {
                fileList.push(filePath);
            }
        }
    }
    return fileList;
}

const htmlFiles = walkDir(rootDir);
const groups = {};
for (const file of htmlFiles) {
    const relPath = path.relative(rootDir, file);
    const parts = relPath.split(path.sep);
    const folder = parts.length > 1 ? parts[0] : 'Root';
    if (!groups[folder]) groups[folder] = [];
    groups[folder].push(relPath);
}

let html = `<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>하루 AI Design Archive - CCX1</title>
    <style>
        :root {
            --apple-bg: #fbfbfd;
            --apple-card: #ffffff;
            --apple-text: #1d1d1f;
            --apple-secondary: #86868b;
            --apple-blue: #0066cc;
            --apple-blue-hover: #0071e3;
            --apple-border: #d2d2d7;
            --apple-font: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        }

        body { 
            font-family: var(--apple-font);
            background-color: var(--apple-bg);
            color: var(--apple-text);
            margin: 0;
            padding: 0;
            line-height: 1.47059;
            font-weight: 400;
            letter-spacing: -.022em;
            -webkit-font-smoothing: antialiased;
        }

        .container {
            max-width: 980px;
            margin: 0 auto;
            padding: 80px 20px;
        }

        header {
            text-align: center;
            margin-bottom: 60px;
            animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        h1 {
            font-size: 48px;
            line-height: 1.08349;
            font-weight: 600;
            letter-spacing: -.003em;
            margin-bottom: 12px;
            color: var(--apple-text);
        }

        .subtitle {
            font-size: 24px;
            line-height: 1.16667;
            font-weight: 400;
            letter-spacing: .009em;
            color: var(--apple-secondary);
            margin-top: 0;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 24px;
            animation: fadeIn 1.2s ease-out;
        }

        .folder-card {
            background: var(--apple-card);
            border-radius: 18px;
            padding: 32px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.04);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
        }

        .folder-card:hover {
            transform: scale(1.02);
            box-shadow: 0 12px 32px rgba(0,0,0,0.08);
        }

        .folder-title {
            font-size: 21px;
            line-height: 1.19048;
            font-weight: 600;
            letter-spacing: .011em;
            margin-top: 0;
            margin-bottom: 16px;
            color: var(--apple-text);
            text-transform: capitalize;
        }

        ul { 
            list-style-type: none; 
            padding-left: 0; 
            margin: 0;
            flex-grow: 1;
        }

        li { 
            margin-bottom: 12px; 
            border-bottom: 1px solid var(--apple-border);
            padding-bottom: 12px;
        }
        
        li:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }

        a { 
            color: var(--apple-blue); 
            text-decoration: none; 
            font-size: 14px;
            line-height: 1.42859;
            font-weight: 400;
            letter-spacing: -.016em;
            display: inline-flex;
            align-items: center;
            transition: color 0.1s;
            word-break: break-all;
        }

        a:hover { 
            text-decoration: underline;
            color: var(--apple-blue-hover);
        }

        a::after {
            content: '›';
            font-family: var(--apple-font);
            font-size: 18px;
            margin-left: 4px;
            position: relative;
            top: 1px;
            transition: transform 0.2s ease;
            display: inline-block;
        }

        a:hover::after {
            transform: translateX(3px);
            text-decoration: none;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .badge {
            display: inline-block;
            background: #f5f5f7;
            color: var(--apple-secondary);
            font-size: 11px;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: 4px;
            margin-bottom: 12px;
            letter-spacing: .02em;
            align-self: flex-start;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Personal Setup</h1>
            <p class="subtitle">CCX1 Design Archive</p>
        </header>
        <div class="grid">
`;

for (const folder of Object.keys(groups).sort()) {
    html += `            <div class="folder-card">\n`;
    html += `                <div class="badge">Project Folder</div>\n`;
    html += `                <h2 class="folder-title">${folder.replace(/_/g, ' ')}</h2>\n`;
    html += `                <ul>\n`;
    for (const relPath of groups[folder].sort()) {
        const fileName = path.basename(relPath, '.html');
        const href = relPath.split(path.sep).map(p => encodeURIComponent(p)).join('/');
        html += `                    <li><a href="${href}">${fileName}</a></li>\n`;
    }
    html += `                </ul>\n`;
    html += `            </div>\n`;
}

html += `
        </div>
    </div>
</body>
</html>`;

fs.writeFileSync(path.join(rootDir, 'index.html'), html);
console.log('index.html successfully updated.');
