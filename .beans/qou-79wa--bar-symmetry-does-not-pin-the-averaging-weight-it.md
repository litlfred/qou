---
# qou-79wa
title: 'Bar symmetry does not pin the averaging weight: it admits the family q^-k/[2]_{q^k}, and the corpus assumes k=0'
status: completed
type: task
priority: normal
created_at: 2026-09-05T09:22:47Z
updated_at: 2026-09-05T09:26:15Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Owner: "derive the
averaging rule". The answer is that **it cannot be derived from its own stated
justification** — bar invariance leaves a one-parameter family, and the corpus
picks a member by an unstated assumption.

## The invariance condition, derived here from scratch

Under `q -> 1/q` the bracket `[2]_q` is FIXED while `b_pp = q^2/[2]_q` and
`b_nn = q^-2/[2]_q` SWAP. So with `f_pn = w.b_pp + (1-w).b_nn`,

    f_pn(1/q) = wbar.b_nn + (1-wbar).b_pp
    f_pn(q)   = w   .b_pp + (1-w)   .b_nn

and `f_pn(1/q) = f_pn(q)` reduces to `(1 - wbar - w)(b_pp - b_nn) = 0`, hence

    wbar = 1 - w        for q != 1

**One equation. Not a determination.** (Stated explicitly so it can be checked
rather than taken on trust — it is the load-bearing step.)

## The family that satisfies it

    w_k = q^-k / [2]_{q^k}      has     wbar_k = q^k/[2]_{q^k} = 1 - w_k

for EVERY `k`. Verified at `k = 0, 0.5, 1, 1.5, 2, 3, 4, 6` to 1e-35, and proved
for all real `k` in Lean.

| k | w_k | delta | |
|---:|---:|---:|---|
| **0** | **0.500000** | **-0.02161775** | wrong — **the corpus** |
| 0.5 | 0.473938 | -0.01083792 | wrong |
| **1** | **0.448018** | **0** | the geometric mean, neutral |
| 1.5 | 0.422377 | +0.01083792 | SEMF |
| **2** | **0.397148** | **+0.02161775** | SEMF |
| 3 | 0.348408 | +0.04277804 | SEMF |

`delta(w_k)` vanishes at exactly `k = 1` and is **odd about it** — so the
corpus's `k = 0` has `k = 2` as its exact mirror, `-0.021618` against
`+0.021618`. Same reflection the power means show about the geometric mean, now
inside a family that is bar-invariant throughout.

## So what actually pins k = 0?

Not bar symmetry. The unstated extra assumption that **`w` carries no `q`** —
an undeformed bracket inside a deformed algebra. That is the same defect
`qou-i01a` found as a consequence (`w - w*` is 151x deformation to flavour);
here it is located in the premise.

## What is derived, and what is NOT

**Derived:** `wbar = 1 - w`; that the family meets it for all `k`; `w_k` strictly
decreasing in `k` for `q > 1`; `w_1` is exactly the crossing; hence the **bound
`delta > 0 <=> k > 1`**.

**NOT derived: `k`.** `k = 2` gives the SEMF sign and is deliberately **not**
adopted on that basis — a target to check a derivation AGAINST, never a
criterion to search ON.

**The one member with an independent argument is `k = 1`**, which uses the
framework's own bracket `[2]_q` and returns the loop value `1/[2]_q` exactly.
It gives **zero** symmetry term, not the SEMF one. Reported rather than skipped
past: the principled member is neutral, and the SEMF-signed members have no
principle yet.

## Artifacts

`content/quantum-observable-universe/lean/QOU/Hecke/BarWeightFamily.lean`,
registered in `QOU.lean`: 4 decls (`bar_weight_bar_eq_one_sub`, `weight_zero`,
`weight_one`, `weight_strictAnti`), all `[propext, Classical.choice,
Quot.sound]`, `lean`-direct exit 0.
`computations/qbeta/qbeta_bar_weight_family_probe.py` (7/7, 40 dps,
float64-guard clean).

**Successor:** derive `k`. It is now a single scalar with a derived admissible
region (`k > 1` for the SEMF sign) and two named landmarks (`k = 0` undeformed,
`k = 1` the framework's own bracket). That is a much smaller target than "derive
the averaging rule".


## 2026-09-05 (later) — `k` enumerated: only k = 0 and k = 1 have arguments

`qou-yf02`. The successor this bean named is answered as far as it can be: `k`
is not derived, but the candidates are now enumerated and the SEMF-signed region
is empty of them.

- `w_k = 1/(q^{2k}+1) = 1/(1 + (b_pp/b_nn)^(k/2))` — `k/2` is the bond-ratio power.
- `f_pn(k) = [2]_{q^(2-k)}/([2]_q [2]_{q^k})`, and `f(k).f(2-k) = 1/[2]_q^2`,
  which is WHY `delta` is odd about `k = 1`.
- `k = 0` derived (undeformed) → wrong sign; `k = 1` derived (the interface IS
  the loop value, and the unique fixed point of the reflection) → **zero**;
  `k > 1` → SEMF sign, **no member with an argument**.
- The corpus with its flavour split sits at `k = -0.00659`, i.e. negative.

**Derivable prediction: `k = 1`, no symmetry energy from this channel.**
