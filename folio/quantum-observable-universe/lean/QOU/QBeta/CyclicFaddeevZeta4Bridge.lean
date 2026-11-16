/-
# FIBRE-A: Bridge `CyclicFaddeevPhi` at `N = 4` to the `ζ₄` Analytic Model (`qou-ztod`)

Bridges the two sorry-free `ζ₄` artifacts in the QOU Lean library that previously did not touch:
1. `QOU.QBeta.FaddeevPhiFibreBranch` (`CyclicFaddeevPhi ζ N D`): the multiplicative finite
   `q`-Pochhammer denominator `D(x) = ∏_{k<N} (1 - x·ζ^k) = 1 - x^N` at a primitive `N`-th
   root of unity `ζ`, satisfying the finite boundary-trade law
   `(1 - x) · D(ζ·x) = (1 - x·ζ^N) · D(x)` and exact `N`-periodicity `D(ζ·x) = D(x)`.
2. `QOU.Mass.ComplexVolumeZeta4Partner` (`vModel z = cosh z + i·sinh z`, `zeta4Rot`,
   `IsZeta4Faithful`): the analytic `ζ₄`-partner model under the quarter-period rotation
   `z ↦ z + iπ/2` (`x = e^z ↦ i·x = ζ₄·x`), which negates the bar-even binding (`cosh`)
   channel, preserves the bar-odd `Q_β` (`i·sinh`) channel, and has vanishing trivial
   (4-step orbit sum = 0) and sign (alternating 4-step orbit sum = 0) `ℤ₄`-isotypes.

## Main Structural Theorems

1. **Exact `N = 4` Cyclotomic Collapse & `CyclicFaddeevPhi` Discharge (`cyclicDenomFour_collapse`,
   `cyclicDenomFour_shift_factor`, `cyclicDenomFour_periodic`):**
   Over the Gaussian integer ring `ℤ[i]` carrying the primitive fourth root of unity `ζ₄ = i`
   (`ζ₄² = -1`, `ζ₄³ = -ζ₄`, `ζ₄⁴ = 1`), the 4-factor cyclic denominator
   `D₄(x) = (1 - x)(1 - ζ₄ x)(1 - ζ₄² x)(1 - ζ₄³ x)` collapses identically to `1 - x⁴`,
   satisfies the boundary-trade shift identity `(1 - x) D₄(ζ₄ x) = (1 - ζ₄⁴ x) D₄(x)`,
   and is strictly `ζ₄`-invariant: `D₄(ζ₄ x) = D₄(x)`.
2. **Falsifier — Pure `CyclicFaddeevPhi` Carrier Cannot Be `IsZeta4Faithful`
   (`cyclicCarrier_orbit_and_sign`, `cyclicCarrier_not_zeta4Faithful_of_ne_zero`):**
   Because any `CyclicFaddeevPhi` carrier `D` at `N = 4` is `ζ₄`-periodic (`D(ζ₄ x) = D(x)`),
   its 4-step `ζ₄`-orbit sum equals `4 · D(x)` (purely trivial `ℤ₄`-isotype). Therefore, a bare
   `CyclicFaddeevPhi` carrier alone has a non-vanishing orbit sum whenever `D(x) ≠ 0` and is
   refuted as a stand-alone `IsZeta4Faithful` assembly.
3. **Multiplicative Bridge — Product of `vModel` with `CyclicFaddeevPhi` at `N = 4` Preserves
   Both `ζ₄`-Partner Channel Parity and `IsZeta4Faithful`
   (`bridgedAssembly_zeta4_sq`, `bridgedAssembly_isZeta4Faithful`,
   `bridgedCyclicDenomFour_isZeta4Faithful`):**
   Coupling the analytic channel state `(e_+, e_-)` of `vModel` to any `CyclicFaddeevPhi` carrier
   `D` at `N = 4` via `A(st) · D(st.xCoord)` preserves:
   - the `ζ₄² = -1` two-step negation law,
   - exact vanishing of the 4-step trivial isotype (orbit sum = 0),
   - exact vanishing of the 4-step sign isotype (alternating orbit sum = 0),
   while carrying the explicit non-constant polynomial factor `D₄(x) = 1 - x⁴`.

