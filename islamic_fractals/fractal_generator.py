# src/fractal_generator.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class IslamicFractalGenerator:
    def __init__(self, background_color='#f5f5dc'):
        self.background_color = background_color
        
    def create_octagon(self, center, size):
        """Create points for an octagon centered at given coordinates"""
        angles = np.linspace(0, 2*np.pi, 9)[:-1]
        x = center[0] + size * np.cos(angles + np.pi/8)
        y = center[1] + size * np.sin(angles + np.pi/8)
        return np.column_stack([x, y])

    def create_star(self, center, size):
        """Create points for an 8-pointed star"""
        outer_angles = np.linspace(0, 2*np.pi, 9)[:-1]
        inner_angles = outer_angles + np.pi/8
        
        outer_x = center[0] + size * np.cos(outer_angles)
        outer_y = center[1] + size * np.sin(outer_angles)
        inner_x = center[0] + (size/2) * np.cos(inner_angles)
        inner_y = center[1] + (size/2) * np.sin(inner_angles)
        
        points = []
        for i in range(8):
            points.extend([(outer_x[i], outer_y[i]), (inner_x[i], inner_y[i])])
        return np.array(points)

    def draw_pattern(self, ax, center, size, depth):
        """Recursively draw the Islamic pattern"""
        if depth <= 0:
            return
        
        octagon = self.create_octagon(center, size)
        polygon = Polygon(octagon, facecolor='none', edgecolor='darkblue', linewidth=1)
        ax.add_patch(polygon)
        
        star = self.create_star(center, size*0.8)
        polygon = Polygon(star, facecolor='none', edgecolor='darkred', linewidth=1)
        ax.add_patch(polygon)
        
        for i in range(8):
            angle = i * np.pi/4
            new_center = (
                center[0] + size*0.7 * np.cos(angle),
                center[1] + size*0.7 * np.sin(angle)
            )
            self.draw_pattern(ax, new_center, size*0.4, depth-1)

    def generate_fractal(self, depth, size=5, dpi=300):
        """Generate a fractal with specified depth and save it"""
        fig, ax = plt.subplots(figsize=(12, 12), dpi=dpi)
        ax.set_aspect('equal')
        ax.set_facecolor(self.background_color)
        fig.patch.set_facecolor(self.background_color)
        
        self.draw_pattern(ax, (0, 0), size, depth)
        
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.axis('off')
        
        return fig, ax
