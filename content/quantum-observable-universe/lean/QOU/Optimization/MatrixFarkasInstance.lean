import QOU.Optimization.LPStrongDuality
import QOU.Mathlib.FinitelyGeneratedConeClosed

/-!
# The Farkas instance, discharged

Bean `qou/kl8z`. `QOU.Optimization.LPStrongDuality` derives
`lp_strong_duality`, `lp_dual_feasible_of_lower_bound` and
`lp_zero_duality_gap` sorry-free from the conditional class
`MatrixFarkas`, whose single field is the Farkas/Gale alternative — and
labels that field "the open analytic import", "the one unproved input in
the whole chain".

**It is no longer unproved.** `QOU.Mathlib.FinitelyGeneratedConeClosed`
proves it, via

```
isClosed_coneSpan → farkas_separation → farkas_vector
                  → farkas_inequality → farkas_alternative_real
```

and this file supplies the instance. With it in scope the three
strong-duality theorems are **unconditional**.

## Why the instance lives here and not in either neighbour

`FinitelyGeneratedConeClosed` is Mathlib-shaped: it knows about cones and
separation and deliberately does not import the QOU LP layer.
`LPStrongDuality` states the class and must not depend on the analytic
development. The instance is the only place the two meet, so it gets its
own file.

## What the instance does not settle

The class remains a `class`, and existing `[MatrixFarkas A a c]` binders
keep working — they are now discharged automatically rather than
assumed. The conditional framing in `LPStrongDuality`'s docstring is
therefore historical, not wrong: it describes how the layer was built.
-/

namespace QOU.Optimization

open QOU.Mathlib

variable {m n : ℕ}

/-- **Farkas' lemma for the standard-form LP, as an instance.**

The class field is `farkas_alternative` verbatim; the proof is
`QOU.Mathlib.farkas_alternative_real`, with the structures
`PrimalFeasible` / `DualFeasible` packed and unpacked around it.

Registered as an `instance`, so every `[MatrixFarkas A a c]` hypothesis
in this namespace now resolves without an assumption. -/
instance matrixFarkas_of_coneClosed
    (A : Fin m → Fin n → ℝ) (a : Fin m → ℝ) (c : Fin n → ℝ) :
    MatrixFarkas A a c where
  farkas_alternative γ hpf hlb := by
    obtain ⟨l, hdual, hobj⟩ :=
      farkas_alternative_real A a c γ
        (by
          obtain ⟨x₀, hx₀⟩ := hpf
          exact ⟨x₀, hx₀.eq, hx₀.nonneg⟩)
        (by
          rintro ⟨x', ⟨hxeq, hxnn⟩, hlt⟩
          exact hlb ⟨x', ⟨hxeq, hxnn⟩, hlt⟩)
    exact ⟨l, ⟨hdual⟩, hobj⟩

/-- **Strong duality, unconditional.** The same statement as
`lp_strong_duality`, with the Farkas hypothesis discharged by the
instance above rather than assumed. -/
theorem lp_strong_duality_uncond {A : Fin m → Fin n → ℝ} {a : Fin m → ℝ}
    {c : Fin n → ℝ} {x : Fin n → ℝ} (hx : PrimalOptimal A a c x) :
    ∃ l, DualOptimal A a c l ∧ dualObj a l = primalObj c x :=
  lp_strong_duality hx

end QOU.Optimization