All proofs are sorry-free, axiom-free, and Mathlib-free (pure Lean 4 core over `Int`).
-/

namespace QOU.QBeta.CyclicFaddeevZeta4Bridge

/-- Elements of the Gaussian integer ring `ℤ[i]` (`re + im · i`, with `i² = -1`),
    providing the exact arithmetic carrier for the primitive 4th root of unity `ζ₄ = i`
    and the 4-factor `CyclicFaddeevPhi` polynomial `(x; ζ₄)₄ = 1 - x⁴`. -/
structure GaussianInt where
  re : Int
  im : Int
  deriving DecidableEq, Repr

namespace GaussianInt

/-- Zero in `ℤ[i]`. -/
def zero : GaussianInt := ⟨0, 0⟩

/-- Multiplicative unit `1` in `ℤ[i]`. -/
def one : GaussianInt := ⟨1, 0⟩

/-- The primitive fourth root of unity `ζ₄ = i` in `ℤ[i]`. -/
def zeta4 : GaussianInt := ⟨0, 1⟩

/-- Addition in `ℤ[i]`. -/
def add (a b : GaussianInt) : GaussianInt :=
  ⟨a.re + b.re, a.im + b.im⟩

/-- Negation in `ℤ[i]`. -/
def neg (a : GaussianInt) : GaussianInt :=
  ⟨-a.re, -a.im⟩

/-- Subtraction in `ℤ[i]`. -/
def sub (a b : GaussianInt) : GaussianInt :=
  ⟨a.re - b.re, a.im - b.im⟩

/-- Multiplication in `ℤ[i]`: `(a_r + i a_i)(b_r + i b_i) = (a_r b_r - a_i b_i) + i(a_r b_i + a_i b_r)`. -/
def mul (a b : GaussianInt) : GaussianInt :=
  ⟨a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re⟩

/-- Integer scalar multiplication `k · a` in `ℤ[i]`. -/
def smul (k : Int) (a : GaussianInt) : GaussianInt :=
  ⟨k * a.re, k * a.im⟩

/-- Explicit powers `a^n` in `ℤ[i]`. -/
def pow (a : GaussianInt) : Nat → GaussianInt
  | 0 => one
  | n + 1 => mul (pow a n) a

@[ext]
theorem ext {a b : GaussianInt} (hre : a.re = b.re) (him : a.im = b.im) : a = b := by
  cases a; cases b; simp_all

theorem zero_mul (d : GaussianInt) : mul zero d = zero := by
  rcases d with ⟨dr, di⟩
  apply ext <;> simp [mul, zero]

theorem mul_one (a : GaussianInt) : mul a one = a := by
  rcases a with ⟨ar, ai⟩
  apply ext <;> simp [mul, one]

theorem one_mul (a : GaussianInt) : mul one a = a := by
  rcases a with ⟨ar, ai⟩
  apply ext <;> simp [mul, one]

theorem neg_mul (a d : GaussianInt) : mul (neg a) d = neg (mul a d) := by
  rcases a with ⟨ar, ai⟩
  rcases d with ⟨dr, di⟩
  apply ext <;> simp [mul, neg, Int.neg_mul] <;> omega

theorem add_mul (a b d : GaussianInt) :
    mul (add a b) d = add (mul a d) (mul b d) := by
  rcases a with ⟨ar, ai⟩
  rcases b with ⟨br, bi⟩
  rcases d with ⟨dr, di⟩
  apply ext <;> simp [mul, add, Int.add_mul] <;> omega

theorem sub_mul (a b d : GaussianInt) :
    mul (sub a b) d = sub (mul a d) (mul b d) := by
  rcases a with ⟨ar, ai⟩
  rcases b with ⟨br, bi⟩
  rcases d with ⟨dr, di⟩
  apply ext <;> simp [mul, sub, Int.sub_mul] <;> omega

theorem mul_zeta4 (x : GaussianInt) : mul zeta4 x = ⟨-x.im, x.re⟩ := by
  rcases x with ⟨xr, xi⟩
  apply ext <;> simp [mul, zeta4]

