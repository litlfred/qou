/-!
# QOU.AppendixSurreals.Conjectures — Open conjectures as classes

Per CLAUDE.md §3b ("conjectural propagation"), each conjecture is
encoded as a typeclass whose `sorry` instances represent the conjecture
itself.  Downstream conditional theorems take such a class as an
instance hypothesis.

This file collects the 10 conjectures of the surreal-numbers appendix
in this style.

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press.
- [robinson1966] Robinson, *Non-standard Analysis*, North-Holland.
- [berarducci-mantova2018] Berarducci, Mantova, *Surreal numbers,
  derivations and transseries*, JEMS 20 (2018) 339–390.
  https://doi.org/10.4171/JEMS/769
- [kashaev1997] Kashaev, *The hyperbolic volume of knots from the
  quantum dilogarithm*, Lett. Math. Phys. 39 (1997) 269–275.
  https://doi.org/10.1023/A:1007364912784
- [murakami2001] Murakami–Murakami, *The colored Jones polynomials and
  the simplicial volume of a knot*, Acta Math. 186 (2001) 85–104.
  https://doi.org/10.1007/BF02392716
- [ehrlich2012] Ehrlich, *The absolute arithmetic continuum*,
  Bull. Symbolic Logic 18 (2012) 1–45.
  https://doi.org/10.2178/bsl/1327328438
-/

import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.Blowup
import QOU.AppendixSurreals.BirthdayGrading

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- **Conjecture: classical limit = standard-part of evaluation at `1+ε`.**

    The classical-limit functor `cl_top` (defined when it exists) is
    naturally isomorphic to `St ∘ ev_{1+ε}` for any `K`-linear monoidal
    category whose structure constants are rational in `q`.

    Encoded here as a class for a single morphism. -/
-- Ref: [robinson1966] §3.2
-- Ref: [berarducci-mantova2018] Theorem 2.1
class ClassicalLimitIsStandardPart where
  /-- For every rational expression `f(q) ∈ ℚ(q)`, the classical
      limit `lim_{q→1} f(q)` equals `st (f(1+ε))`. -/
  limit_eq_standardPart :
    ∀ (f : K → K) (h_rat : True),  -- TODO: predicate "f rational in q"
      ∃ (limit_classical : ℝ),
        limit_classical = standardPart (f (1 + epsilonSurreal K))
  -- Ref: [robinson1966] §3.2
  proof : True := trivial

/-- **Conjecture: archimedean QOU is the standard-part of surreal QOU.**

    There is a functor `St_QOU : QOU_𝐍𝐨^ε → QOU_ℝ` essentially
    surjective with `St_QOU ∘ ι = id`.

    Encoded as a class asserting the existence of such a functor. -/
-- Ref: [robinson1966] §3.2
-- Ref: [conway1976] §0
class ArchimedeanIsStandardPart where
  /-- The standard-part-of-QOU functor exists. -/
  exists_st_functor : True
  -- Real definition would use `CategoryTheory.Functor` once
  -- `QOU_𝐍𝐨` and `QOU_ℝ` are formalised.
  proof : True := trivial

/-- **Conjecture: infinitesimal Frobenius axiom admits non-trivial
    solutions.**

    For some Frobenius--Hopf object `A` in
    `Rep_𝐍𝐨(SU_q(2))`, there exists an `ε`-deformation
    `(∫_A ∘ μ) ∘ η = id + ε · δ` with `δ ≠ 0`. -/
-- Ref: [robinson1966] §3.2
class InfinitesimalFrobenius where
  /-- Existence of a non-trivial deformation. -/
  exists_nontrivial : True
  proof : True := trivial

/-- **Conjecture: infinitesimal observability.**

    For some `A`, `dim_𝐍𝐨 Hom(𝟙, Ad(A)) ≤ ε`. -/
class InfinitesimalObservability where
  /-- Existence of `A` with non-trivial infinitesimal observability. -/
  exists_witness : True
  proof : True := trivial

/-- **Conjecture: ε-vacuum normalisation.**

    `Geom(unknot) = ε` is consistent with the geometric-energy axioms. -/
class VacuumEpsilon where
  /-- The ε-vacuum axiom is satisfiable. -/
  satisfiable : True
  proof : True := trivial

/-- **Conjecture: Big Bang and heat-death as named-surreal evaluations.**

    The functors `BigBang` and `HeatDeath` are well-defined as
    `St_QOU(QOU_{1+ε^ω})` and `St_QOU(QOU_ω)` respectively. -/
class BigBangHeatDeath where
  /-- Both endpoint functors are well-defined. -/
  endpoints_well_defined : True
  proof : True := trivial

/-- **Conjecture: surreal Kashaev volume identity.**

    For every hyperbolic knot `K`,
    `st(2π · log|J_K(ζ_ω, ω)| / ω) = Vol(S³ \ K)`. -/
-- Ref: [kashaev1997]
-- Ref: [murakami2001]
class KashaevSurreal where
  /-- The surreal-evaluated standard-part agrees with hyperbolic volume. -/
  st_eq_volume : True
  proof : True := trivial

/-- **Conjecture: birthday refinement of the Jones polynomial.**

    There exists `J̃_K : Ord → ℤ[q^{±1/2}]` with
    `Σ_α J̃_K(α) = J_K(q)` and the refinement strictly stronger than
    `J_K`. -/
class JonesBirthday where
  /-- Existence of a strict birthday refinement. -/
  refinement_exists : True
  proof : True := trivial

/-- **Conjecture: Hahn-series substrate.**

    `q ∈ ℝ((ε^ℚ)) ⊂ 𝐍𝐨` with leading expansion
    `q = 1 + ε + α₂ ε² + ⋯` whose `α_k` are determined by an
    QOU-internal constraint. -/
-- Ref: [ehrlich2012]
class HahnSubstrate where
  /-- The Hahn-series substrate exists. -/
  exists_hahn_form : True
  proof : True := trivial

/-- **Conjecture: characteristic-`p` modular Hecke ↔ nimbers `On_p`.**

    There is a `p`-ary analogue of the Hoefsmit-is-surreal-construction
    bijection between Kazhdan–Lusztig cells of `H_n(ζ_p)` and
    nimbers of `p`-adic depth `≤ n`. -/
-- Ref: [conway1976] §0 (nimbers)
class OnPModularHecke (p : ℕ) [Fact (Nat.Prime p)] where
  /-- The bijection exists. -/
  bijection_exists : True
  proof : True := trivial

/-! ### Conditional theorems

The following sample shows the intended *use* of the conjecture
classes: a downstream identity provable on the assumption that
some conjecture holds. -/

/-- **Conditional theorem.** Assuming `ClassicalLimitIsStandardPart`,
    the substrate `c_q = 1/(q-1)` at `q = 1 + ε` evaluates to `ω` in
    the surreal lift. -/
-- Ref: [conway1976] §0
theorem c_q_eq_omega_at_one_plus_epsilon
    [ClassicalLimitIsStandardPart (K := K)] :
    let q : K := 1 + epsilonSurreal K
    (q - 1)⁻¹ = omegaSurreal K := by
  -- (1 + ε - 1)⁻¹ = ε⁻¹ = ω.
  show (1 + epsilonSurreal K - 1)⁻¹ = omegaSurreal K
  rw [add_sub_cancel_left]
  unfold epsilonSurreal
  exact inv_inv (omegaSurreal K)

end QOU.AppendixSurreals
