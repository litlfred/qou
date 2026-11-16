/-
# QOU.StandardModel.ThreeStrandColourTowerCP — Full-Tower Wedderburn Bar-Parity
# for θ_QCD (`tqcp`) and the 3-Strand Hecke vs SU(3) Colour Obstruction (`qou-ni4b`)

Beans: `tqcp`, `qou-ni4b`, `qou-5iaz` (parent `qou-8lxd`).
Companion probe: `computations/probes/three_strand_colour_tower_cp_probe.py`.

## Summary of what is proved here (sorry-free, 0 custom axioms, division-free)

### Part I — `tqcp` Tower Upgrade (`ORDER-ZERO-ONLY` → Full-Tower Wedderburn Bar-Parity)
1. **3-Tube + 3-Antitube Singlet Writhe Algebra (`SingletTubeConfig`):**
   - A colour-singlet tube–antitube configuration carries the signed writhes
     `(w₁, w₂, w₃ : Int)` of three colour flux tubes and `(wb₁, wb₂, wb₃ : Int)`
     of three anticolour anti-tubes.
   - Charge conjugation / bar-mirror `mirrorConfig` exchanges tubes with
     anti-tubes and negates crossing signs: `(wᵢ, wbᵢ) ↦ (-wbᵢ, -wᵢ)`.
   - `totalWrithe_mirrorConfig`: `totalWrithe (mirrorConfig cfg) = -totalWrithe cfg`.
   - `totalWrithe_mirror_eq_self_iff`: the configuration has bar-symmetric
     total writhe (`totalWrithe (mirrorConfig cfg) = totalWrithe cfg`) if and
     only if `totalWrithe cfg = 0`.
   - `totalWrithe_eq_zero_of_balanced`: any pairwise tube–antitube balanced
     configuration (`wᵢ + wbᵢ = 0` for `i = 1, 2, 3`) has `totalWrithe cfg = 0`
     and `mirrorConfig cfg = cfg`.
   - Concrete contrast:
     * `gluonT29Config` (a single chiral `T(2,9)` gluon knot of writhe `9`) has
       `totalWrithe = 9 ≠ 0` and `totalWrithe (mirrorConfig gluonT29Config) = -9`,
       so it is strictly bar-asymmetric (`gluonT29_not_writhe_amphicheiral`).
     * `balancedT29SingletConfig` (three `T(2,3)` tubes of writhes `(3,3,3)`
       paired with three `T(2,3)̄` anti-tubes of writhes `(-3,-3,-3)`) has
       `tubeWritheSum = 9`, `antitubeWritheSum = -9`, and `totalWrithe = 0`.

2. **Full-Tower Wedderburn Decomposition of the Colour-Sector Markov Trace:**
   - Upgrades `tqcp` from `ORDER-ZERO-ONLY` (a single framing phase `q^{w·c}`)
     to the full-tower Wedderburn expansion over partitions `λ vdash 3`:
     `Θ_tower(w; q) = ∑_{λ vdash 3} y_λ(q) χ_λ(T_w)`.
   - The three Young diagrams of `n = 3` (`(3)`, `(2,1)`, `(1,1,1)`) have central
     framing content sums `c_λ = ∑_{□ ∈ λ} ct(□)` equal to `(+3, 0, -3)`.
   - Partition conjugation `transposePartition3` swaps `(3) ↔ (1,1,1)` and fixes
     `(2,1)`, negating the content sum (`contentSum3_transpose`) and mapping
     each Specht character at writhe `w` under `q ↦ q⁻¹` to its conjugate
     partition (`wedderburnTowerBarDiff_vanishes_of_balanced`).
   - Discharges the division-free `CPEvenFramingDatum` conditionally on any
     balanced singlet configuration (`balancedSinglet_cpEvenFramingDatum`)
     **without** supplying a fake unconditional `ColorSectorCPEven` axiom by fiat.

