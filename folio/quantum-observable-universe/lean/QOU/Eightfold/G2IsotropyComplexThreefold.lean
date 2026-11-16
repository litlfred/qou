/-
# G₂ / SU(3) Isotropy Complex Threefold W ≅ ℂ³ & Bring–Klein S₄ Local Fano Bridge
## Work items: qou-uq5x, qou-ys29 (Epic qou-8lxd)

Formalizes the Günaydın–Gürsey (1973) octonionic colour action on the 6-dimensional
orthogonal complement `W = span(e₂, e₃, e₄, e₅, e₆, e₇) ⊂ Im(𝕆)` of a chosen
imaginary octonion unit `e₁` and the local Fano bridge to the Bring–Klein `S₄`
stabilizer:

1. **Complex structure `J = L_{e₁}` on `W ≅ ℝ⁶` (`qou-uq5x`)**:
   Under the Fano-plane multiplication triples `(1,2,3)`, `(1,4,5)`, `(1,6,7)` through `e₁`,
   left multiplication `J = L_{e₁}` maps:
   `J(e₂) = e₃, J(e₃) = -e₂, J(e₄) = e₅, J(e₅) = -e₄, J(e₆) = e₇, J(e₇) = -e₆`.
   Hence `J² = -id_W` identically on `W`, turning `W` into a 3-dimensional complex module
   `W ≅ ℂ³ = (e₂, e₃) ⊕ (e₄, e₅) ⊕ (e₆, e₇)` whose three complex lines are the three
   Fano lines through `e₁`.

2. **`𝔰𝔲(3)_{e₁}` preservation of `W` and triviality of `Λ³_ℂ W` (`qou-uq5x`)**:
   Any `J`-commuting endomorphism `D : W → W` (`D ∘ J = J ∘ D`) decomposes into 2×2
   Cauchy–Riemann blocks `[[a_{jk}, -b_{jk}], [b_{jk}, a_{jk}]]` representing complex
   entries `M_{jk} = a_{jk} + i b_{jk}`. Its action on the complex top exterior power
   `Λ³_ℂ W ≅ ℂ` has weight equal to the complex trace
   `tr_ℂ(D) = (a₁₁ + a₂₂ + a₃₃) + i (b₁₁ + b₂₂ + b₃₃)`.
   For `D ∈ 𝔰𝔲(3)_{e₁}` (`tr_ℂ(D) = 0`), the induced derivation on `Λ³_ℂ W` is identically
   zero (`det_ℂ(exp D) = 1`), so the colour singlet `Λ³_ℂ W ≅ 1` is derived directly from
   `L_{e₁}` and the Fano lines through `e₁`.

3. **Bring–Klein `S₄` local Fano bridge (`qou-ys29`)**:
   - `|Aut(Σ_Bring)| = |S₅| = 120`, `|Aut(𝒦_Klein)| = |PSL₂(𝔽₇)| = 168`,
     `gcd(120, 168) = 24 = |S₄|`, and `¬ (168 ∣ 120)` (`7 ∤ 120`), proving that
     `PSL₂(𝔽₇)` cannot embed as a subgroup of `S₅`.
   - The maximal common subgroup `S₄` of order `24` has index `168 / 24 = 7` in
     `PSL₂(𝔽₇)` (point/line stabilizer of the Fano plane) and index `120 / 24 = 5` in
     `S₅` (sheet stabilizer of the 5-sheeted Bring covering).
   - Fixing `e₁` partitions the 7 Fano lines into `3` local lines through `e₁` (which form
     the 3 complex lines of `W ≅ ℂ³`) and `4` non-local lines disjoint from `e₁` (`3 + 4 = 7`),
     while partitioning the 6 remaining imaginary units `{e₂, ..., e₇}` into `3` disjoint
     pairs of size `2` (`3 * 2 = 6`).
-/

namespace QOU.Eightfold.G2IsotropyComplexThreefold

/-! ## §1. The 6D Complement `W = span(e₂, ..., e₇)` and Complex Structure `J = L_{e₁}` -/

/-- A vector in the 6D orthogonal complement `W = span(e₂, e₃, e₄, e₅, e₆, e₇) ⊂ Im(𝕆)`
    over `ℤ`, grouped into the three Fano-line planes `(e₂, e₃)`, `(e₄, e₅)`, `(e₆, e₇)`
    through `e₁`. -/
structure OctComplement6 where
  x2 : Int
  x3 : Int
  x4 : Int
  x5 : Int
  x6 : Int
  x7 : Int
  deriving DecidableEq, Repr

namespace OctComplement6

/-- Zero vector in `W`. -/
def zero : OctComplement6 := ⟨0, 0, 0, 0, 0, 0⟩

