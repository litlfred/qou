import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Div
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.FreeModule.StrongRankCondition
import Mathlib.LinearAlgebra.StdBasis
import Mathlib.RingTheory.Ideal.Maps
import Mathlib.RingTheory.Ideal.Quotient.Defs
import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.RingTheory.Ideal.Span
import Mathlib.Tactic.Ring

/-!
# QOU.Archimedean.genus_ideal_characterisation — genus-filtration ideal as `(u⁵)`

**Lemma** ([`lem:genus-ideal-characterisation`](../../../quantum-observable-universe/brings-surface/genus-ideal-characterisation.md)).

*At genus `g = 4`, define the genus-filtration ideal `I_4 := (u⁵) ⊂ ℤ[u]`.
Then `I_4` is the kernel of the truncation `π_4 : ℤ[u] → ℤ[u]/(u⁵)`.*

## Mathematical formalisation & Round-Trip Pass-3 Alignment

1. **Pass-3 canonical entrypoint (`genus_ideal_characterisation`):**
   Preserved verbatim per Round-Trip Pass 3 (`c3d2cab80a9`):
   `RingHom.ker (Ideal.Quotient.mk (Ideal.span {(X ^ 5 : Polynomial ℤ)})) = Ideal.span {(X ^ 5 : Polynomial ℤ)}`.

2. **Concrete degree-`≤ g` truncation ring (`TruncPoly`, `truncHom`):**
   Constructs `TruncPoly R (g + 1)` (coefficient tuples `(c₀, …, c_g) : Fin (g + 1) → R`
   under truncated Cauchy convolution) and `truncHom R g : Polynomial R →+* TruncPoly R (g + 1)`
   without referencing `(X ^ (g + 1))`, proving:
   - `mem_ker_truncHom_iff_coeff_zero`: `p ∈ ker(truncHom R g) ↔ ∀ k ≤ g, p.coeff k = 0`;
   - `ker_truncHom_eq_span_X_pow`: `RingHom.ker (truncHom R g) = Ideal.span {X ^ (g + 1)}`;
   - `quotientRingEquivTruncPoly` & `quotientLinearEquivFin`: explicit ring and free
     `R`-module isomorphisms `R[X] ⧸ (X ^ (g + 1)) ≃ₗ[R] (Fin (g + 1) → R)` with
     `finrank = g + 1` (`finrank_quotient_span_X_pow`).

-- Ref: [leitner2026] quantum-observable-universe/brings-surface/genus-ideal-characterisation.md
-/

namespace QOU.Archimedean

open Polynomial

/-- **Genus-filtration ideal characterisation** at `g = 4`
    ([`lem:genus-ideal-characterisation`], Pass-3 canonical entrypoint).

    The kernel of the canonical quotient map `ℤ[u] → ℤ[u] / (u⁵)` is the
    principal ideal `(u⁵)`. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/genus-ideal-characterisation.md
theorem genus_ideal_characterisation :
    RingHom.ker
        (Ideal.Quotient.mk (Ideal.span {(X ^ 5 : Polynomial ℤ)}))
      = Ideal.span {(X ^ 5 : Polynomial ℤ)} := by
  exact Ideal.mk_ker

/-! ## Concrete coefficient-truncation ring `TruncPoly` and free quotient basis -/

/-- Truncated polynomial / Hecke-coordinate carrier `TruncPoly R m` retaining
    coefficients in degrees `0, …, m − 1` (`m = g + 1` for surface genus `g`). -/
@[ext]
structure TruncPoly (R : Type*) (m : ℕ) where
  /-- Coefficient at degree `i < m`. -/
  coeff : Fin m → R

namespace TruncPoly

section RingStructure

variable {R : Type*} [CommRing R]

/-- Canonical lift of a truncated tuple `(c₀, …, c_{m−1})` to a polynomial of
    degree `< m`. -/
noncomputable def toPoly {m : ℕ} (a : TruncPoly R m) : Polynomial R :=
  ∑ i : Fin m, Polynomial.monomial (i : ℕ) (a.coeff i)

