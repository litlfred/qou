# Higher-colour does NOT rescue the WRT→`W_λ` route — the conjugation-symmetry foreclosure

**Date:** 2026-06-22
**Branch:** `claude/inspiring-albattani-ijfp7m` (PR #2608)
**Status:** Negative/structural — **resolves** the open object left by the 4-count refinement
([`2026-06-22-keystone-wrt-schurweyl-plancherel-4count.md`](2026-06-22-keystone-wrt-schurweyl-plancherel-4count.md)):
the higher-Wilson-line / colour-ℂ³ Schur–Weyl weighting is foreclosed for **all** colour dimensions.
No fit; structural foreclosure (a search prune), not a keystone closure.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-wrt-schurweyl-plancherel-4count.md`](2026-06-22-keystone-wrt-schurweyl-plancherel-4count.md)
**Script:** [`scripts/keystone_wrt_schurweyl_higher_colour_foreclosure_probe.py`](scripts/keystone_wrt_schurweyl_higher_colour_foreclosure_probe.py) (float64, exit 0)
**Witness:** [`computations/keystone-wrt-schurweyl-higher-colour-foreclosure.witness.json`](../../computations/keystone-wrt-schurweyl-higher-colour-foreclosure.witness.json)

## The question

The 4-count refinement showed that the WRT→`W_λ` route via *fundamental* SU(2) Schur–Weyl is
obstructed (ℂ² annihilates the (3,1,1) peak, #2364), and left the open object:

> derive the higher-Wilson-line / **colour-ℂ³** Schur–Weyl weighting and test whether it lands the
> q-Plancherel `W_λ` without a free parameter.

This note answers it: **no — for every colour dimension `d`.**

## The candidate weighting

From a ℂ^d arena, the natural "colour weighting" of an `H₅(q)`/S₅ block λ is its **gl_d-multiplicity**
in Schur–Weyl, `m_d(λ) = dim L^{gl_d}_λ = #SSYT(λ, entries ≤ d)` (q-deformed:
`s_λ(1,q,…,q^{d-1})`, the colour-multiplicity quantum dimension). Two defining properties of `W_λ` are
incompatible with `m_d(λ)` for **every** `d`.

### (1) Support — even ℂ³ is too small

| `d` | colour Schur–Weyl hosts |
|---|---|
| 2 | (5),(4,1),(3,2) — 3 blocks |
| 3 | + (3,1,1),(2,2,1) — 5 blocks |
| 4 | + (2,1,1,1) — 6 blocks |
| 5 | + (1⁵) — all 7 |

`m_d(λ) = 0` unless `rows(λ) ≤ d`. But `W_λ > 0` on **all 7** λ⊢5 (incl. (2,1,1,1) 4-row, (1⁵) 5-row).
So no `d < 5` even hosts `W_λ`'s support — **colour-ℂ³ still misses (2,1,1,1) and (1⁵)**.

### (2) Conjugation symmetry — the decisive obstruction (all `d`)

`W_λ = W_{λ'}` (Plancherel hallmark; `d_q(λ)=d_q(λ')` from transpose-invariance of the hook multiset).
But the colour-multiplicity is strongly conjugation-**asymmetric** at every `d`:

| pair λ / λ′ | `W_λ = W_{λ'}` | `m₅(λ)` vs `m₅(λ′)` |
|---|---|---|
| (5) / (1⁵) | ✓ equal | **126 vs 1** |
| (4,1) / (2,1,1,1) | ✓ equal | 224 vs 24 |
| (3,2) / (2,2,1) | ✓ equal | 175 vs 75 |

`m_d` favours the colour/production direction (the gl_d *dimension* peaks at (4,1); the
principal-specialization limit at the one-row (5)) — **never** the conjugation-symmetric Plancherel peak
(3,1,1). No `d` (finite or `→∞`) makes `m_d` symmetric, so **no colour weighting can equal `W_λ`**. Even
at `d = 5` (full support), the normalized colour weight vs `W_λ` is off by up to **2064 %**.

## Why — the two sides of Schur–Weyl

`V^{⊗5} = ⊕_λ L^{gl_d}_λ ⊗ S^λ_{H₅(q)}`. The WRT-colour data feeds the **gl_d / colour** side, whose
weight is the multiplicity `m_d(λ)` — the **principal-specialization / production** weight family
(the `y_λ` the [Plancherel-target doc](2026-06-16-keystone-plancherel-target-clarification.md) separated:
signed, peaks toward few rows). The Plancherel `W_λ = d_q(λ)²/[5]_q!` lives on the **symmetric / regular
pairing** (the *square* of the Markov quantum dimension), which is the `d → ∞` **full-Hecke** object —
conjugation-symmetric by construction.

So the WRT-colour Schur–Weyl functor lands the **production** weight, not the **Plancherel** target. They
are the framework's two distinct weight systems; the colour route maps to the wrong one.

## Relation to #2604 and the dual-sides capstone — strengthening, not contradiction

