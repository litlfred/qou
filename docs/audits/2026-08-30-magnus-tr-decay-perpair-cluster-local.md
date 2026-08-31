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

**Measured verdict: (P), decisively, at A=2, A=3, and A=4.** Every one of the local
windows has its normalised trace `max_λ |t_λ^{(a)}|/dim_λ` **peaking at b=1** and
falling into a suppressed tail:

| | windows | self-check err | b1/tail suppression, per window |
|---|---|---|---|
| A=2 (n=6) | 4 | 4.46e-58 (11 parts) | 1.55× .. 6.93× (tail = max b≥3) |
| A=3 (n=9) | 7 | 4.31e-57 (30 parts) | 5.6× .. 12.8× (tail = max b≥3) |
| A=4 (n=12, b≤3) | 10 | 2.59e-56 (50 banked) | 7.3× .. 22.0× (tail = b=3 only) |

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
- **Suppression is modest at small A, sharpens with A.** At A=2 some windows are only
  ~1.5× down. The **fully-comparable** metric (the `b1/b2` ratio, since b=2 is present at
  all three A) sharpens monotonically: window `(0,1)` `3.10 → 3.45 → 3.62` (A=2,3,4);
  window `(2,3)` `1.68 → 2.24 → 2.59`. Consistent with representation stability (growth
  audit §3), but a **uniform quantitative bound is not proved**. The A=4 "tail" column
  above is `b1/b3` (the low-b run stops at b=3), so it is **not** directly comparable to
  the A=2/A=3 tails (which are `b1/max(b≥3)`); use `b1/b2` for cross-A comparison. At A=4
  restricted to b≤3 every window is additionally **strictly monotone** b1>b2>b3 — the
  non-monotone bumps at A=2/A=3 sit at *higher* b (where values are already tiny), which
  this low-b run does not reach. The A=4 self-check anchor is the **banked (gitignored)
  checkpoint**, not a committed witness; the reproducible anchors are A=2/A=3.
- **The reduced single-window estimate is still open.** (P) is a genuine reduction and
  a genuine elimination of the harder sub-route; it is **not** a proof of the theorem.
  Proving `|tr(ρ_λ [A_a,A_{a+1}])|/dim_λ` decays with b (with a rate) remains the open
  work, now on a single 3-strand-local operator instead of the whole Ω₂ sum.

## Lean backing (the algebraic skeleton, sorry-free)

The two load-bearing *structural* assertions are formalized sorry-free in
[`QOU/MassTheory/MagnusOmega2LocalDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MagnusOmega2LocalDecomposition.lean)
(generic `CommRing`; lean-direct exit 0; `#print axioms` = the standard classical base
`{propext, Classical.choice, Quot.sound}`, two declarations not even reaching
`Classical.choice`):

- `commutator_eq_zero_of_commute` — `Commute A B ⟹ A*B−B*A = 0`, the operator content of
  the probe's `if |a−b| ≠ 1: continue` far-commutativity filter.
- `omega2_reduces_to_adjacent` — `Σ_{i<j} ⁅A_i,A_j⁆ = Σ_adjacent ⁅A_a,A_{a+1}⁆` (far pairs
  drop), i.e. Ω₂ *is* a lattice sum of 3-strand-local windows.
- `trace_rho_localSum` / `trace_rho_weightedLocalSum` — `tr(ρ·Σ c_k•O_k) = Σ c_k·tr(ρ·O_k)`,
  the exact algebraic identity the `4.3e-57` self-check verifies numerically.

The `tr(Ω₂)=0` control is already `QOU.MassTheory.trace_commutator_eq_zero`
(MagnusPairingSignStructure.lean), cited not re-proved.

**What is NOT (and must not be) in Lean:** the empirical **peak-at-b=1 decay** itself. It
is a measured fact and the open theorem; axiomatizing it or concluding it by `rfl`/`True`
would be laundering. The Lean formalizes the algebraic skeleton the decay lives on — the
reduction and the per-window linearity — not the analytic decay.

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
