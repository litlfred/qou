import Mathlib.Data.Finset.Basic
import QOU.Photon


/-!
# QOU.Photon.Pieri — Pieri rule shift for degree-one Hecke elements

The photon is `def:photon`, `QOU.Photon.photon`:
`γ(φ) = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` (owner ruling, bean `qou-99qc`,
2026-11-18, confirmed 2026-11-20; the fourth term is the chiral vertex).
Multiplied against a state `β_m` supported on the partition `λ`, its support
is contained in `{λ} ∪ {λ ± □}` (single-box addition or removal). The
degree-one element `1 + Σ_i φ_i σ_i` of the earlier statement is the named
specialisation `φ₀₁ = 0` on one strand pair (photon-usage audit 2026-11-17, C10).

Step 1 of the narrative proof, for the four-term photon, is
`commute_photon_of_commute` below: anything commuting with `σ₀` and `σ₁`
(e.g. a central idempotent `e_λ`) commutes with the whole photon, including
its vertex term `σ₀σ₁⁻¹`. The `λ ± □` part (a photon reaching one further
strand) stays axiomatised in `IsPieriShift`.

Mathlib does not yet carry partition-indexed Hecke-algebra Specht
modules, so we package the Pieri rule as a typeclass `IsPieriShift`
whose existence corresponds to the statement of the rule for the
particular non-commutative Fourier interface in use. Concrete
instances (e.g. for `H_n(q)` at small `n`) supply the support
witnesses by direct computation.

LaTeX label: `prop:pieri-photon-shift`

## References

- [fulton1997] Young Tableaux (Cambridge University Press, 1997),
  Chapter 2.
- [kassel1995] Quantum Groups (Springer GTM 155, 1995), Chapter XI.
- [leitner2026] braids-and-knots / pieri-photon-shift
-/

namespace QOU.Photon

/-- Abstract data for a "non-commutative Fourier transform" with an
    addable/removable-corner adjacency relation on the spectrum. We
    use this in lieu of a full partition-lattice instance, which is
    not yet available in Mathlib. -/
structure PieriInterface where
  /-- Spectrum (e.g. `λ ⊢ n`). -/
  spectrum : Type*
  /-- The set of partitions reachable from `λ` by adding or removing
      a single box. By convention `λ` itself is in this set
      (for the identity term in `γ`). -/
  oneBoxShift : spectrum → Finset spectrum
  /-- The shift relation is reflexive: `λ ∈ oneBoxShift λ`. -/
  shift_self : ∀ lam, lam ∈ oneBoxShift lam

/-- **Pieri rule (axiomatised).**
    A degree-one Hecke element acting on a single-block state shifts
    its non-commutative Fourier support into the one-box neighbourhood.

    Concrete instances populate `support_after` by Pieri's rule
    [`fulton1997`, Ch. 2]. -/
class IsPieriShift (P : PieriInterface) where
  /-- For a degree-one Hecke element `γ` and a `λ`-block state `β`,
      the support of `γ · β` is contained in `oneBoxShift λ`. The
      `support_after` field encodes precisely that containment as a
      function of the source partition. -/
  support_after : P.spectrum → Finset P.spectrum
  /-- The shifted support lies in the one-box neighbourhood. -/
  support_subset : ∀ lam, support_after lam ⊆ P.oneBoxShift lam

/-- **The support-containment theorem.**
    Re-export of the `IsPieriShift` field. Intended use: callers
    quantify over `[IsPieriShift P]` and obtain the support
    containment for free. -/
-- Ref: [leitner2026] prop:pieri-photon-shift
-- Ref: [fulton1997] Young Tableaux, Ch. 2
-- Ref: [kassel1995] Quantum Groups, Ch. XI
theorem pieri_one_box_shift
    (P : PieriInterface) [S : IsPieriShift P] (lam : P.spectrum) :
    S.support_after lam ⊆ P.oneBoxShift lam :=
  S.support_subset lam

/-- The source partition `λ` is always reachable (identity term in `γ`). -/
-- Ref: [leitner2026] prop:pieri-photon-shift
theorem pieri_self_in_shift (P : PieriInterface) (lam : P.spectrum) :
    lam ∈ P.oneBoxShift lam :=
  P.shift_self lam

/-- **Step 1 for the four-term photon.** If `e` commutes with `σ₀` and with the
    unit `σ₁`, it commutes with every photon `γ(φ)`, the vertex term `σ₀σ₁⁻¹`
    included. With `e = e_λ` central this is the level-`n` containment
    `γ · (e_λ β) = e_λ (γ · β)`. Generic ring, no ordering (§7c). -/
-- Ref: [leitner2026] prop:pieri-photon-shift; def:photon
theorem commute_photon_of_commute {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    {e σ₀ : A} {σ₁ : Aˣ} (h0 : Commute e σ₀) (h1 : Commute e (σ₁ : A)) (c : Colour R) :
    Commute e (photon σ₀ σ₁ c) := by
  have hinv : Commute e (↑σ₁⁻¹ : A) := h1.units_inv_right
  have hv : Commute e (vertex σ₀ σ₁) := h0.mul_right hinv
  have hs : ∀ (r : R) {x : A}, Commute e x → Commute e (r • x) := fun r x hx => by
    rw [Algebra.smul_def]
    exact (Algebra.commute_algebraMap_right r e).mul_right hx
  unfold photon
  exact (((Commute.one_right e).add_right (hs _ h0)).add_right (hs _ h1)).add_right (hs _ hv)

end QOU.Photon