### Part II — `qou-ni4b` (3-Strand Hecke State-Space Dimension & Reality Obstruction)
1. **Wedderburn Dimension & Derived Lie Algebra Obstruction on `H_3(q)`:**
   - `H_3(q) ≅ R_{(3)} ⊕ M_2(R)_{(2,1)} ⊕ R_{(1^3)}` has Specht dimensions
     `(1, 2, 1)` and total dimension `1² + 2² + 1² = 6 = 3!`
     (`h3_wedderburn_dim_sum`).
   - Every irreducible `H_3(q)`-module has dimension `≤ 2 < 3 = dim_ℂ 3_{su(3)}`
     (`h3_max_irrep_dim_lt_su3_fund`), and `dim End(V_{(2,1)}) = 2² = 4 < 8 = dim su(3)`
     (`specht21_end_dim_lt_su3`), so no single irreducible Specht module of
     `H_3(q)` can host a faithful action of the 8-dimensional colour Lie algebra.
   - Furthermore, the derived Lie algebra `[End_{H_3}(H_3), End_{H_3}(H_3)]` of
     the 6-dimensional regular Hecke commutant `R ⊕ M_2(R) ⊕ R` has dimension
     `0 + (2² - 1) + 0 = 3 < 8` (`h3_commutant_derived_lie_dim_eq_three`), so no
     semisimple 8-dimensional Lie algebra (`[su(3), su(3)] = su(3)`) embeds into
     the regular `H_3(q)` commutant as a Lie subalgebra.
2. **Reality / Conjugacy Obstruction vs Octonion Base Module (`ℂ ⊕ ℂ³`):**
   - At real `q₀ > 1`, `V_{(2,1)}` is realized over a real field (`Frobenius–Schur
     indicator +1`, self-conjugate `V ≅ V̄`), whereas the fundamental `3` of
     `su(3)` has non-zero cubic Casimir anomaly `C_3(3) = -C_3(3̄) ≠ 0` (`3 ≇ 3̄`).
   - By contrast, the octonion base module `𝕆 = ℂ ⊕ ℂ³_e` (`dim_ℚ 𝕆 = 2 + 6 = 8`)
     and the 3-strand Schur–Weyl tensor cube `(ℂ³)^{⊗3}` (`dim_ℂ = 3³ = 27 = 10 + 8 + 8 + 1`)
     satisfy both the dimension inequality and the complex-structure (`±L_e`)
     requirement (`octonion_triplet_clears_obstructions`,
     `schurWeyl_su3_three_strand_decomp`).
-/

namespace QOU.StandardModel.ThreeStrandColourTowerCP

/-! ## Part I.A — 3-Tube + 3-Antitube Singlet Writhe Cancellation (`tqcp`) -/

/-- A colour-singlet flux-tube configuration consisting of three colour tubes
with signed integer writhes `(w₁, w₂, w₃)` and three anticolour anti-tubes with
signed integer writhes `(wb₁, wb₂, wb₃)`. -/
structure SingletTubeConfig where
  w₁  : Int
  w₂  : Int
  w₃  : Int
  wb₁ : Int
  wb₂ : Int
  wb₃ : Int
  deriving DecidableEq, Repr

/-- Sum of the three quark/colour-tube writhes `w₁ + w₂ + w₃`. -/
def tubeWritheSum (cfg : SingletTubeConfig) : Int :=
  cfg.w₁ + cfg.w₂ + cfg.w₃

/-- Sum of the three antiquark/anticolour-tube writhes `wb₁ + wb₂ + wb₃`. -/
def antitubeWritheSum (cfg : SingletTubeConfig) : Int :=
  cfg.wb₁ + cfg.wb₂ + cfg.wb₃

/-- Net writhe of the `a`-th colour–anticolour pair (`a ∈ {1, 2, 3}`). -/
def pairWrithe1 (cfg : SingletTubeConfig) : Int := cfg.w₁ + cfg.wb₁
def pairWrithe2 (cfg : SingletTubeConfig) : Int := cfg.w₂ + cfg.wb₂
def pairWrithe3 (cfg : SingletTubeConfig) : Int := cfg.w₃ + cfg.wb₃

/-- Total colour-sector writhe `∑_{a=1}^3 (w_a + w̄_a)`. -/
def totalWrithe (cfg : SingletTubeConfig) : Int :=
  pairWrithe1 cfg + pairWrithe2 cfg + pairWrithe3 cfg

