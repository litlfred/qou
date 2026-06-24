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

## Yardstick-free follow-up — the real obstruction is saturation, not the phase

Removing the `k·B₂` yardstick entirely (the #2703 confound) and testing the **total
gap** `Gap = B_AME − B_joint^model` (`|χ|` joint trace, all bonds, no reference)
against `Σ|Δθ|`:

| atom | `B_AME` | `B_joint^model` | Gap | `Σ|Δθ|` | `Gap/Σ|Δθ|` |
|---|---:|---:|---:|---:|---:|
| ³H  | 8.48 | 3.25 | 5.23 | 8.22 | 0.636 |
| ³He | 7.72 | 3.47 | 4.25 | 8.49 | 0.500 |
| ⁴He | 28.30 | 3.80 | 24.49 | 17.23 | 1.421 |

`Gap/Σ|Δθ|` spread = **108%** — far *noisier* than the pairwise version. So removing
the yardstick makes it **worse**, and that exposes the real obstruction:

**`B_joint^model` is nearly A-independent (3.25 → 3.47 → 3.80 MeV) while `B_AME`
scales strongly (8.5 → 7.7 → 28.3).** The `|χ|` joint trace captures a *shrinking*
fraction of binding as A grows — 38% (³H), 45% (³He), **13% (⁴He)**. The
multiplicative deficit `1 − ∏f` **saturates** (exactly `productModel_3body_nonpos`):
summing per-bond gives 7.34 MeV for ⁴He but the joint product gives only 3.80, and
it barely moves with A.

**Reframing the whole thread.** The dominant missing binding is the **extensive
(A-scaling)** part, which **no saturating multiplicative trace can supply** — and the
q-Reeb phase does *not* supply it either (108% spread). The phase is at best a small
directional correction to the *intensive* per-bond residual; the large extensive
binding (and ⁴He's doubly-magic enhancement) is a separate, bigger gap. This points
squarely at the `z2bn` fibre-`R(q,x)` recurrence, whose **solution grows with A**
(the `Iν`-growth regime of the q-Bessel split) — an output of the kernel, not a
saturating product and not a fitted phase scale.

→ `computations/probes/yardstick_free_phase_binding_probe.py` ·
`computations/yardstick-free-phase-binding.witness.json`
