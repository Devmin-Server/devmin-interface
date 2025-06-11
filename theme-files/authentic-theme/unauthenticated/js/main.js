
/*!
 * UltraFast Theme - Main JavaScript
 * Modern Devmin & Usermin Theme
 * Version: 2.0.0
 * License: MIT
 */

(function() {
    'use strict';

    // Theme configuration
    const ThemeConfig = {
        version: '2.0.0',
        name: 'UltraFast Theme',
        hotkeys: true,
        animations: true,
        notifications: true,
        autoSave: true,
        debugMode: false
    };

    // Main theme controller
    class UltraFastTheme {
        constructor() {
            this.init();
            this.bindEvents();
            this.initModules();
        }

        init() {
            console.log(`Initializing ${ThemeConfig.name} v${ThemeConfig.version}`);
            
            // Load user preferences
            this.loadPreferences();
            
            // Apply theme
            this.applyTheme();
            
            // Initialize components
            this.initSidebar();
            this.initNotifications();
            this.initHotkeys();
            this.initFileManager();
            this.initTerminal();
            this.initCodeHighlighting();
        }

        loadPreferences() {
            const saved = localStorage.getItem('ultrafast-theme-prefs');
            if (saved) {
                try {
                    const prefs = JSON.parse(saved);
                    Object.assign(ThemeConfig, prefs);
                } catch (e) {
                    console.warn('Failed to load theme preferences:', e);
                }
            }
        }

        savePreferences() {
            if (ThemeConfig.autoSave) {
                localStorage.setItem('ultrafast-theme-prefs', JSON.stringify(ThemeConfig));
            }
        }

        applyTheme() {
            document.documentElement.setAttribute('data-theme', ThemeConfig.colorScheme || 'default');
            
            if (!ThemeConfig.animations) {
                document.body.classList.add('no-animations');
            }
        }

        bindEvents() {
            // Window events
            window.addEventListener('resize', this.handleResize.bind(this));
            window.addEventListener('beforeunload', this.savePreferences.bind(this));
            
            // Theme toggle
            const themeToggle = document.querySelector('[data-toggle="theme"]');
            if (themeToggle) {
                themeToggle.addEventListener('click', this.toggleTheme.bind(this));
            }

            // Sidebar toggle
            const sidebarToggle = document.querySelector('[data-toggle="sidebar"]');
            if (sidebarToggle) {
                sidebarToggle.addEventListener('click', this.toggleSidebar.bind(this));
            }

            // Notification toggle
            const notificationToggle = document.querySelector('[data-toggle="notifications"]');
            if (notificationToggle) {
                notificationToggle.addEventListener('click', this.toggleNotifications.bind(this));
            }
        }

        // Sidebar functionality
        initSidebar() {
            this.sidebar = document.querySelector('.sidebar');
            if (!this.sidebar) return;

            // Load collapsed state
            if (localStorage.getItem('sidebar-collapsed') === 'true') {
                this.sidebar.classList.add('collapsed');
            }

            // Add mobile detection
            this.updateSidebarForMobile();
        }

        toggleSidebar() {
            if (!this.sidebar) return;

            this.sidebar.classList.toggle('collapsed');
            
            // Save state
            const isCollapsed = this.sidebar.classList.contains('collapsed');
            localStorage.setItem('sidebar-collapsed', isCollapsed);

            // Trigger resize event for content adjustment
            window.dispatchEvent(new Event('resize'));
        }

        updateSidebarForMobile() {
            const isMobile = window.innerWidth <= 768;
            
            if (isMobile) {
                this.sidebar?.classList.add('mobile');
            } else {
                this.sidebar?.classList.remove('mobile', 'mobile-open');
            }
        }

        // Notification system
        initNotifications() {
            this.notificationSlider = document.querySelector('.notification-slider');
            this.notifications = [];
            
            // Create notification container if it doesn't exist
            if (!this.notificationSlider) {
                this.createNotificationSlider();
            }

            // Listen for new notifications
            this.setupNotificationListeners();
        }

        createNotificationSlider() {
            const slider = document.createElement('div');
            slider.className = 'notification-slider';
            slider.innerHTML = `
                <div class="notification-header">
                    <h3>Notifications</h3>
                    <button class="btn-close" data-close="notifications">&times;</button>
                </div>
                <div class="notification-list"></div>
            `;
            document.body.appendChild(slider);
            this.notificationSlider = slider;

            // Bind close button
            slider.querySelector('[data-close="notifications"]')
                  .addEventListener('click', () => this.toggleNotifications());
        }

        setupNotificationListeners() {
            // Listen for Webmin/Usermin messages
            if (window.webmin_notifications) {
                window.webmin_notifications.forEach(notification => {
                    this.addNotification(notification);
                });
            }

            // Setup polling for new notifications
            setInterval(() => {
                this.checkForNewNotifications();
            }, 30000); // Check every 30 seconds
        }

        addNotification(notification) {
            const notificationEl = document.createElement('div');
            notificationEl.className = 'notification-item fade-in';
            
            const type = notification.type || 'info';
            const icon = this.getNotificationIcon(type);
            
            notificationEl.innerHTML = `
                <div class="notification-icon notification-${type}">
                    ${icon}
                </div>
                <div class="notification-content">
                    <div class="notification-title">${notification.title || 'System Message'}</div>
                    <div class="notification-message">${notification.message}</div>
                    <div class="notification-time">${this.formatTime(notification.time || new Date())}</div>
                </div>
            `;

            const list = this.notificationSlider.querySelector('.notification-list');
            list.insertBefore(notificationEl, list.firstChild);

            // Limit to 50 notifications
            const items = list.querySelectorAll('.notification-item');
            if (items.length > 50) {
                items[items.length - 1].remove();
            }

            // Show badge on notification toggle
            this.updateNotificationBadge();
        }

        getNotificationIcon(type) {
            const icons = {
                info: '&#9432;',
                success: '&#10004;',
                warning: '&#9888;',
                error: '&#10006;'
            };
            return icons[type] || icons.info;
        }

        formatTime(date) {
            return new Date(date).toLocaleTimeString();
        }

        toggleNotifications() {
            if (!this.notificationSlider) return;
            
            this.notificationSlider.classList.toggle('open');
        }

        updateNotificationBadge() {
            const badge = document.querySelector('.notification-badge');
            const unreadCount = this.getUnreadNotificationCount();
            
            if (badge) {
                badge.textContent = unreadCount;
                badge.style.display = unreadCount > 0 ? 'block' : 'none';
            }
        }

        getUnreadNotificationCount() {
            // Implementation depends on backend notification system
            return 0;
        }

        checkForNewNotifications() {
            // Implementation for polling new notifications
            // This would typically make an AJAX call to check for new messages
        }

        // Hotkey system
        initHotkeys() {
            if (!ThemeConfig.hotkeys) return;

            this.hotkeys = new Map([
                ['alt+s', () => this.toggleSidebar()],
                ['alt+n', () => this.toggleNotifications()],
                ['alt+t', () => this.toggleTheme()],
                ['alt+f', () => this.focusSearch()],
                ['alt+h', () => this.showHotkeyHelp()],
                ['esc', () => this.closeModals()]
            ]);

            document.addEventListener('keydown', this.handleHotkey.bind(this));
        }

        handleHotkey(event) {
            const key = this.getHotkeyString(event);
            const handler = this.hotkeys.get(key);
            
            if (handler) {
                event.preventDefault();
                handler();
            }
        }

        getHotkeyString(event) {
            const parts = [];
            
            if (event.ctrlKey) parts.push('ctrl');
            if (event.altKey) parts.push('alt');
            if (event.shiftKey) parts.push('shift');
            if (event.metaKey) parts.push('meta');
            
            const key = event.key.toLowerCase();
            if (key !== 'control' && key !== 'alt' && key !== 'shift' && key !== 'meta') {
                parts.push(key);
            }
            
            return parts.join('+');
        }

        showHotkeyHelp() {
            const modal = document.createElement('div');
            modal.className = 'hotkey-modal';
            modal.innerHTML = `
                <div class="modal-content">
                    <h3>Keyboard Shortcuts</h3>
                    <div class="hotkey-list">
                        <div class="hotkey-item">
                            <kbd>Alt + S</kbd>
                            <span>Toggle Sidebar</span>
                        </div>
                        <div class="hotkey-item">
                            <kbd>Alt + N</kbd>
                            <span>Toggle Notifications</span>
                        </div>
                        <div class="hotkey-item">
                            <kbd>Alt + T</kbd>
                            <span>Toggle Theme</span>
                        </div>
                        <div class="hotkey-item">
                            <kbd>Alt + F</kbd>
                            <span>Focus Search</span>
                        </div>
                        <div class="hotkey-item">
                            <kbd>Esc</kbd>
                            <span>Close Modals</span>
                        </div>
                    </div>
                    <button class="btn btn-primary" onclick="this.closest('.hotkey-modal').remove()">Close</button>
                </div>
            `;
            document.body.appendChild(modal);
        }

        focusSearch() {
            const searchInput = document.querySelector('input[type="search"], .search-input');
            if (searchInput) {
                searchInput.focus();
            }
        }

        closeModals() {
            // Close notification slider
            if (this.notificationSlider?.classList.contains('open')) {
                this.toggleNotifications();
            }
            
            // Close other modals
            document.querySelectorAll('.modal, .hotkey-modal').forEach(modal => {
                modal.remove();
            });
        }

        // File Manager enhancements
        initFileManager() {
            const fileManager = document.querySelector('.file-manager, #file-manager');
            if (!fileManager) return;

            this.setupFileDragDrop(fileManager);
            this.setupFilePreview(fileManager);
            this.setupFileSearch(fileManager);
        }

        setupFileDragDrop(container) {
            const dropZone = container.querySelector('.file-content');
            if (!dropZone) return;

            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, e => e.preventDefault());
            });

            dropZone.addEventListener('dragover', () => {
                dropZone.classList.add('drag-over');
            });

            dropZone.addEventListener('dragleave', () => {
                dropZone.classList.remove('drag-over');
            });

            dropZone.addEventListener('drop', (e) => {
                dropZone.classList.remove('drag-over');
                const files = e.dataTransfer.files;
                this.handleFileUpload(files);
            });
        }

        setupFilePreview(container) {
            container.addEventListener('click', (e) => {
                const fileItem = e.target.closest('.file-item');
                if (fileItem) {
                    const fileName = fileItem.dataset.filename;
                    this.previewFile(fileName);
                }
            });
        }

        setupFileSearch(container) {
            const searchInput = container.querySelector('.file-search');
            if (searchInput) {
                searchInput.addEventListener('input', (e) => {
                    this.filterFiles(e.target.value);
                });
            }
        }

        handleFileUpload(files) {
            // Implementation for file upload
            console.log('Uploading files:', files);
        }

        previewFile(fileName) {
            // Implementation for file preview
            console.log('Previewing file:', fileName);
        }

        filterFiles(searchTerm) {
            const fileItems = document.querySelectorAll('.file-item');
            fileItems.forEach(item => {
                const name = item.textContent.toLowerCase();
                const match = name.includes(searchTerm.toLowerCase());
                item.style.display = match ? '' : 'none';
            });
        }

        // Terminal enhancements
        initTerminal() {
            const terminals = document.querySelectorAll('.terminal, .xterm-container');
            terminals.forEach(terminal => {
                this.enhanceTerminal(terminal);
            });
        }

        enhanceTerminal(terminal) {
            // Add terminal toolbar
            const toolbar = document.createElement('div');
            toolbar.className = 'terminal-toolbar';
            toolbar.innerHTML = `
                <div class="terminal-tabs">
                    <div class="terminal-tab active">Terminal 1</div>
                    <button class="btn-new-tab">+</button>
                </div>
                <div class="terminal-actions">
                    <button class="btn-clear" title="Clear">Clear</button>
                    <button class="btn-settings" title="Settings">⚙</button>
                </div>
            `;
            
            terminal.insertBefore(toolbar, terminal.firstChild);

            // Bind terminal actions
            toolbar.querySelector('.btn-clear')?.addEventListener('click', () => {
                this.clearTerminal(terminal);
            });

            toolbar.querySelector('.btn-new-tab')?.addEventListener('click', () => {
                this.newTerminalTab();
            });
        }

        clearTerminal(terminal) {
            const output = terminal.querySelector('.terminal-output, .xterm-screen');
            if (output) {
                output.innerHTML = '';
            }
        }

        newTerminalTab() {
            // Implementation for new terminal tab
            console.log('Creating new terminal tab');
        }

        // Code highlighting
        initCodeHighlighting() {
            if (!ThemeConfig.codeHighlighting) return;

            // Find code blocks
            const codeBlocks = document.querySelectorAll('pre code, .code-editor, textarea[data-syntax]');
            codeBlocks.forEach(block => {
                this.highlightCode(block);
            });
        }

        highlightCode(element) {
            // Simple syntax highlighting implementation
            const language = element.dataset.language || 'text';
            const content = element.textContent;
            
            if (language === 'javascript' || language === 'js') {
                element.innerHTML = this.highlightJavaScript(content);
            } else if (language === 'css') {
                element.innerHTML = this.highlightCSS(content);
            } else if (language === 'html') {
                element.innerHTML = this.highlightHTML(content);
            }
        }

        highlightJavaScript(code) {
            return code
                .replace(/\b(function|var|let|const|if|else|for|while|return|class|extends)\b/g, '<span class="code-keyword">$1</span>')
                .replace(/(["'])([^"']*)\1/g, '<span class="code-string">$1$2$1</span>')
                .replace(/\/\*[\s\S]*?\*\/|\/\/.*$/gm, '<span class="code-comment">$&</span>')
                .replace(/\b(\d+)\b/g, '<span class="code-number">$1</span>');
        }

        highlightCSS(code) {
            return code
                .replace(/([a-z-]+)(?=\s*:)/g, '<span class="code-keyword">$1</span>')
                .replace(/(["'])([^"']*)\1/g, '<span class="code-string">$1$2$1</span>')
                .replace(/\/\*[\s\S]*?\*\//g, '<span class="code-comment">$&</span>');
        }

        highlightHTML(code) {
            return code
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/&lt;(\/?[a-z]+)([^&]*?)&gt;/gi, '<span class="code-keyword">&lt;$1<span class="code-string">$2</span>&gt;</span>');
        }

        // Module-specific initialization
        initModules() {
            // Check for specific Webmin/Usermin modules and enhance them
            this.initConfigServerModule();
            this.initApacheModule();
            this.initMySQLModule();
            this.initSystemInfoModule();
        }

        initConfigServerModule() {
            if (window.location.href.includes('csf') || document.querySelector('.csf-container')) {
                console.log('Initializing ConfigServer Security & Firewall enhancements');
                // Add CSF-specific enhancements
            }
        }

        initApacheModule() {
            if (window.location.href.includes('apache') || document.querySelector('.apache-container')) {
                console.log('Initializing Apache module enhancements');
                // Add Apache-specific enhancements
            }
        }

        initMySQLModule() {
            if (window.location.href.includes('mysql') || document.querySelector('.mysql-container')) {
                console.log('Initializing MySQL module enhancements');
                // Add MySQL-specific enhancements
            }
        }

        initSystemInfoModule() {
            if (window.location.href.includes('sysinfo') || document.querySelector('.sysinfo-container')) {
                console.log('Initializing System Info enhancements');
                this.initSystemCharts();
            }
        }

        initSystemCharts() {
            // Implementation for system monitoring charts
            const chartContainers = document.querySelectorAll('.chart-container');
            chartContainers.forEach(container => {
                this.createChart(container);
            });
        }

        createChart(container) {
            // Simple chart implementation
            const canvas = document.createElement('canvas');
            canvas.width = container.offsetWidth;
            canvas.height = 200;
            container.appendChild(canvas);
            
            // Chart rendering would go here
        }

        // Theme utilities
        toggleTheme() {
            const current = document.documentElement.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            ThemeConfig.colorScheme = newTheme;
            this.savePreferences();
        }

        handleResize() {
            this.updateSidebarForMobile();
            
            // Update other responsive components
            clearTimeout(this.resizeTimeout);
            this.resizeTimeout = setTimeout(() => {
                this.updateCharts();
            }, 250);
        }

        updateCharts() {
            // Update chart sizes on resize
            const charts = document.querySelectorAll('canvas');
            charts.forEach(chart => {
                const container = chart.parentElement;
                chart.width = container.offsetWidth;
            });
        }

        // Public API
        getVersion() {
            return ThemeConfig.version;
        }

        updateConfig(newConfig) {
            Object.assign(ThemeConfig, newConfig);
            this.savePreferences();
            this.applyTheme();
        }

        addNotificationHandler(handler) {
            if (typeof handler === 'function') {
                this.notificationHandlers = this.notificationHandlers || [];
                this.notificationHandlers.push(handler);
            }
        }
    }

    // Auto-update functionality
    class ThemeUpdater {
        constructor() {
            this.checkInterval = 24 * 60 * 60 * 1000; // 24 hours
            this.lastCheck = localStorage.getItem('theme-last-update-check');
            
            if (ThemeConfig.autoUpdateCheck) {
                this.scheduleUpdateCheck();
            }
        }

        scheduleUpdateCheck() {
            const now = Date.now();
            const lastCheck = parseInt(this.lastCheck) || 0;
            
            if (now - lastCheck > this.checkInterval) {
                this.checkForUpdates();
            }
            
            setTimeout(() => this.checkForUpdates(), this.checkInterval);
        }

        async checkForUpdates() {
            try {
                // Implementation would check for theme updates
                localStorage.setItem('theme-last-update-check', Date.now().toString());
                console.log('Checked for theme updates');
            } catch (error) {
                console.warn('Failed to check for updates:', error);
            }
        }
    }

    // Initialize theme when DOM is ready
    function initTheme() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                window.UltraFastTheme = new UltraFastTheme();
                window.ThemeUpdater = new ThemeUpdater();
            });
        } else {
            window.UltraFastTheme = new UltraFastTheme();
            window.ThemeUpdater = new ThemeUpdater();
        }
    }

    // Start initialization
    initTheme();

    // Export for external use
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = { UltraFastTheme, ThemeConfig };
    }

})();
