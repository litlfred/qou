---
# qou-1u90
title: 'Lean: DihedralExact for M i j >= 4 — the order of sigma_i sigma_j'
status: completed
type: task
priority: normal
created_at: 2026-09-06T10:49:37Z
updated_at: 2026-09-07T06:22:32Z
---

## What is open

`QOU.Machinery.CoxeterRankTwo.DihedralExact cs` says: for `i ≠ j` and
`0 < k < M i j`, `(σᵢσⱼ)^k ≠ 1` — i.e. `σᵢσⱼ` has order **exactly** `M i j`,
not merely a divisor of it. The `(σᵢσⱼ)^{M i j} = 1` direction is the defining
relation and holds always.

It is discharged for `M i j ≤ 3` (`CoxeterDihedralDescent.dihedralExact_le_three`)
off `CoxeterGeometricRepresentationFull`'s two unconditional cell-faithfulness
results. **`M i j ≥ 4` is open.**

## Why it is worth recording rather than doing

- **It is the corpus's OWN named open item**, not a gap introduced by the
  Matsumoto work. `CoxeterGeometricRepresentationFull`'s HONESTY note says
  verbatim: *"What this does NOT prove: full Tits faithfulness (`ℓ` of
  arbitrary words / the order of `σᵢσⱼ` being exactly `mᵢⱼ`)"*.
- **No consumer in this corpus needs it.** The Hecke/braid arc is type A
  (`coxA m`, entries 1/2/3), and `Matsumoto.matsumoto_An` /
  `exists_Tw_An` are already hypothesis-free there. `H₃`, `H₄`, `Bₙ`, `G₂`
  would need it; nothing here builds on those.

## The route, and what already exists

The reflection representation. `CoxeterGeometricRepresentationFull` already has
the whole scalar recursion — `reflEnd_pair_apply`, `formLin_i_pair`,
`formLin_j_pair`, and the trig engine `periodic_of_two_step` (a two-step
recursion `u(k+2) = 2cos φ · u(k+1) − u(k)` matched to `α sin(kφ) + β cos(kφ)`),
which it spends proving `reflEnd_pair_pow_eq_one`.

What is missing is the **converse**: the pair `(⟨αᵢ, g^k w⟩, ⟨αⱼ, g^k w⟩)`
evolves by a rotation through `φ = 2π/m`, so it returns to a NONZERO starting
value only when `m | k`. Take `w = αᵢ`, where the initial pair is `(1, c)` with
`c = B(αᵢ,αⱼ) = −cos(π/m)`, hence nonzero. Estimated a bounded extension of that
file (~150–250 lines), all in `ℝ` by necessity (§7c), not a new development.

## Do not confuse this with

`Matsumoto` itself, which is CLOSED (bean qou-06h7). This is only the residual
generality: Matsumoto holds for every Coxeter system satisfying `DihedralExact`,
and unconditionally on type A.


## ✅ CLOSED 2026-09-07 — `DihedralExact` holds for EVERY Coxeter system

`QOU.Machinery.CoxeterDihedralOrder.dihedralExact_full`, sorry-free.

## 🛑 My "no consumer in this corpus needs it" was wrong within a day

That was true when this bean was opened — Matsumoto was the only consumer and
was itself brand new. By the time it was picked up, the arc had grown to
Matsumoto, `exists_Tw`, the subword property, transitivity, lifting, and two
Bruhat-order equivalences — **all hypothesis-free only on type A** because of
this one predicate. A "no consumer" verdict on an open item at the base of an
arc that is still being built has a short shelf life; re-check before deferring
on that ground.

## The proof needs LESS than the one already in the corpus

`reflEnd_pair_pow_eq_one` (the forward direction, `(fᵢfⱼ)^m = 1`) needs
`sin φ ≠ 0`, hence `m ≥ 3`, plus an argument that periodicity kills two
accumulated sums.

The converse needs neither. Track ONE scalar along the orbit of one root,
`x k = ⟨αᵢ, (fᵢfⱼ)^k αᵢ⟩`. The existing `formLin_i_pair` / `formLin_j_pair`
give the 2×2 recursion; eliminating the other coordinate leaves the Chebyshev
two-step `x(k+2) = (4c²−2)·x(k+1) − x k`. The initial data is what does the
work: `x 0 = 1 = cos 0` and `x 1 = 2c²−1 = cos(2π/m)` by the double-angle
formula. Matching against `k ↦ cos(kφ)` — same recursion, same first two terms
— gives `x k = cos(k·2π/m)` with **no sine anywhere**, so `m ≥ 2` suffices.

Then `(fᵢfⱼ)^k = 1` forces `cos(kφ) = 1`, and `0 < kφ < 2π` for `0 < k < m`.
`Real.cos_eq_one_iff_of_lt_of_lt` closes it. `geomRepFull` transports back to
the group.

## What is NOT closed — and it is not `DihedralExact`

`hfin : ∀ i j, i ≠ j → M i j ≠ 0` (no infinite bond orders) is a SEPARATE
hypothesis and survives. It enters via `not_isReduced_alternatingWord`.

This is not an oversight of the cosine argument — that argument genuinely
cannot see `m = 0`. Under the `π/0 = 0` convention `c = −1`, the Chebyshev
parameter is `2`, and `x(k+2) = 2x(k+1) − x k` with `x 0 = x 1 = 1` is constant
`1`. The scalar returns to its start at every `k` and distinguishes nothing —
correctly, since the infinite dihedral group has no relation to detect. Ruling
`m = 0` out belongs in the descent lemma and is a different argument.

**So the scope is every Coxeter system with all bond orders finite** — `Bₙ`,
`Dₙ`, `E₆₇₈`, `F₄`, `H₃`, `H₄`, every `I₂(m)`, not merely `Aₙ`. Restated in
`QOU.IwahoriHecke.MatsumotoUnconditional`.

`CoxeterGeometricRepresentationFull`'s HONESTY note is updated: of the two
things it excluded, this closes the second; `ℓ` of arbitrary words is still open
there.
