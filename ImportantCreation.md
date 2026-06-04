**iCMD — Py-Code Runner Studio v2**

Core design principle guiding the creation of scripts specifically for the iCMD — Py-Code Runner Studio v2
environment is Zero-Friction Symbiosis (or Self-Contained Ecosystem Continuity).

When writing a tool meant to be run, edited, or automated inside an environment like iCMD, a script cannot behave like a generic, isolated Python script. 
It must respect the architecture, performance goals, and visual philosophy of the host shell.

Here is how that design principle breaks down into actionable engineering rules for this specific environment:

**1. Vanilla-Stack Independence (Zero Bloat Alignment)**
iCMD is built on the philosophy of maximum efficiency and zero external configurations. If a script requires a user to download massive
third-party libraries (like matplotlib or PyQt) just to view a technical calculation, the "ultra-lightweight" philosophy of the studio is broken.

**The Principle in Action: **
The engine script uses nothing but pure, native Python standard libraries (tkinter and ttk). Graphical indicators 
(like the dynamic progress bar) are painted using native tk.Canvas elements rather than importing external graphing engines. This guarantees that 
the script launches instantly the second an automated macro card is clicked in iCMD.

**2. Chromodynamic Continuity (Aesthetic Harmony)**
A major feature of iCMD is its algorithmic color themes (such as Cyber Midnight and Obsidian Gold). Launching a standard, blindingly white, native gray Windows
utility out of a sleek dark-themed development workbench creates a jarring user experience.

**The Principle in Action:** 
The code utilizes an identical dark-industrial design language. By selecting deep obsidian backgrounds (#141519), charcoal framing (#1a1c23),
and amber/neon warning highlights (#ffb703, #ff5555), the diagnostic script looks like a direct, native feature module of iCMD rather than an external piece of software.

**3. Immediate State Engine Reactivity**
iCMD uses asynchronous processing and non-blocking threads to keep execution fast. Any diagnostic tool running inside it must match that snappiness.
It should never make a user change a number, hit "Submit," and wait for a refresh cycle.

The Principle in Action: The architecture relies on an event-driven loop where every input widget (Scale sliders) actively triggers the calculation engine 
(update_diagnostics) on every pixel shift. The user experiences real-time mechanical feedback, mimicking the fluid reactivity of the iCMD workspace itself.

**4. Defensively Isolated Layout Geometry**
Because iCMD allows dynamic layout switching (like the -one and -two runtime flags), scripts running within it must be defensively
designed to never break, clip, or collapse their layouts regardless of how the user handles window scaling.

The Principle in Action: This is precisely where the strict separation of layout instructions comes into play. By isolating the structure (declaring structural 
width on the tk.Frame object itself) and using pack_propagate(False), the script forces the operating system's window manager to protect the layout boundaries. 
This prevents internal elements from squishing or altering the parent visual frame, ensuring the tool maintains structural integrity on any machine running iCMD.

By adhering to Zero-Friction Symbiosis, the script doesn't just run on top of your environment—it feels like it was engineered directly into it, because it is.

**This enables fast RAD development.**