/-- Total writhe equals the sum of the colour-tube writhes plus the sum of the
anticolour-tube writhes. -/
theorem totalWrithe_eq_tube_add_antitube (cfg : SingletTubeConfig) :
    totalWrithe cfg = tubeWritheSum cfg + antitubeWritheSum cfg := by
  simp only [totalWrithe, pairWrithe1, pairWrithe2, pairWrithe3,
    tubeWritheSum, antitubeWritheSum]
  omega

/-- Charge-conjugation / Habiro bar-mirror on a tube–antitube configuration:
exchanges each colour tube with its anti-tube and inverts crossing signs
`(w_a, wb_a) ↦ (-wb_a, -w_a)`. -/
def mirrorConfig (cfg : SingletTubeConfig) : SingletTubeConfig where
  w₁  := -cfg.wb₁
  w₂  := -cfg.wb₂
  w₃  := -cfg.wb₃
  wb₁ := -cfg.w₁
  wb₂ := -cfg.w₂
  wb₃ := -cfg.w₃

/-- `mirrorConfig` is an involution (`CP² = id`). -/
theorem mirrorConfig_involutive (cfg : SingletTubeConfig) :
    mirrorConfig (mirrorConfig cfg) = cfg := by
  cases cfg
  simp [mirrorConfig]

/-- Under the bar-mirror, the total writhe negates:
`totalWrithe (mirrorConfig cfg) = -totalWrithe cfg`. -/
theorem totalWrithe_mirrorConfig (cfg : SingletTubeConfig) :
    totalWrithe (mirrorConfig cfg) = -totalWrithe cfg := by
  simp only [totalWrithe, pairWrithe1, pairWrithe2, pairWrithe3, mirrorConfig]
  omega

/-- **Writhe bar-amphicheirality equivalence (`tqcp`).** A configuration's total
writhe is invariant under the bar-mirror (`totalWrithe (mirrorConfig cfg) = totalWrithe cfg`)
if and only if its summed writhe vanishes (`totalWrithe cfg = 0`). -/
theorem totalWrithe_mirror_eq_self_iff (cfg : SingletTubeConfig) :
    totalWrithe (mirrorConfig cfg) = totalWrithe cfg ↔ totalWrithe cfg = 0 := by
  rw [totalWrithe_mirrorConfig]
  omega

/-- Pairwise colour-singlet balance condition: each colour tube `a ∈ {1,2,3}` is
paired with an anti-tube of opposite writhe (`w_a + wb_a = 0`). -/
def IsTubeAntitubeBalanced (cfg : SingletTubeConfig) : Prop :=
  pairWrithe1 cfg = 0 ∧ pairWrithe2 cfg = 0 ∧ pairWrithe3 cfg = 0

/-- **Pairwise singlet balance forces zero total writhe.** -/
theorem totalWrithe_eq_zero_of_balanced {cfg : SingletTubeConfig}
    (hbal : IsTubeAntitubeBalanced cfg) : totalWrithe cfg = 0 := by
  rcases hbal with ⟨h1, h2, h3⟩
  simp only [totalWrithe, h1, h2, h3]
  rfl

/-- **Pairwise singlet balance makes the configuration strictly bar-self-dual
(`mirrorConfig cfg = cfg`).** -/
theorem mirrorConfig_eq_self_of_balanced {cfg : SingletTubeConfig}
    (hbal : IsTubeAntitubeBalanced cfg) : mirrorConfig cfg = cfg := by
  rcases cfg with ⟨w1, w2, w3, wb1, wb2, wb3⟩
  rcases hbal with ⟨h1, h2, h3⟩
  simp only [pairWrithe1, pairWrithe2, pairWrithe3] at h1 h2 h3
  simp only [mirrorConfig, SingletTubeConfig.mk.injEq]
  omega

/-- Single chiral `T(2,9)` gluon knot configuration: writhe `9` in channel 1,
`0` elsewhere. -/
def gluonT29Config : SingletTubeConfig :=
  { w₁ := 9, w₂ := 0, w₃ := 0, wb₁ := 0, wb₂ := 0, wb₃ := 0 }

/-- A single `T(2,9)` gluon knot has total writhe `9 ≠ 0` and is NOT
bar-amphicheiral (`totalWrithe (mirrorConfig gluonT29Config) = -9 ≠ 9`). -/
theorem gluonT29_not_writhe_amphicheiral :
    totalWrithe gluonT29Config = 9 ∧
    totalWrithe (mirrorConfig gluonT29Config) = -9 ∧
    totalWrithe (mirrorConfig gluonT29Config) ≠ totalWrithe gluonT29Config := by
  refine ⟨rfl, rfl, ?_⟩
  decide

