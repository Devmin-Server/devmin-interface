
# UltraFast Theme for Devmin & Usermin

A modern, ultrafast single-page application theme for Devmin and Usermin, inspired by the "authentic-theme" project. This theme provides a sleek, professional, and highly customizable interface with advanced features for system administrators.

## Features

### 🎨 **Highly Configurable**
- Extensive theme options via Devmin/Usermin UI
- Custom logo upload support
- Multiple color schemes (Default, Blue, Purple, Green, Red, Dark)
- Custom CSS and JavaScript injection
- User preference persistence

### ⚡ **Performance & Navigation**
- Ultrafast loading with optimized assets
- Keyboard shortcuts (hotkeys) for quick navigation
- Favorites system for bookmarking frequently used modules
- Responsive design for desktop and mobile devices
- Smooth animations and transitions

### 🔔 **Notification System**
- Slide-out notification panel
- Real-time system alerts
- Notification badges and counters
- Customizable notification preferences

### 📁 **Enhanced Module Support**
- **File Manager**: Drag & drop uploads, code highlighting, image previews
- **ConfigServer Security & Firewall**: Enhanced interface and controls
- **Terminal**: Drop-down interface, multiple tabs, command history
- **Code Editor**: Syntax highlighting for multiple languages

### 🛠 **Developer Features**
- Modern web technologies (HTML5, CSS3, ES6+)
- Modular and maintainable codebase
- API for custom extensions
- Debug mode for development

### 🌍 **Internationalization**
- Multilingual support
- Easy translation workflow
- RTL language support

## Compatibility

- **Devmin**: 2.020+
- **Usermin**: 1.861+
- **Browsers**: Chrome 70+, Firefox 65+, Safari 12+, Edge 79+

## Installation

### Method 1: Direct Download

1. Download the latest `ultrafast-theme.wbt.gz` from the releases page
2. In Devmin, go to **Webmin Configuration** → **Themes**
3. Click **Install Theme** and upload the `.wbt.gz` file
4. Select **UltraFast Theme** from the theme dropdown
5. Click **Change** to apply

### Method 2: Manual Installation

1. Clone or download this repository
2. Copy the `theme-files` directory to your Webmin themes directory:
   ```bash
   cp -r theme-files/authentic-theme /usr/share/webmin/authentic-theme
   ```
3. Restart Webmin:
   ```bash
   systemctl restart webmin
   ```

### Method 3: Build from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ultrafast-theme.git
   cd ultrafast-theme
   ```

2. Build the theme package:
   ```bash
   ./build.sh
   ```

3. Install the generated `.wbt.gz` file via Devmin interface

## Configuration

### Basic Settings

Access theme settings through **Devmin Configuration** → **UltraFast Theme**:

- **Color Scheme**: Choose from predefined color schemes or create custom ones
- **Logo Upload**: Upload your organization's logo (PNG, JPG, SVG supported)
- **Animations**: Enable/disable smooth transitions and animations
- **Hotkeys**: Configure keyboard shortcuts
- **Sidebar**: Set default collapsed/expanded state

### Advanced Customization

#### Custom CSS
Add custom styles in the theme configuration:

```css
/* Example: Custom header styling */
.header {
    background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
}