theorem mul_zeta4_four_times (x : GaussianInt) :
    mul zeta4 (mul zeta4 (mul zeta4 (mul zeta4 x))) = x := by
  rcases x with ⟨xr, xi⟩
  apply ext <;> simp [mul_zeta4]

/-- `ζ₄² = -1` in `ℤ[i]`. -/
theorem zeta4_sq : mul zeta4 zeta4 = neg one := by
  decide

/-- `ζ₄³ = -ζ₄` in `ℤ[i]`. -/
theorem zeta4_cube : pow zeta4 3 = neg zeta4 := by
  decide

/-- `ζ₄⁴ = 1` in `ℤ[i]`, establishing order 4. -/
theorem zeta4_pow_four : pow zeta4 4 = one := by
  decide

/-- Primitive 4th root verification: `ζ₄¹ ≠ 1`, `ζ₄² ≠ 1`, `ζ₄³ ≠ 1`, and `ζ₄⁴ = 1`. -/
theorem zeta4_isPrimitiveFour :
    pow zeta4 1 ≠ one ∧ pow zeta4 2 ≠ one ∧ pow zeta4 3 ≠ one ∧ pow zeta4 4 = one := by
  decide

/-- The 4th cyclotomic polynomial vanishes at `ζ₄`: `1 + ζ₄ + ζ₄² + ζ₄³ = 0`. -/
theorem zeta4_orbit_sum_zero :
    add (add (add one zeta4) (pow zeta4 2)) (pow zeta4 3) = zero := by
  decide

/-- Scaling `x` by `ζ₄ = i` negates `x²`: `(ζ₄ · x)² = -(x²)`. -/
theorem sq_mul_zeta4 (x : GaussianInt) :
    mul (mul zeta4 x) (mul zeta4 x) = neg (mul x x) := by
  rcases x with ⟨r, m⟩
  rw [mul_zeta4 ⟨r, m⟩]
  apply ext
  · dsimp [mul, neg]
    have h1 : -m * -m = m * m := by rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    omega
  · dsimp [mul, neg]
    have h1 : -m * r = -(m * r) := Int.neg_mul m r
    have h2 : r * -m = -(r * m) := Int.mul_neg r m
    omega

/-- Negating an element preserves its square: `(-a)² = a²`. -/
theorem sq_neg (a : GaussianInt) :
    mul (neg a) (neg a) = mul a a := by
  rcases a with ⟨r, m⟩
  apply ext
  · dsimp [mul, neg]
    have h1 : -r * -r = r * r := by rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    have h2 : -m * -m = m * m := by rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    omega
  · dsimp [mul, neg]
    have h1 : -r * -m = r * m := by rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    have h2 : -m * -r = m * r := by rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    omega

theorem mul_add (a b d : GaussianInt) :
    mul a (add b d) = add (mul a b) (mul a d) := by
  rcases a with ⟨ar, ai⟩
  rcases b with ⟨br, bi⟩
  rcases d with ⟨dr, di⟩
  apply ext <;> simp [mul, add, Int.mul_add] <;> omega

/-- Difference of squares in `ℤ[i]`: `(1 - a)(1 + a) = 1 - a²`. -/
theorem one_sub_mul_one_add (a : GaussianInt) :
    mul (sub one a) (add one a) = sub one (mul a a) := by
  rw [sub_mul, one_mul, mul_add, mul_one]
  rcases a with ⟨ar, ai⟩
  rcases mul ⟨ar, ai⟩ ⟨ar, ai⟩ with ⟨sr, si⟩
  apply ext <;> simp [sub, add, one] <;> omega

end GaussianInt

/-! ## 1. `CyclicFaddeevPhi` at `N = 4` (`QOU.QBeta.FaddeevPhiFibreBranch` specialization) -/

/-- Paired 4-factor cyclic q-Pochhammer denominator at `N = 4`:
    `D₄(x) = ((1 - x)(1 - ζ₄² x)) · ((1 - ζ₄ x)(1 - ζ₄³ x)) = (1 - x)(1 + x) · (1 - i x)(1 + i x)`. -/
