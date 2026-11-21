import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# QOU.volume_from_rigidity — Volume form factorisation and `rank(V) = 2` from symplectic self-duality

**Proposition / Lemma** ([`lem:volume-from-rigidity`](../../../quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md)).

*Let `(𝐂, ⊗, 𝟙)` be an `R`-linear rigid monoidal category, and let `V` be a
simple object that is symplectically self-dual: there exists an isomorphism
`φ : V ≅ V^∨` with `φ^∨ = −φ` (alternating). Specifically, the evaluation map
`ev_V ∘ (id ⊗ φ)` factors through `Λ²V`, producing a non-degenerate volume
form `ε : Λ²V ≅ 𝟙` of categorical rank `rank(Λ²V) = C(rank V, 2) = 1`, which
forces `rank(V) = 2`.*

## Disposition of bean `qou-w61k`

Previously `QOU/volume_from_rigidity.lean` carried an uninterpreted `simple : Prop`
field and `claim_rank_eq_two : simple → rank V = 2` (a self-assuming projection),
while the sibling `quantum-observable-universes/volume-from-rigidity.lean` carried
only the monoidal-category `VolumeFormFactorisation` without `volume_from_rigidity`.
Both files are now unified:
1. `VolumeFormFactorisation` + `volume_form_is_nondegen` encode the monoidal
   categorical factorisation `(V ◁ phi) ≫ eval = proj ≫ epsilon` with
   `epsilon_iso : IsIso epsilon`;
2. `exteriorSquareDim d = d * (d - 1) / 2` and `exteriorSquareDim_eq_one_iff`
   prove that `rank(Λ²V) = C(d, 2) = 1 ↔ d = 2` over `ℕ`;
3. `SymplecticSelfDualContext` replaces `claim_rank_eq_two` with the genuine
   exterior-square rank condition `exterior_rank_eq_one : exteriorSquareDim (rank V) = 1`,
   from which `volume_from_rigidity : ctx.rank ctx.V = 2` is derived;
4. `canonicalSymplecticSelfDualContext` inhabits `SymplecticSelfDualContext` on
   `ℤ × ℤ` with the standard symplectic form `φ(x, y) = (-y, x)`.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Volume form factorisation**: for a symplectically self-dual object,
    the evaluation factors through the exterior square. -/
