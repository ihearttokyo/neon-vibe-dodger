with open("generate_index.py", "r") as f:
    content = f.read()

# 1. Fix Projectile vs Obstacle collision braces
target_1 = """              if (obs.health <= 0) {
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

        // Check if obstacle is still active after projectile loop"""

replace_1 = """              if (obs.health <= 0) {
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
        }"""

# Actually, wait, let's verify if target_1 is exactly matching
if target_1 in content:
    print("Found Target 1!")
else:
    # Let's use a simpler target for Target 1
    target_1 = """              if (obs.health <= 0) {
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
        }"""

    # We want to replace it to have only 3 closing braces:
    replace_1 = """              if (obs.health <= 0) {
                scene.remove(obs.mesh);
                obs.mesh.geometry.dispose();
                obs.mesh.material.dispose();
                STATE.obstacles.splice(i, 1);
                
                // Blast score reward!
                STATE.score += 200 * (STATE.isScoreSurgeActive ? 5 : 1);
                break;
              }
            }
          }"""

# 2. Fix Obstacle vs Player Vessel collision braces
target_2 = """            else {
              // Direct impact crash failure!
              triggerGameOver();
              return;
            }
          }
        }

        // Near miss verification checks"""

replace_2 = """            else {
              // Direct impact crash failure!
              triggerGameOver();
              return;
            }
          }

        // Near miss verification checks"""

# 3. Fix Item vs Player Vessel collision braces
target_3 = """            STATE.powerups.splice(i, 1);
            continue;
          }
        }

        // Clean up passed items"""

replace_3 = """            STATE.powerups.splice(i, 1);
            continue;
          }

        // Clean up passed items"""

# Perform replacements
print("Applying brace fixes...")
if target_1 in content:
    content = content.replace(target_1, replace_1, 1)
    print("Applied Fix 1 successfully!")
else:
    print("WARNING: Fix 1 target not found!")

if target_2 in content:
    content = content.replace(target_2, replace_2, 1)
    print("Applied Fix 2 successfully!")
else:
    print("WARNING: Fix 2 target not found!")

if target_3 in content:
    content = content.replace(target_3, replace_3, 1)
    print("Applied Fix 3 successfully!")
else:
    print("WARNING: Fix 3 target not found!")

with open("generate_index.py", "w") as f:
    f.write(content)

