# The reduced single-window estimate is a SUB-DIM trace bound, not a cancellation (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** continue the work.
**Scope:** scope-(a) structural datum; no MeV, no fit, nothing wired.
**Probe:** [`magnus_tr_decay_perpair_cluster_probe.py --raw`](../../computations/deltalambda/magnus_tr_decay_perpair_cluster_probe.py)
**Follows:** #6311 (the tr-decay is per-window LOCAL) — this characterises the *reduced*
target #6311 left open.

## What #6311 left open

#6311 reduced the tr-decay theorem `qou-o6ov` to a **single fixed 3-strand-local operator**:
`|tr(ρ_λ O)|/dim_λ` decays with `b(λ)`, where `O = [A_a,A_{a+1}]`. The open question this
probe answers: **why** does it decay — and therefore which proof route is viable?

Three a-priori regimes for the raw (un-normalised) single-window trace `|t_λ^{(a)}| =
|tr(ρ_λ O)|`, as `b` grows and `dim_λ` climbs:

- **BOUND** — `|t|` bounded by a constant ⇒ decay is trivially `≤ C/dim` (a constant
  operator-trace bound; the cleanest provable route).
- **SUB-DIM** — `|t| = o(dim)` (grows, but strictly slower than `dim`) ⇒ decay from `dim`
  outgrowing a slowly-varying `|t|` (a *sublinear* trace bound `|t| ≤ C·dim^θ`, `θ<1`).
- **CANCELLATION** — `|t|` tracks `dim` ⇒ `|t|/dim` decays only after a signed cancellation;
  needs the connected-diagram (Penrose/Ursell) argument. The hard case.

## Measured (A=3, all 30 partitions, exact mpf dps=140)

Over the steep-dim range `b=1→3`, **`dim(max)` grows ×13.1**, while the raw per-window
peak `max_λ |t_λ^{(a)}|` grows by at most **×1.93**:

| window | raw-`|t|` growth (b=1→3) | ÷ dim growth (×13.1) | regime |
|---|---|---|---|
| (0,1) | ×0.36 | 0.027 | ≈bounded |
| (1,2) | ×0.90 | 0.069 | o(dim) |
| (2,3) | ×1.93 | **0.147** (worst) | o(dim) |
| (3,4) | ×0.90 | 0.068 | o(dim) |
| (4,5) | ×0.93 | 0.071 | o(dim) |
| (5,6) | ×1.80 | 0.137 | o(dim) |
| (6,7) | ×0.47 | 0.036 | ≈bounded |

**In every window raw `|t|` grows at most ~15% as fast as `dim`.** So the decay is
**SUB-DIM**: `|t_λ^{(a)}| = o(dim_λ)`, driven by `dim` outgrowing a slowly-varying raw
single-window trace — **not** a cancellation that tracks `dim`.

**A=2 confirms the regime (all 11 partitions), with a tighter margin.** `dim(max)` grows
only ×3.2 over b=1→3 there, and the worst window is `(2,3)` at raw ×1.0 = **0.313×** the
dim growth — still SUB-DIM in every window, but at 31% vs A=3's 15%. The `o(dim)` margin
**sharpens with A** (the dim growth outpaces the raw trace more decisively as the diagram
fattens), consistent with the representation-stability reading.

## Why this matters (it moves the frontier toward provable)

- The reduced estimate does **not** require the hard dim-tracking connected-diagram
  cancellation. It follows from a **sublinear single-window trace bound**
  `|tr(ρ_λ [A_a,A_{a+1}])| ≤ C·dim_λ^θ` with `θ<1` (or any `o(dim)` rate). That is a
  bound on **one** 3-strand-local operator dressed by the global word — a far smaller,
  more tractable object than the full `Ω₂` sum or a Penrose tree-graph cancellation.
- The natural handle: `O` is supported on Coxeter positions `{a,a+1}` (strands
  `{a,a+1,a+2}`); in the seminormal rep its nonzero rows are only the tableaux that
  differ by moving boxes among those 3 strands. The count of such "active" tableaux
  grows like `dim` of a **rank-bounded** sub-pattern, which is `o(dim_λ)` as the diagram
  fattens — this is the shape of the bound to prove. (Not proved here; this is the target
  the measurement identifies.)

## Honest limits

- **`|t|` is not constant.** It rises ~2× to a mid-`b` peak, then falls. A strict `≤ C`
  constant bound (the BOUND regime) is **false**; the provable target is the **`o(dim)`
  rate**, not a constant.
- **A=2 and A=3, and a `max_λ`-over-partitions statistic.** The `o(dim)` reading is a
  ratio-of-growth-rates measurement over the low-`b` range; the regime holds at both A
  tested (margin 31% at A=2, 15% at A=3), but it is evidence for the regime, not a proof
  of the rate. A cross-`A` confirmation at A=4 low-`b` and a per-partition (not just
  `max_λ`) bound are the next measurements.
- **Still open.** This does not prove the reduced estimate; it identifies the correct
  provable form of it (sublinear trace growth) and rules out the two extremes (constant
  bound: false; dim-tracking cancellation: not what the data shows).

## Bottom line

The tr-decay's remaining open core is a **sublinear single-window trace bound**
`|tr(ρ_λ[A_a,A_{a+1}])| = o(dim_λ)` — measured at A=3 as raw `|t|` growing ≤15% as fast as
`dim`. This is a more hopeful frontier than the connected-diagram cancellation the crude
first reading suggested; the next step is a cross-`A` check and an attempt at the
rank-bounded active-tableau count that would furnish the `θ<1`.
