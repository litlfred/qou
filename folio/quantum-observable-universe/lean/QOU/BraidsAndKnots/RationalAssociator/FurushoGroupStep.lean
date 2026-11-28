import QOU.BraidsAndKnots.RationalAssociator.PentagonObstruction

/-!
# The group-level Furusho step: from any `K`-associator tower, and unconditionally for `E = 1`

Bean `qou-3fdg`, audit §17l.

`PentagonObstruction.lean` leaves two named `Prop`s, `PentagonLiftVanishes E d` and
`FurushoGroupStep E d`. This file proves both of them, and `ObstructionVanishesAt E d`, for every
`d ≥ 3`, from one input: some field `K ⊇ ℚ` carrying group-like `K`-associators for `E` modulo
every `N ≥ 2` (`GroupLikeKAssociatorTower K E`). Nothing ties those `K`-associators to `Φ`.

* `levelInv_of_assocU4`: for `d ≥ 3`, a rational associator `Φ` modulo degree `d`, group-like
  modulo `FF2 d`, carries the level invariant `LevelInv K E d Φ`. The invariant is built at
  degree 3 (`levelInv_three`) and pushed up one degree at a time by `LevelInv.succ_of_assoc`,
  using the truncations of `Φ` itself. This closes the gap noted in §17k ("the level invariant
  for an arbitrary `Φ` does not" exist).
* `furushoGroupStep_of_tower`, `obstructionVanishesAt_of_tower`,
  `pentagonLiftVanishes_of_tower`: the three `Prop`s, for every `d ≥ 3`, from the tower.
* `groupLikeKAssociatorTower_one`: for `E = 1` (the `μ = 0`, `GRT₁` case) the tower is
  inhabited by the constant `Ψ = 1`, over any `K`.
* `furushoGroupStep_one`, `obstructionVanishesAt_one`, `pentagonLiftVanishes_one`: hence, with
  no hypothesis at all, for every `d ≥ 3`. `furushoGroupStep_one` is the group-level form of
  Furusho's Lemma 9 (arXiv math/0702128v3, §2, p. 6-7: a commutator group-like `φ` with
  `c₂(φ) = 0` satisfying the 5-cycle relation satisfies the 3-cycle relation), one degree at a
  time. `obstructionVanishesAt_one` is the one-degree surjectivity `GRT₁ → GRT₁^{(d)}` that the
  same proof uses ("ψ also determines an element of grt₁(k)").

## How this relates to Furusho's argument

Furusho's Lemma 9 compares `φ` with `φ₁ = Exp ψ ∈ GRT₁` agreeing with `φ` modulo degree `n` and
writes `φ = φ₂ ∘ φ₁` (Lemma 8). Here the comparison object is the degree-`(d+1)` rational
associator `Φ + x` produced by `levelStep` from a `K`-associator re-aligned onto `Φ`
(`realign`, which shifts by `Exp` of a `grt` element); the difference `x` has a homogeneous
primitive layer, and the Lie-algebra theorem (`pentagonHexagonLie_of_three_le`, Furusho Thm 3)
kills its linearised defects. For `E = 1` the `K`-associator is `1`, so no existing associator
is used.

For `μ ≠ 0` Furusho's Theorem 10 (p. 7-8) passes to the weight-graded ring and imports
`Gr^W O(M₁) ≅ O(GRT₁)` from [F06, Theorem 6.2.2]; that input is not in the held text, and this
file does not reproduce it. So for `E ≠ 1` the step is proved here only from the tower.

No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct

local notation "F2" => FreeAlgebra ℚ (Fin 2)

variable {K : Type*} [Field K] [Algebra ℚ K]

/-! ### 1. The level invariant for an arbitrary associator modulo `d` -/