/-- Coefficient-truncation map sending `p : R[u]` to `(p.coeff 0, …, p.coeff (m−1))`. -/
def ofPoly (m : ℕ) (p : Polynomial R) : TruncPoly R m :=
  ⟨fun i => p.coeff i⟩

theorem coeff_toPoly {m : ℕ} (a : TruncPoly R m) (i : Fin m) :
    (toPoly a).coeff i = a.coeff i := by
  simp [toPoly, Polynomial.finset_sum_coeff, Polynomial.coeff_monomial, Fin.val_inj]

theorem ofPoly_toPoly {m : ℕ} (a : TruncPoly R m) : ofPoly m (toPoly a) = a := by
  ext i
  exact coeff_toPoly a i

theorem X_pow_dvd_sub_toPoly_ofPoly (m : ℕ) (p : Polynomial R) :
    X ^ m ∣ p - toPoly (ofPoly m p) := by
  rw [Polynomial.X_pow_dvd_iff]
  intro d hd
  let idx : Fin m := ⟨d, hd⟩
  have h := coeff_toPoly (ofPoly m p) idx
  change (toPoly (ofPoly m p)).coeff d = p.coeff d at h
  rw [Polynomial.coeff_sub, h, sub_self]

theorem ofPoly_eq_of_X_pow_dvd_sub (m : ℕ) {p q : Polynomial R} (h : X ^ m ∣ p - q) :
    ofPoly m p = ofPoly m q := by
  ext i
  have hi : (p - q).coeff i = 0 := (Polynomial.X_pow_dvd_iff.mp h) i.val i.isLt
  rw [Polynomial.coeff_sub] at hi
  exact sub_eq_zero.mp hi

theorem ofPoly_mul_eq (m : ℕ) (p q : Polynomial R) :
    ofPoly m (p * q) = ofPoly m (toPoly (ofPoly m p) * toPoly (ofPoly m q)) := by
  apply ofPoly_eq_of_X_pow_dvd_sub m
  have hp : X ^ m ∣ p - toPoly (ofPoly m p) := X_pow_dvd_sub_toPoly_ofPoly m p
  have hq : X ^ m ∣ q - toPoly (ofPoly m q) := X_pow_dvd_sub_toPoly_ofPoly m q
  have hid :
      p * q - toPoly (ofPoly m p) * toPoly (ofPoly m q) =
        (p - toPoly (ofPoly m p)) * q +
          toPoly (ofPoly m p) * (q - toPoly (ofPoly m q)) := by
    ring
  rw [hid]
  exact dvd_add (dvd_mul_of_dvd_left hp q) (dvd_mul_of_dvd_right hq _)

