# NEON VIBE: CYBER RUNNER 🌌

A premium, high-fidelity 3D arcade dodging game inside a rotating cyber tunnel. Built entirely in a **single self-contained HTML file (~65kb)** with no external image/audio dependencies. Inspired by the viral "vibecoding" Reddit demo.

🌐 **Live GitHub Repository**: [github.com/ihearttokyo/neon-vibe-dodger](https://github.com/ihearttokyo/neon-vibe-dodger)

---

## Features

### 1. Visual Splendor (Three.js WebGL)
- **Rotating Double Tunnel**: Two rotating mesh wireframe cylinders rotating in opposite directions, creating a beautiful spatial paradox and an immersive sense of depth.
- **Infinite Particle Starfield**: Over 600 custom neon-scattered points rushing toward the camera to simulate traveling at hyperspace speeds.
- **Futuristic Crystal Vessel**: A multi-faceted glowing octahedron player ship that realistically banks, tilts, and spins as it maneuvers inside the tunnel.
- **Wireframe Obstacles**: Spawning cylinders, prisms, and toruses in 8 radial coordinate tracks.

### 2. Live Audio Synthesizer (Web Audio API)
- Generates a **tempo-synchronized, driving 80s synthwave soundtrack** directly in the browser.
- **Bassline Synth**: A detuned dual-oscillator playing in the key of A minor.
- **Drum Synthesizer**: Procedural kick drums (rapid frequency sweeps) and hi-hats (white noise buffer shaping).
- **Tempo Dynamic Acceleration**: The BPM of the procedural bassline automatically speeds up as your score increases, amplifying gaming tension.
- **Synthesized Retro Sound FX**: Unique sound effects generated in real-time for near-miss bonuses, close dodges, and crashes.

### 3. Visual Safety Harness & Options
- **Strobe/Vibe Mode (Default)**: Full flashing lights sync'd to audio beats, camera shakes, and screen flashes.
- **Safe Mode**: Disables intense strobe flashes, substituting them with smooth, gradual HSL color shifts.
- **Control Modes**: Toggle between WASD/Arrow keys or pointer/mouse tracking inside the tunnel.

---

## The 15 Edge Cases Handled

This clone stands out by addressing 15 critical production edge cases:

1. **Device Pixel Ratio**: Automatically adapts to Retina and High-DPI screens without killing frame rates.
2. **Audio Context Autoplay Policy**: Suspended on load, initialized seamlessly on user start gesture.
3. **Responsive Scaling**: Instantly handles browser window resizes and orientation changes.
4. **Frame-Rate Independence**: All physics, movements, and offsets are computed using delta clock time, guaranteeing uniform speed on 60Hz and 144Hz+ monitors.
5. **Tab Backgrounding**: Listens to browser visibility and suspends game loops and Web Audio scheduled sequences to prevent warping on tab regain.
6. **WebGL Context Loss**: Monitors GPU resets gracefully with an interactive overlay to safely reinitialize.
7. **Procedural Volume Bounds**: Routes all sound outputs through a `DynamicsCompressorNode` to eliminate digital clipping.
8. **Near-Miss Boundaries**: Employs double-gate cylinder boundaries to award near-miss bonuses once per obstacle without double-counting.
9. **Obstacle Spawning Safety**: Employs radial track partition coordinates and guarantees at least a 2-track consecutive gap in obstacle waves so every block is beatable.
10. **Z-Clipping Management**: Controls far/near camera clipping planes perfectly; objects spawn exactly at $Z = -400$ and are garbage-collected as they pass $Z = 20$.
11. **Sticky Key State Clearance**: Listens to window `blur` and `focus` events to force-clear keyboard keydowns if the user Alt-Tabs.
12. **Double-Click & Pinch Zoom Prevention**: Mapped `touch-action: none` and custom handlers to prevent mobile gestures from scaling the web page layout.
13. **Local Storage Try-Catch**: Gracefully handles incognito browser settings by reverting to in-memory scores if `localStorage` throws an exception.
14. **Audio Node Garbage Collection**: Explicitly stops and disconnects all transient oscillators to prevent massive browser audio memory leaks.
15. **Interpolated Color Transitions**: Uses linear interpolation (`lerp`) for gradual, smooth lighting shifts when Safe Mode is enabled.

---

## Running Locally

Since the game is a single-file application, you can run it instantly using any static server.

### Option 1: Python Static Server
Run this inside the directory:
```bash
python3 -m http.server 8000
```
Then navigate to: `http://localhost:8000`

### Option 2: Live HTML
Just double-click the `index.html` file to open it in any modern browser!

---

## Tech Stack
- **Structure**: HTML5
- **Logic**: Vanilla Javascript (ES6)
- **3D Engine**: Three.js (via CDN)
- **Audio Synthesis**: Web Audio API
- **Styling**: Vanilla CSS (Cyberpunk glassmorphic design system)
