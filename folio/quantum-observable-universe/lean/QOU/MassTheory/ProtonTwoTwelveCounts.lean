/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/

/-!
# Counts on the proton object, against the integers 2 and 12

Pre-registered survey: `docs/audits/2026-11-21-proton-two-twelve-count-survey.md` §1.
Production identity: `m_p = 2·m_μ·F_Bor(q) − 12·m_e`, with `β_Bor = (σ₀σ₁⁻¹)³ ∈ B₃`.
One definition per candidate; this file proves the values of K1–K5 and K7.
Nothing here uses an empirical number. Core Lean only (no Mathlib), all by `decide`.

* K3 `pairCrossings_bor`: each of the 3 pairs of closure components crosses 2 times;
  no component crosses itself.
* K4 `components_bor`: the closure has 3 components.
* K5 `seifertChi_bor`: Seifert's algorithm on the closed braid gives χ = 3 − 6 = −3.
* K7 `rotationOrbit_bor`: the word has exactly 2 distinct cyclic rotations.
* K1, K2 at the specialisation `q = 2` (`bor21_at_two`, `bor21_not_scalar`,
  `bor21_no_eigenvalue_one`): on the (2,1) irreducible, `64·β_Bor` is the integer matrix
  below; it is not scalar and does not have eigenvalue 1, while `β_Bor` acts as 1 on the
  two 1-dimensional blocks. Hence at `q = 2` the centraliser of `β_Bor` in
  `H₃ ≅ k × M₂(k) × k` has dimension 1 + 2 + 1 = 4 and `k[β_Bor]` has dimension 3.
  Lifting to generic `q` is the semicontinuity step in the audit (§2), not proved here.

None of K1–K5, K7 equals 12. K3 and K7 equal 2.
-/

namespace QOU.MassTheory.ProtonTwoTwelveCounts

/-- A braid letter on 3 strands: generator index (0 or 1) and sign (`true` = positive). -/
abbrev Letter := Nat × Bool

/-- `β_Bor = (σ₀σ₁⁻¹)³`. -/
def bor : List Letter := [(0, true), (1, false), (0, true), (1, false), (0, true), (1, false)]

/-- Positions after applying one letter: swap the strands at positions `g` and `g+1`.
`pos[s]` is the current position of strand `s`. -/
def stepPos (pos : List Nat) (g : Nat) : List Nat :=
  pos.map fun p => if p = g then g + 1 else if p = g + 1 then g else p

/-- The strand at position `p`. -/
def strandAt (pos : List Nat) (p : Nat) : Nat := (pos.idxOf p)

/-- Crossings as unordered strand pairs `(min, max)`, in word order. -/
def crossings : List Nat → List Letter → List (Nat × Nat)
  | _, [] => []
  | pos, (g, _) :: w =>
      let a := strandAt pos g
      let b := strandAt pos (g + 1)
      (min a b, max a b) :: crossings (stepPos pos g) w

/-- Final positions of the strands. -/
def finalPos : List Nat → List Letter → List Nat
  | pos, [] => pos
  | pos, (g, _) :: w => finalPos (stepPos pos g) w

theorem finalPos_bor : finalPos [0, 1, 2] bor = [0, 1, 2] := by decide

/-- K4: the closure permutation is the identity on 3 strands, so 3 components,
one per strand. -/
def components (w : List Letter) : Nat :=
  ((List.range 3).filter fun s => (finalPos [0, 1, 2] w).getD s 99 = s).length

theorem components_bor : components bor = 3 := by decide

/-- K3: crossings between strands `a < b`. Since the closure permutation is the
identity (`finalPos_bor`), strands are components. -/
def pairCrossings (w : List Letter) (a b : Nat) : Nat :=
  ((crossings [0, 1, 2] w).filter fun c => c = (a, b)).length

theorem pairCrossings_bor :
    pairCrossings bor 0 1 = 2 ∧ pairCrossings bor 0 2 = 2 ∧ pairCrossings bor 1 2 = 2 ∧
    ((crossings [0, 1, 2] bor).filter fun c => c.1 = c.2).length = 0 := by decide

