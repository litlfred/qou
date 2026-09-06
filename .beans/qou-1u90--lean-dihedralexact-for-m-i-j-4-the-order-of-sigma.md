---
# qou-1u90
title: 'Lean: DihedralExact for M i j >= 4 — the order of sigma_i sigma_j'
status: todo
type: task
created_at: 2026-09-06T10:49:37Z
updated_at: 2026-09-06T10:49:37Z
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
