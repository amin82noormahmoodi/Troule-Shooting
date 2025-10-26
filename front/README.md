# Board Troubleshooting Platform - Frontend

A modern, responsive React application for the Board Troubleshooting Platform with a stunning dark theme and smooth animations.

## 🎨 Features

- **Modern UI/UX**: Dark theme with neon highlights and glassmorphism effects
- **Responsive Design**: Optimized for desktop and tablet views
- **Smooth Animations**: Framer Motion for fluid transitions
- **Interactive Components**: Hover effects, loading states, and micro-interactions
- **Toast Notifications**: User-friendly error and success messages
- **Routing**: React Router for seamless navigation

## 🛠️ Tech Stack

- **React 19**: Latest React with modern features
- **Vite**: Fast build tool and dev server
- **Tailwind CSS**: Utility-first CSS framework
- **Framer Motion**: Animation library
- **React Router**: Client-side routing
- **Axios**: HTTP client for API calls
- **Lucide React**: Beautiful icon library
- **React Hot Toast**: Toast notifications

## 📋 Prerequisites

- Node.js 16+
- npm or yarn
- Backend API running on `http://localhost:8000`

## 🚀 Installation

1. **Navigate to frontend directory**
   ```bash
   cd front
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

The application will be available at `http://localhost:5173`

## 🎯 Application Flow

### 1. Board Selection Page (`/`)
- Displays all available boards as interactive cards
- Each card shows board name with animated icons
- Click to navigate to problems page

### 2. Problems Page (`/problems/:boardId`)
- Shows all problems for the selected board
- Problem cards with hover effects and animations
- Click to view solutions for each problem

### 3. Solutions Page (`/solutions/:problemId`)
- Displays all solutions for the selected problem
- Solution cards with success indicators
- Back navigation to problems page

### 4. 404 Page
- Custom 404 page with animations
- Navigation back to home or previous page

## 🎨 Design System

### Color Palette
- **Primary**: Cyan (#00ffff) with gradients
- **Secondary**: Purple (#8b5cf6) and Amber (#f59e0b)
- **Background**: Dark gradient from gray-900 to purple-900
- **Glass Effect**: Semi-transparent with backdrop blur

### Typography
- **Headings**: Poppins font family
- **Body**: Inter font family
- **Gradient Text**: Cyan to purple to amber gradients

### Animations
- **Page Transitions**: Fade in and slide up
- **Hover Effects**: Scale and glow effects
- **Loading States**: Rotating spinners
- **Card Interactions**: 3D hover effects

## 🧩 Component Structure

```
src/
├── components/
│   └── Navbar.jsx          # Navigation bar
├── pages/
│   ├── BoardSelection.jsx  # Home page - board selection
│   ├── ProblemList.jsx     # Problems for selected board
│   ├── SolutionList.jsx    # Solutions for selected problem
│   └── NotFound.jsx        # 404 page
├── api/
│   └── index.js           # API service layer
├── App.jsx               # Main app component
└── main.jsx             # App entry point
```

## 🔧 Configuration

### API Configuration
The API base URL is configured in `src/api/index.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000';
```

### Tailwind Configuration
Custom theme and animations are defined in `tailwind.config.js`:
- Custom color palette
- Animation keyframes
- Font families
- Component classes

## 📱 Responsive Design

### Breakpoints
- **Mobile**: < 768px (single column layout)
- **Tablet**: 768px - 1024px (2-3 column grid)
- **Desktop**: > 1024px (3-4 column grid)

### Layout Features
- Responsive grid system
- Flexible card layouts
- Mobile-friendly navigation
- Touch-optimized interactions

## 🎭 Animation Details

### Page Animations
- **Initial Load**: Fade in with stagger effect
- **Route Changes**: Smooth transitions
- **Loading States**: Rotating spinners

### Component Animations
- **Card Hover**: Scale and glow effects
- **Button Interactions**: Press and hover states
- **Icon Rotations**: 360-degree spins on hover

### Micro-interactions
- **Toast Notifications**: Slide in from top
- **Form Validation**: Shake animations
- **Loading Indicators**: Pulse and rotate

## 🚀 Build and Deploy

### Development
```bash
npm run dev
```

### Production Build
```bash
npm run build
```

### Preview Production Build
```bash
npm run preview
```

## 🔧 Customization

### Theme Colors
Modify colors in `tailwind.config.js`:

```javascript
colors: {
  neon: {
    cyan: '#00ffff',
    purple: '#8b5cf6',
    amber: '#f59e0b',
  }
}
```

### Animations
Add custom animations in `tailwind.config.js`:

```javascript
animation: {
  'custom-animation': 'customKeyframe 2s ease-in-out infinite',
}
```

## 🐛 Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Ensure backend is running on port 8000
   - Check CORS configuration
   - Verify API endpoints

2. **Build Errors**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility
   - Verify all dependencies are installed

3. **Styling Issues**
   - Ensure Tailwind CSS is properly configured
   - Check PostCSS configuration
   - Verify custom CSS is imported

## 📦 Dependencies

### Production
- **react**: UI library
- **react-dom**: DOM rendering
- **react-router-dom**: Routing
- **axios**: HTTP client
- **framer-motion**: Animations
- **lucide-react**: Icons
- **react-hot-toast**: Notifications

### Development
- **vite**: Build tool
- **tailwindcss**: CSS framework
- **autoprefixer**: CSS processing
- **postcss**: CSS transformation
- **eslint**: Code linting

## 🎯 Performance

- **Code Splitting**: Automatic route-based splitting
- **Lazy Loading**: Components loaded on demand
- **Optimized Images**: WebP format support
- **Bundle Analysis**: Built-in Vite analyzer

## 🔄 State Management

- **Local State**: React hooks (useState, useEffect)
- **API State**: Axios interceptors for global error handling
- **Route State**: React Router for navigation state
- **Toast State**: React Hot Toast for notifications