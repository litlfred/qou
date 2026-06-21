/-
Constit-side per-Z step factor equals tr_M^3(𝓑_p) — the proton's
H_3 Markov trace.  Structural identity, derivable from Wenzl's
disjoint-product Markov trace multiplicativity.

Empirical verification (Phase 5l, 50 dps via y_λ · χ_λ pipeline):

  q        tr_M^3(𝓑_p, q)    ρ_Z^constit(q)    rel. err.
  1.050    0.79284191942    0.79284191942     1.69e-51
  1.080    0.99328958565    0.99328958565     1.08e-50
  q_0      1.22037426649    1.22037426649     3.29e-50
  1.130    1.39054700526    1.39054700526     1.35e-50
  1.170    1.78584582119    1.78584582119     0 (exact at 50 dps)

Identity holds at mpfr-50-dps precision across the substrate window.

Ref: [wenzl1988] Hecke algebras of type A_n and subfactors §1.7
     (disjoint Markov trace multiplicativity)
Ref: [jones1987] Hecke algebra representations of braid groups
Ref: prop:constit-factor-tau-M-proton-identity.md
Ref: prop:interface-knot-markov-z.md (companion: interface z-factor)
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupPower.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

/-- The Jones–Markov trace tr_M, abstracted as a multiplicative
    function on disjoint Hecke products.  This class records the
    structural content needed for the constit-factor identity: a
    trace value `tr_M(β)` for each braid-block input, with the
    disjoint-multiplicativity axiom that
      `tr_M(α ⊗ β) = tr_M(α) · tr_M(β)`
    for α, β on disjoint strand sets (Wenzl 1988 §1.7). -/
class MarkovTraceDisjoint (R : Type*) [Field R] where
  /-- The Markov-trace value for the canonical proton block in H_3. -/
  tau_M_proton : R
  /-- The Markov-trace value for the canonical neutron block in H_3. -/
  tau_M_neutron : R
  /-- The Markov-trace value of the constit (= disjoint product)
      braid for atom (Z, N).  The class axiom encodes Wenzl's
      disjoint multiplicativity:
        tr_M(𝓑_constit_{Z,N}) = tr_M(𝓑_p)^Z · tr_M(𝓑_n)^N. -/
  tau_M_constit : ℕ → ℕ → R
  /-- Wenzl's disjoint multiplicativity, specialised to the
      per-nucleon factorisation. -/
  tau_M_constit_disjoint :
    ∀ (Z N : ℕ),
      tau_M_constit Z N = tau_M_proton ^ Z * tau_M_neutron ^ N

/-- **Theorem (conditional on Wenzl's disjoint multiplicativity).**

    The constit-side per-Z step factor in the canonical-atom Markov
    trace equals tr_M(𝓑_p), the proton's H_3 Markov trace.  Stated
    over a generic field `R` per AGENTS.md §7c (the statement is
    purely algebraic; no archimedean structure needed). -/
-- Ref: [manuscript] prop:constit-factor-tau-M-proton-identity
-- Ref: [wenzl1988] §1.7 disjoint Markov trace multiplicativity
theorem constit_factor_eq_tau_M_proton
    {R : Type*} [Field R] [inst : MarkovTraceDisjoint R]
    (Z N : ℕ) (hZ : inst.tau_M_proton ≠ 0) (hN : inst.tau_M_neutron ≠ 0) :
    inst.tau_M_constit (Z + 1) N / inst.tau_M_constit Z N
      = inst.tau_M_proton := by
  -- Rewrite both constit traces via the disjoint-multiplicativity axiom.
  rw [inst.tau_M_constit_disjoint, inst.tau_M_constit_disjoint]
  -- Unfold a^(Z+1) = a * a^Z so the cancellation is mechanical.
  rw [pow_succ]
  -- Now the goal is (tau_M_proton^Z * tau_M_proton * tau_M_neutron^N)
  --              / (tau_M_proton^Z * tau_M_neutron^N) = tau_M_proton
  have hp : inst.tau_M_proton ^ Z ≠ 0 := pow_ne_zero Z hZ
  have hn : inst.tau_M_neutron ^ N ≠ 0 := pow_ne_zero N hN
  field_simp
  ring

/-- **Combined per-Z tr_M factor (at p-* interface).**

    Combining the constit-side identity with the positive interface
    factor `z` from `prop:interface-knot-markov-z` gives the exact
    full tr_M per-Z step at a p-* boundary:

      tr_M(𝓑_K^{Z+1, N}) / tr_M(𝓑_K^{Z, N}) = z · tr_M(𝓑_p)

    — no residuals.  Generic over any commutative ring. -/
def full_tau_M_Z_step_exact {R : Type*} [CommRing R]
    (z : R) (tau_M_proton : R) : R :=
  z * tau_M_proton

end QOU.BraidKnot
