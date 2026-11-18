set_option autoImplicit false

/-!
# Adjacent-Transposition Cubic Relation, Involution Dimension Sum, Transversal Straightening, Hook-Major Sum, and Constructive Unimodular Witness

Formalizes five foundational algebraic identities over `Int` (`qou-36vh`, `qou-3xjy`, `qou-73kb`, `qou-anpu`, `qou-gjnc`):

1. **`qou-36vh` (Adjacent-Transposition Presentation and Cubic Braid Relation on 3-Element Permutations):**
   On 3-component integer vectors `Vec3`, the adjacent transpositions `swap01 (x0, x1, x2) = (x1, x0, x2)` and `swap12 (x0, x1, x2) = (x0, x2, x1)` are involutions (`swap01 (swap01 v) = v`, `swap12 (swap12 v) = v`) and satisfy the cubic braid relation `swap01 (swap12 (swap01 v)) = swap12 (swap01 (swap12 v)) = rev012 v`.

2. **`qou-3xjy` (Quantum Involution Recurrence and Classical Dimension Sum for `n = 3, 4`):**
   The quantum involution polynomials `invPoly2 q = 1 + q`, `invPoly3 q = invPoly2 q + (1 + q) * 1`, and `invPoly4 q = invPoly3 q + (1 + q + q * q) * invPoly2 q` expand to `invPoly3 q = 2 + 2 * q` (with `invPoly3 1 = 4`) and `invPoly4 q = 3 + 4 * q + 2 * (q * q) + q * (q * q)` (with `invPoly4 1 = 10`).

3. **`qou-73kb` (Division-Free Transversal Straightening vs Coset-Multiplied Sum):**
   The coset-multiplied straightening sum `cosetMultipliedSum hCard t0 t1 t2 = hCard * t0 - hCard * t1 + hCard * t2` factors over `Int` as `hCard * transversalSum t0 t1 t2`, so whenever the transversal relation `t1 = t0 + t2` holds, both `transversalSum t0 (t0 + t2) t2 = 0` and `cosetMultipliedSum hCard t0 (t0 + t2) t2 = 0` vanish without dividing by `hCard`.

4. **`qou-anpu` (Major-Index Polynomial and Hook-Product Identity for `(2, 1)` Tableaux):**
   For partition `(2, 1)` of `3`, the major-index generating sum `majGen21 q = q + q * q` factors as `q * (1 + q)` (evaluating to `2` at `q = 1`), and satisfies the cleared-denominator hook-content identity `(1 + q + q * q) * majGen21 q = q * ((1 + q) * (1 + q + q * q))`.

5. **`qou-gjnc` (Constructive Unimodular Linear Combination Witnesses):**
   The explicit linear combination `linearUnimodularEval a b u v = a * u + b * v` satisfies `linearUnimodularEval n (n + 1) (-1) 1 = 1`, `linearUnimodularEval (2 * n + 1) n 1 (-2) = 1`, and `linearUnimodularEval (3 * n + 1) n 1 (-3) = 1` for all `n : Int`.
-/

namespace QOU.Foundations.AdjacentTranspositionCubicRelationInvolutionDimensionSumTransversalStraighteningHookMajorSumConstructiveWitness

/-! ## Section 1: Adjacent-Transposition Presentation and Cubic Relation (`qou-36vh`) -/

/-- Three-component integer vector representing coordinates on 3 strands. -/
@[ext]
structure Vec3 where
  x0 : Int
  x1 : Int
  x2 : Int
  deriving DecidableEq, Repr

/-- First adjacent transposition swapping coordinates `0` and `1`. -/
def swap01 (v : Vec3) : Vec3 :=
  ⟨v.x1, v.x0, v.x2⟩

/-- Second adjacent transposition swapping coordinates `1` and `2`. -/
def swap12 (v : Vec3) : Vec3 :=
  ⟨v.x0, v.x2, v.x1⟩

/-- Reversal permutation swapping coordinates `0` and `2`. -/
def rev012 (v : Vec3) : Vec3 :=
  ⟨v.x2, v.x1, v.x0⟩

/-- **`qou-36vh` (Theorem 1a — Involution and Cubic Braid Relations of Adjacent Transpositions):**
    `swap01 (swap01 v) = v`, `swap12 (swap12 v) = v`,
    `swap01 (swap12 (swap01 v)) = swap12 (swap01 (swap12 v))`, and
    `swap01 (swap12 (swap01 v)) = rev012 v`. -/
theorem swap01_swap12_involutive_and_cubic_braid_eq_rev012 (v : Vec3) :
    swap01 (swap01 v) = v ∧
    swap12 (swap12 v) = v ∧
    swap01 (swap12 (swap01 v)) = swap12 (swap01 (swap12 v)) ∧
    swap01 (swap12 (swap01 v)) = rev012 v := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> ext <;> rfl

/-! ## Section 2: Quantum Involution Recurrence and Classical Dimension Sum (`qou-3xjy`) -/

/-- Degree-2 quantum involution polynomial `1 + q`. -/
def invPoly2 (q : Int) : Int :=
  1 + q

/-- Degree-3 quantum involution polynomial `invPoly2 q + (1 + q)`. -/
def invPoly3 (q : Int) : Int :=
  invPoly2 q + (1 + q)

/-- Degree-4 quantum involution polynomial `invPoly3 q + (1 + q + q^2) * invPoly2 q`. -/
def invPoly4 (q : Int) : Int :=
  invPoly3 q + (1 + q + q * q) * invPoly2 q

