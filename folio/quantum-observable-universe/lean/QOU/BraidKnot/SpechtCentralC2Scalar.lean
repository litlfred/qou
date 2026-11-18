import QOU.BraidKnot.CentralC2Transport
import QOU.BraidKnot.JucysMurphyOV
import QOU.BraidKnot.SpechtActionInjective

/-!
# QOU.BraidKnot.SpechtCentralC2Scalar — `C₂` acts on every Specht block by a scalar

Toward the `SnIsotypicSpechtSplit` instance (epic `qou-nrex`, follow-on to brick 42).

`spechtProduct` — the map the Wedderburn split is built from — sends `C₂` to the family of scalars
the keystone names:

**`spechtProduct_centralC2`** — `spechtProduct n (C₂ n) i = (contentSqSum i.diagram) • 1`.

Three steps, each closing a gap between how the eigenvalue lemma is stated and how the split uses it:

* `asAlgebraHom_comp` — a representation precomposed with a group hom acts through the induced map
  on the monoid algebra. Proved by `MonoidAlgebra.algHom_ext`: two algebra homs agreeing on the
  group elements agree.
* `mapDomain_centralC2` (previous file) — so the induced map carries `C₂ n` to `C₂ (nOf μ)`, which
  is the index the eigenvalue lemma lives at.
* `spechtRep_asAlgebraHom_coe` — the Specht representation is the *restriction* of the ambient
  `Mtab` one, and restriction commutes with the algebra hom. `MonoidAlgebra.induction_on` does it:
  the claim is additive and `k`-homogeneous, so it suffices on group elements, where it is
  `LinearMap.restrict_apply`.

`centralC2_acts_by_contentSqSum` then applies on the nose.

Pure algebra over a characteristic-zero field; nothing archimedean; no fit.
-/

namespace QOU.BraidKnot.SpechtCentralC2Scalar

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]

omit [CharZero k] in
/-- **Precomposition acts through the induced map on the monoid algebra.** -/
theorem asAlgebraHom_comp {G H V : Type} [Monoid G] [Monoid H] [AddCommMonoid V] [Module k V]
    (ρ : Representation k H V) (φ : G →* H) (a : MonoidAlgebra k G) :
    Representation.asAlgebraHom (k := k) (G := G) (V := V) (ρ.comp φ) a
      = ρ.asAlgebraHom (MonoidAlgebra.mapDomainAlgHom k k φ a) := by
  have h : Representation.asAlgebraHom (k := k) (G := G) (V := V) (ρ.comp φ)
      = ρ.asAlgebraHom.comp (MonoidAlgebra.mapDomainAlgHom k k φ) := by
    refine MonoidAlgebra.algHom_ext (fun g => ?_)
    simp [Representation.asAlgebraHom_single, MonoidHom.comp_apply,
      MonoidAlgebra.mapDomainAlgHom_apply]
  rw [h]
  rfl

omit [CharZero k] in
/-- **The Specht representation is the restriction of the ambient one**, at the level of the whole
monoid algebra rather than one group element. -/
theorem spechtRep_asAlgebraHom_coe (μ : YoungDiagram) (a : MonoidAlgebra k (Perm (Fin (nOf μ))))
    (x : SpechtSubmodule (k := k) μ) :
    (((spechtRep (k := k) μ).asAlgebraHom a) x : Mtab (k := k) μ)
      = (Mtab.rep (k := k) μ).asAlgebraHom a (x : Mtab (k := k) μ) := by
  refine MonoidAlgebra.induction_on
    (p := fun b => (((spechtRep (k := k) μ).asAlgebraHom b) x : Mtab (k := k) μ)
      = (Mtab.rep (k := k) μ).asAlgebraHom b (x : Mtab (k := k) μ))
    a (fun g => ?_) (fun p q hp hq => ?_) (fun r p hp => ?_)
  · simp only [MonoidAlgebra.of_apply, Representation.asAlgebraHom_single, one_smul]
    rw [spechtRep]
    simp [LinearMap.restrict_apply]
  · simp [hp, hq]
  · simp [hp]

/-- **`C₂` acts on each Specht block by its content-square sum.** -/
theorem spechtProduct_centralC2 (n : ℕ) (i : PartitionIndex n) :
    SpechtActionInjective.spechtProduct (k := k) n (RegularRepTrace.centralC2 n) i
      = (JucysMurphy.contentSqSum i.diagram) •
        (1 : Module.End k (SpechtSubmodule (k := k) i.diagram)) := by
  rw [SpechtActionInjective.spechtProduct_apply, spechtRepAt, asAlgebraHom_comp,
    CentralC2Transport.mapDomain_centralC2]
  refine LinearMap.ext (fun x => Subtype.ext ?_)
  rw [spechtRep_asAlgebraHom_coe, ← JucysMurphy.centralC2_eq_sum_jucysMurphy_sq,
    JucysMurphy.centralC2_acts_by_contentSqSum (k := k) _ _ x.2]
  rfl

/-- The difference between the Specht product action of `centralC2 n` and the content-square scalar endomorphism vanishes on each block `i`. -/
theorem spechtProduct_centralC2_sub_eq_zero (n : ℕ) (i : PartitionIndex n) :
    SpechtActionInjective.spechtProduct (k := k) n (RegularRepTrace.centralC2 n) i -
      (JucysMurphy.contentSqSum i.diagram) •
        (1 : Module.End k (SpechtSubmodule (k := k) i.diagram)) = 0 := by
  rw [spechtProduct_centralC2]
  exact sub_self _

end QOU.BraidKnot.SpechtCentralC2Scalar
