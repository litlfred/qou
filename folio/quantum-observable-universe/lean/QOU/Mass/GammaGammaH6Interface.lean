import QOU.Mass.GammaGammaFrobeniusSelection

/-!
# The `H₆` interface: the pp bond `(σ₂σ₃⁻¹)^m` is selected by the `H₃` sign table through branching

Bean `qou-ales`, step 6 (owner order 2026-09-12: after merging step 5, *"3"* — the `H₆`
pp bond in Lean). Step 3 (#7192) **measured** on all eleven Wedderburn blocks of `H₆`
that, among the γγ bond candidates `G^m = (σ₂σ₃⁻¹)^m` on the interface between two
nucleon blocks, the minimal non-zero survivor under the Frobenius reading is `G³`,
with the `(3,3)` block the worst offender for every other `m`. This file explains that
table by the branching rule and proves it on an interval.

## The mechanism

The bond word lives in the parabolic subalgebra `⟨σ₂, σ₃⟩ ≅ H₃`. Restricted to it,
each `H₆` irreducible `V_λ` decomposes into `H₃` irreducibles with multiplicities
`(a_λ, b_λ, c_λ)` for `((3), (2,1), (1³))`, and on a γγ word of that subalgebra the
`(3)` and `(1³)` characters are `1` (`trivChar_eq_one`, `altChar_eq_one`), so

    χ_λ(G^m) = a_λ + b_λ · χ_(2,1)(V^m) + c_λ            (`branchedChar`).

By the branching rule (Hoefsmit 1974; for the middle-strand embedding, conjugation by
the distinguished coset representative `T_d`, Dipper–James) the multiplicities are
**path counts in Young's lattice** from `μ ⊢ 3` to `λ ⊢ 6`; this file computes them
by `decide` (`branchOf_*`) and checks `f^λ = a + 2b + c` on all eleven blocks
(`dim_eq_branch`) and `Σ (f^λ)² = 720` (`fDim_sq_sum`).

Convention D (the two-row truncation, owner ruling 2026-08-15 / 2026-09-08) puts the
Markov weight on the two-row partitions `(6), (5,1), (4,2), (3,3)` only; their branching
data are `(1,0,0), (3,1,0), (3,3,0), (1,2,0)`. So under reading 3 the bond `G^m` is
feasible iff `1 + 2χ_m ≥ 0` at `(3,3)` (the other three are weaker), and the `H₃` sign
table decides it.

## What is proved (all sorry-free)

* `branchOf_six … branchOf_threeThree`, `dim_eq_branch`, `fDim_sq_sum` — the path counts.
* `interfaceBond_gammaGamma` — `(σ₂σ₃⁻¹)^m` is γγ-produced.
* `InterfaceBranching q B` — the hypothesis that the block data `B` takes the branched
  values on the interface bonds (the branching rule, **stated, not derived** here;
  verified at the proton pin by `gamma_gamma_h6_interface_branching_probe.py`, 24 values
  to `1e−59` against the step-3 witness).
* `interface_frobeniusFeasible_iff` — under it, reading-3 feasibility of `G^m` is the
  sign condition on the branched characters of the positive-weight blocks.
* `h6_signs_of_small` — for every `0 < x ≤ 1/12`, `1 + 2χ_m(x) < 0` for `m = 1, 2, 4, 5`.
  The interval is **narrower** than step 4's `1/10`: `1 + 2χ_5` changes sign near
  `x ≈ 0.0924`, so the `H₆` selection is not a theorem on `x ≤ 1/10`; `1 < q ≤ 23/20`
  gives `h² ≤ 0.0787 ≤ 1/12` (`h_sq_le_twelfth_of_q_le`) and still contains the pin.
* `interface_frobenius_table` — for every `1 < q ≤ 23/20`, every two-row-supported
  weight with `y_(3,3) > 0`: `G¹, G², G⁴, G⁵` infeasible, `G³` feasible.
* `interfaceSelected_three` — the minimal-crossing feasible non-zero bond with `m ≤ 5`
  is `G³`.

## What is NOT proved

* The branching rule itself (the `InterfaceBranching` hypothesis).
* The diproton sign `B_pp = −4.47` keV: it needs the full 11-letter nucleon words in
  `H₆`, and stays a step-3 measurement.
* `m > 5`; non-γγ letters.

Nothing here reads AME2020, a CODATA binding value, or a census.

## Base ring (§7c)

The Young-lattice section is pure `ℕ`. `branchedChar` and the interval lemmas are on
`ℝ`, as the step-4/5 sign lemmas they extend.
-/

namespace QOU.Mass.GammaGammaH6Interface

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaVertexOrder
open QOU.Mass.GammaGammaFrobeniusSelection

/-! ## Young's lattice, levels `3 → 6`: path counts -/

section Young

/-- A partition, as a weakly decreasing list of positive parts. -/
abbrev Part := List ℕ

/-- Decides the partition condition. -/
def isPartition : Part → Bool
  | [] => true
  | [a] => decide (0 < a)
  | a :: b :: r => decide (b ≤ a) && isPartition (b :: r)

/-- Add one box in row `i` (a new row when `i` is the length). Out-of-range
indices return `[]`, which `covers` filters out. -/
def addBox : Part → ℕ → Part
  | [], 0 => [1]
  | [], _ + 1 => []
  | a :: r, 0 => (a + 1) :: r
  | a :: r, i + 1 => a :: addBox r i

/-- The partitions covering `μ` in Young's lattice. -/
def covers (μ : Part) : List Part :=
  ((List.range (μ.length + 1)).map (addBox μ)).filter
    (fun ν => isPartition ν && ν.sum == μ.sum + 1)

/-- Number of saturated chains `μ ⊂ … ⊂ lam` in Young's lattice, with fuel. -/
def pathCount : ℕ → Part → Part → ℕ
  | 0, μ, lam => if μ = lam then 1 else 0
  | n + 1, μ, lam =>
    if μ = lam then 1 else ((covers μ).map (fun ν => pathCount n ν lam)).sum

/-- `f^λ`, the number of standard Young tableaux, as paths from `∅`. -/
def fDim (lam : Part) : ℕ := pathCount 6 [] lam

/-- Multiplicities of `(3), (2,1), (1³)` in the restriction of `V_λ`, `λ ⊢ 6`, to a
parabolic `H₃` — by the branching rule, the path counts from `μ ⊢ 3` to `λ`. -/
structure Branching where
  /-- multiplicity of the trivial block `(3)` -/
  a : ℕ
  /-- multiplicity of the standard block `(2,1)` -/
  b : ℕ
  /-- multiplicity of the sign block `(1³)` -/
  c : ℕ
  deriving DecidableEq, Repr

/-- The branching data of `λ ⊢ 6`. -/
def branchOf (lam : Part) : Branching :=
  ⟨pathCount 3 [3] lam, pathCount 3 [2, 1] lam, pathCount 3 [1, 1, 1] lam⟩

theorem branchOf_six : branchOf [6] = ⟨1, 0, 0⟩ := by decide
theorem branchOf_fiveOne : branchOf [5, 1] = ⟨3, 1, 0⟩ := by decide
theorem branchOf_fourTwo : branchOf [4, 2] = ⟨3, 3, 0⟩ := by decide
theorem branchOf_threeThree : branchOf [3, 3] = ⟨1, 2, 0⟩ := by decide

/-- The eleven Wedderburn blocks of `H₆`. -/
inductive H6Block
  | six | fiveOne | fourTwo | fourOneOne | threeThree | threeTwoOne | threeOneOneOne
  | twoTwoTwo | twoTwoOneOne | twoOneOneOneOne | oneSix
  deriving DecidableEq

/-- The partition of a block. -/
def H6Block.part : H6Block → Part
  | .six => [6]
  | .fiveOne => [5, 1]
  | .fourTwo => [4, 2]
  | .fourOneOne => [4, 1, 1]
  | .threeThree => [3, 3]
  | .threeTwoOne => [3, 2, 1]
  | .threeOneOneOne => [3, 1, 1, 1]
  | .twoTwoTwo => [2, 2, 2]
  | .twoTwoOneOne => [2, 2, 1, 1]
  | .twoOneOneOneOne => [2, 1, 1, 1, 1]
  | .oneSix => [1, 1, 1, 1, 1, 1]

/-- Block dimension `f^λ`. -/
def H6Block.dim (l : H6Block) : ℕ := fDim l.part

/-- The two-row blocks — the support of the convention-D (two-row truncation)
Markov weight at `n = 6`. -/
def H6Block.twoRow (l : H6Block) : Prop :=
  l = .six ∨ l = .fiveOne ∨ l = .fourTwo ∨ l = .threeThree

/-- **Dimension consistency on all eleven blocks**: `f^λ = a + 2b + c`, i.e. the
paths `∅ → λ` factor through level 3. -/
theorem dim_eq_branch (l : H6Block) :
    l.dim = (branchOf l.part).a + 2 * (branchOf l.part).b + (branchOf l.part).c := by
  cases l <;> decide

/-- Burnside at `n = 6`: `Σ_λ (f^λ)² = 720`. -/
theorem fDim_sq_sum :
    fDim [6] ^ 2 + fDim [5, 1] ^ 2 + fDim [4, 2] ^ 2 + fDim [4, 1, 1] ^ 2 + fDim [3, 3] ^ 2 +
      fDim [3, 2, 1] ^ 2 + fDim [3, 1, 1, 1] ^ 2 + fDim [2, 2, 2] ^ 2 + fDim [2, 2, 1, 1] ^ 2 +
      fDim [2, 1, 1, 1, 1] ^ 2 + fDim [1, 1, 1, 1, 1, 1] ^ 2 = 720 := by
  decide

end Young

/-! ## The branched character -/

/-- The character of a block with branching data `β` on a γγ word of the interface
`H₃`, given that word's `(2,1)` character `chi`: each `(3)` and `(1³)` copy contributes
`1`, each `(2,1)` copy contributes `chi`. -/
def branchedChar (β : Branching) (chi : ℝ) : ℝ := β.a + β.b * chi + β.c

theorem branchedChar_six (t : ℝ) : branchedChar (branchOf H6Block.six.part) t = 1 := by
  rw [show H6Block.six.part = [6] from rfl, branchOf_six]; norm_num [branchedChar]

theorem branchedChar_fiveOne (t : ℝ) :
    branchedChar (branchOf H6Block.fiveOne.part) t = 3 + t := by
  rw [show H6Block.fiveOne.part = [5, 1] from rfl, branchOf_fiveOne]; norm_num [branchedChar]

theorem branchedChar_fourTwo (t : ℝ) :
    branchedChar (branchOf H6Block.fourTwo.part) t = 3 + 3 * t := by
  rw [show H6Block.fourTwo.part = [4, 2] from rfl, branchOf_fourTwo]; norm_num [branchedChar]

theorem branchedChar_threeThree (t : ℝ) :
    branchedChar (branchOf H6Block.threeThree.part) t = 1 + 2 * t := by
  rw [show H6Block.threeThree.part = [3, 3] from rfl, branchOf_threeThree]
  norm_num [branchedChar]

/-! ## Interface words -/

section Words

/-- Shift every generator index by `k`. -/
def shift (k : ℕ) (w : Word) : Word := w.map fun c => ⟨c.gen + k, c.pos⟩

theorem shift_append (k : ℕ) (u v : Word) : shift k (u ++ v) = shift k u ++ shift k v :=
  List.map_append

theorem shift_vertex (k i : ℕ) : shift k (vertex i) = vertex (i + k) := by
  have h : i + 1 + k = i + k + 1 := by omega
  simp [shift, vertex, h]

theorem shift_length (k : ℕ) (w : Word) : (shift k w).length = w.length :=
  List.length_map _

/-- A shifted γγ word is γγ-produced. -/
theorem gammaGamma_shift (k : ℕ) {w : Word} (h : GammaGammaWord w) :
    GammaGammaWord (shift k w) := by
  induction h with
  | nil => exact .nil
  | cons i _ ih =>
    rw [shift_append, shift_vertex]
    exact .cons (i + k) ih

/-- The interface bond `G^m = (σ₂σ₃⁻¹)^m` between two three-strand nucleon blocks. -/
def interfaceBond (m : ℕ) : Word := shift 2 (vertexPow m)

theorem interfaceBond_gammaGamma (m : ℕ) : GammaGammaWord (interfaceBond m) :=
  gammaGamma_shift 2 (vertexPow_gammaGamma m)

theorem interfaceBond_length (m : ℕ) : (interfaceBond m).length = 2 * m := by
  rw [interfaceBond, shift_length, vertexPow_length]

/-- The selected bond, explicitly: `σ₂ σ₃⁻¹ σ₂ σ₃⁻¹ σ₂ σ₃⁻¹`. -/
theorem interfaceBond_three :
    interfaceBond 3 = [⟨2, true⟩, ⟨3, false⟩, ⟨2, true⟩, ⟨3, false⟩, ⟨2, true⟩, ⟨3, false⟩] := by
  decide

end Words

/-! ## The branching hypothesis and what it decides -/

section Interface

/-- **Interface branching**: the `H₆` block data `B` takes, on every interface bond,
the branched value of the step-4/5 vertex character. This is the branching rule for
the Hoefsmit representations restricted to `⟨σ₂, σ₃⟩`, stated as a hypothesis. -/
structure InterfaceBranching (q : ℝ) (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) :
    Prop where
  /-- `χ_λ(G^m) = a_λ + b_λ · tr V^m + c_λ`. -/
  branched : ∀ (l : H6Block) (m : ℕ),
    (B.proj (interfaceBond m) l).trace = branchedChar (branchOf l.part) (hoefsmitVtx q ^ m).trace

/-- Under the branching hypothesis, reading-3 feasibility of `G^m` is the sign condition
on the branched characters of the positive-weight blocks. -/
theorem interface_frobeniusFeasible_iff {q : ℝ} (B : WedderburnBlocks ℝ Word H6Block H6Block.dim)
    (hB : InterfaceBranching q B) (y : H6Block → ℝ) (m : ℕ) :
    FrobeniusFeasible B y (interfaceBond m) ↔
      ∀ l : H6Block, 0 < y l → 0 ≤ branchedChar (branchOf l.part) (hoefsmitVtx q ^ m).trace := by
  constructor
  · intro h l hl
    rw [← hB.branched]
    exact h l hl
  · intro h l hl
    rw [hB.branched]
    exact h l hl

/-- **The `(3,3)` sign condition `1 + 2χ_m < 0` for `m = 1, 2, 4, 5`, on `0 < x ≤ 1/12`.**
The bound is `1/12`, not step 4's `1/10`: `1 + 2χ_5` crosses zero near `x ≈ 0.0924`. -/
theorem h6_signs_of_small {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1 / 12) :
    1 + 2 * (-1 - x) < 0 ∧ 1 + 2 * (x ^ 2 + 2 * x - 1) < 0 ∧
      1 + 2 * (x ^ 4 + 4 * x ^ 3 + 2 * x ^ 2 - 4 * x - 1) < 0 ∧
      1 + 2 * (-x ^ 5 - 5 * x ^ 4 - 5 * x ^ 3 + 5 * x ^ 2 + 5 * x - 1) < 0 := by
  have h2 : x ^ 2 ≤ x / 12 := by nlinarith
  have h3 : x ^ 3 ≤ x / 144 := by nlinarith [pow_nonneg hx.le 2]
  have h4 : x ^ 4 ≤ x / 1728 := by nlinarith [pow_nonneg hx.le 3]
  have p3 : 0 ≤ x ^ 3 := by positivity
  have p4 : 0 ≤ x ^ 4 := by positivity
  have p5 : 0 ≤ x ^ 5 := by positivity
  refine ⟨by linarith, by linarith, by linarith, by linarith⟩

/-- `1 ≤ q ≤ 23/20 ⇒ h² ≤ 1/12` (`h² ≤ 0.0787` there). -/
theorem h_sq_le_twelfth_of_q_le {q : ℝ} (hq1 : 1 ≤ q) (hq2 : q ≤ 23 / 20) :
    (q - q⁻¹) ^ 2 ≤ 1 / 12 := by
  have hq0 : 0 < q := by linarith
  have hi1 : q⁻¹ ≤ 1 := inv_le_one_of_one_le₀ hq1
  have hi2 : 20 / 23 ≤ q⁻¹ := by
    rw [le_inv_comm₀ (by norm_num) hq0]
    calc q ≤ 23 / 20 := hq2
      _ = (20 / 23 : ℝ)⁻¹ := by norm_num
  have hh0 : 0 ≤ q - q⁻¹ := by linarith
  have hh1 : q - q⁻¹ ≤ 129 / 460 := by linarith
  nlinarith

/-- **The `H₆` bond table under reading 3**, for every `1 < q ≤ 23/20`, every block data
satisfying the branching hypothesis, and every Markov weight supported on the two-row
blocks with `y_(3,3) > 0`: `G¹, G², G⁴, G⁵` are infeasible and `G³` is feasible. -/
theorem interface_frobenius_table {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) (hB : InterfaceBranching q B)
    (y : H6Block → ℝ) (hy : ∀ l, 0 < y l → l.twoRow) (h33 : 0 < y .threeThree) :
    ¬ FrobeniusFeasible B y (interfaceBond 1) ∧
      ¬ FrobeniusFeasible B y (interfaceBond 2) ∧
      FrobeniusFeasible B y (interfaceBond 3) ∧
      ¬ FrobeniusFeasible B y (interfaceBond 4) ∧
      ¬ FrobeniusFeasible B y (interfaceBond 5) := by
  obtain ⟨hx, _⟩ := hOf_sq_bounds hq1 hq2
  have hx12 : hOf q ^ 2 ≤ 1 / 12 := h_sq_le_twelfth_of_q_le hq1.le hq2
  obtain ⟨t1, t2, t3, t4, t5⟩ := hoefsmitVtx_traces hq1
  obtain ⟨s1, s2, s4, s5⟩ := h6_signs_of_small hx hx12
  have s3 := (chi_signs_of_small hx (by linarith)).2.2.1
  simp only [interface_frobeniusFeasible_iff B hB y]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t1] at this; linarith
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t2] at this; linarith
  · intro l hl
    rcases hy l hl with rfl | rfl | rfl | rfl
    · rw [branchedChar_six]; norm_num
    · rw [branchedChar_fiveOne, t3]; linarith
    · rw [branchedChar_fourTwo, t3]; linarith
    · rw [branchedChar_threeThree, t3]; linarith
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t4] at this; linarith
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t5] at this; linarith

