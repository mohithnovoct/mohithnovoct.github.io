from fasthtml.common import *
from fasthtml import Raw
import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

# Email configuration
try:
    from email_config_local import EMAIL_CONFIG
except ImportError:
    # Fallback configuration - you should create email_config_local.py
    EMAIL_CONFIG = {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL', 'mohithbutta4002@gmail.com'),
        'sender_password': os.getenv('SENDER_PASSWORD', ''),
        'recipient_email': 'mohithbutta4002@gmail.com'
    }

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
    'Programming Languages': ['Python', 'HTML5', 'CSS', 'JavaScript'],
    'Data Science & ML': ['NumPy', 'Pandas', 'Matplotlib', 'Plotly', 'scikit-learn', 'Seaborn'],
    'Databases': ['PostgreSQL', 'MySQL', 'MongoDB', 'SQLite'],
    'Tools & Platforms': ['Git', 'GitHub', 'GitHub Actions', 'Streamlit', 'Flask', 'Django', 'Rest API','MCP','Cursor']
}

# Email sending function
def send_contact_email(name: str, email: str, subject: str, message: str) -> bool:
    """
    Send contact form email to the configured recipient.
    Returns True if successful, False otherwise.
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender_email']
        msg['To'] = EMAIL_CONFIG['recipient_email']
        msg['Subject'] = f"Portfolio Contact Form: {subject}"
        
        # Create email body
        body = f"""
