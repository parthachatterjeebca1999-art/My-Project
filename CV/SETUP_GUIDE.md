# Somnath Portfolio - Setup Guide

## Quick Start (5 Minutes)

### Step 1: Generate Placeholder Images
1. Open `create_images.html` in your browser
2. Right-click on each image and save to the correct folder:
   - Profile image → `assets/profile/profile.jpg`
   - Project 1 → `assets/projects/project1.jpg`
   - Project 2 → `assets/projects/project2.jpg`
   - Project 3 → `assets/projects/project3.jpg`

### Step 2: Replace with Your Images
1. Take a professional photo of yourself (400x400px recommended)
2. Take screenshots of your projects (600x400px recommended)
3. Replace the placeholder images with your own

### Step 3: Update Personal Information
Edit `index.html` and update:
- Your name and title
- Email address
- Phone number
- Location
- Social media links
- Project descriptions

### Step 4: View Your Portfolio
1. Open `index.html` in your browser
2. Or use a local server (see below)

---

## Detailed Setup Instructions

### Option A: Using File Explorer (Simplest)
1. Navigate to `d:\MY portfolio`
2. Double-click `index.html`
3. Your portfolio opens in the default browser

### Option B: Using Python (Recommended)
```bash
# Open Command Prompt/PowerShell
cd d:\MY portfolio

# Python 3
python -m http.server 8000

# Then open: http://localhost:8000
```

### Option C: Using Node.js
```bash
# Install http-server (one-time)
npm install -g http-server

# Navigate to portfolio folder
cd d:\MY portfolio

# Start server
http-server

# Open: http://localhost:8080
```

### Option D: Using VS Code Live Server
1. Open the portfolio folder in VS Code
2. Install "Live Server" extension
3. Right-click on `index.html`
4. Select "Open with Live Server"

---

## Customization Guide

### 1. Update Personal Information

**Edit `index.html`:**

Find and replace:
- `Somnath Chatterjee` → Your name
- `somnathchatterjeebca1999@gmail.com` → Your email
- `+91 7032294862` → Your phone
- `Raniganj, Paschim Bardhaman` → Your location

### 2. Update Social Media Links

**In `index.html` footer section:**

```html
<a href="https://www.facebook.com/YOUR_USERNAME" target="_blank">
<a href="https://wa.me/YOUR_PHONE_NUMBER" target="_blank">
<a href="https://www.instagram.com/YOUR_USERNAME" target="_blank">
<a href="https://github.com/YOUR_USERNAME" target="_blank">
<a href="https://www.linkedin.com/in/YOUR_PROFILE" target="_blank">
```

### 3. Update Skills

**In `index.html` Skills Section:**

To change skill percentage:
```html
<div class="flex justify-between mb-2">
    <span>Your Skill Name</span>
    <span class="text-cyan-400">YOUR_PERCENTAGE%</span>
</div>
<div class="w-full bg-gray-700 rounded-full h-2 overflow-hidden">
    <div class="bg-gradient-to-r from-cyan-400 to-blue-500 h-full rounded-full skill-bar" 
         style="width: YOUR_PERCENTAGE%"></div>
</div>
```

### 4. Update Education

**In `index.html` Education Table:**

Find the table rows and update:
- Exam Name
- Board/University
- Passing Year
- Institute Name
- Full Marks
- Percentage

### 5. Update Projects

**In `index.html` Projects Section:**

For each project card:
```html
<div class="project-card group">
    <div class="relative overflow-hidden rounded-lg h-64 mb-4">
        <img src="assets/projects/projectX.jpg" alt="Project Name">
        <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-60 transition-all duration-300 flex items-center justify-center">
            <a href="YOUR_PROJECT_LINK" target="_blank" class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 px-6 py-2 bg-cyan-500 rounded-lg font-semibold hover:bg-cyan-600">
                View Project
            </a>
        </div>
    </div>
    <h3 class="text-xl font-semibold mb-2 text-cyan-400">Your Project Title</h3>
    <p class="text-gray-400 text-sm mb-4">Your project description here.</p>
    <div class="flex gap-2 flex-wrap">
        <span class="text-xs bg-cyan-500 bg-opacity-20 text-cyan-300 px-3 py-1 rounded-full">Technology 1</span>
        <span class="text-xs bg-blue-500 bg-opacity-20 text-blue-300 px-3 py-1 rounded-full">Technology 2</span>
    </div>
</div>
```

### 6. Change Colors

