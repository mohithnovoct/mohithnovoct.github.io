from fasthtml.common import *
from fasthtml import Raw
import json
from pathlib import Path

# FastHTML app with modern styling
app, rt = fast_app(
    pico=True,  # Use Pico CSS for modern styling
    hdrs=(
        Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'),
        Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Meta(name='description', content='Python Programmer & AI Enthusiast — Projects, blog, and contact.'),
        Link(rel='alternate', type='application/rss+xml', title='Mohith Butta — RSS', href='/feed.xml'),
        Link(rel='sitemap', type='application/xml', href='/sitemap.xml'),
        Script(src='https://unpkg.com/htmx.org@1.9.10'),
    )
)

# Load blog posts data
def load_posts():
    try:
        with open('assets/posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

# Load individual blog post content
def load_blog_post(slug):
    try:
        with open(f'_posts/2025-08-19-{slug}.md', 'r', encoding='utf-8') as f:
            content = f.read()
            # Parse frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    body = parts[2].strip()
                    
                    # Simple YAML parsing for frontmatter
                    metadata = {}
                    for line in frontmatter.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip()
                            value = value.strip()
                            if value.startswith('[') and value.endswith(']'):
                                # Parse array
                                value = [item.strip().strip('"\'') for item in value[1:-1].split(',')]
                            elif value.startswith('"') and value.endswith('"'):
                                value = value[1:-1]
                            metadata[key] = value
                    
                    return {
                        'metadata': metadata,
                        'content': body
                    }
    except:
        pass
    return None

# Project data
PROJECTS = [
    {
        'title': 'Stock Market Prediction',
        'description': 'Machine learning model for stock price prediction using historical data and technical indicators.',
        'icon': 'fas fa-chart-line',
        'tech': ['Python', 'Scikit-Learn', 'TensorFlow', 'Pandas', 'Matplotlib', 'Yahoo finance API'],
        'github': 'https://github.com/mohithnovoct/Stock_Market_Prediction'
    },
    {
        'title': 'Credit Card Fraud Detection',
        'description': 'Machine learning system to detect fraudulent credit card transactions using various algorithms.',
        'icon': 'fas fa-credit-card',
        'tech': ['Python', 'scikit-learn', 'NumPy', 'Pandas'],
        'github': 'https://github.com/mohithnovoct/CreditCardFraudDetection'
    },
    {
        'title': 'Web Browser',
        'description': 'A custom web browser implementation with modern features and user-friendly interface.',
        'icon': 'fas fa-globe',
        'tech': ['Python', 'Tkinter', 'WebKit'],
        'github': 'https://github.com/mohithnovoct/Web_Browser'
    },
    {
        'title': 'LostNFound',
        'description': 'A web application for lost and found items with search and matching capabilities.',
        'icon': 'fas fa-search',
        'tech': ['Python', 'Flask', 'SQLite', 'HTML/CSS', 'Django', 'Bootstrap'],
        'github': 'https://github.com/mohithnovoct/LostNFound'
    }
]

# Skills data
SKILLS = {
    'Programming Languages': ['Python', 'HTML5', 'CSS'],
    'Data Science & ML': ['NumPy', 'Pandas', 'Matplotlib', 'Plotly', 'scikit-learn', 'Seaborn'],
    'Databases': ['PostgreSQL', 'MySQL', 'MongoDB', 'SQLite'],
    'Tools & Platforms': ['Git', 'GitHub', 'GitHub Actions', 'Streamlit', 'Flask', 'Django', 'Rest API','MCP','Cursor']
}

# Custom CSS for modern 3D-inspired styling
CUSTOM_CSS = """
:root {
    --primary-color: #00ff88;
    --secondary-color: #00d4ff;
    --accent-color: #ff6b6b;
    --success-color: #00ff88;
    --warning-color: #ffd93d;
    --error-color: #ff4757;
    --background: #ffffff;
    --surface: #f8fafc;
    --text-primary: #1a1a1a;
    --text-secondary: #666666;
    --border: transparent;
    --shadow: rgba(0, 0, 0, 0.05);
    --glass-bg: rgba(255, 255, 255, 0.1);
    --glass-border: rgba(255, 255, 255, 0.2);
}

[data-theme="dark"] {
    --primary-color: #00ff88;
    --secondary-color: #00d4ff;
    --accent-color: #ff6b6b;
    --background: #000000;
    --surface: #111111;
    --text-primary: #ffffff;
    --text-secondary: #cccccc;
    --border: transparent;
    --shadow: rgba(0, 0, 0, 0.5);
    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--background);
    transition: all 0.3s ease;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* 3D Background Effects */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 80%, var(--primary-color) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, var(--secondary-color) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, var(--accent-color) 0%, transparent 50%);
    opacity: 0.1;
    z-index: -1;
    animation: float 20s ease-in-out infinite;
}

[data-theme="dark"] body::before {
    opacity: 0.05;
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}

/* Navigation - Glass Morphism */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    z-index: 1000;
    padding: 1.5rem 0;
    border-bottom: 1px solid var(--glass-border);
    transition: all 0.3s ease;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem;
    gap: 2rem;
}

.nav-logo h2 {
    color: var(--primary-color);
    font-weight: 800;
    margin: 0;
    font-size: 1.5rem;
    text-shadow: 0 0 20px var(--primary-color);
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 1.5rem;
    margin: 0;
    padding: 0;
    align-items: center;
}

.nav-link {
    text-decoration: none;
    color: var(--text-primary);
    font-weight: 600;
    transition: all 0.3s ease;
    padding: 0.8rem 1.5rem;
    border-radius: 12px;
    position: relative;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    overflow: hidden;
}

.nav-link::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.2), transparent);
    transition: left 0.5s;
}

.nav-link:hover::before {
    left: 100%;
}

.nav-link:hover {
    background: rgba(0, 255, 136, 0.1);
    border-color: var(--primary-color);
    color: var(--primary-color);
    transform: translateY(-3px);
    box-shadow: 0 12px 35px rgba(0, 255, 136, 0.25);
}

.nav-link.active {
    background: rgba(0, 255, 136, 0.15);
    border-color: var(--primary-color);
    color: var(--primary-color);
    box-shadow: 0 8px 25px rgba(0, 255, 136, 0.2);
}

.theme-toggle {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    color: var(--text-primary);
    font-size: 1.2rem;
    cursor: pointer;
    padding: 0.8rem;
    border-radius: 50%;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    margin-left: 1rem;
}

.theme-toggle:hover {
    background: var(--primary-color);
    color: var(--background);
    transform: scale(1.1);
    box-shadow: 0 0 30px var(--primary-color);
}

/* Hero Section - 3D Design */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 150px 0 100px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 30% 20%, var(--primary-color) 0%, transparent 40%),
        radial-gradient(circle at 70% 80%, var(--secondary-color) 0%, transparent 40%);
    opacity: 0.1;
    z-index: -1;
}

.hero-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem;
    position: relative;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero-title {
    font-size: 4.5rem;
    font-weight: 900;
    margin-bottom: 1.5rem;
    line-height: 1.1;
    letter-spacing: -0.02em;
}

.highlight {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
    display: inline-block;
}

.highlight::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    border-radius: 2px;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { box-shadow: 0 0 5px var(--primary-color); }
    to { box-shadow: 0 0 20px var(--primary-color), 0 0 30px var(--primary-color); }
}

.hero-subtitle {
    font-size: 1.8rem;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    font-weight: 600;
}

.hero-description {
    font-size: 1.2rem;
    color: var(--text-secondary);
    margin-bottom: 3rem;
    max-width: 600px;
    line-height: 1.7;
}

.hero-buttons {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
}

.btn {
    padding: 1rem 2.5rem;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 700;
    transition: all 0.4s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    border: none;
    cursor: pointer;
    font-size: 1.1rem;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.btn:hover::before {
    left: 100%;
}

.btn-primary {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: var(--background);
    box-shadow: 0 10px 30px rgba(0, 255, 136, 0.3);
}

.btn-primary:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 20px 50px rgba(0, 255, 136, 0.5);
}

.btn-secondary {
    background: var(--glass-bg);
    color: var(--text-primary);
    border: 2px solid var(--glass-border);
    backdrop-filter: blur(10px);
}

.btn-secondary:hover {
    background: var(--primary-color);
    color: var(--background);
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 20px 50px rgba(0, 255, 136, 0.3);
}

/* Profile Card - 3D Glass Effect */
.profile-card {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 3rem;
    border-radius: 30px;
    box-shadow: 
        0 25px 50px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    text-align: center;
    border: 1px solid var(--glass-border);
    position: relative;
    overflow: hidden;
    transform: perspective(1000px) rotateY(-5deg) rotateX(5deg);
    transition: all 0.4s ease;
}

.profile-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, var(--primary-color), transparent);
    opacity: 0.1;
    animation: rotate 10s linear infinite;
    z-index: -1;
}

@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.profile-card:hover {
    transform: perspective(1000px) rotateY(0deg) rotateX(0deg) scale(1.05);
    box-shadow: 
        0 35px 70px rgba(0, 0, 0, 0.2),
        0 0 50px rgba(0, 255, 136, 0.3);
}

.profile-avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin: 0 auto 2rem;
    overflow: hidden;
    border: 4px solid var(--primary-color);
    box-shadow: 
        0 0 30px var(--primary-color),
        0 20px 40px rgba(0, 0, 0, 0.2);
    position: relative;
    transition: all 0.4s ease;
}

.profile-avatar::before {
    content: '';
    position: absolute;
    top: -4px;
    left: -4px;
    right: -4px;
    bottom: -4px;
    border-radius: 50%;
    background: linear-gradient(45deg, var(--primary-color), var(--secondary-color), var(--accent-color));
    z-index: -1;
    animation: rotate 3s linear infinite;
}

.profile-avatar:hover {
    transform: scale(1.1);
    box-shadow: 
        0 0 50px var(--primary-color),
        0 30px 60px rgba(0, 0, 0, 0.3);
}

.profile-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

.social-links {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
}

.social-links a {
    width: 60px;
    height: 60px;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-primary);
    text-decoration: none;
    transition: all 0.4s ease;
    border: 1px solid var(--glass-border);
    position: relative;
    overflow: hidden;
}

.social-links a::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: 50%;
}

.social-links a:hover::before {
    opacity: 1;
}

.social-links a:hover {
    color: var(--background);
    transform: translateY(-5px) scale(1.1);
    box-shadow: 0 15px 30px rgba(0, 255, 136, 0.4);
}

.social-links a i {
    position: relative;
    z-index: 1;
}

/* Sections - 3D Design */
.section {
    padding: 120px 0;
    position: relative;
}

.section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 10% 20%, var(--primary-color) 0%, transparent 30%),
        radial-gradient(circle at 90% 80%, var(--secondary-color) 0%, transparent 30%);
    opacity: 0.03;
    z-index: -1;
}

.section-title {
    font-size: 3.5rem;
    font-weight: 900;
    text-align: center;
    margin-bottom: 4rem;
    color: var(--text-primary);
    position: relative;
    letter-spacing: -0.02em;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 4px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    border-radius: 2px;
    animation: glow 2s ease-in-out infinite alternate;
}

/* About Section */
.about-content {
    max-width: 800px;
    margin: 0 auto;
}

.about-text p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    line-height: 1.8;
}

.skills {
    margin-top: 3rem;
}

.skills h3 {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    color: var(--text-primary);
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.skill-category h4 {
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.skill-tag {
    background: var(--surface);
    color: var(--text-primary);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    border: 1px solid var(--border);
}

/* Projects Section - 3D Cards */
.projects {
    background: var(--surface);
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 3rem;
}

.project-card {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 3rem;
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    border: 1px solid var(--glass-border);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    transform: perspective(1000px) rotateX(5deg);
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: -1;
}

.project-card:hover {
    transform: perspective(1000px) rotateX(0deg) translateY(-10px) scale(1.02);
    box-shadow: 
        0 30px 60px rgba(0, 0, 0, 0.2),
        0 0 50px rgba(0, 255, 136, 0.3);
}

.project-card:hover::before {
    opacity: 0.05;
}

.project-icon {
    width: 80px;
    height: 80px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: var(--background);
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0, 255, 136, 0.3);
    position: relative;
    overflow: hidden;
}

.project-icon::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: shine 3s ease-in-out infinite;
}

@keyframes shine {
    0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    50% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    100% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
}

.project-content h3 {
    font-size: 1.6rem;
    margin-bottom: 1.5rem;
    color: var(--text-primary);
    font-weight: 800;
}

.project-content p {
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.7;
    font-size: 1.1rem;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-bottom: 2rem;
}

.tech-tag {
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    color: var(--text-primary);
    padding: 0.5rem 1.2rem;
    border-radius: 25px;
    font-size: 0.9rem;
    border: 1px solid var(--glass-border);
    transition: all 0.3s ease;
}

.tech-tag:hover {
    background: var(--primary-color);
    color: var(--background);
    transform: translateY(-2px);
}

.project-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    transition: all 0.3s ease;
    padding: 1rem 2rem;
    border-radius: 50px;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.project-link:hover {
    background: var(--primary-color);
    color: var(--background);
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(0, 255, 136, 0.4);
}

/* Blog Section */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.blog-card {
    background: var(--background);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 30px var(--shadow);
    border: 1px solid var(--border);
    transition: all 0.3s ease;
}

.blog-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px var(--shadow);
}

.blog-image {
    height: 200px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    color: white;
}

.blog-content {
    padding: 1.5rem;
}

.blog-meta {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}

.blog-date, .blog-category {
    font-size: 0.9rem;
    color: var(--text-secondary);
}

.blog-category {
    color: var(--primary-color);
    font-weight: 600;
}

.blog-content h3 {
    font-size: 1.2rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.blog-content p {
    color: var(--text-secondary);
    margin-bottom: 1rem;
    line-height: 1.6;
}

.read-more {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.3s ease;
}

.read-more:hover {
    color: var(--secondary-color);
}

/* Contact Section */
.contact {
    background: var(--surface);
}

.contact-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    max-width: 1000px;
    margin: 0 auto;
}

.contact-info h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.contact-info p {
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.6;
}

.contact-links {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.contact-link {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: var(--text-primary);
    text-decoration: none;
    padding: 1rem;
    border-radius: 8px;
    background: var(--background);
    border: 1px solid var(--border);
    transition: all 0.3s ease;
}

.contact-link:hover {
    background: var(--primary-color);
    color: white;
    transform: translateX(5px);
}

.contact-form {
    background: var(--background);
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px var(--shadow);
    border: 1px solid var(--border);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 1rem;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: var(--background);
    color: var(--text-primary);
    font-family: inherit;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
}

/* Footer */
.footer {
    background: var(--background);
    padding: 2rem 0;
    border-top: 1px solid var(--border);
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.footer-content p {
    color: var(--text-secondary);
    margin: 0;
}

.footer-links {
    display: flex;
    gap: 2rem;
}

.footer-links a {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-links a:hover {
    color: var(--primary-color);
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-menu {
        display: none;
    }
    
    .hero-container {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 3rem;
    }
    
    .hero-title {
        font-size: 3rem;
    }
    
    .hero-buttons {
        justify-content: center;
    }
    
    .contact-content {
        grid-template-columns: 1fr;
        gap: 3rem;
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
    }
    
    .blog-grid {
        grid-template-columns: 1fr;
    }
    
    .skills-grid {
        grid-template-columns: 1fr;
    }
    
    .footer-content {
        flex-direction: column;
        text-align: center;
    }
    
    .profile-card {
        transform: perspective(1000px) rotateY(0deg) rotateX(0deg);
    }
    
    .project-card {
        transform: perspective(1000px) rotateX(0deg);
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 1rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .section-title {
        font-size: 2.5rem;
    }
    
    .btn {
        padding: 0.8rem 1.5rem;
        font-size: 1rem;
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .project-card {
        padding: 2rem;
    }
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.project-card,
.blog-card {
    animation: fadeInUp 0.6s ease-out;
}

/* Theme Transition */
body,
.navbar,
.project-card,
.blog-card,
.contact-form,
.profile-card {
    transition: all 0.3s ease;
}
"""

# Main route - Homepage
@rt
def index():
    posts = load_posts()
    latest_posts = posts[:3] if posts else []
    
    return Titled(
        "Mohith Butta - Portfolio",
        Style(CUSTOM_CSS),
        
        # Navigation
        Nav(
            Div(
                Div(H2("Mohith Butta", cls="nav-logo")),
                Ul(
                    Li(A("Home", href="#home", cls="nav-link")),
                    Li(A("About", href="#about", cls="nav-link")),
                    Li(A("Projects", href="#projects", cls="nav-link")),
                    Li(A("Blog", href="#blog", cls="nav-link")),
                    Li(A("Contact", href="#contact", cls="nav-link")),
                    cls="nav-menu"
                ),
                Button(
                    I(cls="fas fa-moon"),
                    cls="theme-toggle",
                    id="theme-toggle",
                    onclick="toggleTheme()"
                ),
                cls="nav-container"
            ),
            cls="navbar"
        ),
        
        # Hero Section
        Section(
            Div(
                Div(
                    H1("Hi, I'm ", Span("Mohith Butta", cls="highlight"), cls="hero-title"),
                    P("Python Programmer & AI Enthusiast", cls="hero-subtitle"),
                    P("Building intelligent solutions and exploring the world of machine learning", cls="hero-description"),
                    Div(
                        A("View Projects", href="#projects", cls="btn btn-primary"),
                        A(
                            I(cls="fas fa-download"),
                            " Download Resume",
                            href="Mohith_Butta-Resume.pdf",
                            cls="btn btn-secondary",
                            download=True
                        ),
                        cls="hero-buttons"
                    ),
                    cls="hero-content"
                ),
                Div(
                    Div(
                        Div(
                            Img(src="profile-image.jpg", alt="Mohith Butta", cls="profile-image"),
                            cls="profile-avatar"
                        ),
                        Div(
                            A(I(cls="fab fa-github"), href="https://github.com/mohithnovoct", target="_blank"),
                            A(I(cls="fab fa-linkedin"), href="https://www.linkedin.com/in/mohith-butta-472543285", target="_blank"),
                            A(I(cls="fab fa-twitter"), href="https://x.com/mohith_butta", target="_blank"),
                            cls="social-links"
                        ),
                        cls="profile-card"
                    ),
                    cls="hero-image"
                ),
                cls="hero-container"
            ),
            id="home",
            cls="hero"
        ),
        
        # About Section
        Section(
            Div(
                H2("About Me", cls="section-title"),
                Div(
                    Div(
                        P("I'm a self-taught programmer passionate about Python and artificial intelligence. Currently focused on Deep learning and Generative AI to build intelligent solutions."),
                        P("Based in Bangalore, I love collaborating on projects and exploring new technologies in the AI space."),
                        Div(
                            H3("Tech Stack"),
                            Div(
                                *[
                                    Div(
                                        H4(category),
                                        Div(
                                            *[Span(skill, cls="skill-tag") for skill in skills],
                                            cls="skill-tags"
                                        ),
                                        cls="skill-category"
                                    )
                                    for category, skills in SKILLS.items()
                                ],
                                cls="skills-grid"
                            ),
                            cls="skills"
                        ),
                        cls="about-text"
                    ),
                    cls="about-content"
                ),
                cls="container"
            ),
            id="about",
            cls="section about"
        ),
        
        # Projects Section
        Section(
            Div(
                H2("Featured Projects", cls="section-title"),
                Div(
                    *[
                        Div(
                            Div(I(cls=project['icon']), cls="project-icon"),
                            Div(
                                H3(project['title']),
                                P(project['description']),
                                Div(
                                    *[Span(tech, cls="tech-tag") for tech in project['tech']],
                                    cls="project-tech"
                                ),
                                A(
                                    I(cls="fab fa-github"),
                                    " View Code",
                                    href=project['github'],
                                    target="_blank",
                                    cls="project-link"
                                ),
                                cls="project-content"
                            ),
                            cls="project-card"
                        )
                        for project in PROJECTS
                    ],
                    cls="projects-grid"
                ),
                cls="container"
            ),
            id="projects",
            cls="section projects"
        ),
        
        # Blog Section
        Section(
            Div(
                H2("Latest Blog Posts", cls="section-title"),
                Div(
                    *[
                        Article(
                            Div(I(cls="fas fa-file-alt"), cls="blog-image"),
                            Div(
                                Div(
                                    Span(post['prettyDate'], cls="blog-date"),
                                    Span(post['category'], cls="blog-category") if post.get('category') else "",
                                    cls="blog-meta"
                                ),
                                H3(post['title']),
                                P(post['description']),
                                A("Read More →", href=f"/blog/{post['slug']}", cls="read-more"),
                                cls="blog-content"
                            ),
                            cls="blog-card"
                        )
                        for post in latest_posts
                    ],
                    cls="blog-grid"
                ),
                Div(
                    A("View All Posts", href="/blog/", cls="btn btn-primary"),
                    style="text-align: center; margin-top: 1rem;"
                ),
                cls="container"
            ),
            id="blog",
            cls="section blog"
        ),
        
        # Contact Section
        Section(
            Div(
                H2("Get In Touch", cls="section-title"),
                Div(
                    Div(
                        H3("Let's Connect"),
                        P("I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology and AI."),
                        Div(
                            A(
                                I(cls="fas fa-envelope"),
                                Span("mohithbutta4002@gmail.com"),
                                href="mailto:mohithbutta4002@gmail.com",
                                cls="contact-link"
                            ),
                            A(
                                I(cls="fab fa-github"),
                                Span("github.com/mohithnovoct"),
                                href="https://github.com/mohithnovoct",
                                target="_blank",
                                cls="contact-link"
                            ),
                            A(
                                I(cls="fab fa-linkedin"),
                                Span("linkedin.com/in/mohith-butta"),
                                href="https://www.linkedin.com/in/mohith-butta-472543285",
                                target="_blank",
                                cls="contact-link"
                            ),
                            A(
                                I(cls="fab fa-twitter"),
                                Span("@mohith_butta"),
                                href="https://x.com/mohith_butta",
                                target="_blank",
                                cls="contact-link"
                            ),
                            cls="contact-links"
                        ),
                        cls="contact-info"
                    ),
                    Form(
                        Div(
                            Input(type="text", name="name", placeholder="Your Name", required=True, cls="form-group"),
                            Input(type="email", name="email", placeholder="Your Email", required=True, cls="form-group"),
                            Input(type="text", name="subject", placeholder="Subject", required=True, cls="form-group"),
                            Textarea(name="message", placeholder="Your Message", rows=5, required=True, cls="form-group"),
                            Button("Send Message", type="submit", cls="btn btn-primary"),
                            hx_post="/contact",
                            hx_target="#contact-form",
                            hx_swap="outerHTML"
                        ),
                        id="contact-form",
                        cls="contact-form"
                    ),
                    cls="contact-content"
                ),
                cls="container"
            ),
            id="contact",
            cls="section contact"
        ),
        
        # Footer
        Footer(
            Div(
                Div(
                    P("© 2024 Mohith Butta. All rights reserved."),
                    Div(
                        A("Home", href="#home"),
                        A("About", href="#about"),
                        A("Projects", href="#projects"),
                        A("Blog", href="#blog"),
                        A("Contact", href="#contact"),
                        cls="footer-links"
                    ),
                    cls="footer-content"
                ),
                cls="container"
            ),
            cls="footer"
        ),
        
        # JavaScript for theme toggle and interactions
        Script("""
            // Theme Management
            let currentTheme = localStorage.getItem('theme') || 'light';
            
            function initTheme() {
                if (currentTheme === 'dark') {
                    document.body.setAttribute('data-theme', 'dark');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
                } else {
                    document.body.setAttribute('data-theme', 'light');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
                }
            }
            
            function toggleTheme() {
                if (currentTheme === 'light') {
                    currentTheme = 'dark';
                    document.body.setAttribute('data-theme', 'dark');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
                } else {
                    currentTheme = 'light';
                    document.body.setAttribute('data-theme', 'light');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
                }
                localStorage.setItem('theme', currentTheme);
            }
            
            // Smooth scrolling for navigation links
            document.querySelectorAll('.nav-link').forEach(link => {
                link.addEventListener('click', (e) => {
                    const href = link.getAttribute('href');
                    if (href.startsWith('#')) {
                        e.preventDefault();
                        
                        // Remove active class from all nav links
                        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
                        // Add active class to clicked link
                        link.classList.add('active');
                        
                        const targetSection = document.querySelector(href);
                        if (targetSection) {
                            const offsetTop = targetSection.offsetTop - 80;
                            window.scrollTo({ top: offsetTop, behavior: 'smooth' });
                        }
                    }
                });
            });
            
            // Update active nav link on scroll
            function updateActiveNavLink() {
                const sections = document.querySelectorAll('section[id]');
                const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
                
                let current = '';
                sections.forEach(section => {
                    const sectionTop = section.offsetTop - 100;
                    const sectionHeight = section.clientHeight;
                    if (window.pageYOffset >= sectionTop && window.pageYOffset < sectionTop + sectionHeight) {
                        current = section.getAttribute('id');
                    }
                });
                
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${current}`) {
                        link.classList.add('active');
                    }
                });
            }
            
            // Listen for scroll events
            window.addEventListener('scroll', updateActiveNavLink);
            
            // Initialize theme on page load
            document.addEventListener('DOMContentLoaded', initTheme);
            
            // Navbar scroll effect
            let lastScrollTop = 0;
            window.addEventListener('scroll', () => {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const navbar = document.querySelector('.navbar');
                
                if (scrollTop > lastScrollTop && scrollTop > 100) {
                    navbar.style.transform = 'translateY(-100%)';
                } else {
                    navbar.style.transform = 'translateY(0)';
                }
                
                lastScrollTop = scrollTop;
            });
        """)
    )

# Contact form handler
@rt
def contact(name: str, email: str, subject: str, message: str):
    # Here you would typically send an email or save to database
    # For now, we'll just return a success message
    return Div(
        Div(
            P("Message sent successfully! I'll get back to you soon.", style="color: var(--success-color); font-weight: 600;"),
            Button("Send Another Message", onclick="location.reload()", cls="btn btn-primary"),
            style="text-align: center; padding: 2rem;"
        ),
        id="contact-form",
        cls="contact-form"
    )

# Blog route
@rt
def blog():
    posts = load_posts()
    
    return Titled(
        "Blog - Mohith Butta",
        Style(CUSTOM_CSS),
        
        # Navigation (same as homepage)
        Nav(
            Div(
                Div(A("Mohith Butta", href="/", cls="nav-logo")),
                Ul(
                    Li(A("Home", href="/", cls="nav-link")),
                    Li(A("About", href="/#about", cls="nav-link")),
                    Li(A("Projects", href="/#projects", cls="nav-link")),
                    Li(A("Blog", href="/blog", cls="nav-link")),
                    Li(A("Contact", href="/#contact", cls="nav-link")),
                    cls="nav-menu"
                ),
                Button(
                    I(cls="fas fa-moon"),
                    cls="theme-toggle",
                    id="theme-toggle",
                    onclick="toggleTheme()"
                ),
                cls="nav-container"
            ),
            cls="navbar"
        ),
        
        # Blog content
        Section(
            Div(
                H1("Blog Posts", cls="section-title"),
                Div(
                    *[
                        Article(
                            Div(I(cls="fas fa-file-alt"), cls="blog-image"),
                            Div(
                                Div(
                                    Span(post['prettyDate'], cls="blog-date"),
                                    Span(post['category'], cls="blog-category") if post.get('category') else "",
                                    cls="blog-meta"
                                ),
                                H3(post['title']),
                                P(post['description']),
                                A("Read More →", href=f"/blog/{post['slug']}", cls="read-more"),
                                cls="blog-content"
                            ),
                            cls="blog-card"
                        )
                        for post in posts
                    ],
                    cls="blog-grid"
                ),
                cls="container"
            ),
            style="padding: 120px 0 80px;"
        ),
        
        # Footer
        Footer(
            Div(
                Div(
                    P("© 2024 Mohith Butta. All rights reserved."),
                    cls="footer-content"
                ),
                cls="container"
            ),
            cls="footer"
        ),
        
        # Same JavaScript as homepage
        Script("""
            let currentTheme = localStorage.getItem('theme') || 'light';
            
            function initTheme() {
                if (currentTheme === 'dark') {
                    document.body.setAttribute('data-theme', 'dark');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
                } else {
                    document.body.setAttribute('data-theme', 'light');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
                }
            }
            
            function toggleTheme() {
                if (currentTheme === 'light') {
                    currentTheme = 'dark';
                    document.body.setAttribute('data-theme', 'dark');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
                } else {
                    currentTheme = 'light';
                    document.body.setAttribute('data-theme', 'light');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
                }
                localStorage.setItem('theme', currentTheme);
            }
            
            document.addEventListener('DOMContentLoaded', initTheme);
            
            // Set active nav link for blog page
            document.addEventListener('DOMContentLoaded', () => {
                const blogLink = document.querySelector('.nav-link[href="/blog"]');
                if (blogLink) {
                    blogLink.classList.add('active');
                }
            });
        """)
    )

# Individual blog post route
@rt
def blog_post(slug: str):
    post_data = load_blog_post(slug)
    
    if not post_data:
        return Titled(
            "Post Not Found - Mohith Butta",
            Style(CUSTOM_CSS),
            Div(
                H1("Post Not Found"),
                P("The blog post you're looking for doesn't exist."),
                A("← Back to Blog", href="/blog", cls="btn btn-primary"),
                style="text-align: center; padding: 4rem 2rem;"
            )
        )
    
    metadata = post_data['metadata']
    content = post_data['content']
    
    # Convert markdown to HTML (simple conversion)
    html_content = content.replace('\n\n', '</p><p>').replace('\n', '<br>')
    html_content = f'<p>{html_content}</p>'
    
    # Convert code blocks
    import re
    html_content = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code class="language-\1">\2</code></pre>', html_content, flags=re.DOTALL)
    html_content = re.sub(r'`([^`]+)`', r'<code>\1</code>', html_content)
    
    # Convert headers
    html_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    
    # Convert lists
    html_content = re.sub(r'^- (.*?)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', html_content, flags=re.DOTALL)
    
    return Titled(
        f"{metadata.get('title', 'Blog Post')} - Mohith Butta",
        Style(CUSTOM_CSS),
        
        # Navigation
        Nav(
            Div(
                Div(A("Mohith Butta", href="/", cls="nav-logo")),
                Ul(
                    Li(A("Home", href="/", cls="nav-link")),
                    Li(A("About", href="/#about", cls="nav-link")),
                    Li(A("Projects", href="/#projects", cls="nav-link")),
                    Li(A("Blog", href="/blog", cls="nav-link")),
                    Li(A("Contact", href="/#contact", cls="nav-link")),
                    cls="nav-menu"
                ),
                Button(
                    I(cls="fas fa-moon"),
                    cls="theme-toggle",
                    id="theme-toggle",
                    onclick="toggleTheme()"
                ),
                cls="nav-container"
            ),
            cls="navbar"
        ),
        
        # Blog post content
        Section(
            Div(
                Div(
                    A("← Back to Blog", href="/blog", cls="btn btn-secondary", style="margin-bottom: 2rem;"),
                    H1(metadata.get('title', 'Blog Post'), style="margin-bottom: 1rem;"),
                    Div(
                        Span(metadata.get('date', ''), cls="blog-date"),
                        *[Span(tag, cls="blog-category") for tag in metadata.get('tags', [])],
                        cls="blog-meta",
                        style="margin-bottom: 2rem;"
                    ),
                    Div(
                        Raw(html_content),
                        style="line-height: 1.8; font-size: 1.1rem;"
                    ),
                    cls="blog-content"
                ),
                cls="container",
                style="max-width: 800px; padding: 120px 2rem 80px;"
            )
        ),
        
        # Footer
        Footer(
            Div(
                Div(
                    P("© 2024 Mohith Butta. All rights reserved."),
                    cls="footer-content"
                ),
                cls="container"
            ),
            cls="footer"
        ),
        
        # JavaScript
        Script("""
            let currentTheme = localStorage.getItem('theme') || 'light';
            
            function initTheme() {
                if (currentTheme === 'dark') {
                    document.body.setAttribute('data-theme', 'dark');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
                } else {
                    document.body.setAttribute('data-theme', 'light');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
                }
            }
            
            function toggleTheme() {
                if (currentTheme === 'light') {
                    currentTheme = 'dark';
                    document.body.setAttribute('data-theme', 'dark');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
                } else {
                    currentTheme = 'light';
                    document.body.setAttribute('data-theme', 'light');
                    document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
                }
                localStorage.setItem('theme', currentTheme);
            }
            
            document.addEventListener('DOMContentLoaded', initTheme);
            
            // Set active nav link for blog page
            document.addEventListener('DOMContentLoaded', () => {
                const blogLink = document.querySelector('.nav-link[href="/blog"]');
                if (blogLink) {
                    blogLink.classList.add('active');
                }
            });
        """)
    )

# Serve the application
if __name__ == "__main__":
    serve()
