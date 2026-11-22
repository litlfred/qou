/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalQuotient
import QOU.SchurWeyl.HeckeSemisimpleGeneral
import QOU.MathlibExt.MatrixSemisimple
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# The `wtrace` quotient: semisimple, and of measured dimension

`WtraceRadicalQuotient.traceQuotEquiv` identifies `H_n(q)/rad(wtrace)` with the product of
matrix algebras indexed by the **at-most-two-row** partitions of `n+1`.  This file reads two
consequences off it.

## 🛑 Semisimplicity here is NOT new, and does not need `traceQuotEquiv`

Stated plainly so that nobody later cites `traceQuotEquiv` for it.  There are **three**
independent routes to `IsSemisimpleRing (TraceQuot …)`, and two of them predate this arc:

1. `QOU.SchurWeyl.isSemisimpleRing_hecke_generic` gives `IsSemisimpleRing (Hecke K q q⁻¹ n)`
   at general `n` over any `CharZero` field — itself transported along the pre-existing
   general-`n` `heckeWedderburn`, whose index set is **all** partitions.  Mathlib's
   `RingHom.isSemisimpleRing_of_surjective` ("any quotient of a semisimple ring is
   semisimple") then gives the quotient for free.
2. `QOU.SchurWeyl.semisimple_of_one_lt_unconditional`, at `1 < q`, likewise plus (1)'s
   second step.
3. Transport along `traceQuotEquiv`, which is what is written below because it is one line.

So `traceQuotEquiv` is **not** the first general-`n` Wedderburn decomposition in this corpus —
`heckeWedderburn` is, and it is older.  What `traceQuotEquiv` adds is *which blocks survive the
quotient*: the index set drops from all partitions of `n+1` to the at-most-two-row ones.  That
is a statement about the **index set**, and it is the only thing here that is genuinely
downstream of it.

## What IS downstream of `traceQuotEquiv` only: the dimension

`finrank_traceQuot` below is the increment.  `heckeWedderburn` gives
`finrank (Hecke ℝ q q⁻¹ n) = (n+1)!` by summing `(f^λ)²` over *all* `λ ⊢ n+1`; the quotient's
dimension is the same sum restricted to `ℓ(λ) ≤ 2`, and that restriction is exactly what the
radical identification buys.

**Why this number matters to the arc.** `TL_n(δ)` has dimension `catalan (n+1)`, and
`Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} (f^λ)²` is the Catalan number — so `finrank_traceQuot` is the left-hand
side of the dimension match that a `TL_n(δ)` identification would need.

🛑 **It is not that identification, and a dimension match is not an isomorphism of algebras.**
The identification needs `⟨U_i U_j U_i − v²·U_i⟩ = rad(tr_M)`, the open item
`QOU.MathlibExt.HeckeToTemperleyLieb` records; nothing here closes it.

### 🛑 CORRECTED — the Catalan identity IS proved at general `n`; the blocker is the HOOK LENGTH FORMULA

An earlier version of this docstring said the identity `Σ_{ℓ(λ) ≤ 2} (f^λ)² = catalan (n+1)` is
"proved nowhere in this corpus at general `n`", citing `TemperleyLiebNormalForm`'s
`card_zero … card_six` as `decide` at seven values.  **That cited a different identity.**  Those
seven are the *planar-diagram count* `Fintype.card (NormalIdx m) = catalan (m+1)`.  The
sum-of-squares identity is proved **at general `n`, sorry-free**:
`QOU.Mathlib.ballot_sq_sum_catalan` (reflection + Vandermonde — no induction, no tableau) and
`QOU.Mathlib.dimHLF_two_row_sq_sum`.  Bean `qou-7wf6`, PR #5360.

So what blocks `finrank_traceQuot = catalan (n+1)` is **neither** of those, but the two bridges
between them:

* **The hook length formula, and this is the real gap.**  `dimHLF l := (sz l).factorial /
  prodHooks l` is the hook-length *formula*, while `finrank_traceQuot` counts
  `Fintype.card (StandardYoungTableau …)`.  Identifying them is the Frame–Robinson–Thrall
  theorem, which is **absent from Mathlib** (`Mathlib/Combinatorics/Young/` carries no such
  result and not even `numStandardYoungTableaux`) and is proved in this corpus only for
  `n ≤ 4` — `QOU.Mathlib.SYTEnum.numStandardYoungTableaux_eq_dimHLF_le4`, whose hypothesis is
  literally `hmem : l ∈ shapesLE4`, discharged by `decide` — plus `n = 5` in
  `QOU.Mathlib.SYTFrobeniusDim`.
* **A reindexing** of `TwoRowIdx n` by second-row length, to meet
  `dimHLF_two_row_sq_sum`'s `∑ k ∈ Finset.range (n / 2 + 1)`.  Bounded finite combinatorics.

Consequence worth stating plainly: `QOU.Mathlib.TwoRowDimCatalan`'s own module docstring
describes `dimHLF_two_row_sq_sum` as *"a statement about actual standard-Young-tableau counts,
not about binomial coefficients"*.  Under `dimHLF`'s definition that is an **over-claim at
general `n`** — it is a statement about hook-length-formula values, and their identification
with actual counts is exactly the `n ≤ 4` bridge above.  Flagged, not edited: that file is not
in this tranche.

## The Mathlib position, measured

`IsSemisimpleRing (Matrix ι ι K)` is a **`proof_wanted`** in the pinned Mathlib
(`RingTheory/SimpleModule/Basic.lean`) — not proved there.  It is supplied by this corpus as
`QOU.MathlibExt.MatrixSemisimple.instIsSemisimpleRing_matrix`, which is why the import above
is to the corpus file.  Mathlib's own contributions are the finite-product instance,
`RingEquiv.isSemisimpleRing`, `Module.finrank_pi_fintype` and `Module.finrank_matrix`.

## Scope

`ℝ`, convention D, generic `q` — inherited unchanged from `traceQuotEquiv`.  `wtrace` is
`Hecke ℝ q q⁻¹ n →ₗ[ℝ] ℝ` by construction, so nothing here can be generalised past `ℝ` by
weakening this file; the pin is upstream.  (Contrast route 1 above, which *is* general over
any `CharZero` field — the `ℝ` is the trace's, not the semisimplicity's.)

-- Ref: [leitner2026] beans qou-s7z2, qou-cds1, qou-8iru.
-/

namespace QOU.SchurWeyl.WtraceRadicalSemisimple

open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.WtraceRadicalIdeal QOU.SchurWeyl.WtraceRadicalQuotient
open QOU.QBeta.MarkovTraceQuotient
open QOU.Mathlib (partitionShape StandardYoungTableau)

/-- The at-most-two-row index set is finite — a subtype of `Nat.Partition (n+1)`, which
Mathlib gives as a `Fintype`.  Stated via `Subtype.finite` so that no decidability of the
row-length predicate is needed. -/
instance instFiniteTwoRowIdx (n : ℕ) : Finite (TwoRowIdx n) := Subtype.finite

/-- **The target is semisimple.**  A finite product of matrix algebras over a division ring:
Mathlib's finite-product instance over this corpus's `instIsSemisimpleRing_matrix`. -/
instance instIsSemisimpleRingTwoRowBlocks (n : ℕ) : IsSemisimpleRing (TwoRowBlocks n) :=
  inferInstance

/-- **Semisimplicity by the route that does NOT use `traceQuotEquiv`** — a quotient of a
semisimple ring is semisimple.

This proves, rather than asserts, route (1) of the module docstring, and it is the honest
statement of where this fact comes from.  Note the hypotheses: **`hq0` and `hq2` only.**  The
equivalence route below additionally needs `hq21` and `hgen`, the latter strictly stronger than
`hq2` — so this route is not merely independent of `traceQuotEquiv`, it is *sharper*.

`RingCon.mk'` is the quotient map and is surjective by `Quot.exists_rep`; the semisimplicity of
the numerator is `isSemisimpleRing_hecke_generic`, which holds over any `CharZero` field. -/
theorem isSemisimpleRing_traceQuot_of_hecke {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    IsSemisimpleRing (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) := by
  haveI := isSemisimpleRing_hecke_generic (K := ℝ) q hq0 hq2 n
  exact RingHom.isSemisimpleRing_of_surjective
    (traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)).ringCon.mk'
    (fun x => Quot.exists_rep x)

/-- **`H_n(q) / rad(wtrace)` is semisimple, for every `n`, at convention D.**

🛑 Not new — see this file's module docstring: routes (1) and (2) reach it without
`traceQuotEquiv` at all, and route (1) is general over any `CharZero` field.  Written via the
equivalence only because that is one line.  Do not cite `traceQuotEquiv` as the reason this
holds. -/
theorem isSemisimpleRing_traceQuot {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    IsSemisimpleRing (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) :=
  (traceQuotEquiv hq0 hq2 hq21 hgen n).symm.toRingEquiv.isSemisimpleRing

/-- **The dimension of the quotient is the two-row sum of squares.**

`Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} (f^λ)²`, where `f^λ = card (StandardYoungTableau λ)`.  This is the one
statement in this file that is genuinely downstream of `traceQuotEquiv` rather than of the
older `heckeWedderburn`: the *restriction of the index set* to at-most-two rows is what the
radical identification buys, and the dimension is where that restriction becomes a number.

🛑 This is **not** `= catalan (n+1)`, and not a `TL_n(δ)` identification.  See the module
docstring for both gaps. -/
theorem finrank_traceQuot {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    Module.finrank ℝ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = ∑ lam : TwoRowIdx n,
          Fintype.card (StandardYoungTableau (partitionShape lam.1))
            * Fintype.card (StandardYoungTableau (partitionShape lam.1)) := by
  rw [(traceQuotEquiv hq0 hq2 hq21 hgen n).toLinearEquiv.finrank_eq,
    Module.finrank_pi_fintype]
  refine Finset.sum_congr rfl fun lam _ => ?_
  rw [Module.finrank_matrix, Module.finrank_self, mul_one]

/-- **The dimension is strictly positive** — the equation above is not `0 = 0`.

`finrank_traceQuot` is an equation between two things that could in principle both vanish, and
`AlgEquiv.ofBijective` upstream would have accepted a bijection of one-point algebras.  This
forecloses that reading by reusing `traceQuot_one_ne_zero`: the class of `1` differs from the
class of `0`, so the quotient is `Nontrivial`, and it is finite-dimensional by transport, so its
`finrank` is positive.  Hence the two-row sum of squares is nonzero as well. -/
theorem finrank_traceQuot_pos {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    0 < Module.finrank ℝ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) := by
  haveI : Nontrivial (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) :=
    ⟨⟨_, 0, traceQuot_one_ne_zero hq0 hq2 hq21 hgen n⟩⟩
  haveI : FiniteDimensional ℝ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) :=
    Module.Finite.equiv (traceQuotEquiv hq0 hq2 hq21 hgen n).symm.toLinearEquiv
  exact Module.finrank_pos

end QOU.SchurWeyl.WtraceRadicalSemisimple
