---
# qou-35a8
title: Which Nahm datum A does the tetraplectic sum give beyond 4_1?
status: in-progress
type: task
created_at: 2026-11-27T17:26:40Z
updated_at: 2026-11-28T01:03:40Z
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

## 2026-11-28 follow-up (PR #9868)

- Integral N in the #9852 polarization exists only for RᵃL with a ≤ 4; the integral polarization varies with a, so a uniform integral datum would be a selection.
- Polarization-free replacement: NeumannZagierBloch.det_smul_nzClass_mem_blochGroup (A·Bᵀ symmetric ⇒ det(B)·Σ[z] ∈ B(F)). RᵃL rows in closed form; A·Bᵀ symmetric proved for 3 ≤ a ≤ 8 (decide), probe to a ≤ 12, |det B| = 2(a−2).
- Open: symmetry for all a in Lean; regulator in QOU/Transcendental/.

## 2026-11-28 (PR #9883)

- RaLSymplectic.ra_isSymm_all: A·Bᵀ symmetric for every a ≥ 3 (symbolic). raClass_mem_blochGroup_all: det(B)·Σ[z] ∈ B(F) for every σ₀ᵃσ₁⁻¹, a ≥ 3. Open: |det B| = 2(a−2) in Lean; regulator.

2026-11-28: PR #9891 proves |det raB a| = 2(a − 2) and det raB a ≠ 0 for every a ≥ 3 (RaLDeterminant.lean, no sorry, standard axioms only). With #9883 (A·Bᵀ symmetric) the NZ data are nondegenerate and symplectic for the whole RᵃL family, so N = −B⁻¹A exists over ℚ and det B · Σ[z] ∈ B(F). Integrality of N holds only for a ≤ 4 in this polarization. Still open: the regulator in QOU/Transcendental/.

2026-11-28: PR #9895 — LeptonBundleRegulator.lean (Transcendental). Regulator of any Nahm/NZ class over ℂ = Σ D(zᵢ); μ: D(1/2+y)+2D(y); τ: 2D(A(s))+D(B(s))+2D(s); RᵃL (a≥3): det B·Σ D(zᵢ), det B ≠ 0. Open next: D(z) > 0 for Im z > 0 (not in corpus) to show the classes are nonzero; located-cut volume comparison.

2026-11-28: PR #9898 — BlochWignerPositive.lean: D(z) > 0 for Im z > 0 (blochD_pos); μ and τ regulators positive, so both classes are nonzero in B(ℂ)⊗ℚ. RᵃL family positivity needs the shapes of the geometric solution in H for general a — not yet derived. Next open: located-cut comparison with volume.

2026-11-28: #9900 (RᵃL class nonzero at any upper-half-plane solution) and #9901 (explicit positive angle structure on RᵃL for every a ≥ 3, integer angles, N = 128(a²+1)). Still open: volume maximization (Casson–Rivin / Futer–Guéritaud) from angle structure to shapes in H — the last step to unconditional nonvanishing of every RᵃL class.

## 2026-11-28 — volume concavity: already on main, no new file
Started TetVolumeConcave.lean, then found the result already proved on main, three times over:
`QOU.Knot.Rivin.strictConcaveOn_tetVolLine` (RivinConcavity.lean), `tetVol_strictConcaveOn`
(IdealTetrahedronVolumeConcave.lean) and the multi-tetrahedron `totalVol_strictConcaveOn` /
`totalVol_maximizer_unique` (MultiTetVolumeConcave.lean). Draft dropped, no PR. #9901 (RᵃL positive
angle structure) merged as 30a070c1bd. Remaining for RᵃL: (1) at an interior critical point of total
volume on the RᵃL angle polytope the shapes satisfy the gluing (log-modulus) equations; (2) the maximum is
interior (Futer–Guéritaud boundary argument). L6a4VolumeMaximum.lean is the worked template for (1).

## 2026-11-28 — critical point lemma (PR #9906)
`NZVolumeCritical.lean`: `logModulus_gluing`, `exists_nzSolution_of_isVolMax` (shapes (sin β/sin(α+β))e^{iα}
solve every NZ row exactly, all in H), `regulator_pos_of_isVolMax`. Generic in symplectic (A|B). Still open:
the maximum is interior (Futer–Guéritaud boundary step) — next.
