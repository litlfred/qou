import os
import re

# Completed files list from Batches 1, 2, 3, and 4
completed = {
    # Batch 1
    "BraidKnot/IsotopeKnot/equivalence.lean",
    "Torsion/antiparticle_crossing_reversal.lean",
    "MathlibExt/Scratch.lean",
    "HyperellipticQuintic/zeta5_residue_monodromy.lean",
    # Batch 2
    "HadronicMass/deuteron_binding_energy.lean",
    "HadronicMass/nucleon_borromean_topology.lean",
    "HadronicMass/pair_skein_mass_formula.lean",
    "Experimental/local_substrate_q.lean",
    "Experimental/terminal_resolution.lean",
    "Interactions/nucleon_ordering_factorization.lean",
    "Interactions/UniversalILP.lean",
    "Interactions/inductiveGBReduction.lean",
    "Interactions/confinementUniversality.lean",
    "Archimedean/knot_operator_selection.lean",
    # Batch 3
    "TopologicalMass/cat_descended_is_base_mass.lean",
    "TopologicalMass/cat_eigenspace_decomposition.lean",
    "TopologicalMass/cat_transient_localises_blowup.lean",
    "Torsion/KnotParticleGeneration.lean",
    "Torsion/mass_decomposition_categorical.lean",
    "Torsion/weak_equiv_invariance.lean",
    "QuantumObservableUniverse/exists_axiom_1_frobenius.lean",
    "QuantumObservableUniverse/exists_axiom_2_observability.lean",
    "QuantumObservableUniverse/exists_axiom_3_chern.lean",
    "QuantumObservableUniverse/exists_axiom_4_volume.lean",
    # Batch 4
    "HadronicMass/eos_borromean_cfl.lean",
    "AlgebraicSubstrate/HqBiFiltration/genus_filtration_ideal.lean",
    "AlgebraicSubstrate/HqBiFiltration/genus_maximal_descent.lean",
    "HadronicMass/gram_weighted_qvalue.lean",
    "Archimedean/brings_euler_characteristic.lean",
    "Archimedean/brings_riemann_hurwitz.lean",
    "HadronicMass/geom_yekutieli_alignment.lean",
    "CategoricalReeb/ofWeightDecomposition.lean",
    "CommutativeQOU/u1EquivariantReduction.lean",
    "FluidDynamics/discrete_vortex_spectrum.lean"
}

base_dir = "/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/"

def strip_comments_and_strings(content):
    result = []
    i = 0
    n = len(content)
    in_line_comment = False
    block_comment_depth = 0
    in_string = False
    while i < n:
        if in_line_comment:
            if content[i] == '\n':
                in_line_comment = False
                result.append('\n')
            i += 1
        elif block_comment_depth > 0:
            if i + 1 < n and content[i:i+2] == '/-':
                block_comment_depth += 1
                i += 2
            elif i + 1 < n and content[i:i+2] == '-/':
                block_comment_depth -= 1
                i += 2
            else:
                if content[i] == '\n':
                    result.append('\n')
                i += 1
        elif in_string:
            if content[i] == '\\' and i + 1 < n:
                i += 2
            elif content[i] == '"':
                in_string = False
                i += 1
            else:
                i += 1
        else:
            if i + 1 < n and content[i:i+2] == '--':
                in_line_comment = True
                i += 2
            elif i + 1 < n and content[i:i+2] == '/-':
                block_comment_depth = 1
                i += 2
            elif content[i] == '"':
                in_string = True
                i += 1
            else:
                result.append(content[i])
                i += 1
    return "".join(result)

candidates = []

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".lean"):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir)
            if rel_path in completed:
                continue
            try:
                with open(full_path, "r", encoding="utf-8") as file:
                    content = file.read()
                stripped = strip_comments_and_strings(content)
                matches = list(re.finditer(r'\bsorry\b', stripped))
                if len(matches) > 0:
                    candidates.append((rel_path, len(matches)))
            except Exception as e:
                print(f"Error reading {rel_path}: {e}")

# Sort candidates by number of sorry statements
candidates.sort(key=lambda x: x[1])

print(f"Found {len(candidates)} candidate files containing active sorry statements:")
for path, count in candidates:
    print(f" - {path} ({count} sorrys)")
