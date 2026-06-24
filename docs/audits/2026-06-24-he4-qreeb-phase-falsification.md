# ⁴He falsification of the q-Reeb-phase / pairwise-deficit relation

**Date:** 2026-06-24
**Branch:** `claude/he4-qreeb-phase-falsification-2026-06-24`
**Tests:** the PR #2681 relation `D / Σ|Δθ| ≈ 0.206 MeV/rad` (A=3, T+³He, N=2).

## The test

PR #2681 found that the A=3 pairwise leading-trace deficit `D` and the q-Reeb
rotation-phase magnitude `Σ|Δθ|` co-vary at `0.206 MeV/rad` (5.4% spread, T+³He),
and stated the falsifiable prediction: ⁴He (`Σ|Δθ| = 17.233` rad) should show
`D₄He ≈ 0.206 × 17.233 ≈ 3.56 MeV`.

Computed with the **same machinery**, now on the canonical ⁴He braid
`atom_braid_word_3A(2,2)` (47 crossings on H₁₂, 3 adjacent interfaces at gens
2/5/8 = pp/pn/nn), `|χ|` combiner over the H₁₂ joint trace, **0 fit**:

| quantity | value |
|---|---:|
| per-bond binding (gen 2 / 5 / 8) | +2.024 / +2.442 / +2.876 MeV |
| `B_pair` model (3 adjacent bonds) | +7.342 MeV |
| `pair_target` = 6·B₂ (tetrahedron, 6 pairs) | +13.347 MeV |
| **observed D₄He** | **+6.006 MeV** |
| **predicted D₄He** (0.206 × 17.233) | **+3.559 MeV** |
| `D/Σ|Δθ|` observed | 0.349 MeV/rad |

**Verdict: the constant-scale relation is FALSIFIED at ⁴He** — observed `D/Σ|Δθ|`
= 0.349 vs the A=3 mean 0.206, a **+69%** jump.

## What survives, what doesn't (scope-(a), not structural exclusion)

This is a **scope-limited (a) negative** per the refuted/ruled-out discipline — the
*constant-scale linear* relation, as-is, does not extend to ⁴He. It does **not**
exclude the q-Reeb phase as a magnitude ingredient. Specifically:

- **Falsified:** the *constant* `0.206 MeV/rad` conversion. The scale grows with A
  (T 0.201 → ³He 0.212 → ⁴He 0.349 MeV/rad).
- **Survives:** the **directional** correlation — larger phase, larger deficit
  (`Σ|Δθ|`: 8.22 → 8.49 → 17.23; `D`: 1.65 → 1.80 → 6.01). The q-Reeb phase still
  tracks the missing binding, just not at a fixed scale.
- **Robust (yardstick-free):** per-bond model binding is **deuteron-scale and
  uniform across all of T/³He/⁴He** (2.0–2.9 MeV/bond) — the leading-trace per-bond
  binding is not the problem at any A.

## Two confounds that make this a soft falsification

1. **⁴He is doubly magic** (`B_AME = 28.30 MeV ≫ 6·B₂ = 13.35`) — the `n_pairs·B₂`
   yardstick is on its *weakest* footing exactly here, so part of the +69% is the
   yardstick, not the q-Reeb identification.
2. **The pairs/bonds inflation grows with A.** The yardstick counts `n_pairs`
   (A=3: 3, A=4: 6) while the chain model carries `n_adjacent_bonds` (A=3: 2,
   A=4: 3). The pairs/bonds ratio rises 1.5 → 2.0, mechanically inflating ⁴He's
   target relative to A=3. This alone could account for much of the scale jump.

## Net

The N=2 A=3 coincidence `0.206 MeV/rad` was **not** a universal constant — the
falsification test did its job. The q-Reeb phase remains a *directional* correlate
of the missing binding (consistent with #2612), but **not** a fixed-scale magnitude
source, and the `k·B₂` yardstick demonstrably breaks at a magic nucleus. The
productive next step is yardstick-free: test the phase→binding map against `B_AME`
directly with a derived (not `k·B₂`) pairwise reference, or hand to the `z2bn`
fibre-`R(q,x)` derivation where the A-scaling is an output, not an assumption.

→ `computations/probes/he4_qreeb_phase_falsification_probe.py` ·
`computations/he4-qreeb-phase-falsification.witness.json`