noncomputable instance (m : ℕ) : CommRing (TruncPoly R m) where
  zero := ⟨0⟩
  one := ofPoly m 1
  add a b := ⟨a.coeff + b.coeff⟩
  neg a := ⟨-a.coeff⟩
  sub a b := ⟨a.coeff - b.coeff⟩
  mul a b := ofPoly m (toPoly a * toPoly b)
  nsmul n a := ⟨n • a.coeff⟩
  zsmul z a := ⟨z • a.coeff⟩
  add_assoc a b c := by ext i; exact add_assoc _ _ _
  zero_add a := by ext i; exact zero_add _
  add_zero a := by ext i; exact add_zero _
  add_comm a b := by ext i; exact add_comm _ _
  neg_add_cancel a := by ext i; exact neg_add_cancel _
  sub_eq_add_neg a b := by ext i; exact sub_eq_add_neg _ _
  nsmul_zero a := by ext i; exact zero_smul ℕ (a.coeff i)
  nsmul_succ n a := by ext i; exact AddMonoid.nsmul_succ n (a.coeff i)
  zsmul_zero' a := by ext i; exact zero_smul ℤ (a.coeff i)
  zsmul_succ' n a := by ext i; exact SubNegMonoid.zsmul_succ' n (a.coeff i)
  zsmul_neg' n a := by ext i; exact SubNegMonoid.zsmul_neg' n (a.coeff i)
  left_distrib a b c := by
    change ofPoly m (toPoly a * toPoly ⟨b.coeff + c.coeff⟩) =
      ⟨(ofPoly m (toPoly a * toPoly b)).coeff + (ofPoly m (toPoly a * toPoly c)).coeff⟩
    have hbc : toPoly (⟨b.coeff + c.coeff⟩ : TruncPoly R m) = toPoly b + toPoly c := by
      simp [toPoly, Polynomial.monomial_add, Finset.sum_add_distrib]
    ext i
    rw [hbc, mul_add]
    exact Polynomial.coeff_add _ _ _
  right_distrib a b c := by
    change ofPoly m (toPoly ⟨a.coeff + b.coeff⟩ * toPoly c) =
      ⟨(ofPoly m (toPoly a * toPoly c)).coeff + (ofPoly m (toPoly b * toPoly c)).coeff⟩
    have hab : toPoly (⟨a.coeff + b.coeff⟩ : TruncPoly R m) = toPoly a + toPoly b := by
      simp [toPoly, Polynomial.monomial_add, Finset.sum_add_distrib]
    ext i
    rw [hab, add_mul]
    exact Polynomial.coeff_add _ _ _
  zero_mul a := by
    change ofPoly m (toPoly ⟨0⟩ * toPoly a) = ⟨0⟩
    have hz : toPoly (⟨0⟩ : TruncPoly R m) = 0 := by simp [toPoly]
    ext i
    rw [hz, zero_mul]
    exact Polynomial.coeff_zero _
  mul_zero a := by
    change ofPoly m (toPoly a * toPoly ⟨0⟩) = ⟨0⟩
    have hz : toPoly (⟨0⟩ : TruncPoly R m) = 0 := by simp [toPoly]
    ext i
    rw [hz, mul_zero]
    exact Polynomial.coeff_zero _
  mul_assoc a b c := by
    change ofPoly m (toPoly (ofPoly m (toPoly a * toPoly b)) * toPoly c) =
      ofPoly m (toPoly a * toPoly (ofPoly m (toPoly b * toPoly c)))
    have h1 : ofPoly m ((toPoly a * toPoly b) * toPoly c) =
        ofPoly m (toPoly (ofPoly m (toPoly a * toPoly b)) * toPoly c) := by
      simpa [ofPoly_toPoly] using ofPoly_mul_eq m (toPoly a * toPoly b) (toPoly c)
    have h2 : ofPoly m (toPoly a * (toPoly b * toPoly c)) =
        ofPoly m (toPoly a * toPoly (ofPoly m (toPoly b * toPoly c))) := by
      simpa [ofPoly_toPoly] using ofPoly_mul_eq m (toPoly a) (toPoly b * toPoly c)
    rw [← h1, ← h2, _root_.mul_assoc]
  one_mul a := by
    change ofPoly m (toPoly (ofPoly m 1) * toPoly a) = a
    have h1 : ofPoly m (1 * toPoly a) = ofPoly m (toPoly (ofPoly m 1) * toPoly a) := by
      simpa [ofPoly_toPoly] using ofPoly_mul_eq m 1 (toPoly a)
    rw [← h1, _root_.one_mul, ofPoly_toPoly]
  mul_one a := by
    change ofPoly m (toPoly a * toPoly (ofPoly m 1)) = a
    have h1 : ofPoly m (toPoly a * 1) = ofPoly m (toPoly a * toPoly (ofPoly m 1)) := by
      simpa [ofPoly_toPoly] using ofPoly_mul_eq m (toPoly a) 1
    rw [← h1, _root_.mul_one, ofPoly_toPoly]
  mul_comm a b := by
    change ofPoly m (toPoly a * toPoly b) = ofPoly m (toPoly b * toPoly a)
    rw [_root_.mul_comm]

end RingStructure

end TruncPoly

/-- **Genus-`g` truncation ring homomorphism**
    `π_g : R[u] →+* TruncPoly R (g + 1)` retaining the coefficients of degree `0 ≤ k ≤ g`. -/
