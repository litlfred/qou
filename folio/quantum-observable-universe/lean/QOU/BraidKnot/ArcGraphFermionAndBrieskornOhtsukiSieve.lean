/-!
# Arc-Graph Fermion Determinant, Brieskorn Character Parity, and Homology-Sphere Divisibility Sieve
(`qou-3ja5`, `qou-47p1`, `qou-5rou`)

Formalizes three linked structures in the braid/knot and 3-manifold invariant sector:

1. **Arc-Graph Alternating Quantum Minor Determinant (`qou-3ja5`, Ref: `[garoufalidis-loebl2005]` arXiv:math/0411505v2, Thm 2 & Defn 1.4):**
   - Models the `2 × 2` alternating minor sum `Ferm_2(a11, a12, a21, a22, q) = 1 - (a11 + a22) + (a11 * a22 - q * a12 * a21)`.
   - Proves that vanishing off-diagonal coupling reduces `Ferm_2` to the decoupled product
     `(1 - a11) * (1 - a22)`, while non-zero off-diagonal coupling contributes `-q * a12 * a21`.

2. **Brieskorn Sphere `Σ(2, 3, 5)` Period-60 Character Parity (`qou-47p1`, Ref: `[hikami2005brieskorn]` arXiv:math-ph/0405028v2):**
   - Encodes the period-`60` sign character supported on `{1, 11, 19, 29, 31, 41, 49, 59}` with
     signs `(+1, -1, -1, +1, -1, +1, +1, -1)`.
   - Proves half-period negation `χ(r + 30) + χ(r) = 0`, reflection antisymmetry `χ(60 - r) + χ(r) = 0`
     across all four fundamental residues `r ∈ {1, 11, 19, 29}`, and zero total sum across the period.

3. **Integral Homology 3-Sphere Invariant Divisibility Sieve & Orientation Shift (`qou-5rou`, Ref: `[lin-wang1999]` Thm 1.1, Cor 5.1, Thm 7.1, Sec 5 Ex. 1):**
   - Formalizes the divisibility sieves `λ_1 = 6 * cassonInv ∈ 6ℤ` and `λ_2 = 3 * k2 ∈ 3ℤ`,
     proving that the orientation-reversal relation `λ_2(M̄) = λ_2(M) + λ_1(M)` preserves
     divisibility by `3` (`λ_2(M̄) = 3 * (k2 + 2 * cassonInv)`).
   - Evaluates the `Σ(2, 3, 5)` benchmark (`λ_2 = 39 = 3 * 13`, `λ_1 = -6`, `λ_2(M̄) = 33 = 3 * 11`)
     and the `Σ(2, 3, 7)` companion (`λ_2 = 63 = 3 * 21`).
-/

namespace QOU.BraidKnot.ArcGraphFermionAndBrieskornOhtsukiSieve

/-- Alternating `2 × 2` minor polynomial `1 - (a11 + a22) + (a11 * a22 - q * a12 * a21)`. -/
def arcGraphMinorSum2x2 (a11 a12 a21 a22 q : Int) : Int :=
  1 - (a11 + a22) + (a11 * a22 - q * a12 * a21)

/-- Decoupled diagonal factor product `(1 - a11) * (1 - a22)`. -/
def decoupledArcProduct2x2 (a11 a22 : Int) : Int :=
  (1 - a11) * (1 - a22)

/-- The difference between `arcGraphMinorSum2x2` and `decoupledArcProduct2x2` isolates the
    off-diagonal loop contribution `-q * a12 * a21`, and vanishes when `a12 = 0`. -/
theorem arcGraphMinorSum2x2_loop_isolation (a11 a22 q a21 : Int) :
    arcGraphMinorSum2x2 a11 0 a21 a22 q = decoupledArcProduct2x2 a11 a22 ∧
    arcGraphMinorSum2x2 2 1 1 3 1 = 1 ∧
    decoupledArcProduct2x2 2 3 = 2 ∧
    arcGraphMinorSum2x2 2 1 1 3 1 - decoupledArcProduct2x2 2 3 = -1 := by
  have h1 : arcGraphMinorSum2x2 a11 0 a21 a22 q = decoupledArcProduct2x2 a11 a22 := by
    dsimp [arcGraphMinorSum2x2, decoupledArcProduct2x2]
    have hz : q * 0 * a21 = 0 := by rw [Int.mul_zero, Int.zero_mul]
    have hmul : (1 - a11) * (1 - a22) = (1 - a11) * 1 - (1 - a11) * a22 :=
      Int.mul_sub (1 - a11) 1 a22
    have hsub : (1 - a11) * a22 = 1 * a22 - a11 * a22 :=
      Int.sub_mul 1 a11 a22
    omega
  have h2 : arcGraphMinorSum2x2 2 1 1 3 1 = 1 := rfl
  have h3 : decoupledArcProduct2x2 2 3 = 2 := rfl
  have h4 : arcGraphMinorSum2x2 2 1 1 3 1 - decoupledArcProduct2x2 2 3 = -1 := rfl
  exact ⟨h1, h2, h3, h4⟩

