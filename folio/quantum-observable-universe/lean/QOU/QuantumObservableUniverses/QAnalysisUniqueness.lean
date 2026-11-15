import QOU.QuantumObservableUniverses.QAnalysis

/-!
# QOU.QuantumObservableUniverses.QAnalysisUniqueness

The three q-analysis uniqueness statements, **conditional** on the one
rigidity step their narrative proofs assert, and proved from it.

## Why they are conditional

Until 2026-09-06 each was an unconditional axiom, and all three were
false -- see `QAnalysisUniquenessCounterexamples`.  The structures carry
their ambient maps as free function fields, so agreement of those maps
does not pin the distinguished element.

The repair is not a new hypothesis invented to rescue the claim.  Each
`*_rigid` hypothesis below is a **verbatim restatement of a sentence the
block's own narrative proof already asserts**:

* `prf:q-exponential-unique` -- *"The flow equation on primitives has
  only the trivial solution"* -> `flow_rigid`.
* `prf:q-logarithm-unique` -- *"a primitive fixed by `D_q` with trivial
  counit vanishes"* -> `prim_rigid`.
* `prf:q-dilogarithm-unique` -- *"The solution space of the level-2
  shuffle recursion is one-dimensional modulo lower-level primitives"*
  -> `pentagon_rigid`.

Each is a **kernel-triviality** statement about a single element, from
which two-element uniqueness is *derived* by subtraction.  That is what
keeps these off the self-assuming projection §3b-cond item 5 forbids: a
hypothesis of the form "any two agree" would be the conclusion; a
hypothesis of the form "the difference vanishes" is a strictly weaker
input the proof has to work with.

The narrative proofs also silently need the ambient maps to be
**additive** -- they subtract two grouplikes and apply `Δ`, `ε`, `D_q`
to the difference.  A bare carrier type supports none of that, which is
the deeper reason the original encodings could not be the narrative
proofs.  Additivity is therefore also explicit, over `AddCommGroup`.

## What is still open

Discharging any `*_rigid` hypothesis needs a graded q-shuffle Hopf
algebra -- the degree bound is what makes the narrative's "iterating
`D_q` forces all coefficients to vanish" work -- and the corpus does not
have one.  That gap is now *visible in the type* instead of hidden in an
axiom.

## References

- [kassel1995] Quantum Groups (Springer GTM 155), §III.3, §IV.3
-/

namespace QOU

noncomputable section

/-- **Uniqueness of the q-exponential grouplike, conditional on flow
    rigidity.**

    `flow_rigid` is the narrative proof's own step: an element fixed by
    the Jackson derivative with vanishing counit is zero.  Given it, the
    difference of two grouplikes sharing `counit` and `D_q` is such an
    element. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §III.3
theorem QExponential.unique_of_flow_rigid {H : Type*} [AddCommGroup H]
    (e₁ e₂ : QExponential H)
    (h_counit : e₁.counit = e₂.counit) (h_Dq : e₁.D_q = e₂.D_q)
    (hD_sub : ∀ x y : H, e₁.D_q (x - y) = e₁.D_q x - e₁.D_q y)
    (hε_sub : ∀ x y : H, e₁.counit (x - y) = e₁.counit x - e₁.counit y)
    (flow_rigid : ∀ x : H, e₁.D_q x = x → e₁.counit x = 0 → x = 0) :
    e₁.e_q = e₂.e_q := by
  refine sub_eq_zero.mp (flow_rigid _ ?_ ?_)
  · rw [hD_sub, e₁.flow_invariant, h_Dq, e₂.flow_invariant]
  · rw [hε_sub, e₁.counit_eq_one, h_counit, e₂.counit_eq_one, sub_self]

/-- **Uniqueness of the q-logarithm primitive, conditional on primitive
    rigidity.**

    `prim_rigid` is the narrative proof's own step: a primitive with
    vanishing counit is zero. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV.3
theorem QLogarithm.unique_of_prim_rigid {H : Type*} [AddCommGroup H]
    (l₁ l₂ : QLogarithm H)
    (h_coprod : l₁.coprod = l₂.coprod) (h_counit : l₁.counit = l₂.counit)
    (hΔ_fst : ∀ x y : H, (l₁.coprod (x - y)).1 = (l₁.coprod x).1 - (l₁.coprod y).1)
    (hΔ_snd : ∀ x y : H, (l₁.coprod (x - y)).2 = (l₁.coprod x).2 - (l₁.coprod y).2)
    (hε_sub : ∀ x y : H, l₁.counit (x - y) = l₁.counit x - l₁.counit y)
    (prim_rigid : ∀ x : H, (l₁.coprod x).1 = x → (l₁.coprod x).2 = x →
                            l₁.counit x = 0 → x = 0) :
    l₁.log_q = l₂.log_q := by
  refine sub_eq_zero.mp (prim_rigid _ ?_ ?_ ?_)
  · rw [hΔ_fst, l₁.primitive_left, h_coprod, l₂.primitive_left]
  · rw [hΔ_snd, l₁.primitive_right, h_coprod, l₂.primitive_right]
  · rw [hε_sub, l₁.counit_eq_zero, h_counit, l₂.counit_eq_zero, sub_self]

/-- **Uniqueness of the q-dilogarithm evaluation, conditional on
    pentagon rigidity.**

    The conclusion is about `Li2_eval`, **not** `Li2`, and that is a
    correction rather than a weakening: `Li2` is not mentioned by the
    `pentagon` field, so no hypothesis about the pentagon can reach it.
    The refuted axioms concluded `Li2.1 = Li2.1`, which the pentagon
    never constrained.

    The pentagon relation is additive in `Li2_eval`, so the difference
    of two solutions is again a solution; `pentagon_rigid` -- the
    narrative proof's one-dimensionality step -- then forces it to
    vanish. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV
theorem QDilogarithm.eval_unique_of_pentagon_rigid {H : Type*} [AddCommGroup H]
    (L₁ L₂ : QDilogarithm H)
    (h_mul : L₁.mul = L₂.mul) (h_compl : L₁.compl = L₂.compl)
    (h_div : L₁.div = L₂.div)
    (pentagon_rigid : ∀ f : H → H,
      (∀ x y : H, f y + f x =
        f (L₁.mul x y) +
        f (L₁.div (L₁.mul x (L₁.compl y)) (L₁.compl (L₁.mul x y))) +
        f (L₁.div (L₁.mul y (L₁.compl x)) (L₁.compl (L₁.mul x y)))) →
      f = 0) :
    L₁.Li2_eval = L₂.Li2_eval := by
  have hd : (fun z => L₁.Li2_eval z - L₂.Li2_eval z) = 0 := by
    refine pentagon_rigid _ ?_
    intro x y
    have h1 := L₁.pentagon x y
    have h2 := L₂.pentagon x y
    rw [← h_mul, ← h_compl, ← h_div] at h2
    have h3 := congrArg₂ (· - ·) h1 h2
    dsimp only at h3 ⊢
    abel_nf at h3 ⊢
    exact h3
  funext z
  simpa [sub_eq_zero] using congrFun hd z

end

end QOU