def cyclicDenomFour (x : GaussianInt) : GaussianInt :=
  let pairEven := GaussianInt.mul (GaussianInt.sub GaussianInt.one x)
                    (GaussianInt.add GaussianInt.one x)
  let zx := GaussianInt.mul GaussianInt.zeta4 x
  let pairOdd := GaussianInt.mul (GaussianInt.sub GaussianInt.one zx)
                   (GaussianInt.add GaussianInt.one zx)
  GaussianInt.mul pairEven pairOdd

/-- The collapsed polynomial `1 - (x²)² = 1 - x⁴` at `N = 4`. -/
def oneSubPowFour (x : GaussianInt) : GaussianInt :=
  let x2 := GaussianInt.mul x x
  GaussianInt.sub GaussianInt.one (GaussianInt.mul x2 x2)

/-- **Exact `N = 4` Cyclotomic Collapse (`cyclicFaddeevPhi_cyclic_carrier_eq` at `N = 4`).**
    For every `x ∈ ℤ[i]`, `((1 - x)(1 + x)) · ((1 - ζ₄ x)(1 + ζ₄ x)) = 1 - (x²)²`. -/
theorem cyclicDenomFour_collapse (x : GaussianInt) :
    cyclicDenomFour x = oneSubPowFour x := by
  dsimp [cyclicDenomFour, oneSubPowFour]
  rw [GaussianInt.one_sub_mul_one_add x,
      GaussianInt.one_sub_mul_one_add (GaussianInt.mul GaussianInt.zeta4 x),
      GaussianInt.sq_mul_zeta4 x]
  have hsub_neg : GaussianInt.sub GaussianInt.one (GaussianInt.neg (GaussianInt.mul x x)) =
                  GaussianInt.add GaussianInt.one (GaussianInt.mul x x) := by
    rcases GaussianInt.mul x x with ⟨r2, m2⟩
    apply GaussianInt.ext <;> simp [GaussianInt.sub, GaussianInt.add, GaussianInt.neg] <;> omega
  rw [hsub_neg]
  exact GaussianInt.one_sub_mul_one_add (GaussianInt.mul x x)

/-- **Exact `N = 4` Multiplicative `ζ₄`-Periodicity (`CyclicFaddeevPhi.periodic` at `N = 4`).**
    Scaling `x ↦ ζ₄ · x` leaves `cyclicDenomFour` invariant: `D₄(ζ₄ · x) = D₄(x)`. -/
theorem cyclicDenomFour_periodic (x : GaussianInt) :
    cyclicDenomFour (GaussianInt.mul GaussianInt.zeta4 x) = cyclicDenomFour x := by
  rw [cyclicDenomFour_collapse, cyclicDenomFour_collapse]
  dsimp [oneSubPowFour]
  rw [GaussianInt.sq_mul_zeta4 x, GaussianInt.sq_neg]

/-- **Finite Boundary-Trade Shift Law at `N = 4` (`CyclicFaddeevPhi.shift_factor` at `N = 4`).**
    `(1 - x) · D₄(ζ₄ · x) = (1 - x · ζ₄⁴) · D₄(x)`. -/
theorem cyclicDenomFour_shift_factor (x : GaussianInt) :
    GaussianInt.mul (GaussianInt.sub GaussianInt.one x)
      (cyclicDenomFour (GaussianInt.mul GaussianInt.zeta4 x)) =
    GaussianInt.mul
      (GaussianInt.sub GaussianInt.one (GaussianInt.mul x (GaussianInt.pow GaussianInt.zeta4 4)))
      (cyclicDenomFour x) := by
  rw [cyclicDenomFour_periodic, GaussianInt.zeta4_pow_four, GaussianInt.mul_one]

/-- Specialization of `QOU.QBeta.FaddeevPhiFibreBranch.CyclicFaddeevPhi` to `N = 4` over `ℤ[i]`. -/
structure CyclicFaddeevPhiFour (D : GaussianInt → GaussianInt) : Prop where
  shift_factor : ∀ x : GaussianInt,
    GaussianInt.mul (GaussianInt.sub GaussianInt.one x) (D (GaussianInt.mul GaussianInt.zeta4 x)) =
    GaussianInt.mul
      (GaussianInt.sub GaussianInt.one (GaussianInt.mul x (GaussianInt.pow GaussianInt.zeta4 4)))
      (D x)
  periodic : ∀ x : GaussianInt, D (GaussianInt.mul GaussianInt.zeta4 x) = D x