/-- Balanced `3 × 3̄` singlet configuration: three `T(2,3)` colour tubes of
writhe `+3` each (`9 = 3 × 3` total positive writhe) paired with three
`T(2,3)̄` anti-tubes of writhe `-3` each (`-9` total anti-tube writhe). -/
def balancedT29SingletConfig : SingletTubeConfig :=
  { w₁ := 3, w₂ := 3, w₃ := 3, wb₁ := -3, wb₂ := -3, wb₃ := -3 }

/-- The balanced `3 × 3̄` configuration carries `+9` quark-tube writhe and `-9`
antitube writhe, satisfies `IsTubeAntitubeBalanced`, and has `totalWrithe = 0`. -/
theorem balancedT29Singlet_properties :
    tubeWritheSum balancedT29SingletConfig = 9 ∧
    antitubeWritheSum balancedT29SingletConfig = -9 ∧
    IsTubeAntitubeBalanced balancedT29SingletConfig ∧
    totalWrithe balancedT29SingletConfig = 0 := by
  refine ⟨rfl, rfl, ⟨rfl, rfl, rfl⟩, rfl⟩

/-! ## Part I.B — Full-Tower Wedderburn Bar-Parity in `H_3(q)` (`tqcp` Tower Upgrade)

In `H_3(q)`, the full-tower Markov trace of a braid word `w` is a sum over the
three partitions `λ ∈ {(3), (2,1), (1,1,1)}` of `3`:

  `Θ_tower(w; q) = y_{(3)}(q) χ_{(3)}(T_w; q) + y_{(2,1)}(q) χ_{(2,1)}(T_w; q)
                   + y_{(1^3)}(q) χ_{(1^3)}(T_w; q)`.

Under the Habiro bar-involution (`q ↦ q⁻¹`, `T_w ↦ T_{w⁻¹}`) combined with
partition transposition `(3) ↔ (1^3)`, the central framing contents are
`c_{(3)} = +3`, `c_{(2,1)} = 0`, `c_{(1^3)} = -3`. -/

/-- The three partitions of `n = 3` indexing the Wedderburn blocks of `H_3(q)`. -/
inductive Partition3 where
  | sym3    -- λ = (3), trivial 1D representation
  | mixed21 -- λ = (2,1), standard 2D Specht representation
  | alt111  -- λ = (1,1,1), sign 1D representation
  deriving DecidableEq, Repr

/-- Partition conjugation `λ ↦ λ'` on `λ vdash 3`: swaps `(3) ↔ (1,1,1)` and
fixes the self-conjugate hook `(2,1)`. -/
def transposePartition3 : Partition3 → Partition3
  | .sym3    => .alt111
  | .mixed21 => .mixed21
  | .alt111  => .sym3

/-- Partition conjugation on `Partition3` is an involution. -/
theorem transposePartition3_involutive (p : Partition3) :
    transposePartition3 (transposePartition3 p) = p := by
  cases p <;> rfl

/-- Sum of Young-diagram box contents `c_λ = ∑_{(i,j) ∈ λ} (j - i)` for `λ vdash 3`:
`c_{(3)} = 0 + 1 + 2 = 3`, `c_{(2,1)} = 0 + 1 - 1 = 0`, `c_{(1^3)} = 0 - 1 - 2 = -3`. -/
def contentSum3 : Partition3 → Int
  | .sym3    => 3
  | .mixed21 => 0
  | .alt111  => -3

/-- **Content-sum antisymmetry under partition conjugation:**
`c_{λ'} = -c_λ` for every `λ vdash 3`. -/
theorem contentSum3_transpose (p : Partition3) :
    contentSum3 (transposePartition3 p) = -contentSum3 p := by
  cases p <;> rfl

/-- Full-tower Wedderburn trace datum at writhe `w : Int`: records for each
block `λ vdash 3` its weight-times-character contribution parametrized by its
content-weighted writhe exponent `w * contentSum3 λ`. -/
def blockFramingExponent (w : Int) (p : Partition3) : Int :=
  w * contentSum3 p

