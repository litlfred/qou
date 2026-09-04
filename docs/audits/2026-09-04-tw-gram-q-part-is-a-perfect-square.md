# The q-part of `det(twGram)` is a perfect square — and the sign is forced

**Date:** 2026-09-04 · **Bean:** `qou-kwoa` · **Status:** confirmed at `n = 1, 2, 3`

## Claim

`QOU.Hecke.TwBasis.twGram_det_eq_sq_mul_prod` (Lean, sorry-free, merged in
[#6617](https://github.com/litlfred/qou/pull/6617)) proves

```
det(twGram K (q²) n) = (det P)² · ∏_λ sign(prodComm) · d_λ^(d_λ²),   IsUnit (det P)
```

where `λ` runs over partitions of `n+1` and `d_λ` is the number of standard Young
tableaux of shape `λ`. Because `P` is a change of basis and the block factors are the
only non-square part, this makes **two predictions about a quantity that was measured
independently**, earlier, by a probe that used none of this:

- **(A) Sign.** `prodComm` on `J × J` with `|J| = d` fixes the `d` diagonal pairs and
  swaps the remaining `d(d−1)/2`, so its signature is `(−1)^(d(d−1)/2)`. The sign of the
  determinant is the product over blocks.
- **(B) Square class.** *All* `q`-dependence sits inside `(det P)²`. So after dividing
  out the signed integer constant, the remainder must be a **perfect square in ℚ(q)** —
  every irreducible factor to an even power.

**(B) is the substantive one.** It is not implied by the shape of the measured answer.
A determinant of this size has no reason for every exponent to come out even, and a
single odd exponent anywhere would refute the theorem's claim that the Wedderburn
isomorphism contributes no factor.

## Result — both hold at every rank the probe reached

Verified in exact arithmetic by
[`computations/hecke/tw_gram_square_class_crosscheck.py`](../../computations/hecke/tw_gram_square_class_crosscheck.py)
against the determinants measured by
[`tw_gram_determinant_probe.py`](../../computations/hecke/tw_gram_determinant_probe.py):

| `n` | block dims `d_λ` | predicted sign | predicted constant | q-part after division | square root |
|---|---|---|---|---|---|
| 1 | 1, 1 | `+1` | `1` | `(q+1)²` | `q+1` |
| 2 | 1, 2, 1 | `−1` | `−16` | `q²(q+1)²(q²+q+1)⁶` | `q(q+1)(q²+q+1)³` |
| 3 | 1, 3, 2, 3, 1 | `−1` | `−6198727824` | `q²²(q+1)⁴⁸(q²+1)²⁰(q²+q+1)⁶` | `q¹¹(q+1)²⁴(q²+1)¹⁰(q²+q+1)³` |

The sign test is not a separate computation: dividing by the *predicted signed* constant
must leave leading coefficient `+1`, and it does at all three ranks. A wrong sign would
leave `−1` out front.

## Why this is not circular

The probe obtained its determinants by factoring exact symbolic determinants of the
regular representation, and predates the theorem. The theorem was proved from
`BlockTriangular.det_fintype`, `Pi.basis`, and the algebra-invariance of the regular
trace form. Neither used the other, so the agreement is evidence about both — and in
particular it is evidence that the `T_w` ↔ matrix-unit change of basis really does
account for the whole `q`-dependence.

## What this does NOT establish

- **It is not a proof.** Three ranks are three data points. The theorem is proved in
  Lean; what is *confirmed* here is that its prediction matches measurement where
  measurement exists.
- **It does not evaluate `det P`.** The square-root column above is `|det P|` up to the
  unit — it is read off the measurement, not derived. Deriving it is the open item.
- **It says nothing about the `q`-part of Geck–Pfeiffer.** Note in particular that
  `twGram` is the **regular** trace form `tr(L_{xy})`, whereas Geck–Pfeiffer's Schur
  elements belong to the **canonical symmetrizing trace** `τ` (with `τ(T_w) = δ_{w,1}`).
  These are different forms, and conflating them is the trap here: the `∏_λ d_λ^(d_λ²)`
  derived for the regular form is the analogue of, not the same as, `∏_λ s_λ^{f^λ}`.

## Identified next step, with its route named

Make the sign explicit in Lean:

```lean
Equiv.Perm.sign (Equiv.prodComm ι ι) = (-1) ^ (Fintype.card ι * (Fintype.card ι - 1) / 2)
```

The route through Mathlib: `prodComm ι ι` squares to `1`, so its cycle type is all `2`s;
`Equiv.Perm.sign_of_cycleType` (`Mathlib/GroupTheory/Perm/Cycle/Type.lean:164`) then gives
the sign from `#support / 2`, and `#support = d² − d` because the fixed points are exactly
the diagonal. `two_dvd_card_support` (same file, :194) supplies the divisibility.

**Priced, not guessed:** this is a self-contained counting argument, and the support
computation is the bulk of it. It is not free, and it is not a tranche. Naming the route
rather than asserting a gap is deliberate — earlier in this same arc I recorded
`Matrix.det_blockDiagonal'` as a blocking Mathlib gap when the capability was filed under
`BlockTriangular.det_fintype`, a weaker hypothesis (see
`.claude/agent-memory/corpus-grepper/MEMORY.md`, *"in an UPSTREAM library, grep the
statement SHAPE, not the data structure"*).
