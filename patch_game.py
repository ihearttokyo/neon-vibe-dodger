import os

target_path = "generate_index.py"
with open(target_path, "r") as f:
    content = f.read()

replacements = [
    # 1. Stylesheet (Keyboard focus style)
    (
        """.btn-cyber:active {
      transform: scale(0.98);
    }""",
        """.btn-cyber:active {
      transform: scale(0.98);
    }

    /* Keyboard focus glow outlines */
    .keyboard-focused, :focus-visible {
      outline: 3px solid var(--green) !important;
      box-shadow: 0 0 35px var(--green) !important;
      transform: scale(1.04) !important;
    }

    .switch:has(input.keyboard-focused), .switch:has(input:focus-visible) {
      outline: 3px solid var(--green) !important;
      box-shadow: 0 0 35px var(--green) !important;
      border-radius: 20px;
    }"""
    ),
    
    # 2. Audio element insertion
    (
        """<body>

  <canvas id="game-canvas"></canvas>""",
        """<body>
  <!-- Classic Warez Chiptune Music Stream -->
  <audio id="chiptune-music" loop crossorigin="anonymous" src="https://archive.org/download/essential-keygen-music/01%20-%20rez%2Bkenet%20-%20unreeeal%20superhero%203.mp3"></audio>

  <canvas id="game-canvas"></canvas>"""
    ),

    # 3. Start Screen Credit footer
    (
        """      <button id="btn-start" class="btn-cyber">Start Engine</button>
    </div>
  </div>

  <!-- Level Upgrade Bay Screen -->""",
        """      <button id="btn-start" class="btn-cyber">Start Engine</button>
      <div style="font-size: 0.8rem; color: rgba(255,255,255,0.45); margin-top: 18px; font-family: 'Share Tech Mono', monospace; text-shadow: 0 0 5px rgba(255,255,255,0.1); text-align: center;">
        Music: "Unreeeal Superhero 3" by Kenët & Rez (CC-BY)
      </div>
    </div>
  </div>

  <!-- Level Upgrade Bay Screen -->"""
    ),

    # 4. Upgrade Screen Credit footer
    (
        """      <button id="btn-next-level" class="btn-cyber" style="background: linear-gradient(135deg, var(--green) 0%, var(--cyan) 100%); box-shadow: 0 0 25px rgba(57, 255, 20, 0.4);">Engage Hyperdrive</button>
    </div>
  </div>

  <!-- Game Over Screen -->""",
        """      <button id="btn-next-level" class="btn-cyber" style="background: linear-gradient(135deg, var(--green) 0%, var(--cyan) 100%); box-shadow: 0 0 25px rgba(57, 255, 20, 0.4);">Engage Hyperdrive</button>
      <div style="font-size: 0.8rem; color: rgba(255,255,255,0.45); margin-top: 18px; font-family: 'Share Tech Mono', monospace; text-shadow: 0 0 5px rgba(255,255,255,0.1); text-align: center;">
        Music: "Unreeeal Superhero 3" by Kenët & Rez (CC-BY)
      </div>
    </div>
  </div>

  <!-- Game Over Screen -->"""
    ),

    # 5. Player Core material
    (
        """      // Diamond core mesh
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
      });""",
        """      // Diamond core mesh (Premium solid flat-shaded Phong material)
      const coreGeom = new THREE.OctahedronGeometry(1.2, 0);
      const coreMat = new THREE.MeshPhongMaterial({
        color: 0x00f0ff,
        emissive: 0x00557f,
        emissiveIntensity: 0.85,
        flatShading: true,
        shininess: 100,
        transparent: false
      });
      const coreMesh = new THREE.Mesh(coreGeom, coreMat);
      playerGroup.add(coreMesh);

      // Outer bounding glowing structural lines (Enhanced opacity glow border)
      const outlineGeom = new THREE.OctahedronGeometry(1.4, 0);
      const outlineMat = new THREE.MeshBasicMaterial({
        color: 0xff007f,
        transparent: true,
        opacity: 0.6,
        blending: THREE.AdditiveBlending
      });"""
    ),

    # 6. Obstacle material
    (
        """        const mat = new THREE.MeshBasicMaterial({
          color: color,
          wireframe: true,
          transparent: true,
          opacity: 0.8
        });""",
        """        // Solid high-legibility flat-shaded Phong material with self-illumination
        const mat = new THREE.MeshPhongMaterial({
          color: color,
          emissive: color,
          emissiveIntensity: 0.55,
          flatShading: true,
          shininess: 40,
          transparent: false
        });"""
    ),

    # 7. Collectible material
    (
        """      mat = new THREE.MeshBasicMaterial({
        color: color,
        wireframe: true,
        transparent: true,
        opacity: 0.95
      });""",
        """      // Solid high-legibility flat-shaded Phong material with glossy highlights
      mat = new THREE.MeshPhongMaterial({
        color: color,
        emissive: color,
        emissiveIntensity: 0.65,
        flatShading: true,
        shininess: 80,
        transparent: false
      });"""
    ),

    # 8. Smooth wrapping + pointLight follow player + endless spiral logic
    (
        """      // Smooth interpolation filter of banking angles
      STATE.playerAngle += (STATE.playerAngleTarget - STATE.playerAngle) * 0.15 * frameDelta;
      
      // Lock target limits
      STATE.playerAngle = THREE.MathUtils.clamp(STATE.playerAngle, -Math.PI * 0.95, Math.PI * 0.95);

      // Rotate player ship group relative to tunnel lane angle
      playerGroup.position.x = Math.sin(STATE.playerAngle) * (TUNNEL_RADIUS - 0.7);
      playerGroup.position.y = -Math.cos(STATE.playerAngle) * (TUNNEL_RADIUS - 0.7);
      
      // Auto-align banking tilt angle matching steer velocity
      const shipBankAngle = (STATE.playerAngle - STATE.playerAngleTarget) * 0.45;
      playerGroup.rotation.set(0, 0, STATE.playerAngle - shipBankAngle);""",
        """      // Smooth interpolation filter of banking angles
      STATE.playerAngle += (STATE.playerAngleTarget - STATE.playerAngle) * 0.15 * frameDelta;
      
      // Endless 360-degree spiral rotation wrapping logic (no hard boundaries)
      if (STATE.playerAngleTarget > Math.PI) {
        STATE.playerAngleTarget -= Math.PI * 2;
        STATE.playerAngle -= Math.PI * 2;
      } else if (STATE.playerAngleTarget < -Math.PI) {
        STATE.playerAngleTarget += Math.PI * 2;
        STATE.playerAngle += Math.PI * 2;
      }

      // Rotate player ship group relative to tunnel lane angle
      playerGroup.position.x = Math.sin(STATE.playerAngle) * (TUNNEL_RADIUS - 0.7);
      playerGroup.position.y = -Math.cos(STATE.playerAngle) * (TUNNEL_RADIUS - 0.7);

      // Move pointLight dynamically to follow the player vessel for premium glossy reflections
      if (pointLight) {
        pointLight.position.x = playerGroup.position.x;
        pointLight.position.y = playerGroup.position.y;
        pointLight.position.z = playerGroup.position.z - 5;
      }
      
      // Auto-align banking tilt angle matching steer velocity
      const shipBankAngle = (STATE.playerAngle - STATE.playerAngleTarget) * 0.45;
      playerGroup.rotation.set(0, 0, STATE.playerAngle - shipBankAngle);"""
    ),

    # 9. Projectile vs Obstacle true 3D Euclidean distance collision
    (
        """        // Collision Check: Projectile vs Obstacle
        for (let j = STATE.projectiles.length - 1; j >= 0; j--) {
          const proj = STATE.projectiles[j];
          const distZ = Math.abs(obs.mesh.position.z - proj.mesh.position.z);
          
          if (distZ < 10) {
            // Lane mapping collision vector checks
            const obsAngle = obs.lane * LANE_ANGLE_STEP;
            const projAngle = proj.angle;
            const diffAngle = Math.abs(Math.atan2(Math.sin(obsAngle - projAngle), Math.cos(obsAngle - projAngle)));

            if (diffAngle < 0.5) {""",
        """        // Collision Check: Projectile vs Obstacle (True 3D Euclidean Distance check)
        for (let j = STATE.projectiles.length - 1; j >= 0; j--) {
          const proj = STATE.projectiles[j];
          const dx = obs.mesh.position.x - proj.mesh.position.x;
          const dy = obs.mesh.position.y - proj.mesh.position.y;
          const dz = obs.mesh.position.z - proj.mesh.position.z;
          const dist = Math.sqrt(dx*dx + dy*dy + dz*dz);
          
          if (dist < 3.2) {"""
    ),

    # 10. Obstacle vs Player Vessel true 3D Euclidean distance collision
    (
        """        // Collision Check: Obstacle vs Player Vessel
        const distZ = Math.abs(obs.mesh.position.z - playerGroup.position.z);
        if (distZ < 2.2) {
          const obsAngle = obs.lane * LANE_ANGLE_STEP;
          const diffAngle = Math.abs(Math.atan2(Math.sin(obsAngle - STATE.playerAngle), Math.cos(obsAngle - STATE.playerAngle)));

          if (diffAngle < 0.6) {""",
        """        // Collision Check: Obstacle vs Player Vessel (True 3D Euclidean Distance check)
        const dx_player = obs.mesh.position.x - playerGroup.position.x;
        const dy_player = obs.mesh.position.y - playerGroup.position.y;
        const dz_player = obs.mesh.position.z - playerGroup.position.z;
        const dist_player = Math.sqrt(dx_player*dx_player + dy_player*dy_player + dz_player*dz_player);
        
        if (dist_player < 2.8) {"""
    ),

    # 11. Near Miss Check true 3D Euclidean distance check
    (
        """        // Near miss verification checks (Double Gate boundaries, Edge Case 8)
        if (distZ < 4.0 && obs.mesh.position.z < playerGroup.position.z) {
          const obsAngle = obs.lane * LANE_ANGLE_STEP;
          const diffAngle = Math.abs(Math.atan2(Math.sin(obsAngle - STATE.playerAngle), Math.cos(obsAngle - STATE.playerAngle)));

          if (!obs.nearMissTriggered && diffAngle < 0.65) {""",
        """        // Near miss verification checks (True 3D Euclidean Distance check)
        if (!obs.nearMissTriggered && obs.mesh.position.z < playerGroup.position.z) {
          const dx_player = obs.mesh.position.x - playerGroup.position.x;
          const dy_player = obs.mesh.position.y - playerGroup.position.y;
          const dz_player = obs.mesh.position.z - playerGroup.position.z;
          const dist_player = Math.sqrt(dx_player*dx_player + dy_player*dy_player + dz_player*dz_player);

          if (dist_player < 5.2) {"""
    ),

    # 12. Item vs Player true 3D Euclidean distance check
    (
        """        // Collision Check: Item vs Player Vessel
        const distZ = Math.abs(item.mesh.position.z - playerGroup.position.z);
        if (distZ < 2.5) {
          const itemAngle = item.lane * LANE_ANGLE_STEP;
          const diffAngle = Math.abs(Math.atan2(Math.sin(itemAngle - STATE.playerAngle), Math.cos(itemAngle - STATE.playerAngle)));

          if (diffAngle < 0.7 || STATE.isMagnetActive) {""",
        """        // Collision Check: Item vs Player Vessel (True 3D Euclidean Distance check)
        const dx_item = item.mesh.position.x - playerGroup.position.x;
        const dy_item = item.mesh.position.y - playerGroup.position.y;
        const dz_item = item.mesh.position.z - playerGroup.position.z;
        const dist_item = Math.sqrt(dx_item*dx_item + dy_item*dy_item + dz_item*dz_item);
        const collectionRadius = STATE.isMagnetActive ? 6.0 : 2.6;

          if (dist_item < collectionRadius) {"""
    ),

    # 13. Pause Screen Resume & BGM Controls
    (
        """      const pauseScreen = document.getElementById('pause-screen');
      if (STATE.isGameRunning) {
        // Pause Game
        STATE.isGameRunning = false;
        if (animationFrameId) cancelAnimationFrame(animationFrameId);
        if (sequencerTimer) clearTimeout(sequencerTimer);
        pauseGame();
        pauseScreen.classList.remove('hidden');
        if (document.pointerLockElement === canvas) {
          document.exitPointerLock();
        }
      } else {
        // Resume Game
        pauseScreen.classList.add('hidden');
        if (STATE.mouseEnabled) {
          canvas.requestPointerLock();
        }
        resumeGame();
        clock.getDelta(); // Clear delta accumulator
        STATE.isGameRunning = true;
        animate();
        startSynthSequencer();
      }""",
        """      const pauseScreen = document.getElementById('pause-screen');
      if (STATE.isGameRunning) {
        // Pause Game
        STATE.isGameRunning = false;
        if (animationFrameId) cancelAnimationFrame(animationFrameId);
        if (sequencerTimer) clearTimeout(sequencerTimer);
        pauseGame();
        pauseBGM();
        pauseScreen.classList.remove('hidden');
        resetMenuFocus();
        if (document.pointerLockElement === canvas) {
          document.exitPointerLock();
        }
      } else {
        // Resume Game
        pauseScreen.classList.add('hidden');
        if (STATE.mouseEnabled) {
          canvas.requestPointerLock();
        }
        resumeGame();
        playBGM();
        clock.getDelta(); // Clear delta accumulator
        STATE.isGameRunning = true;
        animate();
        startSynthSequencer();
      }"""
    ),

    # 14. Level Clear BGM pause & reset focus
    (
        """    function triggerLevelClear() {
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
    }""",
        """    function triggerLevelClear() {
      STATE.isGameRunning = false;
      cancelAnimationFrame(animationFrameId);
      if (sequencerTimer) clearTimeout(sequencerTimer);
      pauseGame();
      pauseBGM();

      // Display Upgrade Bay Overlay
      document.getElementById('hud').classList.add('hidden');
      document.getElementById('keyboard-dashboard').classList.add('hidden');
      
      document.getElementById('upgrade-shards').innerText = STATE.neonShardsCount;
      document.getElementById('upgrade-screen').classList.remove('hidden');

      // Update shop buy buttons states
      updateShopButtons();
      resetMenuFocus();
    }"""
    ),

    # 15. Game Over BGM pause & reset focus
    (
        """      playSoundFX('crash');

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
      document.getElementById('game-over-screen').classList.remove('hidden');""",
        """      playSoundFX('crash');

      // Stop audio scheduler loops
      pauseGame();
      pauseBGM();

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
      resetMenuFocus();"""
    ),

    # 16. Engage Hyperdrive BGM play
    (
        """    document.getElementById('btn-next-level').addEventListener('click', () => {
      document.getElementById('upgrade-screen').classList.add('hidden');
      
      // Advance variables
      STATE.currentLevel++;
      document.getElementById('level-title').innerText = `Level ${STATE.currentLevel}`;
      
      // Decrement spawns checks for faster pace (hyper-arcade aggressive progression down to 12 frames)""",
        """    document.getElementById('btn-next-level').addEventListener('click', () => {
      document.getElementById('upgrade-screen').classList.add('hidden');
      
      // Advance variables
      STATE.currentLevel++;
      document.getElementById('level-title').innerText = `Level ${STATE.currentLevel}`;
      
      playBGM();
      
      // Decrement spawns checks for faster pace (hyper-arcade aggressive progression down to 12 frames)"""
    ),

    # 17. Keyboard start engine BGM play + toggle mouse + toggle audio
    (
        """    // Connect Button Gestures
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
    });""",
        """    // Connect Button Gestures
    document.getElementById('btn-start').addEventListener('click', () => {
      initAudio();
      
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      STATE.mouseEnabled = document.getElementById('toggle-mouse').checked;
      STATE.audioEnabled = document.getElementById('toggle-audio').checked;
      playBGM();

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

      playBGM();

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
    });"""
    ),

    # 18. Keyboard menu intercepts & music controllers insertion
    (
        """    // ----------------------------------------------------
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
      if (key === 'p' || e.key === 'Escape') {
        e.preventDefault();
        togglePause();
      }
    });""",
        """    // ----------------------------------------------------
    // KEYBOARD MENU NAVIGATION SYSTEM & WAREZ BGM AUDIO
    // ----------------------------------------------------
    let menuFocusIndex = 0;
    let isBgmPlaying = false;

    function getNavigableElements() {
      const screens = [
        { id: 'start-screen', selectors: ['#toggle-mouse', '#toggle-audio', '#btn-start'] },
        { id: 'upgrade-screen', selectors: ['#buy-shield', '#buy-ammo', '#buy-boost', '#buy-blaster', '#btn-next-level'] },
        { id: 'game-over-screen', selectors: ['#btn-restart'] },
        { id: 'pause-screen', selectors: ['#btn-resume'] }
      ];
      for (const s of screens) {
        const el = document.getElementById(s.id);
        if (el && !el.classList.contains('hidden')) {
          return s.selectors.map(sel => el.querySelector(sel)).filter(Boolean);
        }
      }
      return [];
    }

    function updateMenuFocusVisuals(elements) {
      document.querySelectorAll('.keyboard-focused').forEach(el => {
        el.classList.remove('keyboard-focused');
        el.blur();
      });
      if (elements.length > 0) {
        if (menuFocusIndex < 0) menuFocusIndex = elements.length - 1;
        if (menuFocusIndex >= elements.length) menuFocusIndex = 0;
        const target = elements[menuFocusIndex];
        if (target) {
          target.classList.add('keyboard-focused');
          target.focus();
        }
      }
    }

    function resetMenuFocus() {
      const elements = getNavigableElements();
      menuFocusIndex = elements.findIndex(el => el.tagName === 'BUTTON');
      if (menuFocusIndex < 0) menuFocusIndex = 0;
      updateMenuFocusVisuals(elements);
    }

    function isAnyMenuOpen() {
      const ids = ['start-screen', 'upgrade-screen', 'game-over-screen', 'pause-screen'];
      return ids.some(id => {
        const el = document.getElementById(id);
        return el && !el.classList.contains('hidden');
      });
    }

    function playBGM() {
      const bgm = document.getElementById('chiptune-music');
      const audioToggle = document.getElementById('toggle-audio');
      const audioEnabled = audioToggle ? audioToggle.checked : true;
      if (!bgm || !audioEnabled) {
        if (bgm) bgm.pause();
        isBgmPlaying = false;
        return;
      }
      bgm.volume = 0.45;
      bgm.play()
        .then(() => {
          isBgmPlaying = true;
        })
        .catch(err => {
          console.warn("Chiptune BGM failed to play, falling back to procedural synthesizer:", err);
          isBgmPlaying = false;
        });
    }

    function pauseBGM() {
      const bgm = document.getElementById('chiptune-music');
      if (bgm) bgm.pause();
    }

    // Add DOM event listeners for toggles
    document.getElementById('toggle-audio').addEventListener('change', (e) => {
      STATE.audioEnabled = e.target.checked;
      if (STATE.audioEnabled) {
        initAudio();
        if (audioCtx && audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
        playBGM();
      } else {
        pauseBGM();
      }
    });

    document.getElementById('toggle-mouse').addEventListener('change', (e) => {
      STATE.mouseEnabled = e.target.checked;
      if (STATE.isGameRunning) {
        if (STATE.mouseEnabled) {
          canvas.requestPointerLock();
        } else {
          document.exitPointerLock();
        }
      }
    });

    // ----------------------------------------------------
    // INPUT HANDLERS & MOUSE RELATIVE SHIFTS
    // ----------------------------------------------------
    window.addEventListener('keydown', (e) => {
      const key = e.key.toLowerCase();
      
      // Keyboard menu navigation intercept
      if (isAnyMenuOpen()) {
        const elements = getNavigableElements();
        if (elements.length > 0) {
          if (key === 'arrowdown' || key === 's' || key === 'arrowright' || key === 'd') {
            e.preventDefault();
            menuFocusIndex++;
            updateMenuFocusVisuals(elements);
            playSoundFX('nearmiss');
            return;
          }
          if (key === 'arrowup' || key === 'w' || key === 'arrowleft' || key === 'a') {
            e.preventDefault();
            menuFocusIndex--;
            updateMenuFocusVisuals(elements);
            playSoundFX('nearmiss');
            return;
          }
          if (key === 'enter' || key === ' ') {
            e.preventDefault();
            const target = elements[menuFocusIndex];
            if (target) {
              if (target.tagName === 'INPUT' && target.type === 'checkbox') {
                target.checked = !target.checked;
                target.dispatchEvent(new Event('change'));
                playSoundFX('upgrade');
              } else {
                target.click();
              }
            }
            return;
          }
        }
      }

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
      if (key === 'p' || e.key === 'Escape') {
        e.preventDefault();
        togglePause();
      }
    });"""
    ),

    # 19. Window load resetMenuFocus trigger
    (
        """    // Boot Graphics Framework immediately on load
    window.addEventListener('load', () => {
      initThree();
    });""",
        """    // Boot Graphics Framework immediately on load
    window.addEventListener('load', () => {
      initThree();
      resetMenuFocus();
    });"""
    ),

    # 20. Procedural sound arpeggiator / kick skips
    # Part 20.1 Kick skips
    (
        """        // 1. Kick Drum Synthesizer (Standard beats)
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

          // Audio reactive vector pulsing logic synced to the kick drum""",
        """        // 1. Kick Drum Synthesizer (Standard beats)
        if (beat % 2 === 0) {
          if (!isBgmPlaying) {
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
          }

          // Audio reactive vector pulsing logic synced to the kick drum"""
    ),

    # Part 20.2 Bass skips
    (
        """        // 2. Synthesized detuned synth bass pattern (Fat 80s Arpeggio in A minor)
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
        }""",
        """        // 2. Synthesized detuned synth bass pattern (Fat 80s Arpeggio in A minor)
        const notes = [55, 55, 65, 55, 58, 58, 65, 58]; // MIDI-style frequencies index
        const midiNote = notes[beat % notes.length];
        const freq = Math.pow(2, (midiNote - 69) / 12) * 440;

        if (!isBgmPlaying) {
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
        }"""
    )
]

print("Applying patches...")
patched_count = 0
for i, (search_str, replace_str) in enumerate(replacements):
    if search_str in content:
        content = content.replace(search_str, replace_str)
        print(f"  [{i+1}/{len(replacements)}] Applied replacement successfully!")
        patched_count += 1
    else:
        print(f"  [{i+1}/{len(replacements)}] WARNING: Target string not found!")

if patched_count == len(replacements):
    print("SUCCESS: All patches successfully applied!")
else:
    print(f"WARNING: Only {patched_count} of {len(replacements)} patches were applied.")

with open(target_path, "w") as f:
    f.write(content)

