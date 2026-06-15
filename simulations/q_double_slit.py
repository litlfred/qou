import os
import json
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

VOL_K = 7.327724
TORSION_NORM = 1.0
Q_VALUES = [1.0, 1.05, 1.1097, 1.2, 1.5]
OUTPUT_PATH = "simulations/q_double_slit_output.png"

def load_isotope(z, a):
    """
    Dynamically load arbitrary slit materials directly from the codebase's isotope repository.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths_to_try = [
        os.path.join(base_dir, "computations", f"canonical-isotope-witness-Z{z:02d}.witness.json"),
        os.path.join(base_dir, "computations", f"canonical-isotope-witness-Z{z}.witness.json"),
        os.path.join(base_dir, "qou-mass", "src", "qou_mass", "data", "isotopes", f"canonical-isotope-witness-Z{z}.witness.json"),
        os.path.join(base_dir, "qou-mass", "src", "qou_mass", "data", "isotopes", f"canonical-isotope-witness-Z{z:02d}.witness.json")
    ]
    
    for json_path in paths_to_try:
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                data = json.load(f)
                for row in data.get("data", {}).get("rows", []):
                    if row.get("A") == a:
                        return row
    
    return {"element": "Unknown", "A": a, "Z": z, "ame_reference": {"atomic_mass_u": a}}


class DynamicSpacetimeLattice:
    def __init__(self, isotope_data, initial_q=1.0):
        """
        An explicit structural starting state/lattice.
        The grid is NOT a fixed rigid grid. The coordinate system evolves.
        """
        self.mass = isotope_data["ame_reference"].get("atomic_mass_u", 1.0)
        self.element = isotope_data.get("element", "Unknown")
        
        # Construct the double slit lattice points
        nodes = []
        lattice_spacing = 0.05e-3
        for x_center in [D/2.0, -D/2.0]:
            for y_offset in np.linspace(-d/2, d/2, 5):
                for z_offset in np.linspace(0, w, 2):
                    nodes.append([x_center, y_offset, z_offset])
        self.nodes = np.array(nodes)
        
        # The coordinate grid is non-rigid; lattice nodes possess velocities
        self.velocities = np.zeros_like(self.nodes)
        
        # q is locally a value at a point (a local section)
        # Allows downstream users to pass an arbitrary q_0 initial state per point
        if isinstance(initial_q, (list, np.ndarray)):
            self.q_section = np.array(initial_q, dtype=float)
        else:
            self.q_section = np.full(len(self.nodes), float(initial_q))
            
    def set_arbitrary_q_section(self, q_array):
        """Allows a downstream user to load some arbitrary initial state on the collection of points."""
        assert len(q_array) == len(self.nodes), "q_array must match the number of lattice points."
        self.q_section = np.array(q_array, dtype=float)


class ComplexMolecule:
    def __init__(self, center_position, velocity):
        """
        Molecular emission infrastructure for polyatomic interactions.
        """
        self.center = np.array(center_position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        
        # Define relative geometric structure
        self.atoms_relative = np.array([
            [0.0, 0.0, 0.0],
            [1e-5, 1e-5, 0.0],
            [-1e-5, 1e-5, 0.0]
        ])
        
    def get_absolute_positions(self):
        return self.atoms_relative + self.center


def evaluate_phase_state(q_avg, kinetic_energy, interaction_energy):
    """
    Evaluate material phase states dynamically as a function of the local q-regime.
    """
    effective_temp = (kinetic_energy / (abs(interaction_energy) + 1e-12)) * q_avg
    if effective_temp < 0.5:
        return "Solid"
    elif effective_temp < 1.5:
        return "Liquid"
    elif effective_temp < 5.0:
        return "Gas"
    else:
        return "Plasma"


def simulate_transit(lattice, molecule, dt=1e-7, steps=200):
    """
    Simulate full structural interaction and N-body dynamics, including:
    - Molecule interacting with non-rigid lattice
    - Lattice coordinates evolving
    - q evolving continuously from initial conditions based on local geometry/energy
    """
    trajectory = []
    topological_winding = 0.0
    phase_states = []
    
    # Store history for downstream analytical tools
    lattice_history = []
    q_history = []
    
    for step in range(steps):
        force_on_molecule = np.zeros(3)
        interaction_energy = 0.0
        
        lattice_history.append(lattice.nodes.copy())
        q_history.append(lattice.q_section.copy())
        
        # N-body interaction
        for i, p in enumerate(lattice.nodes):
            q_local = lattice.q_section[i]
            r_vec = molecule.center - p
            dist = np.linalg.norm(r_vec)
            
            if dist > 0:
                # Local q-deformed interaction potential
                f_mag = (1.0 / (dist**2))
                if q_local != 1.0:
                    hbar_q = 1.0 - 1.0/q_local
                    torsion_factor = VOL_K * TORSION_NORM * hbar_q
                    f_mag += torsion_factor / (dist**3)
                
                force_dir = r_vec / dist
                force_vec = f_mag * force_dir * 1e-15
                
                force_on_molecule += force_vec
                
                # Back-reaction: lattice coordinate system is not rigid, it evolves
                force_on_lattice_node = -force_vec
                lattice.velocities[i] += (force_on_lattice_node / lattice.mass) * dt
                
                # The q section evolves locally from initial conditions due to interaction/gravity
                q_evolution_rate = np.dot(force_vec, r_vec) * 1e12  # coupling coefficient
                lattice.q_section[i] += q_evolution_rate * dt
                
                interaction_energy -= f_mag * 1e-15 * dist
        
        # Advance lattice coordinates (structural evolution)
        lattice.nodes += lattice.velocities * dt
        
        # Advance molecule trajectory
        molecule.velocity += (force_on_molecule / lattice.mass) * dt
        molecule.center += molecule.velocity * dt
        trajectory.append(molecule.center.copy())
        
        # State tracking
        q_avg = np.mean(lattice.q_section)
        kinetic_energy = 0.5 * lattice.mass * np.linalg.norm(molecule.velocity)**2
        
        L_z = molecule.center[0]*molecule.velocity[1] - molecule.center[1]*molecule.velocity[0]
        topological_winding += L_z * dt
        
        phase_states.append(evaluate_phase_state(q_avg, kinetic_energy, interaction_energy))
        
    stable_phase = max(set(phase_states), key=phase_states.count)
    final_avg_q = np.mean(lattice.q_section)
    invariant_stable = abs(topological_winding) > 1e-39 and abs(final_avg_q - 1.0) > 1e-5
    
    return np.array(trajectory), lattice_history, q_history, stable_phase, topological_winding, invariant_stable


def run_simulation():
    # Load Carbon-12 for the slit material
    z_material, a_material = 6, 12
    print(f"Loading isotope Z={z_material}, A={a_material} from repository...")
    isotope_data = load_isotope(z_material, a_material)
    print(f"Loaded material: {isotope_data.get('element', 'Unknown')} (Mass: {isotope_data['ame_reference'].get('atomic_mass_u', 'N/A')} u)")
    
    fig, axes = plt.subplots(len(Q_VALUES), 1, figsize=(8, 12))
    if len(Q_VALUES) == 1:
        axes = [axes]
        
    for i, q_0 in enumerate(Q_VALUES):
        print(f"\n--- Simulating q-regime (initial q_0 = {q_0}) ---")
        
        # Initialize the non-rigid lattice with the specific local q_0 section
        lattice = DynamicSpacetimeLattice(isotope_data, initial_q=q_0)
        
        molecule = ComplexMolecule(center_position=[D/4.0, 0.0, -1e-3], velocity=[0.0, 0.0, 2e2])
        
        trajectory, lat_hist, q_hist, phase, winding, inv_stable = simulate_transit(lattice, molecule)
        
        final_q_avg = np.mean(lattice.q_section)
        
        print(f"  Final Avg q: {final_q_avg:.6f} (Evolved from {q_0})")
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

