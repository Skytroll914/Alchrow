# Alchrow [WARNING: Game still has a bit of bug, do expect some runtime error]
A simple game created using PyGames 

Instructions:
- Please make sure the python game file and the 2 assets files are within the same directory
- Open code in IDE and run from there if there are trouble launching it (immediately close upon executing it)

## 🎮 How to Play (Might have some missing info. Soon to be updated to ensure all info are present and accurate)

- Two players battle on the same screen using **elemental arrows**: 🔥 Fire, 💧 Water, 🌪️ Air, 🪨 Earth.
- Each player has:
  - A **character** to move
  - A **barrier** to protect their side
  - A **mana pool** to cast abilities
  - A **health bar** (starts at 100 HP)

### 🎯 Objective
- **Break the opponent’s barrier** and reduce their **health to 0** using elemental attacks.
- First player to bring the opponent's HP to 0 **wins the match**.

## ⚔️ Controls

### Player 1 (Left Side)
- `J` / `K`: Move Up / Down
- `W` + `H`: Shoot Water (Air) arrow — fast, light damage
- `S` + `H`: Shoot Earth arrow — slow, heavy damage, stuns longer
- `A` + `H`: Shoot Water (Side) arrow — moderate damage, quick
- `D` + `H`: Shoot Fire arrow — high character damage

### Player 2 (Right Side)
- `N` / `M`: Move Up / Down
- `↑` + `B`: Shoot Water (Air) arrow
- `↓` + `B`: Shoot Earth arrow
- `←` + `B`: Shoot Water (Side) arrow
- `→` + `B`: Shoot Fire arrow

> 💡 Each arrow consumes mana. Mana regenerates over time.

## 💥 Elements & Effects

- **Air (Up)**: Fastest projectile, weak but hard to dodge.
- **Earth (Down)**: Strong vs barrier, causes longer stun, uses more mana.
- **Water (Left/Side)**: Balanced; medium damage, medium stun.
- **Fire (Right)**: High character damage, ideal for finishing.

## 🧠 Features

- Turn-based projectile animations with unique effects
- Barrier collision & health tracking
- Stun mechanic (players temporarily disabled on hit)
- Visual health and mana indicators
- Sprite-based animation with elemental themes
