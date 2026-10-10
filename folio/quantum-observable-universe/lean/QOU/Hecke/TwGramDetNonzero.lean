import QOU.Hecke.TwGram
import QOU.Hecke.TwGramRankOne
import QOU.MathlibExt.RegTraceGramNondegenerate
import QOU.SchurWeyl.HeckeCarrierEquiv
import QOU.SchurWeyl.HeckeWedderburnGeneral

/-!
# QOU.Hecke.TwGramDetNonzero — `det(twGram) ≠ 0` at every rank

Bean `qou-kwoa`, closing the non-vanishing half of what `qou-0y6h` was opened for.

`QOU/Hecke/TwGram.lean` proves the implication `det(twGram) ≠ 0 ⟹ H_n(q) semisimple` and
records the converse content as the hard, open half:

> *"It does not compute the determinant. That is the remaining content of `qou-0y6h` —
> Geck–Pfeiffer 7.2.6, `det(Gram) = ∏_λ (Schur_λ)^{f^λ}` — and it is the hard half."*

**The determinant does not have to be computed to know it is nonzero.**  Semisimplicity of
the Hecke algebra is proved independently of any Gram determinant, via the Wedderburn
decomposition (`QOU.SchurWeyl.heckeWedderburn`), and the *converse* of the Gram criterion —
`QOU.MathlibExt.regTraceGram_det_ne_zero_of_algEquiv_pi_matrix` — turns that into
`det ≠ 0` directly.  The Schur-element product is still needed for the determinant's
**value**; it is not needed for its non-vanishing.

## What is proved

* `twGram_det_ne_zero` — `det (twGram K (q ^ 2) n) ≠ 0`, for any field of characteristic zero
  and any `q ≠ 0` that is not a root of unity, at **every** `n`.
* `twGram_det_ne_zero_rank_one_agrees` — an independent cross-check.  The only rank whose
  determinant was ever computed by hand is `n = 1`
  (`QOU.Hecke.TwBasis.twGram_det_rank_one : det = (1 + q) ^ 2`).  Specialised at `q ^ 2` that
  says `det = (1 + q ^ 2) ^ 2`, which is nonzero exactly when `q ^ 4 ≠ 1` — and that is what
  `NotRootOfUnity q` supplies.  The general theorem and the hand computation therefore agree
  at the one point where both are available, on the same hypothesis, by two different routes.

## Why the statement is at `q ^ 2`

Exactly the reason recorded in `QOU/SchurWeyl/HeckeCarrierSemisimple.lean`:
`skeinIwahoriEquiv` relates the skein algebra at `q` to the Iwahori algebra — the `T_w` /
`twGram` carrier — at `q ^ 2`, and a general field need not contain a square root.  Over `ℝ`,
or over any field where the Iwahori parameter is a square, `twGram_det_ne_zero_of_sq` gives
the statement at `Q` directly.

## Scope

This is a **magnitude-axis** fact and bears nothing on the P≠NP wall, as `TwGram.lean` also
records.  What it settles is that the `(n+1)! × (n+1)!` table of Markov-trace observables
`tr(L_{T_v T_w})` is nonsingular at every rank — which is the property the Gram criterion was
introduced to use.
-/

namespace QOU.Hecke.TwBasis

open QOU.MathlibExt QOU.SchurWeyl

/-- **`det(twGram) ≠ 0` at every rank**, over any characteristic-zero field, for `q ≠ 0` not a
root of unity.

Composes two isomorphisms — `skeinIwahoriEquiv` (Iwahori at `q ^ 2` is the skein algebra at
`q`) and `heckeWedderburn` (the skein algebra is a product of matrix algebras) — and feeds the
result to the converse Gram criterion.  No determinant is evaluated anywhere in the proof. -/
theorem twGram_det_ne_zero {K : Type*} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    (twGram K (q ^ 2) n).det ≠ 0 := by
  haveI : FiniteDimensional K (QOU.Hecke.IwahoriHecke K (q ^ 2) n) :=
    FiniteDimensional.of_fintype_basis (basisTwOfField K (q ^ 2) n)
  exact regTraceGram_det_ne_zero_of_algEquiv_pi_matrix
    ((skeinIwahoriEquiv q hq0 n).symm.trans (heckeWedderburn q hq0 hq2 n))
    (basisTwOfField K (q ^ 2) n)

/-- **The same at an Iwahori parameter `Q` given as a square.**  The shape a caller holding
`Q` wants, once it can exhibit a square root — mirroring
`QOU.SchurWeyl.isSemisimpleRing_iwahoriHecke_of_sq`. -/
theorem twGram_det_ne_zero_of_sq {K : Type*} [Field K] [CharZero K] {Q q : K}
    (hQ : Q = q ^ 2) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    (twGram K Q n).det ≠ 0 := by
  subst hQ
  exact twGram_det_ne_zero q hq0 hq2 n

/-- **Cross-check at the one rank computed by hand.**

`twGram_det_rank_one` gives `det (twGram K Q 1) = (1 + Q) ^ 2` by direct evaluation of the
four Markov-trace entries.  At `Q = q ^ 2` its non-vanishing is `q ^ 4 ≠ 1`, which is exactly
what `NotRootOfUnity q` supplies — so this reaches the same conclusion as
`twGram_det_ne_zero` at `n = 1` by a completely different route (an explicit `2 × 2`
determinant, rather than Wedderburn plus the trace-form radical).

Kept as a regression: an error in either route would show up as a disagreement here. -/
theorem twGram_det_ne_zero_rank_one_agrees {K : Type*} [Field K] (q : K)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    (twGram K (q ^ 2) 1).det ≠ 0 := by
  rw [twGram_det_rank_one]
  refine pow_ne_zero 2 fun h => ?_
  refine hq2 4 (by norm_num) ?_
  have key : q ^ 4 = (1 + q ^ 2) * (q ^ 2 - 1) + 1 := by ring
  rw [key, h, zero_mul, zero_add]

end QOU.Hecke.TwBasis