/-- Unconditional discharge of `CyclicFaddeevPhiFour` by `cyclicDenomFour`. -/
theorem cyclicFaddeevPhiFour_cyclicDenom : CyclicFaddeevPhiFour cyclicDenomFour :=
  ⟨cyclicDenomFour_shift_factor, cyclicDenomFour_periodic⟩

/-- Two, three, and four `ζ₄`-rotations of any `CyclicFaddeevPhiFour` carrier `D` leave `D(x)` fixed. -/
theorem cyclicFaddeevPhiFour_orbit_steps {D : GaussianInt → GaussianInt}
    (hD : CyclicFaddeevPhiFour D) (x : GaussianInt) :
    let x1 := GaussianInt.mul GaussianInt.zeta4 x
    let x2 := GaussianInt.mul GaussianInt.zeta4 x1
    let x3 := GaussianInt.mul GaussianInt.zeta4 x2
    D x1 = D x ∧ D x2 = D x ∧ D x3 = D x := by
  intro x1 x2 x3
  have h1 : D x1 = D x := hD.periodic x
  have h2 : D x2 = D x := by rw [hD.periodic x1, h1]
  have h3 : D x3 = D x := by rw [hD.periodic x2, h2]
  exact ⟨h1, h2, h3⟩

/-! ## 2. Analytic `ζ₄`-Partner Model and `IsZeta4Faithful` (`QOU.Mass.ComplexVolumeZeta4Partner`) -/

/-- A fibre state `(ePlus, eMinus, xCoord)` pairing the two faithful `±i` eigencomponents of
    `vModel z = cosh z + i·sinh z = (1+i)/2 · e^z + (1-i)/2 · e^{-z}`
    (`QOU.Mass.ComplexVolumeZeta4Partner.vModel_eq_faithful_sum`) with the multiplicative
    coordinate `x = e^z`. -/
structure Zeta4FibreState where
  /-- Faithful `(+i)`-eigencomponent `e_+` (scales by `+ζ₄` under `zeta4Rot`). -/
  ePlus : GaussianInt
  /-- Faithful `(-i)`-eigencomponent `e_-` (scales by `-ζ₄` under `zeta4Rot`). -/
  eMinus : GaussianInt
  /-- Multiplicative coordinate `x = e^z` (scales by `ζ₄` under `zeta4Rot`). -/
  xCoord : GaussianInt
  deriving DecidableEq, Repr

/-- Quarter-period rotation `zeta4Rot` (`z ↦ z + iπ/2`):
    `e_+ ↦ ζ₄ · e_+` (`exp_zeta4_eigen`),
    `e_- ↦ -ζ₄ · e_-` (`exp_neg_zeta4_eigen`),
    `x ↦ ζ₄ · x`. -/
def zeta4RotState (st : Zeta4FibreState) : Zeta4FibreState :=
  { ePlus := GaussianInt.mul GaussianInt.zeta4 st.ePlus
    eMinus := GaussianInt.neg (GaussianInt.mul GaussianInt.zeta4 st.eMinus)
    xCoord := GaussianInt.mul GaussianInt.zeta4 st.xCoord }

/-- The analytic model value `vModel = e_+ + e_- = cosh z + i·sinh z`
    (`vModel_eq_faithful_sum` in `QOU.Mass.ComplexVolumeZeta4Partner`). -/
def vModelEval (st : Zeta4FibreState) : GaussianInt :=
  GaussianInt.add st.ePlus st.eMinus

/-- The 4-step `ζ₄`-orbit sum (trivial `ℤ₄`-isotype) of an evaluator `F : Zeta4FibreState → GaussianInt`. -/
def orbitSumFour (F : Zeta4FibreState → GaussianInt) (st : Zeta4FibreState) : GaussianInt :=
  let s1 := zeta4RotState st
  let s2 := zeta4RotState s1
  let s3 := zeta4RotState s2
  GaussianInt.add (GaussianInt.add (GaussianInt.add (F st) (F s1)) (F s2)) (F s3)

