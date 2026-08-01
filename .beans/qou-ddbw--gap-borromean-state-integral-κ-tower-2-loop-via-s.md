---
# qou-ddbw
title: 'GAP: Borromean state-integral κ-tower (2-loop+) via saddle-point perturbation theory — arrow (A) value-map LHS'
status: todo
type: task
priority: normal
created_at: 2026-08-01T21:07:54Z
updated_at: 2026-08-01T21:08:43Z
---

Arrow (A) value-map, LHS perturbative series for the BORROMEAN.

STATE (2026-08-01):
- 4₁ Ohtsuki κ-tower is DONE in the corpus (exact, not fitted):
  κ₁=11√3π/108, κ₂=2π²/27, κ₃∝√3π³, κ₄∝98π⁴/729; odd κ ∝ √3·π (trace
  field ℚ(√−3)), even κ ∝ π². Fit-validated to ~24 digits. See
  docs/audits/2026-07-12-ohtsuki-higher-rungs-exact.md,
  scripts/qbeta_ohtsuki_kappa1_extract.py, OhtsukiTowerBarParity.lean.
- BORROMEAN κ-tower does NOT exist. This is the gap.

WHY IT MATTERS: the DGG value-map (arrow A: I_𝓑₃ → tr_M) continues the
index to tr_M values through the state-integral perturbative series. The
4₁ side is done; the Borromean side (the actual target) is open.

ROUTE (the honest one): saddle-point perturbation theory of the 𝓑₃
state integral (8 tetrahedra / 2 octahedra, 3-dim saddle) — the exact
2-loop Feynman-diagram expansion around the real saddle (𝓑₃ amphichiral
⇒ CS=0 ⇒ real saddle, shapes z∈{(1+i)/2,1+i}). Gives EXACT κ_n ∈ ℚ(i)·π^n
(Gaussian trace field, analogous to 4₁'s ℚ(√−3)). This is NOT a numerical
fit — the Borromean tower (N≤56, Habiro O(n³)) is too data-limited for κ₁.

ANTI-FABRICATION: do NOT guess the Feynman rules / the exact κ formulas.
Derive them from the state-integral perturbation theory (Dimofte, Ohtsuki)
or reuse/generalize the corpus's 4₁ saddle-perturbation machinery.

PREDICTION to test once computed: Borromean κ_n ∈ ℚ(i)·π^n with a definite
parity structure (odd/even in the amphichiral saddle).

ANCHORS already established (do not re-derive): Vol=8G (#4208/#4494),
NZ torsion=64 (#4253), saddle route (#4494), S₃ trivial + tr_M [2,1]
categorical (#4500). The value-map is scalar-to-scalar (S₃-corrected).
