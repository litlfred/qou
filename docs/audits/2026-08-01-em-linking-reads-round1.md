# EM-linking invariant — round-1 reads (bean qou-o6ml)

**Date:** 2026-08-01. Reads of the uploaded EM-linking literature batch
(`be8fe53f`) against the κ(A) gate (3.2 → 2.1–2.3, from
`em-linking-invariant-scoping.witness.json`). Two parallel readers;
upload-quality problems found — see the re-upload list at the end.

## The keeper results

**1. The Milnor integral IS a mutual-energy integral** (DGKMSV,
"Pontryagin invariants and integral formulas for Milnor's triple
linking number", read in full). For a Brunnian 3-component link
(pairwise linkings zero — exactly the corpus baryon regime), Milnor's
μ̄₁₂₃ equals **the helicity of the characteristic field** `v_L` on the
parameter 3-torus:

- μ(L) = ½ ∫_{T³×T³} v_L(x) × v_L(y) · ∇φ(x−y) — a two-point
  Biot–Savart mutual-energy double integral (their Thm B(2)); φ = the
  torus Green's function. Also a Fourier form (Thm B(3)) that is
  directly computable — their Borromean model integrates to μ ≈ −0.97
  vs the exact −1 at coarse resolution.
- **Per-pair decomposition exists**: the characteristic map normalizes
  `F = (x,y)₊ + (y,z)₊ + (z,x)₊` — an additive sum of *pair* terms,
  coupled only through the normalization. And their asymmetric map
  `h_L` is literally "a pairwise Gauss map modulated by the third
  curve" — the cleanest structural hook for a *per-pair energy inside
  a triple invariant*, which is what the two-like-charge invariant
  needs (a pp-pair energy that exists only because the third strand
  closes the Brunnian structure).
- Caveat kept honest: the paper's integrals produce the topological
  ±1, nothing A-dependent — **κ(A) must come from QOU-side structure**
  (the per-pair blocks of F under the corpus braid closure, or the
  hyperbolic kernel below), not from these formulas alone.

**2. The hyperbolic per-pair kernel exists and decays exponentially**
(DeTurck–Gluck, partially recovered §48–56): explicit Biot–Savart /
linking kernels on H³ of csch/coth class — `φ(α) ~ csch α ≈ 2e^{−α}` —
replacing 1/r². Three structural bonuses for the QOU fibre:
exponential decay makes the descent to a **compact hyperbolic
quotient** convergent (Poincaré series) and kills the H³ Green-operator
non-uniqueness (discrete spectrum); pair-interaction strength falling
exponentially with hyperbolic separation is a *natural mechanism for
an A-dependent factor* — the right shape for κ(A); and their kernel
φ₃ "involves dilogarithms" — direct contact with the corpus Li₂/Li₂^q
machinery.

## Upload-quality problems (blocking full fidelity)

| file | expected | actually contains |
|---|---|---|
| `0808.1533v3.pdf` | Komendarczyk, third-order helicity | duplicate of DGKMSV 1101.3374 |
| `1101.0956v3.pdf` | DGKMSV, generalized Gauss maps | Arcuş (Lie algebroids, unrelated) ×2 + orphaned tail pages (§48–56) of DeTurck–Gluck |
| `0510388v1.pdf` | DeTurck–Gluck electrodynamics | mixed/corrupted; only tail pages recovered |

**Re-upload list** (verified IDs): DeTurck–Gluck is
**arXiv:math/0406276** (not 0510388); the generalized-Gauss-maps pair
is **arXiv:0901.1612** (announcement) + **arXiv:1207.1793** (Part 2,
Euclidean case); the Komendarczyk third-order-helicity papers (Comm.
Math. Phys. 291 (2009); J. Math. Phys. 51 (2010)) carry the
Freedman–He-style **energy lower bounds for Borromean flux tubes** —
the single most gate-relevant missing item.

## Next attack step (when re-uploads land)

Combine: per-pair block of F (keeper 1) × hyperbolic kernel on the
compact fibre (keeper 2) → a candidate per-pair energy whose
A-dependence comes from hyperbolic separation of the colour tubes;
test against κ(A) before anything else. Full text extracts of the
readable material survive in the session scratchpad.
