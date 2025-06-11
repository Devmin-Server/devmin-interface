
import React, { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Badge } from '@/components/ui/badge';
import { 
  Download, 
  Settings, 
  Palette, 
  Code, 
  Smartphone, 
  Zap, 
  Shield, 
  Globe,
  FileText,
  Terminal,
  Bell,
  Star,
  Upload,
  Keyboard
} from 'lucide-react';

const Index = () => {
  const [activeDemo, setActiveDemo] = useState('dashboard');

  const features = [
    {
      icon: <Settings className="w-6 h-6" />,
      title: "Highly Configurable",
      description: "Extensive theme options via Devmin/Usermin UI with custom styles and logo embedding"
    },
    {
      icon: <Keyboard className="w-6 h-6" />,
      title: "Hotkeys & Favorites",
      description: "Quick navigation shortcuts and favorite module bookmarking system"
    },
    {
      icon: <Bell className="w-6 h-6" />,
      title: "Notification Slider",
      description: "Instant access to system messages and alerts with slide-out panel"
    },
    {
      icon: <FileText className="w-6 h-6" />,
      title: "Extended Module Support",
      description: "Enhanced File Manager and ConfigServer Security & Firewall integration"
    },
    {
      icon: <Code className="w-6 h-6" />,
      title: "Code Highlighting",
      description: "Syntax highlighting for file viewing and editing with multiple themes"
    },
    {
      icon: <Terminal className="w-6 h-6" />,
      title: "Enhanced Terminal",
      description: "Drop-down interface for Terminal and Command Shell modules"
    },
    {
      icon: <Smartphone className="w-6 h-6" />,
      title: "Responsive Design",
      description: "Optimized for desktop and mobile with adaptive layouts"
    },
    {
      icon: <Zap className="w-6 h-6" />,
      title: "Easy Updates",
      description: "Manual and automatic theme update support with version management"
    },
    {
      icon: <Upload className="w-6 h-6" />,
      title: "Custom Assets",
      description: "Upload custom CSS, JavaScript, and logos through the interface"
    },
    {
      icon: <Globe className="w-6 h-6" />,
      title: "Multilingual",
      description: "Complete multilingual support with easy translation workflow"
    }
  ];

  const technicalSpecs = [
    { label: "Devmin Compatibility", value: "2.020+" },
    { label: "Usermin Compatibility", value: "1.861+" },
    { label: "License", value: "MIT" },
    { label: "Technologies", value: "HTML5, CSS3, Modern JavaScript" },
    { label: "Package Format", value: ".wbt.gz" }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-slate-200 sticky top-0 z-50">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Shield className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-slate-900">UltraFast Theme</h1>
                <p className="text-sm text-slate-600">Modern Devmin & Usermin Theme</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Badge variant="secondary">v2.0.0</Badge>
              <Button>
                <Download className="w-4 h-4 mr-2" />
                Download Theme
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 px-6">
        <div className="container mx-auto text-center">
          <h2 className="text-5xl font-bold text-slate-900 mb-6">
            The Ultimate <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">Devmin Theme</span>
          </h2>
          <p className="text-xl text-slate-600 mb-8 max-w-3xl mx-auto">
            A modern, ultrafast single-page application theme for Devmin and Usermin, 
            featuring advanced customization, responsive design, and powerful developer tools.
          </p>
          <div className="flex justify-center space-x-4">
            <Button size="lg" className="bg-gradient-to-r from-blue-600 to-purple-600">
              <Download className="w-5 h-5 mr-2" />
              Download Now
            </Button>
            <Button size="lg" variant="outline">
              <Code className="w-5 h-5 mr-2" />
              View Documentation
            </Button>
          </div>
        </div>
      </section>

      {/* Demo Tabs */}
      <section className="py-16 px-6 bg-white">
        <div className="container mx-auto">
          <h3 className="text-3xl font-bold text-center text-slate-900 mb-12">Interactive Demo</h3>
          <Tabs value={activeDemo} onValueChange={setActiveDemo} className="w-full">
            <TabsList className="grid w-full grid-cols-4 max-w-2xl mx-auto">
              <TabsTrigger value="dashboard">Dashboard</TabsTrigger>
              <TabsTrigger value="filemanager">File Manager</TabsTrigger>
              <TabsTrigger value="terminal">Terminal</TabsTrigger>
              <TabsTrigger value="settings">Settings</TabsTrigger>
            </TabsList>
            
            <TabsContent value="dashboard" className="mt-8">
              <Card className="p-8 bg-gradient-to-br from-slate-900 to-slate-800 text-white">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="space-y-4">
                    <h4 className="text-xl font-semibold">System Overview</h4>
                    <div className="space-y-2">
                      <div className="flex justify-between">
                        <span>CPU Usage</span>
                        <span className="text-green-400">23%</span>
                      </div>
                      <div className="flex justify-between">
                        <span>Memory</span>
                        <span className="text-blue-400">67%</span>
                      </div>
                      <div className="flex justify-between">
                        <span>Disk Space</span>
                        <span className="text-yellow-400">45%</span>
                      </div>
                    </div>
                  </div>
                  <div className="space-y-4">
                    <h4 className="text-xl font-semibold">Quick Actions</h4>
                    <div className="grid grid-cols-2 gap-2">
                      <Button variant="secondary" size="sm">Restart</Button>
                      <Button variant="secondary" size="sm">Backup</Button>
                      <Button variant="secondary" size="sm">Logs</Button>
                      <Button variant="secondary" size="sm">Updates</Button>
                    </div>
                  </div>
                  <div className="space-y-4">
                    <h4 className="text-xl font-semibold">Recent Activity</h4>
                    <div className="space-y-2 text-sm">
                      <div>User login: admin</div>
                      <div>Service restart: apache2</div>
                      <div>Backup completed</div>
                    </div>
                  </div>
                </div>
              </Card>
            </TabsContent>

            <TabsContent value="filemanager" className="mt-8">
              <Card className="p-8">
                <div className="space-y-4">
                  <h4 className="text-xl font-semibold">Enhanced File Manager</h4>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <h5 className="font-medium mb-2">Features:</h5>
                      <ul className="space-y-1 text-sm text-slate-600">
                        <li>• Drag & drop file uploads</li>
                        <li>• Code syntax highlighting</li>
                        <li>• Image previews</li>
                        <li>• Advanced search & filtering</li>
                        <li>• Bulk operations</li>
                      </ul>
                    </div>
                    <div className="bg-slate-100 rounded-lg p-4 font-mono text-sm">
                      <div className="text-blue-600">/var/www/html/</div>
                      <div className="ml-4">├── index.html</div>
                      <div className="ml-4">├── css/</div>
                      <div className="ml-4">├── js/</div>
                      <div className="ml-4">└── assets/</div>
                    </div>
                  </div>
                </div>
              </Card>
            </TabsContent>

            <TabsContent value="terminal" className="mt-8">
              <Card className="p-8 bg-black text-green-400">
                <div className="space-y-4">
                  <h4 className="text-xl font-semibold text-white">Enhanced Terminal</h4>
                  <div className="font-mono text-sm space-y-2">
                    <div>root@server:~$ systemctl status apache2</div>
                    <div className="text-green-300">● apache2.service - The Apache HTTP Server</div>
                    <div className="text-green-300">   Loaded: loaded (/lib/systemd/system/apache2.service)</div>
                    <div className="text-green-300">   Active: active (running) since Mon 2024-01-01 10:00:00</div>
                    <div>root@server:~$ <span className="animate-pulse">_</span></div>
                  </div>
                  <div className="text-white text-sm">
                    <strong>Features:</strong> Tab completion, command history, multiple sessions, syntax highlighting
                  </div>
                </div>
              </Card>
            </TabsContent>

            <TabsContent value="settings" className="mt-8">
              <Card className="p-8">
                <div className="space-y-6">
                  <h4 className="text-xl font-semibold">Theme Configuration</h4>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="space-y-4">
                      <h5 className="font-medium">Appearance</h5>
                      <div className="space-y-2">
                        <label className="block text-sm">Color Scheme</label>
                        <div className="flex space-x-2">
                          <div className="w-8 h-8 bg-blue-500 rounded cursor-pointer"></div>
                          <div className="w-8 h-8 bg-purple-500 rounded cursor-pointer"></div>
                          <div className="w-8 h-8 bg-green-500 rounded cursor-pointer"></div>
                          <div className="w-8 h-8 bg-red-500 rounded cursor-pointer"></div>
                        </div>
                      </div>
                      <div className="space-y-2">
                        <label className="block text-sm">Logo Upload</label>
                        <Button variant="outline" size="sm">
                          <Upload className="w-4 h-4 mr-2" />
                          Upload Logo
                        </Button>
                      </div>
                    </div>
                    <div className="space-y-4">
                      <h5 className="font-medium">Behavior</h5>
                      <div className="space-y-2">
                        <div className="flex items-center space-x-2">
                          <input type="checkbox" id="animations" />
                          <label htmlFor="animations" className="text-sm">Enable animations</label>
                        </div>
                        <div className="flex items-center space-x-2">
                          <input type="checkbox" id="hotkeys" />
                          <label htmlFor="hotkeys" className="text-sm">Enable hotkeys</label>
                        </div>
                        <div className="flex items-center space-x-2">
                          <input type="checkbox" id="notifications" />
                          <label htmlFor="notifications" className="text-sm">Show notifications</label>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      </section>

      {/* Features Grid */}
      <section className="py-16 px-6 bg-slate-50">
        <div className="container mx-auto">
          <h3 className="text-3xl font-bold text-center text-slate-900 mb-12">Powerful Features</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <Card key={index} className="p-6 hover:shadow-lg transition-shadow">
                <div className="flex items-start space-x-4">
                  <div className="p-2 bg-blue-100 rounded-lg text-blue-600">
                    {feature.icon}
                  </div>
                  <div>
                    <h4 className="font-semibold text-slate-900 mb-2">{feature.title}</h4>
                    <p className="text-sm text-slate-600">{feature.description}</p>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Technical Specifications */}
      <section className="py-16 px-6 bg-white">
        <div className="container mx-auto">
          <h3 className="text-3xl font-bold text-center text-slate-900 mb-12">Technical Specifications</h3>
          <div className="max-w-2xl mx-auto">
            <Card className="p-8">
              <div className="space-y-4">
                {technicalSpecs.map((spec, index) => (
                  <div key={index} className="flex justify-between items-center py-2 border-b border-slate-100 last:border-b-0">
                    <span className="font-medium text-slate-700">{spec.label}</span>
                    <span className="text-slate-900">{spec.value}</span>
                  </div>
                ))}
              </div>
            </Card>
          </div>
        </div>
      </section>

      {/* Installation Guide */}
      <section className="py-16 px-6 bg-slate-900 text-white">
        <div className="container mx-auto">
          <h3 className="text-3xl font-bold text-center mb-12">Quick Installation</h3>
          <div className="max-w-4xl mx-auto">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
              <div className="space-y-4">
                <div className="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto">
                  <span className="text-2xl font-bold">1</span>
                </div>
                <h4 className="text-xl font-semibold">Download</h4>
                <p className="text-slate-300">Download the .wbt.gz theme package</p>
              </div>
              <div className="space-y-4">
                <div className="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto">
                  <span className="text-2xl font-bold">2</span>
                </div>
                <h4 className="text-xl font-semibold">Install</h4>
                <p className="text-slate-300">Upload via Devmin theme installer</p>
              </div>
              <div className="space-y-4">
                <div className="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto">
                  <span className="text-2xl font-bold">3</span>
                </div>
                <h4 className="text-xl font-semibold">Configure</h4>
                <p className="text-slate-300">Customize colors, logos, and settings</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 px-6 bg-slate-800 text-slate-300">
        <div className="container mx-auto text-center">
          <p>&copy; 2024 UltraFast Theme. Released under MIT License.</p>
          <p className="mt-2 text-sm">Compatible with Devmin 2.020+ and Usermin 1.861+</p>
        </div>
      </footer>
    </div>
  );
};

export default Index;
