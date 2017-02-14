#!/usr/bin/env python

# Cross-compatibility between python versions 2 and 3.
from __future__ import print_function

# Import drawint library.
import sfml as sf

# Shortcuts.
from sfml import Rectangle as Rect
from sfml import Vector2 as Pos
from sfml import Event
from sfml import Keyboard as Key

# Settings.
BORDER = 4

if __name__ == '__main__':
	# Create drawing window.
	win = sf.RenderWindow(sf.VideoMode(640, 480), 'Space Invaders')
	
	# Initialization.
	
	# Mega texture with all sprites.
	t0 = sf.Texture.from_file('invaders.jpg')

	# Ship sprite.
	s0 = sf.Sprite(t0)
	s0_w = 38+2*BORDER
	s0.texture_rectangle = Rect((121-BORDER, 25-BORDER), (s0_w, 23+2*BORDER))
	s0.position = Pos(270, 350)
	

	# Game loop.
	while True:
		# Break if window closed.
		if not win.is_open:
			break
		
		# Input.

		for event in win.events:
			if type(event) is sf.CloseEvent:
				win.close()
		
		# Shooting.
		# Move.
		# Animations.
		# Explosions.
		# Remove.
		
		# Draw.
		win.clear()
		
		win.draw(s0)
		
		win.display()
		
		# Sleep a little.
		sf.sleep(sf.milliseconds(5))