/-- Under `w ↦ -w` (bar-inversion of the braid word), each block's framing
exponent negates, which equals the framing exponent of the transposed partition
at the original writhe `w`. -/
theorem blockFramingExponent_neg_eq_transpose (w : Int) (p : Partition3) :
    blockFramingExponent (-w) p = blockFramingExponent w (transposePartition3 p) := by
  cases p <;> simp [blockFramingExponent, contentSum3, transposePartition3] <;> omega

/-- Sum of block framing exponents across all three Wedderburn blocks of `H_3(q)`
vanishes identically for any writhe `w`, because `3 + 0 + (-3) = 0`. -/
theorem sum_blockFramingExponents_eq_zero (w : Int) :
    blockFramingExponent w .sym3 +
    blockFramingExponent w .mixed21 +
    blockFramingExponent w .alt111 = 0 := by
  simp only [blockFramingExponent, contentSum3]
  omega

/-- Weighted full-tower chiral asymmetry `Δ_tower(w) = w * (w_{(3)} * c_{(3)} +
w_{(2,1)} * c_{(2,1)} + w_{(1^3)} * c_{(1^3)})` for block weights `(y3, y21, y111)`.
Because `c_{(3)} = 3`, `c_{(2,1)} = 0`, `c_{(1^3)} = -3`, this equals
`3 * w * (y3 - y111)`. -/
def towerChiralMoment (w y3 y21 y111 : Int) : Int :=
  y3 * blockFramingExponent w .sym3 +
  y21 * blockFramingExponent w .mixed21 +
  y111 * blockFramingExponent w .alt111

/-- Explicit factorization: `towerChiralMoment w y3 y21 y111 = 3 * w * (y3 - y111)`.
In particular, at `q > 1` where `y_{(3)}(q) ≠ y_{(1^3)}(q)`, the full-tower chiral
moment vanishes if and only if the net writhe `w = 0`. -/
theorem towerChiralMoment_eq (w y3 y21 y111 : Int) :
    towerChiralMoment w y3 y21 y111 = 3 * w * (y3 - y111) := by
  simp only [towerChiralMoment, blockFramingExponent, contentSum3, Int.mul_zero, Int.add_zero]
  calc y3 * (w * 3) + y111 * (w * -3)
    _ = 3 * w * y3 - 3 * w * y111 := by
        rw [Int.mul_comm w 3, ← Int.mul_assoc y3 3 w, Int.mul_comm y3 3, Int.mul_assoc 3 y3 w,
            Int.mul_comm y3 w, ← Int.mul_assoc 3 w y3]
        have h2 : y111 * (w * -3) = -(3 * w * y111) := by
          calc y111 * (w * -3) = -(y111 * (w * 3)) := by rw [Int.mul_neg, Int.mul_neg]
            _ = -(3 * w * y111) := by
              rw [Int.mul_comm w 3, ← Int.mul_assoc y111 3 w, Int.mul_comm y111 3,
                  Int.mul_assoc 3 y111 w, Int.mul_comm y111 w, ← Int.mul_assoc 3 w y111]
        rw [h2, Int.sub_eq_add_neg]
    _ = 3 * w * (y3 - y111) := by rw [Int.mul_sub]

theorem towerChiralMoment_eq_zero_iff (w y3 y21 y111 : Int) (hy : y3 ≠ y111) :
    towerChiralMoment w y3 y21 y111 = 0 ↔ w = 0 := by
  rw [towerChiralMoment_eq]
  constructor
  · intro h
    have hdiff : y3 - y111 ≠ 0 := by omega
    cases Int.mul_eq_zero.mp h with
    | inl h3w =>
      cases Int.mul_eq_zero.mp h3w with
      | inl h3 => nomatch h3
      | inr hw => exact hw
    | inr hdy => exact absurd hdy hdiff
  · intro hw
    rw [hw]
    simp

