# CV Project

## About
A professional CV application with both a static frontend and a Django backend. The frontend is built with semantic HTML and modern CSS, while the backend provides a RESTful API for dynamic content management.

## Features
- **Static Frontend**: Clean, responsive, and print-ready CV
- **Django Backend**: REST API for managing CV content
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Print Styles**: Optimized for A4 paper printing
- **SEO Optimized**: With JSON-LD structured data

## Project Structure
```
cv-project/
├── index.html           # Static frontend entry point
├── styles.css          # Main stylesheet
├── assets/             # Images and other static assets
└── sunil_cv/           # Django project
    ├── manage.py       # Django management script
    ├── requirements.txt # Python dependencies
    ├── sunil_cv/       # Project settings
    └── cv/             # CV app with models and API
        ├── models.py   # Database models
        ├── serializers.py # API serializers
        ├── urls.py     # API endpoints
        └── views.py    # API views
```

## Quick Start (Static Frontend Only)
1. Open `index.html` in any modern browser
2. For print preview: press `Ctrl/Cmd+P` and choose A4, remove headers/footers

## Django Backend Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. Clone the repository
2. Navigate to the project directory:
   ```bash
   cd cv-project
   ```
3. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. Run migrations:
   ```bash
   cd sunil_cv
   python manage.py migrate
   ```
2. (Optional) Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

### Running the Development Server
1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Access the application at http://127.0.0.1:8000/
3. Access the admin interface at http://127.0.0.1:8000/admin/
4. API endpoints are available under http://127.0.0.1:8000/api/

## API Endpoints
- `GET /api/profile/` - Get profile information
- `GET /api/education/` - List education history
- `GET /api/experience/` - List work experience
- `GET /api/projects/` - List projects
- `GET /api/skills/` - List skills by category
- `GET /api/attributes/` - List personal attributes
- `GET /api/languages/` - List languages

## Frontend Development
- The static frontend is in the root directory
- Styles are in `styles.css`
- For development, you can use any static file server or open `index.html` directly

## Deployment
For production deployment, consider using:
- **Frontend**: Netlify, Vercel, or GitHub Pages
- **Backend**: PythonAnywhere, Heroku, or a VPS with Gunicorn/Nginx

## Accessibility
- Semantic HTML5 elements
- Proper heading hierarchy
- Skip link for keyboard navigation
- High contrast colors
- ARIA attributes where needed

## SEO
- Semantic HTML structure
- Meta description and viewport tag
- JSON-LD structured data
- Mobile-responsive design
- Fast loading times

## Images

### Adding Images
1. Place all images in the `assets/` directory
2. Use relative paths to reference images in your HTML/CSS:
   ```html
   <img src="assets/your-image.jpg" alt="Description of image">
   ```
3. For optimized web performance:
   - Use appropriate image formats (JPEG for photos, PNG for graphics with transparency, WebP for modern browsers)
   - Optimize images before adding them to the project
   - Include appropriate `alt` text for accessibility

### Project Screenshot
Add a screenshot of your project here:
```markdown
![CV Project Screenshot](assets/screenshot.png)
```
*Replace `screenshot.png` with your actual screenshot file*

## License
[Specify your license here, e.g., MIT, GPL, etc.]

## Contact
For any questions or feedback, please contact [Your Email]

---

## Preview
<!-- Add more screenshots here if needed -->
<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px;">
  <img src="assets/screenshot-desktop.png" alt="Desktop View" width="45%">
  <img src="assets/screenshot-mobile.png" alt="Mobile View" width="45%">
</div>
