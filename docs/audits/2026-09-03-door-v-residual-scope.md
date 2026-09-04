# The Door-v residual is not full alternation — and the block that says so had the wrong reason

**Date:** 2026-09-03 · **Bean:** `qou-o2n6` · follows `qou-60ew` (#6498) and `qou-4g01` (#6474)
**Lean:** `QOU.Mass.GGMAlternationOnset` (new, sorry-free, ordered field) + three theorems added to
`QOU.Mathlib.RamifiedShiftCalculusSum` (sorry-free, generic `CommRing`)
**Probe:** [`door_v_residual_scope_probe.py`](../../computations/probes/door_v_residual_scope_probe.py) (exit 0; mpmath 60 dps for the one numerical question, symbolic `q` elsewhere)

## The question

#6498 proved *residue and residual are mutually exclusive* for derivative-like sums of shifts
≤ 2 — but under the hypothesis that the jet tower carries the full `(−1)^n` alternation at
**every** level. Its own "Honest gap" asked whether the corpus's Door-v residual is that strong.
This bean measured it. **It is not, and the exclusivity does not reach the low body orders.**

## What the corpus's residual is

`conj:c1-ggm-bar-parity-faces`: the residual is the sign alternation of the growing solution of
the GGM carrier `y_{m+2} − (2 − q^{m+1}) y_{m+1} + y_m = 0`, read **at the level of modules, up to
gauge** — the block explicitly excludes the scalar reading. And it is **asymptotic**: the block
notes the coefficient `2 − q^{m+1}` is positive for `m + 1 < log 2 / log q`.

## Three findings

### 1. The block's stated reason is false; its conclusion survives with a sharper reason

The block says that while the coefficient is positive "no sign change occurs". A three-term
recurrence with coefficient in `(0, 2)` is **oscillatory** — every solution changes sign.
Measured at the proton `q₀` on six generic initial data: **2–3 sign changes inside the window
`m ≤ 5`** in every case (e.g. `y₀ = y₁ = 1` gives `1, 1, −0.11, −1.08, −0.58, 0.81, 0.83, …`).

What **is** true, for every solution and without reference to initial data:

| coefficient sign | consequence | Lean |
|---|---|---|
| `c > 0` | a flip is followed by a same-sign pair — no two consecutive flips | `no_double_flip_of_pos`, `ggm_solution_no_double_flip` |
| `c < 0` | a same-sign pair is followed by a flip | `flip_after_same_of_neg` |
| `|a| < −c·|b|` | a flip persists — the asymptotic `(−1)^m` never stops | `flip_persists_of_lt` |

One-line algebra: `y_{m+2} y_{m+1} = c·y_{m+1}² − y_m y_{m+1}`. This is exactly what the block's
argument needs — same-sign consecutive pairs exist in the window, so the `(−1)^m` twist creates
flips there and the non-negativity obstruction fires on the twisted sequence too. The block's
conclusion (scalar reading excluded) stands; its premise is corrected in place, not deleted.

### 2. The #6498 hypothesis is unsatisfiable by the corpus's carrier

`ggm_full_alternation_forces`: alternation at every level forces `2 ≤ q^{m+1}` for every `m`;
`ggm_full_alternation_impossible_of_lt_two`: at any `q < 2` — every physical substrate value —
**no solution of the GGM recurrence alternates at every level**; it fails already at `m = 0`.
So `twoOp_residual_kills_residue` (#6498) cannot be fed by the Door-v residual as measured.

At the proton `q₀ = 1.10998…`: `log 2 / log q₀ = 6.643`; the coefficient turns negative at
`m = 6`; persistent strict alternation of the growing solution sets in at **`m = 11…14`**,
depending on the initial data (six measured: 14, 11, 12, 12, 11, 13).

### 3. The exclusivity survives, level by level, above the window

`residual_from_level_tower_is_odd_part`: alternation demanded only for `n ≥ n₀` still forces the
tower to be the odd part's from `n₀` on. `shiftOne_iterate_residue_zero_of_two_le`: a shift-1
derivative iterate of length ≥ 2 has a dead residue slot for **every** seed (the `i = 1` factor is
`c₁(−1) = 0`; the #6474 seed hypothesis is needed only for lengths 0 and 1 — probe (2) shows a
Laurent seed is alive there and dead beyond). Hence `twoOp_residual_from_level_kills_residue_beyond`:

> the residue is dead at every level `≥ n₀ + 2`, and levels `2 … n₀ + 1` keep the #6498 formula
> `c₁(−2) c₂(−1) · (Dⁿ f)(1)` — alive on a generic seed (probe (3): levels 2–7 nonzero).

With `n₀ ≥ 6` at `q₀` (and `≥ 11` for persistent alternation), **the residue and the residual
coexist at jet levels 2 … 7 at least** — under the conjecture's own identification jet degree =
body order, that is the deuteron through the `A = 7` terms, the whole light-nucleus window.

## Consequence for W1

The #6474 conclusion "odd shift **and** a non-derivative component" was extended to sums in
#6498 by the residual route. That extension holds only **above the window**. At the low body
orders a mixed-shift `D_q` built from derivatives alone (shift 1 + shift 2, both annihilating
constants) is **not excluded** by anything in the corpus: it has a live residue, and the
residual it must carry is not yet demanded there. The odd-shift requirement stands everywhere
(a pure even sum is dead at every level). `D_q` is not constructed.

## What is still open (bean body carries it)

- Jet level `n` = GGM index `m` rests on the conjecture's "jet degree = body order"; recorded,
  not checked.
- The corpus residual is a sign pattern of one scalar per level, read up to gauge; the shift
  calculus consumes an eigen-relation of the whole coefficient function per level. The
  from-level form closes the *asymptotic* gap; the scalar-vs-eigenfunction gap is a modelling
  choice this tranche does not settle.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/door_v_residual_scope_probe.py
```
