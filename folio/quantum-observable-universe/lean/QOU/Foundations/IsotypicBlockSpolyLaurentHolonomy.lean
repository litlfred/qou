/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Three-Stratum Isotypic Idempotent Decomposition, Overlap S-Polynomial Confluence, Partition Content Orthogonality, Formal Laurent Residue of Exact Forms, and Non-Abelian Plaquette Holonomy (`qou-59vq`, `qou-1o8n`, `qou-1oif`, `qou-1wcu`, `qou-6ers`)

This module provides machine-checked, self-contained algebraic foundations over a generic
commutative ring carrier `R` (`§7c` base-ring minimality: zero `ℝ` occurrences, no order or
archimedean hypotheses) covering five foundational work items under `qou-rtxm` and `qou-c8p8`:

1. **`qou-59vq` (Three-Stratum Central Idempotent Decomposition & Weighted Character Trace):**
   Proves that for three mutually orthogonal central idempotents `e0, e1, e2` (`e_i² = e_i`,
   `e_i · e_j = 0` for `i ≠ j`, `e0 + e1 + e2 = 1`), any element `x` decomposes into isotypic
   components `x0 = e0 · x, x1 = e1 · x, x2 = e2 · x`, projecting onto the `e0`-isotypic
   block annihilates the other blocks, and the three-stratum weighted character trace is
   additive across block characters.
2. **`qou-1o8n` (Overlap Ambiguity Reduction & S-Polynomial Confluence):**
   Proves that in any associative algebra over `R`, if `u · v = f` and `v · w = g`,
   the overlap associativity identity `(u · v) · w = u · (v · w)` forces the S-polynomial
   difference `f · w - u · g` to vanish, and when both `f' · w'` and `u' · g'` reduce to a
   common normal form `nf`, the S-polynomial `f' · w' - u' · g'` vanishes identically.
3. **`qou-1oif` (Three-Box Hook Content Sum Vanishing & Difference-of-Squares Spectral Factor):**
   Proves over generic `R` that for the three-box hook diagram with cell contents `(0, 1, -1)`,
   the symmetric elementary content sum `0 + (1 + (-1))` vanishes, the opposite-corner content
   product `(x + 1) · (x - 1)` equals `x² - 1`, and multiplying by the central content factor
   `x` gives the cubic spectral polynomial `x · ((x + 1) · (x - 1)) = x³ - x`.
4. **`qou-1wcu` (Formal Laurent Residue Vanishing on Exact Differentials & `R`-Linearity):**
   Defines a formal Laurent series window `(am2, am1, a0, a1, a2)` over `R`, its formal
   derivative `(neg am1, zero, a1, add a2 a2, zero)` in the shifted window, and the formal
   residue functional `laurentRes` (extracting the `z⁻¹` coefficient). Proves that `laurentRes`
   vanishes identically on every formal derivative `d(f)`, is `R`-linear, and is invariant
   under adding any exact differential `ω + d(f)`.
5. **`qou-6ers` (Non-Abelian Multiplicative Plaquette Holonomy Triviality under Flat Curvature):**
   Proves over a general (non-commutative) associative monoid/ring carrier `G` that when the
   parallel transports along a square plaquette satisfy the flat-curvature commutation law
   `hBot · hRight = hLeft · hTop` and the top/left edges have right inverses
   `hTop · hTopInv = 1`, `hLeft · hLeftInv = 1`, the oriented boundary holonomy
   `((hBot · hRight) · hTopInv) · hLeftInv` collapses to the multiplicative identity `1`.
-/

namespace QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy

universe u

/-- Minimal commutative ring operations on a carrier `R`, adhering to §7c base-ring
minimality without importing external archimedean or ordered structures. -/
structure CommRingCarrier (R : Type u) where
  add : R → R → R
  mul : R → R → R
  neg : R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  zero_add : ∀ a : R, add zero a = a
  add_zero : ∀ a : R, add a zero = a
  add_left_neg : ∀ a : R, add (neg a) a = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  one_mul : ∀ a : R, mul one a = a
  mul_one : ∀ a : R, mul a one = a
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)

namespace CommRingCarrier

variable {R : Type u} (ops : CommRingCarrier R)

/-- Subtraction defined as `a + (-b)`. -/
def sub (a b : R) : R := ops.add a (ops.neg b)

theorem add_right_neg (a : R) : ops.add a (ops.neg a) = ops.zero := by
  rw [ops.add_comm, ops.add_left_neg]

