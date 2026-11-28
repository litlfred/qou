---
# qou-35a8
title: Which Nahm datum A does the tetraplectic sum give beyond 4_1?
status: in-progress
type: task
created_at: 2026-11-27T17:26:40Z
updated_at: 2026-11-28T00:40:00Z
---

Research path, opened 2026-11-27 (thread 'Reeb flow and tetraplectic structure', PR #9496 merged).

PR #9496 (QOU/MassTheory/NahmBlochBridge.lean, sorry-free) proves: for a symmetric integer matrix A, any solution of 1 - z_i = prod_j z_j^{A_ij} gives sum [z_i] in the Bloch group B(F). For the figure-eight knot 4_1 the datum is A = (-1) (Habiro q->1 ratio, habiro41_nahm_iff), and fig8Class is the Nahm class of A = -I.

OPEN: which Nahm datum A (if any) the tetraplectic sinh-lattice state sum gives for knots beyond 4_1. It must be DERIVED from the state sum's q->1 saddle equations, not chosen to match a volume (no-fit rule).

Next honest step: write the q->1 stationary-phase equations of the tetraplectic sum for a second hyperbolic knot (5_2 is the natural test, 3 tetrahedra) and read A off them; check A is symmetric, so nahmClass_mem_blochGroup applies.

Conjecture-tracking bean: do not close until the mathematics closes (AGENTS.md rule 13a).

## 2026-11-28 progress (thread "Find the tetraplectic Nahm data beyond 41", PR #9852)

- 5₂ was already closed on main before this entry: `TwistKnotNahm.lean` reads the datum off Masbaum's twist-knot sum (`fiveTwo_mem_blochGroup`).
- Beyond that, the lepton words of #9835 through their once-punctured-torus bundles: N = −B⁻¹A from the Floyd–Hatcher NZ rows (the Φ_b state-integral quadratic form). RL (4₁) N=[[0,−1],[−1,0]]; R²L (μ) N=[[−1,−1,−1],[−1,0,−1],[−1,−1,0]], shapes in ℚ(√−7); R⁴L (τ) symmetric 5×5, shapes in the cubic s³−6s²+8s−4 (disc −176). All integral, all signs +1, classes in B(F) (`LeptonBundleNahm.lean`, sorry-free). Probe `lepton_bundle_nahm_probe.py` 18/18.
- Still open: (1) the identification "tetraplectic sum = Φ_b state integral of the layering" is cited, not proved; (2) the datum depends on polarization, only the class is canonical; (3) the regulator / volume statement belongs in QOU/Transcendental/. Bean stays open (rule 13a).