/-- K5: χ of the Seifert surface from Seifert's algorithm on a closed 3-braid:
one disc per strand, one band per crossing. -/
def seifertChi (w : List Letter) : Int := 3 - w.length

theorem seifertChi_bor : seifertChi bor = -3 := by decide

/-- K7: distinct cyclic rotations of the word. -/
def rotations (w : List Letter) : List (List Letter) :=
  ((List.range w.length).map fun i => w.drop i ++ w.take i).eraseDups

theorem rotationOrbit_bor : (rotations bor).length = 2 := by decide

/-! ## K1, K2 at `q = 2`

(2,1) irreducible of `H₃(q)` with `(σ − q)(σ + q⁻¹) = 0`:
`σ₀ = [[q,1],[0,−q⁻¹]]`, `σ₁ = [[−q⁻¹,0],[1,q]]`, and `σᵢ⁻¹ = σᵢ − (q − q⁻¹)`.
At `q = 2`, twice each letter is an integer matrix. -/

/-- 2×2 integer matrices as `(a, b, c, d)` = `[[a,b],[c,d]]`. -/
abbrev M2 := Int × Int × Int × Int

def mul (x y : M2) : M2 :=
  let (a, b, c, d) := x
  let (e, f, g, h) := y
  (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)

/-- `2σ₀` at `q = 2`. -/
def s0 : M2 := (4, 2, 0, -1)
/-- `2σ₁⁻¹` at `q = 2` (`σ₁ − 3/2`). -/
def s1inv : M2 := (-4, 0, 2, 1)
/-- `2σ₀⁻¹` and `2σ₁` at `q = 2`, for the checks below. -/
def s0inv : M2 := (1, 2, 0, -4)
def s1 : M2 := (-1, 0, 2, 4)

/-- Sanity: `(2σ)(2σ⁻¹) = 4·I`, and the braid relation for `2σ₀, 2σ₁`. -/
theorem checks :
    mul s0 s0inv = (4, 0, 0, 4) ∧ mul s1 s1inv = (4, 0, 0, 4) ∧
    mul (mul s0 s1) s0 = mul (mul s1 s0) s1 := by decide

/-- `64·β_Bor` on the (2,1) irreducible at `q = 2`. -/
def bor21 : M2 := mul (mul (mul (mul (mul s0 s1inv) s0) s1inv) s0) s1inv

theorem bor21_at_two : bor21 = (-1628, 306, -306, 55) := by decide

/-- Not scalar (nonzero off-diagonal entry): its centraliser in `M₂` is 2-dimensional. -/
theorem bor21_not_scalar : bor21.2.1 ≠ 0 := by decide

/-- `det(64β − 64·I) ≠ 0`: 1 is not an eigenvalue on (2,1), so the minimal polynomial
of `β_Bor` on `k × M₂(k) × k` is `(x − 1)·χ₍₂,₁₎(x)`, of degree 3. -/
theorem bor21_no_eigenvalue_one :
    let (a, b, c, d) := bor21
    (a - 64) * (d - 64) - b * c ≠ 0 := by decide

/-- `β_Bor` acts as 1 on the trivial and sign blocks. At `q = 2`, scaled by 2 per letter:
trivial `2σ₀ = 4`, `2σ₁⁻¹ = 1`; sign `2σ₀ = −1`, `2σ₁⁻¹ = −4`. Both give `64 = 64·1`. -/
theorem bor_one_dim_blocks : ((4 : Int) * 1) ^ 3 = 64 ∧ ((-1 : Int) * (-4)) ^ 3 = 64 := by
  decide

/-- Summary: none of the computed counts is 12; K3 and K7 give 2. -/
theorem no_count_is_twelve :
    components bor ≠ 12 ∧ pairCrossings bor 0 1 ≠ 12 ∧ seifertChi bor ≠ 12 ∧
    (rotations bor).length ≠ 12 ∧ seifertChi bor ≠ -12 := by decide

end QOU.MassTheory.ProtonTwoTwelveCounts