**Edit `css/style.css`:**

Find and replace color codes:
- Cyan: `#06b6d4` → Your primary color
- Blue: `#3b82f6` → Your secondary color
- Dark: `#111827` → Your background color

Or use `config.json` for reference.

---

## Adding More Sections

### Add a New Section

1. **Create HTML section:**
```html
<section id="new-section" class="py-20 px-4 relative">
    <div class="max-w-6xl mx-auto">
        <h2 class="text-4xl md:text-5xl font-bold mb-12 text-center">
            <span class="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                Section Title
            </span>
        </h2>
        <!-- Your content here -->
    </div>
</section>
```

2. **Add navigation link:**
```html
<li><a href="#new-section" class="nav-link hover:text-cyan-400 transition">New Section</a></li>
```

3. **Add CSS styling** in `css/style.css` if needed

---

## Image Optimization

### Compress Images
1. Visit: https://tinypng.com
2. Upload your images
3. Download compressed versions
4. Replace original files

### Image Formats
- **Profile**: JPG or PNG (400x400px, < 200KB)
- **Projects**: JPG or PNG (600x400px, < 300KB each)
- **Recommended**: Use WebP for better compression

---

## SEO Optimization

### Update Meta Tags

**In `index.html` head section:**
```html
<meta name="description" content="Your portfolio description">
<meta name="keywords" content="your, keywords, here">
<meta name="author" content="Your Name">
<meta property="og:title" content="Your Portfolio Title">
<meta property="og:description" content="Your portfolio description">
<meta property="og:image" content="assets/profile/profile.jpg">
```

### Add Sitemap
Create `sitemap.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://yourportfolio.com/</loc>
        <lastmod>2024-11-26</lastmod>
        <priority>1.0</priority>
    </url>
</urlset>
```

---

## Deployment

### Deploy to Netlify
1. Push code to GitHub
2. Go to https://netlify.com
3. Click "New site from Git"
4. Select your repository
5. Deploy!

### Deploy to Vercel
1. Push code to GitHub
2. Go to https://vercel.com
3. Import your project
4. Deploy!

### Deploy to GitHub Pages
1. Push code to GitHub
2. Go to Settings → Pages
3. Select main branch
4. Your site is live!

---

## Troubleshooting

### Images not showing
- Check file paths in HTML
- Ensure images are in correct folders
- Use absolute paths: `/assets/profile/profile.jpg`

### Styles not applying
- Clear browser cache (Ctrl+Shift+Delete)
- Check CSS file path
- Verify Tailwind CDN is loaded

### Animations not working
- Check browser compatibility
- Ensure JavaScript file is loaded
- Check console for errors (F12)

### Mobile menu not working
- Check JavaScript is enabled
- Verify mobile-menu-btn ID exists
- Test on actual mobile device

---

## Performance Tips

1. **Optimize Images**
   - Use TinyPNG or similar tools
   - Aim for < 100KB per image

2. **Minimize CSS/JS**
   - Use minified versions in production
   - Remove unused code

3. **Use CDN**
   - Tailwind CSS is already from CDN
   - Font Awesome is from CDN

4. **Enable Caching**
   - Browsers cache static files
   - Set cache headers on server

---

## Browser Testing

Test on:
- ✅ Chrome (Desktop & Mobile)
- ✅ Firefox (Desktop & Mobile)
- ✅ Safari (Desktop & Mobile)
- ✅ Edge (Desktop)

---

## File Structure Reference

```
MY portfolio/
├── index.html                 # Main file
├── css/
│   └── style.css             # Styles & animations
├── js/
│   └── script.js             # Interactivity
├── assets/
│   ├── profile/
│   │   └── profile.jpg       # Your photo
│   └── projects/
│       ├── project1.jpg
│       ├── project2.jpg
│       └── project3.jpg
├── config.json               # Configuration
├── create_images.html        # Image generator
├── README.md                 # Documentation
└── SETUP_GUIDE.md           # This file
```

---

## Next Steps

1. ✅ Replace placeholder images
2. ✅ Update personal information
3. ✅ Customize colors and fonts
4. ✅ Add your projects
5. ✅ Test on mobile
6. ✅ Deploy to hosting
7. ✅ Share with recruiters!

---

## Support & Help

- Check README.md for detailed documentation
- Review code comments in HTML/CSS/JS
- Test in browser console (F12)
- Validate HTML: https://validator.w3.org

---

**Happy Coding! 🚀**

Last Updated: November 2024
