# =========================================================================
#  iCMD STUDIO SHOWCASE: THE SELF-REPLICATING CYBERPUNK MATRIX HUD
#  [Requirements: PURE PYTHON - ZERO PIP INSTALLS / NO EXTERNAL CODE]
# =========================================================================
import tkinter as tk
import math
import random
import os
import shutil
import sys

def replicate_and_initialize():
    """
    SELF-REPRODUCTION ENGINE: 
    Instantly reads its own file track and spawns an independent clone copy 
    directly onto the system directory, demonstrating raw script automation.
    """
    try:
        current_file = os.path.abspath(__file__)
        base_dir = os.path.dirname(current_file)
        clone_path = os.path.join(base_dir, "iCMD_Spawned_Clone.py")
        
        # Guard clause to prevent cyclic overwriting if running the clone
        if not current_file.endswith("iCMD_Spawned_Clone.py"):
            shutil.copy(current_file, clone_path)
            print(f"\n[⚡ iCMD Automation Alert]: Script successfully reproduced itself!")
            print(f" ↳ Spawned independent duplicate asset at:\n   {clone_path}\n")
    except Exception as e:
        print(f"[!] Replication pipe bypassed: {str(e)}")

class CyberpunkHUD:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 iCMD — Standalone Vector Engine")
        self.root.geometry("600x450")
        self.root.configure(bg="#08090e")
        self.root.resizable(False, False)
        
        # Center the standalone viewport seamlessly
        x = (self.root.winfo_screenwidth() // 2) - 300
        y = (self.root.winfo_screenheight() // 2) - 225
        self.root.geometry(f"+{x}+{y}")

        # High-tech HUD Header Frame
        header = tk.Frame(root, bg="#111422", height=35, relief=tk.SOLID, bd=1)
        header.pack(fill=tk.X, padx=10, pady=(10, 0))
        lbl = tk.Label(header, text="SYSTEM STATUS: QUANTUM CORE ACTIVE", bg="#111422", fg="#00f0ff", font=("Consolas", 10, "bold"))
        lbl.pack(pady=6)

        # Main Rendering Canvas (Hardware Accelerated Tkinter native Vector Grid)
        self.canvas = tk.Canvas(root, bg="#0b0d17", highlightthickness=1, highlightbackground="#1f2438")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Generate 3D Data Constellation Points (X, Y, Z coordinates)
        self.nodes = []
        num_nodes = 45
        for _ in range(num_nodes):
            self.nodes.append({
                'x': random.uniform(-120, 120),
                'y': random.uniform(-120, 120),
                'z': random.uniform(-120, 120),
                'color': random.choice(["#00f0ff", "#ff007f", "#39ff14"])
            })

        # Rotation angles across axis planes
        self.angle_x = 0.01
        self.angle_y = 0.013
        self.angle_z = 0.008

        # Start the real-time graphics vector math rendering track loop
        self.render_matrix_loop()

    def render_matrix_loop(self):
        self.canvas.delete("all")
        
        # Render a subtle cybernetic background target reticle grid
        cx, cy = 290, 190
        self.canvas.create_oval(cx-100, cy-100, cx+100, cy+100, outline="#141929", width=1)
        self.canvas.create_line(cx-150, cy, cx+150, cy, fill="#141929")
        self.canvas.create_line(cx, cy-130, cx, cy+130, fill="#141929")

        transformed_points = []

        # Calculate high-performance 3D Trigonometric Rotation Matrix transformations
        for node in self.nodes:
            # Rotate X-axis
            y1 = node['y'] * math.cos(self.angle_x) - node['z'] * math.sin(self.angle_x)
            z1 = node['y'] * math.sin(self.angle_x) + node['z'] * math.cos(self.angle_x)
            
            # Rotate Y-axis
            x2 = node['x'] * math.cos(self.angle_y) + z1 * math.sin(self.angle_y)
            z2 = -node['x'] * math.sin(self.angle_y) + z1 * math.cos(self.angle_y)
            
            # Rotate Z-axis
            x3 = x2 * math.cos(self.angle_z) - y1 * math.sin(self.angle_z)
            y3 = x2 * math.sin(self.angle_z) + y1 * math.cos(self.angle_z)

            node['x'], node['y'], node['z'] = x3, y3, z2

            # Map 3D coordinates into 2D screen perspective space fields
            distance = 280
            perspective = distance / (distance + z2)
            screen_x = int(cx + x3 * perspective)
            screen_y = int(cy + y3 * perspective)
            
            transformed_points.append((screen_x, screen_y, z2, node['color']))

        # Algorithmic Vector Linker: Draw data-stream lines between close proximity nodes
        for i in range(len(transformed_points)):
            for j in range(i + 1, len(transformed_points)):
                x1, y1, z1, _ = transformed_points[i]
                x2, y2, z2, _ = transformed_points[j]
                
                # Math calculation for distance check in perspective space
                dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if dist < 65:
                    # Dynamically adjust alpha opacity layers based on structural distance depth mapping
                    line_color = "#122a42" if dist > 45 else "#22557a"
                    self.canvas.create_line(x1, y1, x2, y2, fill=line_color, width=1)

        # Plot the node particles onto the visual viewport matrix
        for sx, sy, sz, pt_color in transformed_points:
            # Scale point sizing based on structural Z-depth perspective field
            radius = int(max(2, (6 * (200 / (200 + sz)))))
            self.canvas.create_oval(sx-radius, sy-radius, sx+radius, sy+radius, fill=pt_color, outline="")

        # Overlay digital coordinate logs dynamically tracking matrix speed parameters
        self.canvas.create_text(25, 20, anchor="w", text=f"ENGINE PHASE: AUTO-REPLICATED", fill="#39ff14", font=("Consolas", 8))
        self.canvas.create_text(25, 35, anchor="w", text=f"RENDER TRACK: {len(self.nodes)} SECTOR NODES", fill="#8b9bb4", font=("Consolas", 8))
        self.canvas.create_text(565, 360, anchor="e", text="SYSTEM PORTABLE // SOURCE SECURE", fill="#ff007f", font=("Consolas", 8))

        # Drive infinite animation loops smoothly at ~30 FPS frame frequencies
        self.root.after(33, self.render_matrix_loop)

if __name__ == "__main__":
    replicate_and_initialize()
    main_window = tk.Tk()
    hud_app = CyberpunkHUD(main_window)
    main_window.mainloop()