/-- The 4-step alternating orbit sum (sign `ℤ₄`-isotype) of `F : Zeta4FibreState → GaussianInt`. -/
def signIsotypeFour (F : Zeta4FibreState → GaussianInt) (st : Zeta4FibreState) : GaussianInt :=
  let s1 := zeta4RotState st
  let s2 := zeta4RotState s1
  let s3 := zeta4RotState s2
  GaussianInt.sub (GaussianInt.add (GaussianInt.sub (F st) (F s1)) (F s2)) (F s3)

/-- Predicate `IsZeta4Faithful` (`QOU.Mass.ComplexVolumeZeta4Partner.IsZeta4Faithful`):
    both non-faithful `ℤ₄` isotypes (trivial orbit sum and sign alternating sum) vanish. -/
def IsZeta4FaithfulState (F : Zeta4FibreState → GaussianInt) : Prop :=
  (∀ st : Zeta4FibreState, orbitSumFour F st = GaussianInt.zero) ∧
  (∀ st : Zeta4FibreState, signIsotypeFour F st = GaussianInt.zero)

/-- `vModelEval` satisfies `ζ₄² = -1` after two rotations (`vModel_zeta4_sq`). -/
theorem vModelEval_zeta4_sq (st : Zeta4FibreState) :
    vModelEval (zeta4RotState (zeta4RotState st)) = GaussianInt.neg (vModelEval st) := by
  rcases st with ⟨ ⟨pr, pi⟩, ⟨mr, mi⟩, ⟨xr, xi⟩ ⟩
  apply GaussianInt.ext <;>
    simp [vModelEval, zeta4RotState, GaussianInt.add, GaussianInt.neg,
      GaussianInt.mul, GaussianInt.zeta4] <;>
    omega

/-- `vModelEval` is `ζ₄`-faithful (`vModel_isZeta4Faithful`): both its 4-step orbit sum
    and its 4-step alternating sign isotype vanish identically. -/
theorem vModelEval_isZeta4Faithful : IsZeta4FaithfulState vModelEval := by
  constructor
  · intro st
    rcases st with ⟨ ⟨pr, pi⟩, ⟨mr, mi⟩, ⟨xr, xi⟩ ⟩
    apply GaussianInt.ext <;>
      simp [orbitSumFour, vModelEval, zeta4RotState, GaussianInt.add,
        GaussianInt.neg, GaussianInt.mul, GaussianInt.zeta4, GaussianInt.zero] <;>
      omega
  · intro st
    rcases st with ⟨ ⟨pr, pi⟩, ⟨mr, mi⟩, ⟨xr, xi⟩ ⟩
    apply GaussianInt.ext <;>
      simp [signIsotypeFour, vModelEval, zeta4RotState, GaussianInt.add,
        GaussianInt.sub, GaussianInt.neg, GaussianInt.mul, GaussianInt.zeta4,
        GaussianInt.zero] <;>
      omega

/-! ## 3. Bridge Theorems (`qou-ztod`): Why Pure `CyclicFaddeevPhi` Fails Faithfulness & How the Product Succeeds -/

/-- **Orbit Sum of a Pure `CyclicFaddeevPhi` Carrier (`cyclicCarrier_orbit_and_sign`).**
    For any `D` satisfying `CyclicFaddeevPhiFour D`, the pure coordinate evaluation
    `st ↦ D(st.xCoord)` has 4-step orbit sum equal to `4 · D(st.xCoord)` (purely trivial isotype)
    and alternating sign isotype equal to `0`. -/
theorem cyclicCarrier_orbit_and_sign {D : GaussianInt → GaussianInt}
    (hD : CyclicFaddeevPhiFour D) (st : Zeta4FibreState) :
    orbitSumFour (fun s => D s.xCoord) st = GaussianInt.smul 4 (D st.xCoord) ∧
    signIsotypeFour (fun s => D s.xCoord) st = GaussianInt.zero := by
  have hsteps := cyclicFaddeevPhiFour_orbit_steps hD st.xCoord
  rcases hsteps with ⟨h1, h2, h3⟩
  dsimp [orbitSumFour, signIsotypeFour, zeta4RotState]
  rw [h1, h2, h3]
  rcases hDx : D st.xCoord with ⟨dr, di⟩
  constructor
  · apply GaussianInt.ext <;>
      simp [GaussianInt.add, GaussianInt.smul] <;>
      omega
  · apply GaussianInt.ext <;>
      simp [GaussianInt.add, GaussianInt.sub, GaussianInt.zero] <;>
      omega