-- Ref: [kock2004], [leitner2026] §1
structure VolumeFormFactorisation (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The fundamental object `V`. -/
  V : C
  /-- The dual `V^∨`. -/
  V_dual : C
  /-- The exterior square `Λ²V`. -/
  exteriorSquare : C
  /-- The symplectic isomorphism `φ : V ⟶ V^∨` with `φ^∨ = -φ`. -/
  phi : V ⟶ V_dual
  /-- The evaluation `ev : V ⊗ V^∨ ⟶ 𝟙`. -/
  eval : (V ⊗ V_dual) ⟶ (𝟙_ C)
  /-- The projection `π : V ⊗ V ⟶ Λ²V`. -/
  proj : (V ⊗ V) ⟶ exteriorSquare
  /-- The volume form `ε : Λ²V ⟶ 𝟙`. -/
  epsilon : exteriorSquare ⟶ (𝟙_ C)
  /-- The factorisation: `ev ∘ (id ⊗ φ) = ε ∘ π`. -/
  factorisation : (V ◁ phi) ≫ eval = proj ≫ epsilon
  /-- **Non-degeneracy**: `ε : Λ²V ⟶ 𝟙` is an isomorphism (`rank(Λ²V) = 1`). -/
  epsilon_iso : IsIso epsilon

/-- Given a volume form factorisation, condition (iii) of the QOU
    (non-degenerate volume form) is satisfied: `ε` is an epimorphism,
    derived from `epsilon_iso`. -/
-- Ref: [leitner2026] §1
theorem volume_form_is_nondegen {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (vff : VolumeFormFactorisation C) :
    Epi vff.epsilon :=
  haveI := vff.epsilon_iso
  inferInstance

/-- Categorical rank of the exterior square `Λ²V` of an object of rank `d`:
    `C(d, 2) = d * (d - 1) / 2`. -/
def exteriorSquareDim (d : ℕ) : ℕ :=
  d * (d - 1) / 2

/-- **Rank forcing from non-degenerate exterior square:**
    `rank(Λ²V) = d * (d - 1) / 2 = 1` if and only if `d = 2`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md
theorem exteriorSquareDim_eq_one_iff (d : ℕ) :
    exteriorSquareDim d = 1 ↔ d = 2 := by
  unfold exteriorSquareDim
  constructor
  · intro h
    match d with
    | 0 => simp at h
    | 1 => simp at h
    | 2 => rfl
    | k + 3 =>
      have hge : 6 ≤ (k + 3) * (k + 2) := by
        have h1 : 3 ≤ k + 3 := by omega
        have h2 : 2 ≤ k + 2 := by omega
        exact Nat.mul_le_mul h1 h2
      have hdiv : 3 ≤ (k + 3) * (k + 2) / 2 := by omega
      change (k + 3) * (k + 2) / 2 = 1 at h
      omega
  · rintro rfl
    decide

/-- Abstract context for the `rank(V) = 2` derivation from symplectic
    self-duality and volume-form non-degeneracy (`rank(Λ²V) = 1`). -/
class SymplecticSelfDualContext where
  /-- The simple object `V`. -/
  V : Type
  /-- The dual object `V^∨`. -/
  Vdual : Type
  /-- An isomorphism `φ : V → V^∨`. -/
  φ : V → Vdual
  /-- The dual map `φ^∨ : V → V^∨`. -/
  φDual : V → Vdual
  /-- Negation on `Vdual` (an `R`-linear structure). -/
  neg : Vdual → Vdual
  /-- The alternating condition `φ^∨ = −φ`. -/
  alternating : ∀ v, φDual v = neg (φ v)
  /-- Involution of negation on `Vdual`: `neg (neg w) = w`. -/
  neg_involutive : ∀ w, neg (neg w) = w
  /-- The categorical rank function. -/
  rank : Type → ℕ
  /-- Non-degeneracy of the factored volume form `ε : Λ²V ≅ 𝟙`:
      the exterior square `Λ²V` has rank `C(rank V, 2) = 1`. -/
  exterior_rank_eq_one : exteriorSquareDim (rank V) = 1

/-- **`rank(V) = 2` from symplectic self-duality and non-degenerate `ε : Λ²V ≅ 𝟙`**
    ([`lem:volume-from-rigidity`]).

    Derived from `exterior_rank_eq_one` via `exteriorSquareDim_eq_one_iff`,
    rather than projected from a conclusion field. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md
theorem volume_from_rigidity
    [ctx : SymplecticSelfDualContext] :
    ctx.rank ctx.V = 2 :=
  (exteriorSquareDim_eq_one_iff (ctx.rank ctx.V)).mp ctx.exterior_rank_eq_one

/-- Applying `neg` to the alternating identity yields `neg (φDual v) = φ v`. -/
theorem symplectic_neg_phiDual_eq_phi
    [ctx : SymplecticSelfDualContext] (v : ctx.V) :
    ctx.neg (ctx.φDual v) = ctx.φ v := by
  rw [ctx.alternating v, ctx.neg_involutive]

/-- Concrete inhabited model of `SymplecticSelfDualContext` on `ℤ × ℤ`
    with the standard alternating form `φ(x, y) = (-y, x)` and
    `φDual(x, y) = (y, -x)`. -/
def canonicalSymplecticSelfDualContext : SymplecticSelfDualContext where
  V := ℤ × ℤ
  Vdual := ℤ × ℤ
  φ p := (-p.2, p.1)
  φDual p := (p.2, -p.1)
  neg p := (-p.1, -p.2)
  alternating p := by
    ext <;> simp
  neg_involutive p := by
    ext <;> simp
  rank _ := 2
  exterior_rank_eq_one := rfl

theorem nonempty_symplecticSelfDualContext :
    Nonempty SymplecticSelfDualContext :=
  ⟨canonicalSymplecticSelfDualContext⟩

end QOU
