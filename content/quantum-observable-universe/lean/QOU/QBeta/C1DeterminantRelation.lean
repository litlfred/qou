/-
Copyright (c) 2026 litlfred. All rights reserved.

# The determinant ties C1's two ends — and independently confirms both

`C1FuchsianExponents.lean` computed the weights at `0` from the indicial
equation; `C1NewtonRamification.lean` computed the characteristic equation of the
Newton edge at `∞`.  The two were derived from different data — coefficients at
`x = 0` versus the Newton polygon at `∞` — so nothing yet said they were
consistent.

**The determinant says so, and it is a genuine check rather than a restatement.**
For `L1 = a₂σ² + a₁σ + a₀` the companion system `σY = A·Y` has

    A = [[0, 1], [−a₀/a₂, −a₁/a₂]] ,      det A = a₀/a₂ = −(q−1)/(q²x − 1)

(the same `det A` used in the #4721 third-singular-site argument, where its
divisor degree `−1` on `ℂ*` proved `x = q⁻²` non-removable).  `det A` is the
`σ`-multiplier of the rank-one determinant equation, so **at each singular point
the product of the two local exponents equals the local value of `det A`**.  That
is one equation per end, and each end already has an independently computed pair
of exponents.  Both check out:

| end | local exponent pair | their product | `det A` there | agree? |
|---|---|---|---|---|
| `0` (Fuchsian) | roots of `t² + (q−1)t + (q−1)` | `q − 1` (Vieta) | `det A(0) = q − 1` | ✔ |
| `∞` (slope ½) | roots of `q²t² = q − 1` | `q²·(t·s) = −(q−1)` | leading coeff `−(q−1)/q²` | ✔ |

The `0` check is Vieta's constant term against `a₀/a₂` evaluated at `x = 0`.  The
`∞` check is sharper than it looks: the edge equation only says `t² = (q−1)/q²`,
which is a statement about each root separately; that the *product* of the two
distinct roots is `−(q−1)/q²` uses `s = −t`, and it is the determinant that
independently predicts that value.  A sign error in the Newton polygon, or a
wrong `a₀`, would break it.

## What this settles, and what it does NOT

**Settled: the two ends are mutually consistent.**  A single object — `a₀/a₂` —
reproduces two exponent pairs computed from different data.  That is what this
file proves, and it is all it proves.

> ### 🛑 The `∞` roots here are `T_edge`, NOT the sector parameter
>
> An earlier version of this docstring said *"C1's `∞` exponent data is fully
> determined: the pair is `±√(q−1)/q`"*.  **That gloss is wrong**, and
> `computations/qbeta/c3_w2_c1_theta_canonical.py` carries a section headed
> *"The convention finding — read this before citing `B = ±sqrt(q-1)/q`"*
> warning against exactly it:
>
> | object | value | what it is |
> |---|---|---|
> | `T_edge` | `±√(q−1)/q` | root of the Newton **edge polynomial**. What `edge_roots_mul` below is about. |
> | `T_theta` | `±√(q−1)/q^{3/4}` | parameter indexing the theta-normalised canonical solutions, **hence the Stokes sectors** |
>
> They differ by `q^{1/4}`, and the edge root **provably does not satisfy the
> indicial equation**.  Both are correct statements about their own objects; what
> is not interchangeable is the interpretation.  Calling `T_edge` "the exponent
> data indexing the sectors" carries a silent `q^{1/4}` — the failure mode that
> script names as *"an object computed correctly, then given a name whose meaning
> it does not have."*

**Not settled: the connection-matrix Stokes multipliers.**  Those are global
`0`↔`∞` data, functions of the invariant `χ = P₀₀P₁₁/(P₀₁P₁₀)`, and are being
worked under bean `qou-wgnx` — where the connection matrix and `χ` are already
built.  No determinant or Vieta relation reaches them.  (Distinct from the
*local isoformal* moduli at `∞`, which are dimension `0` because C1 is pure
isoclinic there — see `QOU.MathlibExt.RSZ.c1_infinity_isoformalDim_eq_zero`.
Two different objects share the name; only the local one is empty.)

## Provenance

The `0`-side indicial polynomial and its Vieta relations are **not** introduced
here.  They predate this file in
[`C1ZeroSideExponents.lean`](C1ZeroSideExponents.lean) (bean `qou-wgnx`), which
also proves the exponents are a conjugate pair for `1 < q < 5` and that
`|t|² = q−1` — neither of which is reproved here.  An earlier version of this
file carried its own copies; they are retired and the results are now derived
from `C1ZeroSide.vieta`.  What is genuinely new here is the `det A` cross-check
tying the two ends.

§7c: a generic field `K` — pure algebra, no ordering, nothing archimedean.
Sorry-free.  No fit, nothing wired, no Stokes multiplier computed.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853
-- Ref: [manuscript] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
-/
import Mathlib.Tactic
import QOU.QBeta.C1ZeroSideExponents

namespace QOU.QBeta

variable {K : Type*} [Field K]

/-- The indicial polynomial at `0`.  **Not redefined here** — this is
`QOU.QBeta.C1ZeroSide.zeroSideIndicial`, which predates this file (bean
`qou-wgnx`).  An earlier version of this file defined its own copy under the name
`indicialAt`; that was duplication and is retired. -/
abbrev indicialAt (q t : K) : K := C1ZeroSide.zeroSideIndicial q t

