# The keystone link is Schur–Weyl DUALITY, not a `WRT = W_λ` identity — the deflationary capstone

**Date:** 2026-06-22
**Branch:** `claude/keystone-schurweyl-dual-sides-2026-06-22`
**Status:** Positive/deflationary — an exact two-sided computation that closes the
"`WRT(S³/2I) = W_λ`" hope: the two are Schur–Weyl *dual*, not equal. No fit.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-schurweyl-su2-rowcount.md`](2026-06-22-keystone-schurweyl-su2-rowcount.md)
**Script:** [`scripts/keystone_schurweyl_dual_sides_probe.py`](scripts/keystone_schurweyl_dual_sides_probe.py)
**Witness:** [`computations/keystone-schurweyl-dual-sides.witness.json`](../../computations/keystone-schurweyl-dual-sides.witness.json)

## The spin-sector realisation attempt, and what it found

The natural next step after the row-count split was: *does the SU(2)/WRT modular weight of a 2-row
block reproduce `W_λ`?* Computing **both sides** of Schur–Weyl `(ℂ²)^{⊗n} = ⊕_{λ:≤2 row} S^λ ⊗ V_λ`
answers it — sharply, and deflationarily.

| λ | spin j | Hecke `d_q(λ)` (S_n side) | SU(2) `[2j+1]_q` (V_λ side) | equal? | `f^λ` | `W_λ` |
|---|--------|---------------------------|------------------------------|--------|-------|-------|
| (5) | 5/2 | 1.0 | 6.38809 | **NO** | 1 | 0.00762 |
| (4,1) | 3/2 | 4.10968 | 4.10968 | yes | 4 | 0.12862 |
| **(3,2)** | 1/2 | **5.22044** (`=[5]_q`) | **2.01090** (`=[2]_q`) | **NO** | 5 | 0.20754 (muon) |

The corpus `W_λ = d_q(λ)²/[n]_q!` is built from the **Hecke / S_n-side** hook-content q-dimension
`d_q(λ)`. The WRT(S³/2I) modular data is the **SU(2) / centralizer-side** quantum dimension
`[2j+1]_q`. **These are different numbers** (they coincide only accidentally at (4,1)): the muon block
(3,2) has Hecke `d_q = [5]_q ≈ 5.22` but SU(2) spin-1/2 dimension `[2]_q ≈ 2.01`.

## The verdict — Schur–Weyl duality, full stop

A direct `WRT(S³/2I) = W_λ` equality is a **category error**: the WRT lives on the SU(2) (`V_λ`) side,
`W_λ` lives on the Hecke (`S^λ`) side. The two are **Schur–Weyl dual** — *paired* by
`(ℂ²)^{⊗n} = ⊕ S^λ ⊗ V_λ`, but **not equal**. The Poincaré sphere is the icosahedral **selector** of
the modular data (confirmed earlier: the E₈ residues `{1,11,19,29}`), but the `W_λ` *numbers* are the
**dual S_n-side q-dimensions** — there is **no closer `WRT = W_λ` identity to be had at the level of
weights.**

This is the honest terminus of the WRT line of attack: it explains *why* every step found the link
"structural, not numerical" — the objects sit on opposite sides of a duality.

## The keystone arc — final assessment (critical-distance)

The open object was driven, this session, through a long chain — Sasakian → modular block weights →
non-compact `E_q(2)` → Habiro-WRT(Σ(2,3,5)) → colour-resolution → Schur–Weyl row-count → **dual-sides**.
Honest summary of what was and was not achieved:

- **Genuine, exact gains:** the finite-Sasakian arena was ruled out and the object relocated to
  representation theory; the geometric angles were made explicit (the exact φ pin, Lean-verified); the
  `W_λ` were reproduced; the WRT q-series was made operational; and the WRT↔`W_λ` relation was
  **identified as Schur–Weyl duality** (this doc). None fitted; nothing wired.
- **What was NOT achieved:** no closure of `conj:s5-so3-fiber-action`, no numerical mass prediction.
  The chain *clarified* the object thoroughly but **terminates in a duality, not an equation** — the
  WRT data does not *compute* `W_λ`, it is *dual* to it.
- **Standing caveats (unresolved):** the muon/electron spin/colour split is a consequence of the
  *posited* home-block assignment (not independent support for it), and its non-monotone relation to
  the mass ordering (lighter electron = colour, heavier muon = spin) has **no clear physical reading**.

**Net:** the keystone's `W_λ`-origin question is now well-understood structurally — it is the
Hecke-side weight of a Schur–Weyl pair whose SU(2) side the Poincaré-sphere WRT selects. A genuine
*closure* (a derived mass relation) would need a mechanism on top of this duality that the corpus does
not yet have; the WRT line, pursued to its end, does not supply one. A clean, honest place to rest.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-keystone-schurweyl-su2-rowcount.md`](2026-06-22-keystone-schurweyl-su2-rowcount.md) — the row-count split this completes.
- [`2026-06-22-keystone-habiro-wrt-s3-2i.md`](2026-06-22-keystone-habiro-wrt-s3-2i.md) — the WRT q-series (the SU(2)-side object).
- [`2026-06-22-keystone-modular-category-identification.md`](2026-06-22-keystone-modular-category-identification.md) — the non-compact `E_q(2)` identification.