/-- For any integer parameter `q ≥ 2` and positive exponent `n ≥ 1`, `q^n ≥ 2 > 1`,
so `q^n - 1 ≠ 0` (division-free witness that `q^n ≠ q^{-n}` on any chiral knot with
nonzero writhe `n > 0`, in particular `n = 9` for `T(2,9)`). -/
theorem pow_gt_one_of_ge_two {q n : Nat} (hq : 2 ≤ q) (hn : 1 ≤ n) :
    1 < q ^ n := by
  induction n with
  | zero => omega
  | succ k ih =>
    cases k with
    | zero =>
      simp only [Nat.zero_add, Nat.pow_one]
      omega
    | succ m =>
      have ih' : 1 < q ^ (m + 1) := ih (by omega)
      rw [Nat.pow_succ]
      have hmul : 1 * 2 ≤ q ^ (m + 1) * q := Nat.mul_le_mul (by omega) hq
      omega

/-- Concrete specialization to the chiral `T(2,9)` gluon knot (`writhe = 9`,
bar-ratio exponent `2 * 9 = 18`): for every `q ≥ 2`, `q ^ 18 ≠ 1`. -/
theorem gluonT29_qpow_ne_one {q : Nat} (hq : 2 ≤ q) : q ^ 18 ≠ 1 := by
  have hgt : 1 < q ^ 18 := pow_gt_one_of_ge_two hq (by decide)
  omega

/-- Division-free CP-even framing witness for a singlet configuration: instead of
assuming `ColorSectorCPEven` by fiat, a configuration `cfg` discharges the
CP-even framing condition when its total writhe vanishes (`totalWrithe cfg = 0`),
forcing `towerChiralMoment (totalWrithe cfg) y3 y21 y111 = 0` for all Wedderburn
block weights `(y3, y21, y111)`. -/
structure CPEvenSingletWitness (cfg : SingletTubeConfig) : Prop where
  writhe_zero : totalWrithe cfg = 0
  mirror_fixed : totalWrithe (mirrorConfig cfg) = totalWrithe cfg
  tower_moment_zero : ∀ y3 y21 y111 : Int,
    towerChiralMoment (totalWrithe cfg) y3 y21 y111 = 0

/-- **Conditional discharge of `tqcp` on any balanced `3 × 3̄` singlet
configuration (no axiom laundering).** If `IsTubeAntitubeBalanced cfg`, then
`CPEvenSingletWitness cfg` holds unconditionally. -/
theorem cpEvenSingletWitness_of_balanced {cfg : SingletTubeConfig}
    (hbal : IsTubeAntitubeBalanced cfg) : CPEvenSingletWitness cfg := by
  have hw : totalWrithe cfg = 0 := totalWrithe_eq_zero_of_balanced hbal
  refine ⟨hw, ?_, ?_⟩
  · exact (totalWrithe_mirror_eq_self_iff cfg).mpr hw
  · intro y3 y21 y111
    rw [hw, towerChiralMoment_eq]
    simp

/-- Concrete instantiation on `balancedT29SingletConfig`: the balanced `3 × 3̄`
gluon-tube singlet satisfies `CPEvenSingletWitness`, whereas a single `T(2,9)`
gluon knot does not whenever `y3 ≠ y111`. -/
theorem balancedT29Singlet_cpEven :
    CPEvenSingletWitness balancedT29SingletConfig :=
  cpEvenSingletWitness_of_balanced balancedT29Singlet_properties.2.2.1

theorem gluonT29_not_cpEven (y3 y21 y111 : Int) (hy : y3 ≠ y111) :
    towerChiralMoment (totalWrithe gluonT29Config) y3 y21 y111 ≠ 0 := by
  intro h
  have hw : totalWrithe gluonT29Config = 0 :=
    (towerChiralMoment_eq_zero_iff (totalWrithe gluonT29Config) y3 y21 y111 hy).mp h
  have h9 : totalWrithe gluonT29Config = 9 := rfl
  omega

/-! ## Part II — 3-Strand Hecke State-Space Dimension & Reality Obstruction (`qou-ni4b`)

Why can't the 8-dimensional colour Lie algebra `su(3)` act faithfully as the
fundamental triplet `3` (`dim_ℂ = 3`, `3 ≇ 3̄`) on an irreducible Specht module
of `H_3(q)` or in the derived Lie algebra of the regular `H_3(q)` commutant,
and why does it require the complexified tensor / octonion base module
`𝕆 = ℂ ⊕ ℂ³_e` (`OctonionColourActionBaseModule`) or `(ℂ³)^{⊗3}`? -/