noncomputable def truncHom (R : Type*) [CommRing R] (g : ℕ) :
    Polynomial R →+* TruncPoly R (g + 1) where
  toFun := TruncPoly.ofPoly (g + 1)
  map_one' := rfl
  map_mul' p q := TruncPoly.ofPoly_mul_eq (g + 1) p q
  map_zero' := by ext i; exact Polynomial.coeff_zero _
  map_add' p q := by ext i; exact Polynomial.coeff_add p q i

/-- Surjectivity of `truncHom R g`: every degree-`≤ g` coefficient profile lifts
    to a polynomial. -/
theorem truncHom_surjective (R : Type*) [CommRing R] (g : ℕ) :
    Function.Surjective (truncHom R g) :=
  fun a => ⟨TruncPoly.toPoly a, TruncPoly.ofPoly_toPoly a⟩

/-- A polynomial `p ∈ R[u]` lies in `ker(truncHom R g)` iff all of its
    coefficients in degrees `k ≤ g` vanish. -/
theorem mem_ker_truncHom_iff_coeff_zero {R : Type*} [CommRing R] (g : ℕ)
    (p : Polynomial R) :
    p ∈ RingHom.ker (truncHom R g) ↔ ∀ k ≤ g, p.coeff k = 0 := by
  rw [RingHom.mem_ker]
  constructor
  · intro hp k hk
    exact congr_arg (fun x => x.coeff ⟨k, Nat.lt_succ_of_le hk⟩) hp
  · intro hp
    ext i
    exact hp i.val (Nat.le_of_lt_succ i.isLt)

/-- **General genus-ideal theorem**: for any commutative ring `R` and any `g : ℕ`,
    the kernel of the degree-`≤ g` coefficient truncation
    `truncHom R g : R[u] →+* TruncPoly R (g + 1)` is **exactly** the principal
    ideal `Ideal.span {X ^ (g + 1)}`. -/
theorem ker_truncHom_eq_span_X_pow (R : Type*) [CommRing R] (g : ℕ) :
    RingHom.ker (truncHom R g) = Ideal.span {(X ^ (g + 1) : Polynomial R)} := by
  ext p
  rw [mem_ker_truncHom_iff_coeff_zero, Ideal.mem_span_singleton, Polynomial.X_pow_dvd_iff]
  constructor
  · intro h d hd
    exact h d (Nat.le_of_lt_succ hd)
  · intro h k hk
    exact h k (Nat.lt_succ_of_le hk)

/-- Explicit ring isomorphism
    `R[u] ⧸ Ideal.span {X ^ (g + 1)} ≃+* TruncPoly R (g + 1)` induced by `truncHom`. -/
noncomputable def quotientRingEquivTruncPoly (R : Type*) [CommRing R] (g : ℕ) :
    (Polynomial R ⧸ Ideal.span {(X ^ (g + 1) : Polynomial R)}) ≃+*
      TruncPoly R (g + 1) :=
  (Ideal.quotEquivOfEq (ker_truncHom_eq_span_X_pow R g).symm).trans
    (RingHom.quotientKerEquivOfSurjective (truncHom_surjective R g))

/-- Explicit `R`-linear isomorphism between the quotient
    `R[u] ⧸ Ideal.span {X ^ (g + 1)}` and the free module `Fin (g + 1) → R`. -/
noncomputable def quotientLinearEquivFin (R : Type*) [CommRing R] (g : ℕ) :
    (Polynomial R ⧸ Ideal.span {(X ^ (g + 1) : Polynomial R)}) ≃ₗ[R]
      (Fin (g + 1) → R) where
  toFun q :=
    (Ideal.Quotient.lift (Ideal.span {(X ^ (g + 1) : Polynomial R)})
      (truncHom R g)
      (fun p hp => by rw [← ker_truncHom_eq_span_X_pow R g] at hp; exact hp) q).coeff
  map_add' q₁ q₂ := by
    refine Quotient.inductionOn₂' q₁ q₂ fun p₁ p₂ => ?_
    ext i
    exact Polynomial.coeff_add p₁ p₂ i
  map_smul' r q := by
    refine Quotient.inductionOn' q fun p => ?_
    ext i
    change (r • p).coeff i = r * p.coeff i
    rw [Polynomial.coeff_smul, smul_eq_mul]
  invFun v := Ideal.Quotient.mk (Ideal.span {(X ^ (g + 1) : Polynomial R)})
    (TruncPoly.toPoly ⟨v⟩)
  left_inv q := by
    refine Quotient.inductionOn' q fun p => ?_
    apply Ideal.Quotient.eq.mpr
    rw [Ideal.mem_span_singleton]
    have hdvd := TruncPoly.X_pow_dvd_sub_toPoly_ofPoly (g + 1) p
    change X ^ (g + 1) ∣ TruncPoly.toPoly (TruncPoly.ofPoly (g + 1) p) - p
    have hsub : TruncPoly.toPoly (TruncPoly.ofPoly (g + 1) p) - p =
        -(p - TruncPoly.toPoly (TruncPoly.ofPoly (g + 1) p)) := by
      ring
    rw [hsub]
    exact dvd_neg.mpr hdvd
  right_inv v := by
    ext i
    exact TruncPoly.coeff_toPoly ⟨v⟩ i

