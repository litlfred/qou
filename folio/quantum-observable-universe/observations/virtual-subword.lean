import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Units.Lemmas
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Finset.Powerset
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# QOU.VirtualSubword — virtual and entangled particles at the level of words

This is the word-level companion of `QOU.Virtual` (`VirtualProjection.lean`). There, an off-shell
dressing is one whose counit vanishes, so it projects to nothing at the base level. Here, a word in
photon letters is evaluated in a group `G` (the braid group, or the units of `H_n(q)`). An
*observable* is a class function, and a subword is *virtual* when inserting it changes no
observable.

Contents:

* `IsObservable f` — `f (x * y) = f (y * x)` (closure / conjugation invariance).
* `ConjEquiv a b` — `a` and `b` are conjugate. `ev w = ev w'` (Gröbner–Shirshov equality) is
  finer.
* `IsVirtual 𝒪 u x v` — inserting `x` between `u` and `v` changes no observable in `𝒪`.
* `pair_isVirtual` — pair creation and annihilation `y · y⁻¹` is virtual for every function.
* `IsVirtualLoop`, `emit_reabsorb_isVirtual` — emission and reabsorption around the closure
  `y · w · y⁻¹` is virtual for every observable.
* `not_observable_of_rotation` — a word reading that changes under a cyclic rotation is not an
  observable. The stage-3 probe (`gg_full_photon_stage3_probe.py`, PR #8128) finds such pairs for
  the site-by-site reading 3.
* Signed strand crossings on `n` strands: `crossSum A` (crossings between a strand in `A` and one
  outside it), `selfSum A`, and `writhe = crossSum A + selfSum A`.
* `trivChar_eq` — in the trivial block (`σ ↦ q`, `σ⁻¹ ↦ q⁻¹`, which satisfies the Hecke relation:
  `trivial_hecke`), a word evaluates to `q ^ writhe = q ^ crossSum A * q ^ selfSum A`.

A pair word is *entangled across `A | Aᶜ`* (`IsEntangledAcross`) when its cross sum is nonzero. For a
pure braid this cross sum is twice the `A`–`Aᶜ` linking number. So the trivial-block shift of a bound
electron factors into an entangled part `q ^ crossSum` and a self-twist part `q ^ selfSum`. The shift
alone does not decide which part it came from.

Base ring: a generic `Field R` (§7c); the only input is `q ≠ 0`. Nothing archimedean is used.

-- Ref: [leitner2026] virtual-particles-exceptional-divisor; gamma-gamma-generates-particles
-/

namespace QOU.VirtualSubword

section Group

variable {G : Type*} [Group G] {R : Type*}

/-- An observable is a class function: it cannot tell `x * y` from `y * x` (braid closure). -/
def IsObservable (f : G → R) : Prop := ∀ x y : G, f (x * y) = f (y * x)

/-- Closure equivalence: `a` and `b` are conjugate. -/
def ConjEquiv (a b : G) : Prop := ∃ y : G, b = y * a * y⁻¹

/-- A subword `x` of `u * x * v` is virtual for the family `𝒪` if inserting it changes no
member of `𝒪`. -/
def IsVirtual (𝒪 : Set (G → R)) (u x v : G) : Prop := ∀ f ∈ 𝒪, f (u * x * v) = f (u * v)

/-- Every observable is constant on closure classes. -/
theorem observable_conj {f : G → R} (hf : IsObservable f) (y w : G) :
    f (y * w * y⁻¹) = f w := by
  rw [hf (y * w) y⁻¹]
  simp

theorem observable_of_conjEquiv {f : G → R} (hf : IsObservable f) {a b : G}
    (h : ConjEquiv a b) : f b = f a := by
  obtain ⟨y, rfl⟩ := h
  exact observable_conj hf y a

/-- **Pair creation and annihilation.** `y · y⁻¹` is virtual for every family of functions,
because it is already trivial in `G` (Gröbner–Shirshov null). -/
theorem pair_isVirtual (𝒪 : Set (G → R)) (u y v : G) : IsVirtual 𝒪 u (y * y⁻¹) v := by
  intro f _
  simp

/-- A split insertion: `y` is emitted before `w` and reabsorbed (`y⁻¹`) after it. It is virtual for
`𝒪` if no member of `𝒪` sees it. -/
def IsVirtualLoop (𝒪 : Set (G → R)) (y w : G) : Prop := ∀ f ∈ 𝒪, f (y * w * y⁻¹) = f w

/-- **Emission and reabsorption around the closure** is virtual for every observable. -/
theorem emit_reabsorb_isVirtual (y w : G) : IsVirtualLoop {f : G → R | IsObservable f} y w :=
  fun _ hf => observable_conj hf y w

/-- A reading of words that changes under a cyclic rotation is not an observable composed with
evaluation. This is the abstract form of the stage-3 counterexamples. -/
theorem not_observable_of_rotation {W : Type*} (ev : W → G) (read : W → R) (f : G → R)
    (hfac : ∀ w, read w = f (ev w)) {w w' : W} {x y : G} (hw : ev w = x * y)
    (hw' : ev w' = y * x) (hne : read w ≠ read w') : ¬ IsObservable f := by
  intro hf
  apply hne
  rw [hfac, hfac, hw, hw', hf]

end Group

section Crossings

/-- A signed braid letter on `n` strands: the site `i` (crossing positions `i` and `i+1`) and the
sign `s ∈ {+1, -1}` (`σ_i` or `σ_i⁻¹`). -/
structure Letter (n : ℕ) where
  site : Fin n
  next : Fin n
  adj : next.val = site.val + 1
  pos : Bool

/-- Sign of a letter. -/
def Letter.sign {n : ℕ} (l : Letter n) : ℤ := if l.pos then 1 else -1

/-- Apply one crossing to the position→strand assignment. -/
def step {n : ℕ} (p : Equiv.Perm (Fin n)) (l : Letter n) : Equiv.Perm (Fin n) :=
  (Equiv.swap l.site l.next).trans p

/-- Signed crossings of a word between a strand in `A` and a strand not in `A`. Positions are
tracked from the start assignment `p`. -/
def crossSum {n : ℕ} (A : Finset (Fin n)) : Equiv.Perm (Fin n) → List (Letter n) → ℤ
  | _, [] => 0
  | p, l :: w =>
      (if (p l.site ∈ A) ≠ (p l.next ∈ A) then l.sign else 0) + crossSum A (step p l) w

/-- Signed crossings of a word between two strands on the same side of the cut. -/
def selfSum {n : ℕ} (A : Finset (Fin n)) : Equiv.Perm (Fin n) → List (Letter n) → ℤ
  | _, [] => 0
  | p, l :: w =>
      (if (p l.site ∈ A) ≠ (p l.next ∈ A) then 0 else l.sign) + selfSum A (step p l) w

/-- The writhe: the sum of all signs. -/
def writhe {n : ℕ} : List (Letter n) → ℤ
  | [] => 0
  | l :: w => l.sign + writhe w

/-- Every crossing either crosses the cut or does not. -/
theorem writhe_eq_cross_add_self {n : ℕ} (A : Finset (Fin n)) :
    ∀ (p : Equiv.Perm (Fin n)) (w : List (Letter n)),
      writhe w = crossSum A p w + selfSum A p w
  | _, [] => by simp [writhe, crossSum, selfSum]
  | p, l :: w => by
      simp only [writhe, crossSum, selfSum]
      rw [writhe_eq_cross_add_self A (step p l) w]
      split_ifs <;> ring

/-- A word is entangled across the cut `A | Aᶜ` when its signed cross count is nonzero (for a pure
braid: twice the `A`–`Aᶜ` linking number is nonzero). -/
def IsEntangledAcross {n : ℕ} (A : Finset (Fin n)) (w : List (Letter n)) : Prop :=
  crossSum A 1 w ≠ 0

end Crossings

section TrivialBlock

variable {R : Type*} [Field R]

/-- The trivial block of `H_n(q)`: `σ ↦ q`, `σ⁻¹ = σ - (q - q⁻¹) ↦ q⁻¹`. -/
def trivLetter (q : R) {n : ℕ} (l : Letter n) : R := if l.pos then q else q⁻¹

/-- The trivial one-dimensional block satisfies the Hecke relation `(σ - q)(σ + q⁻¹) = 0`, and
`σ⁻¹` is sent to `σ - (q - q⁻¹)`. -/
theorem trivial_hecke (q : R) : (q - q) * (q + q⁻¹) = 0 ∧ q - (q - q⁻¹) = q⁻¹ := by
  constructor <;> ring

/-- Evaluation of a word in the trivial block. -/
def trivChar (q : R) {n : ℕ} : List (Letter n) → R
  | [] => 1
  | l :: w => trivLetter q l * trivChar q w

theorem trivLetter_eq_zpow (q : R) {n : ℕ} (l : Letter n) : trivLetter q l = q ^ l.sign := by
  unfold trivLetter Letter.sign
  cases l.pos <;> simp

/-- **Trivial-block shift.** A word evaluates to `q ^ writhe`, which splits into an entangled part
`q ^ crossSum` and a self-twist part `q ^ selfSum`. -/
theorem trivChar_eq {q : R} (hq : q ≠ 0) {n : ℕ} (A : Finset (Fin n)) (w : List (Letter n)) :
    trivChar q w = q ^ writhe w ∧
      trivChar q w = q ^ crossSum A 1 w * q ^ selfSum A 1 w := by
  have h1 : ∀ w : List (Letter n), trivChar q w = q ^ writhe w := by
    intro w
    induction w with
    | nil => simp [trivChar, writhe]
    | cons l w ih =>
        rw [trivChar, writhe, ih, trivLetter_eq_zpow, zpow_add₀ hq]
  refine ⟨h1 w, ?_⟩
  rw [h1 w, writhe_eq_cross_add_self A 1 w, zpow_add₀ hq]

end TrivialBlock

section Borromean

/-! ### Pairwise linking misses three-party entanglement

`V = σ₀ σ₁⁻¹` and `V³` closes to the Borromean rings. Every two-group cut of its three strands has
cross sum `0`, so the pairwise test `IsEntangledAcross` calls it unentangled. Yet `V³ ≠ 1` in a
representation of `B₃`: the reduced Burau representation at `t = 2`. So the entanglement of the
γγ nucleon `V³` (and of the H₂ bond `V³`) is genuinely three-party (Milnor `μ̄₁₂₃`), not pairwise. -/

/-- `σ₀` on three strands. -/
def s0 : Letter 3 := ⟨0, 1, rfl, true⟩
/-- `σ₁⁻¹` on three strands. -/
def s1i : Letter 3 := ⟨1, 2, rfl, false⟩
/-- The word `V³ = (σ₀ σ₁⁻¹)³`. -/
def V3 : List (Letter 3) := [s0, s1i, s0, s1i, s0, s1i]

/-- Every one-strand-versus-two cut of `V³` has signed cross sum `0`. -/
theorem V3_cross_zero :
    crossSum {0} 1 V3 = 0 ∧ crossSum {1} 1 V3 = 0 ∧ crossSum {2} 1 V3 = 0 := by
  decide

/-- `V³` is pure: its strand permutation is the identity. -/
theorem V3_pure : ∀ i : Fin 3, (V3.foldl step (1 : Equiv.Perm (Fin 3))) i = i := by
  decide

/-- 2×2 matrices over `ℚ` as four entries (enough for the witness). -/
structure M2 where
  a : ℚ
  b : ℚ
  c : ℚ
  d : ℚ
deriving DecidableEq

/-- Matrix product. -/
def M2.mul (x y : M2) : M2 :=
  ⟨x.a * y.a + x.b * y.c, x.a * y.b + x.b * y.d, x.c * y.a + x.d * y.c, x.c * y.b + x.d * y.d⟩

/-- The identity matrix. -/
def M2.one : M2 := ⟨1, 0, 0, 1⟩

/-- Reduced Burau at `t = 2`: `σ₀ ↦ [[-t,1],[0,1]]`. -/
def burau0 : M2 := ⟨-2, 1, 0, 1⟩
/-- `σ₁ ↦ [[1,0],[t,-t]]`. -/
def burau1 : M2 := ⟨1, 0, 2, -2⟩
/-- `σ₁⁻¹ ↦ [[1,0],[1,-1/t]]`. -/
def burau1i : M2 := ⟨1, 0, 1, -1/2⟩

/-- The matrices define a representation of `B₃`: `σ₁ σ₁⁻¹ = 1` and the braid relation. -/
theorem burau_rep :
    M2.mul burau1 burau1i = M2.one ∧
      M2.mul (M2.mul burau0 burau1) burau0 = M2.mul (M2.mul burau1 burau0) burau1 := by
  constructor <;> norm_num [M2.mul, M2.one, burau0, burau1, burau1i]

/-- **Borromean witness.** `V³` is not the identity in this representation, so `V³ ≠ 1` in `B₃`,
although every pairwise cut sees cross sum `0`. -/
theorem V3_ne_one :
    (let v := M2.mul burau0 burau1i; M2.mul (M2.mul v v) v) ≠ M2.one := by
  simp only [M2.mul, M2.one, burau0, burau1i, ne_eq, M2.mk.injEq]
  norm_num

end Borromean

section Cumulant

/-! ### Entanglement as a convolution cumulant

Let `F T` be the logarithm of a multiplicative observable of the sub-braid on the strand set `T`,
normalised so that an unlink gives `0`. Split (convolved) pieces make `F` additive. The connected
part `φ T` is the Möbius inversion of `F` over the subsets of `T`. A split sub-braid has `φ = 0`,
so `φ T ≠ 0` certifies `|T|`-party entanglement: `|T| = 2` is the Bell (pairwise) level and
`|T| = 3` with all pairs zero is the GHZ (Borromean) level. -/

variable {ι R : Type*} [DecidableEq ι] [CommRing R]

/-- The connected part (Möbius inversion over subsets) of a set function. -/
def connected (F : Finset ι → R) (T : Finset ι) : R :=
  (-1) ^ T.card * ∑ U ∈ T.powerset, (-1) ^ U.card * F U

/-- On a pair the connected part is the familiar inclusion–exclusion. -/
theorem connected_pair (F : Finset ι → R) {a b : ι} (hab : a ≠ b) :
    connected F {a, b} = F {a, b} - F {a} - F {b} + F ∅ := by
  have hb : a ∉ ({b} : Finset ι) := by simpa using hab
  have hps : ({b} : Finset ι).powerset = {∅, {b}} := by
    ext s; simp [Finset.subset_singleton_iff]
  have hne : ({b} : Finset ι) ≠ ∅ := Finset.singleton_ne_empty b
  have h0 : (∅ : Finset ι) ∉ ({{b}} : Finset (Finset ι)) := by
    simpa [eq_comm] using hne
  simp only [connected, Finset.sum_powerset_insert hb, hps, Finset.sum_insert h0,
    Finset.sum_singleton, Finset.card_insert_of_notMem hb, Finset.card_singleton,
    Finset.card_empty, insert_empty_eq]
  rw [Finset.pair_comm]
  ring

/-- If `F` does not depend on a strand `a`, the signed sum over subsets containing `a` cancels the
sum over subsets avoiding it. -/
theorem sum_signed_eq_zero_of_indep (F : Finset ι → R) {a : ι} {S : Finset ι} (ha : a ∉ S)
    (hind : ∀ U ⊆ S, F (insert a U) = F U) :
    ∑ U ∈ (insert a S).powerset, (-1) ^ U.card * F U = 0 := by
  rw [Finset.sum_powerset_insert ha, ← Finset.sum_add_distrib]
  refine Finset.sum_eq_zero fun U hU => ?_
  have hUS : U ⊆ S := Finset.mem_powerset.mp hU
  have haU : a ∉ U := fun h => ha (hUS h)
  rw [Finset.card_insert_of_notMem haU, hind U hUS, pow_succ]
  ring

/-- A set function that ignores a strand of `T` has zero connected part on `T`. -/
theorem connected_eq_zero_of_indep (F : Finset ι → R) {T : Finset ι} {a : ι} (haT : a ∈ T)
    (hind : ∀ U ⊆ T.erase a, F (insert a U) = F U) : connected F T = 0 := by
  have hT : insert a (T.erase a) = T := Finset.insert_erase haT
  have h := sum_signed_eq_zero_of_indep F (Finset.notMem_erase a T) hind
  rw [hT] at h
  simp [connected, h]

omit [DecidableEq ι] in
/-- The connected part is additive in the set function. -/
theorem connected_add (F G : Finset ι → R) (T : Finset ι) :
    connected (F + G) T = connected F T + connected G T := by
  simp only [connected, Pi.add_apply, mul_add, Finset.sum_add_distrib]

omit [DecidableEq ι] in
/-- The connected part only sees the values of `F` on subsets of `T`. -/
theorem connected_congr {F G : Finset ι → R} {T : Finset ι} (h : ∀ U ⊆ T, F U = G U) :
    connected F T = connected G T := by
  unfold connected
  congr 1
  exact Finset.sum_congr rfl fun U hU => by rw [h U (Finset.mem_powerset.mp hU)]

/-- **Split implies no connected part.** If `T = T₁ ∪ T₂` with `T₁, T₂` disjoint and nonempty, and
`F` is additive over the split on every subset of `T`, then `connected F T = 0`. Contrapositive:
`connected F T ≠ 0` means the strands of `T` do not split into two non-interacting groups. -/
theorem connected_eq_zero_of_split (F : Finset ι → R) {T₁ T₂ : Finset ι}
    (hdisj : Disjoint T₁ T₂) (h₁ : T₁.Nonempty) (h₂ : T₂.Nonempty)
    (hadd : ∀ U ⊆ T₁ ∪ T₂, F U = F (U ∩ T₁) + F (U ∩ T₂)) :
    connected F (T₁ ∪ T₂) = 0 := by
  rw [connected_congr (G := fun U => F (U ∩ T₁) + F (U ∩ T₂)) hadd]
  change connected ((fun U => F (U ∩ T₁)) + (fun U => F (U ∩ T₂))) (T₁ ∪ T₂) = 0
  rw [connected_add]
  obtain ⟨b, hb⟩ := h₂
  obtain ⟨a, ha⟩ := h₁
  have hb1 : b ∉ T₁ := fun h => Finset.disjoint_left.mp hdisj h hb
  have ha2 : a ∉ T₂ := fun h => Finset.disjoint_left.mp hdisj ha h
  rw [connected_eq_zero_of_indep _ (Finset.mem_union_right _ hb) (fun U _ => by
        simp [Finset.insert_inter_of_notMem hb1]),
      connected_eq_zero_of_indep _ (Finset.mem_union_left _ ha) (fun U _ => by
        simp [Finset.insert_inter_of_notMem ha2])]
  simp

/-- The indicator of "contains `S`" has connected part `1` on `S` itself. -/
theorem connected_contains_self (S : Finset ι) :
    connected (fun U => if S ⊆ U then (1 : R) else 0) S = 1 := by
  unfold connected
  rw [Finset.sum_eq_single S]
  · simp only [subset_refl, if_true, mul_one, ← pow_add, ← two_mul, pow_mul]
    simp
  · intro U hU hne
    have hUS : U ⊆ S := Finset.mem_powerset.mp hU
    have : ¬ S ⊆ U := fun h => hne (Finset.Subset.antisymm hUS h)
    simp [this]
  · intro h; exact absurd (Finset.mem_powerset_self S) h

/-- The indicator of "contains `S`" has zero connected part on any `T ≠ S`. -/
theorem connected_contains_ne {S T : Finset ι} (hST : S ≠ T) :
    connected (fun U => if S ⊆ U then (1 : R) else 0) T = 0 := by
  by_cases hsub : S ⊆ T
  · obtain ⟨a, haT, haS⟩ : ∃ a ∈ T, a ∉ S := by
      by_contra h
      push_neg at h
      exact hST (Finset.Subset.antisymm hsub h)
    refine connected_eq_zero_of_indep _ haT fun U _ => ?_
    have : S ⊆ insert a U ↔ S ⊆ U := by
      constructor
      · intro h x hx
        rcases Finset.mem_insert.mp (h hx) with rfl | h'
        · exact absurd hx haS
        · exact h'
      · intro h; exact h.trans (Finset.subset_insert a U)
    simp only [this]
  · rw [connected_congr (G := fun _ => (0 : R)) fun U hU => by
      have : ¬ S ⊆ U := fun h => hsub (h.trans hU)
      simp [this]]
    simp [connected]

omit [DecidableEq ι] in
/-- The connected part commutes with finite sums of set functions. -/
theorem connected_finset_sum {κ : Type*} (s : Finset κ) (F : κ → Finset ι → R) (T : Finset ι) :
    connected (fun U => ∑ k ∈ s, F k U) T = ∑ k ∈ s, connected (F k) T := by
  simp only [connected, Finset.mul_sum]
  exact Finset.sum_comm

omit [DecidableEq ι] in
/-- The connected part commutes with scaling. -/
theorem connected_const_mul (c : R) (F : Finset ι → R) (T : Finset ι) :
    connected (fun U => c * F U) T = c * connected F T := by
  simp only [connected, Finset.mul_sum]
  refine Finset.sum_congr rfl fun U _ => ?_
  ring

/-- A weighted indicator of "contains `S`" has connected part `w` on `S` and `0` elsewhere. -/
theorem connected_weighted_contains (S T : Finset ι) (w : R) :
    connected (fun U => if S ⊆ U then w else 0) T = if S = T then w else 0 := by
  have : (fun U : Finset ι => if S ⊆ U then w else 0)
      = fun U => w * (if S ⊆ U then (1 : R) else 0) := by
    funext U; split_ifs <;> simp
  rw [this, connected_const_mul]
  split_ifs with h
  · subst h; rw [connected_contains_self, mul_one]
  · rw [connected_contains_ne h, mul_zero]

/-- **Möbius coefficient.** If `F U = ∑_{S ∈ P, S ⊆ U} w S` on every `U ⊆ T`, then the connected
part of `F` on `T` is `w T` when `T ∈ P` and `0` otherwise. So `w` lists the genuinely
`|S|`-party terms of `F`, and the connected part reads them off one at a time. -/
theorem connected_eq_coeff (F : Finset ι → R) (P : Finset (Finset ι)) (w : Finset ι → R)
    (T : Finset ι) (hF : ∀ U ⊆ T, F U = ∑ S ∈ P, if S ⊆ U then w S else 0) :
    connected F T = if T ∈ P then w T else 0 := by
  rw [connected_congr hF, connected_finset_sum]
  simp only [connected_weighted_contains]
  rw [Finset.sum_ite_eq']

/-- **Bond-additive set functions have no connected part beyond two parties.** Suppose that on
every `U ⊆ T`, `F U` is a sum of one-strand terms `g a` (for `a ∈ U`) and two-strand bond terms
`b e` over a set `E` of two-element bonds with `e ⊆ U`. Then `connected F T = 0` whenever
`|T| ≥ 3`. For an open chain `E` is the set of adjacent pairs, so an open chain of bonds has zero
`n`-party connected part for every `n ≥ 3`. The bond-additivity of `F` is the input; for a
convolution (connected-sum) product of bonds it is the additivity of `log` of a multiplicative
invariant, and it is not derived here. -/
theorem connected_eq_zero_of_bonds (F : Finset ι → R) (g : ι → R) (E : Finset (Finset ι))
    (b : Finset ι → R) (hE : ∀ e ∈ E, e.card = 2) (T : Finset ι) (h3 : 3 ≤ T.card)
    (hF : ∀ U ⊆ T, F U = ∑ a ∈ T, (if {a} ⊆ U then g a else 0)
        + ∑ e ∈ E, if e ⊆ U then b e else 0) :
    connected F T = 0 := by
  rw [connected_congr hF]
  change connected ((fun U => ∑ a ∈ T, (if {a} ⊆ U then g a else 0))
      + (fun U => ∑ e ∈ E, if e ⊆ U then b e else 0)) T = 0
  rw [connected_add, connected_finset_sum, connected_finset_sum]
  simp only [connected_weighted_contains]
  have h1 : ∀ a ∈ T, ({a} : Finset ι) ≠ T := fun a _ h => by
    have := congrArg Finset.card h; simp at this; omega
  have h2 : ∀ e ∈ E, e ≠ T := fun e he h => by
    have := hE e he; rw [h] at this; omega
  rw [Finset.sum_eq_zero fun a ha => if_neg (h1 a ha),
    Finset.sum_eq_zero fun e he => if_neg (h2 e he), add_zero]

end Cumulant

end QOU.VirtualSubword
