import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

# ==================================================
# GLOBAL STYLE (COMMON TO ALL)
# ==================================================
plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 30,
    "axes.titlesize": 30,
    "axes.labelsize":30,
    "axes.labelweight": "bold",
    "xtick.labelsize": 30,
    "ytick.labelsize": 30,
    "legend.fontsize": 30,
    "lines.linewidth": 2.5,
    "axes.linewidth": 2,
    "grid.linewidth": 1,
})

plt.style.use('classic')

# ---------------- DATA ----------------
path = './Result/'
file = ('/Benchmark_Vivek.csv')
n_rpm = 16

dat = np.loadtxt(path+file, skiprows=1, delimiter=',')

freq = np.reshape(dat[:,1], (n_rpm, int(len(dat)/n_rpm))).T
rpm  = np.reshape(dat[:,2], (n_rpm, int(len(dat)/n_rpm))).T
acc  = np.reshape(dat[:,4], (n_rpm, int(len(dat)/n_rpm))).T

# Avoid log(0)
vmin = 4e-6
acc[acc < vmin] = vmin

# ---------------- PLOT ----------------
fig, ax = plt.subplots(figsize=(10,7), dpi=150)

cs = ax.contourf(freq, rpm, acc,
                 vmin=vmin, vmax=60,
                 locator=ticker.LogLocator(),
                 cmap="gist_rainbow_r")

# Colorbar
cbar = fig.colorbar(cs)
cbar.set_label('Radial Acceleration [m/s$^2$]', fontsize=26, fontweight='bold')

# ---------------- ELECTRICAL ORDER LINES ----------------
p = 5
orders = [2, 4, 6, 8, 10]
rpm_line = np.linspace(200, np.max(rpm), 500)

for k in orders:
    f_order = k * p * rpm_line / 60
    ax.plot(f_order, rpm_line, linestyle='--',linewidth=3, color='black')

    idx = int(len(rpm_line)*0.75)
    ax.text(f_order[idx], rpm_line[idx],
            f'{k}$f_e$',
            fontsize=22,
            fontweight='bold',
            rotation=35,
            color='black')

# ---------------- AXES ----------------
ax.set_xlim(0, 1200)
ax.set_xlabel('Frequency [Hz]', fontsize=26, fontweight='bold')
ax.set_ylabel('Rotational Speed [RPM]', fontsize=26, fontweight='bold')

# Grid
ax.grid(which='major', linestyle='-', alpha=0.2)
ax.minorticks_on()

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.tight_layout()
plt.show()