theorem sub_self (a : R) : ops.sub a a = ops.zero :=
  ops.add_right_neg a

theorem add_left_cancel {a b c : R} (h : ops.add a b = ops.add a c) : b = c := by
  have h1 : ops.add (ops.neg a) (ops.add a b) = ops.add (ops.neg a) (ops.add a c) :=
    congrArg (ops.add (ops.neg a)) h
  rw [← ops.add_assoc, ← ops.add_assoc, ops.add_left_neg, ops.zero_add, ops.zero_add] at h1
  exact h1

theorem add_right_cancel {a b c : R} (h : ops.add a c = ops.add b c) : a = b := by
  apply ops.add_left_cancel (a := c)
  rw [ops.add_comm c a, ops.add_comm c b]
  exact h

theorem mul_zero (a : R) : ops.mul a ops.zero = ops.zero := by
  apply ops.add_left_cancel (a := ops.mul a ops.zero)
  rw [← ops.left_distrib, ops.add_zero, ops.add_zero]

theorem zero_mul (a : R) : ops.mul ops.zero a = ops.zero := by
  rw [ops.mul_comm, ops.mul_zero]

theorem neg_eq_of_add_eq_zero {a b : R} (h : ops.add a b = ops.zero) :
    ops.neg a = b := by
  apply ops.add_right_cancel (c := a)
  rw [ops.add_left_neg, ops.add_comm b a]
  exact h.symm

theorem neg_zero : ops.neg ops.zero = ops.zero := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_zero ops.zero

theorem neg_neg (a : R) : ops.neg (ops.neg a) = a := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_left_neg a

theorem neg_add (a b : R) :
    ops.neg (ops.add a b) = ops.add (ops.neg a) (ops.neg b) := by
  apply ops.neg_eq_of_add_eq_zero
  rw [ops.add_assoc a b, ← ops.add_assoc b (ops.neg a) (ops.neg b),
      ops.add_comm b (ops.neg a), ops.add_assoc (ops.neg a) b (ops.neg b),
      ops.add_right_neg b, ops.add_zero, ops.add_right_neg a]

theorem mul_neg (a b : R) : ops.mul a (ops.neg b) = ops.neg (ops.mul a b) := by
  symm
  apply ops.neg_eq_of_add_eq_zero
  rw [← ops.left_distrib, ops.add_right_neg, ops.mul_zero]

theorem neg_mul (a b : R) : ops.mul (ops.neg a) b = ops.neg (ops.mul a b) := by
  rw [ops.mul_comm (ops.neg a) b, ops.mul_neg, ops.mul_comm b a]

theorem mul_sub {R : Type u} (ops : CommRingCarrier R) (a b c : R) :
    ops.mul a (ops.sub b c) = ops.sub (ops.mul a b) (ops.mul a c) := by
  dsimp only [sub]
  rw [ops.left_distrib, ops.mul_neg]

theorem sub_mul {R : Type u} (ops : CommRingCarrier R) (a b c : R) :
    ops.mul (ops.sub a b) c = ops.sub (ops.mul a c) (ops.mul b c) := by
  dsimp only [sub]
  rw [ops.right_distrib, ops.neg_mul]

end CommRingCarrier

/-! ## Section 1 (`qou-59vq`): Three-Stratum Orthogonal Idempotent Decomposition & Trace Splitting -/

/-- Three-stratum weighted trace `w0 · c0 + w1 · c1 + w2 · c2` over `R` (`qou-59vq`). -/
def isotypicWeightedTrace3 {R : Type u} (ops : CommRingCarrier R)
    (w0 w1 w2 c0 c1 c2 : R) : R :=
  ops.add (ops.add (ops.mul w0 c0) (ops.mul w1 c1)) (ops.mul w2 c2)

/-- **Orthogonal Idempotent Projection and Weighted Trace Additivity (`qou-59vq`):**
1. If `e0, e1, e2` form a complete orthogonal idempotent decomposition of unity
   (`e0 + e1 + e2 = 1`, `e0² = e0`, `e0 · e1 = 0`, `e0 · e2 = 0`), then every element `x`
   is reconstructed from its three stratum projections (`e0 x + e1 x + e2 x = x`), and
   projecting onto the `e0`-isotypic block annihilates the `e1` and `e2` components
   (`e0 · (e0 x + e1 x + e2 x) = e0 x`).
