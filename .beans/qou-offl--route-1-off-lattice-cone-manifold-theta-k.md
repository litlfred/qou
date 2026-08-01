---
# qou-offl
title: 'Route 1 (parent: qnnq): off-lattice ϑ_K = cone-manifold / generalized-Dehn-filling deformation. Non-integer (m,ℓ) is standard geometry: Thurston generalized Dehn surgery coefficients ∈ ℝ², Hodgson–Kerckhoff cone-manifold rigidity, Gukov/Murakami generalized volume conjecture (continuous parameter u off the complete structure). Probe: fit probed ϑ values (4₁: proton 0.203, muon 0.059) to real filling coefficients on the NZ volume function; Lean: conditional NZ dVol/du statement.'
status: todo
type: task
priority: high
created_at: 2026-07-31T19:30:00Z
updated_at: 2026-08-01T22:06:12Z
---

Literature anchors:
- Gukov, "Three-dimensional quantum gravity, Chern-Simons theory, and the A-polynomial" — generalized volume conjecture, continuous u.
- H. Murakami — cone-manifold volumes from deformed colored Jones limits (figure-eight AND Borromean rings; the latter feeds qou-mcus).
- Hodgson–Kerckhoff, "Rigidity of hyperbolic cone-manifolds and hyperbolic Dehn surgery" (JDG 48, 1998) — real cone angles are rigid: an off-lattice ϑ is a well-defined geometric datum, not a fudge.
- Neumann–Zagier volume function Φ(u) for the derivative structure.

The T4-inverted ϑ values are NOT on the (√3/2)·ln q₀ integer lattice — this route says they shouldn't be: the braid word determines a real slope (generalized filling coefficient), quantization to ℤ² is only for closed fillings.


---

## 2026-08-01 RE-SPEC — this is now the arc's live independent leg (PR #4513)

`qou-rdmr` is refuted at scope (a), so this is the remaining candidate for an
`A_ω`-independent determination of ϑ. Two corrections + a test spec.

### Correction 1 — do NOT fit to the T4 ϑ values

This bean says to "fit probed ϑ values to real filling coefficients". Those ϑ
are T4-inverted and therefore `A_ω`-conditioned (see the circularity note);
fitting to them is exactly the `circ-derived-used-as-input` defect. Predict
from geometry first; compare after.

### Correction 2 — the anchors are two DIFFERENT knots

"4₁: proton 0.203, muon 0.059" is wrong. Per `qbeta_t3_multiknot_binding_probe.py`:
muon → 4₁ (figure-eight), proton → 𝔹₃ (Borromean). Two knots, two words.

### The acceptance test (new — this is what makes the route well-posed)

Eliminating `A_ω` between the two anchor equations leaves an invariant built
from measured `S` alone — no `A_ω`, no `q₀`:

    (ln²q₀ − ϑ_μ²) / (ln²q₀ − ϑ_p²)  =  S_μ/S_p  =  −0.2453912076

Solved: ϑ_p² = L − (L − ϑ_μ²)/r,  L = ln²q₀.

**Test:** produce ϑ for BOTH 4₁ and 𝔹₃ from cone-manifold geometry alone, then
check the pair against the curve. Landing on it DETERMINES
`A_ω = S_μ/(κ(L − ϑ_μ²))` — the arc's first genuine determination rather than a
literature import. Missing it refutes the route at scope (a).

### Two hazards to design against

- **Re-parameterization.** If the geometric ϑ carries its own free
  normalization, the route has moved the degree of freedom, not removed it. The
  test is immune only if the normalization is fixed BEFORE the comparison.
  State it up front.
- **Single-anchor fitting.** Any route can hit ONE ϑ by choosing its
  normalization. The curve is a genuine test precisely because it constrains
  the PAIR; a one-anchor match establishes nothing.

Curve: computations/probes/qbeta_qnnq_afree_theta_constraint_probe.py
Note:  docs/scope/2026-08-01-theta-independent-routes.md §2-§3
