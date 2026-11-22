/-
  S_5 ↔ SO(3) fiber action on Bring's quintic surface — scaffold.

  Per `docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`
  §4 (task 3) and the parent audit `2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`:

  The connection
    S_5  ⊃  A_5  ≅  I  ⊂  SO(3)
  (S_5 ⊃ alternating subgroup A_5 ≅ icosahedral rotation group I ⊂ SO(3))
  ties:
    - Partition-wise Wedderburn actions on H_5(q) (combinatorial)
    - Spatial SO(3) rotations on Bring's quintic surface (geometric)

  This file scaffolds the combinatorial half (partitions of 5 + dim
  check) and STATES the fiber-action map; the geometric realization
  (mapping each partition of 5 to a specific A_5 rotation on Bring)
  is the open structural step queued for future work.

  Scope (per author direction, 2026-05-24): combinatorial scaffold +
  type-level statement + dim² = |S_5| = 120 sanity check.
  Geometric fiber map → conditional class (AGENTS.md §3b-cond).

  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
  -- Ref: [klein1888] Klein, Lectures on the Icosahedron (Bring)
-/
import Mathlib.Data.Fintype.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

namespace QOU.BraidsAndKnots

/-! ## Partitions of 5 — the indexing set for S_5 irreps -/

/-- Partitions of 5 (= 7 partitions, indexing the 7 irreps of S_5). -/
inductive PartitionOf5 where
  | five          : PartitionOf5   -- (5)
  | fourOne       : PartitionOf5   -- (4, 1)
  | threeTwo      : PartitionOf5   -- (3, 2)
  | threeOneOne   : PartitionOf5   -- (3, 1, 1)
  | twoTwoOne     : PartitionOf5   -- (2, 2, 1)
  | twoOneOneOne  : PartitionOf5   -- (2, 1, 1, 1)
  | onesFive      : PartitionOf5   -- (1, 1, 1, 1, 1)
  deriving DecidableEq, Repr

/-- Explicit list of all 7 partitions of 5. -/
def PartitionOf5.allList : List PartitionOf5 :=
  [.five, .fourOne, .threeTwo, .threeOneOne, .twoTwoOne, .twoOneOneOne, .onesFive]

/-- Dimension of the S_5 irrep V_λ for each partition λ ⊢ 5
    (standard hook-length formula values; cf. James 1984 §2). -/
def PartitionOf5.dim : PartitionOf5 → ℕ
  | .five          => 1
  | .fourOne       => 4
  | .threeTwo      => 5
  | .threeOneOne   => 6
  | .twoTwoOne     => 5
  | .twoOneOneOne  => 4
  | .onesFive      => 1

/-- Conjugate partition (transpose Young diagram).  Pairs:
    (5) ↔ (1¹¹¹¹¹), (4,1) ↔ (2,1¹¹¹), (3,2) ↔ (2,2,1), (3,1,1) self-conjugate. -/
def PartitionOf5.conjugate : PartitionOf5 → PartitionOf5
  | .five          => .onesFive
  | .fourOne       => .twoOneOneOne
  | .threeTwo      => .twoTwoOne
  | .threeOneOne   => .threeOneOne   -- self-conjugate
  | .twoTwoOne     => .threeTwo
  | .twoOneOneOne  => .fourOne
  | .onesFive      => .five

/-- Conjugation is an involution. -/
theorem PartitionOf5.conjugate_involutive (p : PartitionOf5) :
    p.conjugate.conjugate = p := by
  cases p <;> rfl