2. The three-stratum weighted character trace is additive across block characters. -/
theorem isotypic_three_block_projection_and_trace_add {R : Type u} (ops : CommRingCarrier R)
    (e0 e1 e2 x w0 w1 w2 c0 c1 c2 d0 d1 d2 : R)
    (hSum : ops.add (ops.add e0 e1) e2 = ops.one)
    (he00 : ops.mul e0 e0 = e0)
    (he01 : ops.mul e0 e1 = ops.zero)
    (he02 : ops.mul e0 e2 = ops.zero) :
    ops.add (ops.add (ops.mul e0 x) (ops.mul e1 x)) (ops.mul e2 x) = x ∧
      ops.mul e0 (ops.add (ops.add (ops.mul e0 x) (ops.mul e1 x)) (ops.mul e2 x)) =
        ops.mul e0 x ∧
      isotypicWeightedTrace3 ops w0 w1 w2
        (ops.add c0 d0) (ops.add c1 d1) (ops.add c2 d2) =
      ops.add
        (isotypicWeightedTrace3 ops w0 w1 w2 c0 c1 c2)
        (isotypicWeightedTrace3 ops w0 w1 w2 d0 d1 d2) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [← ops.right_distrib e0 e1 x, ← ops.right_distrib (ops.add e0 e1) e2 x,
        hSum, ops.one_mul]
  · rw [ops.left_distrib, ops.left_distrib,
        ← ops.mul_assoc e0 e0 x,
        ← ops.mul_assoc e0 e1 x,
        ← ops.mul_assoc e0 e2 x,
        he00, he01, he02,
        ops.zero_mul, ops.add_zero, ops.add_zero]
  · dsimp only [isotypicWeightedTrace3]
    rw [ops.left_distrib, ops.left_distrib, ops.left_distrib,
        ops.add_assoc (ops.mul w0 c0) (ops.mul w0 d0)
          (ops.add (ops.mul w1 c1) (ops.mul w1 d1)),
        ← ops.add_assoc (ops.mul w0 d0) (ops.mul w1 c1) (ops.mul w1 d1),
        ops.add_comm (ops.mul w0 d0) (ops.mul w1 c1),
        ops.add_assoc (ops.mul w1 c1) (ops.mul w0 d0) (ops.mul w1 d1),
        ← ops.add_assoc (ops.mul w0 c0) (ops.mul w1 c1)
          (ops.add (ops.mul w0 d0) (ops.mul w1 d1)),
        ops.add_assoc
          (ops.add (ops.mul w0 c0) (ops.mul w1 c1))
          (ops.add (ops.mul w0 d0) (ops.mul w1 d1))
          (ops.add (ops.mul w2 c2) (ops.mul w2 d2)),
        ← ops.add_assoc
          (ops.add (ops.mul w0 d0) (ops.mul w1 d1))
          (ops.mul w2 c2)
          (ops.mul w2 d2),
        ops.add_comm (ops.add (ops.mul w0 d0) (ops.mul w1 d1)) (ops.mul w2 c2),
        ops.add_assoc (ops.mul w2 c2)
          (ops.add (ops.mul w0 d0) (ops.mul w1 d1))
          (ops.mul w2 d2),
        ← ops.add_assoc
          (ops.add (ops.mul w0 c0) (ops.mul w1 c1))
          (ops.mul w2 c2)
          (ops.add (ops.add (ops.mul w0 d0) (ops.mul w1 d1)) (ops.mul w2 d2))]

/-! ## Section 2 (`qou-1o8n`): Overlap Ambiguity S-Polynomial and Confluence Criterion -/

/-- Overlap S-polynomial `f · w - u · g` formed from reduction rules `u · v → f` and
`v · w → g` (`qou-1o8n`). -/
def overlapSPolynomial {R : Type u} (ops : CommRingCarrier R) (f w u g : R) : R :=
  ops.sub (ops.mul f w) (ops.mul u g)

/-- **Overlap Associativity Identity and Normal-Form Confluence (`qou-1o8n`):**
1. If `u · v = f` and `v · w = g` in `R`, associativity `(u · v) · w = u · (v · w)` forces
   `overlapSPolynomial ops f w u g = 0`.
2. More generally, if `f' · w'` and `u' · g'` both reduce to the same normal form `nf`
   (`f' · w' = nf` and `u' · g' = nf`), then `overlapSPolynomial ops f' w' u' g' = 0` (joinability). -/