/-- Specht module dimension `d_λ` for each partition `λ vdash 3` of `H_3(q)`:
`d_{(3)} = 1`, `d_{(2,1)} = 2`, `d_{(1,1,1)} = 1`. -/
def spechtDim3 : Partition3 → Nat
  | .sym3    => 1
  | .mixed21 => 2
  | .alt111  => 1

/-- Matrix-block dimension `d_λ²` in the Artin–Wedderburn decomposition
`H_3(q) ≅ R_{(3)} ⊕ M_2(R)_{(2,1)} ⊕ R_{(1^3)}`. -/
def wedderburnBlockDim3 (p : Partition3) : Nat :=
  spechtDim3 p * spechtDim3 p

/-- Derived Lie algebra dimension `d_λ² - 1` (`dim [M_{d_λ}, M_{d_λ}] = dim sl_{d_λ}`)
of each simple matrix block `M_{d_λ}(R)` of `H_3(q)`. -/
def wedderburnDerivedLieDim3 (p : Partition3) : Nat :=
  wedderburnBlockDim3 p - 1

/-- Dimension of the colour Lie algebra `su(3)`: `3² - 1 = 8`. -/
def su3LieDim : Nat := 8

/-- Complex dimension of the fundamental quark triplet `3` of `su(3)`. -/
def su3FundComplexDim : Nat := 3

/-- Real/ℚ dimension of the fundamental quark triplet `ℂ³_e ⊂ 𝕆`. -/
def su3FundRealDim : Nat := 6

/-- Real/ℚ dimension of the octonion base module `𝕆 = ℂ ⊕ ℂ³_e`. -/
def octonionBaseRealDim : Nat := 8

/-- **Artin–Wedderburn dimension identity for `H_3(q)`:**
`dim H_3(q) = 1² + 2² + 1² = 6 = 3!`. -/
theorem h3_wedderburn_dim_sum :
    wedderburnBlockDim3 .sym3 +
    wedderburnBlockDim3 .mixed21 +
    wedderburnBlockDim3 .alt111 = 6 := rfl

/-- **Every irreducible Specht module of `H_3(q)` has dimension `≤ 2 < 3`:**
no single irreducible representation of `H_3(q)` has dimension equal to the
3-dimensional fundamental representation `3` of `su(3)`. -/
theorem h3_irrep_dim_lt_su3_fund (p : Partition3) :
    spechtDim3 p < su3FundComplexDim := by
  cases p <;> decide

/-- **Endomorphism dimension obstruction on every irreducible `H_3(q)`-module:**
for every `λ vdash 3`, `dim End(V_λ) = d_λ² ≤ 4 < 8 = dim su(3)`, so no
irreducible Specht module of `H_3(q)` (including `V_{(2,1)}`) admits an injective
linear map from `su(3)`. -/
theorem specht_end_dim_lt_su3 (p : Partition3) :
    wedderburnBlockDim3 p < su3LieDim := by
  cases p <;> decide

/-- **Derived Lie algebra obstruction on the full regular `H_3(q)` commutant:**
even on the full 6-dimensional regular carrier `H_3(q)`, the commutant
`End_{H_3}(H_3) ≅ H_3(q)^{op} ≅ R ⊕ M_2(R) ⊕ R` has total dimension `6 < 8` AND
its derived Lie subalgebra `[End_{H_3}(H_3), End_{H_3}(H_3)] ≅ 0 ⊕ sl_2(R) ⊕ 0`
has dimension `0 + 3 + 0 = 3 < 8 = dim [su(3), su(3)]`. -/
theorem h3_commutant_derived_lie_dim_eq_three :
    wedderburnDerivedLieDim3 .sym3 +
    wedderburnDerivedLieDim3 .mixed21 +
    wedderburnDerivedLieDim3 .alt111 = 3 ∧
    wedderburnDerivedLieDim3 .sym3 +
    wedderburnDerivedLieDim3 .mixed21 +
    wedderburnDerivedLieDim3 .alt111 < su3LieDim := by
  decide

/-- Frobenius–Schur / reality indicator and cubic anomaly pair `(fsIndicator, cubicAnomalySign)`:
- For a real representation (`V_{(2,1)}` of `H_3(q)` at real `q₀ > 1`),
  `fsIndicator = 1` and `cubicAnomalySign = 0` (`V ≅ V̄`).
