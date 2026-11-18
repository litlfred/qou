import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.RegularRepTrace

/-!
# QOU.BraidKnot.CentralC2Transport — `C₂` survives the index cast

Toward the `SnIsotypicSpechtSplit` instance (epic `qou-nrex`, follow-on to brick 42).

The Specht machinery indexes representations by `n`, while the Jucys–Murphy eigenvalue lemma
(`centralC2_acts_by_contentSqSum`) is stated at `Specht.nOf μ`. `spechtRepAt` bridges them with
`transportPermHom`, so relating the two needs `C₂` to be carried along that bridge:

**`mapDomain_centralC2`** — `C₂` at one index maps to `C₂` at the other.

That this is true at all is a fact about *which* bridge is used. `transportPermHom h` is
`Equiv.permCongrHom (finCongr h)`, and `finCongr` is the canonical **order-preserving** cast from an
equality of naturals. `C₂ = ∑_k (∑_{i<k} (i k))²` mentions the order, so an arbitrary relabelling
would need the class-sum characterisation to transport; the canonical cast transports termwise.

Pure algebra over a commutative ring; nothing archimedean; no fit.
-/

namespace QOU.BraidKnot.CentralC2Transport

open MonoidAlgebra Finset
open Equiv (Perm)

variable {R : Type} [CommRing R]

/-- Conjugating a transposition by an equivalence transposes the images. -/
theorem permCongr_swap {α β : Type} [DecidableEq α] [DecidableEq β] (e : α ≃ β) (x y : α) :
    e.permCongr (Equiv.swap x y) = Equiv.swap (e x) (e y) :=
  Equiv.symm_trans_swap_trans x y e

/-- `transportPermHom` sends a transposition to the transposition of the cast indices. -/
theorem transportPermHom_swap {a b : ℕ} (h : a = b) (i j : Fin a) :
    SpechtClassification.transportPermHom h (Equiv.swap i j)
      = Equiv.swap (finCongr h i) (finCongr h j) :=
  permCongr_swap (finCongr h) i j

/-- **`C₂` is carried by the index cast.** -/
theorem mapDomain_centralC2 {a b : ℕ} (h : a = b) :
    MonoidAlgebra.mapDomainAlgHom R R (SpechtClassification.transportPermHom h)
        (RegularRepTrace.centralC2 (R := R) a)
      = RegularRepTrace.centralC2 (R := R) b := by
  classical
  rw [RegularRepTrace.centralC2, RegularRepTrace.centralC2, map_sum]
  refine Finset.sum_equiv (finCongr h) (fun i => by simp) (fun kk _ => ?_)
  rw [map_pow, map_sum]
  congr 1
  refine Finset.sum_equiv (finCongr h)
    (fun i => by simp only [Finset.mem_filter, Finset.mem_univ, true_and,
      finCongr_apply, Fin.coe_cast]) (fun i _ => ?_)
  rw [MonoidAlgebra.mapDomainAlgHom_apply, Finsupp.mapDomain_single, transportPermHom_swap]

/-- Subtracting the target element from the mapped element under an index equality cancels to zero (`qou-f4el`). -/
theorem mapDomain_centralC2_sub_eq_zero {a b : ℕ} (h : a = b) :
    MonoidAlgebra.mapDomainAlgHom R R (SpechtClassification.transportPermHom h)
        (RegularRepTrace.centralC2 (R := R) a)
      - RegularRepTrace.centralC2 (R := R) b = 0 := by
  rw [mapDomain_centralC2 h, sub_self]

end QOU.BraidKnot.CentralC2Transport
