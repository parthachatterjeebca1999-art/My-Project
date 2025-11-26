# Quick Reference Guide

## File Locations & What to Edit

### 📄 Main Files
| File | Purpose | Edit For |
|------|---------|----------|
| `index.html` | Main content | Personal info, projects, text |
| `css/style.css` | Styling & animations | Colors, fonts, effects |
| `js/script.js` | Interactivity | Functionality, events |
| `config.json` | Configuration | Easy reference data |

### 📁 Folders
| Folder | Purpose | Add |
|--------|---------|-----|
| `assets/profile/` | Profile photo | Your photo (profile.jpg) |
| `assets/projects/` | Project screenshots | Project images (project1-3.jpg) |
| `css/` | Stylesheets | Custom CSS files |
| `js/` | JavaScript | Custom scripts |

---

## Quick Edits

### Change Your Name
**File:** `index.html`
**Find:** `Somnath Chatterjee`
**Replace:** Your name

### Change Email
**File:** `index.html`
**Find:** `somnathchatterjeebca1999@gmail.com`
**Replace:** Your email

### Change Phone
**File:** `index.html`
**Find:** `+91 7032294862`
**Replace:** Your phone

### Change Location
**File:** `index.html`
**Find:** `Raniganj, Paschim Bardhaman`
**Replace:** Your location

### Change Primary Color
**File:** `css/style.css`
**Find:** `#06b6d4` (Cyan)
**Replace:** Your color code

### Change Secondary Color
**File:** `css/style.css`
**Find:** `#3b82f6` (Blue)
**Replace:** Your color code

---

## Common Tasks

### Add a New Skill
1. Find Skills Section in `index.html`
2. Copy a skill block:
```html
<div>
    <div class="flex justify-between mb-2">
        <span>Skill Name</span>
        <span class="text-cyan-400">XX%</span>
    </div>
    <div class="w-full bg-gray-700 rounded-full h-2 overflow-hidden">
        <div class="bg-gradient-to-r from-cyan-400 to-blue-500 h-full rounded-full skill-bar" style="width: XX%"></div>
    </div>
</div>
```
3. Update skill name and percentage

### Add a New Project
1. Find Projects Section in `index.html`
2. Copy a project card:
```html
<div class="project-card group">
    <div class="relative overflow-hidden rounded-lg h-64 mb-4">
        <img src="assets/projects/projectX.jpg" alt="Project Name">
        <!-- ... rest of card ... -->
    </div>
</div>
```
3. Update image, title, description, and link

### Update Social Links
**File:** `index.html` (Footer section)

```html
<a href="https://www.facebook.com/YOUR_USERNAME" target="_blank">
<a href="https://wa.me/YOUR_PHONE" target="_blank">
<a href="https://www.instagram.com/YOUR_USERNAME" target="_blank">
<a href="https://github.com/YOUR_USERNAME" target="_blank">
<a href="https://www.linkedin.com/in/YOUR_PROFILE" target="_blank">
```

---

## Color Codes

### Current Theme
| Color | Code | Usage |
|-------|------|-------|
| Cyan | `#06b6d4` | Primary accent |
| Blue | `#3b82f6` | Secondary accent |
| Dark | `#111827` | Background |
| Gray | `#1f2937` | Cards |
| White | `#ffffff` | Text |

### Popular Alternatives
| Color | Code |
|-------|------|
| Purple | `#8b5cf6` |
| Pink | `#ec4899` |
| Green | `#10b981` |
| Orange | `#f59e0b` |
| Red | `#ef4444` |

---

## Keyboard Shortcuts

### Browser
| Shortcut | Action |
|----------|--------|
| `F12` | Open Developer Tools |
| `Ctrl+Shift+Delete` | Clear Cache |
| `Ctrl+R` | Refresh Page |
| `Ctrl+Shift+R` | Hard Refresh |

### Code Editor (VS Code)
| Shortcut | Action |
|----------|--------|
| `Ctrl+F` | Find |
| `Ctrl+H` | Find & Replace |
| `Ctrl+/` | Comment |
| `Ctrl+S` | Save |
| `Ctrl+Shift+P` | Command Palette |

---

## Common Issues & Fixes

### Images Not Showing
✅ Check file path is correct
✅ Ensure file exists in folder
✅ Use forward slashes: `/assets/profile/profile.jpg`