/-- **The level invariant holds for every rational associator modulo `d ≥ 3`**, given the
`K`-tower. -/
theorem levelInv_of_assocU4 {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {d : ℕ} (hd : 3 ≤ d) {Φ : F2}
    (hA : AssocU4 d E Φ) (hG : GL d Φ) : LevelInv K E d Φ := by
  have key : ∀ j, 3 ≤ j → j ≤ d → LevelInv K E j Φ := by
    intro j hj
    induction j, hj using Nat.le_induction with
    | base => exact fun hjd => levelInv_three hE hT (hA.trunc hjd) (FF2_anti hjd hG)
    | succ j hj ih =>
      intro hjd
      exact (ih (by omega)).succ_of_assoc (by omega) hE (hA.trunc hjd) (FF2_anti hjd hG)
  exact key d hd le_rfl

/-! ### 2. The three statements from the tower -/

/-- **Furusho's group-level step, from any `K`-associator tower**, for every `d ≥ 3`. -/
theorem furushoGroupStep_of_tower {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {d : ℕ} (hd : 3 ≤ d) : FurushoGroupStep E d := by
  intro Φ hA hG hp
  exact assocU4_succ_of_pentagon (by omega) (pentagonHexagonLie_of_three_le d hd) hE
    (levelInv_of_assocU4 hE hT hd hA (FF2_anti (by omega) hG)) hp hG

/-- **The one-degree lifting obstruction vanishes, from any `K`-associator tower**, for every
`d ≥ 3` and every rational associator `Φ` modulo `d` (not only the ones built from the tower). -/
theorem obstructionVanishesAt_of_tower {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {d : ℕ} (hd : 3 ≤ d) : ObstructionVanishesAt E d := by
  intro Φ hA hG
  obtain ⟨x, hx, ha, hg, -⟩ := levelStep hE (by omega) (levelInv_of_assocU4 hE hT hd hA hG)
  exact (lift_iff_obsLin (by omega) hE hA.const).1 ⟨x, hx, ha, hg⟩

/-- The pentagon part, from any `K`-associator tower, for every `d ≥ 3`. -/
theorem pentagonLiftVanishes_of_tower {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {d : ℕ} (hd : 3 ≤ d) : PentagonLiftVanishes E d :=
  ((obstructionVanishesAt_iff hE hd).1 (obstructionVanishesAt_of_tower hE hT hd)).1

/-! ### 3. The case `E = 1`: no tower needed -/

/-- `1` is a group-like `K`-associator for `E = 1` at every level. -/
theorem assocK_one (N : ℕ) : AssocK K N 1 (1 : K ⊗[ℚ] F2) where
  const := map_one _
  inv a b _ _ := by rw [map_one, map_one, one_mul]
  hex := by simp [HexagonF]
  pent := by simp [PentagonF]

theorem GLK_one (m : ℕ) : GLK K m (1 : K ⊗[ℚ] F2) := by
  unfold GLK
  rw [copK_one, i1K_one, i2K_one, one_mul, sub_self]
  exact zero_mem _

/-- **For `E = 1` the `K`-associator tower is inhabited**, by the constant `1`, over any field
`K ⊇ ℚ`. -/
theorem groupLikeKAssociatorTower_one : GroupLikeKAssociatorTower K (1 : F2) :=
  ⟨fun N _ => ⟨1, assocK_one N, GLK_one N⟩⟩

theorem algebraMapInv_one_F2 : FreeAlgebra.algebraMapInv (1 : F2) = 1 := map_one _

/-- **Furusho's group-level step for `E = 1`, unconditionally** (`d ≥ 3`): a rational element
of `GRT₁` modulo degree `d` (associator for `E = 1`), group-like modulo `FF2 (d + 1)` and
satisfying the pentagon modulo degree `d + 1`, is in `GRT₁` modulo degree `d + 1`. -/
theorem furushoGroupStep_one {d : ℕ} (hd : 3 ≤ d) : FurushoGroupStep (1 : F2) d :=
  furushoGroupStep_of_tower (K := ℚ) algebraMapInv_one_F2 groupLikeKAssociatorTower_one hd

/-- **Every rational element of `GRT₁` modulo `d ≥ 3` lifts one degree**, unconditionally. -/
theorem obstructionVanishesAt_one {d : ℕ} (hd : 3 ≤ d) : ObstructionVanishesAt (1 : F2) d :=
  obstructionVanishesAt_of_tower (K := ℚ) algebraMapInv_one_F2 groupLikeKAssociatorTower_one hd

/-- The pentagon part for `E = 1`, unconditionally. -/
theorem pentagonLiftVanishes_one {d : ℕ} (hd : 3 ≤ d) : PentagonLiftVanishes (1 : F2) d :=
  pentagonLiftVanishes_of_tower (K := ℚ) algebraMapInv_one_F2 groupLikeKAssociatorTower_one hd

end QOU.BraidsAndKnots.RationalAssociator
