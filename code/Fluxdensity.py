import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

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

# ---------------- MAXWELL DATA ----------------
maxwell_path = r"C:/Projects/Inphase/Benchmarking/plot2_2d.csv"
df_mx = pd.read_csv(maxwell_path)

s_mm = df_mx["Distance [mm]"].values
B_mx = df_mx["B_radial []"].values

R_mm = 46.1
theta_mx = (s_mm / R_mm) * (180.0 / np.pi)
theta_mx = theta_mx % 360.0

idx_mx = np.argsort(theta_mx)
theta_mx = theta_mx[idx_mx]
B_mx = B_mx[idx_mx]

B_mx_smooth = savgol_filter(B_mx, 21, 3)

# ---------------- PAPER DATA ----------------
paper_path = "C:/Projects/Inphase/Benchmarking/Default_Dataset.csv"
df_paper = pd.read_csv(paper_path)

theta_paper = df_paper["Distance"].values
B_paper = df_paper["B_radial"].values

idx_paper = np.argsort(theta_paper)
theta_paper = theta_paper[idx_paper]
B_paper = B_paper[idx_paper]

# ---------------- PLOT ----------------
plt.figure(figsize=(10,5), dpi=150)

plt.plot(theta_mx, B_mx_smooth,color='black',linewidth=3, label="Simulation Results")
plt.plot(theta_paper, B_paper, color='red', linewidth=3,linestyle="--", label="Experimental Results")

plt.xlabel(r"Mechanical angle $\theta$ [deg]")
plt.ylabel("Radial flux density [T]")

plt.xlim(0, 360)

plt.legend(frameon=False)
plt.grid(True, linestyle="--", alpha=0.6)

legend = plt.legend(loc="upper right",
                    bbox_to_anchor=(0.98, 1.15),
                    frameon=False)
#plt.xticks(fontweight="bold")
#plt.yticks(fontweight="bold")


plt.tight_layout()
plt.show()