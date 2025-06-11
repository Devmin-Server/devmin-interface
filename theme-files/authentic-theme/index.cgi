
#!/usr/bin/perl
# UltraFast Theme - Main theme file for Devmin/Usermin
# Version: 2.0.0
# License: MIT

BEGIN { push(@INC, ".."); };
use strict;
use warnings;
use WebminCore;

# Theme configuration
our %theme_config = (
    'name' => 'UltraFast Theme',
    'version' => '2.0.0',
    'author' => 'UltraFast Team',
    'description' => 'Modern, ultrafast single-page application theme for Devmin and Usermin',
    'compatible_version' => '2.020',
    'usermin_compatible_version' => '1.861'
);

# Initialize theme
init_config();
ReadParse();

# Get theme setting
sub get_theme_setting {
    my ($key, $default) = @_;
    return $config{$key} || $default;
}

# Generate theme header
sub theme_header {
    my ($title, $extra_head) = @_;
    
    # Get user preferences
    my $color_scheme = get_theme_setting('theme_color_scheme', 'default');
    my $animations = get_theme_setting('theme_animations', 1);
    my $hotkeys = get_theme_setting('theme_hotkeys', 1);
    my $custom_css = get_theme_setting('theme_custom_css', '');
    my $custom_js = get_theme_setting('theme_custom_js', '');
    my $logo = get_theme_setting('theme_logo', '/lovable-uploads/0ffc6cf2-4a5d-4208-845a-0a7f7c387ff6.png');
    
    # Start HTML output
    print "Content-type: text/html\n\n";
    print <<EOF;
<!DOCTYPE html>
<html lang="en" data-theme="$color_scheme">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title - DEVIT Control Panel</title>
    
    <!-- Theme Stylesheets -->
    <link rel="stylesheet" href="$gconfig{'webprefix'}/unauthenticated/css/styles.css">
    
    <!-- Theme JavaScript -->
    <script src="$gconfig{'webprefix'}/unauthenticated/js/main.js"></script>
    
    <!-- Custom CSS -->
    <style id="custom-theme-css">
        $custom_css
    </style>
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="$gconfig{'webprefix'}/favicon.ico">
    
    $extra_head
</head>
<body class="theme-ultrafast" data-animations="$animations" data-hotkeys="$hotkeys">
    
    <!-- Header -->
    <header class="header">
        <div class="header-content">
            <div class="logo">
                <img src="$logo" alt="DEVIT Logo" class="logo-icon">
                <div class="logo-text">
                    <div class="logo-title">DEVIT</div>
                    <div class="logo-subtitle">Control Panel</div>
                </div>
            </div>
            
            <div class="header-actions">
                <button class="btn btn-icon" data-toggle="notifications" title="Notifications (Alt+N)">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                        <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
                    </svg>
                    <span class="notification-badge hidden">0</span>
                </button>
                <button class="btn btn-icon" data-toggle="theme" title="Toggle Theme (Alt+T)">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                    </svg>
                </button>
                <button class="btn btn-icon" data-toggle="sidebar" title="Toggle Sidebar (Alt+S)">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="3" y1="6" x2="21" y2="6"/>
                        <line x1="3" y1="12" x2="21" y2="12"/>
                        <line x1="3" y1="18" x2="21" y2="18"/>
                    </svg>
                </button>
            </div>
        </div>
    </header>
    
    <!-- Navigation -->
    <nav class="nav">
        <div class="nav-content">
EOF

    # Generate navigation items
    my @nav_items = (
        { 'title' => 'Dashboard', 'icon' => 'dashboard', 'href' => '/', 'hotkey' => 'D' },
        { 'title' => 'System', 'icon' => 'system', 'href' => '/system/', 'hotkey' => 'S' },
        { 'title' => 'Servers', 'icon' => 'servers', 'href' => '/servers/', 'hotkey' => 'R' },
        { 'title' => 'Tools', 'icon' => 'tools', 'href' => '/tools/', 'hotkey' => 'T' },
        { 'title' => 'Settings', 'icon' => 'settings', 'href' => '/settings/', 'hotkey' => 'G' }
    );
    
    foreach my $item (@nav_items) {
        my $active = ($ENV{'REQUEST_URI'} =~ /^$item->{'href'}/) ? ' active' : '';
        my $icon_svg = get_nav_icon($item->{'icon'});
        print <<EOF;
            <a href="$item->{'href'}" class="nav-item$active" data-hotkey="$item->{'hotkey'}">
                <span class="nav-icon">$icon_svg</span>
                <span class="nav-text">$item->{'title'}</span>
                <span class="hotkey-hint">Alt+$item->{'hotkey'}</span>
            </a>
EOF
    }
    
    print <<EOF;
        </div>
    </nav>
    
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
EOF

    # Generate sidebar content
    generate_sidebar();
    
    print <<EOF;
    </aside>
    
    <!-- Main Content -->
    <main class="main-content" id="main-content">
        <div class="content-wrapper">
EOF

    # Custom JavaScript
    if ($custom_js) {
        print "<script>$custom_js</script>";
    }
}