/-- The candidate bonds: the non-zero interface γγ bonds with `1 ≤ m ≤ n`. -/
def interfaceCands (n : ℕ) : Set Word := {w | ∃ m, 1 ≤ m ∧ m ≤ n ∧ w = interfaceBond m}

/-- **Reading 3 selects the pp bond `G³ = (σ₂σ₃⁻¹)³`** on the `H₆` interface: the
minimal-crossing feasible non-zero bond with `m ≤ 5`, for every `1 < q ≤ 23/20`, under
the branching hypothesis and any two-row-supported weight with `y_(3,3) > 0`. -/
theorem interfaceSelected_three {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) (hB : InterfaceBranching q B)
    (y : H6Block → ℝ) (hy : ∀ l, 0 < y l → l.twoRow) (h33 : 0 < y .threeThree) :
    FrobeniusSelected B y (interfaceCands 5) (fun w => (w.length : ℝ)) (interfaceBond 3) := by
  obtain ⟨n1, n2, f3, n4, n5⟩ := interface_frobenius_table hq1 hq2 B hB y hy h33
  refine ⟨⟨3, by norm_num, by norm_num, rfl⟩, f3, ?_⟩
  rintro w' ⟨m, hm1, hm5, rfl⟩ hf
  interval_cases m
  · exact absurd hf n1
  · exact absurd hf n2
  · exact le_rfl
  · exact absurd hf n4
  · exact absurd hf n5

/-- Any reading-3-selected bond on these candidates has six crossings. -/
theorem interfaceSelected_length_eq_six {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) (hB : InterfaceBranching q B)
    (y : H6Block → ℝ) (hy : ∀ l, 0 < y l → l.twoRow) (h33 : 0 < y .threeThree) {w : Word}
    (hw : FrobeniusSelected B y (interfaceCands 5) (fun w => (w.length : ℝ)) w) :
    w.length = 6 := by
  have h := hw.cost_eq (interfaceSelected_three hq1 hq2 B hB y hy h33)
  have : (w.length : ℝ) = ((interfaceBond 3).length : ℝ) := by simpa using h
  rw [interfaceBond_length] at this
  exact_mod_cast this

end Interface

end QOU.Mass.GammaGammaH6Interface
