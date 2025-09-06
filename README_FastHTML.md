# Modern Portfolio Website with FastHTML

This is a complete redesign of your portfolio website using [FastHTML](https://www.fastht.ml/), a modern Python web framework that combines Starlette, Uvicorn, HTMX, and FastTags for creating server-rendered hypermedia applications.

## Features

✨ **Modern Design**
- Clean, professional layout with smooth animations
- Dark/Light theme toggle with persistent storage
- Fully responsive design for all devices
- Modern CSS with CSS custom properties

🚀 **FastHTML Benefits**
- Server-side rendering with HTMX for dynamic interactions
- Python-based templating with FastTags
- Built-in Pico CSS framework for modern styling
- No JavaScript framework dependencies (React/Vue/Svelte)

📱 **Responsive & Interactive**
- Mobile-first responsive design
- Smooth scrolling navigation
- Interactive contact form with HTMX
- Dynamic blog post loading
- Hover effects and animations

🎨 **Modern UI Components**
- Gradient backgrounds and modern cards
- Font Awesome icons
- Inter font family for typography
- CSS Grid and Flexbox layouts

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access Your Website**
   Open your browser and go to `http://localhost:5001`

## Project Structure

```
├── app.py                 # Main FastHTML application
├── requirements.txt       # Python dependencies
├── assets/
│   └── posts.json        # Blog posts data
├── profile-image.jpg     # Your profile picture
├── Mohith_Butta-Resume.pdf # Your resume
└── README_FastHTML.md    # This file
```

## Key Features Implemented

### 🏠 Homepage (`/`)
- Hero section with profile card and social links
- About section with skills grid
- Featured projects showcase
- Latest blog posts
- Contact form with HTMX integration

### 📝 Blog (`/blog`)
- Complete blog listing page
- Dynamic post loading from JSON
- Responsive blog cards

### 🎨 Modern Styling
- CSS custom properties for theming
- Dark/Light mode toggle
- Smooth animations and transitions
- Mobile-responsive design

### ⚡ HTMX Integration
- Contact form submission without page reload
- Dynamic content updates
- Modern web interactions

## Customization

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
The CSS is embedded in the `CUSTOM_CSS` variable in `app.py`. You can modify colors, fonts, and layouts there.

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production, you can use:
- **Railway**: Connect your GitHub repo
- **Render**: Deploy as a web service
- **Heroku**: Use the Procfile method
- **DigitalOcean App Platform**: Direct deployment

### Environment Variables
Set these for production:
```bash
export PORT=8000  # or your preferred port
```

## FastHTML Advantages

1. **Python-First**: Write everything in Python, no JavaScript framework needed
2. **Server-Side Rendering**: Better SEO and initial load performance
3. **HTMX Integration**: Modern web interactions without complex JavaScript
4. **FastTags**: Clean, Pythonic HTML generation
5. **Built-in Styling**: Pico CSS included for modern, accessible design

## Migration from Static Site

Your original static site assets are preserved:
- `profile-image.jpg` - Your profile picture
- `Mohith_Butta-Resume.pdf` - Your resume
- `assets/posts.json` - Blog posts data
- All existing blog content in `_posts/` and `blog/` directories

## Next Steps

1. **Test the Application**: Run `python app.py` and test all features
2. **Customize Content**: Update projects, skills, and personal information
3. **Deploy**: Choose a hosting platform and deploy your new FastHTML site
4. **Domain Setup**: Configure your custom domain if needed

## Support

- [FastHTML Documentation](https://www.fastht.ml/docs/)
- [HTMX Documentation](https://htmx.org/docs/)
- [Pico CSS Documentation](https://picocss.com/docs/)

Your modern FastHTML portfolio is ready to go! 🚀