# Get navigation icon SVG
sub get_nav_icon {
    my ($icon) = @_;
    
    my %icons = (
        'dashboard' => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/></svg>',
        'system' => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
        'servers' => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
        'tools' => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
        'settings' => '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>'
    );
    
    return $icons{$icon} || '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg>';
}

# ... keep existing code (generate_sidebar, theme_footer, and all other functions remain the same)

# Main execution
if (!$in{'action'}) {
    theme_header("Dashboard");
    
    # Dashboard content with DEVIT branding
    print <<EOF;
    <div class="dashboard">
        <div class="dashboard-header">
            <h1>DEVIT Control Panel</h1>
            <p>Welcome to your development infrastructure management system</p>
        </div>
        
        <div class="dashboard-stats">
            <div class="stat-card">
                <div class="stat-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="4" y="4" width="16" height="6" rx="1"/>
                        <rect x="4" y="14" width="16" height="6" rx="1"/>
                        <path d="M22 14h-4m-2 0h-2m8-6h-6"/>
                    </svg>
                </div>
                <div class="stat-content">
                    <div class="stat-title">CPU Usage</div>
                    <div class="stat-value" id="cpu-usage">--</div>
                </div>
            </div>
            
            <div class="stat-card">
                <div class="stat-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                    </svg>
                </div>
                <div class="stat-content">
                    <div class="stat-title">Memory Usage</div>
                    <div class="stat-value" id="memory-usage">--</div>
                </div>
            </div>
            
            <div class="stat-card">
                <div class="stat-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="13" r="8"/>
                        <path d="M12 9v4l2 2"/>
                        <path d="M5 7a15.1 15.1 0 0 1 4-4"/>
                        <path d="M19 7a15.1 15.1 0 0 0-4-4"/>
                    </svg>
                </div>
                <div class="stat-content">
                    <div class="stat-title">Disk Usage</div>
                    <div class="stat-value" id="disk-usage">--</div>
                </div>
            </div>
            
            <div class="stat-card">
                <div class="stat-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="12,6 12,12 16,14"/>
                    </svg>
                </div>
                <div class="stat-content">
                    <div class="stat-title">Uptime</div>
                    <div class="stat-value" id="uptime">--</div>
                </div>
            </div>
        </div>
        
        <div class="dashboard-content">
            <div class="dashboard-section">
                <h2>Quick Actions</h2>
                <div class="action-grid">
                    <button class="action-card" onclick="location.href='/apache/'">
                        <div class="action-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="10"/>
                                <line x1="2" y1="12" x2="22" y2="12"/>
                                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
                            </svg>
                        </div>
                        <div class="action-title">Apache Web Server</div>
                    </button>
                    
                    <button class="action-card" onclick="location.href='/mysql/'">
                        <div class="action-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <ellipse cx="12" cy="5" rx="9" ry="3"/>
                                <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/>
                                <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>
                            </svg>
                        </div>
                        <div class="action-title">MySQL Database</div>
                    </button>
                    
                    <button class="action-card" onclick="location.href='/firewall/'">
                        <div class="action-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            </svg>
                        </div>
                        <div class="action-title">Firewall</div>
                    </button>
                    
                    <button class="action-card" onclick="location.href='/backup-config/'">
                        <div class="action-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                                <polyline points="14,2 14,8 20,8"/>
                                <line x1="16" y1="13" x2="8" y2="13"/>
                                <line x1="16" y1="17" x2="8" y2="17"/>
                                <polyline points="10,9 9,9 8,9"/>
                            </svg>
                        </div>
                        <div class="action-title">Backup</div>
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Load dashboard data
        if (window.UltraFastTheme) {
            setInterval(() => {
                fetch('?action=get_system_status')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('cpu-usage').textContent = data.cpu_usage + '%';
                        document.getElementById('memory-usage').textContent = data.memory_usage + '%';
                        document.getElementById('disk-usage').textContent = data.disk_usage + '%';
                        document.getElementById('uptime').textContent = formatUptime(data.uptime);
                    });
            }, 5000);
        }
        
        function formatUptime(seconds) {
            const days = Math.floor(seconds / 86400);
            const hours = Math.floor((seconds % 86400) / 3600);
            const minutes = Math.floor((seconds % 3600) / 60);
            return days + 'd ' + hours + 'h ' + minutes + 'm';
        }
    </script>
EOF
    
    theme_footer();
}

1;
