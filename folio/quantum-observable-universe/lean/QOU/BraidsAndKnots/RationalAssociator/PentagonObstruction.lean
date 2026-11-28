import QOU.BraidsAndKnots.RationalAssociator.Obstruction
import QOU.BraidsAndKnots.RationalAssociator.FurushoHexagon

/-!
# The lifting obstruction splits into a pentagon part and a group-level Furusho step

Bean `qou-3fdg`, audit §17k.

`Obstruction.lean` states the one-degree lifting question as `ObstructionVanishesAt E d`: every
rational group-like associator `Φ` modulo degree `d` (for `E`) extends to one modulo degree
`d + 1`. Classically this needs a `K`-associator (KZ). This file removes the `K`-tower from the
statement of what is left, at the price of two named `Prop`s, and shows that nothing is lost:
for `d ≥ 3` the splitting is an **equivalence**.

* `exists_GL_lift`: the group-likeness half of the obstruction always vanishes. If `Φ` is
  group-like modulo `FF2 d`, some `x ∈ FF d` makes `Φ + x` group-like modulo `FF2 (d + 1)`.
  The proof builds a product of truncated exponentials of homogeneous primitives, one degree at
  a time (`GL_expPoly`, `exists_primitive_layer`); no field `K` and no logarithm.
* `PentagonLiftVanishes E d`: for every rational associator `Φ` modulo degree `d` (all of
  (5.12), the hexagon for `E` and the pentagon, modulo degree `d`), group-like
  modulo `FF2 (d + 1)`, a homogeneous primitive (Lie, by Friedrichs) `h` of degree `d` makes
  `Φ + h` satisfy the **pentagon alone** modulo degree `d + 1`. This is the obstruction in the
  pentagon (Drinfeld–Kohno / Stasheff) complex, an `H⁴`-type statement.
* `FurushoGroupStep E d`: a rational associator modulo degree `d`, group-like modulo
  `FF2 (d + 1)`, that satisfies the pentagon modulo degree `d + 1` is an associator modulo
  degree `d + 1`. This is the group-level form of Furusho's pentagon ⇒ hexagon at one degree.
* `obstructionVanishesAt_of_pentagon`: the two `Prop`s give `ObstructionVanishesAt E d`, for
  every `d ≥ 2`, with no `K`.
