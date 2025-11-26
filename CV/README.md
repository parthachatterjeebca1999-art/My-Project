# Somnath Portfolio Website

A professional, fully animated portfolio website for Somnath Chatterjee built with HTML, CSS, Tailwind CSS, and JavaScript.

## Features

✨ **Modern Design**
- Responsive and mobile-friendly layout
- Gradient backgrounds and glassmorphism effects
- Smooth animations and transitions
- Professional color scheme (Cyan & Blue)

🎯 **Key Sections**
- Hero section with animated profile image
- About me with personal information
- Technical skills with animated progress bars
- Education qualifications with dynamic table
- Project showcase with hover effects
- Contact information and social links
- Footer with social media icons

🚀 **Interactive Elements**
- Smooth scroll navigation
- Mobile menu toggle
- Animated skill bars on scroll
- Project card hover effects
- Scroll-to-top button
- Parallax effects
- Intersection Observer animations

📱 **Responsive Design**
- Mobile-first approach
- Tablet and desktop optimized
- Touch-friendly navigation
- Optimized for all screen sizes

## Project Structure

```
MY portfolio/
├── index.html                 # Main HTML file
├── css/
│   └── style.css             # Custom CSS with animations
├── js/
│   └── script.js             # JavaScript functionality
├── assets/
│   ├── profile/
│   │   └── profile.jpg       # Profile photo
│   └── projects/
│       ├── project1.jpg      # Project 1 image
│       ├── project2.jpg      # Project 2 image
│       └── project3.jpg      # Project 3 image
└── README.md                 # This file
```

## Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Advanced styling with animations
- **Tailwind CSS** - Utility-first CSS framework
- **JavaScript (ES6+)** - Interactive functionality
- **jQuery** - DOM manipulation (optional)
- **Font Awesome** - Icon library

## Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- No server required - works with file:// protocol

### Installation

1. **Clone or Download**
   ```bash
   # If using git
   git clone <repository-url>
   
   # Or download the ZIP file and extract it
   ```

2. **Add Your Profile Photo**
   - Place your profile image in `assets/profile/` folder
   - Name it `profile.jpg` (or update the filename in HTML)
   - Recommended size: 400x400px

3. **Add Project Images**
   - Place project screenshots in `assets/projects/` folder
   - Name them `project1.jpg`, `project2.jpg`, `project3.jpg`
   - Recommended size: 600x400px

4. **Update Content**
   - Edit `index.html` to update personal information
   - Update project links and descriptions
   - Modify social media links in the footer

5. **Open in Browser**
   ```bash
   # Simply open the index.html file in your browser
   # Or use a local server for better performance
   ```

### Using a Local Server (Recommended)

**Using Python 3:**
```bash
python -m http.server 8000
# Then visit http://localhost:8000
```

**Using Python 2:**
```bash
python -m SimpleHTTPServer 8000
# Then visit http://localhost:8000
```

**Using Node.js (http-server):**
```bash
npm install -g http-server
http-server
# Then visit http://localhost:8080
```

**Using Live Server (VS Code Extension):**
- Install "Live Server" extension
- Right-click on index.html
- Select "Open with Live Server"

## Customization

### Colors
Edit the color scheme in `css/style.css`:
- Primary: `#06b6d4` (Cyan)
- Secondary: `#3b82f6` (Blue)
- Background: `#111827` (Dark Gray)

### Fonts
Update font family in `css/style.css`:
```css
body {
    font-family: 'Your Font', sans-serif;
}
```

### Content
Update personal information in `index.html`:
- Name and title
- Email and phone
- Social media links
- Project descriptions
- Skills and education

### Animations
Modify animation speeds in `css/style.css`:
```css
@keyframes fade-in {
    /* Adjust timing here */
}
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Tips

1. **Optimize Images**
   - Use tools like TinyPNG or ImageOptim
   - Recommended format: WebP for better compression

2. **Lazy Loading**
   - Images are lazy-loaded for better performance
   - Use `data-src` attribute for images

3. **Caching**
   - Browser caches static files automatically
   - Consider using a CDN for production

## Deployment

### Deploy to Netlify
1. Push your code to GitHub
2. Connect your GitHub repo to Netlify
3. Netlify will automatically deploy on every push

### Deploy to Vercel
1. Push your code to GitHub
2. Import project in Vercel
3. Vercel will handle deployment

### Deploy to GitHub Pages
1. Push your code to GitHub
2. Go to Settings → Pages
3. Select main branch as source
4. Your site will be live at `username.github.io/repository`

### Deploy to Traditional Hosting
1. Upload files via FTP
2. Ensure `index.html` is in the root directory
3. Access via your domain

## SEO Optimization

The website includes:
- Meta tags for description
- Semantic HTML structure
- Open Graph tags (can be added)
- Schema markup (can be added)

To improve SEO:
1. Add meta description
2. Add keywords
3. Create sitemap.xml
4. Add robots.txt
5. Optimize images with alt text

## Accessibility

The website follows WCAG guidelines:
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Color contrast compliance
- Mobile accessibility

## Troubleshooting

### Images not loading
- Check file paths in HTML
- Ensure images are in correct folders
- Use absolute paths if needed

### Animations not working
- Check browser compatibility
- Ensure CSS file is linked correctly
- Clear browser cache (Ctrl+Shift+Delete)

### Mobile menu not working
- Check JavaScript file is loaded
- Verify mobile-menu-btn ID exists
- Check console for errors (F12)

### Styles not applying
- Clear browser cache
- Check CSS file path
- Verify Tailwind CSS CDN is loaded
- Check for CSS conflicts

## Performance Metrics

Target metrics:
- Lighthouse Score: 90+
- Page Load Time: < 2 seconds
- First Contentful Paint: < 1 second
- Cumulative Layout Shift: < 0.1

## Future Enhancements

- [ ] Add blog section
- [ ] Implement contact form with backend
- [ ] Add dark/light theme toggle
- [ ] Add multi-language support
- [ ] Add testimonials section
- [ ] Add experience timeline
- [ ] Add certifications section
- [ ] Add downloadable resume

## License

This portfolio template is free to use and modify for personal use.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check browser console (F12) for errors
4. Contact the developer

## Credits

- **Framework**: Tailwind CSS
- **Icons**: Font Awesome
- **Fonts**: Google Fonts
- **Inspiration**: Modern portfolio designs

## Version History

### v1.0.0 (2024)
- Initial release
- Hero section with animations
- About section with personal info
- Skills section with progress bars
- Education section with table
- Projects showcase
- Contact section
- Footer with social links
- Mobile responsive design
- Smooth animations throughout

---

**Last Updated**: November 2024
**Created for**: Somnath Chatterjee
**Status**: Production Ready ✅
