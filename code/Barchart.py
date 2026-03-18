import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# GLOBAL STYLE
# ==================================================
plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 18,
    "axes.titlesize": 22,
    "axes.labelsize": 22,
    "axes.labelweight": "bold",
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "legend.fontsize": 18,
    "lines.linewidth": 2.5,
    "axes.linewidth": 2,
})

# ---------------- DATA ----------------
modes = ['m = 2', 'm = 3', 'm = 4', 'm = 0 (breathing)']

exp = [720, 1495, 2424, 7500]
sim = [785, 1343, 2621, 7535]

x = np.arange(len(modes))
width = 0.35

# ---------------- PLOT ----------------
fig, ax = plt.subplots(figsize=(10,7), dpi=150)

bars1 = ax.bar(x - width/2, exp, width, label='Experimental', color='steelblue')
bars2 = ax.bar(x + width/2, sim, width, label='Simulated', color='orange')

ax.set_ylabel('Frequency (Hz)')
ax.set_xlabel('Mode')
ax.set_title('Experimental vs Simulated Modal Frequencies')

ax.set_xticks(x)
ax.set_xticklabels(modes)

ax.legend()

# Value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2,
                height + 100,
                f'{int(height)}',
                ha='center')

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('modal_frequencies_highres.png', dpi=300, bbox_inches='tight')
plt.show()