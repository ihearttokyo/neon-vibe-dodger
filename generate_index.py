import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>NEON VIBE: CYBER RUNNER</title>
  
  <!-- SEO Tags -->
  <meta name="description" content="An intense, high-fidelity 3D synthwave tunnel dodge game built with Three.js and procedural Web Audio. Fully immersive with weapons, upgrades, and powerups.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap" rel="stylesheet">
  
  <!-- Three.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <!-- Three.js Post-Processing CDN Modules -->
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/LuminosityHighPassShader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"></script>

  <style>
    :root {
      --magenta: #ff007f;
      --cyan: #00f0ff;
      --purple: #9d00ff;
      --yellow: #ffdf00;
      --green: #39ff14;
      --red: #ff3131;
      --bg-dark: #070212;
      --glass-bg: rgba(7, 3, 20, 0.75);
      --glass-border: rgba(0, 240, 255, 0.3);
    }

    * {
      box-sizing: border-box;
      user-select: none;
      margin: 0;
      padding: 0;
    }

    body, html {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: var(--bg-dark);
      font-family: 'Orbitron', sans-serif;
      color: #fff;
    }

    #game-canvas {
      width: 100%;
      height: 100%;
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
    }

    /* Screen Overlays */
    .screen-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 10;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.4s;
      background: radial-gradient(circle at center, rgba(12, 5, 28, 0.5) 0%, rgba(3, 0, 15, 0.95) 100%);
    }

    .screen-overlay.hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }

    .glass-card {
      background: var(--glass-bg);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      border: 2px solid var(--glass-border);
      border-radius: 20px;
      padding: 40px;
      width: 90%;
      max-width: 520px;
      text-align: center;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6), 
                  0 0 35px rgba(255, 0, 127, 0.2), 
                  inset 0 0 15px rgba(0, 240, 255, 0.1);
      transform: translateY(0);
      animation: float-in 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes float-in {
      from {
        opacity: 0;
        transform: translateY(40px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .game-title {
      font-weight: 900;
      font-size: 3.2rem;
      text-transform: uppercase;
      letter-spacing: 5px;
      margin-bottom: 10px;
      background: linear-gradient(135deg, var(--cyan) 0%, var(--magenta) 50%, var(--purple) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 20px rgba(0, 240, 255, 0.35);
      animation: titlePulse 2s infinite alternate ease-in-out;
    }

    @keyframes titlePulse {
      0% { filter: drop-shadow(0 0 5px rgba(0, 240, 255, 0.3)); }
      100% { filter: drop-shadow(0 0 20px rgba(255, 0, 127, 0.6)); }
    }

    .tagline {
      font-size: 0.95rem;
      line-height: 1.6;
      color: rgba(255, 255, 255, 0.7);
      margin-bottom: 30px;
      font-family: 'Share Tech Mono', monospace;
    }

    .control-row {
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin-bottom: 30px;
      text-align: left;
    }

    .form-group {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
    }

    .form-label {
      font-size: 0.85rem;
      font-weight: bold;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--cyan);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .form-desc {
      font-size: 0.75rem;
      color: rgba(255, 255, 255, 0.5);
      margin-top: 3px;
    }

    /* Switch Styling */
    .switch {
      position: relative;
      display: inline-block;
      width: 46px;
      height: 24px;
    }

    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }

    .slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      transition: .3s;
      border-radius: 24px;
    }

    .slider:before {
      position: absolute;
      content: "";
      height: 16px;
      width: 16px;
      left: 3px;
      bottom: 3px;
      background-color: #fff;
      transition: .3s;
      border-radius: 50%;
      box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
    }

    input:checked + .slider {
      background-color: rgba(0, 240, 255, 0.2);
      border-color: var(--cyan);
    }

    input:checked + .slider:before {
      transform: translateX(22px);
      background-color: var(--cyan);
      box-shadow: 0 0 10px var(--cyan);
    }

    .btn-cyber {
      background: linear-gradient(135deg, var(--cyan) 0%, var(--purple) 100%);
      border: none;
      color: #fff;
      padding: 16px 32px;
      font-size: 1.1rem;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 3px;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.4);
      transition: all 0.2s;
      width: 100%;
      position: relative;
      overflow: hidden;
    }

    .btn-cyber:hover {
      transform: scale(1.02);
      box-shadow: 0 0 35px rgba(255, 0, 127, 0.6);
      background: linear-gradient(135deg, var(--magenta) 0%, var(--purple) 100%);
    }

    .btn-cyber:active {
      transform: scale(0.98);
    }

    /* HUD Styling */
    #hud {
      position: absolute;
      top: 20px;
      left: 20px;
      right: 20px;
      display: flex;
      justify-content: space-between;
      z-index: 5;
      pointer-events: none;
      transition: opacity 0.5s;
    }

    #hud.hidden {
      opacity: 0;
    }

    .hud-left, .hud-right, .hud-center {
      display: flex;
      gap: 15px;
      align-items: flex-start;
    }

    .hud-center {
      flex-direction: column;
      align-items: center;
      width: 250px;
    }

    .hud-element {
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      padding: 10px 18px;
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
    }

    .hud-label {
      font-family: 'Share Tech Mono', monospace;
      font-size: 0.7rem;
      color: rgba(255, 255, 255, 0.5);
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 2px;
    }

    .hud-value {
      font-size: 1.4rem;
      font-weight: 900;
      color: #fff;
      letter-spacing: 1px;
      text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
    }

    #multiplier-badge {
      font-size: 0.75rem;
      background: var(--magenta);
      color: #fff;
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: 6px;
      vertical-align: middle;
      text-shadow: none;
      box-shadow: 0 0 8px var(--magenta);
    }

    /* Energy/Progress bars */
    .bar-container {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 5px;
    }

    .bar-bg {
      width: 120px;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
    }

    .bar-fill {
      width: 100%;
      height: 100%;
      transition: width 0.1s ease;
    }

    #boost-bar-fill {
      background: linear-gradient(90deg, var(--cyan), var(--purple));
      box-shadow: 0 0 8px var(--cyan);
    }

    #level-bar-fill {
      background: linear-gradient(90deg, var(--green), var(--cyan));
      box-shadow: 0 0 8px var(--green);
    }

    /* Key Badge */
    .key-badge {
      background: #222;
      border: 1px solid #444;
      border-radius: 4px;
      padding: 1px 5px;
      font-family: 'Share Tech Mono', monospace;
      font-size: 0.8rem;
      color: var(--cyan);
      box-shadow: 0 2px 0 #000;
      margin: 0 3px;
    }

    /* HUD Visual Indicators */
    .vessel-shields {
      display: flex;
      gap: 5px;
      margin-top: 3px;
    }

    .shield-node {
      width: 12px;
      height: 12px;
      border: 1px solid var(--cyan);
      border-radius: 20px;
      box-shadow: 0 0 4px var(--cyan);
      transition: all 0.3s;
    }

    .shield-node.active {
      background: var(--cyan);
      box-shadow: 0 0 10px var(--cyan);
    }

    .shield-node.empty {
      background: rgba(0, 0, 0, 0.5);
      border-color: rgba(255, 255, 255, 0.2);
      box-shadow: none;
    }

    /* Near Miss Indicator */
    #near-miss-indicator {
      position: absolute;
      top: 15%;
      left: 50%;
      transform: translateX(-50%);
      font-size: 1.8rem;
      font-weight: 900;
      color: var(--yellow);
      letter-spacing: 4px;
      text-transform: uppercase;
      opacity: 0;
      pointer-events: none;
      z-index: 4;
      text-shadow: 0 0 15px var(--yellow);
    }

    .near-miss-animate {
      animation: alertSlide 0.6s cubic-bezier(0.19, 1, 0.22, 1) forwards;
    }

    @keyframes alertSlide {
      0% { opacity: 0; transform: translate(-50%, -20px) scale(0.8); }
      30% { opacity: 1; transform: translate(-50%, 0) scale(1.1); }
      70% { opacity: 1; transform: translate(-50%, 0) scale(1); }
      100% { opacity: 0; transform: translate(-50%, 20px) scale(0.9); }
    }

    /* Active Buff Banner */
    #buff-banner {
      position: absolute;
      top: 140px;
      left: 50%;
      transform: translateX(-50%);
      font-family: 'Share Tech Mono', monospace;
      font-size: 1.1rem;
      letter-spacing: 2px;
      color: var(--yellow);
      text-shadow: 0 0 10px var(--yellow);
      font-weight: bold;
      z-index: 5;
      text-transform: uppercase;
      opacity: 0;
      transition: opacity 0.2s;
    }

    /* Screen Glitch overlay */
    #crt-glitch {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 8;
      opacity: 0;
      transition: opacity 0.15s ease;
      background: rgba(255, 0, 0, 0.15);
      border: 3px solid rgba(255, 0, 0, 0.3);
      box-shadow: inset 0 0 80px rgba(255, 0, 0, 0.4);
    }

    .glitching {
      animation: screenNoise 0.15s infinite;
    }

    @keyframes screenNoise {
      0% { transform: translate(2px, 1px) skewX(2deg); filter: hue-rotate(90deg); }
      20% { transform: translate(-1px, -2px) skewX(-1deg); filter: grayscale(0.5); }
      40% { transform: translate(3px, -1px) skewX(0deg); }
      60% { transform: translate(-2px, 3px) skewX(3deg); filter: invert(0.1); }
      80% { transform: translate(1px, -3px) skewX(-2deg); }
      100% { transform: translate(-3px, 2px) skewX(1deg); }
    }

    /* Interactive Keyboard Visual Dashboard overlay */
    #keyboard-dashboard {
      position: absolute;
      bottom: 25px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 5;
      display: flex;
      gap: 15px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      padding: 10px 20px;
      border-radius: 12px;
      pointer-events: none;
      transition: opacity 0.5s;
      font-size: 0.75rem;
      color: rgba(255, 255, 255, 0.6);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }

    #keyboard-dashboard.hidden {
      opacity: 0;
    }

    .key-group {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .keycap {
      background: #151125;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 5px;
      padding: 4px 8px;
      font-weight: bold;
      color: var(--cyan);
      box-shadow: 0 3px 0 #000, 0 5px 10px rgba(0, 0, 0, 0.5);
      transition: all 0.08s ease;
      font-family: 'Share Tech Mono', monospace;
      text-shadow: 0 0 4px var(--cyan);
    }

    .keycap.active {
      transform: translateY(3px);
      box-shadow: 0 0 10px var(--cyan), 0 0 2px var(--cyan);
      background: var(--cyan);
      color: #050212;
      border-color: var(--cyan);
      text-shadow: none;
    }

    /* Upgrade Shop Grid UI */
    .upgrade-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 15px;
      margin-bottom: 25px;
      max-height: 280px;
      overflow-y: auto;
      padding-right: 5px;
    }

    .upgrade-item {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(0, 240, 255, 0.2);
      border-radius: 10px;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s;
    }

    .upgrade-item:hover {
      background: rgba(0, 240, 255, 0.08);
      border-color: var(--cyan);
    }

    .upgrade-details {
      text-align: left;
    }

    .upgrade-name {
      font-weight: bold;
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #fff;
    }

    .upgrade-cost {
      font-family: 'Share Tech Mono', monospace;
      font-size: 0.8rem;
      color: var(--yellow);
      margin-top: 2px;
    }

    .btn-buy {
      background: var(--magenta);
      border: none;
      color: #fff;
      font-family: 'Orbitron', sans-serif;
      font-weight: 900;
      font-size: 0.75rem;
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      box-shadow: 0 0 10px var(--magenta);
      transition: all 0.15s;
    }

    .btn-buy:hover {
      background: #ff00ab;
      transform: scale(1.05);
    }

    .btn-buy:active {
      transform: scale(0.95);
    }

    .btn-buy.disabled {
      background: rgba(255, 255, 255, 0.15);
      color: rgba(255, 255, 255, 0.3);
      box-shadow: none;
      cursor: not-allowed;
      transform: none !important;
    }

    /* Scrollbar */
    .upgrade-grid::-webkit-scrollbar {
      width: 6px;
    }
    .upgrade-grid::-webkit-scrollbar-track {
      background: rgba(0,0,0,0.2);
    }
    .upgrade-grid::-webkit-scrollbar-thumb {
      background: var(--cyan);
      border-radius: 3px;
    }
  </style>