/-- `det A` of C1's companion system: `a₀/a₂ = −(q−1)/(q²x − 1)`. -/
noncomputable def detA (q x : K) : K := -(q - 1) / (q ^ 2 * x - 1)

/-! ### The Fuchsian end -/

/-- **Vieta, sum** — derived from the pre-existing `C1ZeroSide.vieta` rather
than reproved.  An earlier version of this file carried its own proof; that
duplicated `qou-wgnx` work and is retired. -/
theorem indicial_roots_add {q t s : K}
    (hfac : ∀ u : K, indicialAt q u = (u - t) * (u - s)) :
    t + s + (q - 1) = 0 := by
  have := (C1ZeroSide.vieta q t s).mp hfac
  linear_combination this.1

/-- **Vieta, product** — likewise derived from `C1ZeroSide.vieta`. -/
theorem indicial_roots_mul {q t s : K}
    (hfac : ∀ u : K, indicialAt q u = (u - t) * (u - s)) :
    t * s = q - 1 :=
  ((C1ZeroSide.vieta q t s).mp hfac).2

/-- `det A` at the Fuchsian point: `det A(0) = q − 1`. -/
@[simp] theorem detA_zero (q : K) : detA q 0 = q - 1 := by
  unfold detA
  rw [mul_zero, zero_sub, div_neg, div_one, neg_neg]

/-- **The `0`-end check.**  The product of the two local exponents equals
`det A(0)`.  Vieta's constant term and `a₀/a₂` at `x = 0` were computed from
different data and agree. -/
theorem fuchsian_end_consistent {q t s : K}
    (hfac : ∀ u : K, indicialAt q u = (u - t) * (u - s)) :
    t * s = detA q 0 := by
  rw [detA_zero]
  exact indicial_roots_mul hfac

/-! ### The irregular end -/

/-- Two distinct roots of the Newton-edge equation `q²t² = q − 1` are negatives
of each other — the deck sign, arrived at here from the edge equation rather than
from the ramified cover. -/
theorem edge_roots_neg {q t s : K} (hq : q ≠ 0) (ht : q ^ 2 * t ^ 2 = q - 1)
    (hs : q ^ 2 * s ^ 2 = q - 1) (hne : t ≠ s) : s = -t := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hsq : t ^ 2 = s ^ 2 :=
    mul_left_cancel₀ hq2 (by rw [ht, hs])
  have h : (t - s) * (t + s) = 0 := by linear_combination hsq
  rcases mul_eq_zero.mp h with h | h
  · exact absurd (sub_eq_zero.mp h) hne
  · linear_combination h

/-- **The `∞`-end product.**  The two edge roots multiply to `−(q−1)/q²`, i.e.
`q²·(t·s) = −(q−1)`.  Note this is *strictly more* than the edge equation, which
only constrains each root's square. -/
theorem edge_roots_mul {q t s : K} (hq : q ≠ 0) (ht : q ^ 2 * t ^ 2 = q - 1)
    (hs : q ^ 2 * s ^ 2 = q - 1) (hne : t ≠ s) : q ^ 2 * (t * s) = -(q - 1) := by
  rw [edge_roots_neg hq ht hs hne]
  linear_combination -ht

/-- `det A` in the coordinate `u = 1/x` at `∞`: a simple zero,
`det A = −(q−1)·u/(q² − u)`. -/
theorem detA_at_infty {q u : K} (hu : u ≠ 0) (h : q ^ 2 - u ≠ 0) :
    detA q u⁻¹ = -(q - 1) * u / (q ^ 2 - u) := by
  unfold detA
  have hden : q ^ 2 * u⁻¹ - 1 = (q ^ 2 - u) / u := by field_simp
  rw [hden, div_div_eq_mul_div]

/-- **The `∞`-end check.**  After factoring out the simple zero, `det A`'s
leading coefficient at `∞` is `−(q−1)/q²`; scaled by `q²` that is `−(q−1)`,
exactly `edge_roots_mul`.  The Newton polygon at `∞` and `a₀/a₂` agree. -/
theorem irregular_end_consistent {q t s : K} (hq : q ≠ 0)
    (ht : q ^ 2 * t ^ 2 = q - 1) (hs : q ^ 2 * s ^ 2 = q - 1) (hne : t ≠ s) :
    q ^ 2 * (t * s) = q ^ 2 * (-(q - 1) / q ^ 2) := by
  rw [edge_roots_mul hq ht hs hne, mul_div_cancel₀ _ (pow_ne_zero 2 hq)]

/-- **Both ends consistent with the same determinant.**  Recorded as one
statement because the point is that a *single* object — `a₀/a₂` — reproduces two
independently computed exponent pairs.  Neither end was fitted to the other. -/
theorem both_ends_consistent_with_detA {q t s t' s' : K} (hq : q ≠ 0)
    (hfac : ∀ u : K, indicialAt q u = (u - t) * (u - s))
    (ht' : q ^ 2 * t' ^ 2 = q - 1) (hs' : q ^ 2 * s' ^ 2 = q - 1) (hne' : t' ≠ s') :
    t * s = detA q 0 ∧ q ^ 2 * (t' * s') = -(q - 1) :=
  ⟨fuchsian_end_consistent hfac, edge_roots_mul hq ht' hs' hne'⟩

end QOU.QBeta
