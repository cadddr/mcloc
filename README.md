### mcloc for Monte Carlo localization

Basically, an exercise of visualizing one of my favorite algorithms in Processing. 

See for an introduction: https://en.wikipedia.org/wiki/Monte_Carlo_localization

<img src="https://raw.github.com/cadddr/mcloc/master/gif/1.gif" width="238" /> 
<img src="https://raw.github.com/cadddr/mcloc/master/gif/2.gif" width="238" /> 
<img src="https://raw.github.com/cadddr/mcloc/master/gif/3.gif" width="238" />

(obstacles/landmarks are too dark/small to see in the above animations but they give a gist)

### On Model Correctness
Please note that model is not yet completely correct but it does already show some interesting visuals.

### Installation
The code requires 
- Processing 2+ https://processing.org/ with the 
- Processing.py's Python mode installed https://github.com/jdf/processing.py to run.

(I believe, the extension of the main file 'mcloc.py' will need to be changed to '.pyde' for it to open in the Processing IDE)

OR

Just use Processing.py's .sh (or .bat) as a "custom Python interpreter" for any other IDE. 

PyCharm required some tinkering, though. It wouldn't allow to just add it saying it didn't look like a legit Python SDK. So I had to put Processing.py's directory alongside the normal Python interpreter:

in /Library/Frameworks/Python.framework/Versions/<here> on Mac 

AND create a symbolik link for the .sh with the name 'python' and then point PyCharm to that symlink. 
It first showed some warning about an unknown/invalid interpreter but they went away and it "compiled". (Although with a Processing.py splashscreen, which I personally find less annoying than having to use Processing's native IDE.) 

I also tried linking the executable inside the processing-py app but it just got ugly -- with uncontrolled spawning of JVMs even without me having to hit 'run' in PyCharm so the above seems more decent.

### Running
Just run the 'mcloc' file in Processing or as I described -- it will initialize and start the update loop. 

### Representation
It's a 2D grid world, which is a sort of fusion between the actual world geometry and agent's belief about their location. Each cell is shaded proportionally to the probability of the agent being there such that lighter colors indicate higher likelihood. Obstacles are shaded as completely black (zero likelihood). 

### Keyboard Controls
The idea was to give a lot of flexibility to experimentat with model parameters (e.g. sensor noise) and some visual aspects too.

So far supported:
- R toggles the random walk.
- M toggles the highlight of the agent's actual position.
- H slightly highlights the obstacles.
- G toggles the grid outline (purely visual purpose).

More to come (i.e. the promised sensor noise).