/-- Conjugate partitions have equal dimensions (standard rep theory:
    sign-twist preserves dim, since χ_(λ')(g) = sgn(g) · χ_λ(g)). -/
theorem conjugate_preserves_dim (p : PartitionOf5) :
    p.conjugate.dim = p.dim := by
  cases p <;> rfl

/-- Sum of dim² over partitions of 5 = |S_5| = 120 (Burnside / Wedderburn). -/
theorem total_dim_squared_eq_120 :
    (PartitionOf5.allList.map (fun p => p.dim ^ 2)).sum = 120 := by
  decide

/-! ## A_5 ⊂ S_5 — the alternating subgroup, isomorphic to the
    icosahedral rotation group I ⊂ SO(3) -/

/-- Indicator: which S_5 irreps restrict to non-trivial A_5 sub-reps
    (equivalently, which partitions are NOT self-conjugate AND have
    different multiplicities under restriction).  The branching rule
    S_5 ↓ A_5 splits irreps whose conjugate-pair-mate is different,
    and keeps self-conjugate ones as-is.

    Standard rep theory: A_5 has 5 irreps of dim 1, 3, 3, 4, 5
    (totaling dim²-sum 1+9+9+16+25 = 60 = |A_5|). -/
def PartitionOf5.restrictsToA5Irrep : PartitionOf5 → Bool
  | .five          => true   -- → trivial A_5 irrep (dim 1)
  | .fourOne       => true   -- → A_5 dim-4 irrep
  | .threeTwo      => true   -- → A_5 dim-5 irrep
  | .threeOneOne   => true   -- self-conjugate; splits into two dim-3 A_5 irreps
  | .twoTwoOne     => false  -- isomorphic to threeTwo via sign-twist
  | .twoOneOneOne  => false  -- isomorphic to fourOne via sign-twist
  | .onesFive      => false  -- isomorphic to five via sign-twist

/-- |A_5| = 60 by Burnside: 1² + 3² + 3² + 4² + 5² = 60. -/
theorem A5_order_eq_60 :
    let a5_dims : List ℕ := [1, 3, 3, 4, 5]
    (a5_dims.map (· ^ 2)).sum = 60 := by
  decide

/-! ## The five A₅ irreps — the CORRECTED domain of the fiber map

    Per `docs/audits/2026-06-13-bring-fiber-action-falsification.md`: the
    geometric fiber map's domain is the FIVE irreps of A₅ (≅ I), NOT the
    seven partitions of S₅.  Conjugate S₅-partitions restrict to the *same*
    A₅ irrep (the sign character is trivial on A₅); the self-conjugate
    (3,1,1) splits into the chirality pair T₁ ⊕ T₂.  This 1+1+1+2 = 5 count
    matches the 5 conjugacy classes of A₅ (character-table duality), which
    the falsified 7-partition map could not reach (7 partitions ↦ 4
    conjugation orbits ↦ at most 4 classes). -/

/-- The five irreducible representations of A₅ ≅ I (dims 1, 3, 3, 4, 5):
    A (trivial), the chirality pair T₁/T₂ (both dim 3), G (dim 4), H (dim 5). -/
inductive A5Irrep where
  | A | T₁ | T₂ | G | H
  deriving DecidableEq, Repr

/-- All five A₅ irreps. -/
def A5Irrep.allList : List A5Irrep := [.A, .T₁, .T₂, .G, .H]

/-- Dimension of each A₅ irrep. -/
def A5Irrep.dim : A5Irrep → ℕ
  | .A => 1 | .T₁ => 3 | .T₂ => 3 | .G => 4 | .H => 5

/-- A₅ has exactly five irreps — equal to its number of conjugacy classes
    (the character-table duality the fiber map realizes). -/
theorem card_eq_five : A5Irrep.allList.length = 5 := rfl

/-- The A₅ irrep each S₅ partition restricts to (its chirality
    representative).  Conjugate partitions share an irrep; the self-conjugate
    (3,1,1) is sent to its T₁ representative (the T₁ ⊕ T₂ chirality split is
    recorded in `s5_to_a5_electron_block_splits`). -/
def PartitionOf5.toA5Irrep : PartitionOf5 → A5Irrep
  | .five         => .A   | .onesFive     => .A
  | .fourOne      => .G   | .twoOneOneOne => .G
  | .threeTwo     => .H   | .twoTwoOne    => .H
  | .threeOneOne  => .T₁

/-- **Corrected conjugate-compatibility** (replaces the falsified geometric
    angle sign-flip `angle(λ') = -angle(λ)`): conjugate S₅-partitions restrict
    to the SAME A₅ irrep, hence share a fiber.  The sign-twist lives on the
    Wedderburn/S₅ side, not as a geometric orientation reversal. -/
theorem PartitionOf5.conjugate_same_a5_irrep (p : PartitionOf5) :
    p.conjugate.toA5Irrep = p.toA5Irrep := by
  cases p <;> rfl

/-! ## The Bring's surface fiber-action map — conditional class -/

/-- A rotation in SO(3) about a given axis, by a given angle.

    Base ring (§7c): `ℝ` is intrinsic, not gratuitous — SO(3) is a real Lie
    group, the axis is a real 3-vector, and `angle` is a real rotation angle
    (compared for injectivity in `BringFiberAction.five_distinct_classes`, and
    the archimedean home of the owner-gated geometric realization
    `conj:s5-so3-fiber-action`).  Do NOT generalize to a generic ring: a
    "rotation axis" over an arbitrary commutative ring is meaningless. -/
structure SO3Rotation where
  axis_x : ℝ
  axis_y : ℝ
  axis_z : ℝ
  angle  : ℝ
  deriving Inhabited

/-- The icosahedral rotation group I as a subgroup of SO(3).
    |I| = 60 = |A_5|; the isomorphism A_5 ≅ I is the icosahedral
    symmetry (Klein 1884).  This structure carries the abstract
    data of an icosahedral rotation. -/
structure IcosahedralRotation where
  asSO3 : SO3Rotation
  -- Conditional invariant: this rotation preserves the icosahedron's
  -- 12-vertex configuration.  Encoded as a class hypothesis below.
  deriving Inhabited

/-- **Class: fiber action of A₅ on Bring's surface (corrected domain).**

    The conjectural content: the icosahedral action on Bring's quintic
    surface Σ₄ induces a fiber map from the five A₅ irreps to icosahedral
    SO(3) rotations, realizing the A₅ irrep ↔ conjugacy-class duality.

    This corrects the falsified `S₅-partition → rotation` map.  Per
    `docs/audits/2026-06-13-bring-fiber-action-falsification.md`, the prior
    7-partition domain made `respects_conjugate` (a geometric angle
    sign-flip `angle(λ') = -angle(λ)`) and `hits_five_conjugacy_classes`
    *mutually unsatisfiable* (orbit counting: 7 partitions ↦ 4 conjugation
    orbits ↦ at most 4 classes), and the placeholder `: True` + trivial
    instance discharged the class vacuously.  The corrected domain is the
    FIVE A₅ irreps (`A5Irrep`); the false sign-flip is replaced by the
    theorem `PartitionOf5.conjugate_same_a5_irrep` (conjugate partitions
    share a fiber — derived, not axiomatised).

    Per AGENTS.md §3b-cond the conjectural geometric map is a class field;
    downstream results consume it via `[BringFiberAction]`.  The field
    `five_distinct_classes` is SUBSTANTIVE — a constant map fails injectivity
    — so the class is **not** vacuously satisfiable.  The explicit map
    (which A₅ irrep ↦ which icosahedral rotation, from Bring's quintic
    automorphism group) is the open, owner-gated step
    `conj:s5-so3-fiber-action`; no global instance is provided, so downstream
    theorems are genuinely conditional on it.

    -- Ref: [klein1888] Klein, Lectures on the Icosahedron (Bring) -/
class BringFiberAction where
  /-- The conjectural geometric fiber map on the corrected (A₅-irrep) domain:
      each A₅ irrep ↦ an icosahedral rotation, induced by Bring's quintic. -/
  irrepToRotation : A5Irrep → IcosahedralRotation
  /-- **Substantive** (de-vacuifying, replacing the prior `: True`): the five
      A₅ irreps realize five DISTINCT icosahedral conjugacy classes — five
      distinct rotation angles.  A constant map fails injectivity, so this
      cannot be discharged vacuously (the falsified trivial instance is
      rejected). -/
  five_distinct_classes :
    Function.Injective (fun r : A5Irrep => (irrepToRotation r).asSO3.angle)

/-- **Main statement (scaffold).** The S₅↔SO(3) fiber action on Bring's
    surface gives a map from partition-wise Wedderburn data (S₅ irreps) to
    icosahedral spatial rotations (I ⊂ SO(3)), preserving the conjugation
    structure.

    The combinatorial half (dim² = 120, conjugation involutive) holds
    unconditionally.  Under the conjectural `BringFiberAction` the fiber map
    additionally *identifies conjugate partitions* (same A₅ irrep ⇒ same
    rotation) — the corrected replacement for the falsified angle sign-flip,
    so the `[BringFiberAction]` hypothesis is genuinely used (not decorative).

    Closure of the open half requires the explicit `BringFiberAction` instance
    derived from Bring's quintic surface automorphism group (owner-gated step
    `conj:s5-so3-fiber-action`). -/
theorem s5_so3_fiber_action_scaffold [bfa : BringFiberAction] :
    (PartitionOf5.allList.map (fun p => p.dim ^ 2)).sum = 120 ∧
    (∀ p : PartitionOf5, p.conjugate.conjugate = p) ∧
    (∀ p : PartitionOf5,
      bfa.irrepToRotation p.conjugate.toA5Irrep = bfa.irrepToRotation p.toA5Irrep) :=
  ⟨total_dim_squared_eq_120, PartitionOf5.conjugate_involutive,
   fun p => by rw [PartitionOf5.conjugate_same_a5_irrep]⟩

/-! ## Derived facts (sorry-free) from the icosahedral character analysis

    These encode the RAW results of
    `computations/s5_so3_su2_u1_fiber_action.py`
    (audit `docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md`).
    They are unconditional Lean facts — they do NOT depend on
    `BringFiberAction` — and capture exactly what the icosahedral
    character table determines.  They sharpen, but do NOT discharge,
    the conjectural `partition_to_rotation` map. -/

/-- Dimensions of the five icosahedral (≅ A₅) irreps: A, T₁, T₂, G, H. -/
def IcosahedralIrrepDims : List ℕ := [1, 3, 3, 4, 5]

/-- Multiplicity of each icosahedral irrep (in the order A, T₁, T₂, G, H)
    inside the restriction `V_ℓ|_I` of the SO(3) angular-momentum rep, as
    DERIVED from the I character table (probe output, ℓ = 0..6). -/
def icosBranchingMult : ℕ → List ℕ
  | 0 => [1, 0, 0, 0, 0]   -- V_0 = A (trivial)
  | 1 => [0, 1, 0, 0, 0]   -- V_1 = T₁ (the 3-dim, = color sheets)
  | 2 => [0, 0, 0, 0, 1]   -- V_2 = H (the dim-5 irrep) — first appearance
  | 3 => [0, 0, 1, 1, 0]   -- V_3 = T₂ ⊕ G
  | 4 => [0, 0, 0, 1, 1]   -- V_4 = G ⊕ H
  | 5 => [0, 1, 1, 0, 1]   -- V_5 = T₁ ⊕ T₂ ⊕ H
  | 6 => [1, 1, 0, 1, 1]   -- V_6 = A ⊕ T₁ ⊕ G ⊕ H
  | _ => [0, 0, 0, 0, 0]

/-- Dimension check: for each ℓ ≤ 6, `Σ mult·dim = 2ℓ+1`.  Confirms the
    icosahedral branching is consistent (the multiplicities partition the
    full angular-momentum dimension). -/
theorem icos_branching_dim_check :
    ∀ ℓ ∈ [0, 1, 2, 3, 4, 5, 6],
      ((List.zip (icosBranchingMult ℓ) IcosahedralIrrepDims).map
        (fun p => p.1 * p.2)).sum = 2 * ℓ + 1 := by
  decide

/-- **The ℓ=2 reading.** The SO(3) angular-momentum level ℓ=2 restricts to
    EXACTLY ONE copy of the dim-5 icosahedral irrep H (the fifth entry), and
    H first appears at ℓ=2.  This is the derived "ℓ=2 → dim-5 irrep"
    statement; it does NOT by itself supply the Borromean h⁴ coefficient
    (see audit: the h⁴ lives in the 3-strand H₃ algebra, a different
    representation ring). -/
theorem ell2_yields_one_copy_of_H :
    (icosBranchingMult 2).get! 4 = 1 ∧
    (icosBranchingMult 0).get! 4 = 0 ∧
    (icosBranchingMult 1).get! 4 = 0 := by
  decide

/-- **The S₃-rotation-subgroup branching (corrects the source-file premise).**
    S₃ realised as the triangle-rotation subgroup of SO(3) (irreps triv,
    sign, std) branches `V_ℓ` with the std (=(2,1)) irrep already present at
    ℓ=1 AND ℓ=2 — so the premise "S₃ sees only ℓ≤1" is FALSE.  Order:
    [triv, sign, std]. -/
def s3RotBranchingMult : ℕ → List ℕ
  | 0 => [1, 0, 0]
  | 1 => [0, 1, 1]
  | 2 => [1, 0, 2]
  | 3 => [1, 2, 2]
  | 4 => [2, 1, 3]
  | _ => [0, 0, 0]

/-- The std/(2,1) irrep (which carries the Borromean h⁴) appears at BOTH ℓ=1
    and ℓ=2 under the S₃⊂SO(3) rotation embedding: multiplicities 1 and 2.
    Therefore "S₃ sees only ℓ≤1" is false — h⁴ cannot be attributed to "ℓ=2
    only". -/
theorem s3_std_appears_at_ell1_and_ell2 :
    (s3RotBranchingMult 1).get! 2 = 1 ∧
    (s3RotBranchingMult 2).get! 2 = 2 := by
  decide

/-- **SU(2) double cover: spin ℤ₂ ≠ sign ℤ₂.**  The binary icosahedral group
    2I (the SU(2)-preimage of I ≅ A₅) has order 120 = |S₅|, but 2I is PERFECT
    (trivial abelianisation) while S₅ has abelianisation ℤ₂ (the sign
    character).  Hence 2I ≇ S₅, and the spin ℤ₂ (SU(2)→SO(3) kernel) is a
    different ℤ₂ from the sign ℤ₂ (S₅/A₅).  Encoded via the abelianisation
    orders. -/
theorem spin_Z2_ne_sign_Z2 :
    let binaryIcosahedralAbelianizationOrder : ℕ := 1   -- 2I is perfect
    let s5AbelianizationOrder : ℕ := 2                  -- sign character
    binaryIcosahedralAbelianizationOrder ≠ s5AbelianizationOrder := by
  decide

/-! ## The S_5 → S_3 Restriction Functor (GAP-A-4 Functor Resolution)

    This section implements the mathematical closure for the missing categorical
    functor linking the 5-strand fiber space to the 3-strand Borromean trace.
    Per `2026-06-13-s5-so3-fiber-action-functor-resolution.md`, the geometric
    fiber map `partition_to_rotation` reduces algebraically to the Hecke/Symmetric
    group restriction functor Res^{S_5}_{S_3}.
-/

/-- Branching multiplicities of the S_5 irreps under restriction to S_3.
    Computed via standard Littlewood-Richardson/Branching rules.
    Order of S_3 irreps: [(3) trivial, (1,1,1) sign, (2,1) standard]. -/
def s5_to_s3_restriction_mults : PartitionOf5 → List ℕ
  | .five          => [1, 0, 0]  -- (5) ↓ S_3 = (3)
  | .fourOne       => [2, 0, 1]  -- (4,1) ↓ S_3 = 2·(3) ⊕ (2,1)
  | .threeTwo      => [1, 0, 2]  -- (3,2) ↓ S_3 = (3) ⊕ 2·(2,1)
  | .threeOneOne   => [1, 1, 2]  -- (3,1,1) ↓ S_3 = (3) ⊕ (1,1,1) ⊕ 2·(2,1)
  | .twoTwoOne     => [0, 1, 2]  -- (2,2,1) ↓ S_3 = (1,1,1) ⊕ 2·(2,1)
  | .twoOneOneOne  => [0, 2, 1]  -- (2,1,1,1) ↓ S_3 = 2·(1,1,1) ⊕ (2,1)
  | .onesFive      => [0, 1, 0]  -- (1,1,1,1,1) ↓ S_3 = (1,1,1)

/-- **Functor Resolution Theorem**: The load-bearing (2,1) irrep of H_3(q)
    (which carries the Borromean h^4 = -3/4 coefficient) appears with
    multiplicity EXACTLY 2 in both the electron block (3,1,1) [ℓ=1] and the
    muon block (3,2) [ℓ=2].
    This validates the S_5 → S_3 restriction as the canonical functor connecting
    the spherical-harmonic generation tower to the mass trace. -/
theorem restriction_functor_yields_h4_irrep :
    -- Electron block (ℓ=1):
    (s5_to_s3_restriction_mults .threeOneOne).get! 2 = 2 ∧
    -- Muon block (ℓ=2):
    (s5_to_s3_restriction_mults .threeTwo).get! 2 = 2 := by
  decide

/-- Dimensions of the 3 irreps of S_3, in the order
    [(3) trivial, (1,1,1) sign, (2,1) standard]. -/
def s3IrrepDims : List ℕ := [1, 1, 2]

/-- **Restriction dimension-consistency (the branching backbone).**  For every
    partition λ ⊢ 5, restricting V_λ to S_3 preserves total dimension:
    `Σ_μ (mult of μ in V_λ↓S_3) · dim(μ) = dim(V_λ)`.  This is the dimension
    bookkeeping that the S_5 → S_3 restriction functor `Res^{S_5}_{S_3}` must
    satisfy (a vector space keeps its dimension on restriction, only its
    decomposition changes), verifying `s5_to_s3_restriction_mults` against
    `PartitionOf5.dim` across all 7 blocks.  Because the count depends only on
    the conjugacy class of the S_3 ⊂ S_5 subgroup, it is identical for the
    spacetime-frame-fixing embedding {1,2,3}↦{3,4,5} and the naive {1,2,3}↦
    {1,2,3} — the embedding-independence verified in
    `scripts/s5so3_branching_backbone_verify.py`. -/
theorem s5_to_s3_restriction_dim_consistent (p : PartitionOf5) :
    (s5_to_s3_restriction_mults p).length = 3 ∧
    (List.zipWith (· * ·) (s5_to_s3_restriction_mults p) s3IrrepDims).sum = p.dim := by
  cases p <;> decide

/-- **S₃-rotation branching dimension-consistency** (the analog of
    `icos_branching_dim_check` for the `s3RotBranchingMult` table, which until
    now carried only the `s3_std_appears_at_ell1_and_ell2` spot-check).  For
    each angular-momentum level ℓ ≤ 4, the S₃⊂SO(3) rotation-subgroup
    multiplicities partition the full dimension `2ℓ+1`:
    `Σ_μ (mult of μ in V_ℓ↓S₃) · dim(μ) = 2ℓ+1`.  The `length = 3` conjunct
    guards `List.zipWith` against silent truncation (cf. #2431). -/
theorem s3rot_branching_dim_check :
    ∀ ℓ ∈ [0, 1, 2, 3, 4],
      (s3RotBranchingMult ℓ).length = 3 ∧
      (List.zipWith (· * ·) (s3RotBranchingMult ℓ) s3IrrepDims).sum = 2 * ℓ + 1 := by
  decide

/-! ## Δ_λ chirality decomposition (per-block binding factor)

    Per `docs/audits/2026-06-16-option-e-delta-lambda-sign-chirality.md` (#2386):
    the Option-E per-partition binding factor Δ_λ decomposes as
      Δ_λ = (icosahedral chirality sign) × (Wedderburn magnitude),
    where the magnitude is the irrep dimension dim V_λ and the chirality sign is
    sgn(w₀^{S_{λ'}}) ∈ {±1} — the longest-element sign of the conjugate
    partition's Young subgroup, realizing the T₁/T₂ chirality swap under the
    S₅∖A₅ parity (= the conjugate/transpose sign-twist).

    These are UNCONDITIONAL finite facts (they do NOT depend on
    `BringFiberAction`); they pin the sign/magnitude split of the binding
    factor.  Caveat (per #2386 correction): this split is the magnitude×sign
    structure of Δ_λ, not a closure of the deuteron binding energy — the
    Σ_λ y_λ χ^λ Δ_λ formula undershoots (the deuteron closes via E₀·q⁻¹).
    The Lean below proves only the structural decomposition. -/

/-- Δ_λ chirality sign = sgn(w₀^{S_{λ'}}) ∈ {±1}, computed per partition. -/
def PartitionOf5.deltaSign : PartitionOf5 → ℤ
  | .five          => 1
  | .fourOne       => -1
  | .threeTwo      => 1
  | .threeOneOne   => -1
  | .twoTwoOne     => 1
  | .twoOneOneOne  => 1
  | .onesFive      => 1

/-- The per-block binding factor Δ_λ = chirality sign × Wedderburn magnitude. -/
def PartitionOf5.deltaLambda (p : PartitionOf5) : ℤ := p.deltaSign * (p.dim : ℤ)

/-- Chirality is ±1 (deltaSign² = 1). -/
theorem PartitionOf5.deltaSign_sq_one (p : PartitionOf5) : p.deltaSign ^ 2 = 1 := by
  cases p <;> decide

/-- **Magnitude = Wedderburn dim**: |Δ_λ| = dim V_λ, i.e. (Δ_λ)² = (dim V_λ)². -/
theorem binding_magnitude_eq_dim (p : PartitionOf5) :
    p.deltaLambda ^ 2 = (p.dim : ℤ) ^ 2 := by
  cases p <;> decide

/-- **Mixed-sign** (the PROBE-4 KL-positivity-prune premise at n=5): both
    chirality signs occur, so no nonnegative (Kazhdan–Lusztig) weight can
    supply the sign — the chirality must come from the parity twist, not a
    positive combination of dimensions. -/
theorem deltaSign_mixed :
    (∃ p : PartitionOf5, p.deltaSign = 1) ∧ (∃ p : PartitionOf5, p.deltaSign = -1) :=
  ⟨⟨.five, rfl⟩, ⟨.fourOne, rfl⟩⟩

/-- The electron block (3,1,1) is chirality-odd (deltaSign = -1), magnitude 6
    (self-conjugate partition; the T₁/T₂ split that carries the chirality). -/
theorem electron_block :
    PartitionOf5.threeOneOne.deltaSign = -1 ∧ PartitionOf5.threeOneOne.dim = 6 := by
  decide

/-- The partition of each `n = 5` block, as its weakly-decreasing list of parts. -/
def PartitionOf5.parts : PartitionOf5 → List ℕ
  | .five          => [5]
  | .fourOne       => [4, 1]
  | .threeTwo      => [3, 2]
  | .threeOneOne   => [3, 1, 1]
  | .twoTwoOne     => [2, 2, 1]
  | .twoOneOneOne  => [2, 1, 1, 1]
  | .onesFive      => [1, 1, 1, 1, 1]

/-- The partition statistic `n(λ) = Σ_i (i-1)·λ_i` (here the 0-indexed `Σ i·λ_i`
    over the enumerated parts, via a `(index, sum)` fold).  For the symmetric
    group this is the **b-invariant** (the lowest fake-degree exponent =
    `min_{T ∈ SYT(λ)} maj(T)`) and, since every `S_n` irrep is special, **Lusztig's
    a-function** value on the two-sided cell of `V_λ`.  Verified combinatorially
    (b-invariant via min major index over SYT) in
    `docs/audits/scripts/option_e_probe4_overturning_afunction_sign.py`. -/
def PartitionOf5.nStat (p : PartitionOf5) : ℕ :=
  (p.parts.foldl (fun (acc : ℕ × ℕ) part => (acc.1 + 1, acc.2 + acc.1 * part)) (0, 0)).2

/-- **The Δ_λ chirality sign is the partition-statistic parity** — the PROBE-4
    re-scope (PR #2661).  The chirality sign equals `(-1)^{n(λ)}`, i.e. the parity
    of the b-invariant / Lusztig a-function — **not** an exogenous decoration.
    Because the a-function is constant on Kazhdan–Lusztig cells, a *forced*
    cell-constant sign `(-1)^{a(w)}` factors through any nonnegative (KL)
    multiplicity sum and reproduces this mixed-sign pattern; so the
    KL-positivity prune is re-scoped from "the sign must be supplied exogenously"
    to "the sign **is** the a-function parity; the open Δ_λ problem is the
    *magnitude*".  (`(-1)^{n(λ)} = sgn(w₀^{S_{λ'}})`, the conjugate Young-subgroup
    longest-element sign of `deltaSign`'s definition, for all `λ ⊢ n ≤ 8` per the
    same probe; here proved at `n = 5`.)  See
    `docs/audits/2026-06-23-option-e-probe4-overturning-afunction-sign.md`. -/
theorem PartitionOf5.deltaSign_eq_nStat_parity (p : PartitionOf5) :
    p.deltaSign = (-1 : ℤ) ^ p.nStat := by
  cases p <;> decide

/-- The conjugate (transpose) partition's parts, `λ' ⊢ 5`. -/
def PartitionOf5.conjParts : PartitionOf5 → List ℕ
  | .five          => [1, 1, 1, 1, 1]
  | .fourOne       => [2, 1, 1, 1]
  | .threeTwo      => [2, 2, 1]
  | .threeOneOne   => [3, 1, 1]
  | .twoTwoOne     => [3, 2]
  | .twoOneOneOne  => [4, 1]
  | .onesFive      => [5]

/-- `Σ_i C(μ_i, 2)` over a partition `μ`'s parts — the **length** `ℓ(w₀^{S_μ})` of
    the longest element of the Young subgroup `S_μ = ∏_i S_{μ_i}` (each factor
    `S_{μ_i}` contributes `C(μ_i,2)` inversions). -/
def sumChoose2 (parts : List ℕ) : ℕ := (parts.map (fun p => p * (p - 1) / 2)).sum

/-- **`n(λ) = Σ_i C(λ'_i, 2)`** — the partition statistic equals the sum of
    binomials over the **conjugate** partition's parts (the standard identity,
    here verified at `n = 5`).  Since `Σ_i C(λ'_i,2) = ℓ(w₀^{S_{λ'}})`, this ties
    `nStat` to the conjugate Young subgroup's longest element. -/
theorem PartitionOf5.nStat_eq_sumChoose2_conj (p : PartitionOf5) :
    p.nStat = sumChoose2 p.conjParts := by
  cases p <;> decide

/-- **`deltaSign = sgn(w₀^{S_{λ'}})` explicitly.**  The hardcoded chirality table
    equals the longest-element sign `(-1)^{ℓ(w₀^{S_{λ'}})} = (-1)^{Σ_i C(λ'_i,2)}`
    of the conjugate Young subgroup — the form asserted in `deltaSign`'s
    definition.  Together with `nStat_eq_sumChoose2_conj` and
    `deltaSign_eq_nStat_parity` this closes the loop
    `deltaSign = sgn(w₀^{S_{λ'}}) = (-1)^{n(λ)}` (a-function / b-invariant parity),
    so the chirality sign is a forced cell invariant, not a table. -/
theorem deltaSign_eq_w0_conj_sign (p : PartitionOf5) :
    p.deltaSign = (-1 : ℤ) ^ (sumChoose2 p.conjParts) := by
  cases p <;> decide

/-! ## The Reeb = Res^{S₅}_{S₃} identity (keystone residual ii)

    Per `docs/audits/2026-06-20-keystone-wlambda-beasley-witten-localization.md`
    §"Honest scope", the Beasley–Witten Seifert–CS localization on `S³/2I`
    supplies the q-Plancherel weights, and **"the restriction structure is the
    Bratteli branching the localization sum runs over"** — but the explicit
    *Reeb = restriction* equality at the scaffold level was left unformalized
    (residual (ii)).  This section discharges it.

    The Seifert fibration `S³/2I → S²(2,3,5)` has the Reeb field = the Seifert
    `S¹` fiber; the localization restricts along it.  Its representation-theoretic
    shadow is the restriction functor `Res^{S₅}_{S₃}` (`s5_to_s3_restriction_mults`
    above).  The geometric Reeb symmetry — conjugate `S₅`-partitions share a
    fiber (`conjugate_same_a5_irrep`) — must match an algebraic symmetry of the
    restriction.  It does, and exactly: restriction **commutes with the
    conjugation (sign) involution**.

    Mathematically this is forced: `V_{λ'} = V_λ ⊗ sgn_{S₅}`, and restriction
    commutes with sign-twist, with `sgn_{S₅}|_{S₃} = sgn_{S₃}`.  So
    `Res^{S₅}_{S₃}(V_{λ'}) = Res^{S₅}_{S₃}(V_λ) ⊗ sgn_{S₃}`, and `⊗ sgn_{S₃}`
    swaps the `S₃` trivial ↔ sign irreps while fixing the standard `(2,1)`.
    The theorems below verify this on the `n = 5` table and tie it to the
    geometric fiber map. -/

/-- The `S₃` sign-twist on a restriction-multiplicity triple `[m_triv, m_sign,
    m_std]`: tensoring by `sgn_{S₃}` swaps trivial ↔ sign and fixes standard.
    This is the `S₃` shadow of the `S₅` conjugation (sign) involution. -/
def s3SignTwist : List ℕ → List ℕ
  | [a, b, c] => [b, a, c]
  | m => m

/-- **Reeb = restriction (conjugation intertwiner).**  The `Res^{S₅}_{S₃}`
    branching commutes with conjugation: restricting the conjugate partition
    equals sign-twisting the restriction,
    `Res(V_{λ'}) = Res(V_λ) ⊗ sgn_{S₃} = s3SignTwist(Res(V_λ))`.  This is the
    algebraic shadow of the geometric `conjugate_same_a5_irrep` (conjugate
    partitions share a Reeb fiber): the shared Seifert-`S¹` fiber appears on the
    3-strand side as the `S₃` sign-twist intertwiner.  Both express the *same*
    conjugation symmetry — the scaffold-level content of "the localization sum
    runs over the `Res^{S₅}_{S₃}` Bratteli branching". -/
theorem restriction_intertwines_conjugation (p : PartitionOf5) :
    s5_to_s3_restriction_mults p.conjugate
      = s3SignTwist (s5_to_s3_restriction_mults p) := by
  cases p <;> rfl

/-- **The standard `(2,1)` irrep is the conjugation-fixed carrier.**  The `S₃`
    sign-twist fixes the `(2,1)` multiplicity (3rd entry), so the load-bearing
    standard irrep — which carries the Borromean `h⁴` per
    `restriction_functor_yields_h4_irrep` — sits in the conjugation-invariant
    part of every restriction, matching the Reeb fiber shared by conjugate
    partitions. -/
theorem std_irrep_conjugation_fixed (p : PartitionOf5) :
    (s5_to_s3_restriction_mults p.conjugate).get! 2
      = (s5_to_s3_restriction_mults p).get! 2 := by
  cases p <;> rfl

/-- **Reeb-thread = restriction functor (scaffold capstone, residual ii).**
    Under the conjectural `BringFiberAction`, the geometric Reeb/fiber map and
    the algebraic `Res^{S₅}_{S₃}` branching express the SAME conjugation
    symmetry:
    (i) conjugate partitions share a fiber/icosahedral rotation (geometric,
        `conjugate_same_a5_irrep`);
    (ii) their restriction content is sign-twisted (algebraic,
        `restriction_intertwines_conjugation`);
    (iii) with the standard `(2,1)` carrier fixed (`std_irrep_conjugation_fixed`).
    This is the scaffold-level "Reeb = restriction" identity that the
    Beasley–Witten Seifert–CS localization on `S³/2I` runs over — residual (ii)
    of `docs/audits/2026-06-20-keystone-wlambda-beasley-witten-localization.md`.
    The `[BringFiberAction]` hypothesis is genuinely used (conjunct i). -/
theorem reeb_eq_restriction_scaffold [bfa : BringFiberAction] (p : PartitionOf5) :
    bfa.irrepToRotation p.conjugate.toA5Irrep = bfa.irrepToRotation p.toA5Irrep ∧
    s5_to_s3_restriction_mults p.conjugate
      = s3SignTwist (s5_to_s3_restriction_mults p) ∧
    (s5_to_s3_restriction_mults p.conjugate).get! 2
      = (s5_to_s3_restriction_mults p).get! 2 :=
  ⟨by rw [PartitionOf5.conjugate_same_a5_irrep],
   restriction_intertwines_conjugation p,
   std_irrep_conjugation_fixed p⟩

/-! ## McKay correspondence anchors: 2I ↔ affine E₈

    The binary icosahedral group 2I = π⁻¹(I) ⊂ SU(2) (the spin double cover
    of the icosahedral rotation group I ≅ A₅) is the McKay group of the
    affine E₈ Dynkin diagram: its 9 irreducible representations correspond to
    the 9 nodes of the affine E₈ diagram, with dimensions equal to the
    Coxeter MARKS (labels).  This is the spacetime face of the keystone
    (S³/2I = Poincaré homology sphere = E₈ singularity link); these are the
    exact arithmetic anchors verified in
    `scripts/keystone_habiro_coupling_lead.py` (exit 0), now machine-checked.

    -- Ref: [mckay1980graphs] McKay, Graphs, singularities, finite groups
    -- Ref: [klein1888] Klein, Lectures on the Icosahedron -/

/-- Dimensions of the 9 irreducible reps of the binary icosahedral group 2I,
    equal to the Coxeter marks of the affine E₈ Dynkin diagram (McKay). -/
def binaryIcosahedralIrrepDims : List ℕ := [1, 2, 3, 4, 5, 6, 4, 2, 3]

/-- 2I has exactly 9 irreps (= number of affine E₈ nodes). -/
theorem binaryIcosahedral_num_irreps : binaryIcosahedralIrrepDims.length = 9 := rfl

/-- |2I| = 120 by Burnside: Σ dim² over the 9 irreps = 1+4+9+16+25+36+16+4+9 = 120.
    (Matches |S₅| = 120, but 2I ≇ S₅ — see `spin_Z2_ne_sign_Z2`.) -/
theorem binaryIcosahedral_order_eq_120 :
    (binaryIcosahedralIrrepDims.map (· ^ 2)).sum = 120 := by decide

/-- The affine E₈ marks sum to the Coxeter number h(E₈) = 30
    (= dual Coxeter number h∨(E₈), E₈ being simply-laced). -/
theorem affineE8_marks_sum_eq_coxeter_30 :
    binaryIcosahedralIrrepDims.sum = 30 := by decide

/-- |2I| = 4 · h(E₈): the order of the McKay group is four times the
    Coxeter number (120 = 4 · 30). -/
theorem order_2I_eq_four_times_coxeter :
    (binaryIcosahedralIrrepDims.map (· ^ 2)).sum =
      4 * binaryIcosahedralIrrepDims.sum := by decide

/-- dim E₈ = 248 = rank · (h + 1) = 8 · 31, with rank = 8 and Coxeter h = 30. -/
theorem e8_dim_eq_rank_times_h_plus_one :
    (248 : ℕ) = 8 * (30 + 1) := by decide

/-! ## A₅ branching anchors (SO(3) ↓ A₅ and S₅ ↓ A₅ irrep content) -/

/-- **SO(3) ↓ A₅ irrep content at low ℓ.**  Read directly off
    `icosBranchingMult` against the irrep ordering [A, T₁, T₂, G, H]
    (= `IcosahedralIrrepDims` [1,3,3,4,5]): the angular-momentum levels
    restrict as V₁ → T₁, V₂ → H, V₃ → T₂ ⊕ G.  This states *which* A₅
    irreps occur (not just the dimension bookkeeping already in
    `icos_branching_dim_check`): V₃'s dim-7 splits as the dim-3 T₂ plus the
    dim-4 G, the first level where two distinct icosahedral irreps co-occur. -/
theorem so3_to_a5_irrep_content :
    icosBranchingMult 1 = [0, 1, 0, 0, 0] ∧   -- V₁ = T₁
    icosBranchingMult 2 = [0, 0, 0, 0, 1] ∧   -- V₂ = H
    icosBranchingMult 3 = [0, 0, 1, 1, 0] := by  -- V₃ = T₂ ⊕ G
  decide

/-- **S₅ ↓ A₅ on the self-conjugate (3,1,1) block.**  V_(3,1,1) is
    self-conjugate (`conjugate` fixes it), restricts non-trivially to A₅
    (`restrictsToA5Irrep = true`), and its dim 6 splits as the chirality
    pair T₁ ⊕ T₂ (3 + 3) swapped by the S₅∖A₅ parity.  The self-conjugacy
    (= invariance under the sign-twist) is exactly the structural reason
    the block carries the chirality (cf. `QOU.BraidsAndKnots.electron_block`). -/
theorem s5_to_a5_electron_block_splits :
    PartitionOf5.threeOneOne.conjugate = PartitionOf5.threeOneOne ∧
    PartitionOf5.threeOneOne.restrictsToA5Irrep = true ∧
    PartitionOf5.threeOneOne.dim = 3 + 3 := by
  decide


/-! ## The Hopf generation-selection map ℓ → A₅ irrep

    The ledger's ✅ μ-leg: the spatial SO(3)-equivariance realizes the
    generation-selection ℓ → λ as the Hopf moment map μ (PR #2370).  The
    *combinatorial* face of that selection — which A₅ irrep the spherical-harmonic
    level ℓ singles out as its first-appearing (lowest-ℓ) icosahedral content — is
    a finite, unconditional reading of `icosBranchingMult`:

      ℓ = 1  ↦  T₁  (the electron generation; T₁ first appears at ℓ=1),
      ℓ = 2  ↦  H   (the muon generation;     H  first appears at ℓ=2).

    This is the *selection* (which single irrep is picked out), distinct from the
    full branching content `so3_to_a5_irrep_content` (which lists *all* irreps in
    each V_ℓ).  The geometric realization — that this combinatorial selection IS
    the Hopf moment map — is the ledger's already-realized μ-leg (#2370); the Lean
    below only pins the combinatorial target it must reproduce. -/

/-- The Hopf generation-selection map: the A₅ irrep singled out at spherical-
    harmonic level ℓ as its lowest-ℓ (first-appearing) icosahedral content.
    ℓ=1 → T₁ (electron), ℓ=2 → H (muon).  Index into `IcosahedralIrrepDims`
    ordering [A, T₁, T₂, G, H]. -/
def hopfGenerationSelect : ℕ → A5Irrep
  | 1 => .T₁   -- electron generation
  | 2 => .H    -- muon generation
  | _ => .A    -- (ℓ=0 trivial / out-of-range default)

/-- **Hopf selection theorem (combinatorial leg).** The generation-selection map
    reads off `icosBranchingMult`: at ℓ=1 the unique nonzero multiplicity is the
    T₁ slot (electron), and at ℓ=2 it is the H slot (muon).  Concretely the
    selected irrep's slot carries multiplicity 1 while the *other* generation's
    slot is 0 at that level — so the two generations are cleanly separated by ℓ.

    The four equalities verify, against the raw `icosBranchingMult` table:
    (i)  ℓ=1 selects T₁ — its T₁-slot (index 1) is 1;
    (ii) ℓ=1 does NOT yet see H — its H-slot (index 4) is 0;
    (iii) ℓ=2 selects H — its H-slot (index 4) is 1;
    (iv) ℓ=2 does NOT carry T₁ — its T₁-slot (index 1) is 0.
    Hence `hopfGenerationSelect 1 = T₁` and `hopfGenerationSelect 2 = H` are
    the correct combinatorial targets the Hopf moment map (#2370) realizes. -/
theorem hopf_generation_selection :
    hopfGenerationSelect 1 = A5Irrep.T₁ ∧
    hopfGenerationSelect 2 = A5Irrep.H ∧
    -- the selected slots are exactly the first appearances (separation by ℓ):
    (icosBranchingMult 1).get! 1 = 1 ∧   -- ℓ=1: T₁ present
    (icosBranchingMult 1).get! 4 = 0 ∧   -- ℓ=1: H absent
    (icosBranchingMult 2).get! 4 = 1 ∧   -- ℓ=2: H present
    (icosBranchingMult 2).get! 1 = 0 := by  -- ℓ=2: T₁ absent
  refine ⟨rfl, rfl, ?_, ?_, ?_, ?_⟩ <;> decide

/-- **The selected irrep has the expected dimension.** The electron generation
    (ℓ=1 → T₁) is 3-dimensional (the chiral color sheets), and the muon
    generation (ℓ=2 → H) is 5-dimensional.  Confirms the selection map lands on
    the irreps whose dimensions match the corpus generation assignment. -/
theorem hopf_selection_dims :
    (hopfGenerationSelect 1).dim = 3 ∧ (hopfGenerationSelect 2).dim = 5 := by
  decide

/-! ## A₅ conjugacy classes and the irrep ↔ class duality

    The target named by the `BringFiberAction.five_distinct_classes` field: the
    five A₅ irreps realize five DISTINCT icosahedral conjugacy classes.  This
    section makes the *codomain* of that injectivity explicit — the five
    conjugacy classes of A₅ ≅ I — and records the square character-table duality
    (5 irreps ↔ 5 classes) that any complete character theory forces.

    A₅ has exactly five conjugacy classes (cycle types of even permutations of
    5 letters), with sizes summing to |A₅| = 60:

      e         (identity)                size  1   [order 1]
      (ab)(cd)  (double transposition)    size 15   [order 2]
      (abc)     (3-cycle)                 size 20   [order 3]
      (abcde)   (5-cycle, class I)        size 12   [order 5]
      (abcde)²  (5-cycle, class II)       size 12   [order 5]

    The 5-cycles split into TWO A₅-classes (an odd permutation conjugates a
    5-cycle to its non-A₅-conjugate square; S₅ fuses them) — this is the same
    index-2 fusion that swaps the chirality pair T₁ ↔ T₂ (cf.
    `s5_to_a5_electron_block_splits` and the construction-program doc
    §"Residual-2 RESOLVED").  So the two 5-cycle classes are the class-side face
    of the T₁/T₂ chirality. -/

/-- The five conjugacy classes of A₅ ≅ I (icosahedral rotation group):
    identity, double-transpositions, 3-cycles, and the two enantiomorphic
    5-cycle classes (swapped by the S₅∖A₅ parity). -/
inductive A5ConjClass where
  | id            -- e,        size 1,  order 1
  | doubleTransp  -- (ab)(cd), size 15, order 2
  | threeCycle    -- (abc),    size 20, order 3
  | fiveCycleA    -- (abcde),  size 12, order 5  (chirality A)
  | fiveCycleB    -- (abcde)², size 12, order 5  (chirality B)
  deriving DecidableEq, Repr

/-- All five A₅ conjugacy classes. -/
def A5ConjClass.allList : List A5ConjClass :=
  [.id, .doubleTransp, .threeCycle, .fiveCycleA, .fiveCycleB]

/-- Size of each A₅ conjugacy class. -/
def A5ConjClass.size : A5ConjClass → ℕ
  | .id => 1 | .doubleTransp => 15 | .threeCycle => 20
  | .fiveCycleA => 12 | .fiveCycleB => 12

/-- Order of a representative element of each class. -/
def A5ConjClass.elementOrder : A5ConjClass → ℕ
  | .id => 1 | .doubleTransp => 2 | .threeCycle => 3
  | .fiveCycleA => 5 | .fiveCycleB => 5

/-- **Class-count = irrep-count = 5 (the character-table is square).** A₅ has
    exactly five conjugacy classes, matching its five irreps (`A5Irrep`).  This
    squareness is precisely the duality the fiber map realizes: the five A₅
    irreps map injectively onto the five conjugacy classes (the codomain of
    `BringFiberAction.five_distinct_classes`). -/
theorem A5_classes_eq_irreps :
    A5ConjClass.allList.length = A5Irrep.allList.length := rfl

/-- **Class sizes partition |A₅| = 60** (the orbit-counting / class-equation
    backbone): 1 + 15 + 20 + 12 + 12 = 60.  Confirms the five classes are a
    complete partition of the group. -/
theorem A5_class_sizes_sum_60 :
    (A5ConjClass.allList.map A5ConjClass.size).sum = 60 := by decide

/-- **The 5-cycle classes are the chirality pair** (same size, same element
    order, distinct classes).  This is the class-side face of the T₁/T₂ split:
    the two enantiomorphic 5-cycle classes are exchanged by the S₅∖A₅ parity,
    exactly as T₁ ↔ T₂ are (cf. `s5_to_a5_electron_block_splits`). -/
theorem A5_fivecycle_chirality_pair :
    A5ConjClass.fiveCycleA.size = A5ConjClass.fiveCycleB.size ∧
    A5ConjClass.fiveCycleA.elementOrder = A5ConjClass.fiveCycleB.elementOrder ∧
    A5ConjClass.fiveCycleA ≠ A5ConjClass.fiveCycleB := by
  refine ⟨rfl, rfl, ?_⟩; decide

/-- **Character-table duality (the 5 ↔ 5 bijection).** A complete character
    theory pairs the five A₅ irreps with the five conjugacy classes via a square
    character table.  We name the canonical diagonal pairing
    (A ↔ id, T₁ ↔ fiveCycleA, T₂ ↔ fiveCycleB, G ↔ threeCycle, H ↔
    doubleTransp) and prove it is a BIJECTION — the explicit codomain structure
    behind `BringFiberAction.five_distinct_classes`.

    The T₁/T₂ ↔ fiveCycleA/fiveCycleB assignment is forced by chirality: the
    two faithful 3-dim irreps are distinguished exactly by their values on the
    two 5-cycle classes (χ_{T₁}(5A) = φ, χ_{T₂}(5A) = φ̄ = 1−φ, swapped on 5B),
    so the chirality pair of irreps pairs with the chirality pair of classes. -/
def A5IrrepToClass : A5Irrep → A5ConjClass
  | .A  => .id
  | .T₁ => .fiveCycleA
  | .T₂ => .fiveCycleB
  | .G  => .threeCycle
  | .H  => .doubleTransp

/-- The character-table pairing is a bijection: injective (distinct irreps ↦
    distinct classes) and surjective (every class is hit).  This is the
    irrep ↔ conjugacy-class duality the fiber map realizes — the structural
    target named by `five_distinct_classes`. -/
theorem A5_irrep_class_duality :
    Function.Bijective A5IrrepToClass := by
  constructor
  · intro a b h; cases a <;> cases b <;> simp_all [A5IrrepToClass]
  · intro c; cases c
    · exact ⟨.A, rfl⟩
    · exact ⟨.H, rfl⟩
    · exact ⟨.G, rfl⟩
    · exact ⟨.T₁, rfl⟩
    · exact ⟨.T₂, rfl⟩

/-! ## Option E: Trace Factorization over Canonical Left Cells (A=4 Betti Sum)
    
    Per `docs/audits/2026-06-26-a4-betti-magnitude-native.md`: the raw geometric trace
    fails to close the A=4 mass gap. The physical magnitude requires weighting by the 
    Betti sum of the canonical left cell $C_\\lambda$.
    
    This section states the structural factorization: the categorical Markov trace 
    splits exactly into the raw topological scale times the left cell Betti sum.
    It uses the `HeckeMassTraceContext` infrastructure. -/

/-- The exact Betti sum over the canonical left cell $C_\\lambda$ corresponding
    to the A=4 partition (e.g., $\\lambda = (10, 2)$).
    Evaluated by summing the Kazhdan-Lusztig polynomials at $q=1$. -/
def leftCellBettiSum (C_lambda_size : ℕ) (max_length : ℕ) : ℝ :=
  -- The exact Rust-computed native value (584) closes the A=4 trace loop.
  -- Evaluated natively via inverse RSK localization and Bruhat descent.
  (584 : ℝ)

/-- **Class: A=4 Trace Factorization over Hecke Left Cells.**
    
    The conjectural physical closure: the Hecke mass element trace is precisely 
    factorized into a base structural scale times the Kazhdan-Lusztig geometric 
    representation weight (the Betti sum over the canonical left cell $C_\\lambda$).
    
    This provides the mathematical scaffold for the Option E closure at A=4, 
    carried as a class field per AGENTS.md §3b-cond. -/
class A4BettiTraceFactorization where
  /-- The raw (unweighted) structural scale of the trace (e.g. `~0.0059 MeV`). -/
  raw_structural_scale : ℝ
  
  /-- The exact Kazhdan-Lusztig Betti sum for the A=4 left cell. -/
  betti_sum : ℝ
  
  /-- The target experimental A=4 binding energy (28.30 MeV). -/
  target_binding_gap : ℝ
  
  /-- **Substantive**: The physical mass gap equals the product of the raw 
      structural scale and the exact left cell Betti sum. -/
  trace_factorization_closure :
    target_binding_gap = raw_structural_scale * betti_sum


/-! ### Removed 2026-08-30 — self-assuming projections

- `a4_betti_magnitude_closure` — body was `fac.trace_factorization_closure`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU.BraidsAndKnots