* `furushoGroupStep_of_obstructionVanishesAt`: conversely, for `d ≥ 3`, `ObstructionVanishesAt
  E d` gives the group-level step. This is where `pentagonHexagonLie_of_three_le` (#9876) is
  used: a lift `Φ + x` exists, the primitive layer `k` of `x` has zero linearised pentagon
  (both `Φ` and `Φ + x` satisfy the pentagon), so `assocLin k = 0`, so `Φ` already was an
  associator.
* `obstructionVanishesAt_iff`: for `d ≥ 3`,
  `ObstructionVanishesAt E d ↔ PentagonLiftVanishes E d ∧ FurushoGroupStep E d`.
* `compatible_of_pentagon_furusho`: a degree-3 seed and both `Prop`s for every `d ≥ 3` give a
  compatible sequence of rational group-like associators, with no `K`-tower.

## What is not proved

Neither `PentagonLiftVanishes E d` nor `FurushoGroupStep E d`. The first is the pentagon
`H⁴` statement: one would show the pentagon defect of `Φ` is a cocycle in the five-strand
complex and that such cocycles are coboundaries of Lie elements. The second is Furusho's
group-level theorem at one degree. Both are classical consequences of the existence of the KZ
associator; neither has an algebraic proof here. No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### 1. The group-likeness part of the obstruction vanishes -/

/-- Group-likeness is closed under products (over `ℚ`, via `GLK` at `K = ℚ`). -/
theorem GL.mul {m : ℕ} {a b : F2} (ha : GL m a) (hb : GL m b) : GL m (a * b) := by
  have h := GLK.mul (GLK_of_GL (K := ℚ) ha) (GLK_of_GL (K := ℚ) hb)
  rw [Algebra.TensorProduct.tmul_mul_tmul, mul_one] at h
  exact GL_of_GLK h

theorem GL_one (m : ℕ) : GL m (1 : F2) := by
  unfold GL
  rw [map_one, Algebra.TensorProduct.one_def, sub_self]
  exact zero_mem _

/-- **The group-likeness half of the obstruction vanishes.** If `ε(Φ) = 1` and `Φ` is
group-like modulo `FF2 d` (`d ≥ 1`), there is `x ∈ FF d` with `Φ + x` group-like modulo
`FF2 (d + 1)`. -/
theorem exists_GL_lift {d : ℕ} (hd : 1 ≤ d) {Φ : F2} (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hg : GL d Φ) : ∃ x ∈ FF d, GL (d + 1) (Φ + x) := by
  have hΦ1 := sub_one_mem_FF_one hΦ
  have key : ∀ m, 1 ≤ m → m ≤ d → ∃ Ψ : F2, GL (d + 1) Ψ ∧ Ψ - Φ ∈ FF m := by
    intro m hm
    induction m, hm using Nat.le_induction with
    | base =>
      intro _
      refine ⟨1, GL_one _, ?_⟩
      rw [← neg_sub]; exact neg_mem hΦ1
    | succ m hm ih =>
      intro hmd
      obtain ⟨Ψ, hΨ, hΨΦ⟩ := ih (by omega)
      set y := Φ - Ψ with hy
      have hyF : y ∈ FF m := by rw [hy, ← neg_sub]; exact neg_mem hΨΦ
      have hΨ1 : Ψ - 1 ∈ FF 1 := by
        have e : Ψ - 1 = (Ψ - Φ) + (Φ - 1) := by abel
        rw [e]; exact add_mem (FF_anti hm hΨΦ) hΦ1
      have hδ : primDef y ∈ FF2 (m + 1) := by
        refine primDef_mem_of_GL_add hm hΨ1 hyF (FF2_anti (by omega) hΨ) ?_
        rw [hy, add_sub_cancel]; exact FF2_anti (by omega) hg
      obtain ⟨k, -, hyk, hkp⟩ := exists_primitive_layer hyF hδ
      have hkF : k ∈ FF m := by
        have e : k = y - (y - k) := by abel
        rw [e]; exact sub_mem hyF (FF_anti (by omega) hyk)
      refine ⟨Ψ * expPoly k (d + 1), hΨ.mul (GL_expPoly hkp (FF_anti hm hkF) _), ?_⟩
      have e : Ψ * expPoly k (d + 1) - Φ =
          Ψ * (expPoly k (d + 1) - 1 - k) + (Ψ - 1) * k - (y - k) := by
        rw [hy]; noncomm_ring
      rw [e]
      refine sub_mem (add_mem ?_ ?_) hyk
      · exact mul_mem_FF' (zero_add _) (mem_FF_zero Ψ)
          (expPoly_congr hm (by omega) hkF)
      · exact mul_mem_FF' (by omega) hΨ1 hkF
  obtain ⟨Ψ, hΨ, hΨΦ⟩ := key d hd le_rfl
  exact ⟨Ψ - Φ, hΨΦ, by rwa [add_sub_cancel]⟩

/-! ### 2. The two remaining statements -/

/-- The one-degree lifting statement of `AssociatorObstructionVanishes`, at a single `d`. -/
def ObstructionVanishesAt (E : F2) (d : ℕ) : Prop :=
  ∀ Φ : F2, AssocU4 d E Φ → GL d Φ → ∃ x ∈ FF d, obsLin d x = obstruction d E Φ

theorem associatorObstructionVanishes_iff (E : F2) :
    AssociatorObstructionVanishes E ↔ ∀ d, 1 ≤ d → ObstructionVanishesAt E d :=
  Iff.rfl

/-- **The pentagon (`H⁴`-type) part of the obstruction, as a statement** (a `Prop`, not
proved). A rational associator modulo degree `d`, group-like modulo `FF2 (d + 1)`, has a
homogeneous primitive correction of degree `d` after which the pentagon alone holds modulo
degree `d + 1`. -/
def PentagonLiftVanishes (E : F2) (d : ℕ) : Prop :=
  ∀ Φ : F2, AssocU4 d E Φ → GL (d + 1) Φ →
    ∃ h ∈ FF d, Homog d h ∧ IsPrimitive h ∧
      Pentagon (Φ + h) (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5)

/-- **Furusho's pentagon ⇒ hexagon, group level, at one degree** (a `Prop`, not proved). A
rational associator modulo degree `d`, group-like modulo `FF2 (d + 1)`, satisfying the pentagon
modulo degree `d + 1`, is an associator modulo degree `d + 1`. -/
def FurushoGroupStep (E : F2) (d : ℕ) : Prop :=
  ∀ Φ : F2, AssocU4 d E Φ → GL (d + 1) Φ →
    Pentagon Φ (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5) →
      AssocU4 (d + 1) E Φ

/-! ### 3. The splitting -/

/-- Adding an element of `FF d` does not change being an associator modulo degree `d`. -/
theorem AssocU4.add_FF {d : ℕ} (hd : 2 ≤ d) {E Φ x : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (h : AssocU4 d E Φ) (hx : x ∈ FF d) : AssocU4 d E (Φ + x) := by
  obtain ⟨e, rfl⟩ : ∃ e, d = e + 1 := ⟨d - 1, by omega⟩
  refine (assocU4_add_iff (by omega) hE h.const (FF_anti (by omega) hx)).2 ?_
  rw [assocLin_eq_zero_of_mem_FF hx, (assocU4_iff.1 h).2, neg_zero]

/-- Adding a homogeneous primitive of degree `d` keeps group-likeness modulo `FF2 (d + 1)`. -/
theorem GL.add_primitive {d : ℕ} (hd : 1 ≤ d) {Φ h : F2} (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hg : GL (d + 1) Φ) (hF : h ∈ FF d) (hp : IsPrimitive h) : GL (d + 1) (Φ + h) := by
  rw [GL_add_iff hd (sub_one_mem_FF_one hΦ) hF, (isPrimitive_iff h).1 hp, add_zero]
  exact hg

/-- **The two statements give the obstruction vanishing**, at any `d ≥ 2`, with no field `K`. -/
theorem obstructionVanishesAt_of_pentagon {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 2 ≤ d) (hP : PentagonLiftVanishes E d) (hF : FurushoGroupStep E d) :
    ObstructionVanishesAt E d := by
  intro Φ hA hG
  obtain ⟨x, hx, hgx⟩ := exists_GL_lift (by omega) hA.const hG
  have hA1 : AssocU4 d E (Φ + x) := hA.add_FF hd hE hx
  obtain ⟨h, hhF, -, hhp, hpent⟩ := hP (Φ + x) hA1 hgx
  have hc1 : FreeAlgebra.algebraMapInv (Φ + x) = 1 := hA1.const
  have hA2 : AssocU4 d E (Φ + x + h) := hA1.add_FF hd hE hhF
  have hg2 : GL (d + 1) (Φ + x + h) := hgx.add_primitive (by omega) hc1 hhF hhp
  have hfin := hF _ hA2 hg2 hpent
  refine (lift_iff_obsLin (by omega) hE hA.const).1 ⟨x + h, add_mem hx hhF, ?_, ?_⟩
  · rwa [← add_assoc]
  · rwa [← add_assoc]

/-- **Conversely, for `d ≥ 3` the obstruction vanishing gives the group-level Furusho step.**
This uses the Lie-algebra form of Furusho's theorem (`pentagonHexagonLie_of_three_le`). -/
theorem furushoGroupStep_of_obstructionVanishesAt {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 3 ≤ d) (hV : ObstructionVanishesAt E d) : FurushoGroupStep E d := by
  intro Φ hA hG hp
  have hΦ := hA.const
  obtain ⟨x₀, hx₀, hl⟩ := hV Φ hA (FF2_anti (by omega) hG)
  obtain ⟨x, hx, ha, hgx⟩ := (lift_iff_obsLin (by omega) hE hΦ).2 ⟨x₀, hx₀, hl⟩
  have hδ : primDef x ∈ FF2 (d + 1) :=
    primDef_mem_of_GL_add (by omega) (sub_one_mem_FF_one hΦ) hx hG hgx
  obtain ⟨k, hk, hxk, hkp⟩ := exists_primitive_layer hx hδ
  have hdef : assocDefect (d + 1) E Φ = -assocLin (d + 1) x := by
    have h0 := (assocU4_iff.1 ha).2
    rw [assocDefect_add (by omega) hE hΦ hx] at h0
    exact eq_neg_of_add_eq_zero_left h0
  have hlk : assocLin (d + 1) k = assocLin (d + 1) x := by
    have e : k = x - (x - k) := by abel
    rw [e, map_sub, assocLin_eq_zero_of_mem_FF hxk, sub_zero]
  have hpk : (assocLin (d + 1) k).2.2 = 0 := by
    rw [hlk, ← neg_neg (assocLin (d + 1) x), ← hdef, Prod.snd_neg, Prod.snd_neg,
      assocDefect_pent_eq_zero hp, neg_zero]
  have hk0 := pentagonHexagonLie_of_three_le d hd k hk hkp hpk
  refine assocU4_iff.2 ⟨hΦ, ?_⟩
  rw [hdef, ← hlk, hk0, neg_zero]

/-- For `d ≥ 3` the obstruction vanishing implies the pentagon lift (trivially). -/
theorem pentagonLiftVanishes_of_obstructionVanishesAt {E : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) {d : ℕ} (hd : 1 ≤ d)
    (hV : ObstructionVanishesAt E d) : PentagonLiftVanishes E d := by
  intro Φ hA hG
  have hΦ := hA.const
  obtain ⟨h, hhF, hh, hhp, hl⟩ :=
    (lift_iff_primitive hd hE hΦ hG).1
      ((lift_iff_obsLin hd hE hΦ).2 (hV Φ hA (FF2_anti (by omega) hG)))
  exact ⟨h, hhF, hh, hhp, ((assocU4_add_iff hd hE hΦ hhF).2 hl).pent⟩

/-- **The splitting is exact for `d ≥ 3`.** -/
theorem obstructionVanishesAt_iff {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) {d : ℕ}
    (hd : 3 ≤ d) :
    ObstructionVanishesAt E d ↔ PentagonLiftVanishes E d ∧ FurushoGroupStep E d :=
  ⟨fun hV => ⟨pentagonLiftVanishes_of_obstructionVanishesAt hE (by omega) hV,
      furushoGroupStep_of_obstructionVanishesAt hE hd hV⟩,
    fun h => obstructionVanishesAt_of_pentagon hE (by omega) h.1 h.2⟩

/-! ### 4. The tower, with no `K` -/

/-- **A compatible rational tower from a degree-3 seed and the two statements**, with no field
`K` and no `GroupLikeKAssociatorTower`. -/
theorem compatible_of_pentagon_furusho {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {Φ₃ : F2} (h3 : AssocU4 3 E Φ₃) (hg3 : GL 3 Φ₃)
    (hP : ∀ d, 3 ≤ d → PentagonLiftVanishes E d) (hF : ∀ d, 3 ≤ d → FurushoGroupStep E d) :
    ∃ Φ : ℕ → F2, (∀ N, 3 ≤ N → AssocU4 N E (Φ N) ∧ GL N (Φ N)) ∧
      ∀ N, 3 ≤ N → Φ (N + 1) - Φ N ∈ FF N := by
  obtain ⟨f, -, hf⟩ := exists_seq_of_step (α := F2)
    (fun k a => AssocU4 (k + 3) E a ∧ GL (k + 3) a)
    (fun k a b => b - a ∈ FF (k + 3))
    (a₀ := Φ₃) ⟨h3, hg3⟩ (fun k a ha => by
      have hV := obstructionVanishesAt_of_pentagon hE (by omega : 2 ≤ k + 3)
        (hP (k + 3) (by omega)) (hF (k + 3) (by omega))
      obtain ⟨x, hx, hl⟩ := hV a ha.1 ha.2
      obtain ⟨y, hy, hA, hG⟩ :=
        (lift_iff_obsLin (by omega : 1 ≤ k + 3) hE ha.1.const).2 ⟨x, hx, hl⟩
      exact ⟨a + y, ⟨hA, hG⟩, by simpa using hy⟩)
  refine ⟨fun N => f (N - 3), fun N hN => ?_, fun N hN => ?_⟩
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 3 := ⟨N - 3, by omega⟩
    simpa using (hf k).1
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 3 := ⟨N - 3, by omega⟩
    have := (hf k).2
    simpa [show k + 3 + 1 - 3 = k + 1 by omega] using this

end QOU.BraidsAndKnots.RationalAssociator