/-- Explicit free `R`-basis `{1, u, …, u^g}` of `R[u] ⧸ Ideal.span {u^(g+1)}`. -/
noncomputable def quotientMonomialBasis (R : Type*) [CommRing R] (g : ℕ) :
    Module.Basis (Fin (g + 1)) R
      (Polynomial R ⧸ Ideal.span {(X ^ (g + 1) : Polynomial R)}) :=
  (Pi.basisFun R (Fin (g + 1))).map (quotientLinearEquivFin R g).symm

/-- Free `finrank` of `R[u] ⧸ Ideal.span {u^(g+1)}` equals `g + 1` over any
    nontrivial commutative ring `R`. -/
theorem finrank_quotient_span_X_pow (R : Type*) [CommRing R] [Nontrivial R] (g : ℕ) :
    Module.finrank R (Polynomial R ⧸ Ideal.span {(X ^ (g + 1) : Polynomial R)}) = g + 1 := by
  rw [LinearEquiv.finrank_eq (quotientLinearEquivFin R g),
    Module.finrank_eq_card_basis (Pi.basisFun R (Fin (g + 1))), Fintype.card_fin]

/-- Seifert-homology rank condition (`prf:genus-ideal-characterisation`):
    for odd `p ≥ 1`, `p − 1 ≤ 2g ↔ (p − 1) / 2 ≤ g`. -/
theorem seifert_homology_rank_fit_iff {p g : ℕ} (_hp : p % 2 = 1) :
    p - 1 ≤ 2 * g ↔ (p - 1) / 2 ≤ g := by
  omega

/-- Full coefficient-truncation and rank characterisation of `(u⁵) ⊂ ℤ[u]` at `g = 4`. -/
theorem genus_ideal_truncHom_characterisation :
    RingHom.ker (truncHom ℤ 4) = Ideal.span {(X ^ 5 : Polynomial ℤ)} ∧
    (∀ p : Polynomial ℤ,
      p ∈ Ideal.span {(X ^ 5 : Polynomial ℤ)} ↔ ∀ k ≤ 4, p.coeff k = 0) ∧
    (∀ k : ℕ, (X ^ k : Polynomial ℤ) ∈ RingHom.ker (truncHom ℤ 4) ↔ 5 ≤ k) ∧
    Module.finrank ℤ (Polynomial ℤ ⧸ Ideal.span {(X ^ 5 : Polynomial ℤ)}) = 5 := by
  refine ⟨ker_truncHom_eq_span_X_pow ℤ 4, ?_, ?_, finrank_quotient_span_X_pow ℤ 4⟩
  · intro p
    rw [← ker_truncHom_eq_span_X_pow ℤ 4, mem_ker_truncHom_iff_coeff_zero]
  · intro k
    rw [mem_ker_truncHom_iff_coeff_zero]
    constructor
    · intro hk
      by_contra hlt
      have hle : k ≤ 4 := by omega
      have h1 : (X ^ k : Polynomial ℤ).coeff k = 0 := hk k hle
      simp at h1
    · intro hk5 m hm4
      have hne : m ≠ k := by omega
      simp [Polynomial.coeff_X_pow, hne]

end QOU.Archimedean