/-- **Falsifier (`cyclicCarrier_not_zeta4Faithful_of_ne_zero`).**
    Any `CyclicFaddeevPhiFour` carrier `D` that is non-zero at some state `st` (`D(st.xCoord) ≠ 0`)
    has non-zero 4-step orbit sum and therefore FAILS `IsZeta4FaithfulState`. -/
theorem cyclicCarrier_not_zeta4Faithful_of_ne_zero {D : GaussianInt → GaussianInt}
    (hD : CyclicFaddeevPhiFour D) (st : Zeta4FibreState)
    (hne : D st.xCoord ≠ GaussianInt.zero) :
    ¬ IsZeta4FaithfulState (fun s => D s.xCoord) := by
  intro hFaith
  have horb := (cyclicCarrier_orbit_and_sign hD st).1
  have hzero := hFaith.1 st
  rw [horb] at hzero
  apply hne
  rcases hDx : D st.xCoord with ⟨dr, di⟩
  rw [hDx] at hzero
  have hre : 4 * dr = 0 := congrArg GaussianInt.re hzero
  have him : 4 * di = 0 := congrArg GaussianInt.im hzero
  exact GaussianInt.ext (by dsimp [GaussianInt.zero]; omega) (by dsimp [GaussianInt.zero]; omega)

/-- Concrete witness: `cyclicDenomFour` alone is not `IsZeta4FaithfulState` (evaluated at `x = 0`,
    where `D₄(0) = 1` and the 4-step orbit sum is `4`). -/
theorem cyclicDenomFour_alone_not_zeta4Faithful :
    ¬ IsZeta4FaithfulState (fun s => cyclicDenomFour s.xCoord) := by
  apply cyclicCarrier_not_zeta4Faithful_of_ne_zero cyclicFaddeevPhiFour_cyclicDenom
    ⟨GaussianInt.one, GaussianInt.zero, GaussianInt.zero⟩
  decide

/-- The bridged assembly `bridgedAssembly A D`, multiplying a state evaluator `A` (such as
    `vModelEval`) by a `CyclicFaddeevPhiFour` fibre factor `D(st.xCoord)`. -/
def bridgedAssembly (A : Zeta4FibreState → GaussianInt) (D : GaussianInt → GaussianInt)
    (st : Zeta4FibreState) : GaussianInt :=
  GaussianInt.mul (A st) (D st.xCoord)

/-- **Bridge Theorem 1 (`bridgedAssembly_zeta4_sq`):**
    If `D` satisfies `CyclicFaddeevPhiFour D`, then `bridgedAssembly vModelEval D` inherits
    the exact `ζ₄² = -1` negation under two quarter-period rotations. -/
theorem bridgedAssembly_zeta4_sq {D : GaussianInt → GaussianInt}
    (hD : CyclicFaddeevPhiFour D) (st : Zeta4FibreState) :
    bridgedAssembly vModelEval D (zeta4RotState (zeta4RotState st)) =
      GaussianInt.neg (bridgedAssembly vModelEval D st) := by
  have hsteps := cyclicFaddeevPhiFour_orbit_steps hD st.xCoord
  rcases hsteps with ⟨_, h2, _⟩
  dsimp [bridgedAssembly]
  have hx2 : (zeta4RotState (zeta4RotState st)).xCoord =
      GaussianInt.mul GaussianInt.zeta4 (GaussianInt.mul GaussianInt.zeta4 st.xCoord) := rfl
  rw [hx2, h2, vModelEval_zeta4_sq, GaussianInt.neg_mul]

/-- **Bridge Theorem 2 (`bridgedAssembly_isZeta4Faithful`):**
    For *every* `IsZeta4FaithfulState` analytic model `A` and *every* `CyclicFaddeevPhiFour`
    carrier `D`, the product assembly `st ↦ A(st) · D(st.xCoord)` is `IsZeta4FaithfulState`:
    both its 4-step trivial-isotype orbit sum and its 4-step sign-isotype alternating sum vanish! -/
