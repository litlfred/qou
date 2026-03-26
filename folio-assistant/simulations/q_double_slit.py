"""
2D q-deformed double-slit interference simulation.

Models wave propagation using the q-deformed differential:
    d_q = q^{-1} d + (1 - q^{-1}) pi_V(d)

where hbar_q = 1 - q^{-1} is the quantum Planck constant, and the
torsion phase inside the slit material is proportional to Vol(K),
the hyperbolic volume of the hadronic knot modeling the slit material.

At q=1, hbar_q=0 and classical double-slit interference is recovered exactly.

Usage:
    python simulations/q_double_slit.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Configurable geometric parameters
# ============================================================
L = 1.0              # Emitter-to-slit distance [m]
D = 0.5e-3           # Slit spacing center-to-center [m]
d = 0.1e-3           # Slit width [m]
w = 0.05e-3          # Slit thickness / depth [m]
H = 1.0              # Slit-to-screen distance [m]
wavelength = 500e-9  # de Broglie wavelength [m]

# ============================================================
# Torsion / knot parameters
# ============================================================
# Hyperbolic volume of the Borromean link complement (6_2^3)
VOL_K = 7.327724

# Normalization factor for the torsion strength (dimensionless, tunable)
TORSION_NORM = 1.0

# ============================================================
# q-deformation sweep values
# ============================================================
Q_VALUES = [1.0, 1.05, 1.1097, 1.2, 1.5]

# ============================================================
# Numerical resolution
# ============================================================
N_SLIT_POINTS = 200   # Number of secondary-source points per slit
N_SCREEN = 2000       # Number of screen sampling points
SCREEN_HALF_WIDTH = 5e-3  # Half-width of the screen sampling region [m]

# ============================================================
# Output
# ============================================================
OUTPUT_PATH = "simulations/q_double_slit_output.png"

# Derived constant
WAVENUMBER = 2.0 * np.pi / wavelength  # k [1/m]


def hbar_q(q: float) -> float:
    """Quantum Planck constant: hbar_q = 1 - q^{-1}."""
    if q == 1.0:
        return 0.0
    return 1.0 - 1.0 / q


def torsion_phase_profile(y_in_slit: np.ndarray, slit_half_width: float,
                          q: float) -> np.ndarray:
    """
    Compute the torsion phase for points inside the slit.

    The torsion field is stronger near the slit walls (Reeb push) and
    vanishes at the slit center. We model this as:

        torsion(y) = Vol(K) * TORSION_NORM * (2|y| / d)^2

    where y is measured from the slit center, so the profile is parabolic
    with maximum at the walls.

    The total extra phase accumulated traversing slit depth w is:
        delta_phi_torsion = hbar_q * torsion(y) * k * w

    where k = 2*pi/wavelength is the wavenumber.
    """
    hq = hbar_q(q)
    if hq == 0.0:
        return np.zeros_like(y_in_slit)

    # Normalized transverse position: 0 at center, 1 at wall
    eta = np.abs(y_in_slit) / slit_half_width
    # Parabolic torsion profile (quadratic in distance from center)
    torsion_strength = VOL_K * TORSION_NORM * eta ** 2
    return hq * torsion_strength * WAVENUMBER * w


def compute_intensity(q: float, screen_y: np.ndarray) -> np.ndarray:
    """
    Compute the intensity pattern on the screen using Huygens-Fresnel
    summation with q-deformation corrections.

    Each point within the two slit apertures acts as a secondary source.
    For each source point at transverse position y_s:
      - Classical phase from emitter to slit: k * sqrt(L^2 + y_s^2)
      - Classical phase from slit to screen:  k * sqrt(H^2 + (y_screen - y_s)^2)
      - q-deformation correction: torsion phase from traversing slit depth

    We sum complex amplitudes and take |sum|^2.
    """
    slit_half = d / 2.0

    # Slit 1 center at +D/2, slit 2 center at -D/2
    slit_centers = np.array([D / 2.0, -D / 2.0])

    # Secondary source points within each slit (relative to slit center)
    dy = np.linspace(-slit_half, slit_half, N_SLIT_POINTS)

    # Precompute torsion phase for each position within the slit
    torsion_phases = torsion_phase_profile(dy, slit_half, q)

    # Accumulate complex amplitude at each screen point
    # Shape: screen_y is (N_SCREEN,), we vectorize over it
    amplitude = np.zeros(len(screen_y), dtype=complex)

    for center in slit_centers:
        # Absolute positions of secondary sources
        y_sources = center + dy  # shape (N_SLIT_POINTS,)

        for j, y_s in enumerate(y_sources):
            # Distance from emitter (at origin) to source point in slit plane
            r1 = np.sqrt(L ** 2 + y_s ** 2)
            # Distance from source point to each screen point
            r2 = np.sqrt(H ** 2 + (screen_y - y_s) ** 2)

            # Classical phase accumulation
            phase_classical = WAVENUMBER * (r1 + r2)

            # q-deformation: extra phase from torsion inside slit material
            phase_torsion = torsion_phases[j]

            # Total phase
            total_phase = phase_classical + phase_torsion

            # Huygens-Fresnel: amplitude weighted by 1/sqrt(r2) for 2D
            # (cylindrical wave spreading). The 1/r1 factor is common
            # to all screen points for a given source so only affects
            # overall normalization.
            amplitude += np.exp(1j * total_phase) / np.sqrt(r2)

    intensity = np.abs(amplitude) ** 2
    # Normalize to peak = 1
    intensity /= intensity.max()
    return intensity


def run_simulation():
    """Run the q-sweep simulation and produce plots."""
    screen_y = np.linspace(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH, N_SCREEN)
    screen_y_mm = screen_y * 1e3  # Convert to mm for plotting

    # ----- Compute intensities for each q value -----
    results = {}
    for q in Q_VALUES:
        print(f"  Computing q = {q:.4f}  (hbar_q = {hbar_q(q):.6f}) ...")
        results[q] = compute_intensity(q, screen_y)

    # ----- Color map for q values -----
    cmap = plt.cm.viridis
    colors = [cmap(i / max(len(Q_VALUES) - 1, 1)) for i in range(len(Q_VALUES))]
    linestyles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]

    # ----- Figure with two subplots -----
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8),
                                    gridspec_kw={'height_ratios': [3, 1]})

    # --- Main plot: intensity vs screen position ---
    for i, q in enumerate(Q_VALUES):
        label = f"q = {q:.4f}" if q != 1.0 else "q = 1.0 (classical)"
        lw = 2.0 if q == 1.0 else 1.3
        ax1.plot(screen_y_mm, results[q],
                 color=colors[i], linestyle=linestyles[i % len(linestyles)],
                 linewidth=lw, label=label)

    ax1.set_xlabel("Screen position [mm]")
    ax1.set_ylabel("Normalized intensity")
    ax1.set_title("q-Deformed Double-Slit Interference Pattern")
    ax1.legend(loc="upper right", fontsize=9)
    ax1.set_xlim(-SCREEN_HALF_WIDTH * 1e3, SCREEN_HALF_WIDTH * 1e3)
    ax1.set_ylim(bottom=0)
    ax1.grid(True, alpha=0.3)

    # --- Secondary plot: torsion phase profile across slit width ---
    slit_half = d / 2.0
    y_slit = np.linspace(-slit_half, slit_half, 500)
    y_slit_um = y_slit * 1e6  # Convert to micrometers

    for i, q in enumerate(Q_VALUES):
        if q == 1.0:
            continue  # Zero torsion, skip
        phases = torsion_phase_profile(y_slit, slit_half, q)
        label = f"q = {q:.4f}"
        ax2.plot(y_slit_um, phases,
                 color=colors[i], linestyle=linestyles[i % len(linestyles)],
                 linewidth=1.3, label=label)

    ax2.set_xlabel("Position within slit [μm]")
    ax2.set_ylabel("Torsion phase [rad]")
    ax2.set_title("Torsion Phase Profile Across Slit Width")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=150, bbox_inches='tight')
    print(f"\n  Plot saved to {OUTPUT_PATH}")
    plt.close(fig)


if __name__ == "__main__":
    print("q-Deformed Double-Slit Simulation")
    print("=" * 40)
    print(f"  Wavelength:     {wavelength * 1e9:.0f} nm")
    print(f"  Slit spacing:   {D * 1e3:.2f} mm")
    print(f"  Slit width:     {d * 1e6:.0f} μm")
    print(f"  Slit thickness: {w * 1e6:.0f} μm")
    print(f"  Vol(K):         {VOL_K} (Borromean rings)")
    print(f"  q values:       {Q_VALUES}")
    print()
    run_simulation()
    print("  Done.")