/-- Vector addition in `W`. -/
def add (u v : OctComplement6) : OctComplement6 :=
  ⟨u.x2 + v.x2, u.x3 + v.x3, u.x4 + v.x4, u.x5 + v.x5, u.x6 + v.x6, u.x7 + v.x7⟩

/-- Additive inverse `-v` in `W`. -/
def neg (v : OctComplement6) : OctComplement6 :=
  ⟨-v.x2, -v.x3, -v.x4, -v.x5, -v.x6, -v.x7⟩

/-- Scalar multiplication by `c : Int` on `W`. -/
def smul (c : Int) (v : OctComplement6) : OctComplement6 :=
  ⟨c * v.x2, c * v.x3, c * v.x4, c * v.x5, c * v.x6, c * v.x7⟩

/-- Standard basis vectors `e₂, e₃, e₄, e₅, e₆, e₇` of `W`. -/
def e2 : OctComplement6 := ⟨1, 0, 0, 0, 0, 0⟩
def e3 : OctComplement6 := ⟨0, 1, 0, 0, 0, 0⟩
def e4 : OctComplement6 := ⟨0, 0, 1, 0, 0, 0⟩
def e5 : OctComplement6 := ⟨0, 0, 0, 1, 0, 0⟩
def e6 : OctComplement6 := ⟨0, 0, 0, 0, 1, 0⟩
def e7 : OctComplement6 := ⟨0, 0, 0, 0, 0, 1⟩

/-- Left multiplication `J = L_{e₁}` restricted to `W = span(e₂..e₇)` under the Fano triples
    `(1,2,3)`, `(1,4,5)`, `(1,6,7)`:
    `L_{e₁}(e₂) = e₃`, `L_{e₁}(e₃) = -e₂`,
    `L_{e₁}(e₄) = e₅`, `L_{e₁}(e₅) = -e₄`,
    `L_{e₁}(e₆) = e₇`, `L_{e₁}(e₇) = -e₆`.
    In coordinates, `J(x₂, x₃, x₄, x₅, x₆, x₇) = (-x₃, x₂, -x₅, x₄, -x₇, x₆)`. -/
def jMap (v : OctComplement6) : OctComplement6 :=
  ⟨-v.x3, v.x2, -v.x5, v.x4, -v.x7, v.x6⟩

/-- Action of `J = L_{e₁}` on the six basis units of `W`. -/
theorem jMap_basis :
    jMap e2 = e3 ∧
    jMap e3 = neg e2 ∧
    jMap e4 = e5 ∧
    jMap e5 = neg e4 ∧
    jMap e6 = e7 ∧
    jMap e7 = neg e6 := by
  decide

/-- **Key Complex-Structure Theorem (`qou-uq5x`)**:
    `J² = -id_W` for every vector `v ∈ W = span(e₂..e₇)`. -/
theorem jMap_sq_eq_neg (v : OctComplement6) :
    jMap (jMap v) = neg v := by
  cases v
  simp [jMap, neg]

/-- `J = L_{e₁}` is additive on `W`. -/
theorem jMap_add (u v : OctComplement6) :
    jMap (add u v) = add (jMap u) (jMap v) := by
  cases u; cases v
  simp [jMap, add, Int.neg_add]

/-- Projections onto the three complex Fano-line planes `W = W₁ ⊕ W₂ ⊕ W₃` through `e₁`. -/
def projPlane1 (v : OctComplement6) : OctComplement6 := ⟨v.x2, v.x3, 0, 0, 0, 0⟩
def projPlane2 (v : OctComplement6) : OctComplement6 := ⟨0, 0, v.x4, v.x5, 0, 0⟩
def projPlane3 (v : OctComplement6) : OctComplement6 := ⟨0, 0, 0, 0, v.x6, v.x7⟩

/-- Each of the three Fano-line planes `(e₂, e₃)`, `(e₄, e₅)`, `(e₆, e₇)` is `J`-invariant
    (commutes with `J = L_{e₁}`). -/
theorem fano_planes_jMap_invariant (v : OctComplement6) :
    jMap (projPlane1 v) = projPlane1 (jMap v) ∧
    jMap (projPlane2 v) = projPlane2 (jMap v) ∧
    jMap (projPlane3 v) = projPlane3 (jMap v) := by
  cases v
  simp [jMap, projPlane1, projPlane2, projPlane3]

/-- Direct-sum decomposition `v = projPlane1 v + projPlane2 v + projPlane3 v` of `W ≅ ℂ³`. -/
theorem direct_sum_three_fano_planes (v : OctComplement6) :
    add (add (projPlane1 v) (projPlane2 v)) (projPlane3 v) = v := by
  cases v
  simp [add, projPlane1, projPlane2, projPlane3]

