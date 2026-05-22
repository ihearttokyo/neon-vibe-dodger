import SwiftUI
import WebKit

struct WebView: NSViewRepresentable {
    func makeNSView(context: Context) -> WKWebView {
        let preferences = WKWebpagePreferences()
        preferences.allowsContentJavaScript = true
        
        let configuration = WKWebViewConfiguration()
        configuration.defaultWebpagePreferences = preferences
        
        // Enable web security bypass and developer tools
        configuration.preferences.setValue(true, forKey: "developerExtrasEnabled")
        configuration.setValue(true, forKey: "allowUniversalAccessFromFileURLs")
        
        let webView = WKWebView(frame: .zero, configuration: configuration)
        webView.wantsLayer = true
        
        // Set transparent background to let window color show through
        webView.setValue(false, forKey: "drawsBackground")
        
        // Enable media playback without user gesture
        configuration.mediaTypesRequiringUserActionForPlayback = []
        
        // Load the local index.html resource
        if let url = Bundle.module.url(forResource: "index", withExtension: "html") {
            webView.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
        } else {
            // Fallback: search main bundle
            if let fallbackUrl = Bundle.main.url(forResource: "index", withExtension: "html") {
                webView.loadFileURL(fallbackUrl, allowingReadAccessTo: fallbackUrl.deletingLastPathComponent())
            } else {
                print("ERROR: Could not locate index.html in resources.")
            }
        }
        
        return webView
    }
    
    func updateNSView(_ nsView: WKWebView, context: Context) {}
}

@main
struct NeonVibeApp: App {
    var body: some Scene {
        Window("Neon Vibe Dodger", id: "main") {
            WebView()
                .frame(minWidth: 1024, minHeight: 768)
                .background(Color.black)
                .edgesIgnoringSafeArea(.all)
        }
        .windowStyle(.hiddenTitleBar)
        .windowToolbarStyle(.unifiedCompact)
    }
}
