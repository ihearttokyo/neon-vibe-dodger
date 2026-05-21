import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>NEON VIBE: CYBER RUNNER</title>
  
  <!-- SEO Tags -->
  <meta name="description" content="A premium 3D synthwave tunnel dodge game built with Three.js and procedural Web Audio. Fully responsive with an epilepsy-safe visual harness.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
  
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
      --bg-dark: #03001e;
      --bg-light: #7303c0;
      --glass-bg: rgba(10, 10, 25, 0.7);
      --glass-border: rgba(0, 240, 255, 0.25);
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
      font-family: 'Inter', sans-serif;
      color: #fff;
      touch-action: none;
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

    /* Screen Overlays & Interfaces */
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
      transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.5s;
      background: radial-gradient(circle at center, rgba(12, 5, 28, 0.4) 0%, rgba(3, 0, 30, 0.9) 100%);
    }

    .screen-overlay.hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }

    .glass-card {
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      padding: 40px;
      max-width: 500px;
      width: 90%;
      text-align: center;
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), 
                  0 0 30px rgba(255, 0, 127, 0.15), 
                  inset 0 0 15px rgba(0, 240, 255, 0.05);
      transform: translateY(0);
      animation: float-in 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes float-in {
      from {
        opacity: 0;
        transform: translateY(30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .game-title {
      font-family: 'Orbitron', sans-serif;
      font-size: 3rem;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 4px;
      margin-bottom: 15px;
      background: linear-gradient(135deg, var(--cyan) 0%, var(--magenta) 50%, var(--purple) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 15px rgba(0, 240, 255, 0.3));
    }

    .tagline {
      font-size: 0.95rem;
      line-height: 1.6;
      color: #a0aec0;
      margin-bottom: 30px;
    }

    /* Interactive Switch Controls */
    .control-row {
      margin-bottom: 35px;
      text-align: left;
    }

    .form-group {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 0;
      border-bottom: 1px solid rgba(0, 240, 255, 0.1);
    }

    .form-group:last-child {
      border-bottom: none;
    }

    .form-label {
      font-family: 'Orbitron', sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      letter-spacing: 1px;
      color: #e2e8f0;
      text-transform: uppercase;
    }

    .form-desc {
      font-size: 0.75rem;
      color: #718096;
      margin-top: 3px;
    }

    /* Switch Styling */
    .switch {
      position: relative;
      display: inline-block;
      width: 52px;
      height: 28px;
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
      transition: .4s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: 34px;
      border: 1px solid rgba(0, 240, 255, 0.2);
    }

    .slider:before {
      position: absolute;
      content: "";
      height: 20px;
      width: 20px;
      left: 3px;
      bottom: 3px;
      background-color: #718096;
      transition: .4s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: 50%;
    }

    input:checked + .slider {
      background-color: rgba(0, 240, 255, 0.2);
      border-color: var(--cyan);
      box-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
    }

    input:checked + .slider:before {
      transform: translateX(24px);
      background-color: var(--cyan);
      box-shadow: 0 0 10px var(--cyan);
    }

    /* Cyber button styling */
    .btn-cyber {
      width: 100%;
      background: linear-gradient(135deg, var(--cyan) 0%, var(--purple) 100%);
      border: none;
      border-radius: 12px;
      padding: 16px 32px;
      color: #fff;
      font-family: 'Orbitron', sans-serif;
      font-weight: 900;
      font-size: 1.1rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
      position: relative;
      overflow: hidden;
    }

    .btn-cyber:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 35px rgba(0, 240, 255, 0.7), 0 0 15px rgba(255, 0, 127, 0.4);
    }

    .btn-cyber:active {
      transform: translateY(1px);
    }

    /* HUD elements */
    #hud {
      position: absolute;
      top: 30px;
      width: 100%;
      padding: 0 40px;
      z-index: 5;
      display: flex;
      justify-content: space-between;
      pointer-events: none;
      transition: opacity 0.5s;
    }

    #hud.hidden {
      opacity: 0;
    }

    .hud-element {
      background: rgba(10, 10, 25, 0.6);
      border: 1px solid var(--glass-border);
      border-radius: 12px;
      padding: 10px 20px;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      display: flex;
      flex-direction: column;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }

    .hud-label {
      font-family: 'Orbitron', sans-serif;
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #718096;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    .hud-value {
      font-family: 'Orbitron', sans-serif;
      font-size: 1.4rem;
      font-weight: 900;
      color: var(--cyan);
      letter-spacing: 1.5px;
      text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
    }

    #multiplier-badge {
      display: inline-block;
      margin-left: 10px;
      background: linear-gradient(135deg, var(--magenta) 0%, var(--purple) 100%);
      color: #fff;
      font-size: 0.75rem;
      padding: 2px 8px;
      border-radius: 6px;
      vertical-align: middle;
      text-shadow: none;
      box-shadow: 0 0 10px rgba(255, 0, 127, 0.4);
    }

    /* Screen shake / stroboscopic stabs */
    .shake-animation {
      animation: screen-shake 0.15s infinite;
    }

    @keyframes screen-shake {
      0% { transform: translate(0, 0); }
      20% { transform: translate(-4px, 4px); }
      40% { transform: translate(-4px, -4px); }
      60% { transform: translate(4px, 4px); }
      80% { transform: translate(4px, -4px); }
      100% { transform: translate(0, 0); }
    }

    /* Near miss pop indicator */
    #near-miss-indicator {
      position: absolute;
      top: 30%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.5);
      z-index: 4;
      font-family: 'Orbitron', sans-serif;
      font-weight: 900;
      font-size: 3rem;
      letter-spacing: 4px;
      text-transform: uppercase;
      background: linear-gradient(135deg, #fff 0%, var(--cyan) 50%, var(--magenta) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      opacity: 0;
      pointer-events: none;
    }

    .near-miss-animate {
      animation: near-miss-flash 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes near-miss-flash {
      0% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.5);
        filter: blur(10px);
      }
      15% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1.1);
        filter: blur(0px);
      }
      30% {
        transform: translate(-50%, -50%) scale(1.0);
      }
      80% {
        opacity: 1;
      }
      100% {
        opacity: 0;
        transform: translate(-50%, -100%) scale(0.85);
        filter: blur(5px);
      }
    }

    /* Small helpful tips overlay */
    #controls-tip {
      position: absolute;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 5;
      background: rgba(10, 10, 25, 0.6);
      border: 1px solid rgba(0, 240, 255, 0.15);
      border-radius: 30px;
      padding: 8px 20px;
      font-family: 'Orbitron', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 1px;
      color: #718096;
      backdrop-filter: blur(8px);
      pointer-events: none;
      transition: opacity 0.5s;
    }

    #controls-tip.hidden {
      opacity: 0;
    }

    .key-badge {
      display: inline-block;
      background: rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      font-weight: 900;
      margin: 0 2px;
    }

    /* Epilepsy safety notification bar */
    #safety-badge {
      position: absolute;
      top: 15px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(255, 0, 127, 0.15);
      border: 1px solid rgba(255, 0, 127, 0.3);
      border-radius: 6px;
      padding: 4px 12px;
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 1px;
      color: var(--magenta);
      z-index: 6;
      text-transform: uppercase;
      box-shadow: 0 0 10px rgba(255, 0, 127, 0.1);
      display: none;
    }

    #safety-badge.active {
      display: block;
    }
  </style>