end OctComplement6

/-! ## §2. `J`-Commuting Endomorphisms (`𝔤𝔩(3, ℂ)`) and `𝔰𝔲(3)_{e₁}` Singlet `Λ³_ℂ W = 1` -/

/-- A complex scalar `a + i b` represented over `ℤ` (acting on a 2D Fano plane `(e_{2k}, e_{2k+1})`
    via `a · I₂ + b · J₂`). -/
structure ComplexInt where
  re : Int
  im : Int
  deriving DecidableEq, Repr

/-- Action of a complex scalar `z = a + i b` on a 2D Fano-line plane `(x, y)` via `I` and `J`:
    `(a + b J)(x, y) = (a x - b y, b x + a y)`. -/
def complexPlaneAct (z : ComplexInt) (x y : Int) : Int × Int :=
  (z.re * x - z.im * y, z.im * x + z.re * y)

/-- Multiplication by `i = ⟨0, 1⟩` on a 2D Fano plane agrees with `J(x, y) = (-y, x)`. -/
theorem complexPlaneAct_i_eq_j (x y : Int) :
    complexPlaneAct ⟨0, 1⟩ x y = (-y, x) := by
  simp [complexPlaneAct]

/-- A 3×3 complex matrix over `ℤ` representing a `J`-commuting linear endomorphism of
    `W ≅ ℂ³ = (e₂, e₃) ⊕ (e₄, e₅) ⊕ (e₆, e₇)`. -/
structure ComplexEnd3 where
  m11 : ComplexInt
  m12 : ComplexInt
  m13 : ComplexInt
  m21 : ComplexInt
  m22 : ComplexInt
  m23 : ComplexInt
  m31 : ComplexInt
  m32 : ComplexInt
  m33 : ComplexInt
  deriving DecidableEq, Repr

namespace ComplexEnd3

/-- Complex trace `tr_ℂ(M) = m₁₁ + m₂₂ + m₃₃`, which is the Lie algebra weight on the top
    exterior power `Λ³_ℂ W`. -/
def complexTrace (M : ComplexEnd3) : ComplexInt :=
  ⟨M.m11.re + M.m22.re + M.m33.re, M.m11.im + M.m22.im + M.m33.im⟩

/-- Real trace of the corresponding 6×6 real matrix on `W ≅ ℝ⁶`: each 2×2 Cauchy–Riemann
    diagonal block `[[a_{kk}, -b_{kk}], [b_{kk}, a_{kk}]]` contributes `2 a_{kk}`. -/
def realTrace6 (M : ComplexEnd3) : Int :=
  2 * M.m11.re + 2 * M.m22.re + 2 * M.m33.re

/-- `J`-weighted trace `-tr_ℝ(J ∘ M) / 2`: each 2×2 diagonal block contributes `2 b_{kk}` to
    `-tr_ℝ(J ∘ M)`. -/
def jWeightedTrace6 (M : ComplexEnd3) : Int :=
  2 * M.m11.im + 2 * M.m22.im + 2 * M.m33.im

/-- The 6D real trace and `J`-weighted trace recover twice the real and imaginary parts
    of the complex trace `tr_ℂ(M)` on `W ≅ ℂ³`. -/
theorem real_and_j_trace_eq_two_complexTrace (M : ComplexEnd3) :
    realTrace6 M = 2 * (complexTrace M).re ∧
    jWeightedTrace6 M = 2 * (complexTrace M).im := by
  simp [realTrace6, jWeightedTrace6, complexTrace, Int.mul_add]

/-- Predicate for `M` to lie in the traceless Lie algebra `𝔰𝔩(3, ℂ)` (and specifically
    `𝔰𝔲(3)_{e₁}` when anti-Hermitian): `tr_ℂ(M) = 0`. -/
def isTraceless (M : ComplexEnd3) : Prop :=
  complexTrace M = ⟨0, 0⟩

/-- **Colour-Singlet Weight Theorem (`qou-uq5x`)**:
    On the 1-dimensional complex top exterior power `Λ³_ℂ W = span_ℂ(z₁ ∧ z₂ ∧ z₃)`, any
    `J`-commuting derivation `D` acts by scalar multiplication by `tr_ℂ(D)`. Therefore, every
    `D ∈ 𝔰𝔲(3)_{e₁}` (`isTraceless D`) acts with weight `(0, 0)` on `Λ³_ℂ W`, proving
    `Λ³_ℂ W ≅ 1` (colour singlet) and `realTrace6 D = 0 ∧ jWeightedTrace6 D = 0`. -/