### Styles Not Applied
✅ Clear browser cache (Ctrl+Shift+Delete)
✅ Check CSS file is linked
✅ Verify Tailwind CDN is loaded

### Mobile Menu Not Working
✅ Check JavaScript is enabled
✅ Verify mobile-menu-btn ID exists
✅ Test on actual mobile device

### Animations Not Smooth
✅ Check browser compatibility
✅ Reduce animation duration
✅ Disable other animations

---

## Useful Links

### Tools
- **Image Compression:** https://tinypng.com
- **Color Picker:** https://htmlcolorcodes.com
- **Icon Library:** https://fontawesome.com
- **Fonts:** https://fonts.google.com

### Validation
- **HTML Validator:** https://validator.w3.org
- **CSS Validator:** https://jigsaw.w3.org/css-validator
- **Lighthouse:** Built into Chrome DevTools

### Deployment
- **Netlify:** https://netlify.com
- **Vercel:** https://vercel.com
- **GitHub Pages:** https://pages.github.com

### Learning
- **MDN Web Docs:** https://developer.mozilla.org
- **W3Schools:** https://w3schools.com
- **CSS Tricks:** https://css-tricks.com

---

## Responsive Breakpoints

| Device | Width | Class |
|--------|-------|-------|
| Mobile | < 640px | `sm:` |
| Tablet | 640px - 1024px | `md:` |
| Desktop | > 1024px | `lg:` |

Example:
```html
<div class="text-sm md:text-lg lg:text-xl">
    Responsive text
</div>
```

---

## CSS Classes Reference

### Text
```css
.text-cyan-400      /* Cyan text */
.text-gray-300      /* Gray text */
.font-bold          /* Bold text */
.text-center        /* Center text */
.text-gradient      /* Gradient text */
```

### Spacing
```css
.p-4                /* Padding 1rem */
.m-4                /* Margin 1rem */
.mb-4               /* Margin bottom */
.px-4               /* Padding horizontal */
.py-4               /* Padding vertical */
```

### Layout
```css
.flex               /* Flexbox */
.grid               /* Grid layout */
.gap-4              /* Gap between items */
.justify-center     /* Center horizontally */
.items-center       /* Center vertically */
```

### Effects
```css
.shadow-lg          /* Large shadow */
.rounded-lg         /* Rounded corners */
.opacity-50         /* 50% opacity */
.hover:scale-110    /* Scale on hover */
.transition         /* Smooth transition */
```

---

## JavaScript Functions

### Scroll to Section
```javascript
document.querySelector('#section-id').scrollIntoView({
    behavior: 'smooth'
});
```

### Add Class
```javascript
element.classList.add('class-name');
```

### Remove Class
```javascript
element.classList.remove('class-name');
```

### Toggle Class
```javascript
element.classList.toggle('class-name');
```

### Event Listener
```javascript
element.addEventListener('click', function() {
    // Do something
});
```

---

## Performance Tips

1. **Compress Images** - Use TinyPNG
2. **Minimize CSS/JS** - Use minifiers
3. **Use CDN** - Already included
4. **Enable Caching** - Set headers
5. **Lazy Load** - Load images on scroll
6. **Remove Unused Code** - Clean up CSS

---

## Checklist Before Sharing

- [ ] Updated all personal information
- [ ] Added your profile photo
- [ ] Added project screenshots
- [ ] Updated social media links
- [ ] Tested on mobile
- [ ] Tested in multiple browsers
- [ ] Checked for typos
- [ ] Verified all links work
- [ ] Optimized images
- [ ] Deployed to hosting

---

## Version Control (Git)

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial portfolio commit"

# Add remote
git remote add origin https://github.com/username/portfolio.git

# Push to GitHub
git push -u origin main
```

---

## Deployment Commands

### Netlify
```bash
npm install -g netlify-cli
netlify deploy
```

### Vercel
```bash
npm install -g vercel
vercel
```

### GitHub Pages
```bash
git push origin main
# Then enable Pages in GitHub Settings
```

---

## Support Resources

- **README.md** - Full documentation
- **SETUP_GUIDE.md** - Detailed setup instructions
- **config.json** - Configuration reference
- **Browser DevTools** - Debug issues (F12)
- **GitHub Issues** - Report problems

---

**Last Updated:** November 2024
**Version:** 1.0.0
**Status:** Production Ready ✅