theorem overlap_spolynomial_assoc_and_joinable {R : Type u} (ops : CommRingCarrier R)
    (u v w f g f' g' w' u' nf : R)
    (hRule1 : ops.mul u v = f)
    (hRule2 : ops.mul v w = g)
    (hJoin1 : ops.mul f' w' = nf)
    (hJoin2 : ops.mul u' g' = nf) :
    overlapSPolynomial ops f w u g = ops.zero ∧
      overlapSPolynomial ops f' w' u' g' = ops.zero := by
  refine ⟨?_, ?_⟩
  · dsimp only [overlapSPolynomial]
    rw [← hRule1, ← hRule2, ops.mul_assoc, ops.sub_self]
  · dsimp only [overlapSPolynomial]
    rw [hJoin1, hJoin2, ops.sub_self]

/-! ## Section 3 (`qou-1oif`): Three-Box Hook Content Sum and Spectral Polynomial -/

/-- Content-shifted spectral product `x · ((x + 1) · (x - 1))` for a three-box hook diagram
with contents `(0, 1, -1)` (`qou-1oif`). -/
def hookThreeSpectralProduct {R : Type u} (ops : CommRingCarrier R) (x : R) : R :=
  ops.mul x (ops.mul (ops.add x ops.one) (ops.sub x ops.one))

/-- **Three-Box Hook Content Sum Vanishing and Cubic Factorization (`qou-1oif`):**
For the three-box hook diagram with cell contents `(0, 1, -1)`:
1. The content sum `0 + (1 + (-1))` vanishes in any commutative ring `R`;
2. The content-shifted spectral product `x · ((x + 1) · (x - 1))` equals `x³ - x`. -/
theorem hook_three_content_sum_and_cubic_factor {R : Type u} (ops : CommRingCarrier R)
    (x : R) :
    ops.add ops.zero (ops.add ops.one (ops.neg ops.one)) = ops.zero ∧
      hookThreeSpectralProduct ops x =
        ops.sub (ops.mul x (ops.mul x x)) x := by
  refine ⟨?_, ?_⟩
  · rw [ops.add_right_neg, ops.add_zero]
  · dsimp only [hookThreeSpectralProduct]
    have hDiffSq :
        ops.mul (ops.add x ops.one) (ops.sub x ops.one) =
          ops.sub (ops.mul x x) ops.one := by
      rw [ops.mul_sub, ops.right_distrib, ops.right_distrib,
          ops.one_mul, ops.mul_one, ops.mul_one]
      dsimp only [CommRingCarrier.sub]
      rw [ops.neg_add,
          ops.add_assoc (ops.mul x x) x (ops.add (ops.neg x) (ops.neg ops.one)),
          ← ops.add_assoc x (ops.neg x) (ops.neg ops.one),
          ops.add_right_neg, ops.zero_add]
    rw [hDiffSq, ops.mul_sub, ops.mul_one]

/-! ## Section 4 (`qou-1wcu`): Formal Laurent Residue of Exact Differentials & `R`-Linearity -/

/-- Formal 5-term Laurent window `am2 z⁻² + am1 z⁻¹ + a0 + a1 z + a2 z²` over `R` (`qou-1wcu`). -/
structure LaurentWindow (R : Type u) where
  am2 : R
  am1 : R
  a0 : R
  a1 : R
  a2 : R

/-- Pointwise addition of two formal Laurent windows over `R`. -/
def laurentAdd {R : Type u} (ops : CommRingCarrier R)
    (f g : LaurentWindow R) : LaurentWindow R :=
  { am2 := ops.add f.am2 g.am2
    am1 := ops.add f.am1 g.am1
    a0 := ops.add f.a0 g.a0
    a1 := ops.add f.a1 g.a1
    a2 := ops.add f.a2 g.a2 }

/-- Scalar multiplication of a formal Laurent window by `c : R`. -/
def laurentSmul {R : Type u} (ops : CommRingCarrier R)
    (c : R) (f : LaurentWindow R) : LaurentWindow R :=
  { am2 := ops.mul c f.am2
    am1 := ops.mul c f.am1
    a0 := ops.mul c f.a0
    a1 := ops.mul c f.a1
    a2 := ops.mul c f.a2 }

/-- Formal derivative `d/dz` of a Laurent window: the `z⁻²` coefficient comes from `-1 · am1`,
the `z⁻¹` coefficient is `0 · a0 = 0` (no `z⁰` term Differentiates to `z⁻¹`), the `z⁰`
coefficient is `a1`, and the `z¹` coefficient is `a2 + a2` (`qou-1wcu`). -/
def laurentDeriv {R : Type u} (ops : CommRingCarrier R)
    (f : LaurentWindow R) : LaurentWindow R :=
  { am2 := ops.neg f.am1
    am1 := ops.zero
    a0 := f.a1
    a1 := ops.add f.a2 f.a2
    a2 := ops.zero }