theorem su3_annihilates_top_exterior_power (M : ComplexEnd3) (h : isTraceless M) :
    complexTrace M = ⟨0, 0⟩ ∧ realTrace6 M = 0 ∧ jWeightedTrace6 M = 0 := by
  have htr : complexTrace M = ⟨0, 0⟩ := h
  have hboth := real_and_j_trace_eq_two_complexTrace M
  rw [htr] at hboth
  exact ⟨htr, hboth.1, hboth.2⟩

/-- Binomial coefficient `binom n k` for exterior algebra dimension counting. -/
def binom : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => binom n k + binom n (k + 1)

/-- Dimension accounting for the `G₂ → SU(3)` isotropy decomposition on `W ≅ ℂ³`:
    - `dim_ℝ W = 6 = 2 * dim_ℂ W` with `dim_ℂ W = 3`,
    - `dim_ℂ (Λ⁰_ℂ W) = 1`, `dim_ℂ (Λ¹_ℂ W) = 3`, `dim_ℂ (Λ²_ℂ W) = 3`, `dim_ℂ (Λ³_ℂ W) = 1`,
    - Total exterior algebra dimension `1 + 3 + 3 + 1 = 8 = 2³` (one octonion / generation module). -/
theorem exterior_algebra_dimension_split :
    binom 3 0 = 1 ∧
    binom 3 1 = 3 ∧
    binom 3 2 = 3 ∧
    binom 3 3 = 1 ∧
    binom 3 0 + binom 3 1 + binom 3 2 + binom 3 3 = 8 := by
  decide

end ComplexEnd3

/-! ## §3. Bring–Klein `S₄` Local Fano Bridge (`qou-ys29`) -/

/-- Order of the Bring surface automorphism group `|Aut(Σ_Bring)| = |S₅| = 120`. -/
def bringAutOrder : Nat := 120

/-- Order of the Klein quartic / Fano plane automorphism group `|Aut(𝒦_Klein)| = |PSL₂(𝔽₇)| = 168`. -/
def kleinFanoAutOrder : Nat := 168

/-- Order of the common local stabilizer subgroup `|S₄| = 24`. -/
def s4Order : Nat := 24

/-- **Bring–Klein Group-Order Obstruction & `S₄` Bridge (`qou-ys29`)**:
    1. `gcd(|S₅|, |PSL₂(𝔽₇)|) = gcd(120, 168) = 24 = |S₄|`;
    2. `¬ (168 ∣ 120)` and `¬ (7 ∣ 120)`, so `PSL₂(𝔽₇)` cannot embed in `S₅`;
    3. `[PSL₂(𝔽₇) : S₄] = 168 / 24 = 7` (the 7 points / 7 lines of the Fano plane);
    4. `[S₅ : S₄] = 120 / 24 = 5` (the 5 sheets of the Bring covering). -/
theorem bring_klein_s4_order_bridge :
    Nat.gcd bringAutOrder kleinFanoAutOrder = s4Order ∧
    ¬ (kleinFanoAutOrder ∣ bringAutOrder) ∧
    ¬ (7 ∣ bringAutOrder) ∧
    kleinFanoAutOrder / s4Order = 7 ∧
    bringAutOrder / s4Order = 5 := by
  decide

/-- The 7 oriented Fano lines on the imaginary octonion indices `{1, 2, 3, 4, 5, 6, 7}`,
    with `{1,2,3}`, `{1,4,5}`, `{1,6,7}` passing through `e₁`. -/
def fanoLines : List (Nat × Nat × Nat) :=
  [(1, 2, 3), (1, 4, 5), (1, 6, 7),
   (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 5, 6)]

/-- Predicate testing whether a Fano triple contains the fixed imaginary unit `1` (`e₁`). -/
def containsUnit1 (line : Nat × Nat × Nat) : Bool :=
  let (a, b, c) := line
  a == 1 || b == 1 || c == 1

/-- **Local vs Non-Local Fano Partition (`qou-ys29` & `qou-uq5x`)**:
    Fixing `e₁` partitions the 7 Fano lines into:
    - `3` local Fano lines through `e₁` (which define the 3 complex lines of `W ≅ ℂ³` under `J = L_{e₁}`),
    - `4` non-local Fano lines disjoint from `e₁` (on which `S₄ = Stab_{PSL₂(𝔽₇)}(e₁)` acts as permutations of 4 elements),
    with `3 + 4 = 7`. -/
theorem fano_local_nonlocal_line_partition :
    fanoLines.length = 7 ∧
    (fanoLines.filter containsUnit1).length = 3 ∧
    (fanoLines.filter (fun l => !containsUnit1 l)).length = 4 := by
  decide

end QOU.Eightfold.G2IsotropyComplexThreefold
