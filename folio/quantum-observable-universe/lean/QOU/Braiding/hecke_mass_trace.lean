import QOU.Hecke.Algebra
import QOU.Hecke.MarkovTrace

/-!
# QOU.Braiding.hecke_mass_trace — `𝔪(ϱ_β) = |tr_M(Φ_mass(β))|`

**Conjecture** ([`conj:hecke-mass-trace`](../../../mass-theory/hecke-mass-trace.md)).

*Let `(𝐂, A, τ)` be a QOU, let `ϱ : 𝟙 → A` be a vortex with braid
representative `β ∈ B_n`, and let `Φ_mass(β) ∈ H_n(R, q)` be its
Hecke mass element.  The categorical mass equals the norm of the
Markov trace of the Hecke mass element:*

```
  𝔪(ϱ_β) = | tr_M(Φ_mass(β)) |
```

*Moreover the topological decomposition descends:*

```
  tr_M(Φ_mass(β)) = tr_M(Φ^desc(β)) + Σ_i tr_M(Φ^trans_i(β)).
```

The Lean encoding uses the existing `QOU.Hecke.MarkovTrace`
infrastructure for the Markov trace, with abstract fields for the
Hecke mass element and its descended and transient components.

The class `HeckeMassTraceContext` is the conjecture carrier. Its field
`claim_cat_mass_eq_norm_trace` is the open equality; no instance exists.
The trace-level split is not assumed: `trace_split_of_phi_split` derives
it from the element-level hypothesis `phi_split` by linearity of `tr_M`.
Until 2026-11-20 this file carried the split as a second class field and
a `def hecke_mass_trace` that only returned the two fields; that
self-projection is removed (bean qou-tm3c).

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/hecke-mass-trace.md
-/

namespace QOU.Braiding

universe u

/-- Conjecture carrier for `conj:hecke-mass-trace`, typed against the
    existing `QOU.Hecke.MarkovTrace` infrastructure. -/
class HeckeMassTraceContext where
  -- Witness: computations/none
  /-- The coefficient ring `R`. -/
  R : Type u
  ringR : CommRing R
  invR  : Inv R
  /-- The Hecke parameter `q : R`. -/
  q : R
  /-- The strand count `n`. -/
  n : ℕ
  /-- The Hecke algebra `A = H_n(R, q)`. -/
  A : Type u
  ringA  : Ring A
  algebraA : @Algebra R A ringR.toCommSemiring ringA.toSemiring
  /-- The Hecke-algebra typeclass instance. -/
  heckeInst : @QOU.Hecke.HeckeAlgebra R n q A ringR invR ringA algebraA
  /-- The Markov-trace instance on `A`. -/
  markovInst : @QOU.Hecke.MarkovTrace R n q A ringR invR ringA algebraA heckeInst
  /-- The Hecke mass element `Φ_mass(β) ∈ A`. -/
  Phi_mass : A
  /-- The descended component `Φ^desc(β) ∈ A`. -/
  Phi_desc : A
  /-- The transient components `Φ^trans_i(β) ∈ A` (finite list). -/
  Phi_trans : List A
  /-- The categorical mass `𝔪(ϱ_β) : R`. -/
  cat_mass : R
  /-- The `|·| : R → R` absolute-value-like norm. -/
  norm : R → R
  /-- **The conjecture** (`conj:hecke-mass-trace`): the categorical mass
      equals the norm of the Markov trace of the Hecke mass element.
      This field is the open content. No instance is constructed in the
      corpus, and nothing in this file derives it. -/
  claim_cat_mass_eq_norm_trace :
    cat_mass = norm (markovInst.trace Phi_mass)
  /-- **Hypothesis**: the Hecke mass element splits as its descended
      component plus the sum of its transient components. This is the
      image under `τ` of the idempotent splitting by the descent
      involution. It is a hypothesis here, not a consequence. -/
  phi_split :
    Phi_mass = Phi_desc + Phi_trans.foldr (fun a acc => a + acc) 0

/-- The Markov trace commutes with the right fold that sums a list. This is
    linearity of `tr_M`, by induction on the list. -/
-- Ref: [kassel1995] Ch. X (the Markov trace is R-linear)
theorem trace_foldr_add [ctx : HeckeMassTraceContext] (l : List ctx.A) :
    letI := ctx.ringR
    letI := ctx.invR
    letI := ctx.ringA
    letI := ctx.algebraA
    ctx.markovInst.trace (l.foldr (fun a acc => a + acc) 0)
      = l.foldr (fun a acc => ctx.markovInst.trace a + acc) (0 : ctx.R) := by
  letI := ctx.ringR
  letI := ctx.invR
  letI := ctx.ringA
  letI := ctx.algebraA
  induction l with
  | nil => simp only [List.foldr_nil, map_zero]
  | cons a t ih => rw [List.foldr_cons, List.foldr_cons, map_add, ih]

/-- **Trace-level split** (the second display of `conj:hecke-mass-trace`).

    Derived from the element-level hypothesis `phi_split` and linearity of
    the Markov trace. It does not use the conjectural field
    `claim_cat_mass_eq_norm_trace`, and it says nothing about norms: the
    norm-level decomposition of the mass is `conj:topological-mass`. -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
theorem trace_split_of_phi_split [ctx : HeckeMassTraceContext] :
    letI := ctx.ringR
    letI := ctx.invR
    letI := ctx.ringA
    letI := ctx.algebraA
    ctx.markovInst.trace ctx.Phi_mass
      = ctx.markovInst.trace ctx.Phi_desc
        + ctx.Phi_trans.foldr (fun a acc => ctx.markovInst.trace a + acc) (0 : ctx.R) := by
  letI := ctx.ringR
  letI := ctx.invR
  letI := ctx.ringA
  letI := ctx.algebraA
  rw [ctx.phi_split, map_add, trace_foldr_add]

end QOU.Braiding