/-- Formal Laurent residue functional extracting the `z⁻¹` coefficient `am1` (`qou-1wcu`). -/
def laurentRes {R : Type u} (f : LaurentWindow R) : R :=
  f.am1

/-- **Formal Laurent Residue Vanishing on Exact Forms and `R`-Linearity (`qou-1wcu`):**
For any formal Laurent windows `f, w1, w2` over `R` and scalars `c1, c2 : R`:
1. The formal Laurent residue of an exact differential `laurentDeriv ops f` is `0`;
2. `laurentRes` is `R`-linear:
   `laurentRes (c1 · w1 + c2 · w2) = c1 · laurentRes w1 + c2 · laurentRes w2`;
3. Adding an exact differential `laurentDeriv ops f` to any form `w1` leaves its residue
   unchanged (`laurentRes (w1 + d(f)) = laurentRes w1`). -/
theorem laurent_residue_exact_zero_and_linear {R : Type u} (ops : CommRingCarrier R)
    (f w1 w2 : LaurentWindow R) (c1 c2 : R) :
    laurentRes (laurentDeriv ops f) = ops.zero ∧
      laurentRes (laurentAdd ops (laurentSmul ops c1 w1) (laurentSmul ops c2 w2)) =
        ops.add (ops.mul c1 (laurentRes w1)) (ops.mul c2 (laurentRes w2)) ∧
      laurentRes (laurentAdd ops w1 (laurentDeriv ops f)) = laurentRes w1 := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [laurentRes, laurentDeriv]
  · dsimp only [laurentRes, laurentAdd, laurentSmul]
  · dsimp only [laurentRes, laurentAdd, laurentDeriv]
    exact ops.add_zero w1.am1

/-! ## Section 5 (`qou-6ers`): Non-Abelian Multiplicative Plaquette Holonomy Triviality -/

/-- Minimal associative multiplicative monoid structure for non-abelian path-ordered
holonomy transport (`qou-6ers`). -/
structure AssocMonoidCarrier (G : Type u) where
  mul : G → G → G
  one : G
  mul_assoc : ∀ a b c : G, mul (mul a b) c = mul a (mul b c)
  one_mul : ∀ a : G, mul one a = a
  mul_one : ∀ a : G, mul a one = a

/-- Oriented boundary holonomy `((hBot · hRight) · hTopInv) · hLeftInv` around a square
plaquette (`qou-6ers`). -/
def plaquetteHolonomy {G : Type u} (M : AssocMonoidCarrier G)
    (hBot hRight hTopInv hLeftInv : G) : G :=
  M.mul (M.mul (M.mul hBot hRight) hTopInv) hLeftInv

/-- **Flat-Curvature Non-Abelian Plaquette Holonomy Collapse and Gauge Conjugation (`qou-6ers`):**
In any non-commutative associative monoid `G`:
1. If the bottom-then-right parallel transport equals the left-then-top transport
   (`hBot · hRight = hLeft · hTop`) and `hTop · hTopInv = 1`, `hLeft · hLeftInv = 1`,
   then `plaquetteHolonomy M hBot hRight hTopInv hLeftInv = 1`;
2. Under basepoint gauge conjugation by `g` with `gInv · g = 1`, a trivial holonomy `1`
   remains `gInv · (1 · g) = 1`. -/
theorem flat_plaquette_holonomy_eq_one_and_gauge_invariant {G : Type u}
    (M : AssocMonoidCarrier G)
    (hBot hRight hTop hLeft hTopInv hLeftInv g gInv : G)
    (hFlat : M.mul hBot hRight = M.mul hLeft hTop)
    (hTopR : M.mul hTop hTopInv = M.one)
    (hLeftR : M.mul hLeft hLeftInv = M.one)
    (hgL : M.mul gInv g = M.one) :
    plaquetteHolonomy M hBot hRight hTopInv hLeftInv = M.one ∧
      M.mul gInv (M.mul (plaquetteHolonomy M hBot hRight hTopInv hLeftInv) g) = M.one := by
  have hHol : plaquetteHolonomy M hBot hRight hTopInv hLeftInv = M.one := by
    dsimp only [plaquetteHolonomy]
    rw [hFlat,
        M.mul_assoc hLeft hTop hTopInv,
        hTopR, M.mul_one, hLeftR]
  refine ⟨hHol, ?_⟩
  rw [hHol, M.one_mul, hgL]

end QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy
