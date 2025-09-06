# Mohith Butta - Portfolio Website

A modern, 3D-inspired portfolio website built with FastHTML, featuring a sleek design with glass morphism effects, dark/light theme toggle, and responsive layout.

## 🚀 Features

- **Modern 3D Design**: Glass morphism effects, 3D transformations, and animated gradients
- **Dark/Light Theme**: Toggle between black/grey dark mode and light mode
- **Responsive Layout**: Works perfectly on all devices
- **FastHTML Framework**: Python-based web framework with HTMX integration
- **Blog System**: Dynamic blog posts with markdown support
- **GitHub Pages Ready**: Automatic deployment with GitHub Actions

## 🎨 Design Highlights

- **Glass Morphism**: Transparent cards with backdrop blur effects
- **3D Transformations**: Perspective and rotation effects on interactive elements
- **Neon Color Palette**: Bright green (#00ff88) and cyan (#00d4ff) accents
- **Animated Backgrounds**: Subtle floating gradient orbs
- **Glowing Effects**: Text and element shadows with neon colors

## 📁 Project Structure

```
├── app.py                 # Main FastHTML application
├── build_static.py        # Static site generator for GitHub Pages
├── requirements.txt       # Python dependencies
├── _posts/               # Blog post markdown files
├── assets/               # Static assets and data
├── .github/workflows/    # GitHub Actions for deployment
└── README.md            # This file
```

## 🛠️ Development

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastHTML application:**
   ```bash
   python app.py
   ```

3. **Access your website:**
   Open `http://localhost:5001` in your browser

### Static Site Generation

For GitHub Pages deployment:

```bash
python build_static.py
```

This generates static HTML files in the `_site/` directory.

## 🚀 Deployment

### GitHub Pages (Automatic)

The repository is configured with GitHub Actions for automatic deployment:

1. Push changes to the `main` branch
2. GitHub Actions will automatically:
   - Generate static HTML files
   - Deploy to GitHub Pages
   - Update your live website

### Manual Deployment

1. Generate static files:
   ```bash
   python build_static.py
   ```

2. Deploy the `_site/` directory to your hosting provider

## 📝 Blog Posts

Blog posts are written in Markdown format in the `_posts/` directory. Each post includes:

- Frontmatter with metadata (title, date, tags, description)
- Markdown content with code syntax highlighting
- Automatic HTML generation

### Adding New Blog Posts

1. Create a new markdown file in `_posts/` with the format: `YYYY-MM-DD-slug.md`
2. Add frontmatter with post metadata
3. Write your content in Markdown
4. The post will automatically appear on the website

## 🎯 Key Technologies

- **FastHTML**: Python web framework with FastTags
- **HTMX**: Modern web interactions without complex JavaScript
- **Pico CSS**: Minimal CSS framework for modern styling
- **GitHub Actions**: Automated deployment pipeline
- **Markdown**: Blog post content format

## 🔧 Customization

### Adding New Projects

Edit the `PROJECTS` list in `app.py`:

```python
PROJECTS = [
    {
        'title': 'Your Project',
        'description': 'Project description',
        'icon': 'fas fa-icon-name',
        'tech': ['Python', 'FastHTML', 'HTMX'],
        'github': 'https://github.com/yourusername/project'
    },
    # ... more projects
]
```

### Adding New Skills

Edit the `SKILLS` dictionary in `app.py`:

```python
SKILLS = {
    'New Category': ['Skill 1', 'Skill 2', 'Skill 3'],
    # ... existing categories
}
```

### Styling Customization

The CSS is embedded in the `CUSTOM_CSS` variable in `app.py`. You can modify:
- Colors and themes
- Layout and spacing
- Animations and effects
- Responsive breakpoints

## 📱 Responsive Design

The website is fully responsive with:
- Mobile-first approach
- Flexible grid layouts
- Touch-friendly navigation
- Optimized for all screen sizes

## 🌙 Theme System

- **Light Mode**: Clean white background with dark text
- **Dark Mode**: Pure black background with neon accents
- **Persistent Storage**: Theme preference saved in localStorage
- **Smooth Transitions**: Animated theme switching

## 🔗 Links

- **Live Website**: [mohithnovoct.github.io](https://mohithnovoct.github.io)
- **GitHub Repository**: [mohithnovoct/mohithnovoct.github.io](https://github.com/mohithnovoct/mohithnovoct.github.io)
- **FastHTML Documentation**: [fastht.ml](https://www.fastht.ml/)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using FastHTML and modern web technologies.