/* Example: Custom card styling */
.card {
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
```

#### Custom JavaScript
Extend theme functionality:

```javascript
// Example: Add custom dashboard widget
document.addEventListener('DOMContentLoaded', function() {
    if (window.UltraFastTheme) {
        window.UltraFastTheme.addNotificationHandler(function(notification) {
            // Custom notification handling
            console.log('Custom notification:', notification);
        });
    }
});
```

#### Logo Upload
1. Go to theme settings
2. Click **Upload Logo**
3. Select your logo file (recommended: 200x50px, PNG format)
4. Click **Save** to apply

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Alt + S` | Toggle Sidebar |
| `Alt + N` | Toggle Notifications |
| `Alt + T` | Toggle Theme (Light/Dark) |
| `Alt + F` | Focus Search |
| `Alt + H` | Show Hotkey Help |
| `Esc` | Close Modals/Panels |

## Module Enhancements

### File Manager
- **Drag & Drop**: Upload files by dragging them into the file area
- **Code Highlighting**: Automatic syntax highlighting for code files
- **Image Preview**: Thumbnail previews for image files
- **Advanced Search**: Filter files by name, type, or date
- **Bulk Operations**: Select multiple files for batch operations

### Terminal
- **Multiple Tabs**: Open multiple terminal sessions
- **Command History**: Access previous commands with arrow keys
- **Auto-completion**: Tab completion for commands and file paths
- **Drop-down Mode**: Compact terminal that slides down from the top

### ConfigServer Security & Firewall
- **Enhanced Interface**: Improved layout and controls
- **Real-time Status**: Live updates of firewall status
- **Quick Actions**: One-click common operations
- **Rule Validation**: Syntax checking for firewall rules

## Troubleshooting

### Theme Not Applying
1. Clear browser cache and cookies
2. Restart Webmin service: `systemctl restart webmin`
3. Check file permissions in the theme directory
4. Verify theme files are properly installed

### Performance Issues
1. Disable animations in theme settings
2. Clear browser cache
3. Check system resources (CPU, memory)
4. Reduce number of dashboard widgets

### Customization Not Working
1. Verify CSS/JavaScript syntax
2. Check browser developer console for errors
3. Ensure custom code doesn't conflict with theme
4. Test in incognito/private browsing mode

### Mobile Display Issues
1. Clear mobile browser cache
2. Check viewport meta tag is present
3. Verify responsive CSS is loading
4. Test on different mobile devices/browsers

## Updates

### Automatic Updates
The theme can check for updates automatically:

1. Enable **Auto Update Check** in theme settings
2. Updates are checked every 24 hours
3. Notifications appear when updates are available

### Manual Updates
1. Download the latest version
2. Follow installation instructions
3. Settings and customizations are preserved

### Update Notifications
- Update availability notifications
- Changelog display
- One-click update process (when available)

## Development

### Project Structure
```
ultrafast-theme/
├── src/                          # React development files
├── theme-files/                  # Webmin theme files
│   ├── authentic-theme/
│   │   ├── index.cgi            # Main theme file
│   │   └── unauthenticated/
│   │       ├── css/             # Stylesheets
│   │       └── js/              # JavaScript files
│   ├── theme.info               # Theme metadata
│   └── config.info              # Configuration options
├── build.sh                     # Build script
├── package.json                 # Node.js dependencies
└── README.md                    # This file
```

### Building from Source

Requirements:
- Node.js 16+
- Perl 5.10+
- Basic build tools

Build steps:
```bash
# Install dependencies
npm install

# Build CSS and JavaScript
npm run build

# Create theme package
./build.sh

# Generated file: ultrafast-theme.wbt.gz
```

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Coding Standards
- Follow existing code style
- Comment complex functionality
- Test on multiple browsers
- Maintain backwards compatibility

## Support

### Community
- GitHub Issues: Report bugs and request features
- Discussions: Ask questions and share customizations
- Wiki: Documentation and tutorials

### Professional Support
For enterprise support and custom development:
- Email: support@ultrafast-theme.com
- Documentation: https://docs.ultrafast-theme.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-party Credits
- Icons: Lucide React
- Fonts: System fonts with fallbacks
- Inspiration: Authentic Theme project

## Changelog

### Version 2.0.0 (Current)
- Complete rewrite with modern technologies
- Enhanced mobile responsiveness
- Advanced notification system
- Improved module integration
- Better accessibility support

### Version 1.x
- Initial release
- Basic theme functionality
- Limited customization options

## Roadmap

### Version 2.1.0 (Planned)
- [ ] Enhanced dark mode
- [ ] More color scheme options
- [ ] Advanced file manager features
- [ ] Improved terminal emulation

### Version 2.2.0 (Future)
- [ ] Plugin system
- [ ] Advanced dashboard widgets
- [ ] Real-time collaboration features
- [ ] Enhanced security features

---

**Made with ❤️ for the Devmin/Usermin community**
