
# UltraFast Theme Installation Guide

## Quick Installation

### Option 1: Web Interface Installation (Recommended)

1. **Download the Theme**
   - Download `ultrafast-theme-2.0.0.wbt.gz` from the releases page
   - Save it to your local computer

2. **Access Devmin/Usermin**
   - Open your web browser
   - Navigate to your Devmin interface (usually `https://your-server:10000`)
   - Log in with administrator credentials

3. **Install the Theme**
   - Go to **Webmin Configuration** → **Themes**
   - Click **Install theme**
   - Click **Choose File** and select the downloaded `.wbt.gz` file
   - Click **Install**

4. **Apply the Theme**
   - In the **Current theme** dropdown, select **UltraFast Theme**
   - Click **Change**
   - The page will reload with the new theme

### Option 2: Command Line Installation

1. **Download and Extract**
   ```bash
   cd /tmp
   wget https://github.com/your-repo/ultrafast-theme/releases/download/v2.0.0/ultrafast-theme-2.0.0.wbt.gz
   tar -xzf ultrafast-theme-2.0.0.wbt.gz
   ```

2. **Install Files**
   ```bash
   # For Webmin
   sudo cp -r authentic-theme /usr/share/webmin/
   
   # For Usermin (if needed)
   sudo cp -r authentic-theme /usr/share/usermin/
   ```

3. **Set Permissions**
   ```bash
   sudo chown -R root:root /usr/share/webmin/authentic-theme
   sudo chmod -R 755 /usr/share/webmin/authentic-theme
   ```

4. **Restart Services**
   ```bash
   sudo systemctl restart webmin
   sudo systemctl restart usermin  # if using Usermin
   ```

## Post-Installation Configuration

### 1. Basic Theme Setup

1. **Access Theme Settings**
   - Go to **Webmin Configuration** → **UltraFast Theme**
   - Configure basic settings:
     - Color scheme
     - Animation preferences
     - Hotkey settings

2. **Upload Your Logo**
   - In theme settings, find the **Logo Upload** section
   - Click **Choose File** and select your logo
   - Recommended format: PNG, maximum size: 200x50 pixels
   - Click **Upload** to apply

### 2. Advanced Configuration

#### Custom CSS Styling
```css
/* Add in Custom CSS section */
:root {
    --primary-color: #your-brand-color;
    --secondary-color: #your-secondary-color;
}

.header {
    background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
}
```

#### Custom JavaScript
```javascript
// Add in Custom JavaScript section
document.addEventListener('DOMContentLoaded', function() {
    // Your custom functionality here
    console.log('UltraFast Theme loaded with custom scripts');
});
```

### 3. Module-Specific Configuration

#### File Manager Enhancement
The theme automatically enhances the File Manager module. No additional configuration is required.

#### Terminal Enhancement
1. Go to **Others** → **Command Shell**
2. The enhanced terminal interface will be automatically applied
3. Use `Ctrl+Shift+T` to open new terminal tabs

#### ConfigServer Security & Firewall
If you have CSF installed:
1. The theme will automatically detect and enhance the CSF interface
2. Additional quick-action buttons will appear
3. Real-time status updates will be enabled

## Verification

### 1. Check Theme is Active
- Look for the new header design with logo
- Verify the sidebar is present and functional
- Test the notification slider (bell icon in header)

### 2. Test Features
- **Hotkeys**: Press `Alt+H` to see the hotkey help
- **Sidebar**: Press `Alt+S` to toggle sidebar
- **Notifications**: Press `Alt+N` to open notification panel
- **Theme Toggle**: Press `Alt+T` to switch between light/dark themes

### 3. Mobile Responsiveness
- Access the interface from a mobile device
- Verify the layout adapts properly
- Test touch navigation

## Troubleshooting

### Theme Not Appearing
1. **Clear Browser Cache**
   ```bash
   # Clear browser cache and hard refresh (Ctrl+F5)
   ```

2. **Check File Permissions**
   ```bash
   sudo find /usr/share/webmin/authentic-theme -type f -exec chmod 644 {} \;
   sudo find /usr/share/webmin/authentic-theme -type d -exec chmod 755 {} \;
   ```

3. **Restart Webmin**
   ```bash
   sudo systemctl restart webmin
   ```

### Configuration Not Saving
1. **Check Config Directory Permissions**
   ```bash
   sudo chown -R webmin:webmin /etc/webmin
   sudo chmod 755 /etc/webmin
   ```

2. **Verify Theme Config File**
   ```bash
   ls -la /etc/webmin/authentic-theme/
   ```

### Performance Issues
1. **Disable Animations**
   - Go to theme settings
   - Set "Enable animations" to "No"
   - Save configuration

2. **Clear Theme Cache**
   ```bash
   sudo rm -rf /var/webmin/cache/authentic-theme/
   sudo systemctl restart webmin
   ```

### Custom CSS/JS Not Working
1. **Check Syntax**
   - Ensure CSS/JavaScript syntax is correct
   - Check browser developer console for errors

2. **Test in Isolation**
   - Add one custom rule at a time
   - Test after each addition

## Backup and Restore

### Backup Theme Settings
```bash
# Backup current theme configuration
sudo cp -r /etc/webmin/authentic-theme /etc/webmin/authentic-theme.backup

# Backup custom assets
sudo tar -czf ultrafast-theme-backup.tar.gz /etc/webmin/authentic-theme
```

### Restore Theme Settings
```bash
# Restore from backup
sudo tar -xzf ultrafast-theme-backup.tar.gz -C /
sudo systemctl restart webmin
```

## Uninstallation

### Complete Removal
```bash
# Remove theme files
sudo rm -rf /usr/share/webmin/authentic-theme

# Remove configuration
sudo rm -rf /etc/webmin/authentic-theme

# Restart Webmin
sudo systemctl restart webmin
```

### Switch to Default Theme
1. Go to **Webmin Configuration** → **Themes**
2. Select **Default Webmin Theme** from dropdown
3. Click **Change**

## Support

### Getting Help
- **Documentation**: Check the README.md file
- **Issues**: Report bugs on GitHub Issues
- **Community**: Join discussions on GitHub Discussions

### Log Files
Check these files for troubleshooting:
- `/var/webmin/miniserv.log` - Webmin server logs
- Browser Developer Console - JavaScript errors
- `/var/log/syslog` - System logs

### System Requirements
- **Webmin**: 2.020 or higher
- **Usermin**: 1.861 or higher (if using Usermin)
- **Browsers**: Chrome 70+, Firefox 65+, Safari 12+, Edge 79+
- **System**: Any Linux distribution supported by Webmin

---

For additional help, please consult the full README.md file or visit our support channels.