</head>
<body>
  <canvas id="game-canvas"></canvas>

  <!-- Epilepsy Safety Active Badge -->
  <div id="safety-badge">Safety Visual Mode Enabled</div>

  <!-- Dynamic Near Miss Pop Element -->
  <div id="near-miss-indicator">Near Miss</div>

  <!-- Screen 1: Splash/Start Screen -->
  <div id="start-screen" class="screen-overlay">
    <div class="glass-card">
      <h1 class="game-title">Neon Vibe</h1>
      <p class="tagline">Navigate the hyper-speed rotating neon tunnel and dodge intense space obstacles in a pure synthwave flow state.</p>
      
      <div class="control-row">
        <!-- Epilepsy Toggle -->
        <div class="form-group">
          <div>
            <div class="form-label">Safe Visual Mode</div>
            <div class="form-desc">Disables intense strobes & flashy color changes</div>
          </div>
          <label class="switch">
            <input type="checkbox" id="toggle-safety">
            <span class="slider"></span>
          </label>
        </div>

        <!-- Audio Toggle -->
        <div class="form-group">
          <div>
            <div class="form-label">Procedural Synth Audio</div>
            <div class="form-desc">Synthesized retro beats & 80s bass loops</div>
          </div>
          <label class="switch">
            <input type="checkbox" id="toggle-audio" checked>
            <span class="slider"></span>
          </label>
        </div>

        <!-- Control Type Toggle -->
        <div class="form-group">
          <div>
            <div class="form-label">Mouse Control Mode</div>
            <div class="form-desc">Fly with cursor inside the tunnel</div>
          </div>
          <label class="switch">
            <input type="checkbox" id="toggle-mouse" checked>
            <span class="slider"></span>
          </label>
        </div>
      </div>

      <button id="btn-start" class="btn-cyber">Start Engine</button>
    </div>
  </div>

  <!-- Screen 2: Game Over Screen -->
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

  <!-- Screen 3: GPU/WebGL Context Lost Fallback Screen -->
  <div id="context-lost-screen" class="screen-overlay hidden">
    <div class="glass-card" style="border-color: var(--magenta);">
      <h1 class="game-title">Graphics Reset</h1>
      <p class="tagline">Your WebGL graphics context was lost due to GPU resource limits.</p>
      <button id="btn-reload" class="btn-cyber">Reinitialize</button>
    </div>
  </div>

  <!-- HUD overlay element -->
  <div id="hud" class="hidden">
    <div class="hud-element" id="score-container">
      <span class="hud-label">Score</span>
      <span class="hud-value" id="score-value">00000</span>
    </div>
    <div class="hud-element" id="multiplier-container">
      <span class="hud-label">Speed Level</span>
      <span class="hud-value"><span id="speed-level">1.0x</span><span id="multiplier-badge">x1</span></span>
    </div>
  </div>

  <!-- Responsive Flight Tips Banner -->
  <div id="controls-tip" class="hidden">
    USE <span class="key-badge">A</span> / <span class="key-badge">D</span> OR <span class="key-badge">←</span> / <span class="key-badge">→</span> TO DODGE
  </div>

  <!-- Procedural audio synthesis code & Game Core -->
  <script>
    // Game constants
    const TUNNEL_RADIUS = 20;
    const TUNNEL_LENGTH = 800;
    const TRACKS_COUNT = 8; // 8 sectors in cylinder

    // Game state
    const STATE = {
      score: 0,
      highScore: 0,
      speedLevel: 1.0,
      obstacleSpeed: 95, // Units per second base
      obstaclesPassedCount: 0,
      spawnTimer: 0,
      spawnInterval: 1.8, // Spawning waves every 1.8s
      playerAngle: 0,
      playerAngleTarget: 0,
      isGameRunning: false,
      isVibeModeSafe: false, // Default is false to load full retro stroboscopic hyper-glowing experience
      audioEnabled: true,
      mouseEnabled: true,
      keys: { left: false, right: false, a: false, d: false },
      obstacles: [],
      starfield: null,
      contextLost: false,
      safetyBadgeEl: document.getElementById('safety-badge'),
      beatTriggered: false
    };

    // Safe localStorage high-score fetch (Edge Case 13)
    try {
      const savedScore = localStorage.getItem('neon_vibe_high_score');
      if (savedScore) {
        STATE.highScore = parseInt(savedScore, 10);
      }
    } catch (e) {
      console.warn("localStorage is disabled or not accessible. High score will reset on page reload.", e);
    }

    // Canvas sizes
    const canvas = document.getElementById('game-canvas');
    let width = window.innerWidth;
    let height = window.innerHeight;

    // Three.js instances
    let renderer, scene, camera, clock, composer;
    let tunnelMesh, tunnelWireframe;
    let playerGroup, playerCrystal;
    let pointLight, dirLight, ambientLight;

    // Advanced neon visuals
    let tunnelRings = [];
    let playerTrail;
    let retroSun, sunMaterial;

    // Web Audio Synthesizer variables (Edge Case 2)
    let audioCtx = null;
    let mainGainNode = null;
    let compressorNode = null;
    let sequencerTimer = null;
    let synthBPM = 115;
    let currentBeat = 0;
    let drumVolume = 0.35;
    let synthVolume = 0.25;

    // Sync checkbox visual elements with STATE default properties explicitly (Edge Case 14 / browser reload sync)
    document.getElementById('toggle-safety').checked = STATE.isVibeModeSafe;
    document.getElementById('toggle-audio').checked = STATE.audioEnabled;
    document.getElementById('toggle-mouse').checked = STATE.mouseEnabled;

    // Setup visual safety flags on checkboxes instantly
    document.getElementById('toggle-safety').addEventListener('change', (e) => {
      STATE.isVibeModeSafe = e.target.checked;
      if (STATE.isVibeModeSafe) {
        STATE.safetyBadgeEl.classList.add('active');
        if (scene) {
          scene.background.setHex(0x05031a);
          scene.fog.color.setHex(0x05031a);
        }
        if (composer && composer.passes[1]) {
          composer.passes[1].strength = 0.6; // Soft bloom in safe mode
        }
      } else {
        STATE.safetyBadgeEl.classList.remove('active');
        if (scene) {
          scene.background.setHex(0x0f001e);
          scene.fog.color.setHex(0x0f001e);
        }
        if (composer && composer.passes[1]) {
          composer.passes[1].strength = 1.8; // High neon bloom
        }
      }
    });

    document.getElementById('toggle-audio').addEventListener('change', (e) => {
      STATE.audioEnabled = e.target.checked;
      toggleMasterAudio(STATE.audioEnabled);
    });

    document.getElementById('toggle-mouse').addEventListener('change', (e) => {
      STATE.mouseEnabled = e.target.checked;
      const tip = document.getElementById('controls-tip');
      if (STATE.isGameRunning) {
        if (STATE.mouseEnabled) {
          tip.innerText = "MOVE CURSOR TO STEER SHIP";
        } else {
          tip.innerText = "USE A / D OR ← / → TO DODGE";
        }
      }
    });

    // ----------------------------------------------------
    // PROCEDURAL WEB AUDIO SYNTH ENGINE (Edge Case 2 & 7)
    // ----------------------------------------------------

    function initAudio() {
      if (audioCtx) return;

      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (!AudioContextClass) return;

      audioCtx = new AudioContextClass();
      
      // Setup dynamic compressor to prevent clipping (Edge Case 7)
      compressorNode = audioCtx.createDynamicsCompressor();
      compressorNode.threshold.setValueAtTime(-12, audioCtx.currentTime);
      compressorNode.knee.setValueAtTime(30, audioCtx.currentTime);
      compressorNode.ratio.setValueAtTime(12, audioCtx.currentTime);
      compressorNode.attack.setValueAtTime(0.003, audioCtx.currentTime);
      compressorNode.release.setValueAtTime(0.08, audioCtx.currentTime);

      mainGainNode = audioCtx.createGain();
      mainGainNode.gain.setValueAtTime(STATE.audioEnabled ? 1.0 : 0.0, audioCtx.currentTime);

      // Route Audio Pipeline
      mainGainNode.connect(compressorNode);
      compressorNode.connect(audioCtx.destination);
    }

    function toggleMasterAudio(enable) {
      if (!mainGainNode || !audioCtx) return;
      // Exponential ramp to prevent abrupt clicks/popping sounds
      mainGainNode.gain.exponentialRampToValueAtTime(
        enable ? 1.0 : 0.0001, 
        audioCtx.currentTime + 0.08
      );
    }

    function playProceduralKick(time) {
      if (!audioCtx || STATE.contextLost) return;

      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.connect(gain);
      gain.connect(mainGainNode);

      // Deep kick drum pitch sweep
      osc.frequency.setValueAtTime(140, time);
      osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.16);

      // Volume envelope
      gain.gain.setValueAtTime(drumVolume, time);
      gain.gain.exponentialRampToValueAtTime(0.0001, time + 0.18);

      osc.start(time);
      // Disconnect node properly (Edge Case 14)
      osc.stop(time + 0.20);
      setTimeout(() => {
        osc.disconnect();
        gain.disconnect();
      }, 300);
    }

    function playProceduralHiHat(time) {
      if (!audioCtx || STATE.contextLost) return;

      const bufferSize = audioCtx.sampleRate * 0.05;
      const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
      const data = buffer.getChannelData(0);

      // Generate white noise for hi-hat hiss
      for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
      }

      const noiseNode = audioCtx.createBufferSource();
      noiseNode.buffer = buffer;

      const filter = audioCtx.createBiquadFilter();
      filter.type = 'highpass';
      filter.frequency.setValueAtTime(7500, time);

      const gain = audioCtx.createGain();
      gain.gain.setValueAtTime(drumVolume * 0.45, time);
      gain.gain.exponentialRampToValueAtTime(0.0001, time + 0.04);

      noiseNode.connect(filter);
      filter.connect(gain);
      gain.connect(mainGainNode);

      noiseNode.start(time);
      noiseNode.stop(time + 0.05);
      
      setTimeout(() => {
        noiseNode.disconnect();
        filter.disconnect();
        gain.disconnect();
      }, 200);
    }

    function playProceduralBass(time, noteIndex) {
      if (!audioCtx || STATE.contextLost) return;

      // Synthwave baseline notes (A minor progression)
      // A1, G1, F1, E1
      const progressNotes = [55.0, 48.99, 43.65, 41.20];
      const baseFreq = progressNotes[noteIndex % progressNotes.length];

      // detuned dual saw oscillators to get standard fat 80s bassline
      const osc1 = audioCtx.createOscillator();
      const osc2 = audioCtx.createOscillator();
      const gainNode = audioCtx.createGain();
      const filterNode = audioCtx.createBiquadFilter();

      osc1.type = 'sawtooth';
      osc2.type = 'sawtooth';

      // Clamp frequency inputs to prevent negatives (Edge Case 7)
      const freq1 = Math.max(0.01, baseFreq - 1.2);
      const freq2 = Math.max(0.01, baseFreq + 1.2);

      osc1.frequency.setValueAtTime(freq1, time);
      osc2.frequency.setValueAtTime(freq2, time);

      filterNode.type = 'lowpass';
      filterNode.frequency.setValueAtTime(250, time);
      // Sweep lowpass cutoff on note strike
      filterNode.frequency.exponentialRampToValueAtTime(800, time + 0.04);
      filterNode.frequency.exponentialRampToValueAtTime(120, time + 0.14);

      gainNode.gain.setValueAtTime(synthVolume, time);
      gainNode.gain.exponentialRampToValueAtTime(0.0001, time + 0.15);

      // Route Synth
      osc1.connect(filterNode);
      osc2.connect(filterNode);
      filterNode.connect(gainNode);
      gainNode.connect(mainGainNode);

      osc1.start(time);
      osc2.start(time);
      osc1.stop(time + 0.16);
      osc2.stop(time + 0.16);

      setTimeout(() => {
        osc1.disconnect();
        osc2.disconnect();
        filterNode.disconnect();
        gainNode.disconnect();
      }, 300);
    }

    function playSoundFX(type) {
      if (!audioCtx || !STATE.audioEnabled || STATE.contextLost) return;

      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      
      osc.connect(gain);
      gain.connect(mainGainNode);

      const time = audioCtx.currentTime;

      if (type === 'dodge') {
        // High neon synth chime
        osc.type = 'sine';
        osc.frequency.setValueAtTime(780, time);
        osc.frequency.exponentialRampToValueAtTime(1560, time + 0.12);
        gain.gain.setValueAtTime(0.12, time);
        gain.gain.exponentialRampToValueAtTime(0.0001, time + 0.15);
        osc.start(time);
        osc.stop(time + 0.16);
      } else if (type === 'nearmiss') {
        // Sci-Fi sweep whistle
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(280, time);
        osc.frequency.exponentialRampToValueAtTime(1180, time + 0.06);
        osc.frequency.exponentialRampToValueAtTime(450, time + 0.2);
        gain.gain.setValueAtTime(0.24, time);
        gain.gain.exponentialRampToValueAtTime(0.0001, time + 0.22);
        osc.start(time);
        osc.stop(time + 0.23);
      } else if (type === 'crash') {
        // Intense noise explosion crash
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(180, time);
        osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.6);
        gain.gain.setValueAtTime(0.65, time);
        gain.gain.exponentialRampToValueAtTime(0.0001, time + 0.65);
        osc.start(time);
        osc.stop(time + 0.7);
      }

      setTimeout(() => {
        osc.disconnect();
        gain.disconnect();
      }, 800);
    }

    // BPM Sequencer Loop Coordinator
    function startSynthSequencer() {
      let nextNoteTime = audioCtx.currentTime;

      function scheduler() {
        if (!STATE.isGameRunning) return;

        while (nextNoteTime < audioCtx.currentTime + 0.08) {
          scheduleBeat(currentBeat, nextNoteTime);
          
          // Move time forward based on dynamic BPM progression
          const secondsPerBeat = 60.0 / synthBPM / 4.0; // 16th notes
          nextNoteTime += secondsPerBeat;
          currentBeat++;
        }
        sequencerTimer = setTimeout(scheduler, 25);
      }
      
      scheduler();
    }

    function scheduleBeat(beat, time) {
      // Four beats per measure
      const step = beat % 16;
      
      // Retro Driving drum Kick pattern (1 and 3 beats)
      if (step === 0 || step === 8) {
        playProceduralKick(time);
        // Sync light flashing to beats
        triggerBeatVibePulse();
      }

      // Snare drum/hat off-beat sizzle
      if (step === 4 || step === 12) {
        playProceduralHiHat(time);
      }

      // Play 80s driving sixteenth-bassline notes
      if (step % 2 === 0) {
        const noteIndex = Math.floor(beat / 4);
        playProceduralBass(time, noteIndex);
      }
    }

    function triggerBeatVibePulse() {
      if (!STATE.isGameRunning) return;
      STATE.beatTriggered = true;
      
      // Strobes disabled if Safe Mode active
      if (STATE.isVibeModeSafe) {
        // Slow color morph
        if (ambientLight) {
          const t = clock.getElapsedTime() * 0.15;
          ambientLight.color.setHSL(t % 1, 0.6, 0.35);
        }
        return;
      }

      // Strobe Mode visual action! Flashes scene lighting on beat
      if (pointLight) {
        pointLight.intensity = 25;
      }

      // Flash background slightly (cyber ambient glow shift)
      if (scene) {
        const strobeColors = [0xff007f, 0x00f0ff, 0x9d00ff];
        const randomColor = strobeColors[Math.floor(Math.random() * strobeColors.length)];
        
        if (dirLight) dirLight.color.setHex(randomColor);
      }

      // Add a tiny screen shake class on beat to feel the sound waves!
      if (!STATE.isVibeModeSafe) {
        document.body.classList.add('shake-animation');
        setTimeout(() => {
          document.body.classList.remove('shake-animation');
        }, 50);
      }
    }

    // ----------------------------------------------------
    // THREE.JS WEBGL RENDER ENGINE (Post-Processing & Shaders)
    // ----------------------------------------------------

    // Retro Sun shaders
    const sunVertexShader = `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `;

    const sunFragmentShader = `
      varying vec2 vUv;
      uniform float time;
      uniform vec3 color1;
      uniform vec3 color2;
      void main() {
        float dist = length(vUv - vec2(0.5));
        if (dist > 0.5) discard;
        
        // Synthwave striped sun pattern
        float threshold = 0.18 + 0.18 * (1.0 - vUv.y);
        float stripe = step(threshold, sin(vUv.y * 36.0 - time * 2.2));
        
        // Orange to Magenta vertical gradient
        vec3 col = mix(color2, color1, vUv.y);
        
        // Smooth edge fade
        float alpha = stripe * smoothstep(0.5, 0.46, dist);
        
        gl_FragColor = vec4(col, alpha);
      }
    `;

    // Initialize Three.js Graphic Framework
    function initThree() {
      clock = new THREE.Clock();

      // Scene
      scene = new THREE.Scene();
      scene.background = new THREE.Color(STATE.isVibeModeSafe ? 0x05031a : 0x0f001e);
      scene.fog = new THREE.FogExp2(STATE.isVibeModeSafe ? 0x05031a : 0x0f001e, 0.0035);

      // Camera
      camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
      camera.position.set(0, 0, 10);
      camera.lookAt(0, 0, -100);

      // WebGL Renderer with dynamic pixel capping (Edge Case 1)
      renderer = new THREE.WebGLRenderer({
        canvas: canvas,
        antialias: true,
        powerPreference: "high-performance",
        alpha: false
      });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.setSize(width, height);
      renderer.toneMapping = THREE.ACESFilmicToneMapping;

      // Handle lost graphics context immediately (Edge Case 6)
      canvas.addEventListener('webglcontextlost', (e) => {
        e.preventDefault();
        STATE.contextLost = true;
        document.getElementById('context-lost-screen').classList.remove('hidden');
        cancelAnimationFrame(animationFrameId);
        if (sequencerTimer) clearTimeout(sequencerTimer);
      }, false);

      canvas.addEventListener('webglcontextrestored', () => {
        window.location.reload();
      }, false);

      // Lighting system
      ambientLight = new THREE.AmbientLight(0xff007f, 0.35);
      scene.add(ambientLight);

      pointLight = new THREE.PointLight(0x00f0ff, 12, 60);
      pointLight.position.set(0, 0, 5);
      scene.add(pointLight);

      dirLight = new THREE.DirectionalLight(0x9d00ff, 1.5);
      dirLight.position.set(0, 1, -1);
      scene.add(dirLight);

      // ----------------------------------------------------
      // POST-PROCESSING PIPELINE (Glowing UnrealBloom)
      // ----------------------------------------------------
      const renderScene = new THREE.RenderPass(scene, camera);
      const bloomPass = new THREE.UnrealBloomPass(
        new THREE.Vector2(window.innerWidth, window.innerHeight),
        STATE.isVibeModeSafe ? 0.6 : 1.8, // Strength of glow
        0.4,  // Radius
        0.85  // Threshold
      );
      bloomPass.threshold = 0.12;
      bloomPass.radius = 0.55;

      composer = new THREE.EffectComposer(renderer);
      composer.addPass(renderScene);
      composer.addPass(bloomPass);

      // Build scrolling grid tunnel
      buildTunnel();

      // Build horizontal striped horizon sun
      buildRetroSun();

      // Build moving neon grid pulse rings
      buildTunnelRings();

      // Build particle lines starfield (hyperspace stretch)
      buildStarfield();

      // Build player vessel + exhaust trail
      buildPlayer();
      buildPlayerTrail();

      // Re-adjust camera and view sizes instantly on resize (Edge Case 3)
      window.addEventListener('resize', handleWindowResize, false);
      
      // Clear keyboard stuck state maps dynamically when window loses focus (Edge Case 11)
      window.addEventListener('blur', clearInputStates);
      window.addEventListener('focus', clearInputStates);
    }

    function buildTunnel() {
      // Primary cylindrical cage mesh
      const geom = new THREE.CylinderGeometry(20, 20, TUNNEL_LENGTH, 16, 60, true);
      geom.rotateX(Math.PI / 2);

      const material = new THREE.MeshBasicMaterial({
        color: 0x1d003b,
        wireframe: true,
        side: THREE.BackSide,
        transparent: true,
        opacity: 0.3
      });

      tunnelMesh = new THREE.Mesh(geom, material);
      tunnelMesh.position.set(0, 0, -TUNNEL_LENGTH / 2 + 10);
      scene.add(tunnelMesh);

      // Secondary layered glowing wireframe for stunning depth parallaxes
      const wireframeGeom = new THREE.CylinderGeometry(20.3, 20.3, TUNNEL_LENGTH, 8, 30, true);
      wireframeGeom.rotateX(Math.PI / 2);
      
      const wireframeMat = new THREE.MeshBasicMaterial({
        color: 0xff007f,
        wireframe: true,
        side: THREE.BackSide,
        transparent: true,
        opacity: 0.12
      });

      tunnelWireframe = new THREE.Mesh(wireframeGeom, wireframeMat);
      tunnelWireframe.position.copy(tunnelMesh.position);
      scene.add(tunnelWireframe);
    }

    function buildRetroSun() {
      const sunGeom = new THREE.PlaneGeometry(150, 150);
      sunMaterial = new THREE.ShaderMaterial({
        vertexShader: sunVertexShader,
        fragmentShader: sunFragmentShader,
        uniforms: {
          time: { value: 0 },
          color1: { value: new THREE.Color(0xff7700) }, // Orange glow
          color2: { value: new THREE.Color(0xff00aa) }  // Magenta glow
        },
        transparent: true,
        depthWrite: false,
        side: THREE.DoubleSide
      });

      retroSun = new THREE.Mesh(sunGeom, sunMaterial);
      retroSun.position.set(0, 0, -380);
      scene.add(retroSun);
    }

    function buildTunnelRings() {
      const ringCount = 12;
      for (let i = 0; i < ringCount; i++) {
        const ringGeom = new THREE.RingGeometry(19.8, 20.2, 32);
        const ringMat = new THREE.MeshBasicMaterial({
          color: i % 2 === 0 ? 0x00f0ff : 0xff007f,
          side: THREE.DoubleSide,
          transparent: true,
          opacity: 0.6
        });
        
        const ring = new THREE.Mesh(ringGeom, ringMat);
        ring.position.set(0, 0, -((i / ringCount) * TUNNEL_LENGTH));
        scene.add(ring);
        tunnelRings.push(ring);
      }
    }

    function buildStarfield() {
      // Create high-fidelity star lines stretching dynamically to simulate hyper-speed (Edge Case 10)
      const lineCount = 350;
      const geom = new THREE.BufferGeometry();
      const positions = new Float32Array(lineCount * 2 * 3); // 2 points per segment
      const colors = new Float32Array(lineCount * 2 * 3);

      for (let i = 0; i < lineCount; i++) {
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * 18.5 + 1.0; 
        
        const x = radius * Math.cos(angle);
        const y = radius * Math.sin(angle);
        const z = -Math.random() * TUNNEL_LENGTH;

        // Line Start
        positions[i * 6] = x;
        positions[i * 6 + 1] = y;
        positions[i * 6 + 2] = z;

        // Line End (Fitted segment trail)
        positions[i * 6 + 3] = x;
        positions[i * 6 + 4] = y;
        positions[i * 6 + 5] = z - 6.0;

        // Colors: mix cyber cyan and magenta
        const isCyan = Math.random() > 0.5;
        const r = isCyan ? 0.0 : 1.0;
        const g = isCyan ? 0.94 : 0.0;
        const b = 1.0;

        colors[i * 6] = r;
        colors[i * 6 + 1] = g;
        colors[i * 6 + 2] = b;

        colors[i * 6 + 3] = r * 0.4;
        colors[i * 6 + 4] = g * 0.4;
        colors[i * 6 + 5] = b * 0.4;
      }

      geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      geom.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const starMat = new THREE.LineBasicMaterial({
        vertexColors: true,
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending
      });

      STATE.starfield = new THREE.LineSegments(geom, starMat);
      scene.add(STATE.starfield);
    }

    function buildPlayer() {
      // Build a premium floating crystal diamond structure
      playerGroup = new THREE.Group();
      playerGroup.position.set(0, -TUNNEL_RADIUS, -10); // Position bottom of tunnel circle
      scene.add(playerGroup);

      // Core diamond geometric crystal
      const geom = new THREE.OctahedronGeometry(1.2, 0);
      const mat = new THREE.MeshStandardMaterial({
        color: 0x00f0ff,
        emissive: 0x0066aa,
        roughness: 0.05,
        metalness: 0.95,
        flatShading: true
      });

      playerCrystal = new THREE.Mesh(geom, mat);
      playerGroup.add(playerCrystal);

      // Outer delicate neon lines wrapping the player crystal
      const outerGeom = new THREE.OctahedronGeometry(1.5, 1);
      const outerMat = new THREE.MeshBasicMaterial({
        color: 0xff007f,
        wireframe: true,
        transparent: true,
        opacity: 0.75
      });
      const outerShell = new THREE.Mesh(outerGeom, outerMat);
      playerGroup.add(outerShell);
    }

    function buildPlayerTrail() {
      // Exhaust fire/sparks trailing behind player jet
      const trailCount = 30;
      const geom = new THREE.BufferGeometry();
      const positions = new Float32Array(trailCount * 3);
      const colors = new Float32Array(trailCount * 3);

      for (let i = 0; i < trailCount; i++) {
        positions[i * 3] = 0;
        positions[i * 3 + 1] = 0;
        positions[i * 3 + 2] = -10;

        const ratio = i / trailCount;
        colors[i * 3] = ratio;       // R gradient toward magenta
        colors[i * 3 + 1] = 0.9 - ratio; // G
        colors[i * 3 + 2] = 1.0;     // B
      }

      geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      geom.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const trailMat = new THREE.PointsMaterial({
        size: 0.65,
        vertexColors: true,
        transparent: true,
        opacity: 0.9,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      playerTrail = new THREE.Points(geom, trailMat);
      scene.add(playerTrail);
    }

    function handleWindowResize() {
      width = window.innerWidth;
      height = window.innerHeight;
      
      if (camera && renderer) {
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
      }
      if (composer) {
        composer.setSize(width, height);
      }
    }

    // Input handlers
    const keyMap = STATE.keys;
    window.addEventListener('keydown', (e) => {
      const key = e.key.toLowerCase();
      if (key === 'a' || key === 'arrowleft') keyMap.left = true;
      if (key === 'd' || key === 'arrowright') keyMap.right = true;
    });

    window.addEventListener('keyup', (e) => {
      const key = e.key.toLowerCase();
      if (key === 'a' || key === 'arrowleft') keyMap.left = false;
      if (key === 'd' || key === 'arrowright') keyMap.right = false;
    });

    // Touch and mouse steering input (Edge Case 12)
    window.addEventListener('mousemove', (e) => {
      if (!STATE.isGameRunning || !STATE.mouseEnabled) return;
      // Map mouse coordinate horizontally to angle
      const normX = e.clientX / window.innerWidth; // 0 to 1
      STATE.playerAngleTarget = (normX * Math.PI * 2.2) - Math.PI * 1.1;
    });

    window.addEventListener('touchmove', (e) => {
      if (!STATE.isGameRunning) return;
      // Force prevent default mobile touch behaviors to block scrolling/zooming
      if (e.cancelable) e.preventDefault();
      
      if (e.touches.length > 0) {
        const touch = e.touches[0];
        const normX = touch.clientX / window.innerWidth;
        STATE.playerAngleTarget = (normX * Math.PI * 2.2) - Math.PI * 1.1;
      }
    }, { passive: false });

    // Touch start also prevents default to block double tap zooms
    window.addEventListener('touchstart', (e) => {
      if (STATE.isGameRunning && e.cancelable) {
        e.preventDefault();
      }
    }, { passive: false });

    function clearInputStates() {
      keyMap.left = false;
      keyMap.right = false;
      keyMap.a = false;
      keyMap.d = false;
    }

    // Spawning coordinates logic mapping obstacles in 8 lanes
    function spawnObstacle() {
      if (!STATE.isGameRunning) return;

      const shapes = ['prism', 'box', 'torus'];
      const chosenShape = shapes[Math.floor(Math.random() * shapes.length)];
      
      // Determine tracks to spawn. Spawn between 1 and 3 obstacles in a wave
      // Guaranteeing safe-path logic by keeping at least two adjacent lanes open (Edge Case 9)
      const obstacleLanes = [];
      const density = Math.min(3, Math.floor(Math.random() * 2) + 1 + Math.floor(STATE.score / 15000));
      
      const activeSlots = [0, 1, 2, 3, 4, 5, 6, 7];
      // Shuffle active slots
      for (let i = activeSlots.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [activeSlots[i], activeSlots[j]] = [activeSlots[j], activeSlots[i]];
      }

      // Pick selected slots
      const selectedTracks = [];
      for (let i = 0; i < density; i++) {
        selectedTracks.push(activeSlots[i]);
      }

      selectedTracks.forEach(lane => {
        const angle = (lane / TRACKS_COUNT) * Math.PI * 2;
        
        // Nested premium design for Obstacles (Inner solid core + outer wireframe)
        const obsGroup = new THREE.Group();

        let innerGeom, outerGeom;
        if (chosenShape === 'box') {
          innerGeom = new THREE.BoxGeometry(1.6, 1.6, 1.6);
          outerGeom = new THREE.BoxGeometry(2.6, 2.6, 2.6);
        } else if (chosenShape === 'torus') {
          innerGeom = new THREE.TorusGeometry(1.1, 0.25, 8, 16);
          outerGeom = new THREE.TorusGeometry(1.8, 0.45, 8, 16);
        } else {
          innerGeom = new THREE.ConeGeometry(1.2, 2.2, 5);
          innerGeom.rotateX(Math.PI / 2);
          outerGeom = new THREE.ConeGeometry(2.0, 3.4, 5);
          outerGeom.rotateX(Math.PI / 2);
        }

        const isCyan = Math.random() > 0.5;
        const color = isCyan ? 0x00f0ff : 0xff007f;
        const glowColor = isCyan ? 0x0088cc : 0xaa0055;

        // Core Solid material with glowing tone
        const innerMat = new THREE.MeshStandardMaterial({
          color: color,
          emissive: glowColor,
          roughness: 0.1,
          metalness: 0.8,
          transparent: true,
          opacity: 0.8,
          flatShading: true
        });

        // Outer neon wireframe shell
        const outerMat = new THREE.MeshBasicMaterial({
          color: color,
          wireframe: true,
          transparent: true,
          opacity: 0.9
        });

        const innerMesh = new THREE.Mesh(innerGeom, innerMat);
        const outerMesh = new THREE.Mesh(outerGeom, outerMat);

        obsGroup.add(innerMesh);
        obsGroup.add(outerMesh);

        obsGroup.position.set(
          (TUNNEL_RADIUS - 0.5) * Math.cos(angle),
          (TUNNEL_RADIUS - 0.5) * Math.sin(angle),
          -TUNNEL_LENGTH + 20 // Spawn far deep inside tunnel (Edge Case 10)
        );

        scene.add(obsGroup);

        // Store custom state
        STATE.obstacles.push({
          mesh: obsGroup,
          angle: angle,
          lane: lane,
          passed: false,
          nearMissTriggered: false,
          spinSpeedX: Math.random() * 2 + 1,
          spinSpeedY: Math.random() * 2 + 1
        });
      });
    }

    // Visibility handlers to prevent minification jumps and warping (Edge Case 5)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (STATE.isGameRunning) {
          pauseGame();
        }
      }
    });

    function pauseGame() {
      if (audioCtx && audioCtx.state === 'running') {
        audioCtx.suspend();
      }
    }

    function resumeGame() {
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    // Main animation run frame loop
    let animationFrameId;
    
    function animate() {
      animationFrameId = requestAnimationFrame(animate);

      // Handle graphics lost context instantly
      if (STATE.contextLost) return;

      const delta = Math.min(0.1, clock.getDelta()); // Cap delta to prevent massive jumps on stutter
      
      // Frame rate independence implementation (Edge Case 4)
      const currentSpeed = STATE.obstacleSpeed * STATE.speedLevel * delta;

      if (STATE.isGameRunning) {
        // Incremental score
        STATE.score += Math.floor(180 * delta);
        document.getElementById('score-value').innerText = String(STATE.score).padStart(5, '0');

        // Linear speed progression loop
        STATE.speedLevel = 1.0 + (STATE.score / 22000);
        synthBPM = 115 + Math.min(45, (STATE.score / 1800)); // Dynamic BPM acceleration
        document.getElementById('speed-level').innerText = STATE.speedLevel.toFixed(1) + 'x';
        document.getElementById('multiplier-badge').innerText = 'x' + Math.floor(STATE.speedLevel);

        // Player movement handling (Keyboard steering)
        if (!STATE.mouseEnabled) {
          const rotationSpeed = 2.8 * delta;
          if (keyMap.left) STATE.playerAngleTarget += rotationSpeed;
          if (keyMap.right) STATE.playerAngleTarget -= rotationSpeed;
        }

        // Smooth radial landing interpolation
        STATE.playerAngle = THREE.MathUtils.lerp(STATE.playerAngle, STATE.playerAngleTarget, 0.15);

        // Update player physical coordinates
        const playerX = (TUNNEL_RADIUS - 0.6) * Math.cos(STATE.playerAngle);
        const playerY = (TUNNEL_RADIUS - 0.6) * Math.sin(STATE.playerAngle);
        playerGroup.position.set(playerX, playerY, -10);

        // Responsive banking and flight tilt animations
        const bankingAngle = (STATE.playerAngleTarget - STATE.playerAngle) * 0.85;
        playerGroup.rotation.z = STATE.playerAngle + Math.PI / 2 + bankingAngle;
        playerCrystal.rotation.y += 1.8 * delta;

        // Hover bobbing effect (float animation)
        const hoverOffset = Math.sin(clock.getElapsedTime() * 4.0) * 0.12;
        playerGroup.position.x += hoverOffset * Math.cos(STATE.playerAngle + Math.PI/2);
        playerGroup.position.y += hoverOffset * Math.sin(STATE.playerAngle + Math.PI/2);

        // Update Player Engine Exhaust sparks trail
        updatePlayerTrail();

        // Animate scrolling double-tunnels
        tunnelMesh.rotation.z += 0.05 * STATE.speedLevel * delta;
        tunnelWireframe.rotation.z -= 0.08 * STATE.speedLevel * delta;

        // Animate deep spaces stars
        animateStarfield(currentSpeed, delta);

        // Update scrolling neon grid rings
        animateTunnelRings(currentSpeed, delta);

        // Update, animate, and check collision on all active obstacles
        updateObstacles(currentSpeed, delta);

        // Update retro sun uniforms
        if (retroSun && sunMaterial) {
          sunMaterial.uniforms.time.value = clock.getElapsedTime();
          
          // Sun pulses on beats!
          if (STATE.beatTriggered) {
            retroSun.scale.set(1.08, 1.08, 1.08);
          } else {
            retroSun.scale.lerp(new THREE.Vector3(1, 1, 1), 0.15);
          }
        }

        // Wave spawner loop coordinator
        STATE.spawnTimer += delta;
        if (STATE.spawnTimer >= STATE.spawnInterval / STATE.speedLevel) {
          spawnObstacle();
          STATE.spawnTimer = 0;
        }

        // Beat fading interpolation logic for lights (Edge Case 15)
        if (pointLight) {
          pointLight.intensity = THREE.MathUtils.lerp(pointLight.intensity, 10, 0.15);
        }
        
        // Reset beat triggers at end of frame
        STATE.beatTriggered = false;
      }

      // Render through blooming composer
      if (composer) {
        composer.render();
      } else {
        renderer.render(scene, camera);
      }
    }

    function updatePlayerTrail() {
      if (!playerTrail) return;
      const positions = playerTrail.geometry.attributes.position.array;
      const count = positions.length / 3;

      // Shift older sparks backward with dispersion
      for (let i = count - 1; i > 0; i--) {
        positions[i * 3] = positions[(i - 1) * 3] + (Math.random() - 0.5) * 0.12;
        positions[i * 3 + 1] = positions[(i - 1) * 3 + 1] + (Math.random() - 0.5) * 0.12;
        positions[i * 3 + 2] = positions[(i - 1) * 3 + 2] + 0.95 + Math.random() * 0.45;
      }

      // Anchored spark index 0 sits at player exhaust jet
      positions[0] = playerGroup.position.x;
      positions[1] = playerGroup.position.y;
      positions[2] = playerGroup.position.z + 1.2;

      playerTrail.geometry.attributes.position.needsUpdate = true;
    }

    function animateStarfield(speed, delta) {
      if (!STATE.starfield) return;

      const positions = STATE.starfield.geometry.attributes.position.array;
      const count = positions.length / 6;
      
      // Dynamic star lines stretch segment length relative to speed
      const stretch = 5.0 + STATE.speedLevel * 9.0;

      for (let i = 0; i < count; i++) {
        // Move line start and end forward
        positions[i * 6 + 2] += speed * 1.5;
        positions[i * 6 + 5] += speed * 1.5;

        // Enforce trailing stretch segment relative to head
        positions[i * 6 + 5] = positions[i * 6 + 2] - stretch;

        // Reset passed segments back to far horizon (Edge Case 10)
        if (positions[i * 6 + 5] > 15) {
          const angle = Math.random() * Math.PI * 2;
          const radius = Math.random() * 18.5 + 1.0;
          const newZ = -TUNNEL_LENGTH;

          positions[i * 6] = radius * Math.cos(angle);
          positions[i * 6 + 1] = radius * Math.sin(angle);
          positions[i * 6 + 2] = newZ;

          positions[i * 6 + 3] = radius * Math.cos(angle);
          positions[i * 6 + 4] = radius * Math.sin(angle);
          positions[i * 6 + 5] = newZ - stretch;
        }
      }

      STATE.starfield.geometry.attributes.position.needsUpdate = true;
    }

    function animateTunnelRings(speed, delta) {
      tunnelRings.forEach(ring => {
        ring.position.z += speed * 1.05;
        ring.rotation.z += 0.01;

        // Scale pulses on beats!
        if (STATE.beatTriggered) {
          ring.scale.set(1.15, 1.15, 1.0);
        } else {
          ring.scale.lerp(new THREE.Vector3(1, 1, 1), 0.12);
        }

        // Fade opacity in distance
        const distZ = ring.position.z;
        if (distZ > 12) {
          ring.position.z = -TUNNEL_LENGTH;
          ring.material.color.setHex(Math.random() > 0.5 ? 0x00f0ff : 0xff007f);
        }

        const normZ = Math.min(1.0, Math.max(0.0, (distZ + TUNNEL_LENGTH) / TUNNEL_LENGTH));
        ring.material.opacity = Math.pow(normZ, 2.5) * 0.65;
      });
    }

    function updateObstacles(speed, delta) {
      for (let i = STATE.obstacles.length - 1; i >= 0; i--) {
        const obs = STATE.obstacles[i];
        
        // Move obstacle toward the player
        obs.mesh.position.z += speed;
        
        // Spin child meshes inside obstacle group independently
        obs.mesh.children.forEach((child, idx) => {
          const mult = idx === 0 ? 1 : -1;
          child.rotation.x += obs.spinSpeedX * delta * mult;
          child.rotation.y += obs.spinSpeedY * delta * mult;
        });

        const distanceZ = obs.mesh.position.z - (-10); // Player sits at Z = -10

        // 1. In-bounds collision testing (Radial coordinate mapping)
        if (Math.abs(distanceZ) < 1.6) {
          // Check radial angle distances
          let diffAngle = Math.abs(obs.angle - STATE.playerAngle);
          diffAngle = Math.min(diffAngle, Math.PI * 2 - diffAngle);

          if (diffAngle < 0.28) {
            triggerGameOver();
            return;
          }

          // 2. Near Miss check trigger (Edge Case 8)
          if (!obs.nearMissTriggered && diffAngle < 0.65) {
            obs.nearMissTriggered = true;
            triggerNearMiss();
          }
        }

        // Clean up passed obstacles (Edge Case 10)
        if (obs.mesh.position.z > 20) {
          scene.remove(obs.mesh);
          obs.mesh.children.forEach(child => {
            child.geometry.dispose();
            child.material.dispose();
          });
          STATE.obstacles.splice(i, 1);
          
          if (STATE.isGameRunning) {
            STATE.obstaclesPassedCount++;
            // Reward dodging
            STATE.score += 150;
            playSoundFX('dodge');
          }
        }
      }
    }

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

      // Update High Scores
      if (STATE.score > STATE.highScore) {
        STATE.highScore = STATE.score;
        try {
          localStorage.setItem('neon_vibe_high_score', STATE.highScore);
        } catch (e) {
          console.warn("Could not save high score to localStorage.", e);
        }
      }

      // Display Overlays
      document.getElementById('hud').classList.add('hidden');
      document.getElementById('controls-tip').classList.add('hidden');
      document.getElementById('final-score').innerText = String(STATE.score).padStart(5, '0');
      document.getElementById('high-score').innerText = String(STATE.highScore).padStart(5, '0');
      document.getElementById('game-over-screen').classList.remove('hidden');
    }

    function resetGameState() {
      // Clear 3D Obstacles
      STATE.obstacles.forEach(obs => {
        scene.remove(obs.mesh);
        obs.mesh.children.forEach(child => {
          child.geometry.dispose();
          child.material.dispose();
        });
      });
      STATE.obstacles = [];

      // Reset variables
      STATE.score = 0;
      STATE.speedLevel = 1.0;
      STATE.spawnTimer = 0;
      STATE.playerAngle = 0;
      STATE.playerAngleTarget = 0;
      STATE.obstaclesPassedCount = 0;
      synthBPM = 115;
      currentBeat = 0;

      // Position tunnel rings
      tunnelRings.forEach((ring, i) => {
        ring.position.set(0, 0, -((i / tunnelRings.length) * TUNNEL_LENGTH));
      });

      playerGroup.position.set(0, -TUNNEL_RADIUS + 0.6, -10);
      playerGroup.rotation.set(0, 0, 0);

      document.getElementById('score-value').innerText = "00000";
      document.getElementById('speed-level').innerText = "1.0x";
      document.getElementById('multiplier-badge').innerText = "x1";
    }

    // Connect Button Gestures
    document.getElementById('btn-start').addEventListener('click', () => {
      initAudio();
      
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      // Hide start screen overlay
      document.getElementById('start-screen').classList.add('hidden');
      document.getElementById('hud').classList.remove('hidden');
      
      const tip = document.getElementById('controls-tip');
      tip.classList.remove('hidden');
      if (STATE.mouseEnabled) {
        tip.innerText = "MOVE CURSOR TO STEER SHIP";
      } else {
        tip.innerText = "USE A / D OR ← / → TO DODGE";
      }

      // Setup safety visuals immediately
      if (STATE.isVibeModeSafe) {
        STATE.safetyBadgeEl.classList.add('active');
        if (scene) {
          scene.background.setHex(0x05031a);
          scene.fog.color.setHex(0x05031a);
        }
        if (composer && composer.passes[1]) {
          composer.passes[1].strength = 0.6;
        }
      } else {
        STATE.safetyBadgeEl.classList.remove('active');
        if (scene) {
          scene.background.setHex(0x0f001e);
          scene.fog.color.setHex(0x0f001e);
        }
        if (composer && composer.passes[1]) {
          composer.passes[1].strength = 1.8;
        }
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
      
      const tip = document.getElementById('controls-tip');
      tip.classList.remove('hidden');

      resetGameState();

      STATE.isGameRunning = true;
      animate();
      startSynthSequencer();
    });

    document.getElementById('btn-reload').addEventListener('click', () => {
      window.location.reload();
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
