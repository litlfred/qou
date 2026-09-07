---
# qou-yf02
title: 'Derive k: only k=0 and k=1 have arguments, and neither gives the SEMF sign'
status: completed
type: task
priority: normal
created_at: 2026-09-05T09:39:11Z
updated_at: 2026-09-05T09:42:36Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Owner: "derive k",
following `qou-79wa` which reduced the averaging rule to this one scalar.

**Result: `k` is not derived, and the ENUMERATION is the finding — only `k = 0`
and `k = 1` have arguments, and neither gives the SEMF sign.**

## The family is simpler than its definition

    w_k = q^-k/[2]_{q^k} = 1/(q^{2k}+1) = 1/(1 + (b_pp/b_nn)^(k/2))

since `b_pp/b_nn = q^4 = 1.51795324982`. So **`k/2` is literally the power of
the bond ratio the average is weighted by** — `k = 0` weights by ratio^0 (flat),
`k = 1` by its square root, `k = 2` by the ratio itself. And the interface closes:

    f_pn(k) = [2]_{q^(2-k)} / ([2]_q . [2]_{q^k})

one expression covering the arithmetic mean (`k=0`), geometric (`k=1`) and
harmonic (`k=2`). Verified exact to 1e-40 at `k = 0, 0.5, 1, 1.5, 2, 3`.

## The reflection is one line from it

    f_pn(k) . f_pn(2-k) = 1/[2]_q^2 = 0.247297886748034598

for every `k`. So `k -> 2-k` **inverts the interface about the loop value**, and
that is *why* `delta` is odd about `k = 1` — a fact previously observed
numerically and now explained. `k = 1` is the only fixed point.

## Which members have an argument — the enumeration IS the result

| k | w_k | delta | argument | |
|---:|---:|---:|---|---|
| **0** | 0.500000 | **-0.02161775** | undeformed limit — what "flat average" MEANS | **wrong sign** |
| **1** | 0.448018 | **0** | interface IS the loop value `1/[2]_q`; unique fixed point of the reflection | **zero** |
| 2 | 0.397148 | +0.02161775 | **none** | SEMF |

`k = 0` is genuinely derived — from an assumption the deformation contradicts.
`k = 1` has two independent characterisations of the same point. **Nothing in
the SEMF-signed region `k > 1` has an argument.**

## And the corpus sits at NEGATIVE k

Solving `1/2 + delta_flavour/4 = 1/(q^{2k}+1)` gives **`k = -0.00659`**. The
corpus's one bar-breaking ingredient moves it *further* from `k > 1`, not toward
it — and by 1/151 of what the sign needs in any case (`qou-i01a`).

## The two readings of k = 2 I considered, and why neither is a principle

Written down so a successor attacks them rather than rediscovering them.

- **(A)** `w_2 = b_nn/(b_pp + b_nn)` — weight each branch by the OTHER's bond
  factor. A cross-weighting with no stated motivation anywhere in the corpus.
- **(B)** the harmonic mean is what one averages when averaging RATES (parallel
  resistances, inverse times). But the bond factors are trace AMPLITUDES, and
  nothing identifies them with a reciprocal quantity.

Both are stories. **`k = 2` gives the SEMF sign and is NOT adopted on that
basis** — a target to check a derivation AGAINST, never a criterion to search ON.

## The derivable prediction

**`k = 1`, `delta = 0`: the p-n interface contributes NO symmetry energy, and
the SEMF symmetry term comes from outside this channel.** Falsifiable, and the
honest close of the arc that began with "the symmetry energy has no available
route".

**What would overturn it:** a principle producing `k` from the ALGEBRA — a
strand count, a colour count, a Casimir — rather than from a choice of mean.
That is the shape the successor needs, and it is a much smaller target than
"derive the averaging rule" was.

## Artifacts

`QOU/Hecke/BarWeightFamily.lean` grows 4 -> 8 decls, all `[propext,
Classical.choice, Quot.sound]`, `lean`-direct exit 0: `weight_eq_inv_rpow`,
`interface_closed_form`, `interface_reflection`, `interface_one_eq_loop_value`.
`computations/qbeta/qbeta_averaging_index_k_probe.py` (6/6, 40 dps,
float64-guard clean).
