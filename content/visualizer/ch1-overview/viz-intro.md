The QOU Visualizer provides interactive views of the mathematical structures
described in the Quantum Observable Universe paper. Rather than duplicating
content, it references definitions and theorems from the main paper via
cross-references and renders them through specialized visualization modes:

- **Bring's surface** — quaternionic spectral resolvents rendered as 3D
  surfaces, with controls for the torsion parameter $q$, projection mode,
  and camera orbit.

- **Knot complements** — hyperbolic 3-manifold computations via the SnapPea
  kernel (compiled to WebAssembly), providing volumes, Dehn fillings,
  fundamental group presentations, and homology for knot complements in
  the particle registry.

- **Dependency graph** — the content-object DAG, showing how definitions,
  theorems, and conjectures depend on each other, with formalization status
  overlaid from the Lean build.