New message from your portfolio contact form:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio website.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to server and send email
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()  # Enable security
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['recipient_email'], text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Custom CSS for minimalist black design
CUSTOM_CSS = """
:root {
    --primary-color: #ffffff;
    --secondary-color: #cccccc;
    --accent-color: #888888;
    --success-color: #00ff88;
    --warning-color: #ffd93d;
    --error-color: #ff4757;
    --background: #000000;
    --surface: #111111;
    --surface-light: #1a1a1a;
    --text-primary: #ffffff;
    --text-secondary: #cccccc;
    --text-muted: #888888;
    --border: #333333;
    --shadow: rgba(0, 0, 0, 0.8);
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.1);
    --hover-bg: rgba(255, 255, 255, 0.05);
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
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Minimalist background with subtle grid */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 50px 50px;
    z-index: -1;
    pointer-events: none;
}

/* Navigation - Minimalist Black Design */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    z-index: 1000;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border);
    transition: all 0.3s ease;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    gap: 2rem;
}

.nav-logo h2 {
    color: var(--primary-color);
    font-weight: 700;
    margin: 0;
    font-size: 1.3rem;
    letter-spacing: -0.5px;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 0;
    margin: 0;
    padding: 0;
    align-items: center;
}

.nav-link {
    text-decoration: none;
    color: var(--text-secondary);
    font-weight: 400;
    transition: all 0.3s ease;
    padding: 0.5rem 1.5rem;
    position: relative;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 1px;
    background: var(--primary-color);
    transition: all 0.3s ease;
    transform: translateX(-50%);
}

.nav-link:hover::after {
    width: 80%;
}

.nav-link:hover {
    color: var(--primary-color);
}

.nav-link.active {
    color: var(--primary-color);
}

.nav-link.active::after {
    width: 80%;
}



/* Hero Section - Minimalist Black Design */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 120px 0 80px;
    position: relative;
}

.hero-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    position: relative;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 300;
    margin-bottom: 1rem;
    line-height: 1.2;
    letter-spacing: -1px;
    color: var(--text-primary);
}

.highlight {
    color: var(--primary-color);
    font-weight: 700;
    position: relative;
    display: inline-block;
}

.hero-subtitle {
    font-size: 1.4rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
    font-weight: 300;
    letter-spacing: 1px;
}

.hero-description {
    font-size: 1rem;
    color: var(--text-secondary);
    margin-bottom: 3rem;
    max-width: 500px;
    line-height: 1.6;
    font-weight: 300;
}

.hero-buttons {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.btn {
    padding: 0.8rem 2rem;
    border-radius: 2px;
    text-decoration: none;
    font-weight: 400;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    border: none;
    cursor: pointer;
    font-size: 0.9rem;
    position: relative;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.btn-primary {
    background: var(--primary-color);
    color: var(--background);
    border: 1px solid var(--primary-color);
}

.btn-primary:hover {
    background: transparent;
    color: var(--primary-color);
    border-color: var(--primary-color);
}

.btn-secondary {
    background: transparent;
    color: var(--text-secondary);
    border: 1px solid var(--border);
}

.btn-secondary:hover {
    background: var(--hover-bg);
    color: var(--primary-color);
    border-color: var(--primary-color);
}

/* Profile Card - Minimalist Black Design */
.profile-card {
    background: var(--surface);
    padding: 2rem;
    border-radius: 4px;
    border: 1px solid var(--border);
    text-align: center;
    position: relative;
    transition: all 0.3s ease;
}

.profile-card:hover {
    border-color: var(--primary-color);
}

.profile-avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin: 0 auto 2rem;
    overflow: hidden;
    border: 2px solid var(--border);
    position: relative;
    transition: all 0.3s ease;
}

.profile-avatar:hover {
    border-color: var(--primary-color);
}

.profile-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

.social-links {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

.social-links a {
    width: 40px;
    height: 40px;
    background: transparent;
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-secondary);
    text-decoration: none;
    transition: all 0.3s ease;
    border: 1px solid var(--border);
    font-size: 0.9rem;
}

.social-links a:hover {
    color: var(--primary-color);
    border-color: var(--primary-color);
    background: var(--hover-bg);
}

/* Sections - Minimalist Black Design */
.section {
    padding: 80px 0;
    position: relative;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 300;
    text-align: center;
    margin-bottom: 3rem;
    color: var(--text-primary);
    position: relative;
    letter-spacing: -0.5px;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 1px;
    background: var(--primary-color);
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

/* Projects Section - Minimalist Black Cards */
.projects {
    background: var(--surface);
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.project-card {
    background: var(--background);
    border-radius: 4px;
    padding: 2rem;
    border: 1px solid var(--border);
    transition: all 0.3s ease;
    position: relative;
}

.project-card:hover {
    border-color: var(--primary-color);
    transform: translateY(-2px);
}

.project-icon {
    width: 50px;
    height: 50px;
    background: var(--surface);
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    border: 1px solid var(--border);
    transition: all 0.3s ease;
}

.project-card:hover .project-icon {
    border-color: var(--primary-color);
    color: var(--primary-color);
}

.project-content h3 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
    font-weight: 400;
    letter-spacing: -0.5px;
}

.project-content p {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    line-height: 1.6;
    font-size: 0.95rem;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.tech-tag {
    background: var(--surface);
    color: var(--text-secondary);
    padding: 0.3rem 0.8rem;
    border-radius: 2px;
    font-size: 0.8rem;
    border: 1px solid var(--border);
    transition: all 0.3s ease;
}

.tech-tag:hover {
    background: var(--hover-bg);
    color: var(--primary-color);
    border-color: var(--primary-color);
}

.project-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 400;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    padding: 0.5rem 1rem;
    border: 1px solid var(--border);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.8rem;
}

.project-link:hover {
    color: var(--primary-color);
    border-color: var(--primary-color);
    background: var(--hover-bg);
}

/* Blog Section */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.blog-card {
    background: var(--background);
    border-radius: 4px;
    overflow: hidden;
    border: 1px solid var(--border);
    transition: all 0.3s ease;
}

.blog-card:hover {
    border-color: var(--primary-color);
    transform: translateY(-2px);
}

.blog-image {
    height: 150px;
    background: var(--surface);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: var(--text-secondary);
    border-bottom: 1px solid var(--border);
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
    font-size: 0.8rem;
    color: var(--text-muted);
}

.blog-category {
    color: var(--primary-color);
    font-weight: 400;
}

.blog-content h3 {
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
    font-weight: 400;
}

.blog-content p {
    color: var(--text-secondary);
    margin-bottom: 1rem;
    line-height: 1.6;
    font-size: 0.9rem;
}

.read-more {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 400;
    transition: color 0.3s ease;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.read-more:hover {
    color: var(--primary-color);
}

/* Contact Section */
.contact {
    background: var(--surface);
}

.contact-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    max-width: 1000px;
    margin: 0 auto;
}

.contact-info h3 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
    font-weight: 400;
}

.contact-info p {
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.6;
    font-size: 0.95rem;
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
    color: var(--text-secondary);
    text-decoration: none;
    padding: 1rem;
    border-radius: 2px;
    background: var(--background);
    border: 1px solid var(--border);
    transition: all 0.3s ease;
    font-size: 0.9rem;
}

.contact-link:hover {
    color: var(--primary-color);
    border-color: var(--primary-color);
    background: var(--hover-bg);
}

.contact-form {
    background: var(--background);
    padding: 2rem;
    border-radius: 4px;
    border: 1px solid var(--border);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid var(--border);
    border-radius: 2px;
    background: var(--background);
    color: var(--text-primary);
    font-family: inherit;
    transition: border-color 0.3s ease;
    font-size: 0.9rem;
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
    color: var(--text-muted);
    margin: 0;
    font-size: 0.9rem;
}

.footer-links {
    display: flex;
    gap: 2rem;
}

.footer-links a {
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.3s ease;
    font-size: 0.9rem;
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
        gap: 2rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .hero-buttons {
        justify-content: center;
    }
    
    .contact-content {
        grid-template-columns: 1fr;
        gap: 2rem;
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
}

@media (max-width: 480px) {
    .container {
        padding: 0 1rem;
    }
    
    .hero-title {
        font-size: 2rem;
    }
    
    .section-title {
        font-size: 2rem;
    }
    
    .btn {
        padding: 0.7rem 1.5rem;
        font-size: 0.8rem;
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .project-card {
        padding: 1.5rem;
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
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.project-card,
.blog-card {
    animation: fadeInUp 0.4s ease-out;
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
                            href="Mohith_Butta_Resume.pdf",
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
        
        # JavaScript for interactions
        Script("""
            
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
            
            // Initialize on page load
            document.addEventListener('DOMContentLoaded', () => {
                // Page is ready
            });
            
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
    # Send the email
    email_sent = send_contact_email(name, email, subject, message)
    
    if email_sent:
        # Success message
        return Div(
            Div(
                I(cls="fas fa-check-circle", style="font-size: 3rem; color: var(--success-color); margin-bottom: 1rem;"),
                H3("Message Sent Successfully!", style="color: var(--success-color); margin-bottom: 1rem;"),
                P("Thank you for reaching out! I'll get back to you as soon as possible.", style="margin-bottom: 2rem;"),
                Button("Send Another Message", onclick="location.reload()", cls="btn btn-primary"),
                style="text-align: center; padding: 2rem;"
            ),
            id="contact-form",
            cls="contact-form"
        )
    else:
        # Error message
        return Div(
            Div(
                I(cls="fas fa-exclamation-triangle", style="font-size: 3rem; color: var(--error-color); margin-bottom: 1rem;"),
                H3("Oops! Something went wrong", style="color: var(--error-color); margin-bottom: 1rem;"),
                P("There was an issue sending your message. Please try again or contact me directly at mohithbutta4002@gmail.com", style="margin-bottom: 2rem;"),
                Button("Try Again", onclick="location.reload()", cls="btn btn-primary"),
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
        
        # JavaScript for blog page
        Script("""
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
