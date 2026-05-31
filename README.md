# NEON VIBE: CYBER RUNNER v0.0.1-alpha 🌌

A premium, high-fidelity 3D arcade dodging game inside a rotating cyber tunnel. Built as a self-contained HTML/Three.js experience and containerized inside a **native macOS desktop application** via SwiftUI + WKWebView. 

🌐 **Live GitHub Repository**: [github.com/ihearttokyo/neon-vibe-dodger](https://github.com/ihearttokyo/neon-vibe-dodger)

---

## What's New: Native macOS Executable & Gameplay Upgrades 🚀

We have elevated this clone from a simple browser page into a complete **native macOS desktop experience** with premium gameplay enhancements:

1. **Native macOS App Container (`NeonVibe.app`)**:
   - Packaged as a native SwiftUI app hosting a customized `WKWebView` with full keyboard routing and local file serving context.
   - Built entirely with Swift Package Manager (no heavy `.xcodeproj` files needed!).
   - Features custom local assets loading with `.loadFileURL(_:allowingReadAccessTo:)` to bypass CORS security constraints while keeping full support for web-based CDN assets.
   
2. **Premium Solid Mesh Renderings**:
   - Replaced transparent wireframes with high-fidelity, solid flat-shaded `MeshPhongMaterial` models.
   - Implemented dynamic `PointLight` tracking that rides just ahead of the player vessel, casting gorgeous glossy reflections on moving hazards.

3. **True 3D Euclidean Physics**:
   - Replaced basic angular checks with accurate 3D distance collision checks (`Math.sqrt(dx^2 + dy^2 + dz^2)`), offering pixel-perfect hitbox precision for projectiles, powerups, shields, and near-misses.

4. **Endless 360° Spiral Looping**:
   - Removed strict angular clamping, allowing seamless infinite rotation wrapping around the circular track.

5. **Full Keyboard Menu Navigation**:
   - The game menus (Start, Pause, Upgrade Bay, Game Over) are 100% keyboard navigable with Arrow/WASD keys and highlighted by pulsing neon focus outlines.

6. **Cyber chiptune Music Streaming**:
   - Feeds a loopable retro soundtrack directly from the Internet Archive ("Unreeeal Superhero 3" by Kenët & Rez, CC-BY-NC-SA), with a robust offline fallback to the procedural synth engine if network is unavailable.

---

## Tech Stack
- **Game Core**: HTML5 / JavaScript (ES6)
- **3D Engine**: Three.js WebGL (via CDN)
- **Synth Engine**: Web Audio API
- **macOS Container**: SwiftUI + WKWebView in Swift 6.1 (SPM)
- **Styling**: Cyberpunk Glassmorphic CSS

---

## Native macOS Compilation & Setup 🍏

### 1. Build and Package
To build the `.app` bundle natively from the terminal using the Swift Compiler, run:
```bash
cd macOSWrapper
./Scripts/compile_and_run.sh
```
This script will:
1. Compile the Swift executable targets via `swift build -c release`.
2. Generate the full `.app` bundle under `macOSWrapper/NeonVibe.app`.
3. Apply ad-hoc developer code signing.
4. Launch the native desktop application.

### 2. Manual Execution
Once packaged, you can open the bundle directly:
```bash
open macOSWrapper/NeonVibe.app
```

---

## Running in Browser 🌐

Double-click `index.html` to open it in any modern browser, or run a fast local server:
```bash
python3 -m http.server 8000
```
Then navigate to `http://localhost:8000`.

---

## Controls 🎮
- **A / D (or Left / Right Arrows)**: Rotate around the tunnel
- **Left Click / Space**: Fire Plasma Blaster bullets
- **Shift (Hold)**: Thruster Boost (increases speed & score multiplier)
- **Escape**: Pause / Resume the game
- **Menus**: Arrow keys / WASD to select buttons/checkboxes, Enter / Space to confirm.

---

## Credits
- Chiptune Soundtrack: *Unreeeal Superhero 3* by **Kenët & Rez** (CC-BY-NC-SA).
- Created with absolute style and passion. 🌴🍹 *Now let's go home and sip some delicious mai tais with our friends!*
