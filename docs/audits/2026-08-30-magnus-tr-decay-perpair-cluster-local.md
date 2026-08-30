# tr-decay theorem (qou-o6ov): the decay is PER-WINDOW LOCAL, not an inter-window cancellation

**Date:** 2026-08-30
**Directive (owner):** continue working the theorem.
**Scope:** scope-(a) structural datum; no MeV, no fit, nothing wired.
**Probe:** [`computations/deltalambda/magnus_tr_decay_perpair_cluster_probe.py`](../../computations/deltalambda/magnus_tr_decay_perpair_cluster_probe.py)

## What was open

The theorem `qou-o6ov` (corrected form): `|tr(ρ_λ Ω₂_λ)|/dim_λ` decays with
`b(λ)=n−λ₁`. Two proof routes were already closed as negatives:

- **Kerov–Olshanski content-polynomiality — REFUTED** (#6291): `tr/dim` is not a
  low-degree polynomial in the content power-sums.
- **2-row closed-form decay — not clean**: the 2-row trace is non-monotone, no tidy
  law to bound.

The one surviving route is the **cluster/cumulant** connected-diagram cancellation.
That route has a fork the whole strategy turns on, and this probe resolves it.

## The exact local structure (measured, self-checked)

By far-commutativity (`[A_a,A_b]=0` for `|a−b|≥2`),
```
Ω₂ = ½ Σ_{i<j} [A_{g_i},A_{g_j}] = ½ Σ_{(a,a+1)} mult(a,a+1)·[A_a,A_{a+1}]
```
keeps only **adjacent-generator** commutators. The adjacent-pair multiplicities of the
canonical atom word `atom_braid_word_3A` are **period-3 translation-invariant**,
identical in every nucleon window and identical across A:
```
(3m,3m+1):28    (3m+1,3m+2):4    (3m+2,3m+3):7      [last window has no +3 bond]
```
So **Ω₂ is a genuine lattice sum of local operators**, one 3-strand-window motif per
nucleon — the MPO / transfer-matrix picture made exact, not an analogy. (The
multiplicity *pattern* is period-3; the actual per-window traces are **not**
translation-invariant — the global word breaks strict translation symmetry, values at
b=1 range 2.5–9.9 across the 7 windows at A=3.)

Define the per-window local trace `t_λ^{(a)} := tr(ρ_λ·[A_a,A_{a+1}])`. Then
`2·tr(ρ_λ Ω₂) = Σ_a mult(a,a+1)·t_λ^{(a)}`, **self-checked against the committed
witnesses to full precision**: max abs error `4.31e-57` (A=3, 30 partitions) /
`4.46e-58` (A=2, 11 partitions). The local decomposition is exact.

## The fork, and the answer: (P) per-window local

The b-decay of `tr(ρ_λ Ω₂)` could arise two ways:

- **(P) per-window local** — each `|t_λ^{(a)}|/dim_λ` already peaks at low b. Then the
  theorem localizes to **one** local-operator estimate, summed over a λ-independent
  number of windows.
- **(C) inter-window cancellation** — individual windows do not decay; the decay only
  appears after the signed sum (the harder Penrose/Ursell connected-diagram story).

**Measured verdict: (P), decisively, at both A=2 and A=3.** Every one of the local
windows has its normalised trace `max_λ |t_λ^{(a)}|/dim_λ` **peaking at b=1** and
falling into a suppressed b≥3 tail:

| | windows | b1/tail(b≥3) suppression, per window |
|---|---|---|
| A=2 (n=6) | 4 | 1.55× .. 6.93× |
| A=3 (n=9) | 7 | 5.6× .. 12.8× |

No window carries its mass at high b, so the b-decay is **already present per
window** — it is **not** an inter-window cancellation. This **rules out the (C)
sub-route** and reduces the theorem to a single local estimate:

> **Reduced target.** For a *fixed* 3-strand-local operator `O = [A_a,A_{a+1}]`,
> `|tr(ρ_λ O)|/dim_λ` decays with `b(λ)`. (`O` is local; the word `ρ_λ` is still
> global.)

## Honest limits (what this does NOT establish)

- **Not monotone.** The per-window fall is not strictly monotone in b — small bumps at
  high b where values are already small. "(P)" is a **peak-at-b=1** statement, not a
  monotone-decay one; a monotone bound is a separate, stronger claim.
- **Suppression is modest at small A.** At A=2 some windows are only ~1.5× down. The
  suppression **sharpens with A** (A=2: 1.5–6.9×; A=3: 5.6–12.8×) — consistent with the
  representation-stability reading (growth audit §3), but a **uniform quantitative
  bound is not proved** here.
- **The reduced single-window estimate is still open.** (P) is a genuine reduction and
  a genuine elimination of the harder sub-route; it is **not** a proof of the theorem.
  Proving `|tr(ρ_λ [A_a,A_{a+1}])|/dim_λ` decays with b (with a rate) remains the open
  work, now on a single 3-strand-local operator instead of the whole Ω₂ sum.

## Bottom line

- **New positive structural result:** the tr-decay is **per-window local (P)**, not an
  inter-window cancellation — the first positive finding on `qou-o6ov` (the two prior
  route-tests were negatives). It eliminates the Penrose/Ursell connected-cancellation
  sub-route and **localizes the theorem** to one 3-strand operator's normalised trace.
- **Exact infrastructure:** the period-3 lattice decomposition of Ω₂, self-checked to
  `4.3e-57` against the committed witnesses.
- **Still open:** the reduced single-window normalised-trace decay estimate (with a
  rate) — the target that would close the theorem and upgrade the row-truncation bound
  from heuristic to rigorous.
