# color_seed_demo
 These scripts produce a deterministic color field
 
 That is, it will seed a random.Random instance with a fixed value, and produce a series of 24 bit RGB colored ansi blocks on the terminal, demonstrating the deterministic nature (if so configured/desired) of pseudo random number generators.  This visualization can greatly aid in the understand of procedural generation methods.
 
 Screenshots are included, one from a native Linux terminal, one from PuTTY on Windows, showing the exact same colors.
 The second script produces similar output, but with a procedurally chosen and colored character, as well.
 If you pass an argument to the scripts, it will use this as the random number seed rather than the default, and it will render the same on different machines.

# symbols-24bit
  This script will produce a similar deterministic color field, but with Unicode characters, and double-width fields for visibility.  Random, yet deterministic: background color, foreground color, and Unicode symbol.
  
  As with the color_seed_demo, screenshots are provided, and if you provide an argument, it will use that for the seed value, and produce a repeatable output.  The screenshot is taken at 18-point in Linux, to show some detail of the Unicode symbols.

# cursetangles
  This script will draw deterministic rectangles on a curses terminal screen/window
  using procedural generation so that it will be the same each time, but appear random.
  This script accepts a single optional command line argument as a seed, if desired.
  The location, shape and color of the rectangles is unique per seed.  A short delay
  is in place so the observer can watch the rectangles being drawn.

# proctangles
  This script will draw 60 deterministic rectangles on a tkinter canvas
  using procedural generation so that it will be the same each time,but appear random.
  This script accepts a single optional command line argument as a seed, if desired.
  You will need a graphical DISPLAY or x-forwarded display to permit this script to function.
  Also, the script will pause for a keypress at the end, before the canvas is destroyed.
  A screenshot is included as well, from Linux.
