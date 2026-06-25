# Spectral-bridge calibration: the `→ λ₊` convergence is tautological — the physical `lw` sequence is super-geometric (z2bn lever-1)

**Date:** 2026-06-25
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)`)
**Reconciles:** the spectral-bridge deliverable ([PR #2718](https://github.com/litlfred/qou/pull/2718),
`docs/audits/2026-06-24-binding-recurrence-spectral-bridge.md`) ↔ the recurrence-falsification
([PR #2708](https://github.com/litlfred/qou/pull/2708),
`docs/audits/2026-06-24-lever1-lw-depth2-recurrence-falsified.md`) — two same-day, same-lever
results that are in direct tension and do not cross-reference each other.
**Scope:** (a)-scope re-calibration of an over-claim; **not** a refutation. The qualitative
conclusion stands and is *reinforced*; the Lean is correct and untouched.

## The tension

Both artifacts are individually correct on their own numbers, but the spectral bridge tabulates a
sequence it presents as the physical body-order binding coefficients `a_D⁽ⁿ⁾`, while the
falsification shows those very coefficients diverge from it:

- **Spectral bridge** (`binding-recurrence-spectral-bridge.witness.json`) lists
  `aD_sequence_2_to_9 = 1, 1.337, 2.533, 5.356, 11.619, 25.346, …` with `growth_ratios → λ₊ = 2.1846`,
  and asserts `ratio_convergence` as a **passed, "Empirical (non-tautological) … tests the actual
  a_D⁽ⁿ⁾ sequence"** check (producer comment, `binding_recurrence_spectral_bridge_probe.py:106-108`).
- **Falsification** computes the physical selection-rule values directly,
  `a_D⁽ⁿ⁾ = lw(n−1)`, `lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q(λ)`, and gets
  `1, 1.337, 2.533, 5.376, 13.560, 37.368, …` with ratios `1.34 → 2.76` **increasing** (super-geometric).

The bridge's `5.356 = τ·2.533 − 1.337`: its `aD_sequence` is the **iterated fixed-τ recurrence**
`a_{n+2} = τ·a_{n+1} − a_n` seeded by the 3 anchors, **not** the physical `lw` values. The two
agree only on the seed (`n ≤ 4`); past it they diverge. Any depth-2 recurrence with `τ > 2`
converges to `λ₊` by construction, so `ratio_convergence → λ₊` is **tautological** — it tests the
quadratic the probe used to define `λ₊`, not the physics. The producer's comment claiming the
opposite is the locus of the over-claim.

## Independent verification (float64, neither prior probe trusted)

Recomputed `lw(c)` from q-hook lengths and the iterated recurrence from the same seed
(`q₀ = 1.10997858275`; symmetric `[k]_q`, `dim_q(λ) = [n]_q!/∏_{cells}[hook]_q`; validated against
the corpus closed forms `lw(2) = (q+1)²/(3q)`, `lw(3) = Family-A`):

| `n` | physical `lw(n−1)` (q-hook, = #2708) | iterated fixed-τ (= #2718 witness) | divergence |
|---|---:|---:|---:|
| 4 | 2.532780 | 2.532780 | 0.000 % |
| 5 | 5.376138 | 5.355617 | **0.382 %** |
| 6 | 13.559827 | 11.618829 | **14.31 %** |
| 7 | 37.367807 | 25.345817 | **32.17 %** |

physical ratios `lw(c)/lw(c−1)` = `1.337, 1.894, 2.123, 2.522, 2.756` — past `λ₊ = 2.1846` by `n = 6`
and still rising. The #2708 residuals `lw(c+1) − (τ·lw(c) − lw(c−1))` = `+0.0205, +1.887, +6.914`
reproduce exactly. So the bridge's tabulated sequence is the recurrence's own output, and the
physical binding coefficients run *away* from it — faster, not slower.

## Honest (a)/(b) reconciliation

- **Qualitative conclusion — CONFIRMED and reinforced (not refuted).** "The binding is *extensive*
  (A-scaling), not saturating like the `|χ|` joint trace (`λ_eff ≈ 1`)" is correct: the physical
  ratios are `> 1` and *rising*. Super-geometric growth is *more* extensive than the bridge's
  geometric `λ₊`, so the bridge's headline answer to PR #2703's "what supplies extensive binding?"
  survives — strengthened.
- **Quantitative claim — re-scoped to (a).** `λ₊ = 2.185` is **not** "the binding growth rate" and
  the `→ λ₊` convergence is **not** an empirical property of `a_D⁽ⁿ⁾`. The physical rate is variable
  and exceeds `λ₊` by `n = 6`. `λ₊ > 1` is a correct-but-weaker **witness of extensivity from the
  seed kernel only** — the fixed-τ depth-2 kernel *under-counts* the true growth (#2708's
  `(b)`-exclusion: `lw` is not `A·λᶜ + B·λ⁻ᶜ` for any fixed `λ`; window-`τ` drifts
  `2.6424 → 2.6505 → 2.9933`). **This `(b)`-exclusion is now Lean-formalized sorry-free** —
  `QOU/Mass/Lever1Depth2Exclusion.lean` (PR #2764), `depth2_no_fixed_tau : ∀ τ, ¬(seed ∧ next)`
  at `q = 1` (seed forces `τ = 21/8`, the `c = 4` check needs `26/5`, residual `−7/240 ≠ 0`). The
  present finding is its **spectral-bridge complement**: the bridge that appeared to *validate* the
  fixed-τ kernel did so tautologically — it iterated that very kernel.
- **Lean is correct and unchanged.** `QOU/Mass/BindingRecurrenceSpectral.lean`
  (`lambdaPlus_isRoot`, `lambda_product_eq_one`, `lambdaPlus_gt_one`: `τ > 2 ⇒ λ₊ > 1`) is pure,
  unconditional algebra about the roots of `x² − τx + 1`. It states a true **conditional** (*if* the
  binding genfun had this fixed-τ kernel, *then* extensive). Only its docstring's implication that
  the kernel describes the physical sequence is tightened here.

## Stale witness caveat (separate, pre-existing)

`binding-recurrence-spectral-bridge.witness.json` `caveats[0]` still asserts the magic-A ⁴He +5.87 %
"is a finite-truncation residual of the geometric series" — the over-claim the bridge's **own audit
retracted** the same day (`2026-06-24-binding-recurrence-spectral-bridge.md:60-67`, cross-ref
`2026-06-24-magic-a-truncation-overclaim-correction.md`). The producer prose (comment + caveat +
description) is corrected on this branch. **Correction (2026-06-25): the witness regen is runnable
here, not a full-env follow-up.** This probe is pure `mpmath`/`sympy` (no `pyhecke_native`), and
`mpmath` pip-installs (PyPI reachable, verified) — so it carries **none** of the ct80-class
`mpf → f64` regression risk (that risk is specific to `pyhecke_native`-dependent producers, and
that wheel is *not* on PyPI). The regen merely propagates the corrected framing strings; the witness
*numbers* are already correct.

## What to do next (no closure; redirects the lever)

The honest continuations are #2708's two, unchanged:

1. **Drop `a_D = lw` beyond the seed** — compute the genuine prolonged periods of the abelianised
   `λ_SW` connection on the coral `E_q`; `lw` is then only the `c = 1,2,3` physical anchors.
   *(Owner **lifted** this gate 2026-06-25, PR #2764 — the coral `E_q` `λ_SW` holonomy `τ`-derivation
   is now in-scope; formalize-first, no-fit guard. Numerical elliptic-period integration may suffice
   without full Sage.)*
2. **Keep `a_D = lw`, drop depth-2-constant** — `B` is then a variable-kernel `q`/`n`-dependent
   object (consistent with super-geometric growth), forfeiting the clean `τ = 2cosh θ` rapidity.

**Producer enhancement (runnable here — pure `mpmath`/`sympy`):** have
`binding_recurrence_spectral_bridge_probe.py` also emit the *physical* `lw` sequence beside the
iterated one and assert the divergence honestly (reference algorithm: this audit's q-hook recompute),
so the witness shows the comparison rather than only the tautological tail. No fit; nothing wired;
no tier change. Owner closes the bean (§4a).

→ probes: `binding_recurrence_spectral_bridge_probe.py` (#2718) ·
`computations/substrate/lever1_lw_depth2_recurrence_test.py` (#2708) ·
`QOU/Mass/BindingRecurrenceSpectral.lean`
