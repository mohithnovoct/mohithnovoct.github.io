#!/usr/bin/env python3
"""
Static site generator for GitHub Pages deployment
Converts FastHTML app to static HTML files
"""

import os
import json
import re
from pathlib import Path

def load_posts():
    """Load blog posts data"""
    try:
        with open('assets/posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def load_blog_post(slug):
    """Load individual blog post content"""
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

def convert_markdown_to_html(content):
    """Convert markdown to HTML"""
    # Convert code blocks
    content = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code class="language-\1">\2</code></pre>', content, flags=re.DOTALL)
    content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
    
    # Convert headers
    content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    
    # Convert lists
    content = re.sub(r'^- (.*?)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', content, flags=re.DOTALL)
    
    # Convert paragraphs
    content = content.replace('\n\n', '</p><p>').replace('\n', '<br>')
    content = f'<p>{content}</p>'
    
    return content

def generate_homepage():
    """Generate homepage HTML"""
    posts = load_posts()
    latest_posts = posts[:3] if posts else []
    
    # Read the CSS from app.py
    css_content = ""
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract CSS from CUSTOM_CSS variable
            start = content.find('CUSTOM_CSS = """')
            if start != -1:
                start += len('CUSTOM_CSS = """')
                end = content.find('"""', start)
                if end != -1:
                    css_content = content[start:end]
    except:
        pass
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mohith Butta - Portfolio</title>
    <meta name="description" content="Python Programmer & AI Enthusiast — Projects, blog, and contact.">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="alternate" type="application/rss+xml" title="Mohith Butta — RSS" href="/feed.xml">
    <link rel="sitemap" type="application/xml" href="/sitemap.xml">
    <style>{css_content}</style>
</head>
<body class="light-mode">
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2>Mohith Butta</h2>
            </div>
            <ul class="nav-menu">
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#blog" class="nav-link">Blog</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-toggle">
                <button id="theme-toggle" class="theme-btn">
                    <i class="fas fa-moon"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1 class="hero-title">Hi, I'm <span class="highlight">Mohith Butta</span></h1>
                <p class="hero-subtitle">Python Programmer & AI Enthusiast</p>
                <p class="hero-description">Building intelligent solutions and exploring the world of machine learning</p>
                <div class="hero-buttons">
                    <a href="#projects" class="btn btn-primary">View Projects</a>
                    <a href="Mohith_Butta-Resume.pdf" class="btn btn-secondary" download>
                        <i class="fas fa-download"></i> Download Resume
                    </a>
                </div>
            </div>
            <div class="hero-image">
                <div class="profile-card">
                    <div class="profile-avatar">
                        <img src="profile-image.jpg" alt="Mohith Butta" class="profile-image">
                    </div>
                    <div class="social-links">
                        <a href="https://github.com/mohithnovoct" target="_blank"><i class="fab fa-github"></i></a>
                        <a href="https://www.linkedin.com/in/mohith-butta-472543285" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://x.com/mohith_butta" target="_blank"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>I'm a self-taught programmer passionate about Python and artificial intelligence. Currently focused on Deep learning and Generative AI to build intelligent solutions.</p>
                    <p>Based in Bangalore, I love collaborating on projects and exploring new technologies in the AI space.</p>
                    
                    <div class="skills">
                        <h3>Tech Stack</h3>
                        <div class="skills-grid">
                            <div class="skill-category">
                                <h4>Programming Languages</h4>
                                <div class="skill-tags">
                                    <span class="skill-tag">Python</span>
                                    <span class="skill-tag">HTML5</span>
                                    <span class="skill-tag">CSS</span>
                                </div>
                            </div>
                            <div class="skill-category">
                                <h4>Data Science & ML</h4>
                                <div class="skill-tags">
                                    <span class="skill-tag">NumPy</span>
                                    <span class="skill-tag">Pandas</span>
                                    <span class="skill-tag">Matplotlib</span>
                                    <span class="skill-tag">Plotly</span>
                                    <span class="skill-tag">scikit-learn</span>
                                    <span class="skill-tag">Seaborn</span>
                                </div>
                            </div>
                            <div class="skill-category">
                                <h4>Databases</h4>
                                <div class="skill-tags">
                                    <span class="skill-tag">PostgreSQL</span>
                                    <span class="skill-tag">MySQL</span>
                                    <span class="skill-tag">MongoDB</span>
                                    <span class="skill-tag">SQLite</span>
                                </div>
                            </div>
                            <div class="skill-category">
                                <h4>Tools & Platforms</h4>
                                <div class="skill-tags">
                                    <span class="skill-tag">Git</span>
                                    <span class="skill-tag">GitHub</span>
                                    <span class="skill-tag">GitHub Actions</span>
                                    <span class="skill-tag">Streamlit</span>
                                    <span class="skill-tag">Flask</span>
                                    <span class="skill-tag">Django</span>
                                    <span class="skill-tag">Rest API</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <h2 class="section-title">Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="project-content">
                        <h3>Stock Market Prediction</h3>
                        <p>Machine learning model for stock price prediction using historical data and technical indicators.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Scikit-Learn</span>
                            <span class="tech-tag">TensorFlow</span>
                            <span class="tech-tag">Pandas</span>
                            <span class="tech-tag">Matplotlib</span>
                            <span class="tech-tag">Yahoo finance API</span>
                        </div>
                        <div class="project-links">
                            <a href="https://github.com/mohithnovoct/Stock_Market_Prediction" target="_blank" class="project-link">
                                <i class="fab fa-github"></i> View Code
                            </a>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-icon">
                        <i class="fas fa-credit-card"></i>
                    </div>
                    <div class="project-content">
                        <h3>Credit Card Fraud Detection</h3>
                        <p>Machine learning system to detect fraudulent credit card transactions using various algorithms.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">scikit-learn</span>
                            <span class="tech-tag">NumPy</span>
                            <span class="tech-tag">Pandas</span>
                        </div>
                        <div class="project-links">
                            <a href="https://github.com/mohithnovoct/CreditCardFraudDetection" target="_blank" class="project-link">
                                <i class="fab fa-github"></i> View Code
                            </a>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-icon">
                        <i class="fas fa-globe"></i>
                    </div>
                    <div class="project-content">
                        <h3>Web Browser</h3>
                        <p>A custom web browser implementation with modern features and user-friendly interface.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Tkinter</span>
                            <span class="tech-tag">WebKit</span>
                        </div>
                        <div class="project-links">
                            <a href="https://github.com/mohithnovoct/Web_Browser" target="_blank" class="project-link">
                                <i class="fab fa-github"></i> View Code
                            </a>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="project-content">
                        <h3>LostNFound</h3>
                        <p>A web application for lost and found items with search and matching capabilities.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Flask</span>
                            <span class="tech-tag">SQLite</span>
                            <span class="tech-tag">HTML/CSS</span>
                            <span class="tech-tag">Django</span>
                            <span class="tech-tag">Bootstrap</span>
                        </div>
                        <div class="project-links">
                            <a href="https://github.com/mohithnovoct/LostNFound" target="_blank" class="project-link">
                                <i class="fab fa-github"></i> View Code
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Blog Section -->
    <section id="blog" class="blog">
        <div class="container">
            <h2 class="section-title">Latest Blog Posts</h2>
            <div id="latest-posts" class="blog-grid">
                {''.join([f'''
                <article class="blog-card">
                    <div class="blog-image">
                        <i class="fas fa-file-alt"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="blog-date">{post['prettyDate']}</span>
                            <span class="blog-category">{post.get('category', 'blog')}</span>
                        </div>
                        <h3>{post['title']}</h3>
                        <p>{post['description']}</p>
                        <a href="/blog/{post['slug']}" class="read-more">Read More →</a>
                    </div>
                </article>
                ''' for post in latest_posts])}
            </div>
            <div style="text-align:center;margin-top:1rem;">
                <a href="/blog/" class="btn btn-primary">View All Posts</a>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <div class="contact-content">
                <div class="contact-info">
                    <h3>Let's Connect</h3>
                    <p>I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology and AI.</p>
                    <div class="contact-links">
                        <a href="mailto:mohithbutta4002@gmail.com" class="contact-link">
                            <i class="fas fa-envelope"></i>
                            <span>mohithbutta4002@gmail.com</span>
                        </a>
                        <a href="https://github.com/mohithnovoct" target="_blank" class="contact-link">
                            <i class="fab fa-github"></i>
                            <span>github.com/mohithnovoct</span>
                        </a>
                        <a href="https://www.linkedin.com/in/mohith-butta-472543285" target="_blank" class="contact-link">
                            <i class="fab fa-linkedin"></i>
                            <span>linkedin.com/in/mohith-butta</span>
                        </a>
                        <a href="https://x.com/mohith_butta" target="_blank" class="contact-link">
                            <i class="fab fa-twitter"></i>
                            <span>@mohith_butta</span>
                        </a>
                    </div>
                </div>
                <div class="contact-form">
                    <form id="contact-form">
                        <div class="form-group">
                            <input type="text" id="name" name="name" placeholder="Your Name" required>
                        </div>
                        <div class="form-group">
                            <input type="email" id="email" name="email" placeholder="Your Email" required>
                        </div>
                        <div class="form-group">
                            <input type="text" id="subject" name="subject" placeholder="Subject" required>
                        </div>
                        <div class="form-group">
                            <textarea id="message" name="message" placeholder="Your Message" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p>&copy; 2024 Mohith Butta. All rights reserved.</p>
                <div class="footer-links">
                    <a href="#home">Home</a>
                    <a href="#about">About</a>
                    <a href="#projects">Projects</a>
                    <a href="#blog">Blog</a>
                    <a href="#contact">Contact</a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // Theme Management
        let currentTheme = localStorage.getItem('theme') || 'light';
        
        function initTheme() {{
            if (currentTheme === 'dark') {{
                document.body.setAttribute('data-theme', 'dark');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
            }} else {{
                document.body.setAttribute('data-theme', 'light');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
            }}
        }}
        
        function toggleTheme() {{
            if (currentTheme === 'light') {{
                currentTheme = 'dark';
                document.body.setAttribute('data-theme', 'dark');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
            }} else {{
                currentTheme = 'light';
                document.body.setAttribute('data-theme', 'light');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
            }}
            localStorage.setItem('theme', currentTheme);
        }}
        
        // Smooth scrolling for navigation links
        document.querySelectorAll('.nav-link').forEach(link => {{
            link.addEventListener('click', (e) => {{
                const href = link.getAttribute('href');
                if (href.startsWith('#')) {{
                    e.preventDefault();
                    const targetSection = document.querySelector(href);
                    if (targetSection) {{
                        const offsetTop = targetSection.offsetTop - 80;
                        window.scrollTo({{ top: offsetTop, behavior: 'smooth' }});
                    }}
                }}
            }});
        }});
        
        // Initialize theme on page load
        document.addEventListener('DOMContentLoaded', initTheme);
        
        // Theme toggle event listener
        document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
        
        // Navbar scroll effect
        let lastScrollTop = 0;
        window.addEventListener('scroll', () => {{
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const navbar = document.querySelector('.navbar');
            
            if (scrollTop > lastScrollTop && scrollTop > 100) {{
                navbar.style.transform = 'translateY(-100%)';
            }} else {{
                navbar.style.transform = 'translateY(0)';
            }}
            
            lastScrollTop = scrollTop;
        }});
    </script>
</body>
</html>"""
    
    return html

def generate_blog_listing():
    """Generate blog listing page"""
    posts = load_posts()
    
    # Read the CSS from app.py
    css_content = ""
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
            start = content.find('CUSTOM_CSS = """')
            if start != -1:
                start += len('CUSTOM_CSS = """')
                end = content.find('"""', start)
                if end != -1:
                    css_content = content[start:end]
    except:
        pass
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - Mohith Butta</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>{css_content}</style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2><a href="/" style="text-decoration: none; color: inherit;">Mohith Butta</a></h2>
            </div>
            <ul class="nav-menu">
                <li><a href="/" class="nav-link">Home</a></li>
                <li><a href="/#about" class="nav-link">About</a></li>
                <li><a href="/#projects" class="nav-link">Projects</a></li>
                <li><a href="/blog" class="nav-link">Blog</a></li>
                <li><a href="/#contact" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-toggle">
                <button id="theme-toggle" class="theme-btn">
                    <i class="fas fa-moon"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- Blog content -->
    <section style="padding: 120px 0 80px;">
        <div class="container">
            <h1 class="section-title">Blog Posts</h1>
            <div class="blog-grid">
                {''.join([f'''
                <article class="blog-card">
                    <div class="blog-image">
                        <i class="fas fa-file-alt"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="blog-date">{post['prettyDate']}</span>
                            <span class="blog-category">{post.get('category', 'blog')}</span>
                        </div>
                        <h3>{post['title']}</h3>
                        <p>{post['description']}</p>
                        <a href="/blog/{post['slug']}" class="read-more">Read More →</a>
                    </div>
                </article>
                ''' for post in posts])}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p>&copy; 2024 Mohith Butta. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        let currentTheme = localStorage.getItem('theme') || 'light';
        
        function initTheme() {{
            if (currentTheme === 'dark') {{
                document.body.setAttribute('data-theme', 'dark');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
            }} else {{
                document.body.setAttribute('data-theme', 'light');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
            }}
        }}
        
        function toggleTheme() {{
            if (currentTheme === 'light') {{
                currentTheme = 'dark';
                document.body.setAttribute('data-theme', 'dark');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
            }} else {{
                currentTheme = 'light';
                document.body.setAttribute('data-theme', 'light');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
            }}
            localStorage.setItem('theme', currentTheme);
        }}
        
        document.addEventListener('DOMContentLoaded', initTheme);
        document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
    </script>
</body>
</html>"""
    
    return html

def generate_blog_post(slug):
    """Generate individual blog post page"""
    post_data = load_blog_post(slug)
    
    if not post_data:
        return None
    
    metadata = post_data['metadata']
    content = post_data['content']
    html_content = convert_markdown_to_html(content)
    
    # Read the CSS from app.py
    css_content = ""
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
            start = content.find('CUSTOM_CSS = """')
            if start != -1:
                start += len('CUSTOM_CSS = """')
                end = content.find('"""', start)
                if end != -1:
                    css_content = content[start:end]
    except:
        pass
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('title', 'Blog Post')} - Mohith Butta</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>{css_content}</style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2><a href="/" style="text-decoration: none; color: inherit;">Mohith Butta</a></h2>
            </div>
            <ul class="nav-menu">
                <li><a href="/" class="nav-link">Home</a></li>
                <li><a href="/#about" class="nav-link">About</a></li>
                <li><a href="/#projects" class="nav-link">Projects</a></li>
                <li><a href="/blog" class="nav-link">Blog</a></li>
                <li><a href="/#contact" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-toggle">
                <button id="theme-toggle" class="theme-btn">
                    <i class="fas fa-moon"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- Blog post content -->
    <section style="padding: 120px 0 80px;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content">
                <a href="/blog" class="btn btn-secondary" style="margin-bottom: 2rem;">← Back to Blog</a>
                <h1 style="margin-bottom: 1rem;">{metadata.get('title', 'Blog Post')}</h1>
                <div class="blog-meta" style="margin-bottom: 2rem;">
                    <span class="blog-date">{metadata.get('date', '')}</span>
                    {''.join([f'<span class="blog-category">{tag}</span>' for tag in metadata.get('tags', [])])}
                </div>
                <div style="line-height: 1.8; font-size: 1.1rem;">
                    {html_content}
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p>&copy; 2024 Mohith Butta. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        let currentTheme = localStorage.getItem('theme') || 'light';
        
        function initTheme() {{
            if (currentTheme === 'dark') {{
                document.body.setAttribute('data-theme', 'dark');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
            }} else {{
                document.body.setAttribute('data-theme', 'light');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
            }}
        }}
        
        function toggleTheme() {{
            if (currentTheme === 'light') {{
                currentTheme = 'dark';
                document.body.setAttribute('data-theme', 'dark');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
            }} else {{
                currentTheme = 'light';
                document.body.setAttribute('data-theme', 'light');
                document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-moon"></i>';
            }}
            localStorage.setItem('theme', currentTheme);
        }}
        
        document.addEventListener('DOMContentLoaded', initTheme);
        document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
    </script>
