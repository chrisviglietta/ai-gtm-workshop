# Chris — The Living Watercolor Storybook

10 looping clips (7 s, 24 fps, 876–888×1500 portrait, H.264, no audio) made from the supplied 10-panel watercolor sheet.

Every frame is built from the original painting. Nothing is repainted. Wind ripples move through the scarf and hair, and the body breathes, leans and tilts with small rotations. The stars shimmer, the fox tilts its head, swishes its tail and blinks, the leaves and petals drift, the sand wisps blow and the clouds move.

Regenerate: `cd source && python3 scenes.py ../clips` (needs numpy, opencv-python-headless and ffmpeg).

## Version 2: more movement
- Stars twinkle, pulse in size and sway gently left and right. A shooting star crosses the sky in scenes 1, 2, 7 and 9.
- Planets rock gently on their axis in scenes 1, 2, 7, 8 and 10.
- Clouds drift noticeably in scenes 4 and 10, and the sun sinks a little further.
- Scene 6: Chris is cut out of the painting, so he walks across the dunes with a stepping stride and leaves the frame. The area where he was standing is filled in. He loops back in from the left.
- More falling leaves and drifting petals, a bigger fox-tail swish and wider arm movement on the bridge.

## Book 2 (plates XI–XX)
Plates XI–XX come from the second sheet. Their scene definitions are in `source/scenes2.py`.

They add a galaxy swirling in its own plane, a floating rocket with a flickering flame, factory smoke, robots bobbing and tilting their heads, a swinging claw, glowing boxes and sprouts, floating planets, a floating castle and balloon, drifting clouds, a light pulse running down the painted comet's tail and a shimmering distant city.

To add more sheets, follow the playbook in `.claude/skills/living-storybook/SKILL.md`. It covers the process, the motion vocabulary and the lessons learned, and should be updated after every batch.