/-- **`qou-3xjy` (Theorem 2a — Expansion and Classical `q = 1` Evaluation of `invPoly3` and `invPoly4`):**
    `invPoly3 q = 2 + 2 * q`, `invPoly3 1 = 4`,
    `invPoly4 q = 3 + 4 * q + 2 * (q * q) + q * (q * q)`, and `invPoly4 1 = 10`. -/
theorem invPoly3_and_invPoly4_expansion_and_classical_eval (q : Int) :
    invPoly3 q = 2 + 2 * q ∧
    invPoly3 1 = 4 ∧
    invPoly4 q = 3 + 4 * q + 2 * (q * q) + q * (q * q) ∧
    invPoly4 1 = 10 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · dsimp only [invPoly3, invPoly2]
    omega
  · rfl
  · dsimp only [invPoly4, invPoly3, invPoly2]
    rw [Int.mul_add (1 + q + q * q) 1 q,
        Int.add_mul (1 + q) (q * q) q,
        Int.add_mul 1 q q,
        Int.mul_comm (q * q) q]
    omega
  · rfl

/-! ## Section 3: Division-Free Transversal Straightening vs Coset-Multiplied Sum (`qou-73kb`) -/

/-- Division-free transversal straightening combination `t0 - t1 + t2`. -/
def transversalSum (t0 t1 t2 : Int) : Int :=
  t0 - t1 + t2

/-- Coset-multiplied straightening combination `hCard * t0 - hCard * t1 + hCard * t2`. -/
def cosetMultipliedSum (hCard t0 t1 t2 : Int) : Int :=
  hCard * t0 - hCard * t1 + hCard * t2

/-- **`qou-73kb` (Theorem 3a — Division-Free Factorization and Unconditional Transversal Vanishing):**
    `cosetMultipliedSum hCard t0 t1 t2 = hCard * transversalSum t0 t1 t2`,
    `transversalSum t0 (t0 + t2) t2 = 0`, and
    `cosetMultipliedSum hCard t0 (t0 + t2) t2 = 0` for all `hCard t0 t1 t2 : Int`. -/
theorem cosetMultipliedSum_factorization_and_transversal_zero (hCard t0 t1 t2 : Int) :
    cosetMultipliedSum hCard t0 t1 t2 = hCard * transversalSum t0 t1 t2 ∧
    transversalSum t0 (t0 + t2) t2 = 0 ∧
    cosetMultipliedSum hCard t0 (t0 + t2) t2 = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [cosetMultipliedSum, transversalSum]
    rw [Int.mul_add hCard (t0 - t1) t2, Int.mul_sub hCard t0 t1]
  · dsimp only [transversalSum]
    omega
  · dsimp only [cosetMultipliedSum]
    rw [Int.mul_add hCard t0 t2]
    omega

/-! ## Section 4: Major-Index Polynomial and Hook-Product Identity for `(2, 1)` (`qou-anpu`) -/

/-- Major-index generating sum `q + q^2` for standard tableaux of shape `(2, 1)`. -/
def majGen21 (q : Int) : Int :=
  q + q * q

/-- Cleared-denominator major-index side `(1 + q + q^2) * majGen21 q`. -/
def clearedMajLHS21 (q : Int) : Int :=
  (1 + q + q * q) * majGen21 q

/-- Cleared-denominator hook-content side `q * ((1 + q) * (1 + q + q^2))`. -/
def clearedHookRHS21 (q : Int) : Int :=
  q * ((1 + q) * (1 + q + q * q))

/-- **`qou-anpu` (Theorem 4a — Major-Index Factorization and Hook-Product Identity for `(2, 1)`):**
    `majGen21 q = q * (1 + q)`, `majGen21 1 = 2`, and `clearedMajLHS21 q = clearedHookRHS21 q`. -/
theorem majGen21_factorization_and_clearedHook_identity (q : Int) :
    majGen21 q = q * (1 + q) ∧
    majGen21 1 = 2 ∧
    clearedMajLHS21 q = clearedHookRHS21 q := by
  have hmaj : majGen21 q = q * (1 + q) := by
    dsimp only [majGen21]
    rw [Int.mul_add q 1 q, Int.mul_one q]
  refine ⟨hmaj, rfl, ?_⟩
  · dsimp only [clearedMajLHS21, clearedHookRHS21]
    rw [hmaj, Int.mul_comm (1 + q + q * q) (q * (1 + q)),
        Int.mul_assoc q (1 + q) (1 + q + q * q)]

/-! ## Section 5: Constructive Unimodular Linear Combination Witnesses (`qou-gjnc`) -/

/-- Evaluation of a two-term integer linear combination `a * u + b * v`. -/
def linearUnimodularEval (a b u v : Int) : Int :=
  a * u + b * v

/-- **`qou-gjnc` (Theorem 5a — Explicit Constructive Unimodular Witnesses):**
    `linearUnimodularEval n (n + 1) (-1) 1 = 1`,
    `linearUnimodularEval (2 * n + 1) n 1 (-2) = 1`, and
    `linearUnimodularEval (3 * n + 1) n 1 (-3) = 1` for all `n : Int`. -/
theorem constructive_unimodular_witness_identities (n : Int) :
    linearUnimodularEval n (n + 1) (-1) 1 = 1 ∧
    linearUnimodularEval (2 * n + 1) n 1 (-2) = 1 ∧
    linearUnimodularEval (3 * n + 1) n 1 (-3) = 1 := by
  dsimp only [linearUnimodularEval]
  refine ⟨?_, ?_, ?_⟩ <;> omega

end QOU.Foundations.AdjacentTranspositionCubicRelationInvolutionDimensionSumTransversalStraighteningHookMajorSumConstructiveWitness
