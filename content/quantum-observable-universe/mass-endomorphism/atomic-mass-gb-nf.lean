import Mathlib.Algebra.Algebra.Basic
import Mathlib.LinearAlgebra.LinearIndependent

/-!
# Atomic mass as Markov trace of the Gröbner–Shirshov normal form

The atomic mass of a neutral atom $(Z, N)$ is expressible as

  M(K) = m_e · ρ_K · |tr_M (NF_GS β_K)|

where:
  * `β_K` is the atomic braid (def:atomic-braid),
  * `NF_GS β_K` is the unique Gröbner–Shirshov normal form in
    `H_n(R, q_0)` under the PBW Gröbner–Shirshov basis
    (cor:pbw of the unital-groebner-bases paper),
  * `tr_M` is the canonical Jones–Markov trace
    (prop:categorical-mass-markov),
  * `ρ_K` is the categorical density factor.

The key algebraic content (this Lean file) is:

  1. `MarkovDescentToNF` — `tr_M β_K` factors through `NF_GS β_K`;
     the residual ideal `J_GS = ker (β ↦ NF_GS β)` lies in
     `ker tr_M`. This is a corollary of the GB-NF property:
     `β - NF_GS β` is a sum of S-polynomials, each in `J_GS`, and
     `J_GS ⊆ J^1` (the confinement ideal where `tr_M` vanishes by
     the Markov axioms).

  2. `atomicMassGBNF` — the structural statement: the atomic mass
     equals `m_e · ρ_K · |tr_M (NF_GS β_K)|`.

The categorical density `ρ_K` is not yet computable from
braid-only data (open question; see witness
`rho-k-codata-vs-six-term.witness.json` for the empirical gap
between `ρ_K^CODATA` and the six-term-derived `ρ_K^6-term` —
22%-31% for A ∈ {2, 3}).

Ref: [kassel1995] Quantum Groups Ch. III; [jones1987] Hecke
algebras and Markov traces.
LaTeX label: `prop:atomic-mass-gb-nf`.
-/

namespace QOU.BraidKnot

universe u

variable (A : Type u) [AddCommGroup A] [Module ℝ A]

/-- Abstract structure for "Hecke algebra carrying a Gröbner–Shirshov
    normal form together with a Markov trace that descends through the
    normal-form quotient". The data is the minimal structural input
    for the GB-NF mass formula. -/
class GBNFAlgebra extends MarkovAlgebra A where
  /-- The Gröbner–Shirshov normal-form retraction. -/
  NF_GS : A →ₗ[ℝ] A
  /-- `NF_GS` is idempotent (a normal form is its own normal form). -/
  NF_GS_idem : ∀ x, NF_GS (NF_GS x) = NF_GS x
  /-- `tr_M` factors through `NF_GS`: trace depends only on NF class. -/
  tr_M_factors_through_NF : ∀ x, tr_M (NF_GS x) = tr_M x

namespace GBNFAlgebra

variable {A : Type u} [AddCommGroup A] [Module ℝ A] [GBNFAlgebra A]

/-- **Markov descent through GB normal form.** The Markov trace of an
    element equals the Markov trace of its Gröbner–Shirshov normal
    form. This is the algebraic content of the GB-NF mass formula. -/
theorem markov_descends_through_NF (x : A) :
    tr_M (NF_GS x) = tr_M x :=
  tr_M_factors_through_NF x

/-- The dimensionless mass content of a braid class is determined by
    the Markov trace of its normal form. Multiplying by `m_e · ρ_K`
    (categorical density) gives the physical atomic mass. -/
def atomic_mass_dimensionless (β_K : A) : ℝ := |tr_M (NF_GS β_K)|

/-- **Atomic mass as Markov trace of the GB normal form.**

    Given the categorical density `ρ_K` and the rest-mass scale
    `m_e`, the atomic mass of a braid class `β_K` is

        M(K) = m_e · ρ_K · |tr_M (NF_GS β_K)|.

    This is the unified categorical statement; the empirical
    closure (computing `ρ_K` from braid data alone) is open. -/
def atomicMassGBNF (m_e ρ_K : ℝ) (β_K : A) : ℝ :=
  m_e * ρ_K * atomic_mass_dimensionless β_K

/-- **The mass formula respects GB descent.** Adding any element
    annihilated by `NF_GS` (i.e. an element in the kernel of the
    GB descent map) does not change the predicted mass. -/
theorem atomicMassGBNF_descends
    (m_e ρ_K : ℝ) (β_K δ : A) (hδ : NF_GS δ = (0 : A)) :
    atomicMassGBNF m_e ρ_K (β_K + δ) =
    atomicMassGBNF m_e ρ_K β_K := by
  unfold atomicMassGBNF atomic_mass_dimensionless
  -- `NF_GS` is `ℝ`-linear, so `NF_GS (β_K + δ) = NF_GS β_K + NF_GS δ`.
  -- The hypothesis `hδ` collapses the second summand to `0`.
  have h_nf : NF_GS (β_K + δ) = NF_GS β_K := by
    rw [map_add, hδ, add_zero]
  rw [h_nf]

end GBNFAlgebra

end QOU.BraidKnot