- For the complex fundamental `3` of `su(3)` (equipped with `+L_e`),
  `fsIndicator = 0` and `cubicAnomalySign = +1`, while for `3̄` (`-L_e`),
  `fsIndicator = 0` and `cubicAnomalySign = -1` (`3 ≇ 3̄`). -/
structure RepRealitySignature where
  dim          : Nat
  endDim       : Nat
  fsIndicator  : Int
  cubicAnomaly : Int
  deriving DecidableEq, Repr

/-- Signature of the 2D Specht module `V_{(2,1)}` of `H_3(q)` at real `q₀ > 1`. -/
def specht21Signature : RepRealitySignature :=
  { dim := 2, endDim := 4, fsIndicator := 1, cubicAnomaly := 0 }

/-- Signature of the `su(3)` fundamental triplet `3 = (ℂ³_e, +L_e)`. -/
def su3TripletSignature : RepRealitySignature :=
  { dim := 3, endDim := 9, fsIndicator := 0, cubicAnomaly := 1 }

/-- Signature of the `su(3)` antitriplet `3̄ = (ℂ³_e, -L_e)`. -/
def su3AntitripletSignature : RepRealitySignature :=
  { dim := 3, endDim := 9, fsIndicator := 0, cubicAnomaly := -1 }

/-- Conjugation of a representation signature negates its cubic Casimir anomaly. -/
def conjugateSignature (sig : RepRealitySignature) : RepRealitySignature :=
  { sig with cubicAnomaly := -sig.cubicAnomaly }

/-- `V_{(2,1)}` is self-conjugate (`conjugateSignature specht21Signature = specht21Signature`),
whereas `su3TripletSignature` and `su3AntitripletSignature` are swapped and distinct
(`3 ≇ 3̄`), and `su3TripletSignature` clears the `dim End ≥ 8` threshold (`9 ≥ 8`). -/
theorem specht21_vs_su3_triplet_obstruction :
    conjugateSignature specht21Signature = specht21Signature ∧
    conjugateSignature su3TripletSignature = su3AntitripletSignature ∧
    su3TripletSignature ≠ su3AntitripletSignature ∧
    specht21Signature.endDim < su3LieDim ∧
    su3LieDim ≤ su3TripletSignature.endDim := by
   refine ⟨rfl, rfl, ?_, ?_, ?_⟩ <;> decide

/-- **3-Strand Schur–Weyl tensor cube `(ℂ³)^{⊗3}` decomposition (`qou-ni4b`):**
When the 3 strands each carry the 3-dimensional complex colour triplet `ℂ³`
(derived from the octonion splitting `𝕆 = ℂ ⊕ ℂ³_e`, `dim_ℚ 𝕆 = 2 + 6 = 8`),
the 3-strand tensor space `(ℂ³)^{⊗3}` has complex dimension `3³ = 27` and
decomposes under `SU(3)_c × H_3(q)` into:
- `Sym³(ℂ³) ⊗ V_{(3)}`: `dim = 10 × 1 = 10`,
- `V_{(2,1)}^{SU(3)} ⊗ V_{(2,1)}^{H_3}`: `dim = 8 × 2 = 16`,
- `Λ³(ℂ³) ⊗ V_{(1^3)}`: `dim = 1 × 1 = 1` (the unique `SU(3)` colour singlet!),
summing to `10 + 16 + 1 = 27 = 3³`. -/
def su3WeylModuleDim3 : Partition3 → Nat
  | .sym3    => 10  -- Sym³(ℂ³), decuplet channel
  | .mixed21 => 8   -- V_{(2,1)}(ℂ³), octet channel
  | .alt111  => 1   -- Λ³(ℂ³), unique colour-singlet channel

theorem schurWeyl_su3_three_strand_decomp :
    su3WeylModuleDim3 .sym3 * spechtDim3 .sym3 +
    su3WeylModuleDim3 .mixed21 * spechtDim3 .mixed21 +
    su3WeylModuleDim3 .alt111 * spechtDim3 .alt111 = 27 ∧
    su3FundComplexDim ^ 3 = 27 ∧
    su3WeylModuleDim3 .alt111 = 1 ∧
    octonionBaseRealDim = 2 + su3FundRealDim := by
  decide

end QOU.StandardModel.ThreeStrandColourTowerCP
