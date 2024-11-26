# src/utils.py
import os
from pathlib import Path

def ensure_directory(directory):
    """Ensure the specified directory exists"""
    Path(directory).mkdir(parents=True, exist_ok=True)

def save_figure(fig, filename, directory='output'):
    """Save figure with proper directory handling"""
    ensure_directory(directory)
    filepath = os.path.join(directory, filename)
    fig.savefig(filepath, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