The merged [#2604 row-count split](2026-06-22-keystone-schurweyl-su2-rowcount.md) establishes the
**support** side: the SU(2) ≤2-row rule sends the muon (3,2) to the spin sector and the electron (3,1,1)
to colour, and its own table already lists (2,1,1,1)→SU(4), (1⁵)→SU(5). This note **continues** that
result on the **weight** side and sharpens its "colour sector ← SU(3)" headline:

1. **Support:** SU(3)/ℂ³ does not cover `W_λ`'s support — (2,1,1,1),(1⁵) need `d = 4, 5`; the minimal
   `d` hosting all of `W_λ` is **5** (consistent with #2604's table, sharper than its headline).
2. **Weight (the new constraint):** the natural colour weight — the gl_d **multiplicity** `m_d(λ)` — is
   conjugation-asymmetric and equals `W_λ` for **no** `d`; a colour route to `W_λ` cannot use the
   multiplicity, it must reproduce the **symmetric** measure `d_q(λ)²/[5]_q!`.

This does **not** refute #2604's "SU(N) **coloured-invariant**" path (a colored WRT/modular quantity is a
different object than the multiplicity `m_d`); it **constrains** it — whatever the coloured invariants
produce, to land `W_λ` they must reproduce the conjugation-symmetric Plancherel measure, intrinsically the
`d → ∞` full-Hecke object.

The on-main **dual-sides capstone** ([`…-schurweyl-dual-sides.md`](2026-06-22-keystone-schurweyl-dual-sides.md))
makes the adjacent point for the **`d = 2` spin sector** at the q-deformed level: the SU(2) quantum
dimension `[2j+1]_q` ≠ the Hecke `d_q`, so WRT and `W_λ` are Schur–Weyl *dual*, not equal. This
foreclosure is the **all-`d` generalization on the multiplicity side** — `m_d(λ)` (which is `[2j+1]` at
`d = 2`) ≠ `W_λ` for every `d`, with conjugation symmetry as the mechanism. The capstone eliminates the
`V_λ`-quantum-dimension candidate (`d = 2`); this eliminates the `V_λ`-multiplicity candidate (all `d`) —
together the two natural colour-side candidates for `W_λ` are closed.

## Net — the multiplicity route is foreclosed; the open object relocates

- The higher-colour escape via the **colour-multiplicity weight** (colour-ℂ³ or any ℂ^d) **does not
  rescue** the WRT→`W_λ` route. The obstruction is not "ℂ² is too small" but the structural mismatch
  **colour-multiplicity (production) ≠ Plancherel** (broken conjugation symmetry, all `d`).
- Reproducing `W_λ` requires the **symmetric pairing / full Markov quantum dimension squared**
  (`d_q(λ)²`, `d → ∞` full Hecke). Any surviving colour route (incl. #2604's coloured invariants) must
  meet that symmetric-measure constraint. This loops the keystone's geometric-realization object back to:
  - [#2406 — "no finite colour-SU(3) arena; the trace is the full-Hecke principal specialization"](2026-06-16-keystone-arena-is-full-hecke-not-su3.md), and
  - #2409 — the infinite-dim full-Hecke realization (the live attack on exactly that object).
- This is a forward (formalize-first) prune: it removes the finite-colour-**multiplicity** branch and pins
  the symmetric-measure constraint on the rest. Not a closure.

## Cross-checks (probe, no fit)

- colour multiplicities `m_d(λ)` reproduced as integer #SSYT (hook-content), all `d ∈ {2,3,4,5}`.
- support counts 3/5/6/7 for `d = 2/3/4/5`; `W_λ` support = 7 → `min d = 5`.
- conjugation asymmetry exhibited on all three conjugate pairs; `W_λ = W_{λ'}` to `< 10⁻¹²`.
- `d = 5` normalized colour weight vs `W_λ`: max rel Δ = **2064 %**.

## Cross-references

- [`2026-06-22-keystone-wrt-schurweyl-plancherel-4count.md`](2026-06-22-keystone-wrt-schurweyl-plancherel-4count.md) — the 4-count refinement this resolves.
- [`2026-06-16-keystone-plancherel-target-clarification.md`](2026-06-16-keystone-plancherel-target-clarification.md) — `y_λ` (production) vs `W_λ` (Plancherel).
- [`2026-06-22-keystone-schurweyl-su2-rowcount.md`](2026-06-22-keystone-schurweyl-su2-rowcount.md) — #2604, the on-main SU(2) row-count spin/colour split this continues (weight side).
- [`2026-06-22-keystone-schurweyl-dual-sides.md`](2026-06-22-keystone-schurweyl-dual-sides.md) — the on-main dual-sides capstone (`d=2` `[2j+1]_q ≠ d_q`); this foreclosure is its all-`d` multiplicity-side generalization.
- [`2026-06-16-keystone-arena-is-full-hecke-not-su3.md`](2026-06-16-keystone-arena-is-full-hecke-not-su3.md) — #2406, the full-Hecke object the route relocates to.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the keystone ledger.
