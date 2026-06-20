# Madelung from the confinement SDP + canonical T_ee — falsifiable test (negative, well-localised)

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Compute:** [`computations/madelung_sdp_filling_order.py`](../../computations/madelung_sdp_filling_order.py)
**Class:** falsifiable probe (formalize-first).

## Question

The confinement SDP **is** the many-body optimiser, so the electron filling
*order* should be its optimal active-set dressing sequence. Does running it with
the **canonical** electron–electron crossing `T_ee` reproduce the Madelung
(`n+ℓ`) order — the chemical noble gases `[2,10,18,36,…]` — or only the
hydrogenic / pure-2n² `[2,10,28,60]`?

## Result (predicted, then confirmed)

| step | input | closed shells |
|---|---|---|
| (1) | bare σ-tower radial `E(n) ∝ −λ₊⁻ⁿ` (ℓ-degenerate) | **`[2,10,28,60]`** (pure-2n²) |
| (2) | + canonical `T_ee` screening, **ℓ-independent** | **`[2,10,28,60]`** (unchanged) |
| (3) | + `c·ℓ` penetration (screening ↑ with ℓ) | moves off 2n² only for `c>0`; does not cleanly reach `[2,10,18,36]` |
| (3') | **structural** screening `∝ [2ℓ+1]_q` (angular q-dim, **canonical** s, no tuning) | `1s2s3s4s2p3p…` **ℓ-dominated**, `[8,26,46,60]` — overshoots |
| (4) | SDP `lp_dual_solver` primal `x*` | selects the min-cost orbital ✓ (gap 0) |

**The SDP optimiser is free (4):** `x*` picks the minimum-cost orbital, so the
filling *order* is exactly whatever the cost (screening) dictates — the whole
Aufbau machine is the SDP's active set swept over electron count.

**But the canonical `T_ee` does NOT give Madelung.** It is the *same* `σ`
crossing for every orbital, independent of angular momentum `ℓ`, so its screening
is ℓ-independent: it shifts all `ℓ` in a shell equally, gives **no ℓ-splitting**,
and the closed shells stay at the pure-2n² `[2,10,28,60]` — Ni(28), Nd(60), not
Ar(18), Kr(36).

## The missing ingredient, sharpened by the structural try (3'): it is the *balance*, not the *existence* of ℓ-penetration

The first read (steps 1–3) said "the bare `σ` crossing carries no ℓ-dependence."
The **structural try (3')** sharpens this. Using the orbital's own angular
q-dimension `[2ℓ+1]_q` (from the self-square `V_ℓ`) as the screening modulation,
with the **canonical** `T_ee` weight and **no tuning**:

- it **does** rise with `ℓ` — the **right penetration direction** (the structure
  *supplies* ℓ-penetration after all, via the angular q-dimension);
- but it **overshoots** badly: `s·[3]_q ≈ 0.76` against a radial spacing `≈ 0.09`
  — ~10×. The order collapses to **ℓ-dominated** (`1s 2s 3s 4s 2p 3p …`,
  closures `[8,26,46,60]`), not `n+ℓ`.

So the categorical structure supplies **both** ingredients — radial `n`
(σ-tower) **and** angular ℓ-penetration (the q-dimension, correct sign) — but
**not in the Madelung balance**. Madelung (`n+ℓ`, the `4s`/`3d` near-degeneracy)
needs the ℓ-splitting to be a *small fraction* of the radial spacing; QOU's
canonical `T_ee` is ~8× too strong for that delicate near-degeneracy. The open
question therefore sharpens:

> **Not "is there ℓ-penetration?" (there is) — but "why is the radial : angular
> SCALE BALANCE the `n+ℓ` one?"**

Pinning that ratio to land on `[2,10,18,36]` is **tuning** (fitting) — the
discipline-forbidden move, and even the canonical structural form does not hit it
on its own. (Consistent with Madelung being semi-empirical even in standard QM —
Cr, Cu, Pd, the lanthanides break it.)

## Bottom line for the owner's question

*"How much of the screening step do we need to show / do we get it from the SDP?"*
— **Most of it: the SDP gives the optimiser and the order-from-cost for free.**
What is **not** free, and is now the precise open item, is the **ℓ-penetration**
of `T_ee` (the `ℓ`-graded inter-electron coupling). That is the single categorical
piece between the SDP and the periodic table's *ordering* (Gap 2); the *capacity*
2n² (Gap 1) is the separate self-square result
([`2026-06-20-shell-2n2-from-self-square-no-second-su2.md`](2026-06-20-shell-2n2-from-self-square-no-second-su2.md)).
