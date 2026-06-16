import numpy as np
import matplotlib.pyplot as plt

# Import the generic evolutionary infrastructure for dynamical system simulations
from q_dynamics_engine import (
    load_isotope,
    DynamicSpacetimeLattice,
    ComplexMolecule,
    simulate_transit,
    M_MU_M_E_RATIOS
)

# ============================================================
# Configurable geometric parameters
# ============================================================
L = 1.0              # Emitter-to-slit distance [m]
D = 0.5e-3           # Slit spacing center-to-center [m]
d = 0.1e-3           # Slit width [m]
w = 0.05e-3          # Slit thickness / depth [m]
H = 1.0              # Slit-to-screen distance [m]
wavelength = 500e-9  # de Broglie wavelength [m]

OUTPUT_PATH = "simulations/q_double_slit_output.png"

def create_double_slit_nodes():
    """Generate the explicit structural lattice points for the double slit."""
    nodes = []
    for x_center in [D/2.0, -D/2.0]:
        for y_offset in np.linspace(-d/2, d/2, 5):
            for z_offset in np.linspace(0, w, 2):
                nodes.append([x_center, y_offset, z_offset])
    return nodes


def run_simulation():
    # Load Carbon-12 for the slit material
    z_material, a_material = 6, 12
    print(f"Loading isotope Z={z_material}, A={a_material} from repository...")
    isotope_data = load_isotope(z_material, a_material)
    print(f"Loaded material: {isotope_data.get('element', 'Unknown')} (Mass: {isotope_data['ame_reference'].get('atomic_mass_u', 'N/A')} u)")
    
    nodes = create_double_slit_nodes()
    
    fig, axes = plt.subplots(len(M_MU_M_E_RATIOS), 1, figsize=(8, 12))
    if len(M_MU_M_E_RATIOS) == 1:
        axes = [axes]
        
    for i, q_0 in enumerate(M_MU_M_E_RATIOS):
        print(f"\n--- Simulating q-regime (initial mass ratio q_0 = {q_0}) ---")
        
        # Initialize the non-rigid lattice with the specific local q_0 section
        lattice = DynamicSpacetimeLattice(isotope_data, nodes, initial_q=q_0)
        
        # The molecule acts as the transiting particle interacting with the non-rigid slit
        molecule = ComplexMolecule(center_position=[D/4.0, 0.0, -1e-3], velocity=[0.0, 0.0, 2e2])
        
        trajectory, lat_hist, q_hist, phase, winding, inv_stable = simulate_transit(lattice, molecule)
        
        final_q_avg = np.mean(lattice.q_section)
        
        print(f"  Final Avg q (Mass Ratio): {final_q_avg:.6f} (Evolved from {q_0})")
        print(f"  Dynamic Phase State: {phase}")
        print(f"  Topological Winding: {winding:.4e}")
        print(f"  Topological Invariant Stable: {inv_stable}")
        
        ax = axes[i]
        # Plot initial lattice projected on x-y
        ax.scatter(lat_hist[0][:, 0]*1e3, lat_hist[0][:, 1]*1e3, c='lightgray', s=10, label='Initial Lattice')
        # Plot final evolved lattice
        ax.scatter(lattice.nodes[:, 0]*1e3, lattice.nodes[:, 1]*1e3, c='red', s=10, marker='x', label='Evolved Lattice')
        # Plot molecule trajectory
        ax.plot(trajectory[:, 0]*1e3, trajectory[:, 1]*1e3, c='blue', label='Molecule Trajectory')
        
        ax.set_title(f"Initial q_0={q_0} | Final <q>={final_q_avg:.4f} | Phase: {phase}")
        ax.set_xlabel("x [mm]")
        ax.set_ylabel("y [mm]")
        ax.legend(loc="lower right", fontsize=8)
        ax.grid(True)

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    print(f"\nSaved evolutionary infrastructure output to {OUTPUT_PATH}")


if __name__ == "__main__":
    run_simulation()
