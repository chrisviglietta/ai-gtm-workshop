---
name: living-storybook
description: Animate new sheets of Chris's watercolor storybook illustrations into looping clips and add them to the Living Storybook page. Use when the user shares more storybook images or asks to change how existing plates move.
---

# Living Storybook playbook

Turns a sheet of watercolor panels into 7-second looping MP4s. Each frame is the original painting, warped by smooth displacement fields; nothing is repainted. Everything lives in `living-storybook/`:

- `source/animate.py` is the engine (the `Scene` class and its effects).
- `source/scenes.py` holds book 1 (plates I–X), and `source/scenes2.py` holds book 2 (plates XI–XX). Add `scenesN.py` for each new sheet.
- `source/crop_sheet.py`, `source/motionmap.py`, `source/check.py` and `source/zoom.py` are the tools.
- `clips/` holds the output, and `storybook.html` is the published page (artifact `https://claude.ai/artifact/BYBCnFoP1mfcYeUYo3E2GW`).

Setup: `pip install opencv-python-headless`. ffmpeg and numpy are preinstalled. Run every tool from `living-storybook/source/`.

## Process for a new sheet

1. **Crop:** `python3 crop_sheet.py SHEET.webp <next plate number>` writes `pNN.png` and `gridNN.png`.
2. **Read coordinates** from the grid sheets: heads, scarf extent, neck anchor, feet, planets, stars, and every object that should move. For any panel that looks off, `python3 zoom.py NN x0 y0 x1 y1 3 out.png` gives a zoomed grid.
3. **Write the scenes** in a new `scenesN.py`, copying the pattern in `scenes2.py`, and add the names to `NAMES`.
4. **Check placement before rendering:** `python3 motionmap.py scenesN <plates...>` writes `out3/mm_*.jpg`. Red marks where pixels move and blue where glows act. Fix anything that misses its object. This step caught a whole misplaced plate in book 2, so never skip it.
5. **Render:** `python3 scenesN.py ../clips <plates...>`. A clip takes about 80s, and three processes can run in parallel.
6. **Check the result:** `python3 check.py NAME <dir>` reports the loop seam and writes a contact sheet. Read the sheet and zoom into anything suspicious.
7. **Publish:** add `<figure>` entries to `storybook.html` with Roman-numeral folios, then republish the same artifact with the new clips in `files`. Commit and push.

## Motion vocabulary (what the user has liked)

- **Every plate:** scarf ripple (`scarf`), hair sway (`hair`) and breathing (`breathe`). The scarf is Chris's signature, so it always moves.
- **Stars:** `stars()` twinkles, pulses in size and sways left and right. Add a `shooting_star()` once per loop in any plate with sky.
- **Planets Chris stands on:** `planet(cx, cy, r, band)` rocks the disc ±1–2.5°. `band` keeps whatever stands on top still. A continuous spin can't loop seamlessly, so it rocks.
- **Clouds and mist:** `shift` or `drift` them horizontally by 3–6 px. Use `keep_out` so nothing else gets dragged along.
- **Floating things** (rocket, balloon, castle, planets in the sky): `shift` with a soft mask, ±2–3.5 px vertical, plus a small `rotate`.
- **Glowing objects:** `glow()` with an `ellipse(..., p=1)` mask. Never use a box mask, because it shows as a rectangle.
- **Other effects:** smoke uses `billow`, flames use `flicker`, a galaxy uses `galaxy` (it swirls in its own tilted plane), a painted comet uses `comet_sweep`, and heat haze uses `shimmer`.
- **Walking:** the `Walker` class in `scenes.py` uses GrabCut to cut Chris out, inpaints the background and swings the legs as cut-out puppet pieces about the hip. Start the loop with Chris where he was painted, so the first frame isn't empty.
- **Gestures:** a head tilt or lean uses `ease_hold`, and a single gesture that returns uses `bump`.

## Lessons learned (add to this list every batch)

1. **Stars are detected by color and catch other things.** Chris's skin, golden castles, small planets and glowing boxes all pass the star threshold. Pass `only=[(x, y), ...]` with the real star centers whenever anything else golden is nearby, and use `exclude=` for faces.
2. **Saturation differs between sheets.** Book 2's paper and stars are paler. The star threshold now adapts to the paper's median saturation; check `sc.n_stars` after building a scene.
3. **Masks bleed into neighbours.** A cloud mask that overlapped Chris's trousers dragged them along in book 1, plate 10. Subtract the figure with `keep_out`, or `(1 - soft(box))`.
4. **Grid sheets mislead vertically.** Coordinates read from the 5-panel overview were about 25–90 px too high on one plate. Zoom into any plate whose motion map looks wrong.
5. **Rotation sign:** with `rotate()`, a positive angle moves the top of the masked area to the right. The leg swing in `Walker` was reversed on the first try, so check two frames after any new rotation.
6. **Video needs even dimensions.** `load()` crops panels to even width and height for H.264.
7. **Loops:** every motion uses `sin(TAU*k*t/T)` with integer `k`. A one-way motion (the sinking sun) jumps at the seam, so keep it tiny.
8. **Don't add objects** unless the user asks. Petals, leaves and shooting stars were requested. Don't invent new characters.
