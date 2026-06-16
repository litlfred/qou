import QOU.Hecke.Algebra
import QOU.Hecke.MarkovTrace

/-!
# QOU.Braiding.hecke_mass_trace — `𝔪(ϱ_β) = |tr_M(Φ_mass(β))|`

**Proposition** ([`prop:hecke-mass-trace`](../../../quantum-observable-universe/braids-and-knots/hecke-mass-trace.md)).

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
Hecke mass element and the topological decomposition components.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hecke-mass-trace.md
-/

namespace QOU.Braiding

universe u

/-- Abstract context for the `hecke_mass_trace` claim — typed against
    the existing `QOU.Hecke.MarkovTrace` infrastructure. -/
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
  heckeInst : @QOU.Hecke.HeckeAlgebra R n q A ringR ringA algebraA
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
  /-- **Manuscript claim (i)**: the categorical mass equals the norm of
      the Markov trace of the Hecke mass element.  Carried as a class
      field per CLAUDE.md §3b-cond — downstream consumers take
      `[HeckeMassTraceContext]` as an explicit hypothesis to obtain this
      identity without a naked `sorry`; the identity is conditional on
      the class instance, not an unconditional theorem. -/
  claim_cat_mass_eq_norm_trace :
    cat_mass = norm (markovInst.trace Phi_mass)
  /-- **Manuscript claim (ii)**: the Markov trace decomposes additively
      over the descended + transient pieces.  The fibre functor `τ` is
      exact and monoidal, so the mass identity descends to `H_n(R, q)`;
      `tr_M` is `R`-linear in its argument.  §3b-cond class field. -/
  claim_trace_decomposition :
    markovInst.trace Phi_mass
      = markovInst.trace Phi_desc
        + (Phi_trans.foldr (fun a acc => markovInst.trace a + acc) 0)

/-- **Hecke-mass-trace identity** ([`prop:hecke-mass-trace`]).

    The categorical mass coincides with the norm of the Markov trace
    of the Hecke mass element; the trace decomposes additively over
    the descended + transient pieces. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hecke-mass-trace.md
theorem hecke_mass_trace [ctx : HeckeMassTraceContext] :
    -- (i) Mass = norm of Markov trace
    (ctx.cat_mass = ctx.norm (ctx.markovInst.trace ctx.Phi_mass)) ∧
    -- (ii) Topological decomposition descends to H_n(R, q)
    (ctx.markovInst.trace ctx.Phi_mass
       = ctx.markovInst.trace ctx.Phi_desc
         + (ctx.Phi_trans.foldr (fun a acc => ctx.markovInst.trace a + acc) 0)) :=
  -- The manuscript's categorical argument is carried as the two class
  -- fields `claim_cat_mass_eq_norm_trace` + `claim_trace_decomposition`
  -- (§3b-cond); this theorem recombines them.
  -- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hecke-mass-trace.md
  ⟨ctx.claim_cat_mass_eq_norm_trace, ctx.claim_trace_decomposition⟩

end QOU.Braiding