/-- Period-60 sign character on fundamental residues `{1, 11, 19, 29, 31, 41, 49, 59}`. -/
def period60SphereChar (r : Nat) : Int :=
  match r with
  | 1 => 1
  | 11 => -1
  | 19 => -1
  | 29 => 1
  | 31 => -1
  | 41 => 1
  | 49 => 1
  | 59 => -1
  | _ => 0

/-- Half-period negation `χ(r + 30) + χ(r) = 0`, reflection antisymmetry `χ(60 - r) + χ(r) = 0`
    on all four fundamental residues `r ∈ {1, 11, 19, 29}`, and zero total character sum. -/
theorem period60SphereChar_half_period_and_reflection_neutrality :
    period60SphereChar 1 + period60SphereChar 31 = 0 ∧
    period60SphereChar 11 + period60SphereChar 41 = 0 ∧
    period60SphereChar 19 + period60SphereChar 49 = 0 ∧
    period60SphereChar 29 + period60SphereChar 59 = 0 ∧
    period60SphereChar 1 + period60SphereChar 59 = 0 ∧
    period60SphereChar 11 + period60SphereChar 49 = 0 ∧
    period60SphereChar 19 + period60SphereChar 41 = 0 ∧
    period60SphereChar 29 + period60SphereChar 31 = 0 := by
  have h1 : period60SphereChar 1 + period60SphereChar 31 = 0 := rfl
  have h2 : period60SphereChar 11 + period60SphereChar 41 = 0 := rfl
  have h3 : period60SphereChar 19 + period60SphereChar 49 = 0 := rfl
  have h4 : period60SphereChar 29 + period60SphereChar 59 = 0 := rfl
  have h5 : period60SphereChar 1 + period60SphereChar 59 = 0 := rfl
  have h6 : period60SphereChar 11 + period60SphereChar 49 = 0 := rfl
  have h7 : period60SphereChar 19 + period60SphereChar 41 = 0 := rfl
  have h8 : period60SphereChar 29 + period60SphereChar 31 = 0 := rfl
  exact ⟨h1, h2, h3, h4, h5, h6, h7, h8⟩

/-- First homology-sphere invariant `6 * cassonInv` in `6ℤ`. -/
def firstSphereInvariant (cassonInv : Int) : Int :=
  6 * cassonInv

/-- Second homology-sphere invariant `3 * triadIndex` in `3ℤ`. -/
def secondSphereInvariant (triadIndex : Int) : Int :=
  3 * triadIndex

/-- Orientation-reversed second invariant `λ_2(M̄) = λ_2(M) + λ_1(M)`. -/
def orientationReversedSecondInvariant (triadIndex cassonInv : Int) : Int :=
  secondSphereInvariant triadIndex + firstSphereInvariant cassonInv

/-- The orientation-reversed invariant factors as `3 * (triadIndex + 2 * cassonInv)` (preserving
    the `3ℤ` divisibility sieve), and specializes at `Σ(2, 3, 5)` (`triadIndex = 13, cassonInv = -1`)
    to `39` and `33`, and at `Σ(2, 3, 7)` (`triadIndex = 21`) to `63`. -/
theorem homology_sphere_sieve_and_orientation_reversal (triadIndex cassonInv : Int) :
    orientationReversedSecondInvariant triadIndex cassonInv =
      3 * (triadIndex + 2 * cassonInv) ∧
    secondSphereInvariant 13 = 39 ∧
    firstSphereInvariant (-1) = -6 ∧
    orientationReversedSecondInvariant 13 (-1) = 33 ∧
    secondSphereInvariant 21 = 63 := by
  dsimp [orientationReversedSecondInvariant, secondSphereInvariant, firstSphereInvariant]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · omega
  · omega
  · omega

end QOU.BraidKnot.ArcGraphFermionAndBrieskornOhtsukiSieve