</body>
</html>"""
    
    return html

def main():
    """Generate all static files"""
    print("Generating static site for GitHub Pages...")
    
    # Create output directory
    os.makedirs('_site', exist_ok=True)
    os.makedirs('_site/blog', exist_ok=True)
    
    # Generate homepage
    print("Generating homepage...")
    with open('_site/index.html', 'w', encoding='utf-8') as f:
        f.write(generate_homepage())
    
    # Generate blog listing
    print("Generating blog listing...")
    with open('_site/blog/index.html', 'w', encoding='utf-8') as f:
        f.write(generate_blog_listing())
    
    # Generate individual blog posts
    posts = load_posts()
    for post in posts:
        slug = post['slug']
        print(f"Generating blog post: {slug}")
        html = generate_blog_post(slug)
        if html:
            # Create directory if it doesn't exist
            os.makedirs(f'_site/blog/{slug}', exist_ok=True)
            with open(f'_site/blog/{slug}/index.html', 'w', encoding='utf-8') as f:
                f.write(html)
    
    # Copy static assets
    print("Copying static assets...")
    import shutil
    
    # Copy essential files
    files_to_copy = [
        'profile-image.jpg',
        'Mohith_Butta-Resume.pdf',
        'feed.xml',
        'sitemap.xml',
        'robots.txt'
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, f'_site/{file}')
            print(f"Copied {file}")
    
    print("Static site generation complete!")
    print("Files generated in _site/ directory")
    print("You can now deploy the _site/ directory to GitHub Pages")

if __name__ == "__main__":
    main()