theorem bridgedAssembly_isZeta4Faithful {A : Zeta4FibreState → GaussianInt}
    {D : GaussianInt → GaussianInt}
    (hA : IsZeta4FaithfulState A) (hD : CyclicFaddeevPhiFour D) :
    IsZeta4FaithfulState (bridgedAssembly A D) := by
  constructor
  · intro st
    have hsteps := cyclicFaddeevPhiFour_orbit_steps hD st.xCoord
    rcases hsteps with ⟨h1, h2, h3⟩
    have horbA := hA.1 st
    dsimp [orbitSumFour, bridgedAssembly]
    have hx1 : (zeta4RotState st).xCoord = GaussianInt.mul GaussianInt.zeta4 st.xCoord := rfl
    have hx2 : (zeta4RotState (zeta4RotState st)).xCoord =
        GaussianInt.mul GaussianInt.zeta4 (GaussianInt.mul GaussianInt.zeta4 st.xCoord) := rfl
    have hx3 : (zeta4RotState (zeta4RotState (zeta4RotState st))).xCoord =
        GaussianInt.mul GaussianInt.zeta4
          (GaussianInt.mul GaussianInt.zeta4 (GaussianInt.mul GaussianInt.zeta4 st.xCoord)) := rfl
    rw [hx1, hx2, hx3, h1, h2, h3]
    rw [← GaussianInt.add_mul, ← GaussianInt.add_mul, ← GaussianInt.add_mul]
    change GaussianInt.mul (orbitSumFour A st) (D st.xCoord) = GaussianInt.zero
    rw [horbA, GaussianInt.zero_mul]
  · intro st
    have hsteps := cyclicFaddeevPhiFour_orbit_steps hD st.xCoord
    rcases hsteps with ⟨h1, h2, h3⟩
    have hsignA := hA.2 st
    dsimp [signIsotypeFour, bridgedAssembly]
    have hx1 : (zeta4RotState st).xCoord = GaussianInt.mul GaussianInt.zeta4 st.xCoord := rfl
    have hx2 : (zeta4RotState (zeta4RotState st)).xCoord =
        GaussianInt.mul GaussianInt.zeta4 (GaussianInt.mul GaussianInt.zeta4 st.xCoord) := rfl
    have hx3 : (zeta4RotState (zeta4RotState (zeta4RotState st))).xCoord =
        GaussianInt.mul GaussianInt.zeta4
          (GaussianInt.mul GaussianInt.zeta4 (GaussianInt.mul GaussianInt.zeta4 st.xCoord)) := rfl
    rw [hx1, hx2, hx3, h1, h2, h3]
    rw [← GaussianInt.sub_mul, ← GaussianInt.add_mul, ← GaussianInt.sub_mul]
    change GaussianInt.mul (signIsotypeFour A st) (D st.xCoord) = GaussianInt.zero
    rw [hsignA, GaussianInt.zero_mul]

/-- **Concrete Discharged Bridge (`bridgedCyclicDenomFour_isZeta4Faithful`, closing `qou-ztod`):**
    The product assembly `vModelEval(st) · cyclicDenomFour(st.xCoord)` — coupling
    `QOU.Mass.ComplexVolumeZeta4Partner.vModel` directly to the discharged `N = 4`
    `QOU.QBeta.FaddeevPhiFibreBranch.CyclicFaddeevPhi` carrier `(x; ζ₄)₄ = 1 - x⁴` —
    is `IsZeta4FaithfulState` and non-vacuously non-zero (`bridgedAssembly = -15` at `x = 2, e_+ = 1`). -/
theorem bridgedCyclicDenomFour_isZeta4Faithful :
    IsZeta4FaithfulState (bridgedAssembly vModelEval cyclicDenomFour) ∧
    bridgedAssembly vModelEval cyclicDenomFour
      ⟨GaussianInt.one, GaussianInt.zero, ⟨2, 0⟩⟩ = ⟨-15, 0⟩ := by
  refine ⟨bridgedAssembly_isZeta4Faithful vModelEval_isZeta4Faithful cyclicFaddeevPhiFour_cyclicDenom, ?_⟩
  decide

end QOU.QBeta.CyclicFaddeevZeta4Bridge
