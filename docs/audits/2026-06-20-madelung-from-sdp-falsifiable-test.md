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
| (4) | SDP `lp_dual_solver` primal `x*` | selects the min-cost orbital ✓ (gap 0) |

**The SDP optimiser is free (4):** `x*` picks the minimum-cost orbital, so the
filling *order* is exactly whatever the cost (screening) dictates — the whole
Aufbau machine is the SDP's active set swept over electron count.

**But the canonical `T_ee` does NOT give Madelung.** It is the *same* `σ`
crossing for every orbital, independent of angular momentum `ℓ`, so its screening
is ℓ-independent: it shifts all `ℓ` in a shell equally, gives **no ℓ-splitting**,
and the closed shells stay at the pure-2n² `[2,10,28,60]` — Ni(28), Nd(60), not
Ar(18), Kr(36).

## The missing ingredient, precisely localised: ℓ-penetration

The closures move off 2n² **only** when screening **rises with ℓ** (step 3) —
i.e. the **penetration** asymmetry (low-ℓ orbitals penetrate the core, are
screened less, bind tighter). The bare `σ` crossing does not carry that
ℓ-dependence. So the open question is sharp and categorical:

> **Where does ℓ-penetration live — how does an orbital's angular momentum `ℓ`
> modulate its `T_ee` coupling to the inner core?**

This is *not* a separate many-body screening theory (the SDP already is that);
it is one missing structural input — an ℓ-graded electron–electron coupling.
Note: tuning a `c·ℓ` term to hit `[2,10,18,36]` would be **fitting**, not a
derivation, and even a crude `c·ℓ` does not cleanly reproduce Madelung — fitting
with the noble gases as the loss is exactly the discipline-forbidden move.
(Consistent with Madelung being semi-empirical even in standard QM — Cr, Cu, Pd,
the lanthanides break it.)

## Bottom line for the owner's question

*"How much of the screening step do we need to show / do we get it from the SDP?"*
— **Most of it: the SDP gives the optimiser and the order-from-cost for free.**
What is **not** free, and is now the precise open item, is the **ℓ-penetration**
of `T_ee` (the `ℓ`-graded inter-electron coupling). That is the single categorical
piece between the SDP and the periodic table's *ordering* (Gap 2); the *capacity*
2n² (Gap 1) is the separate self-square result
([`2026-06-20-shell-2n2-from-self-square-no-second-su2.md`](2026-06-20-shell-2n2-from-self-square-no-second-su2.md)).
