
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

# Get theme settings
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
    my $logo = get_theme_setting('theme_logo', '');
    
    # Start HTML output
    print "Content-type: text/html\n\n";
    print <<EOF;
<!DOCTYPE html>
<html lang="en" data-theme="$color_scheme">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title - Devmin</title>
    
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
EOF

    if ($logo) {
        print "<img src='$logo' alt='Logo' class='logo-icon'>";
    } else {
        print "<div class='logo-icon'>🛡️</div>";
    }
    
    print <<EOF;
                <div class="logo-text">
                    <div class="logo-title">Devmin</div>
                    <div class="logo-subtitle">System Administration</div>
                </div>
            </div>
            
            <div class="header-actions">
                <button class="btn btn-icon" data-toggle="notifications" title="Notifications (Alt+N)">
                    🔔
                    <span class="notification-badge hidden">0</span>
                </button>
                <button class="btn btn-icon" data-toggle="theme" title="Toggle Theme (Alt+T)">
                    🌙
                </button>
                <button class="btn btn-icon" data-toggle="sidebar" title="Toggle Sidebar (Alt+S)">
                    ☰
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
        { 'title' => 'Dashboard', 'icon' => '📊', 'href' => '/', 'hotkey' => 'D' },
        { 'title' => 'System', 'icon' => '⚙️', 'href' => '/system/', 'hotkey' => 'S' },
        { 'title' => 'Servers', 'icon' => '🖥️', 'href' => '/servers/', 'hotkey' => 'R' },
        { 'title' => 'Tools', 'icon' => '🔧', 'href' => '/tools/', 'hotkey' => 'T' },
        { 'title' => 'Settings', 'icon' => '⚙️', 'href' => '/settings/', 'hotkey' => 'G' }
    );
    
    foreach my $item (@nav_items) {
        my $active = ($ENV{'REQUEST_URI'} =~ /^$item->{'href'}/) ? ' active' : '';
        print <<EOF;
            <a href="$item->{'href'}" class="nav-item$active" data-hotkey="$item->{'hotkey'}">
                <span class="nav-icon">$item->{'icon'}</span>
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

# Generate sidebar
sub generate_sidebar {
    # Get available modules
    my @modules = get_visible_modules();
    
    print "<div class='sidebar-section'>";
    print "<h3 class='sidebar-title'>Modules</h3>";
    
    foreach my $module (@modules) {
        my $icon = get_module_icon($module);
        my $active = ($ENV{'SCRIPT_NAME'} =~ /$module/) ? ' active' : '';
        
        print <<EOF;
        <a href="/$module/" class="sidebar-item$active">
            <span class="sidebar-icon">$icon</span>
            <span class="sidebar-text">$module</span>
        </a>
EOF
    }
    
    print "</div>";
    
    # Quick actions section
    print "<div class='sidebar-section'>";
    print "<h3 class='sidebar-title'>Quick Actions</h3>";
    
    my @quick_actions = (
        { 'title' => 'Restart Services', 'icon' => '🔄', 'action' => 'restart-services' },
        { 'title' => 'System Backup', 'icon' => '💾', 'action' => 'backup' },
        { 'title' => 'View Logs', 'icon' => '📋', 'action' => 'logs' },
        { 'title' => 'Check Updates', 'icon' => '⬆️', 'action' => 'updates' }
    );
    
    foreach my $action (@quick_actions) {
        print <<EOF;
        <button class="sidebar-item sidebar-action" data-action="$action->{'action'}">
            <span class="sidebar-icon">$action->{'icon'}</span>
            <span class="sidebar-text">$action->{'title'}</span>
        </button>
EOF
    }
    
    print "</div>";
}

# Get module icon
sub get_module_icon {
    my ($module) = @_;
    
    my %icons = (
        'apache' => '🌐',
        'mysql' => '🗄️',
        'postgresql' => '🗄️',
        'bind8' => '🌍',
        'dhcpd' => '📡',
        'postfix' => '📧',
        'dovecot' => '📬',
        'samba' => '📁',
        'squid' => '🔄',
        'ipsec' => '🔒',
        'firewall' => '🛡️',
        'fail2ban' => '🚫',
        'cron' => '⏰',
        'mount' => '💽',
        'fdisk' => '💾',
        'backup-config' => '💾',
        'webmin' => '⚙️',
        'usermin' => '👤'
    );
    
    return $icons{$module} || '📦';
}

# Theme footer
sub theme_footer {
    print <<EOF;
        </div>
    </main>
    
    <!-- Notification Slider -->
    <div class="notification-slider" id="notification-slider">
        <div class="notification-header">
            <h3>Notifications</h3>
            <button class="btn-close" data-close="notifications">&times;</button>
        </div>
        <div class="notification-list" id="notification-list">
            <!-- Notifications will be dynamically added here -->
        </div>
    </div>
    
    <!-- Loading overlay -->
    <div class="loading-overlay hidden" id="loading-overlay">
        <div class="loading-spinner"></div>
        <div class="loading-text">Loading...</div>
    </div>
    
    <!-- Theme initialization -->
    <script>
        // Initialize theme with server-side configuration
        if (window.UltraFastTheme) {
            window.UltraFastTheme.updateConfig({
                colorScheme: '$color_scheme',
                animations: $animations,
                hotkeys: $hotkeys,
                serverUrl: '$gconfig{"webprefix"}',
                version: '$theme_config{"version"}'
            });
        }
    </script>
    
</body>
</html>
EOF
}

# Get visible modules for current user
sub get_visible_modules {
    my @modules;
    
    # This would normally read from Webmin's module list
    # For demonstration, we'll return a sample list
    @modules = qw(
        apache mysql postgresql bind8 dhcpd postfix dovecot
        samba squid firewall fail2ban cron mount fdisk
        backup-config webmin usermin
    );
    
    return @modules;
}

# AJAX handlers
if ($in{'action'}) {
    handle_ajax_request();
    exit;
}

sub handle_ajax_request {
    my $action = $in{'action'};
    
    print "Content-type: application/json\n\n";
    
    if ($action eq 'get_notifications') {
        handle_get_notifications();
    } elsif ($action eq 'save_preferences') {
        handle_save_preferences();
    } elsif ($action eq 'get_system_status') {
        handle_get_system_status();
    } elsif ($action eq 'upload_logo') {
        handle_upload_logo();
    } else {
        print '{"error": "Unknown action"}';
    }
}

sub handle_get_notifications {
    # Get system notifications
    my @notifications = (
        {
            'id' => 1,
            'type' => 'info',
            'title' => 'System Update Available',
            'message' => 'A new system update is available for installation.',
            'time' => time(),
            'read' => 0
        },
        {
            'id' => 2,
            'type' => 'warning',
            'title' => 'High CPU Usage',
            'message' => 'CPU usage has been above 80% for the last 10 minutes.',
            'time' => time() - 600,
            'read' => 0
        }
    );
    
    print to_json(\@notifications);
}

sub handle_save_preferences {
    # Save user preferences
    my $prefs = from_json($in{'preferences'});
    
    foreach my $key (keys %$prefs) {
        if ($key =~ /^theme_/) {
            $config{$key} = $prefs->{$key};
        }
    }
    
    write_file("$config_directory/config", \%config);
    print '{"success": true}';
}

sub handle_get_system_status {
    # Get basic system information
    my %status = (
        'cpu_usage' => get_cpu_usage(),
        'memory_usage' => get_memory_usage(),
        'disk_usage' => get_disk_usage(),
        'load_average' => get_load_average(),
        'uptime' => get_uptime()
    );
    
    print to_json(\%status);
}

sub handle_upload_logo {
    # Handle logo upload
    my $upload = $in{'logo_file'};
    
    if ($upload) {
        my $filename = $upload;
        $filename =~ s/.*[\/\\]//;
        
        # Save uploaded file
        my $logo_path = "$config_directory/theme_logo_$filename";
        
        open(my $fh, '>', $logo_path) or die "Cannot write to $logo_path: $!";
        binmode($fh);
        print $fh $upload;
        close($fh);
        
        # Update configuration
        $config{'theme_logo'} = "$gconfig{'webprefix'}/theme_logo_$filename";
        write_file("$config_directory/config", \%config);
        
        print to_json({'success' => 1, 'logo_url' => $config{'theme_logo'}});
    } else {
        print '{"error": "No file uploaded"}';
    }
}

# Utility functions for system information
sub get_cpu_usage {
    # Implementation depends on the system
    return int(rand(100));
}

sub get_memory_usage {
    # Implementation depends on the system
    return int(rand(100));
}

sub get_disk_usage {
    # Implementation depends on the system
    return int(rand(100));
}

sub get_load_average {
    if (open(my $fh, '<', '/proc/loadavg')) {
        my $line = <$fh>;
        close($fh);
        my @load = split(/\s+/, $line);
        return $load[0];
    }
    return '0.00';
}

sub get_uptime {
    if (open(my $fh, '<', '/proc/uptime')) {
        my $line = <$fh>;
        close($fh);
        my ($uptime) = split(/\s+/, $line);
        return int($uptime);
    }
    return 0;
}

# JSON utilities
sub to_json {
    my ($data) = @_;
    
    # Simple JSON encoding (for complex data, use JSON module)
    if (ref($data) eq 'ARRAY') {
        return '[' . join(',', map { to_json($_) } @$data) . ']';
    } elsif (ref($data) eq 'HASH') {
        my @pairs;
        foreach my $key (keys %$data) {
            push @pairs, '"' . $key . '":' . to_json($data->{$key});
        }
        return '{' . join(',', @pairs) . '}';
    } elsif ($data =~ /^-?\d+(\.\d+)?$/) {
        return $data;
    } else {
        $data =~ s/\\/\\\\/g;
        $data =~ s/"/\\"/g;
        $data =~ s/\n/\\n/g;
        $data =~ s/\r/\\r/g;
        $data =~ s/\t/\\t/g;
        return '"' . $data . '"';
    }
}

sub from_json {
    my ($json) = @_;
    # Simple JSON decoding (for complex data, use JSON module)
    # This is a basic implementation - in production, use a proper JSON library
    return eval $json;
}

# Main execution
if (!$in{'action'}) {
    theme_header("Dashboard");
    
    # Dashboard content
    print <<EOF;
    <div class="dashboard">
        <div class="dashboard-header">
            <h1>System Dashboard</h1>
            <p>Welcome to your Devmin control panel</p>
        </div>
        
        <div class="dashboard-stats">
            <div class="stat-card">
                <div class="stat-icon">💻</div>
                <div class="stat-content">
                    <div class="stat-title">CPU Usage</div>
                    <div class="stat-value" id="cpu-usage">--</div>
                </div>
            </div>
            
            <div class="stat-card">
                <div class="stat-icon">🧠</div>
                <div class="stat-content">
                    <div class="stat-title">Memory Usage</div>
                    <div class="stat-value" id="memory-usage">--</div>
                </div>
            </div>
            
            <div class="stat-card">
                <div class="stat-icon">💾</div>
                <div class="stat-content">
                    <div class="stat-title">Disk Usage</div>
                    <div class="stat-value" id="disk-usage">--</div>
                </div>
            </div>
            
            <div class="stat-card">
                <div class="stat-icon">⏱️</div>
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
                        <div class="action-icon">🌐</div>
                        <div class="action-title">Apache Web Server</div>
                    </button>
                    
                    <button class="action-card" onclick="location.href='/mysql/'">
                        <div class="action-icon">🗄️</div>
                        <div class="action-title">MySQL Database</div>
                    </button>
                    
                    <button class="action-card" onclick="location.href='/firewall/'">
                        <div class="action-icon">🛡️</div>
                        <div class="action-title">Firewall</div>
                    </button>
                    
                    <button class="action-card" onclick="location.href='/backup-config/'">
                        <div class="action-icon">💾</div>
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
