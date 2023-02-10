## The Humble Raycaster

### Revisting the Past: The Horrors of Java

Learning to program in highschool
Making games in simple 2d Java 
Move on to 3d games
Raycasting are some of the simplest 3d graphics techniques

Doom + Wolfenstein

Had not played them myself.
Demons and fascists are probably too scary for children anyways.

Principles of raycasting
Draw diagram on ipad

Having made all of my other games with Java swing, I saw no reason to learn anything new.
I drew each pixel to the screen with a separate call to `drawImage`, making the framerate painfully slow.
My original raycaster along with all of my other little Java applets were lost to the sands of time.

### Redesigning in the Present: Reimplementation in C

A few summers ago, I decided to revisit the raycaster as a weekend project with a few more years of experience with 3d graphics.
GLFW for window management. 
Could be as simple as writing pixel array to the screen, but I wanted to do some experiments with opengl.
Experiment with pixel buffer. Inconclusive if it was actually faster.
Experiment with shaders over top.

I decided to add a few more features, variable floor and ceiling heights, looking up and down.
Keep a history of the floor and ceiling heights for each cell encountered by the ray.

### Running into the Future: Experiments with WebAssembly + Emscripten

Sadly, Java applets like Flash have been deprecated, a decisive victory for people annoyed by web pages asking them to enable these plugins.
Ultimately, the myriad of security issues posed by these technologies were not worth fixing.
As mentioned in my other post on WebAssembly [here](/test_problem.html), I like the idea of apps that can run locally on your machine without intercation with a server.
I think there is a need for a secure and cross-platform way to distribute these applications.
It seems for now, the best way to do this is making static web apps to run in a browser (many people carry devices with browsers in their pockets).
While JavaScript is a great tool for running programs in the browser (arguably the only tool for a long time), not everyone
wants to be a Javascript developer. 
Wasm is new bytecode adopted by the major browsers.
There are wasm compilers for many languages.
In particular [emscripten](https://emscripten.org/) supports any LLVM supported language, including C, C++, and most typically Rust.
Importantly, emscripten provides bindings for WebGL, enabling building graphical apps and games.


I built my raycaster using emscripten.
Common error is seeing a black screen -> difficult to debug
Image of emscripten black screen.
Fails silently.
Webgl is a version of OpenGL Es 2.
No support for pixel buffers.
Browser is a good debugging tool, actually fixed a lot of bugs, removed deprecated code from the project.
After a few hours, I got it to work.
You can play with it below.

You can find the source on Github here:
[https://github.com/arw12625/Rayngler](https://github.com/arw12625/Rayngler)
It has tools for building as an executable or as a web app with emscripten.

<iframe src="/raycaster_embed.html" title="description" frameBorder="0" scrolling="no" width="800" height="600"></iframe>

Wasm was designed with security in mind.
Will it have the same fate as applets and Flash?
Only time will tell.
I wonder how long until this app stops working.
I guess I'll have to revisit the raycaster again when that happens.