</head>
<body>

  <canvas id="game-canvas"></canvas>
  <div id="crt-glitch"></div>

  <!-- Start Overlay Screen -->
  <div id="start-screen" class="screen-overlay">
    <div class="glass-card">
      <h1 class="game-title">Neon Vibe</h1>
      <p class="tagline">Navigate the hyper-speed rotating neon tunnel and dodge intense space obstacles in a pure synthwave flow state.</p>
      
      <div class="control-row">
        <div class="form-group">
          <div>
            <div class="form-label" style="color: var(--cyan);">Mouse Control Mode</div>
            <div class="form-desc">Steers with cursor (Pointer Lock coordinates)</div>
          </div>
          <label class="switch">
            <input type="checkbox" id="toggle-mouse" checked>
            <span class="slider"></span>
          </label>
        </div>
        <div class="form-group">
          <div>
            <div class="form-label" style="color: var(--magenta);">Procedural Synth Audio</div>
            <div class="form-desc">Synthesized retro beats & 80s bass loops</div>
          </div>
          <label class="switch">
            <input type="checkbox" id="toggle-audio" checked>
            <span class="slider"></span>
          </label>
        </div>
      </div>
      
      <button id="btn-start" class="btn-cyber">Start Engine</button>
    </div>
  </div>

  <!-- Level Upgrade Bay Screen -->
  <div id="upgrade-screen" class="screen-overlay hidden">
    <div class="glass-card" style="border-color: var(--green); max-width: 550px; box-shadow: 0 0 35px rgba(57, 255, 20, 0.2);">
      <h1 class="game-title" style="background: linear-gradient(135deg, var(--green) 0%, var(--cyan) 100%); -webkit-background-clip: text; text-shadow: 0 0 20px rgba(57, 255, 20, 0.35);">Upgrade Bay</h1>
      <p class="tagline" style="margin-bottom: 20px;">Level Clear! Synthesize ship custom configurations using collected Neon Shards.</p>
      
      <div style="display: flex; justify-content: space-between; background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(255,255,255,0.08); padding: 10px 20px; border-radius: 8px; margin-bottom: 20px;">
        <span class="form-label" style="color: var(--yellow);">Collected Shards</span>
        <span class="hud-value" id="upgrade-shards" style="color: var(--yellow);">0</span>
      </div>

      <div class="upgrade-grid">
        <div class="upgrade-item">
          <div class="upgrade-details">
            <div class="upgrade-name">Energy Barrier (Shield)</div>
            <div class="upgrade-cost">Cost: 10 Shards (Max 3 Nodes)</div>
          </div>
          <button id="buy-shield" class="btn-buy">Synthesize</button>
        </div>
        <div class="upgrade-item">
          <div class="upgrade-details">
            <div class="upgrade-name">Laser Ammo Refill (+40 Charges)</div>
            <div class="upgrade-cost">Cost: 5 Shards</div>
          </div>
          <button id="buy-ammo" class="btn-buy">Synthesize</button>
        </div>
        <div class="upgrade-item">
          <div class="upgrade-details">
            <div class="upgrade-name">Thruster Battery Upgrade</div>
            <div class="upgrade-cost">Cost: 15 Shards (Boost recharge rate +30%)</div>
          </div>
          <button id="buy-boost" class="btn-buy">Synthesize</button>
        </div>
        <div class="upgrade-item">
          <div class="upgrade-details">
            <div class="upgrade-name">Weapon Heat Dissipation</div>
            <div class="upgrade-cost">Cost: 15 Shards (Blaster cooldown -35%)</div>
          </div>
          <button id="buy-blaster" class="btn-buy">Synthesize</button>
        </div>
      </div>

      <button id="btn-next-level" class="btn-cyber" style="background: linear-gradient(135deg, var(--green) 0%, var(--cyan) 100%); box-shadow: 0 0 25px rgba(57, 255, 20, 0.4);">Engage Hyperdrive</button>
    </div>
  </div>

  <!-- Game Over Screen -->
  <div id="game-over-screen" class="screen-overlay hidden">
    <div class="glass-card" style="border-color: var(--magenta);">
      <h1 class="game-title" style="background: linear-gradient(135deg, var(--magenta) 0%, var(--purple) 100%); -webkit-background-clip: text;">System Crash</h1>
      <p class="tagline">Your vessel collided with a hyper-space prism. System failure imminent.</p>
      
      <div class="control-row" style="margin-bottom: 25px;">
        <div class="form-group" style="justify-content: space-between;">
          <span class="form-label" style="color: var(--cyan);">Final Score</span>
          <span class="hud-value" id="final-score" style="color: #fff;">00000</span>
        </div>
        <div class="form-group" style="justify-content: space-between;">
          <span class="form-label" style="color: var(--magenta);">Best Attempt</span>
          <span class="hud-value" id="high-score" style="color: var(--magenta);">00000</span>
        </div>
      </div>
      
      <button id="btn-restart" class="btn-cyber" style="background: linear-gradient(135deg, var(--magenta) 0%, var(--purple) 100%); box-shadow: 0 0 20px rgba(255, 0, 127, 0.4);">Reboot System</button>
    </div>
  </div>

  <!-- WebGL Loss Screen -->
  <div id="context-lost-screen" class="screen-overlay hidden">
    <div class="glass-card" style="border-color: var(--magenta);">
      <h1 class="game-title">Graphics Reset</h1>
      <p class="tagline">Your WebGL graphics context was lost due to GPU resource limits.</p>
      <button id="btn-reload" class="btn-cyber">Reinitialize</button>
    </div>
  </div>

  <!-- Floating Active HUD -->
  <div id="hud" class="hidden">
    <div class="hud-left">
      <div class="hud-element" id="score-container">
        <span class="hud-label">Score</span>
        <span class="hud-value" id="score-value">00000</span>
      </div>
      <div class="hud-element" id="shards-container">
        <span class="hud-label">Shards</span>
        <span class="hud-value" id="shards-value" style="color: var(--yellow);">000</span>
      </div>
    </div>
    
    <div class="hud-center">
      <div class="hud-element" style="width: 100%; align-items: center;">
        <span class="hud-label" id="level-title">Level 1</span>
        <div class="bar-container">
          <span class="hud-label" style="margin-bottom: 0;">TIME</span>
          <div class="bar-bg">
            <div id="level-bar-fill" class="bar-fill"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="hud-right">
      <div class="hud-element" id="weapons-container">
        <span class="hud-label">Blaster Ammo</span>
        <span class="hud-value" id="ammo-value" style="color: var(--cyan);">040</span>
      </div>
      <div class="hud-element" id="multiplier-container">
        <span class="hud-label">Speed Level</span>
        <span class="hud-value"><span id="speed-level">1.0x</span><span id="multiplier-badge">x1</span></span>
      </div>
      <div class="hud-element" id="barrier-container">
        <span class="hud-label">Barrier Nodes</span>
        <div class="vessel-shields" id="shield-display">
          <div class="shield-node empty"></div>
          <div class="shield-node empty"></div>
          <div class="shield-node empty"></div>
        </div>
      </div>
      <div class="hud-element" id="boost-container">
        <span class="hud-label">Boost Energy</span>
        <div class="bar-container">
          <div class="bar-bg" style="width: 100px;">
            <div id="boost-bar-fill" class="bar-fill"></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="near-miss-indicator">NEAR MISS</div>
  <div id="buff-banner">INVINCIBLE</div>

  <!-- Interactive Keyboard Visual Dashboard -->
  <div id="keyboard-dashboard" class="hidden">
    <div class="key-group">
      <span class="keycap" id="key-left">A</span>
      <span class="keycap" id="key-right">D</span>
      <span style="font-family:'Share Tech Mono';">Steer</span>
    </div>
    <div style="width:1px; background:rgba(255,255,255,0.15); height:16px;"></div>
    <div class="key-group">
      <span class="keycap" id="key-boost" style="padding:4px 6px;">Shift</span>
      <span style="font-family:'Share Tech Mono';">Boost</span>
    </div>
    <div style="width:1px; background:rgba(255,255,255,0.15); height:16px;"></div>
    <div class="key-group">
      <span class="keycap" id="key-shoot" style="padding:4px 20px;">Space</span>
      <span style="font-family:'Share Tech Mono';">Blaster</span>
    </div>
  </div>

  <!-- Procedural audio synthesis code & Game Core -->
  <script>
    // Game constants
    const TUNNEL_RADIUS = 20;
    const TUNNEL_LENGTH = 800;
    const OBSTACLE_COUNT = 24;
    const LANE_COUNT = 8;
    const LANE_ANGLE_STEP = (Math.PI * 2) / LANE_COUNT;

    // Game variables state mapping (Edge Case 15 synchronized form hooks)
    const STATE = {
      isGameRunning: false,
      isPointerLocked: false,
      mouseEnabled: true,
      
      score: 0,
      highScore: 0,
      neonShardsCount: 0,
      laserAmmo: 40,
      shieldCapacity: 0,
      maxShieldCapacity: 3,
      
      speedLevel: 1.0,
      boostEnergy: 100,
      maxBoostEnergy: 100,
      boostActive: false,
      
      levelTimeLeft: 30.0,
      currentLevel: 1,
      
      // Upgrade tiers
      boostUpgradeTier: 0,
      blasterUpgradeTier: 0,
      
      // Keyboard input states
      playerAngle: 0,
      playerAngleTarget: 0,
      
      obstacles: [],
      projectiles: [],
      particles: [],
      powerups: [],
      
      spawnTimer: 0,
      spawnInterval: 45, // frames between spawn checks
      
      // Active Powerup Buff States
      isInvincible: false,
      invincibilityTime: 0,
      isMagnetActive: false,
      magnetTime: 0,
      isTimeWarpActive: false,
      timeWarpTime: 0,
      isScoreSurgeActive: false,
      scoreSurgeTime: 0,
      isControlsInverted: false,
      controlsInvertedTime: 0,
      
      // Gun cooldown
      lastShotTime: 0,
      shotCooldown: 300, // milliseconds
      
      obstaclesPassedCount: 0
    };

    // Keyboard Maps
    const keyMap = {
      left: false,
      right: false,
      boost: false,
      shoot: false
    };

    // Three.js instances
    let scene, camera, renderer, composer, clock;
    let tunnelGroup, playerGroup, starField;
    const STAR_COUNT = 650;
    let ambientLight, pointLight;
    let exhaustParticles = [];
    let animationFrameId;

    // Procedural sound generators variables (Web Audio API)
    let audioCtx = null;
    let sequencerTimer = null;
    let synthBPM = 115;
    let currentBeat = 0;
    let synthNodes = [];

    // Pointer Lock setup
    const canvas = document.getElementById('game-canvas');
    canvas.addEventListener('click', () => {
      if (STATE.isGameRunning && STATE.mouseEnabled) {
        canvas.requestPointerLock();
      }
    });

    document.addEventListener('pointerlockchange', () => {
      if (document.pointerLockElement === canvas) {
        STATE.isPointerLocked = true;
      } else {
        STATE.isPointerLocked = false;
      }
    });

    // Check localStorage fallback (Edge Case 13 privacy access sandbox checks)
    try {
      const stored = localStorage.getItem('neon_vibe_dodger_highscore');
      if (stored) STATE.highScore = parseInt(stored, 10);
    } catch (e) {
      console.warn("Storage API disabled. Highscore tracking will default to in-memory.");
    }

    // ----------------------------------------------------
    // PROCEDURAL REALTIME SYNTHWAVE AUDIO ENGINE
    // ----------------------------------------------------
    function initAudio() {
      if (audioCtx) return;
      
      // Initialize dynamic AudioContext (Edge Case 2 Gesture Autoplay Restrictions)
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioContextClass();
      
      // High-performance limiting compressor node to avoid digital clipping (Edge Case 7)
      const compressor = audioCtx.createDynamicsCompressor();
      compressor.threshold.setValueAtTime(-14, audioCtx.currentTime);
      compressor.knee.setValueAtTime(40, audioCtx.currentTime);
      compressor.ratio.setValueAtTime(12, audioCtx.currentTime);
      compressor.attack.setValueAtTime(0.003, audioCtx.currentTime);
      compressor.release.setValueAtTime(0.08, audioCtx.currentTime);
      compressor.connect(audioCtx.destination);
      
      // Master Volume node
      const masterVolume = audioCtx.createGain();
      masterVolume.gain.setValueAtTime(0.18, audioCtx.currentTime);
      masterVolume.connect(compressor);
      
      STATE.masterGainNode = masterVolume;
    }

    function toggleMasterAudio(enabled) {
      if (!STATE.masterGainNode) return;
      STATE.masterGainNode.gain.linearRampToValueAtTime(
        enabled ? 0.18 : 0, 
        audioCtx.currentTime + 0.1
      );
    }

    // Dynamic Sound Effects (Procedural real-time frequency curves)
    function playSoundFX(type) {
      if (!audioCtx || audioCtx.state === 'suspended') return;

      const now = audioCtx.currentTime;
      
      if (type === 'shoot') {
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(580, now);
        osc.frequency.exponentialRampToValueAtTime(80, now + 0.15);
        
        gainNode.gain.setValueAtTime(0.1, now);
        gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
        
        osc.connect(gainNode);
        gainNode.connect(STATE.masterGainNode);
        
        osc.start(now);
        osc.stop(now + 0.16);
      } 
      else if (type === 'hit') {
        const osc = audioCtx.createOscillator();
        const noise = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(180, now);
        osc.frequency.linearRampToValueAtTime(30, now + 0.4);
        
        gainNode.gain.setValueAtTime(0.3, now);
        gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
        
        osc.connect(gainNode);
        gainNode.connect(STATE.masterGainNode);
        
        osc.start(now);
        osc.stop(now + 0.4);
      }
      else if (type === 'nearmiss') {
        // High-pitched synth whistle
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(900, now);
        osc.frequency.exponentialRampToValueAtTime(1800, now + 0.2);
        
        gainNode.gain.setValueAtTime(0, now);
        gainNode.gain.linearRampToValueAtTime(0.1, now + 0.05);
        gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
        
        osc.connect(gainNode);
        gainNode.connect(STATE.masterGainNode);
        
        osc.start(now);
        osc.stop(now + 0.25);
      } 
      else if (type === 'shards') {
        // Sparkling bell sound
        const osc = audioCtx.createOscillator();
        const osc2 = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(1200, now);
        osc.frequency.setValueAtTime(1500, now + 0.05);
        
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(2400, now);
        
        gainNode.gain.setValueAtTime(0.12, now);
        gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
        
        osc.connect(gainNode);
        osc2.connect(gainNode);
        gainNode.connect(STATE.masterGainNode);
        
        osc.start(now);
        osc2.start(now);
        osc.stop(now + 0.3);
        osc2.stop(now + 0.3);
      }
      else if (type === 'shield_up') {
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.3);
        gainNode.gain.setValueAtTime(0.15, now);
        gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
        osc.connect(gainNode);
        gainNode.connect(STATE.masterGainNode);
        osc.start(now);
        osc.stop(now + 0.3);
      }
      else if (type === 'glitch') {
        // Static noise burst
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(60, now);
        osc.frequency.linearRampToValueAtTime(220, now + 0.2);
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.setValueAtTime(0.05, now + 0.1);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
        osc.connect(gain);
        gain.connect(STATE.masterGainNode);
        osc.start(now);
        osc.stop(now + 0.25);
      }
      else if (type === 'emp') {
        // Exploding synth pop
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(200, now);
        osc.frequency.exponentialRampToValueAtTime(20, now + 0.4);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
        osc.connect(gain);
        gain.connect(STATE.masterGainNode);
        osc.start(now);
        osc.stop(now + 0.4);
      }
      else if (type === 'crash') {
        // Low thunder crash
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(80, now);
        osc.frequency.exponentialRampToValueAtTime(10, now + 0.8);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
        osc.connect(gain);
        gain.connect(STATE.masterGainNode);
        osc.start(now);
        osc.stop(now + 0.8);
      }
    }

    // Synthesized loop sequencer (Fat detuned 80s bassline + kick drum synthesizer)
    function startSynthSequencer() {
      if (!audioCtx) return;
      
      const secondsPerBeat = 60.0 / synthBPM;
      const eighthNoteTime = secondsPerBeat / 2.0;

      const scheduleNextBeat = (beat, time) => {
        if (!STATE.isGameRunning) return;
        
        // Dynamic speed beats acceleration matching score multipliers
        const speedFactor = 1.0 + (STATE.speedLevel - 1.0) * 0.25;
        const actualInterval = eighthNoteTime / speedFactor;
        
        // 1. Kick Drum Synthesizer (Standard beats)
        if (beat % 2 === 0) {
          const kickOsc = audioCtx.createOscillator();
          const kickGain = audioCtx.createGain();
          
          kickOsc.type = 'sine';
          kickOsc.frequency.setValueAtTime(150, time);
          kickOsc.frequency.exponentialRampToValueAtTime(45, time + 0.12);
          
          kickGain.gain.setValueAtTime(0.35, time);
          kickGain.gain.exponentialRampToValueAtTime(0.001, time + 0.15);
          
          kickOsc.connect(kickGain);
          kickGain.connect(STATE.masterGainNode);
          
          kickOsc.start(time);
          kickOsc.stop(time + 0.16);

          // Audio reactive vector pulsing logic synced to the kick drum
          if (ambientLight) {
            ambientLight.color.setHex(beat % 4 === 0 ? 0xff007f : 0x00f0ff);
          }
          if (pointLight) {
            pointLight.intensity = 18.0;
          }
        }

        // 2. Synthesized detuned synth bass pattern (Fat 80s Arpeggio in A minor)
        const notes = [55, 55, 65, 55, 58, 58, 65, 58]; // MIDI-style frequencies index
        const midiNote = notes[beat % notes.length];
        const freq = Math.pow(2, (midiNote - 69) / 12) * 440;

        const bassOsc = audioCtx.createOscillator();
        const bassOsc2 = audioCtx.createOscillator();
        const bassFilter = audioCtx.createBiquadFilter();
        const bassGain = audioCtx.createGain();

        bassOsc.type = 'sawtooth';
        bassOsc.frequency.setValueAtTime(freq, time);
        
        bassOsc2.type = 'sawtooth';
        bassOsc2.frequency.setValueAtTime(freq * 1.015, time); // detune
        
        bassFilter.type = 'lowpass';
        bassFilter.Q.setValueAtTime(6, time);
        bassFilter.frequency.setValueAtTime(180, time);
        bassFilter.frequency.exponentialRampToValueAtTime(680, time + actualInterval * 0.7);

        bassGain.gain.setValueAtTime(0.12, time);
        bassGain.gain.exponentialRampToValueAtTime(0.001, time + actualInterval * 0.95);

        bassOsc.connect(bassFilter);
        bassOsc2.connect(bassFilter);
        bassFilter.connect(bassGain);
        bassGain.connect(STATE.masterGainNode);

        bassOsc.start(time);
        bassOsc2.start(time);
        bassOsc.stop(time + actualInterval);
        bassOsc2.stop(time + actualInterval);

        // Keep tracks of active oscillators to disconnect them gracefully on backgrounding (Edge Case 14)
        synthNodes.push(bassOsc, bassOsc2);
        if (synthNodes.length > 30) {
          synthNodes.splice(0, 10);
        }

        // Schedule next eighth note in loop arpeggiation
        const nextBeat = (beat + 1) % 16;
        const nextTime = time + actualInterval;
        
        sequencerTimer = setTimeout(() => {
          scheduleNextBeat(nextBeat, nextTime);
        }, actualInterval * 1000);
      };

      scheduleNextBeat(currentBeat, audioCtx.currentTime + 0.05);
    }

    function pauseGame() {
      if (audioCtx) {
        audioCtx.suspend();
      }
    }

    function resumeGame() {
      if (audioCtx) {
        audioCtx.resume();
      }
    }

    // ----------------------------------------------------
    // GRAPHIC SYSTEM LAYERS (Three.js WebGL + UnrealBloom)
    // ----------------------------------------------------
    function initThree() {
      const w = window.innerWidth;
      const h = window.innerHeight;

      // 1. Setup Scene, Camera, & WebGL Renderer (High-DPI retina capped ratio, Edge Case 1)
      scene = new THREE.Scene();
      scene.background = new THREE.Color(0x070212);
      scene.fog = new THREE.FogExp2(0x070212, 0.0028);

      camera = new THREE.PerspectiveCamera(65, w / h, 0.1, TUNNEL_LENGTH + 100);
      camera.position.set(0, 0, 0);

      renderer = new THREE.WebGLRenderer({
        canvas: canvas,
        antialias: true,
        alpha: false,
        powerPreference: "high-performance"
      });
      renderer.setSize(w, h);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2.0));
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.0;

      // 2. High-fidelity dynamic Post-Processing Composer (UnrealBloom)
      const renderPass = new THREE.RenderPass(scene, camera);
      const bloomPass = new THREE.UnrealBloomPass(
        new THREE.Vector2(w, h), 
        1.8,  // strength
        0.5,  // radius
        0.18  // threshold
      );

      composer = new THREE.EffectComposer(renderer);
      composer.addPass(renderPass);
      composer.addPass(bloomPass);

      // 3. Build Double Rotating Wireframe Tunnel (Vector aesthetic, reverse rot)
      tunnelGroup = new THREE.Group();
      scene.add(tunnelGroup);

      // Inner cylinder wireframe (magenta vectors)
      const innerGeom = new THREE.CylinderGeometry(
        TUNNEL_RADIUS, TUNNEL_RADIUS, TUNNEL_LENGTH, 
        12, 100, true
      );
      innerGeom.rotateX(Math.PI / 2);
      innerGeom.translate(0, 0, -TUNNEL_LENGTH / 2);

      const innerMat = new THREE.MeshBasicMaterial({
        color: 0xff007f,
        wireframe: true,
        transparent: true,
        opacity: 0.18,
        blending: THREE.AdditiveBlending
      });
      const innerTunnel = new THREE.Mesh(innerGeom, innerMat);
      tunnelGroup.add(innerTunnel);

      // Outer cylinder wireframe (violet vectors, rotating opposite)
      const outerGeom = new THREE.CylinderGeometry(
        TUNNEL_RADIUS + 0.5, TUNNEL_RADIUS + 0.5, TUNNEL_LENGTH, 
        8, 40, true
      );
      outerGeom.rotateX(Math.PI / 2);
      outerGeom.translate(0, 0, -TUNNEL_LENGTH / 2);

      const outerMat = new THREE.MeshBasicMaterial({
        color: 0x9d00ff,
        wireframe: true,
        transparent: true,
        opacity: 0.08,
        blending: THREE.AdditiveBlending
      });
      const outerTunnel = new THREE.Mesh(outerGeom, outerMat);
      tunnelGroup.add(outerTunnel);

      // Save references for animations
      STATE.innerMesh = innerTunnel;
      STATE.outerMesh = outerTunnel;

      // 4. Build Scrolling Structural Rib Ring Barriers down the tunnel
      STATE.ribs = [];
      const ribCount = 35;
      const ribDistance = TUNNEL_LENGTH / ribCount;

      for (let i = 0; i < ribCount; i++) {
        const ringGeom = new THREE.RingGeometry(TUNNEL_RADIUS - 0.2, TUNNEL_RADIUS + 0.2, 32);
        const ringMat = new THREE.MeshBasicMaterial({
          color: 0x00f0ff,
          transparent: true,
          opacity: 0.25,
          side: THREE.DoubleSide,
          blending: THREE.AdditiveBlending
        });
        const ringMesh = new THREE.Mesh(ringGeom, ringMat);
        ringMesh.position.set(0, 0, -(i * ribDistance));
        tunnelGroup.add(ringMesh);
        STATE.ribs.push(ringMesh);
      }

      // 5. Starfield Warp Speed Particle Points
      const starGeom = new THREE.BufferGeometry();
      const starCount = STAR_COUNT;
      const starPositions = new Float32Array(starCount * 3);

      for (let i = 0; i < STAR_COUNT; i++) {
        // Distribute coordinates uniformly inside a cylinder volume
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * (TUNNEL_RADIUS - 1.5);
        starPositions[i * 3] = Math.cos(angle) * radius;
        starPositions[i * 3 + 1] = Math.sin(angle) * radius;
        starPositions[i * 3 + 2] = -Math.random() * TUNNEL_LENGTH;
      }

      starGeom.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
      const starMat = new THREE.PointsMaterial({
        color: 0xffffff,
        size: 0.5,
        sizeAttenuation: true,
        transparent: true,
        opacity: 0.8,
        blending: THREE.AdditiveBlending
      });
      starField = new THREE.Points(starGeom, starMat);
      scene.add(starField);

      // 6. Build Glowing Striped Synthwave Sun (ShaderMaterial with DoubleSide)
      const sunGeom = new THREE.PlaneGeometry(160, 160);
      const sunMat = new THREE.ShaderMaterial({
        transparent: true,
        side: THREE.DoubleSide,
        uniforms: {
          colorTop: { value: new THREE.Color(0xff007f) },
          colorBottom: { value: new THREE.Color(0xffdf00) },
          stripes: { value: 9.0 },
          stripeRatio: { value: 0.55 },
          glow: { value: 0.35 }
        },
        vertexShader: `
          varying vec2 vUv;
          void main() {
            vUv = uv;
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          varying vec2 vUv;
          uniform vec3 colorTop;
          uniform vec3 colorBottom;
          uniform float stripes;
          uniform float stripeRatio;
          uniform float glow;
          void main() {
            // Radial mask
            float dist = distance(vUv, vec2(0.5, 0.5));
            if (dist > 0.5) {
              discard;
            }
            
            // Vertical gradient
            vec3 finalColor = mix(colorBottom, colorTop, vUv.y);
            
            // Horizontal striped culling slits
            float stripeVal = sin(vUv.y * 3.14159 * stripes);
            if (vUv.y < 0.6 && stripeVal < (stripeRatio * (1.0 - vUv.y * 1.2))) {
              discard;
            }
            
            // Subtle glow around circle edges
            float alpha = 1.0 - smoothstep(0.48, 0.5, dist);
            gl_FragColor = vec4(finalColor, alpha * (1.0 + glow));
          }
        `,
        blending: THREE.AdditiveBlending
      });
      
      const sunMesh = new THREE.Mesh(sunGeom, sunMat);
      sunMesh.position.set(0, 25, -TUNNEL_LENGTH + 20);
      scene.add(sunMesh);

      // 7. Futuristic Player Crystal Vessel (Neon diamond prism)
      playerGroup = new THREE.Group();
      scene.add(playerGroup);

      // Diamond core mesh
      const coreGeom = new THREE.OctahedronGeometry(1.2, 0);
      const coreMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        wireframe: true
      });
      const coreMesh = new THREE.Mesh(coreGeom, coreMat);
      playerGroup.add(coreMesh);

      // Outer bounding glowing structural lines
      const outlineGeom = new THREE.OctahedronGeometry(1.4, 0);
      const outlineMat = new THREE.MeshBasicMaterial({
        color: 0xff007f,
        transparent: true,
        opacity: 0.4,
        blending: THREE.AdditiveBlending
      });
      const outlineMesh = new THREE.Mesh(outlineGeom, outlineMat);
      playerGroup.add(outlineMesh);
      
      // Keep reference for rotating crystal vessel core
      STATE.playerCoreMesh = coreMesh;
      STATE.playerOutlineMesh = outlineMesh;

      // Position ship on the floor base of the tunnel
      playerGroup.position.set(0, -TUNNEL_RADIUS + 0.6, -10);

      // Shield Bubble Mesh
      const shieldGeom = new THREE.SphereGeometry(2.0, 16, 16);
      const shieldMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        wireframe: true,
        transparent: true,
        opacity: 0,
        blending: THREE.AdditiveBlending
      });
      const shieldMesh = new THREE.Mesh(shieldGeom, shieldMat);
      playerGroup.add(shieldMesh);
      STATE.playerShieldMesh = shieldMesh;

      // 8. Lights
      ambientLight = new THREE.AmbientLight(0xff007f, 0.4);
      scene.add(ambientLight);

      pointLight = new THREE.PointLight(0x00f0ff, 12, 120);
      pointLight.position.set(0, 0, -20);
      scene.add(pointLight);

      // Clock
      clock = new THREE.Clock();

      // Handle window responsive scaling layout (Edge Case 3)
      window.addEventListener('resize', onWindowResize);
      
      // Handle WebGL context losses reboot (Edge Case 6)
      canvas.addEventListener('webglcontextlost', (e) => {
        e.preventDefault();
        STATE.isGameRunning = false;
        if (animationFrameId) cancelAnimationFrame(animationFrameId);
        document.getElementById('hud').classList.add('hidden');
        document.getElementById('keyboard-dashboard').classList.add('hidden');
        document.getElementById('context-lost-screen').classList.remove('hidden');
      });
    }

    function onWindowResize() {
      const w = window.innerWidth;
      const h = window.innerHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
      composer.setSize(w, h);
    }

    // ----------------------------------------------------
    // PROJECTILES, POWERUPS, HAZARDS & DYNAMIC SPINS
    // ----------------------------------------------------
    function spawnObstacle() {
      if (!STATE.isGameRunning) return;

      // 1. Spawning partitioned path selection logic (Edge Case 9 Circular lanes)
      const playerLane = Math.floor((STATE.playerAngle + Math.PI) / LANE_ANGLE_STEP) % LANE_COUNT;
      const safeLane1 = (playerLane + 3) % LANE_COUNT;
      const safeLane2 = (playerLane + 4) % LANE_COUNT;
      const safeLane3 = (playerLane + 5) % LANE_COUNT;

      // Decide spawn count (Increases as Levels advance)
      const count = Math.min(6, 1 + Math.floor(STATE.currentLevel / 2));
      const chosenLanes = new Set();

      for (let k = 0; k < count; k++) {
        let attempts = 0;
        let lane = Math.floor(Math.random() * LANE_COUNT);
        
        // Guarantee player has a valid navigation bypass lane
        while (
          (lane === safeLane1 || lane === safeLane2 || lane === safeLane3 || chosenLanes.has(lane)) 
          && attempts < 10
        ) {
          lane = Math.floor(Math.random() * LANE_COUNT);
          attempts++;
        }
        
        chosenLanes.add(lane);

        // Build obstacle geometries (Varied retro prisms, boxes, toruses)
        const geoms = [
          new THREE.ConeGeometry(2.0, 4.5, 4),
          new THREE.BoxGeometry(2.4, 2.4, 2.4),
          new THREE.TorusGeometry(1.6, 0.5, 8, 16)
        ];
        
        // Pick geom
        const geom = geoms[Math.floor(Math.random() * geoms.length)];
        
        // Dynamic color signatures based on lane index
        const colors = [0xff007f, 0x00f0ff, 0x9d00ff, 0xff0055];
        const color = colors[lane % colors.length];

        const mat = new THREE.MeshBasicMaterial({
          color: color,
          wireframe: true,
          transparent: true,
          opacity: 0.8
        });

        // Group together structural outline
        const mesh = new THREE.Mesh(geom, mat);

        // Position on far boundary
        const angle = lane * LANE_ANGLE_STEP;
        const radius = TUNNEL_RADIUS - 1.2;
        mesh.position.set(
          Math.cos(angle) * radius,
          Math.sin(angle) * radius,
          -TUNNEL_LENGTH
        );

        // Spin obstacle orientation slightly
        mesh.rotation.set(Math.random(), Math.random(), Math.random());

        // Spawn speeds scale up with current level
        const baseSpeed = 4.8 + (STATE.currentLevel * 0.7);
        const speed = baseSpeed + Math.random() * 1.5;

        scene.add(mesh);
        STATE.obstacles.push({
          mesh: mesh,
          lane: lane,
          speed: speed,
          nearMissTriggered: false,
          health: 1 // Blaster takes 1 hit to destroy standard obstacles
        });
      }
    }

    function spawnCollectible() {
      if (!STATE.isGameRunning) return;

      // Lane selection
      const lane = Math.floor(Math.random() * LANE_COUNT);
      const angle = lane * LANE_ANGLE_STEP;
      const radius = TUNNEL_RADIUS - 1.2;

      // Pick random collectable or hazard (15 dynamic options)
      const types = [
        'shard', 'shard', 'shard', 'shard', // high probability
        'shield', 'boost_battery', 'blaster_ammo',
        'invincibility', 'magnet', 'time_warp', 'emp', 'surge',
        'hazard_glitch', 'hazard_invert', 'hazard_drain'
      ];
      const type = types[Math.floor(Math.random() * types.length)];

      let geom, mat, color;

      if (type === 'shard') {
        geom = new THREE.OctahedronGeometry(0.8, 0); // double-pyramid
        color = 0xffdf00; // yellow
      } else if (type === 'shield') {
        geom = new THREE.SphereGeometry(0.9, 8, 8);
        color = 0x00f0ff; // cyan
      } else if (type === 'boost_battery') {
        geom = new THREE.CylinderGeometry(0.5, 0.5, 1.4, 6);
        color = 0x9d00ff; // purple
      } else if (type === 'blaster_ammo') {
        geom = new THREE.BoxGeometry(0.7, 1.4, 0.7);
        color = 0x39ff14; // green
      } else if (type === 'invincibility') {
        geom = new THREE.IcosahedronGeometry(0.9, 0);
        color = 0xffffff; // white
      } else if (type === 'magnet') {
        geom = new THREE.TorusGeometry(0.7, 0.25, 4, 8);
        color = 0xff3131; // red
      } else if (type === 'time_warp') {
        geom = new THREE.DodecahedronGeometry(0.8, 0);
        color = 0x00ffff; // cyan clock
      } else if (type === 'emp') {
        geom = new THREE.RingGeometry(0.3, 0.9, 8);
        color = 0xff00ff; // magenta pulse
      } else if (type === 'surge') {
        geom = new THREE.ConeGeometry(0.7, 1.5, 4);
        color = 0xff00ab; // hot pink
      } else {
        // Hazards
        geom = new THREE.BoxGeometry(1.2, 1.2, 1.2);
        color = 0xff3131; // bright hazard red
      }

      mat = new THREE.MeshBasicMaterial({
        color: color,
        wireframe: true,
        transparent: true,
        opacity: 0.95
      });

      const mesh = new THREE.Mesh(geom, mat);
      mesh.position.set(
        Math.cos(angle) * radius,
        Math.sin(angle) * radius,
        -TUNNEL_LENGTH
      );
      mesh.rotation.set(Math.random(), Math.random(), Math.random());

      scene.add(mesh);
      STATE.powerups.push({
        mesh: mesh,
        lane: lane,
        type: type,
        speed: 5.5 + STATE.currentLevel * 0.5
      });
    }

    // Fire laser blaster projectile down the lane
    function fireBlaster() {
      if (!STATE.isGameRunning || STATE.laserAmmo <= 0) return;

      const now = Date.now();
      const actualCooldown = STATE.shotCooldown * (1.0 - STATE.blasterUpgradeTier * 0.175);
      if (now - STATE.lastShotTime < actualCooldown) return; // rate limit

      STATE.lastShotTime = now;
      STATE.laserAmmo--;
      document.getElementById('ammo-value').innerText = String(STATE.laserAmmo).padStart(3, '0');

      playSoundFX('shoot');

      // Create cylindrical projectile mesh
      const geom = new THREE.CylinderGeometry(0.12, 0.12, 2.5, 4);
      geom.rotateX(Math.PI / 2); // align forward
      const mat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        transparent: true,
        opacity: 0.9,
        blending: THREE.AdditiveBlending
      });
      const boltMesh = new THREE.Mesh(geom, mat);

      // Start bullet at player coordinates
      boltMesh.position.copy(playerGroup.position);
      boltMesh.position.z = -12; // slightly ahead of ship
      
      // Direct bolt angle along the ship orientation lane
      boltMesh.rotation.copy(playerGroup.rotation);

      scene.add(boltMesh);
      
      // Determine the angle lane of the bullet to lock onto target vectors
      STATE.projectiles.push({
        mesh: boltMesh,
        angle: STATE.playerAngle,
        speed: 15.0 // extremely rapid forward velocity
      });

      // Muzzle flash point light intensity push
      if (pointLight) {
        pointLight.intensity = 20.0;
        pointLight.color.setHex(0x00f0ff);
      }
    }

    // ----------------------------------------------------
    // DYNAMIC GAME LOOPS & RENDERING MECHANICS
    // ----------------------------------------------------
    function animate() {
      if (!STATE.isGameRunning) return;

      animationFrameId = requestAnimationFrame(animate);

      const delta = clock.getDelta();
      
      // Frame rate independence multipliers (Edge Case 4 delta frames)
      const frameDelta = delta * 60.0; 

      // 1. Dynamic steer navigation processing (Mouse movementX vs keyboard bindings)
      let steerAngle = 0;
      if (keyMap.left) steerAngle = -0.045 * frameDelta;
      if (keyMap.right) steerAngle = 0.045 * frameDelta;

      // Handle reversed controls hazard state
      if (STATE.isControlsInverted) {
        steerAngle = -steerAngle;
      }

      // Add key-pressing active glow visual states in HUD dashboard overlay
      const leftKey = document.getElementById('key-left');
      const rightKey = document.getElementById('key-right');
      if (keyMap.left) {
        leftKey.classList.add('active');
      } else {
        leftKey.classList.remove('active');
      }
      if (keyMap.right) {
        rightKey.classList.add('active');
      } else {
        rightKey.classList.remove('active');
      }

      // Merge steer angles into player rotation targets
      STATE.playerAngleTarget += steerAngle;

      // Smooth interpolation filter of banking angles
      STATE.playerAngle += (STATE.playerAngleTarget - STATE.playerAngle) * 0.15 * frameDelta;
      
      // Lock target limits
      STATE.playerAngle = THREE.MathUtils.clamp(STATE.playerAngle, -Math.PI * 0.95, Math.PI * 0.95);

      // Rotate player ship group relative to tunnel lane angle
      playerGroup.position.x = Math.sin(STATE.playerAngle) * (TUNNEL_RADIUS - 0.7);
      playerGroup.position.y = -Math.cos(STATE.playerAngle) * (TUNNEL_RADIUS - 0.7);
      
      // Auto-align banking tilt angle matching steer velocity
      const shipBankAngle = (STATE.playerAngle - STATE.playerAngleTarget) * 0.45;
      playerGroup.rotation.set(0, 0, STATE.playerAngle - shipBankAngle);

      // Rotate player core crystals visually
      if (STATE.playerCoreMesh) STATE.playerCoreMesh.rotation.y += 0.02 * frameDelta;
      if (STATE.playerOutlineMesh) STATE.playerOutlineMesh.rotation.z -= 0.01 * frameDelta;

      // 2. Recharging thruster Shift Boost mechanism
      const boostFill = document.getElementById('boost-bar-fill');
      if (keyMap.boost && STATE.boostEnergy > 5.0) {
        STATE.boostActive = true;
        STATE.boostEnergy = Math.max(0, STATE.boostEnergy - 0.7 * frameDelta);
        document.getElementById('key-boost').classList.add('active');
      } else {
        STATE.boostActive = false;
        const actualRecharge = 0.22 * (1.0 + STATE.boostUpgradeTier * 0.3) * frameDelta;
        STATE.boostEnergy = Math.min(STATE.maxBoostEnergy, STATE.boostEnergy + actualRecharge);
        document.getElementById('key-boost').classList.remove('active');
      }
      boostFill.style.width = `${STATE.boostEnergy}%`;

      // Active score speed multiplier scales
      let currentVelocity = 1.0;
      if (STATE.boostActive) {
        currentVelocity = 1.85; // extreme warp push
      }
      
      // Slow obstacle rate if Time Warp is active
      let obstacleSlowFactor = 1.0;
      if (STATE.isTimeWarpActive) {
        obstacleSlowFactor = 0.45;
      }

      // Smooth blend ambient multiplier counters
      STATE.speedLevel += (currentVelocity - STATE.speedLevel) * 0.1 * frameDelta;
      document.getElementById('speed-level').innerText = `${STATE.speedLevel.toFixed(1)}x`;
      document.getElementById('multiplier-badge').innerText = `x${STATE.isScoreSurgeActive ? 5 : 1}`;

      // Increment scores based on speed levels
      STATE.score += Math.floor(STATE.speedLevel * (STATE.isScoreSurgeActive ? 5.0 : 1.0) * frameDelta * 2.0);
      document.getElementById('score-value').innerText = String(STATE.score).padStart(5, '0');

      // 3. Projectiles travel physics loop
      const spaceKey = document.getElementById('key-shoot');
      if (keyMap.shoot) {
        spaceKey.classList.add('active');
      } else {
        spaceKey.classList.remove('active');
      }

      for (let i = STATE.projectiles.length - 1; i >= 0; i--) {
        const proj = STATE.projectiles[i];
        proj.mesh.position.z -= proj.speed * frameDelta;
        
        // Remove distant blasters
        if (proj.mesh.position.z < -TUNNEL_LENGTH) {
          scene.remove(proj.mesh);
          proj.mesh.geometry.dispose();
          proj.mesh.material.dispose();
          STATE.projectiles.splice(i, 1);
        }
      }

      // 4. Starfield speeds & Exhaust tail particles (Frame rate scaling exhaust, Edge Case 1)
      if (starField) {
        const positions = starField.geometry.attributes.position.array;
        const speed = 4.2 * STATE.speedLevel * frameDelta;
        
        for (let i = 0; i < STAR_COUNT; i++) {
          positions[i * 3 + 2] += speed;
          // Loop star coordinates back to far clipping planes (Edge Case 10 Z-clip)
          if (positions[i * 3 + 2] > 0) {
            positions[i * 3 + 2] = -TUNNEL_LENGTH;
          }
        }
        starField.geometry.attributes.position.needsUpdate = true;
      }

      // Update structural ribs scrolling down Z axis
      STATE.ribs.forEach(rib => {
        rib.position.z += 3.5 * STATE.speedLevel * frameDelta;
        if (rib.position.z > 0) {
          rib.position.z = -TUNNEL_LENGTH;
        }
      });

      // Render player exhaust glowing particles
      if (Math.random() < 0.65) {
        createExhaustParticle();
      }
      updateExhaustParticles(frameDelta);

      // 5. Active Buff States timer reductions
      if (STATE.isInvincible) {
        STATE.invincibilityTime -= delta;
        if (STATE.invincibilityTime <= 0) {
          STATE.isInvincible = false;
          document.getElementById('buff-banner').style.opacity = 0;
          STATE.playerOutlineMesh.material.color.setHex(0xff007f);
        } else {
          // White star glow outline
          STATE.playerOutlineMesh.material.color.setHex(0xffffff);
        }
      }
      if (STATE.isMagnetActive) {
        STATE.magnetTime -= delta;
        if (STATE.magnetTime <= 0) {
          STATE.isMagnetActive = false;
        }
      }
      if (STATE.isTimeWarpActive) {
        STATE.timeWarpTime -= delta;
        if (STATE.timeWarpTime <= 0) {
          STATE.isTimeWarpActive = false;
        }
      }
      if (STATE.isScoreSurgeActive) {
        STATE.scoreSurgeTime -= delta;
        if (STATE.scoreSurgeTime <= 0) {
          STATE.isScoreSurgeActive = false;
        }
      }
      if (STATE.isControlsInverted) {
        STATE.controlsInvertedTime -= delta;
        if (STATE.controlsInvertedTime <= 0) {
          STATE.isControlsInverted = false;
        }
      }

      // 6. Level Timer countdown loop
      STATE.levelTimeLeft = Math.max(0, STATE.levelTimeLeft - delta);
      const levelBar = document.getElementById('level-bar-fill');
      const progressPercent = (STATE.levelTimeLeft / 30.0) * 100.0;
      levelBar.style.width = `${progressPercent}%`;

      if (STATE.levelTimeLeft <= 0) {
        triggerLevelClear();
      }

      // 7. Spawn frequency checks
      STATE.spawnTimer += 1.0 * frameDelta;
      if (STATE.spawnTimer >= STATE.spawnInterval) {
        STATE.spawnTimer = 0;
        if (Math.random() < 0.85) spawnObstacle();
        if (Math.random() < 0.45) spawnCollectible();
      }

      // 8. Obstacles physics progression & collision matrices
      for (let i = STATE.obstacles.length - 1; i >= 0; i--) {
        const obs = STATE.obstacles[i];
        
        // Move along Z axis
        obs.mesh.position.z += obs.speed * STATE.speedLevel * obstacleSlowFactor * frameDelta;
        
        // Dynamic spin
        obs.mesh.rotation.x += 0.015 * frameDelta;
        obs.mesh.rotation.y += 0.01 * frameDelta;

        // Collision Check: Projectile vs Obstacle
        for (let j = STATE.projectiles.length - 1; j >= 0; j--) {
          const proj = STATE.projectiles[j];
          const distZ = Math.abs(obs.mesh.position.z - proj.mesh.position.z);
          
          if (distZ < 10) {
            // Lane mapping collision vector checks
            const obsAngle = obs.lane * LANE_ANGLE_STEP;
            const projAngle = proj.angle;
            const diffAngle = Math.abs(Math.atan2(Math.sin(obsAngle - projAngle), Math.cos(obsAngle - projAngle)));

            if (diffAngle < 0.5) {
              // Hit obstacle!
              playSoundFX('hit');
              createNeonExplosion(obs.mesh.position, obs.mesh.material.color.getHex());
              
              // Remove projectile
              scene.remove(proj.mesh);
              proj.mesh.geometry.dispose();
              proj.mesh.material.dispose();
              STATE.projectiles.splice(j, 1);

              // Damage obstacle
              obs.health--;
              if (obs.health <= 0) {
                scene.remove(obs.mesh);
                obs.mesh.geometry.dispose();
                obs.mesh.material.dispose();
                STATE.obstacles.splice(i, 1);
                
                // Blast score reward!
                STATE.score += 200 * (STATE.isScoreSurgeActive ? 5 : 1);
                break;
              }
            }
          }
        }

        // Check if obstacle is still active after projectile loop
        if (!STATE.obstacles[i]) continue;

        // Collision Check: Obstacle vs Player Vessel
        const distZ = Math.abs(obs.mesh.position.z - playerGroup.position.z);
        if (distZ < 2.2) {
          const obsAngle = obs.lane * LANE_ANGLE_STEP;
          const diffAngle = Math.abs(Math.atan2(Math.sin(obsAngle - STATE.playerAngle), Math.cos(obsAngle - STATE.playerAngle)));

          if (diffAngle < 0.6) {
            // Collision!
            if (STATE.isInvincible) {
              // Destroy obstacle on impact if invincible
              playSoundFX('hit');
              createNeonExplosion(obs.mesh.position, obs.mesh.material.color.getHex());
              scene.remove(obs.mesh);
              obs.mesh.geometry.dispose();
              obs.mesh.material.dispose();
              STATE.obstacles.splice(i, 1);
              STATE.score += 150;
            } 
            else if (STATE.shieldCapacity > 0) {
              // Shield absorbs hit
              STATE.shieldCapacity--;
              updateShieldHUD();
              triggerShieldBreakFX();
              
              // Destroy obstacle
              createNeonExplosion(obs.mesh.position, obs.mesh.material.color.getHex());
              scene.remove(obs.mesh);
              obs.mesh.geometry.dispose();
              obs.mesh.material.dispose();
              STATE.obstacles.splice(i, 1);
            }
            else {
              // Direct impact crash failure!
              triggerGameOver();
              return;
            }
          }
        }

        // Near miss verification checks (Double Gate boundaries, Edge Case 8)
        if (distZ < 4.0 && obs.mesh.position.z < playerGroup.position.z) {
          const obsAngle = obs.lane * LANE_ANGLE_STEP;
          const diffAngle = Math.abs(Math.atan2(Math.sin(obsAngle - STATE.playerAngle), Math.cos(obsAngle - STATE.playerAngle)));

          if (!obs.nearMissTriggered && diffAngle < 0.65) {
            obs.nearMissTriggered = true;
            triggerNearMiss();
          }
        }

        // Clean up passed obstacles (Edge Case 10 Z-clipping boundaries)
        if (obs.mesh.position.z > 20) {
          scene.remove(obs.mesh);
          obs.mesh.geometry.dispose();
          obs.mesh.material.dispose();
          STATE.obstacles.splice(i, 1);
          
          if (STATE.isGameRunning) {
            STATE.obstaclesPassedCount++;
            STATE.score += 150 * (STATE.isScoreSurgeActive ? 5 : 1);
            playSoundFX('nearmiss');
          }
        }
      }

      // 9. Powerups/Hazards physics progression & collections
      for (let i = STATE.powerups.length - 1; i >= 0; i--) {
        const item = STATE.powerups[i];
        
        // Pull items towards ship if Shard Magnet is active
        if (STATE.isMagnetActive && item.mesh.position.z > -100) {
          const target = playerGroup.position.clone();
          item.mesh.position.lerp(target, 0.08 * frameDelta);
        } else {
          item.mesh.position.z += item.speed * STATE.speedLevel * frameDelta;
        }

        item.mesh.rotation.y += 0.02 * frameDelta;
        item.mesh.rotation.x += 0.01 * frameDelta;

        // Collision Check: Item vs Player Vessel
        const distZ = Math.abs(item.mesh.position.z - playerGroup.position.z);
        if (distZ < 2.5) {
          const itemAngle = item.lane * LANE_ANGLE_STEP;
          const diffAngle = Math.abs(Math.atan2(Math.sin(itemAngle - STATE.playerAngle), Math.cos(itemAngle - STATE.playerAngle)));

          if (diffAngle < 0.7 || STATE.isMagnetActive) {
            // Collected powerup/hazard!
            triggerItemCollection(item.type);
            
            // Remove
            scene.remove(item.mesh);
            item.mesh.geometry.dispose();
            item.mesh.material.dispose();
            STATE.powerups.splice(i, 1);
            continue;
          }
        }

        // Clean up passed items
        if (item.mesh.position.z > 20) {
          scene.remove(item.mesh);
          item.mesh.geometry.dispose();
          item.mesh.material.dispose();
          STATE.powerups.splice(i, 1);
        }
      }

      // Soft light ambient pulses fading
      if (pointLight && pointLight.intensity > 12) {
        pointLight.intensity -= 0.3 * frameDelta;
      }

      // Render Three.js passes
      composer.render();
    }

    // ----------------------------------------------------
    // ITEM COLLECTION EFFECTS & DYNAMIC BUFFS
    // ----------------------------------------------------
    function triggerItemCollection(type) {
      if (type === 'shard') {
        STATE.neonShardsCount++;
        document.getElementById('shards-value').innerText = String(STATE.neonShardsCount).padStart(3, '0');
        STATE.score += 100;
        playSoundFX('shards');
      } 
      else if (type === 'shield') {
        STATE.shieldCapacity = Math.min(STATE.maxShieldCapacity, STATE.shieldCapacity + 1);
        updateShieldHUD();
        playSoundFX('shield_up');
      }
      else if (type === 'boost_battery') {
        STATE.boostEnergy = Math.min(STATE.maxBoostEnergy, STATE.boostEnergy + 40);
        playSoundFX('shield_up');
      }
      else if (type === 'blaster_ammo') {
        STATE.laserAmmo = Math.min(999, STATE.laserAmmo + 40);
        document.getElementById('ammo-value').innerText = String(STATE.laserAmmo).padStart(3, '0');
        playSoundFX('shards');
      }
      else if (type === 'invincibility') {
        STATE.isInvincible = true;
        STATE.invincibilityTime = 6.0; // 6 seconds
        showBuffBanner('INVINCIBLE', 'var(--cyan)');
        playSoundFX('shield_up');
      }
      else if (type === 'magnet') {
        STATE.isMagnetActive = true;
        STATE.magnetTime = 8.0;
        showBuffBanner('MAGNET ACTIVE', 'var(--yellow)');
        playSoundFX('shards');
      }
      else if (type === 'time_warp') {
        STATE.isTimeWarpActive = true;
        STATE.timeWarpTime = 6.0;
        showBuffBanner('TIME WARP SLOW', 'var(--green)');
        playSoundFX('shield_up');
      }
      else if (type === 'emp') {
        triggerEMPSchockwave();
      }
      else if (type === 'surge') {
        STATE.isScoreSurgeActive = true;
        STATE.scoreSurgeTime = 8.0;
        showBuffBanner('SCORE SURGE x5', 'var(--magenta)');
        playSoundFX('shield_up');
      }
      // Hazards (Only hit if NOT invincible/shielded)
      else if (!STATE.isInvincible) {
        if (type === 'hazard_glitch') {
          triggerGlitchStrobe();
        } 
        else if (type === 'hazard_invert') {
          STATE.isControlsInverted = true;
          STATE.controlsInvertedTime = 5.0;
          showBuffBanner('CONTROLS REVERSED', 'var(--red)');
          playSoundFX('glitch');
        } 
        else if (type === 'hazard_drain') {
          STATE.boostEnergy = 0;
          showBuffBanner('BATTERY CRITICAL', 'var(--red)');
          playSoundFX('hit');
        }
      }
    }

    function showBuffBanner(text, color) {
      const banner = document.getElementById('buff-banner');
      banner.innerText = text;
      banner.style.color = color;
      banner.style.textShadow = `0 0 10px ${color}`;
      banner.style.opacity = 1;
    }

    function triggerEMPSchockwave() {
      playSoundFX('emp');
      
      // Clear all active obstacles
      STATE.obstacles.forEach(obs => {
        createNeonExplosion(obs.mesh.position, obs.mesh.material.color.getHex());
        scene.remove(obs.mesh);
        obs.mesh.geometry.dispose();
        obs.mesh.material.dispose();
        STATE.score += 100;
      });
      STATE.obstacles = [];

      // Massive flash effect
      if (pointLight) {
        pointLight.intensity = 45.0;
        pointLight.color.setHex(0xff00ff);
      }
    }

    function triggerGlitchStrobe() {
      playSoundFX('glitch');
      
      const glitch = document.getElementById('crt-glitch');
      glitch.style.opacity = 1;
      glitch.classList.add('glitching');

      setTimeout(() => {
        glitch.style.opacity = 0;
        glitch.classList.remove('glitching');
      }, 1000);
    }

    function triggerShieldBreakFX() {
      playSoundFX('hit');
      
      // Red flash on pointlight
      if (pointLight) {
        pointLight.color.setHex(0xff3131);
        pointLight.intensity = 25.0;
      }
    }

    function updateShieldHUD() {
      const display = document.getElementById('shield-display');
      const nodes = display.children;
      
      for (let i = 0; i < 3; i++) {
        if (i < STATE.shieldCapacity) {
          nodes[i].className = 'shield-node active';
        } else {
          nodes[i].className = 'shield-node empty';
        }
      }

      // Scale Shield Bubble Mesh visual opacity
      if (STATE.playerShieldMesh) {
        STATE.playerShieldMesh.material.opacity = STATE.shieldCapacity > 0 ? 0.35 : 0;
      }
    }

    // ----------------------------------------------------
    // DYNAMIC LEVEL CLEAR & UPGRADE SHOP
    // ----------------------------------------------------
    function triggerLevelClear() {
      STATE.isGameRunning = false;
      cancelAnimationFrame(animationFrameId);
      if (sequencerTimer) clearTimeout(sequencerTimer);
      pauseGame();

      // Display Upgrade Bay Overlay
      document.getElementById('hud').classList.add('hidden');
      document.getElementById('keyboard-dashboard').classList.add('hidden');
      
      document.getElementById('upgrade-shards').innerText = STATE.neonShardsCount;
      document.getElementById('upgrade-screen').classList.remove('hidden');

      // Update shop buy buttons states
      updateShopButtons();
    }

    function updateShopButtons() {
      const shieldBtn = document.getElementById('buy-shield');
      const ammoBtn = document.getElementById('buy-ammo');
      const boostBtn = document.getElementById('buy-boost');
      const blasterBtn = document.getElementById('buy-blaster');

      // Shield Nodes Upgrade
      if (STATE.shieldCapacity >= STATE.maxShieldCapacity) {
        shieldBtn.innerText = "MAXED";
        shieldBtn.className = "btn-buy disabled";
      } else {
        shieldBtn.innerText = "Buy (10 Shards)";
        shieldBtn.className = STATE.neonShardsCount >= 10 ? "btn-buy" : "btn-buy disabled";
      }

      // Ammo Upgrade
      ammoBtn.innerText = "Buy (5 Shards)";
      ammoBtn.className = STATE.neonShardsCount >= 5 ? "btn-buy" : "btn-buy disabled";

      // Boost Battery Upgrade
      if (STATE.boostUpgradeTier >= 3) {
        boostBtn.innerText = "MAXED";
        boostBtn.className = "btn-buy disabled";
      } else {
        boostBtn.innerText = `Buy (15 Shards)`;
        boostBtn.className = STATE.neonShardsCount >= 15 ? "btn-buy" : "btn-buy disabled";
      }

      // Blaster Dissipation Rate Upgrade
      if (STATE.blasterUpgradeTier >= 3) {
        blasterBtn.innerText = "MAXED";
        blasterBtn.className = "btn-buy disabled";
      } else {
        blasterBtn.innerText = `Buy (15 Shards)`;
        blasterBtn.className = STATE.neonShardsCount >= 15 ? "btn-buy" : "btn-buy disabled";
      }
    }

    // Connect Upgrade Shopping Click actions
    document.getElementById('buy-shield').addEventListener('click', () => {
      if (STATE.shieldCapacity < STATE.maxShieldCapacity && STATE.neonShardsCount >= 10) {
        STATE.neonShardsCount -= 10;
        STATE.shieldCapacity++;
        playSoundFX('shield_up');
        document.getElementById('upgrade-shards').innerText = STATE.neonShardsCount;
        updateShopButtons();
      }
    });

    document.getElementById('buy-ammo').addEventListener('click', () => {
      if (STATE.neonShardsCount >= 5) {
        STATE.neonShardsCount -= 5;
        STATE.laserAmmo = Math.min(999, STATE.laserAmmo + 40);
        playSoundFX('shards');
        document.getElementById('upgrade-shards').innerText = STATE.neonShardsCount;
        updateShopButtons();
      }
    });

    document.getElementById('buy-boost').addEventListener('click', () => {
      if (STATE.boostUpgradeTier < 3 && STATE.neonShardsCount >= 15) {
        STATE.neonShardsCount -= 15;
        STATE.boostUpgradeTier++;
        playSoundFX('shield_up');
        document.getElementById('upgrade-shards').innerText = STATE.neonShardsCount;
        updateShopButtons();
      }
    });

    document.getElementById('buy-blaster').addEventListener('click', () => {
      if (STATE.blasterUpgradeTier < 3 && STATE.neonShardsCount >= 15) {
        STATE.neonShardsCount -= 15;
        STATE.blasterUpgradeTier++;
        playSoundFX('shield_up');
        document.getElementById('upgrade-shards').innerText = STATE.neonShardsCount;
        updateShopButtons();
      }
    });

    document.getElementById('btn-next-level').addEventListener('click', () => {
      document.getElementById('upgrade-screen').classList.add('hidden');
      
      // Advance variables
      STATE.currentLevel++;
      document.getElementById('level-title').innerText = `Level ${STATE.currentLevel}`;
      
      // Decrement spawns checks for faster pace
      STATE.spawnInterval = Math.max(22, 45 - STATE.currentLevel * 3);
      STATE.levelTimeLeft = 30.0;

      // Sync shards counts back to active gameplay HUD
      document.getElementById('shards-value').innerText = String(STATE.neonShardsCount).padStart(3, '0');
      document.getElementById('ammo-value').innerText = String(STATE.laserAmmo).padStart(3, '0');
      updateShieldHUD();

      // Show HUD
      document.getElementById('hud').classList.remove('hidden');
      document.getElementById('keyboard-dashboard').classList.remove('hidden');

      resumeGame();
      clock.getDelta(); // Clear timers
      
      STATE.isGameRunning = true;
      animate();
      startSynthSequencer();
    });

    // ----------------------------------------------------
    // VEHICLE PARTICLES EXHAUST & EXPLOSIONS
    // ----------------------------------------------------
    function createExhaustParticle() {
      // Cylindrical coordinates based on ship engine tail positions
      const particleGeom = new THREE.BoxGeometry(0.3, 0.3, 0.3);
      const color = STATE.boostActive ? 0x00f0ff : 0xff007f;
      const mat = new THREE.MeshBasicMaterial({
        color: color,
        transparent: true,
        opacity: 0.8
      });
      const mesh = new THREE.Mesh(particleGeom, mat);
      
      // Start behind the ship
      mesh.position.copy(playerGroup.position);
      mesh.position.z -= 1.0;
      mesh.position.y += (Math.random() - 0.5) * 0.4;
      mesh.position.x += (Math.random() - 0.5) * 0.4;

      scene.add(mesh);
      exhaustParticles.push({
        mesh: mesh,
        vx: (Math.random() - 0.5) * 0.15,
        vy: (Math.random() - 0.5) * 0.15,
        vz: 1.8 + Math.random() * 2.5, // moving backward
        life: 1.0 // opacity fade
      });
    }

    function updateExhaustParticles(frameDelta) {
      for (let i = exhaustParticles.length - 1; i >= 0; i--) {
        const p = exhaustParticles[i];
        p.mesh.position.x += p.vx * frameDelta;
        p.mesh.position.y += p.vy * frameDelta;
        p.mesh.position.z += p.vz * frameDelta;
        p.life -= 0.045 * frameDelta;
        
        p.mesh.material.opacity = p.life;
        p.mesh.scale.setScalar(p.life);

        if (p.life <= 0) {
          scene.remove(p.mesh);
          p.mesh.geometry.dispose();
          p.mesh.material.dispose();
          exhaustParticles.splice(i, 1);
        }
      }
    }

    // Glowing multi-colored shard explosion
    function createNeonExplosion(position, colorHex) {
      const particleCount = 20;
      const geom = new THREE.BoxGeometry(0.4, 0.4, 0.4);
      
      for (let k = 0; k < particleCount; k++) {
        const mat = new THREE.MeshBasicMaterial({
          color: colorHex,
          transparent: true,
          opacity: 0.95
        });
        const mesh = new THREE.Mesh(geom, mat);
        mesh.position.copy(position);
        scene.add(mesh);

        // Vector velocities
        const angle = Math.random() * Math.PI * 2;
        const speed2D = 0.5 + Math.random() * 1.5;
        
        STATE.particles.push({
          mesh: mesh,
          vx: Math.cos(angle) * speed2D,
          vy: Math.sin(angle) * speed2D,
          vz: -2.0 + Math.random() * 4.0,
          life: 1.0
        });
      }

      // Execute secondary particle checks
      setTimeout(() => {
        updateExplosionParticles();
      }, 10);
    }

    function updateExplosionParticles() {
      // Loop over global debris
      for (let i = STATE.particles.length - 1; i >= 0; i--) {
        const p = STATE.particles[i];
        p.mesh.position.x += p.vx * 0.15;
        p.mesh.position.y += p.vy * 0.15;
        p.mesh.position.z += p.vz * 0.15;
        p.life -= 0.05;
        
        p.mesh.material.opacity = p.life;
        p.mesh.scale.setScalar(p.life);

        if (p.life <= 0) {
          scene.remove(p.mesh);
          p.mesh.geometry.dispose();
          p.mesh.material.dispose();
          STATE.particles.splice(i, 1);
        }
      }
    }

    // ----------------------------------------------------
    // DYNAMIC GAME STATE TRIGGERS
    // ----------------------------------------------------
    function triggerNearMiss() {
      STATE.score += 250;
      playSoundFX('nearmiss');
      
      const indicator = document.getElementById('near-miss-indicator');
      indicator.classList.remove('near-miss-animate');
      void indicator.offsetWidth; // Repaint trigger
      indicator.classList.add('near-miss-animate');
    }

    function triggerGameOver() {
      STATE.isGameRunning = false;
      cancelAnimationFrame(animationFrameId);
      
      if (sequencerTimer) clearTimeout(sequencerTimer);
      
      playSoundFX('crash');

      // Stop audio scheduler loops
      pauseGame();

      // Lock cursor out on death
      document.exitPointerLock();

      // Update High Scores
      if (STATE.score > STATE.highScore) {
        STATE.highScore = STATE.score;
        try {
          localStorage.setItem('neon_vibe_dodger_highscore', STATE.highScore);
        } catch (e) {
          console.warn("Storage API disabled. Highscore not saved.");
        }
      }

      // Display Overlays
      document.getElementById('hud').classList.add('hidden');
      document.getElementById('keyboard-dashboard').classList.add('hidden');
      document.getElementById('final-score').innerText = String(STATE.score).padStart(5, '0');
      document.getElementById('high-score').innerText = String(STATE.highScore).padStart(5, '0');
      document.getElementById('game-over-screen').classList.remove('hidden');
    }

    function resetGameState() {
      // Clear 3D Obstacles
      STATE.obstacles.forEach(obs => {
        scene.remove(obs.mesh);
        obs.mesh.geometry.dispose();
        obs.mesh.material.dispose();
      });
      STATE.obstacles = [];

      // Clear Projectiles
      STATE.projectiles.forEach(p => {
        scene.remove(p.mesh);
        p.mesh.geometry.dispose();
        p.mesh.material.dispose();
      });
      STATE.projectiles = [];

      // Clear Collectibles
      STATE.powerups.forEach(p => {
        scene.remove(p.mesh);
        p.mesh.geometry.dispose();
        p.mesh.material.dispose();
      });
      STATE.powerups = [];

      // Reset variables
      STATE.score = 0;
      STATE.speedLevel = 1.0;
      STATE.spawnTimer = 0;
      STATE.playerAngle = 0;
      STATE.playerAngleTarget = 0;
      STATE.obstaclesPassedCount = 0;
      STATE.neonShardsCount = 0;
      STATE.laserAmmo = 40;
      STATE.shieldCapacity = 0;
      STATE.currentLevel = 1;
      STATE.levelTimeLeft = 30.0;
      STATE.boostEnergy = 100;
      
      STATE.boostUpgradeTier = 0;
      STATE.blasterUpgradeTier = 0;

      // Buffs
      STATE.isInvincible = false;
      STATE.isMagnetActive = false;
      STATE.isTimeWarpActive = false;
      STATE.isScoreSurgeActive = false;
      STATE.isControlsInverted = false;
      
      synthBPM = 115;
      currentBeat = 0;

      // Position tunnel rings
      STATE.ribs.forEach((ring, i) => {
        ring.position.set(0, 0, -(i * (TUNNEL_LENGTH / 35)));
      });

      playerGroup.position.set(0, -TUNNEL_RADIUS + 0.6, -10);
      playerGroup.rotation.set(0, 0, 0);

      document.getElementById('score-value').innerText = "00000";
      document.getElementById('shards-value').innerText = "000";
      document.getElementById('ammo-value').innerText = "040";
      document.getElementById('speed-level').innerText = "1.0x";
      document.getElementById('multiplier-badge').innerText = "x1";
      document.getElementById('level-title').innerText = "Level 1";
      
      updateShieldHUD();
    }

    // Connect Button Gestures
    document.getElementById('btn-start').addEventListener('click', () => {
      initAudio();
      
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      STATE.mouseEnabled = document.getElementById('toggle-mouse').checked;

      // Hide start screen overlay
      document.getElementById('start-screen').classList.add('hidden');
      document.getElementById('hud').classList.remove('hidden');
      document.getElementById('keyboard-dashboard').classList.remove('hidden');
      
      if (STATE.mouseEnabled) {
        canvas.requestPointerLock();
      }

      resetGameState();
      
      STATE.isGameRunning = true;
      animate();
      startSynthSequencer();
    });

    document.getElementById('btn-restart').addEventListener('click', () => {
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      document.getElementById('game-over-screen').classList.add('hidden');
      document.getElementById('hud').classList.remove('hidden');
      document.getElementById('keyboard-dashboard').classList.remove('hidden');
      
      if (STATE.mouseEnabled) {
        canvas.requestPointerLock();
      }

      resetGameState();

      STATE.isGameRunning = true;
      animate();
      startSynthSequencer();
    });

    document.getElementById('btn-reload').addEventListener('click', () => {
      window.location.reload();
    });

    // ----------------------------------------------------
    // INPUT HANDLERS & MOUSE RELATIVE SHIFTS
    // ----------------------------------------------------
    window.addEventListener('keydown', (e) => {
      const key = e.key.toLowerCase();
      if (key === 'a' || key === 'arrowleft') keyMap.left = true;
      if (key === 'd' || key === 'arrowright') keyMap.right = true;
      if (key === 'shift') keyMap.boost = true;
      if (e.key === ' ' || key === 'spacebar') {
        e.preventDefault();
        // Arcade pacing: Fire blasters manual-shoot discrete triggers
        if (!keyMap.shoot) {
          keyMap.shoot = true;
          fireBlaster();
        }
      }
    });

    window.addEventListener('keyup', (e) => {
      const key = e.key.toLowerCase();
      if (key === 'a' || key === 'arrowleft') keyMap.left = false;
      if (key === 'd' || key === 'arrowright') keyMap.right = false;
      if (key === 'shift') keyMap.boost = false;
      if (e.key === ' ' || key === 'spacebar') keyMap.shoot = false;
    });

    // Capture Relative pointer lock mouse coordinates
    window.addEventListener('mousemove', (e) => {
      if (STATE.isGameRunning && STATE.mouseEnabled) {
        if (STATE.isPointerLocked) {
          // Locked coords movement multiplier (Highly responsive relative inputs)
          STATE.playerAngleTarget += e.movementX * 0.0035;
        } else {
          // Standard browser hover layout coords fallback
          const normalizedX = (e.clientX / window.innerWidth) * 2 - 1;
          STATE.playerAngleTarget = normalizedX * Math.PI * 0.95;
        }
      }
    });

    // Click trigger manual arcade blasters when mouse is steering
    window.addEventListener('mousedown', (e) => {
      if (STATE.isGameRunning && STATE.mouseEnabled && STATE.isPointerLocked) {
        if (e.button === 0) {
          // Left click shoot blasters
          fireBlaster();
        }
      }
    });

    // Tab background suspends (Edge Case 5 visibility loops)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        STATE.isGameRunning = false;
        pauseGame();
        // Flush inputs
        keyMap.left = false;
        keyMap.right = false;
        keyMap.boost = false;
        keyMap.shoot = false;
      } else {
        if (document.getElementById('start-screen').classList.contains('hidden') && 
            document.getElementById('game-over-screen').classList.contains('hidden') &&
            document.getElementById('upgrade-screen').classList.contains('hidden')) {
          resumeGame();
          clock.getDelta(); // Reset delta
          STATE.isGameRunning = true;
          animate();
          startSynthSequencer();
        }
      }
    });

    // Window focus loss flush registers (Edge Case 11)
    window.addEventListener('blur', () => {
      keyMap.left = false;
      keyMap.right = false;
      keyMap.boost = false;
      keyMap.shoot = false;
    });

    // Boot Graphics Framework immediately on load
    window.addEventListener('load', () => {
      initThree();
    });
  </script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
print("index.html generated successfully!")
