import os
import json
import numpy as np

VOL_K = 7.327724
TORSION_NORM = 1.0
Q0_VACUUM = 1.1097

def load_isotope(z, a):
    """
    Dynamically load arbitrary materials directly from the codebase's isotope repository.
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
    def __init__(self, isotope_data, nodes, initial_q=1.0):
        """
        An explicit structural starting state/lattice.
        The grid is NOT a fixed rigid grid. The coordinate system evolves.
        """
        self.mass = isotope_data["ame_reference"].get("atomic_mass_u", 1.0)
        self.element = isotope_data.get("element", "Unknown")
        
        # The coordinate grid is non-rigid; lattice nodes possess velocities
        self.nodes = np.array(nodes, dtype=float)
        self.velocities = np.zeros_like(self.nodes)
        
        # q is locally a value at a point (a local section)
        if isinstance(initial_q, (list, np.ndarray)):
            self.q_section = np.array(initial_q, dtype=float)
        else:
            self.q_section = np.full(len(self.nodes), float(initial_q))
            
    def set_arbitrary_q_section(self, q_array):
        assert len(q_array) == len(self.nodes), "q_array must match the number of lattice points."
        self.q_section = np.array(q_array, dtype=float)


class ComplexMolecule:
    def __init__(self, center_position, velocity):
        """
        Molecular emission infrastructure for polyatomic interactions.
        """
        self.center = np.array(center_position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        
        self.atoms_relative = np.array([
            [0.0, 0.0, 0.0],
            [1e-5, 1e-5, 0.0],
            [-1e-5, 1e-5, 0.0]
        ])
        
    def get_absolute_positions(self):
        return self.atoms_relative + self.center


def evaluate_phase_state(q_avg, kinetic_energy, interaction_energy):
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
    - Inertial mass dynamically coupled to the evolving mass ratio q
    """
    trajectory = []
    topological_winding = 0.0
    phase_states = []
    
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
                f_mag = (1.0 / (dist**2))
                if q_local != 1.0:
                    hbar_q = 1.0 - 1.0/q_local
                    torsion_factor = VOL_K * TORSION_NORM * hbar_q
                    f_mag += torsion_factor / (dist**3)
                
                force_dir = r_vec / dist
                force_vec = f_mag * force_dir * 1e-15
                
                force_on_molecule += force_vec
                force_on_lattice_node = -force_vec
                
                # The absolute inertial mass of the node shifts dynamically based on the local mass ratio q(p)
                dynamic_mass_i = lattice.mass * (q_local / Q0_VACUUM)
                lattice.velocities[i] += (force_on_lattice_node / dynamic_mass_i) * dt
                
                # The q section evolves locally
                q_evolution_rate = np.dot(force_vec, r_vec) * 1e12
                lattice.q_section[i] += q_evolution_rate * dt
                
                interaction_energy -= f_mag * 1e-15 * dist
        
        # Advance lattice coordinates
        lattice.nodes += lattice.velocities * dt
        
        # Advance molecule trajectory with dynamically shifting effective mass
        molecule_mass = lattice.mass * (np.mean(lattice.q_section) / Q0_VACUUM)
        molecule.velocity += (force_on_molecule / molecule_mass) * dt
        molecule.center += molecule.velocity * dt
        trajectory.append(molecule.center.copy())
        
        q_avg = np.mean(lattice.q_section)
        kinetic_energy = 0.5 * lattice.mass * np.linalg.norm(molecule.velocity)**2
        
        L_z = molecule.center[0]*molecule.velocity[1] - molecule.center[1]*molecule.velocity[0]
        topological_winding += L_z * dt
        
        phase_states.append(evaluate_phase_state(q_avg, kinetic_energy, interaction_energy))
        
    stable_phase = max(set(phase_states), key=phase_states.count)
    final_avg_q = np.mean(lattice.q_section)
    invariant_stable = abs(topological_winding) > 1e-39 and abs(final_avg_q - 1.0) > 1e-5
    
    return np.array(trajectory), lattice_history, q_history, stable_phase, topological_winding, invariant_stable
