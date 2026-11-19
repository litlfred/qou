import QOU.Brings.CohomologicalGenusFourAndSymplecticEmbeddings
import QOU.Eightfold.RowCapObstruction
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Degree-3 Kummer Pushforward, Split Unimodular Gauge Algebra, Fractional Hypercharge, Anomaly Cancellation, Jimbo `N = 3` Schur–Weyl Action, and `3 / 8` UV Weinberg Angle

Unconditional Lean 4 formalization of the Wave-5 Standard Model algebraic package over Bring's
genus-4 curve (`QOU.Brings.CohomologicalGenusFourAndSymplecticEmbeddings`) and the `N = 3`
resolution of the eightfold-way row-cap obstruction (`QOU.Eightfold.RowCapObstruction`):

1. **§1 — Degree-3 Cyclic Kummer Pushforward and Split `12`-Dimensional Gauge Subalgebra:**
   - Connects `IsUniformChiralityZ3KummerCover 6 4` ($d = 3, b = 6, g = 4, \chi_{\mathrm{eu}} = -6$)
     to the degree-3 cyclic Kummer extension `KummerCubic R u` ($\cong R[t]/(t^3 - u)$).
   - Scalar restriction (`pushforward`) equips any rank-1 `KummerCubic R u`-module with an
     explicit `Fin 3`-indexed $R$-basis (`Module.finrank R (KummerCubic R u) = 3`), contrasting
     $\binom{3}{3} = 1$ (`weylDimAlt 3 = 1`) on $W_3$ with $\binom{2}{2} = 1, \binom{2}{3} = 0$
     (`weylDimAlt 2 = 0`) on the unramified base spinor $V_2$.
   - On the split fibre $F = V_2 \oplus W_3^* \cong K^2 \oplus K^3$, the split unimodular matrix
     subspace `splitUnimodularSubmodule K ≤ Matrix (Fin 5) (Fin 5) K` is closed under matrix
     commutator $[X, Y] = X Y - Y X$, has `Module.finrank K (splitUnimodularSubmodule K) = 12`
     ($8 + 3 + 1$), and has identically vanishing $(2, 3)$ and $(3, 2)$ leptoquark blocks
     (excluding all $24 - 12 = 12$ off-diagonal proton-decay generators of $\mathfrak{sl}_5$).

2. **§2 — Fractional Hypercharge Forcing, Exterior Chiral Generation, and Global `ℤ_6` Kernel:**
   - Block-scalar matrices $\mathrm{diag}(y_2 I_2, y_3 I_3)$ form the exact centralizer of
     $\mathfrak{gl}_2 \oplus \mathfrak{gl}_3$ inside block-diagonal `5 × 5` matrices, and
     tracelessness $2 y_2 + 3 y_3 = 0$ holds if and only if $y_3 = -(2/3) y_2$. Setting
     $y_2 = -1/2$ forces $y_3 = +1/3$ on $W_3^*$ ($-1/3$ on $W_3$).
   - Exterior-power additivity on $\Lambda^1(V_2 \oplus W_3^*) \oplus \Lambda^2(V_2^* \oplus W_3)$
     ($5 + 10 = 15$ Weyl states, $16$ with $\Lambda^0$) yields $L_L = (1, 2, -1/2)$,
     $d_R^c = (\bar{3}, 1, +1/3)$, $e_R^c = (1, 1, +1)$, $Q_L = (3, 2, +1/6)$, and
     $u_R^c = (\bar{3}, 1, -2/3)$, together with Gell-Mann–Nishijima electric charges $Q = T_3 + Y$.
   - In `ZMod 3 × ZMod 2 × ZMod 6`, the subgroup acting trivially on all five chiral multiplets
     is the cyclic image of `z6KernelEmbed : ZMod 6 → ZMod 3 × ZMod 2 × ZMod 6` of exact
     cardinality `6`, corresponding to $(SU(3)_c \times SU(2)_L \times U(1)_Y)/\mathbb{Z}_6$.

3. **§3 — Cancellation of All Five Gauge/Gravitational Anomalies and Hypercharge Uniqueness:**
   - Vanishing of $[SU(3)_c]^3$, $[SU(3)_c]^2 U(1)_Y$, $[SU(2)_L]^2 U(1)_Y$, $\mathrm{Tr}(Y)$,
     and $\mathrm{Tr}(Y^3)$ on $\mathcal{S}_{\mathrm{chiral}}$.
   - Over any characteristic-0 field $K$, eliminating the three linear anomaly constraints reduces
     $\mathrm{Tr}(Y^3)$ to $18\,Y_Q\,(4 Y_Q + Y_{u^c})\,(2 Y_Q - Y_{u^c})$, so $Y_L = -1/2$
     forces $Y_Q = 1/6$, $Y_{e^c} = 1$, and $(Y_{u^c}, Y_{d^c}) \in \{(-2/3, 1/3), (1/3, -2/3)\}$.

4. **§4 — Jimbo `N = 3` (`a = q³`) `R`-Matrix on `W_3 ⊗ W_3` and `3^⊗3` Singlet Survival:**
   - Explicit `9 × 9` braided Jimbo matrix `jimboR3 q qi` on `Fin 3 × Fin 3` satisfying both the
     Hecke quadratic `(R - q I)(R + q⁻¹ I) = 0` (`qi * q = 1`) and the `27 × 27` Yang–Baxter braid
     identity `R₁₂ R₂₃ R₁₂ = R₂₃ R₁₂ R₂₃` on `Fin 3 × Fin 3 × Fin 3`.
   - Quantum-weighted partial trace on the second factor evaluates to $q^5 \cdot I_{W_3}$, giving
     the HOMFLY-PT Markov parameter $z_3(q) = \frac{q^5}{q^4 + q^2 + 1} = \frac{q^3}{[3]_q}$.
   - On the three-strand $q$-antisymmetriser $e_{(1,1,1)} \in H_3(q)$, the $N = 2$ weight vanishes
     identically whereas the $N = 3$ weight equals $[3]_q^{-3} > 0$ for all real $q > 0$,
     matching the quantum Schur–Weyl identity $\dim_q V_{(3)} + 2 \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)} = [3]_q^3$
     and its $q = 1$ limit $10 + 16 + 1 = 27$.

5. **§5 — Canonical UV Weinberg Angle `sin² θ_W = 3 / 8` and `q`-Deformed Bounds:**
   - $\mathrm{Tr}(T_3^2) = 2$, $\mathrm{Tr}(Y^2) = 10/3$, $\mathrm{Tr}(Q^2) = 16/3$, giving
     $\sin^2\theta_W^{\mathrm{UV}} = \frac{\mathrm{Tr}(T_3^2)}{\mathrm{Tr}(T_3^2) + \mathrm{Tr}(Y^2)} = \frac{3}{8}$
     without off-diagonal $SU(5)$ gauge bosons, together with strict $(0, 1)$ bounds, bar
     invariance, and $q = 1$ limit $3/8$ for the quantum-dimension deformation `weinbergSinSqQ`.
-/

namespace QOU.StandardModel.BringPushforwardAndGaugeGroupUnification

open QOU.Brings.CohomologicalGenusFourAndSymplecticEmbeddings
open QOU.Eightfold.RowCapObstruction

-- ============================================================================
-- §1. Degree-3 Cyclic Kummer Pushforward W₃ = π_* 𝓛 & Split 12D Gauge Algebra
-- ============================================================================

/-- Connection to `CohomologicalGenusFourAndSymplecticEmbeddings`: the minimal hyperbolic
uniform-chirality $\mathbb{Z}_3$-Kummer cover of $\mathbb{P}^1$ has degree $d = 3$, branch count
$b = 6$, genus $g = 4$, Euler characteristic $\chi_{\mathrm{eu}} = -6$, and induces a non-empty
singlet exterior channel (`weylDimAlt 3 = 1`) unavailable on the rank-2 base (`weylDimAlt 2 = 0`). -/
theorem bring_kummer_cover_and_exterior_ranks :
    IsUniformChiralityZ3KummerCover 6 4 ∧
    topEulerChar 4 = -6 ∧
    Nat.choose 3 3 = 1 ∧
    weylDimAlt 3 = 1 ∧
    Nat.choose 2 2 = 1 ∧
    Nat.choose 2 3 = 0 ∧
    weylDimAlt 2 = 0 := by
  refine ⟨minimal_hyperbolic_z3_kummer_forces_genus_four.1, ?_, by decide, ?_, by decide,
    by decide, ?_⟩
  · decide
  · unfold weylDimAlt; decide
  · unfold weylDimAlt; decide

/-- Carrier of the degree-3 cyclic Kummer extension $R[t]/(t^3 - u)$ with $R$-basis $\{1, t, t^2\}$. -/
@[ext]
structure KummerCubic (R : Type*) (_u : R) where
  /-- Coefficient of $1$. -/
  c0 : R
  /-- Coefficient of $t$. -/
  c1 : R
  /-- Coefficient of $t^2$. -/
  c2 : R
  deriving DecidableEq

namespace KummerCubic

section RingAndModule

variable {R : Type*} [CommRing R] {u : R}

instance : Zero (KummerCubic R u) := ⟨⟨0, 0, 0⟩⟩
instance : One (KummerCubic R u) := ⟨⟨1, 0, 0⟩⟩

instance : Add (KummerCubic R u) :=
  ⟨fun a b => ⟨a.c0 + b.c0, a.c1 + b.c1, a.c2 + b.c2⟩⟩

instance : Neg (KummerCubic R u) :=
  ⟨fun a => ⟨-a.c0, -a.c1, -a.c2⟩⟩

instance : Sub (KummerCubic R u) :=
  ⟨fun a b => ⟨a.c0 - b.c0, a.c1 - b.c1, a.c2 - b.c2⟩⟩

instance : Mul (KummerCubic R u) :=
  ⟨fun a b =>
    ⟨a.c0 * b.c0 + u * (a.c1 * b.c2 + a.c2 * b.c1),
     a.c0 * b.c1 + a.c1 * b.c0 + u * (a.c2 * b.c2),
     a.c0 * b.c2 + a.c1 * b.c1 + a.c2 * b.c0⟩⟩

instance : SMul ℕ (KummerCubic R u) :=
  ⟨fun n a => ⟨n • a.c0, n • a.c1, n • a.c2⟩⟩

instance : SMul ℤ (KummerCubic R u) :=
  ⟨fun n a => ⟨n • a.c0, n • a.c1, n • a.c2⟩⟩

@[simp] theorem zero_c0 : (0 : KummerCubic R u).c0 = 0 := rfl
@[simp] theorem zero_c1 : (0 : KummerCubic R u).c1 = 0 := rfl
@[simp] theorem zero_c2 : (0 : KummerCubic R u).c2 = 0 := rfl
@[simp] theorem one_c0 : (1 : KummerCubic R u).c0 = 1 := rfl
@[simp] theorem one_c1 : (1 : KummerCubic R u).c1 = 0 := rfl
@[simp] theorem one_c2 : (1 : KummerCubic R u).c2 = 0 := rfl
@[simp] theorem add_c0 (a b : KummerCubic R u) : (a + b).c0 = a.c0 + b.c0 := rfl
@[simp] theorem add_c1 (a b : KummerCubic R u) : (a + b).c1 = a.c1 + b.c1 := rfl
@[simp] theorem add_c2 (a b : KummerCubic R u) : (a + b).c2 = a.c2 + b.c2 := rfl
@[simp] theorem neg_c0 (a : KummerCubic R u) : (-a).c0 = -a.c0 := rfl
@[simp] theorem neg_c1 (a : KummerCubic R u) : (-a).c1 = -a.c1 := rfl
@[simp] theorem neg_c2 (a : KummerCubic R u) : (-a).c2 = -a.c2 := rfl
@[simp] theorem sub_c0 (a b : KummerCubic R u) : (a - b).c0 = a.c0 - b.c0 := rfl
@[simp] theorem sub_c1 (a b : KummerCubic R u) : (a - b).c1 = a.c1 - b.c1 := rfl
@[simp] theorem sub_c2 (a b : KummerCubic R u) : (a - b).c2 = a.c2 - b.c2 := rfl
@[simp] theorem mul_c0 (a b : KummerCubic R u) :
    (a * b).c0 = a.c0 * b.c0 + u * (a.c1 * b.c2 + a.c2 * b.c1) := rfl
@[simp] theorem mul_c1 (a b : KummerCubic R u) :
    (a * b).c1 = a.c0 * b.c1 + a.c1 * b.c0 + u * (a.c2 * b.c2) := rfl
@[simp] theorem mul_c2 (a b : KummerCubic R u) :
    (a * b).c2 = a.c0 * b.c2 + a.c1 * b.c1 + a.c2 * b.c0 := rfl

instance : CommRing (KummerCubic R u) where
  add_assoc a b c := by ext <;> simp <;> ring
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  nsmul := (· • ·)
  nsmul_zero a := by ext <;> exact zero_nsmul _
  nsmul_succ n a := by ext <;> exact succ_nsmul _ n
  zsmul := (· • ·)
  zsmul_zero' a := by ext <;> exact zero_zsmul _
  zsmul_succ' n a := by ext <;> exact SubNegMonoid.zsmul_succ' n _
  zsmul_neg' n a := by ext <;> exact SubNegMonoid.zsmul_neg' n _
  sub_eq_add_neg a b := by ext <;> simp [sub_eq_add_neg]
  neg_add_cancel a := by ext <;> simp
  add_comm a b := by ext <;> simp [add_comm]
  left_distrib a b c := by ext <;> simp <;> ring
  right_distrib a b c := by ext <;> simp <;> ring
  zero_mul a := by ext <;> simp
  mul_zero a := by ext <;> simp
  mul_assoc a b c := by ext <;> simp <;> ring
  one_mul a := by ext <;> simp
  mul_one a := by ext <;> simp
  mul_comm a b := by ext <;> simp <;> ring

instance : SMul R (KummerCubic R u) :=
  ⟨fun r a => ⟨r * a.c0, r * a.c1, r * a.c2⟩⟩

@[simp] theorem smul_c0 (r : R) (a : KummerCubic R u) : (r • a).c0 = r * a.c0 := rfl
@[simp] theorem smul_c1 (r : R) (a : KummerCubic R u) : (r • a).c1 = r * a.c1 := rfl
@[simp] theorem smul_c2 (r : R) (a : KummerCubic R u) : (r • a).c2 = r * a.c2 := rfl

instance : Module R (KummerCubic R u) where
  one_smul a := by ext <;> exact one_mul _
  mul_smul r s a := by ext <;> exact mul_assoc r s _
  smul_zero r := by ext <;> exact mul_zero r
  smul_add r a b := by ext <;> exact mul_add r _ _
  add_smul r s a := by ext <;> exact add_mul r s _
  zero_smul a := by ext <;> exact zero_mul _

instance : Algebra R (KummerCubic R u) :=
  Algebra.ofModule
    (fun r a b => by ext <;> simp <;> ring)
    (fun r a b => by ext <;> simp <;> ring)

/-- Radical Kummer generator $t \in R[t]/(t^3 - u)$. -/
def gen (R : Type*) [CommRing R] (u : R) : KummerCubic R u := ⟨0, 1, 0⟩

/-- Defining Kummer relation $t^3 = u \cdot 1$ inside `KummerCubic R u`. -/
theorem gen_pow_three (u : R) :
    (gen R u) ^ 3 = algebraMap R (KummerCubic R u) u := by
  rw [pow_three, Algebra.algebraMap_eq_smul_one]
  ext <;> simp [gen]

/-- Cyclic $\mathbb{Z}_3$ deck-transformation endomorphism $t \mapsto \omega t$ for any $\omega \in R$
satisfying $\omega^3 = 1$. -/
def deckAut (u ω : R) (hω : ω ^ 3 = 1) : KummerCubic R u →ₐ[R] KummerCubic R u where
  toFun a := ⟨a.c0, ω * a.c1, ω ^ 2 * a.c2⟩
  map_one' := by ext <;> simp
  map_mul' a b := by
    ext <;> simp
    · linear_combination -u * (a.c1 * b.c2 + a.c2 * b.c1) * hω
    · linear_combination -u * a.c2 * b.c2 * ω * hω
    · ring
  map_zero' := by ext <;> simp
  map_add' a b := by ext <;> simp <;> ring
  commutes' r := by
    rw [Algebra.algebraMap_eq_smul_one]
    ext <;> simp

/-- Threefold iteration of `deckAut` is the identity ($\mathbb{Z}_3$ deck group). -/
theorem deckAut_cubed_id (u ω : R) (hω : ω ^ 3 = 1) (a : KummerCubic R u) :
    deckAut u ω hω (deckAut u ω hω (deckAut u ω hω a)) = a := by
  apply KummerCubic.ext
  · rfl
  · dsimp [deckAut]
    linear_combination a.c1 * hω
  · dsimp [deckAut]
    linear_combination a.c2 * (ω ^ 3 + 1) * hω

/-- Explicit $R$-linear pushforward isomorphism identifying the rank-1 `KummerCubic R u`-module
with the rank-3 free $R$-module $W_3 = (\mathrm{Fin}\,3 \to R)$. -/
def pushforwardEquiv (u : R) : KummerCubic R u ≃ₗ[R] (Fin 3 → R) where
  toFun a := ![a.c0, a.c1, a.c2]
  invFun f := ⟨f 0, f 1, f 2⟩
  map_add' a b := by
    funext i; fin_cases i <;> rfl
  map_smul' r a := by
    funext i; fin_cases i <;> rfl
  left_inv a := by ext <;> rfl
  right_inv f := by
    funext i; fin_cases i <;> rfl

/-- Explicit `Fin 3`-indexed $R$-basis $\{1, t, t^2\}$ of the pushed-forward rank-1 Kummer bundle. -/
noncomputable def pushforwardBasis (u : R) : Module.Basis (Fin 3) R (KummerCubic R u) :=
  (Pi.basisFun R (Fin 3)).map (pushforwardEquiv u).symm

/-- **Rank-3 pushforward theorem:** scalar restriction of a rank-1 `KummerCubic R u`-module has
exact $R$-rank $3$. -/
theorem finrank_pushforward [StrongRankCondition R] (u : R) :
    Module.finrank R (KummerCubic R u) = 3 := by
  rw [Module.finrank_eq_card_basis (pushforwardBasis u), Fintype.card_fin]

end RingAndModule

end KummerCubic

section SplitGaugeAlgebra

/-- Matrix commutator $[X, Y] = X Y - Y X$. -/
def matComm {n R : Type*} [Fintype n] [DecidableEq n] [Ring R]
    (X Y : Matrix n n R) : Matrix n n R :=
  X * Y - Y * X

/-- Explicit sum of diagonal entries for $2 \times 2$, $3 \times 3$, and $5 \times 5$ matrices. -/
def tr2 {R : Type*} [AddCommMonoid R] (A : Matrix (Fin 2) (Fin 2) R) : R :=
  A 0 0 + A 1 1

def tr3 {R : Type*} [AddCommMonoid R] (B : Matrix (Fin 3) (Fin 3) R) : R :=
  B 0 0 + B 1 1 + B 2 2

def tr5 {R : Type*} [AddCommMonoid R] (M : Matrix (Fin 5) (Fin 5) R) : R :=
  M 0 0 + M 1 1 + M 2 2 + M 3 3 + M 4 4

/-- Block-diagonal embedding of $(A_2, A_3) \in M_2(R) \times M_3(R)$ into $M_5(R)$ along the
split fibre $F = V_2 \oplus W_3^* \cong R^2 \oplus R^3$. -/
def blockDiag2x3 {R : Type*} [Zero R]
    (A : Matrix (Fin 2) (Fin 2) R) (B : Matrix (Fin 3) (Fin 3) R) :
    Matrix (Fin 5) (Fin 5) R :=
  fun i j =>
    if hi : i.val < 2 then
      if hj : j.val < 2 then A ⟨i.val, hi⟩ ⟨j.val, hj⟩ else 0
    else
      if hj : j.val < 2 then 0
      else B ⟨i.val - 2, by omega⟩ ⟨j.val - 2, by omega⟩

theorem blockDiag2x3_mul {R : Type*} [Semiring R]
    (A₁ A₂ : Matrix (Fin 2) (Fin 2) R) (B₁ B₂ : Matrix (Fin 3) (Fin 3) R) :
    blockDiag2x3 A₁ B₁ * blockDiag2x3 A₂ B₂ = blockDiag2x3 (A₁ * A₂) (B₁ * B₂) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [blockDiag2x3, Matrix.mul_apply, Fin.sum_univ_five, Fin.sum_univ_two, Fin.sum_univ_three]

theorem blockDiag2x3_sub {R : Type*} [Ring R]
    (A₁ A₂ : Matrix (Fin 2) (Fin 2) R) (B₁ B₂ : Matrix (Fin 3) (Fin 3) R) :
    blockDiag2x3 A₁ B₁ - blockDiag2x3 A₂ B₂ = blockDiag2x3 (A₁ - A₂) (B₁ - B₂) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [blockDiag2x3]

/-- Block-diagonal matrices preserve the split structure under matrix commutator. -/
theorem blockDiag2x3_matComm {R : Type*} [Ring R]
    (A₁ A₂ : Matrix (Fin 2) (Fin 2) R) (B₁ B₂ : Matrix (Fin 3) (Fin 3) R) :
    matComm (blockDiag2x3 A₁ B₁) (blockDiag2x3 A₂ B₂) =
      blockDiag2x3 (matComm A₁ A₂) (matComm B₁ B₂) := by
  unfold matComm
  rw [blockDiag2x3_mul, blockDiag2x3_mul, blockDiag2x3_sub]

/-- Additivity of trace across `blockDiag2x3`: $\mathrm{tr}_5(A_2 \oplus A_3) = \mathrm{tr}_2(A_2) + \mathrm{tr}_3(A_3)$. -/
theorem tr5_blockDiag2x3 {R : Type*} [AddCommMonoid R]
    (A : Matrix (Fin 2) (Fin 2) R) (B : Matrix (Fin 3) (Fin 3) R) :
    tr5 (blockDiag2x3 A B) = tr2 A + tr3 B := by
  unfold tr5 tr2 tr3 blockDiag2x3
  dsimp
  abel

/-- Trace of any $5 \times 5$ commutator over a commutative ring vanishes. -/
theorem tr5_matComm_eq_zero {R : Type*} [CommRing R] (X Y : Matrix (Fin 5) (Fin 5) R) :
    tr5 (matComm X Y) = 0 := by
  unfold tr5 matComm
  simp only [Matrix.sub_apply, Matrix.mul_apply, Fin.sum_univ_five]
  ring

/-- Predicate cutting out the split unimodular gauge algebra inside $M_5(R)$: all off-diagonal
$(2, 3)$ and $(3, 2)$ leptoquark entries vanish, and $\mathrm{tr}_5(M) = 0$. -/
def IsSplitUnimodular5 {R : Type*} [AddCommMonoid R] (M : Matrix (Fin 5) (Fin 5) R) : Prop :=
  (∀ i j : Fin 5, (i.val < 2 ↔ ¬ j.val < 2) → M i j = 0) ∧ tr5 M = 0

/-- Every split-block matrix `M` equals `blockDiag2x3` of its upper-left $2 \times 2$ and
lower-right $3 \times 3$ blocks. -/
theorem eq_blockDiag2x3_of_no_leptoquark {R : Type*} [Zero R] (M : Matrix (Fin 5) (Fin 5) R)
    (h0 : ∀ i j : Fin 5, (i.val < 2 ↔ ¬ j.val < 2) → M i j = 0) :
    M = blockDiag2x3 (fun a b => M ⟨a.val, by omega⟩ ⟨b.val, by omega⟩)
      (fun a b => M ⟨a.val + 2, by omega⟩ ⟨b.val + 2, by omega⟩) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    first
    | rfl
    | exact h0 _ _ (by decide)

/-- The split unimodular gauge algebra as a `K`-submodule of `Matrix (Fin 5) (Fin 5) K`. -/
def splitUnimodularSubmodule (K : Type*) [Field K] :
    Submodule K (Matrix (Fin 5) (Fin 5) K) where
  carrier := {M | IsSplitUnimodular5 M}
  zero_mem' := ⟨fun _ _ _ => rfl, by simp [tr5]⟩
  add_mem' {X Y} hX hY := by
    refine ⟨fun i j hij => ?_, ?_⟩
    · simp [hX.1 i j hij, hY.1 i j hij]
    · have hXtr : tr5 X = 0 := hX.2
      have hYtr : tr5 Y = 0 := hY.2
      unfold tr5 at hXtr hYtr ⊢
      simp only [Matrix.add_apply]
      linear_combination hXtr + hYtr
  smul_mem' c {X} hX := by
    refine ⟨fun i j hij => ?_, ?_⟩
    · simp [hX.1 i j hij]
    · have hXtr : tr5 X = 0 := hX.2
      unfold tr5 at hXtr ⊢
      simp only [Matrix.smul_apply, smul_eq_mul]
      linear_combination c * hXtr

theorem blockDiag2x3_no_leptoquark {R : Type*} [Zero R]
    (A : Matrix (Fin 2) (Fin 2) R) (B : Matrix (Fin 3) (Fin 3) R)
    (i j : Fin 5) (hij : i.val < 2 ↔ ¬ j.val < 2) :
    blockDiag2x3 A B i j = 0 := by
  unfold blockDiag2x3
  by_cases hi : i.val < 2
  · rw [dif_pos hi, dif_neg (hij.mp hi)]
  · have hj : j.val < 2 := Classical.not_not.mp (mt hij.mpr hi)
    rw [dif_neg hi, dif_pos hj]

/-- **Lie-subalgebra closure:** `splitUnimodularSubmodule K` is closed under the matrix commutator
`[X, Y] = X Y - Y X` inside $\mathfrak{sl}_5(K)$. -/
theorem splitUnimodular_matComm_mem {K : Type*} [Field K]
    {X Y : Matrix (Fin 5) (Fin 5) K}
    (hX : X ∈ splitUnimodularSubmodule K) (hY : Y ∈ splitUnimodularSubmodule K) :
    matComm X Y ∈ splitUnimodularSubmodule K := by
  refine ⟨?_, tr5_matComm_eq_zero X Y⟩
  rw [eq_blockDiag2x3_of_no_leptoquark X hX.1,
      eq_blockDiag2x3_of_no_leptoquark Y hY.1,
      blockDiag2x3_matComm]
  exact blockDiag2x3_no_leptoquark _ _

/-- Explicit `12`-parameter coordinate chart on `splitUnimodularSubmodule K`:
indices `0..2` span $\mathfrak{sl}_2(K)$, indices `3..10` span $\mathfrak{sl}_3(K)$, and index `11`
spans the traceless hypercharge generator (`M 4 4 = -(M 0 0 + M 1 1 + M 2 2 + M 3 3)`). -/
def splitUnimodularFromCoords {K : Type*} [Field K] (v : Fin 12 → K) :
    Matrix (Fin 5) (Fin 5) K :=
  blockDiag2x3
    !![v 0, v 1;
       v 2, v 11 - v 0]
    !![v 3, v 4, v 5;
       v 6, v 7, v 8;
       v 9, v 10, -(v 11 + v 3 + v 7)]

theorem splitUnimodularFromCoords_mem {K : Type*} [Field K] (v : Fin 12 → K) :
    splitUnimodularFromCoords v ∈ splitUnimodularSubmodule K := by
  refine ⟨blockDiag2x3_no_leptoquark _ _, ?_⟩
  unfold splitUnimodularFromCoords
  rw [tr5_blockDiag2x3]
  unfold tr2 tr3
  simp
  ring

/-- Inverse coordinate extraction on `splitUnimodularSubmodule K`. -/
def splitUnimodularToCoords {K : Type*} [Field K]
    (M : splitUnimodularSubmodule K) : Fin 12 → K :=
  ![M.1 0 0, M.1 0 1, M.1 1 0,
    M.1 2 2, M.1 2 3, M.1 2 4,
    M.1 3 2, M.1 3 3, M.1 3 4,
    M.1 4 2, M.1 4 3, M.1 0 0 + M.1 1 1]

/-- Linear isomorphism `(Fin 12 → K) ≃ₗ[K] splitUnimodularSubmodule K`. -/
def splitUnimodularEquiv (K : Type*) [Field K] :
    (Fin 12 → K) ≃ₗ[K] splitUnimodularSubmodule K where
  toFun v := ⟨splitUnimodularFromCoords v, splitUnimodularFromCoords_mem v⟩
  invFun M := splitUnimodularToCoords M
  map_add' u w := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [splitUnimodularFromCoords, blockDiag2x3] <;> ring
  map_smul' c u := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [splitUnimodularFromCoords, blockDiag2x3] <;> ring
  left_inv v := by
    funext k
    fin_cases k <;>
      simp [splitUnimodularToCoords, splitUnimodularFromCoords, blockDiag2x3]
  right_inv M := by
    rcases M with ⟨M, hlepto, htr⟩
    ext i j
    unfold tr5 at htr
    fin_cases i <;> fin_cases j
    -- upper-left 2x2
    · rfl
    · rfl
    · exact (hlepto 0 2 (by decide)).symm
    · exact (hlepto 0 3 (by decide)).symm
    · exact (hlepto 0 4 (by decide)).symm
    · rfl
    · simp [splitUnimodularFromCoords, splitUnimodularToCoords, blockDiag2x3]
    · exact (hlepto 1 2 (by decide)).symm
    · exact (hlepto 1 3 (by decide)).symm
    · exact (hlepto 1 4 (by decide)).symm
    -- rows 2, 3, 4
    · exact (hlepto 2 0 (by decide)).symm
    · exact (hlepto 2 1 (by decide)).symm
    · rfl
    · rfl
    · rfl
    · exact (hlepto 3 0 (by decide)).symm
    · exact (hlepto 3 1 (by decide)).symm
    · rfl
    · rfl
    · rfl
    · exact (hlepto 4 0 (by decide)).symm
    · exact (hlepto 4 1 (by decide)).symm
    · rfl
    · rfl
    · simp [splitUnimodularFromCoords, splitUnimodularToCoords, blockDiag2x3]
      linear_combination -htr

/-- **Exact dimension `12 = 8 + 3 + 1` of the split unimodular gauge Lie algebra** and absence of
all `12` off-diagonal leptoquark proton-decay generators (`24 - 12 = 12`). -/
theorem finrank_splitUnimodular_eq_twelve (K : Type*) [Field K] :
    Module.finrank K (splitUnimodularSubmodule K) = 12 ∧
    8 + 3 + 1 = 12 ∧
    (5 ^ 2 - 1) - 12 = 12 ∧
    ∀ M ∈ splitUnimodularSubmodule K,
      ∀ (i : Fin 2) (j : Fin 3),
        M ⟨i.val, by omega⟩ ⟨j.val + 2, by omega⟩ = 0 ∧
        M ⟨j.val + 2, by omega⟩ ⟨i.val, by omega⟩ = 0 := by
  refine ⟨?_, by decide, by decide, ?_⟩
  · rw [← LinearEquiv.finrank_eq (splitUnimodularEquiv K), Module.finrank_fin_fun]
  · intro M hM i j
    fin_cases i <;> fin_cases j <;>
      exact ⟨hM.1 _ _ (by decide), hM.1 _ _ (by decide)⟩

end SplitGaugeAlgebra

-- ============================================================================
-- §2. Unimodular Hypercharge Quantization, Exterior Chiral Generation & ℤ_6
-- ============================================================================

section HyperchargeAndChiralGeneration

/-- Block-scalar hypercharge generator $\mathrm{diag}(y_2, y_2, y_3, y_3, y_3) \in M_5(R)$. -/
def hyperchargeDiag {R : Type*} [Semiring R] (y2 y3 : R) : Matrix (Fin 5) (Fin 5) R :=
  blockDiag2x3 (y2 • (1 : Matrix (Fin 2) (Fin 2) R)) (y3 • (1 : Matrix (Fin 3) (Fin 3) R))

/-- **Exact centralizer characterization:** a split matrix `blockDiag2x3 D₂ D₃` commutes with every
`blockDiag2x3 A₂ A₃` if and only if it has the block-scalar form `hyperchargeDiag y2 y3`. -/
theorem commutes_all_split_iff_hyperchargeDiag {K : Type*} [Field K]
    (D₂ : Matrix (Fin 2) (Fin 2) K) (D₃ : Matrix (Fin 3) (Fin 3) K) :
    (∀ (A₂ : Matrix (Fin 2) (Fin 2) K) (A₃ : Matrix (Fin 3) (Fin 3) K),
      matComm (blockDiag2x3 D₂ D₃) (blockDiag2x3 A₂ A₃) = 0) ↔
    ∃ y2 y3 : K, blockDiag2x3 D₂ D₃ = hyperchargeDiag y2 y3 := by
  constructor
  · intro hcomm
    refine ⟨D₂ 0 0, D₃ 0 0, ?_⟩
    have h2 : ∀ A₂ : Matrix (Fin 2) (Fin 2) K, D₂ * A₂ = A₂ * D₂ := by
      intro A₂
      have h := hcomm A₂ 0
      rw [blockDiag2x3_matComm] at h
      ext a b
      have hab := congrFun (congrFun h ⟨a.val, by omega⟩) ⟨b.val, by omega⟩
      simpa [blockDiag2x3, matComm, sub_eq_zero] using hab
    have h3 : ∀ A₃ : Matrix (Fin 3) (Fin 3) K, D₃ * A₃ = A₃ * D₃ := by
      intro A₃
      have h := hcomm 0 A₃
      rw [blockDiag2x3_matComm] at h
      ext a b
      have hab := congrFun (congrFun h ⟨a.val + 2, by omega⟩) ⟨b.val + 2, by omega⟩
      simpa [blockDiag2x3, matComm, sub_eq_zero] using hab
    have hD2_01 : D₂ 0 1 = 0 := by
      have := congrFun (congrFun (h2 !![1, 0; 0, 0]) 0) 1
      simpa [Matrix.mul_apply, Fin.sum_univ_two] using this.symm
    have hD2_10 : D₂ 1 0 = 0 := by
      have := congrFun (congrFun (h2 !![1, 0; 0, 0]) 1) 0
      simpa [Matrix.mul_apply, Fin.sum_univ_two] using this
    have hD2_11 : D₂ 1 1 = D₂ 0 0 := by
      have := congrFun (congrFun (h2 !![0, 1; 1, 0]) 0) 1
      simpa [Matrix.mul_apply, Fin.sum_univ_two] using this.symm
    have hD3_01 : D₃ 0 1 = 0 := by
      have := congrFun (congrFun (h3 !![1, 0, 0; 0, 0, 0; 0, 0, 0]) 0) 1
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this.symm
    have hD3_02 : D₃ 0 2 = 0 := by
      have := congrFun (congrFun (h3 !![1, 0, 0; 0, 0, 0; 0, 0, 0]) 0) 2
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this.symm
    have hD3_10 : D₃ 1 0 = 0 := by
      have := congrFun (congrFun (h3 !![1, 0, 0; 0, 0, 0; 0, 0, 0]) 1) 0
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this
    have hD3_12 : D₃ 1 2 = 0 := by
      have := congrFun (congrFun (h3 !![0, 0, 0; 0, 1, 0; 0, 0, 0]) 1) 2
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this.symm
    have hD3_20 : D₃ 2 0 = 0 := by
      have := congrFun (congrFun (h3 !![1, 0, 0; 0, 0, 0; 0, 0, 0]) 2) 0
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this
    have hD3_21 : D₃ 2 1 = 0 := by
      have := congrFun (congrFun (h3 !![0, 0, 0; 0, 1, 0; 0, 0, 0]) 2) 1
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this
    have hD3_11 : D₃ 1 1 = D₃ 0 0 := by
      have := congrFun (congrFun (h3 !![0, 1, 0; 1, 0, 0; 0, 0, 0]) 0) 1
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this.symm
    have hD3_22 : D₃ 2 2 = D₃ 0 0 := by
      have := congrFun (congrFun (h3 !![0, 0, 1; 0, 0, 0; 1, 0, 0]) 0) 2
      simpa [Matrix.mul_apply, Fin.sum_univ_three] using this.symm
    unfold hyperchargeDiag
    congr 1
    · ext a b; fin_cases a <;> fin_cases b <;> simp_all
    · ext a b; fin_cases a <;> fin_cases b <;> simp_all
  · rintro ⟨y2, y3, hEq⟩ A₂ A₃
    rw [hEq]
    unfold hyperchargeDiag
    rw [blockDiag2x3_matComm]
    have hc2 : matComm (y2 • (1 : Matrix (Fin 2) (Fin 2) K)) A₂ = 0 := by
      simp [matComm]
    have hc3 : matComm (y3 • (1 : Matrix (Fin 3) (Fin 3) K)) A₃ = 0 := by
      simp [matComm]
    rw [hc2, hc3]
    ext i j; fin_cases i <;> fin_cases j <;> rfl

/-- **Fractional Hypercharge Forcing:** over any characteristic-0 field $K$, unimodularity
$\mathrm{tr}_5(\mathrm{hyperchargeDiag}(y_2, y_3)) = 0$ holds iff $y_3 = -(2/3) y_2$; setting
$y_2 = -1/2$ uniquely forces $y_3 = +1/3$ on $W_3^*$ (and $-1/3$ on $W_3$). -/
theorem hypercharge_traceless_iff {K : Type*} [Field K] [CharZero K] (y2 y3 : K) :
    (tr5 (hyperchargeDiag y2 y3) = 0 ↔ y3 = -(2 / 3 : K) * y2) ∧
    (tr5 (hyperchargeDiag (-1 / 2 : K) y3) = 0 ↔ y3 = (1 / 3 : K)) := by
  have htr : ∀ a b : K, tr5 (hyperchargeDiag a b) = 2 * a + 3 * b := by
    intro a b
    unfold hyperchargeDiag
    rw [tr5_blockDiag2x3]
    unfold tr2 tr3
    simp
    ring
  rw [htr y2 y3, htr (-1 / 2) y3]
  have h3ne : (3 : K) ≠ 0 := by norm_num
  constructor
  · constructor
    · intro h
      apply mul_left_cancel₀ h3ne
      linear_combination h
    · intro h
      rw [h]
      ring
  · constructor
    · intro h
      apply mul_left_cancel₀ h3ne
      linear_combination h
    · intro h
      rw [h]
      norm_num

/-- The five left-handed Weyl multiplets of one Standard Model generation carried by
$\mathcal{S}_{\mathrm{chiral}} = \Lambda^1(V_2 \oplus W_3^*) \oplus \Lambda^2(V_2^* \oplus W_3)$. -/
inductive ChiralMultiplet where
  | LL
  | dRc
  | eRc
  | QL
  | uRc
  deriving DecidableEq, Fintype

/-- Color $SU(3)_c$ dimension $d_3$ of each multiplet in $\mathcal{S}_{\mathrm{chiral}}$. -/
def smColorDim : ChiralMultiplet → ℕ
  | .LL => 1
  | .dRc => 3
  | .eRc => 1
  | .QL => 3
  | .uRc => 3

/-- Weak $SU(2)_L$ dimension $d_2$ of each multiplet in $\mathcal{S}_{\mathrm{chiral}}$. -/
def smWeakDim : ChiralMultiplet → ℕ
  | .LL => 2
  | .dRc => 1
  | .eRc => 1
  | .QL => 2
  | .uRc => 1

/-- Total Weyl multiplicity $d_3 \cdot d_2$ of each multiplet. -/
def smWeylMult (m : ChiralMultiplet) : ℕ :=
  smColorDim m * smWeakDim m

/-- Exterior-power induced hypercharge on $\Lambda^1(V_2 \oplus W_3^*) \oplus \Lambda^2(V_2^* \oplus W_3)$
derived from a base doublet hypercharge $y_{V_2}$ and dual-triplet hypercharge $y_{W_3^*}$:
- $L_L \subset V_2$: $y_{V_2}$,
- $d_R^c \subset W_3^*$: $y_{W_3^*}$,
- $e_R^c = \Lambda^2 V_2^*$: $(-y_{V_2}) + (-y_{V_2})$,
- $Q_L = V_2^* \otimes W_3$: $(-y_{V_2}) + (-y_{W_3^*})$,
- $u_R^c = \Lambda^2 W_3$: $(-y_{W_3^*}) + (-y_{W_3^*})$. -/
def inducedExteriorHypercharge {K : Type*} [Ring K] (yV2 yW3Dual : K) : ChiralMultiplet → K
  | .LL => yV2
  | .dRc => yW3Dual
  | .eRc => (-yV2) + (-yV2)
  | .QL => (-yV2) + (-yW3Dual)
  | .uRc => (-yW3Dual) + (-yW3Dual)

/-- Standard Model hypercharges specialized at $(y_{V_2}, y_{W_3^*}) = (-1/2, +1/3)$. -/
noncomputable def smHypercharge {K : Type*} [Field K] (m : ChiralMultiplet) : K :=
  inducedExteriorHypercharge (-1 / 2 : K) (1 / 3 : K) m

/-- **Exterior chiral generation quantum numbers and Gell-Mann–Nishijima electric charges:**
1. The exterior sum $\Lambda^1(V_2 \oplus W_3^*) \oplus \Lambda^2(V_2^* \oplus W_3)$ has
   $5 + 10 = 15$ Weyl states ($16$ with $\Lambda^0$).
2. Evaluating `smHypercharge` yields $(-1/2, +1/3, +1, +1/6, -2/3)$ across
   $(L_L, d_R^c, e_R^c, Q_L, u_R^c)$.
3. Gell-Mann–Nishijima $Q = T_3 + Y$ yields $(0, -1)$ on $(\nu_L, e_L)$, $(+2/3, -1/3)$ on
   $(u_L, d_L)$, $-2/3$ on $u_R^c$, $+1/3$ on $d_R^c$, and $+1$ on $e_R^c$. -/
theorem exterior_chiral_generation_quantum_numbers {K : Type*} [Field K] [CharZero K] :
    (∑ m : ChiralMultiplet, smWeylMult m) = 15 ∧
    Nat.choose 5 1 + Nat.choose 5 2 = 15 ∧
    Nat.choose 5 0 + Nat.choose 5 1 + Nat.choose 5 2 = 16 ∧
    smHypercharge (K := K) .LL = -1 / 2 ∧
    smHypercharge (K := K) .dRc = 1 / 3 ∧
    smHypercharge (K := K) .eRc = 1 ∧
    smHypercharge (K := K) .QL = 1 / 6 ∧
    smHypercharge (K := K) .uRc = -2 / 3 ∧
    (1 / 2 : K) + smHypercharge .LL = 0 ∧
    (-1 / 2 : K) + smHypercharge .LL = -1 ∧
    (1 / 2 : K) + smHypercharge .QL = 2 / 3 ∧
    (-1 / 2 : K) + smHypercharge .QL = -1 / 3 := by
  refine ⟨by decide, by decide, by decide, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (unfold smHypercharge inducedExteriorHypercharge; norm_num)

/-- Integer $6Y$ charges of the five chiral multiplets (`-3, +2, +6, +1, -4`). -/
def sixTimesHypercharge : ChiralMultiplet → ℤ
  | .LL => -3
  | .dRc => 2
  | .eRc => 6
  | .QL => 1
  | .uRc => -4

/-- Signed $SU(3)_c$ triality exponent in units of $2\pi i / 6$ (`+2` on $3$, `-2` on $\bar{3}$,
`0` on singlets). -/
def su3PhaseCoeff6 : ChiralMultiplet → ZMod 6
  | .LL => 0
  | .dRc => -2
  | .eRc => 0
  | .QL => 2
  | .uRc => -2

/-- $SU(2)_L$ center exponent in units of $2\pi i / 6$ (`3` on doublets, `0` on singlets). -/
def su2PhaseCoeff6 : ChiralMultiplet → ZMod 6
  | .LL => 3
  | .dRc => 0
  | .eRc => 0
  | .QL => 3
  | .uRc => 0

/-- Total central phase in `ZMod 6` (units of $2\pi i / 6$) assigned to multiplet `m` by a
triple `(a, b, c) : ZMod 3 × ZMod 2 × ZMod 6` representing
$(e^{2\pi i a / 3} I_3,\; (-1)^b I_2,\; e^{2\pi i c / 6}) \in Z(SU(3)_c) \times Z(SU(2)_L) \times U(1)_Y$. -/
def centralPhaseOnMultiplet (t : ZMod 3 × ZMod 2 × ZMod 6) (m : ChiralMultiplet) : ZMod 6 :=
  su3PhaseCoeff6 m * (t.1.val : ZMod 6) +
    su2PhaseCoeff6 m * (t.2.1.val : ZMod 6) +
    (sixTimesHypercharge m : ZMod 6) * t.2.2

/-- Predicate asserting that `t ∈ ZMod 3 × ZMod 2 × ZMod 6` acts trivially on all five Standard
Model chiral multiplets. -/
def ActsTriviallyOnChiralGen (t : ZMod 3 × ZMod 2 × ZMod 6) : Prop :=
  ∀ m : ChiralMultiplet, centralPhaseOnMultiplet t m = 0

instance (t : ZMod 3 × ZMod 2 × ZMod 6) : Decidable (ActsTriviallyOnChiralGen t) := by
  unfold ActsTriviallyOnChiralGen
  infer_instance

/-- Canonical cyclic $\mathbb{Z}_6$ embedding $k \mapsto (k \bmod 3,\; k \bmod 2,\; k)$ into
`ZMod 3 × ZMod 2 × ZMod 6`. -/
def z6KernelEmbed (k : ZMod 6) : ZMod 3 × ZMod 2 × ZMod 6 :=
  ((k.val : ZMod 3), (k.val : ZMod 2), k)

/-- **Global $\mathbb{Z}_6$ Kernel Theorem (`G_SM ≅ (SU(3)_c × SU(2)_L × U(1)_Y) / ℤ_6`):**
1. `z6KernelEmbed` is injective and every `z6KernelEmbed k` ($k \in \mathrm{ZMod}\,6$) acts
   trivially on all five chiral multiplets.
2. Conversely, a central triple `t : ZMod 3 × ZMod 2 × ZMod 6` acts trivially on all five chiral
   multiplets if and only if `t` lies in the range of `z6KernelEmbed`.
3. The kernel subtype `{t : ZMod 3 × ZMod 2 × ZMod 6 // ActsTriviallyOnChiralGen t}` has exact
   cardinality `6`. -/
theorem global_z6_kernel_theorem :
    Function.Injective z6KernelEmbed ∧
    (∀ t : ZMod 3 × ZMod 2 × ZMod 6,
      ActsTriviallyOnChiralGen t ↔ ∃ k : ZMod 6, z6KernelEmbed k = t) ∧
    Fintype.card {t : ZMod 3 × ZMod 2 × ZMod 6 // ActsTriviallyOnChiralGen t} = 6 := by
  refine ⟨?_, ?_, by decide⟩
  · intro k₁ k₂ h
    exact congrArg (fun x => x.2.2) h
  · decide

end HyperchargeAndChiralGeneration

-- ============================================================================
-- §3. Cancellation of All 5 Gauge & Gravitational Anomalies + Uniqueness
-- ============================================================================

section AnomalyCancellationAndUniqueness

/-- Cubic $[SU(3)_c]^3$ anomaly index on $\mathcal{S}_{\mathrm{chiral}}$: two left-handed color
triplets ($Q_L$, index $+1$ each) and two left-handed anti-triplets ($u_R^c, d_R^c$, index $-1$
each). -/
def anomSU3Cube : ℤ := 2 * 1 + 1 * (-1) + 1 * (-1)

/-- Mixed $[SU(3)_c]^2 U(1)_Y$ anomaly polynomial $2 Y_Q + Y_{u^c} + Y_{d^c}$. -/
def anomSU3SqU1 {K : Type*} [Ring K] (yQ yUc yDc : K) : K :=
  2 * yQ + yUc + yDc

/-- Mixed $[SU(2)_L]^2 U(1)_Y$ anomaly polynomial $3 Y_Q + Y_L$. -/
def anomSU2SqU1 {K : Type*} [Ring K] (yQ yL : K) : K :=
  3 * yQ + yL

/-- Mixed gravitational–$U(1)_Y$ linear trace $6 Y_Q + 3 Y_{u^c} + 3 Y_{d^c} + 2 Y_L + Y_{e^c}$. -/
def anomGravU1 {K : Type*} [Ring K] (yQ yUc yDc yL yEc : K) : K :=
  6 * yQ + 3 * yUc + 3 * yDc + 2 * yL + yEc

/-- Cubic $[U(1)_Y]^3$ trace $6 Y_Q^3 + 3 Y_{u^c}^3 + 3 Y_{d^c}^3 + 2 Y_L^3 + Y_{e^c}^3$. -/
def anomU1Cube {K : Type*} [Ring K] (yQ yUc yDc yL yEc : K) : K :=
  6 * yQ ^ 3 + 3 * yUc ^ 3 + 3 * yDc ^ 3 + 2 * yL ^ 3 + yEc ^ 3

/-- **Exact cancellation of all five gauge and gravitational anomalies** for the induced exterior
hypercharges `smHypercharge` over any characteristic-0 field $K$ (and even prior to fixing
$y_{V_2}, y_{W_3^*}$ once $2 y_{V_2} + 3 y_{W_3^*} = 0$!). -/
theorem sm_all_five_anomalies_cancel {K : Type*} [Field K] [CharZero K] :
    anomSU3Cube = 0 ∧
    anomSU3SqU1 (smHypercharge (K := K) .QL)
      (smHypercharge .uRc) (smHypercharge .dRc) = 0 ∧
    anomSU2SqU1 (smHypercharge (K := K) .QL)
      (smHypercharge .LL) = 0 ∧
    anomGravU1 (smHypercharge (K := K) .QL)
      (smHypercharge .uRc) (smHypercharge .dRc)
      (smHypercharge .LL) (smHypercharge .eRc) = 0 ∧
    anomU1Cube (smHypercharge (K := K) .QL)
      (smHypercharge .uRc) (smHypercharge .dRc)
      (smHypercharge .LL) (smHypercharge .eRc) = 0 := by
  refine ⟨rfl, ?_, ?_, ?_, ?_⟩ <;>
    (simp only [anomSU3SqU1, anomSU2SqU1, anomGravU1, anomU1Cube,
       smHypercharge, inducedExteriorHypercharge];
     norm_num)

/-- Exact polynomial factorization of the reduced cubic $[U(1)_Y]^3$ anomaly after eliminating
$Y_{d^c} = -2 Y_Q - Y_{u^c}$, $Y_L = -3 Y_Q$, and $Y_{e^c} = 6 Y_Q$:
`anomU1Cube Y_Q Y_{u^c} (-2 Y_Q - Y_{u^c}) (-3 Y_Q) (6 Y_Q) = 18 * Y_Q * (4 Y_Q + Y_{u^c}) * (2 Y_Q - Y_{u^c})`. -/
theorem anomU1Cube_reduced_factorization {R : Type*} [CommRing R] (yQ yUc : R) :
    anomU1Cube yQ yUc (-2 * yQ - yUc) (-3 * yQ) (6 * yQ) =
      18 * yQ * (4 * yQ + yUc) * (2 * yQ - yUc) := by
  unfold anomU1Cube
  ring

/-- **General Anomaly Classification Theorem:** over any characteristic-0 field $K$, any hypercharge
5-tuple $(Y_Q, Y_{u^c}, Y_{d^c}, Y_L, Y_{e^c}) \in K^5$ cancelling $[SU(3)_c]^2 U(1)_Y$,
$[SU(2)_L]^2 U(1)_Y$, $\mathrm{Tr}(Y)$, and $\mathrm{Tr}(Y^3)$ lies either on the vector-like
branch ($Y_Q = Y_L = Y_{e^c} = 0$, $Y_{d^c} = -Y_{u^c}$) or on the Standard Model chiral branch
up to $u_R^c \leftrightarrow d_R^c$ swap. -/
theorem sm_hypercharge_anomaly_classification {K : Type*} [Field K] [CharZero K]
    (yQ yUc yDc yL yEc : K)
    (h3 : anomSU3SqU1 yQ yUc yDc = 0)
    (h2 : anomSU2SqU1 yQ yL = 0)
    (hG : anomGravU1 yQ yUc yDc yL yEc = 0)
    (h1 : anomU1Cube yQ yUc yDc yL yEc = 0) :
    (yQ = 0 ∧ yL = 0 ∧ yEc = 0 ∧ yDc = -yUc) ∨
    (yL = -3 * yQ ∧ yEc = 6 * yQ ∧
      ((yUc = -4 * yQ ∧ yDc = 2 * yQ) ∨ (yUc = 2 * yQ ∧ yDc = -4 * yQ))) := by
  unfold anomSU3SqU1 at h3
  unfold anomSU2SqU1 at h2
  unfold anomGravU1 at hG
  have hyDc : yDc = -2 * yQ - yUc := by linear_combination h3
  have hyL : yL = -3 * yQ := by linear_combination h2
  have hyEc : yEc = 6 * yQ := by linear_combination hG - 3 * h3 - 2 * h2
  rw [hyDc, hyL, hyEc, anomU1Cube_reduced_factorization] at h1
  have h18 : (18 : K) ≠ 0 := by norm_num
  have hprod : yQ * (4 * yQ + yUc) * (2 * yQ - yUc) = 0 := by
    apply mul_left_cancel₀ h18
    linear_combination h1
  rcases mul_eq_zero.mp hprod with hprod1 | hright
  · rcases mul_eq_zero.mp hprod1 with hyQ0 | hleft
    · left
      subst hyQ0
      exact ⟨rfl, by linear_combination hyL, by linear_combination hyEc,
        by linear_combination hyDc⟩
    · right
      have hyUc : yUc = -4 * yQ := by linear_combination hleft
      refine ⟨hyL, hyEc, Or.inl ⟨hyUc, ?_⟩⟩
      linear_combination hyDc - hyUc
  · right
    have hyUc : yUc = 2 * yQ := by linear_combination -hright
    refine ⟨hyL, hyEc, Or.inr ⟨hyUc, ?_⟩⟩
    linear_combination hyDc - hyUc

/-- **Normalized Hypercharge Uniqueness Theorem (`sm_hypercharge_uniqueness`):**
over any characteristic-0 field $K$, imposing anomaly cancellation together with the lepton-doublet
normalization $Y_L = -1/2$ uniquely forces $Y_Q = 1/6$, $Y_{e^c} = 1$, and
$(Y_{u^c}, Y_{d^c}) \in \{(-2/3, 1/3), (1/3, -2/3)\}$. -/
theorem sm_hypercharge_uniqueness {K : Type*} [Field K] [CharZero K]
    (yQ yUc yDc yL yEc : K)
    (h3 : anomSU3SqU1 yQ yUc yDc = 0)
    (h2 : anomSU2SqU1 yQ yL = 0)
    (hG : anomGravU1 yQ yUc yDc yL yEc = 0)
    (h1 : anomU1Cube yQ yUc yDc yL yEc = 0)
    (hNorm : yL = -1 / 2) :
    yQ = 1 / 6 ∧ yEc = 1 ∧
      ((yUc = -2 / 3 ∧ yDc = 1 / 3) ∨ (yUc = 1 / 3 ∧ yDc = -2 / 3)) := by
  rcases sm_hypercharge_anomaly_classification yQ yUc yDc yL yEc h3 h2 hG h1 with
    ⟨_, hyL0, _, _⟩ | ⟨hyL, hyEc, hpair⟩
  · exfalso
    rw [hyL0] at hNorm
    norm_num at hNorm
  · have hyQ : yQ = 1 / 6 := by
      rw [eq_div_iff (by norm_num : (6 : K) ≠ 0)]
      linear_combination 2 * hyL - 2 * hNorm
    rw [hyQ] at hyEc hpair
    refine ⟨hyQ, by linear_combination hyEc, ?_⟩
    rcases hpair with ⟨hu, hd⟩ | ⟨hu, hd⟩
    · left
      exact ⟨by linear_combination hu, by linear_combination hd⟩
    · right
      exact ⟨by linear_combination hu, by linear_combination hd⟩

end AnomalyCancellationAndUniqueness

-- ============================================================================
-- §4. Jimbo N = 3 (a = q³) R-Matrix on W₃ ⊗ W₃ & 3^⊗3 Singlet Survival
-- ============================================================================

section JimboR3AndEightfoldSurvival

/-- Explicit $9 \times 9$ braided Jimbo matrix $\check{R}_{W_3}$ on `Fin 3 × Fin 3`:
- $\check{R}(e_i \otimes e_i) = q\,(e_i \otimes e_i)$,
- $\check{R}(e_i \otimes e_j) = (q - q^{-1})\,(e_i \otimes e_j) + e_j \otimes e_i$ for $i < j$,
- $\check{R}(e_i \otimes e_j) = e_j \otimes e_i$ for $i > j$. -/
def jimboR3 {R : Type*} [CommRing R] (q qi : R) :
    Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R :=
  fun ⟨r, s⟩ ⟨i, j⟩ =>
    if i = j then
      if r = i ∧ s = i then q else 0
    else if i < j then
      if r = i ∧ s = j then q - qi
      else if r = j ∧ s = i then 1
      else 0
    else
      if r = j ∧ s = i then 1 else 0

/-- Direct two-slot vector action corresponding to `Matrix.mulVec (jimboR3 q qi)`. -/
def jimboAct2 {R : Type*} [CommRing R] (q qi : R)
    (v : Fin 3 × Fin 3 → R) : Fin 3 × Fin 3 → R :=
  fun ⟨r, s⟩ =>
    if r = s then q * v (r, r)
    else if r < s then (q - qi) * v (r, s) + v (s, r)
    else v (s, r)

theorem jimboR3_mulVec_eq {R : Type*} [CommRing R] (q qi : R) (v : Fin 3 × Fin 3 → R) :
    (jimboR3 q qi).mulVec v = jimboAct2 q qi v := by
  funext ⟨r, s⟩
  fin_cases r <;> fin_cases s <;>
    (simp [Matrix.mulVec, dotProduct, Fintype.sum_prod_type, Fin.sum_univ_three,
      jimboR3, jimboAct2]; try ring)

/-- **Exact `9 × 9` Quadratic Hecke Relation (`jimboR3_hecke_quadratic`):**
`(jimboR3 q qi - q • 1) * (jimboR3 q qi + qi • 1) = 0` over any commutative ring $R$ with
`qi * q = 1`, establishing that $H_n(q)$ acts on $W_3^{\otimes n}$ at the identical deformation
parameter $q$ as on $V_2^{\otimes n}$. -/
theorem jimboR3_hecke_quadratic {R : Type*} [CommRing R] {q qi : R} (hqi : qi * q = 1) :
    (jimboR3 q qi - q • (1 : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R)) *
      (jimboR3 q qi + qi • (1 : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R)) = 0 := by
  suffices hsq : jimboR3 q qi * jimboR3 q qi =
      (q - qi) • jimboR3 q qi + (1 : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R) by
    ext u w
    have hentry := congrFun (congrFun hsq u) w
    have hlhs :
        ((jimboR3 q qi - q • 1) * (jimboR3 q qi + qi • 1)) u w =
          (jimboR3 q qi * jimboR3 q qi) u w - ((q - qi) • jimboR3 q qi) u w -
            (q * qi) * (1 : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R) u w := by
      simp only [sub_mul, mul_add, Matrix.sub_apply, Matrix.add_apply,
        Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one,
        smul_smul, Matrix.smul_apply, smul_eq_mul]
      ring
    rw [hlhs, hentry, show q * qi = 1 by rw [mul_comm]; exact hqi]
    simp only [Matrix.add_apply, Matrix.zero_apply, one_mul]
    ring
  ext u w
  have hv := congrFun (jimboR3_mulVec_eq q qi ((jimboR3 q qi).mulVec (Pi.single w 1))) u
  rw [Matrix.mulVec_mulVec, Matrix.mulVec_single_one] at hv
  simp only [Matrix.col_apply] at hv
  rw [hv, jimboR3_mulVec_eq]
  have hqqi : q * qi = 1 := by rw [mul_comm]; exact hqi
  rcases u with ⟨r, s⟩
  rcases w with ⟨i, j⟩
  fin_cases r <;> fin_cases s <;> fin_cases i <;> fin_cases j <;>
    (simp [jimboAct2, jimboR3]; try (ring_nf; repeat' rw [hqqi]; ring))

/-- `27 × 27` tensor-leg matrix $\check{R}_{12} = \check{R}_{W_3} \otimes I_{W_3}$ on
`Fin 3 × Fin 3 × Fin 3`. -/
def jimboR3_12 {R : Type*} [CommRing R] (q qi : R) :
    Matrix (Fin 3 × Fin 3 × Fin 3) (Fin 3 × Fin 3 × Fin 3) R :=
  fun ⟨r, s, t⟩ ⟨i, j, k⟩ =>
    if t = k then jimboR3 q qi (r, s) (i, j) else 0

/-- `27 × 27` tensor-leg matrix $\check{R}_{23} = I_{W_3} \otimes \check{R}_{W_3}$ on
`Fin 3 × Fin 3 × Fin 3`. -/
def jimboR3_23 {R : Type*} [CommRing R] (q qi : R) :
    Matrix (Fin 3 × Fin 3 × Fin 3) (Fin 3 × Fin 3 × Fin 3) R :=
  fun ⟨r, s, t⟩ ⟨i, j, k⟩ =>
    if r = i then jimboR3 q qi (s, t) (j, k) else 0

/-- Three-slot vector action of $\check{R}_{12}$. -/
def jimboAct12 {R : Type*} [CommRing R] (q qi : R)
    (w : Fin 3 × Fin 3 × Fin 3 → R) : Fin 3 × Fin 3 × Fin 3 → R :=
  fun ⟨r, s, t⟩ => jimboAct2 q qi (fun p => w (p.1, p.2, t)) (r, s)

/-- Three-slot vector action of $\check{R}_{23}$. -/
def jimboAct23 {R : Type*} [CommRing R] (q qi : R)
    (w : Fin 3 × Fin 3 × Fin 3 → R) : Fin 3 × Fin 3 × Fin 3 → R :=
  fun ⟨r, s, t⟩ => jimboAct2 q qi (fun p => w (r, p.1, p.2)) (s, t)

theorem jimboR3_12_mulVec_eq {R : Type*} [CommRing R] (q qi : R)
    (w : Fin 3 × Fin 3 × Fin 3 → R) :
    (jimboR3_12 q qi).mulVec w = jimboAct12 q qi w := by
  funext ⟨r, s, t⟩
  rw [jimboAct12, ← jimboR3_mulVec_eq]
  simp only [Matrix.mulVec, dotProduct, Fintype.sum_prod_type, jimboR3_12]
  simp only [ite_mul, zero_mul, Finset.sum_ite_eq, Finset.mem_univ, ↓reduceIte]

theorem jimboR3_23_mulVec_eq {R : Type*} [CommRing R] (q qi : R)
    (w : Fin 3 × Fin 3 × Fin 3 → R) :
    (jimboR3_23 q qi).mulVec w = jimboAct23 q qi w := by
  funext ⟨r, s, t⟩
  rw [jimboAct23, ← jimboR3_mulVec_eq]
  simp only [Matrix.mulVec, dotProduct, Fintype.sum_prod_type, jimboR3_23]
  have hsum :
      (∑ x : Fin 3, ∑ x_1 : Fin 3, ∑ x_2 : Fin 3,
        (if r = x then jimboR3 q qi (s, t) (x_1, x_2) else 0) * w (x, x_1, x_2)) =
      ∑ x : Fin 3, if r = x then
        (∑ x_1 : Fin 3, ∑ x_2 : Fin 3, jimboR3 q qi (s, t) (x_1, x_2) * w (x, x_1, x_2))
      else 0 := by
    refine Finset.sum_congr rfl (fun x _ => ?_)
    by_cases hrx : r = x
    · simp [hrx]
    · simp [hrx]
  rw [hsum, Finset.sum_ite_eq]
  simp only [Finset.mem_univ, ↓reduceIte]

/-- **Exact `27 × 27` Braid / Yang–Baxter Identity (`jimboR3_braid_relation`):**
`jimboR3_12 q qi * jimboR3_23 q qi * jimboR3_12 q qi = jimboR3_23 q qi * jimboR3_12 q qi * jimboR3_23 q qi`
over any commutative ring $R$ with `qi * q = 1`. -/
theorem jimboR3_braid_relation {R : Type*} [CommRing R] {q qi : R} (hqi : qi * q = 1) :
    jimboR3_12 q qi * jimboR3_23 q qi * jimboR3_12 q qi =
      jimboR3_23 q qi * jimboR3_12 q qi * jimboR3_23 q qi := by
  have hqqi : q * qi = 1 := by rw [mul_comm]; exact hqi
  have hq2qi : q ^ 2 * qi = q := by linear_combination q * hqqi
  have hqqi2 : q * qi ^ 2 = qi := by linear_combination qi * hqqi
  have hact : ∀ w : Fin 3 × Fin 3 × Fin 3 → R,
      jimboAct12 q qi (jimboAct23 q qi (jimboAct12 q qi w)) =
        jimboAct23 q qi (jimboAct12 q qi (jimboAct23 q qi w)) := by
    intro w
    funext ⟨r, s, t⟩
    fin_cases r <;> fin_cases s <;> fin_cases t <;>
      (simp [jimboAct12, jimboAct23, jimboAct2];
       try (ring_nf; repeat' rw [hqqi]; repeat' rw [hq2qi]; repeat' rw [hqqi2]; ring))
  ext u v
  have hlhs :
      (jimboR3_12 q qi * jimboR3_23 q qi * jimboR3_12 q qi) u v =
        jimboAct12 q qi (jimboAct23 q qi (jimboAct12 q qi (Pi.single v 1))) u := by
    rw [← jimboR3_12_mulVec_eq, ← jimboR3_23_mulVec_eq, ← jimboR3_12_mulVec_eq,
      Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, Matrix.mulVec_single_one, Matrix.col_apply]
  have hrhs :
      (jimboR3_23 q qi * jimboR3_12 q qi * jimboR3_23 q qi) u v =
        jimboAct23 q qi (jimboAct12 q qi (jimboAct23 q qi (Pi.single v 1))) u := by
    rw [← jimboR3_23_mulVec_eq, ← jimboR3_12_mulVec_eq, ← jimboR3_23_mulVec_eq,
      Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, Matrix.mulVec_single_one, Matrix.col_apply]
  rw [hlhs, hrhs, hact]

/-- Unnormalized $U_q(\mathfrak{sl}_3)$ Cartan quantum-trace weights $(1, q^2, q^4)$ on $W_3$. -/
def sl3QTraceWeight {R : Type*} [Semiring R] (q : R) : Fin 3 → R
  | 0 => 1
  | 1 => q ^ 2
  | 2 => q ^ 4

/-- **Partial quantum trace of `jimboR3` on the second tensor factor:**
for all $i, r \in \mathrm{Fin}\,3$ and `qi * q = 1`,
$\sum_{j=0}^2 \mu_j\, (\check{R}_{W_3})_{(r, j), (i, j)} = \delta_{r, i}\, q^5$. -/
theorem jimboR3_partial_qtrace_eq_q5_one {R : Type*} [CommRing R] {q qi : R}
    (hqi : qi * q = 1) (r i : Fin 3) :
    (∑ j : Fin 3, sl3QTraceWeight q j * jimboR3 q qi (r, j) (i, j)) =
      if r = i then q ^ 5 else 0 := by
  fin_cases r <;> fin_cases i <;>
    simp [Fin.sum_univ_three, sl3QTraceWeight, jimboR3]
  · linear_combination -(q ^ 3 + q) * hqi
  · linear_combination -q ^ 3 * hqi
  · ring

/-- Symmetric quantum integers $[2]_q = q + q^{-1}$ and $[3]_q = q^2 + 1 + q^{-2}$. -/
noncomputable def qBracket2 {K : Type*} [Field K] (q : K) : K := q + q⁻¹

noncomputable def qBracket3 {K : Type*} [Field K] (q : K) : K := q ^ 2 + 1 + (q⁻¹) ^ 2

/-- Normalized $N = 2$ and $N = 3$ ($a = q^3$) HOMFLY-PT Markov trace parameters. -/
noncomputable def markovZ2 {K : Type*} [Field K] (q : K) : K :=
  q ^ 3 / (q ^ 2 + 1)

noncomputable def markovZ3 {K : Type*} [Field K] (q : K) : K :=
  q ^ 5 / (q ^ 4 + q ^ 2 + 1)

/-- Normalized Markov trace of the three-strand $q$-antisymmetriser $e_{(1,1,1)} \in H_3(q)$ as a
function of the single-crossing Markov parameter $z$:
`w111OfZ q z = (q³ / ([2]_q [3]_q)) * (1 - (2 q⁻¹ + q⁻³) z + (q⁻² + q⁻⁴) z²)`. -/
noncomputable def w111OfZ {K : Type*} [Field K] (q z : K) : K :=
  (q ^ 3 / (qBracket2 q * qBracket3 q)) *
    (1 - (2 * q⁻¹ + (q⁻¹) ^ 3) * z + ((q⁻¹) ^ 2 + (q⁻¹) ^ 4) * z ^ 2)

/-- Quantum Weyl dimensions of $V_{(3)}$, $V_{(2,1)}$, and $V_{(1,1,1)}$ for $U_q(\mathfrak{sl}_3)$. -/
noncomputable def qWeylDim3Sym {K : Type*} [Field K] (q : K) : K :=
  (q ^ 3 + q + q⁻¹ + (q⁻¹) ^ 3) * (q ^ 4 + q ^ 2 + 1 + (q⁻¹) ^ 2 + (q⁻¹) ^ 4) / qBracket2 q

noncomputable def qWeylDim3Mixed {K : Type*} [Field K] (q : K) : K :=
  qBracket2 q * (q ^ 3 + q + q⁻¹ + (q⁻¹) ^ 3)

noncomputable def qWeylDim3Alt {K : Type*} [Field K] (_q : K) : K := 1

/-- **HOMFLY-PT `N = 3` (`a = q³`) Markov Parameter and Survival of the Baryon Singlet `(1, 1, 1)`:**
1. Normalized partial quantum trace gives `markovZ3 q = q³ / [3]_q`.
2. At `N = 2` (`z = markovZ2 q`), the $(1, 1, 1)$ Wenzl weight vanishes identically (`w111OfZ q (markovZ2 q) = 0`),
   reflecting `weylDimAlt 2 = 0`.
3. At `N = 3` (`z = markovZ3 q`), `w111OfZ q (markovZ3 q) = 1 / [3]_q³`, which is strictly positive
   for every real $q > 0$ and equals $1 / 27$ at $q = 1$.
4. Quantum Schur–Weyl dimensions satisfy `1 * qWeylDim3Sym q + 2 * qWeylDim3Mixed q + 1 * qWeylDim3Alt q = [3]_q³`
   for all $q \neq 0$, specializing at $q = 1$ to `10 * 1 + 8 * 2 + 1 * 1 = 27 = 3³`
   (`weylDimSym 3 = 10`, `weylDimMixed 3 = 8`, `weylDimAlt 3 = 1`). -/
theorem homfly_sl3_markov_and_baryon_singlet_survival :
    (∀ q : ℝ, q ≠ 0 → markovZ3 q = q ^ 3 / qBracket3 q) ∧
    (∀ q : ℝ, q ≠ 0 → w111OfZ q (markovZ2 q) = 0) ∧
    (∀ q : ℝ, 0 < q →
      w111OfZ q (markovZ3 q) = 1 / (qBracket3 q) ^ 3 ∧ 0 < w111OfZ q (markovZ3 q)) ∧
    w111OfZ (1 : ℝ) (markovZ3 1) = 1 / 27 ∧
    (∀ q : ℝ, q ≠ 0 →
      1 * qWeylDim3Sym q + 2 * qWeylDim3Mixed q + 1 * qWeylDim3Alt q = (qBracket3 q) ^ 3) ∧
    weylDimSym 3 = 10 ∧ weylDimMixed 3 = 8 ∧ weylDimAlt 3 = 1 ∧
    1 * weylDimSym 3 + 2 * weylDimMixed 3 + 1 * weylDimAlt 3 = 3 ^ 3 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro q hq0
    unfold markovZ3 qBracket3
    have hden : q ^ 4 + q ^ 2 + 1 = q ^ 2 * (q ^ 2 + 1 + (q⁻¹) ^ 2) := by
      field_simp
    have hq3 : q ^ 2 + 1 + (q⁻¹) ^ 2 ≠ 0 := by
      intro h
      have hmul := congrArg (fun x => q ^ 2 * x) h
      dsimp at hmul
      rw [mul_zero, ← hden] at hmul
      have hpos : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
      linarith
    field_simp
  · intro q hq0
    unfold w111OfZ markovZ2 qBracket2 qBracket3
    have hfac :
        1 - (2 * q⁻¹ + (q⁻¹) ^ 3) * (q ^ 3 / (q ^ 2 + 1)) +
          ((q⁻¹) ^ 2 + (q⁻¹) ^ 4) * (q ^ 3 / (q ^ 2 + 1)) ^ 2 = 0 := by
      have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
      field_simp
      ring
    rw [hfac, mul_zero]
  · intro q hqpos
    have hq0 : q ≠ 0 := ne_of_gt hqpos
    have hq2pos : 0 < qBracket2 q := by unfold qBracket2; positivity
    have hq3pos : 0 < qBracket3 q := by unfold qBracket3; positivity
    have hq421 : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
    have heq : w111OfZ q (markovZ3 q) = 1 / (qBracket3 q) ^ 3 := by
      unfold w111OfZ markovZ3 qBracket2 qBracket3
      have hq2ne : q + q⁻¹ ≠ 0 := ne_of_gt hq2pos
      have hq3ne : q ^ 2 + 1 + (q⁻¹) ^ 2 ≠ 0 := ne_of_gt hq3pos
      have hq4ne : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt hq421
      field_simp
      ring
    exact ⟨heq, by rw [heq]; positivity⟩
  · unfold w111OfZ markovZ3 qBracket2 qBracket3
    norm_num
  · intro q hq0
    unfold qWeylDim3Sym qWeylDim3Mixed qWeylDim3Alt qBracket3 qBracket2
    have hq2ne : q + q⁻¹ ≠ 0 := by
      intro h
      have hmul := congrArg (fun x => q * x) h
      dsimp at hmul
      have h1 : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
      rw [h1, mul_zero] at hmul
      have : 0 < q ^ 2 + 1 := by positivity
      linarith
    field_simp
    ring
  · unfold weylDimSym; decide
  · unfold weylDimMixed; decide
  · unfold weylDimAlt; decide
  · unfold weylDimSym weylDimMixed weylDimAlt; decide

end JimboR3AndEightfoldSurvival

-- ============================================================================
-- §5. Canonical UV Weinberg Angle sin² θ_W^UV = 3 / 8 & q-Deformed Bounds
-- ============================================================================

section WeinbergAngleUVAndQDeformed

/-- Quadratic weak-isospin trace $\mathrm{Tr}_m(T_3^2)$ on a single chiral multiplet $m$:
each $SU(2)_L$ doublet contributes $(+1/2)^2 + (-1/2)^2 = 1/2$ per color state, while $SU(2)_L$
singlets contribute $0$. -/
noncomputable def multipletTrT3Sq {K : Type*} [Field K] : ChiralMultiplet → K
  | .LL => (smColorDim .LL : K) * (1 / 2)
  | .dRc => 0
  | .eRc => 0
  | .QL => (smColorDim .QL : K) * (1 / 2)
  | .uRc => 0

/-- Total $\mathrm{Tr}_{\mathcal{S}_{\mathrm{chiral}}}(T_3^2)$ over one chiral generation. -/
noncomputable def chiralGenTrT3Sq {K : Type*} [Field K] : K :=
  ∑ m : ChiralMultiplet, multipletTrT3Sq m

/-- Total $\mathrm{Tr}_{\mathcal{S}_{\mathrm{chiral}}}(Y^2)$ over one chiral generation. -/
noncomputable def chiralGenTrYSq {K : Type*} [Field K] : K :=
  ∑ m : ChiralMultiplet, (smWeylMult m : K) * (smHypercharge (K := K) m) ^ 2

/-- Total $\mathrm{Tr}_{\mathcal{S}_{\mathrm{chiral}}}(Q^2)$ of $Q = T_3 + Y$ across all `15` Weyl
states of one chiral generation (`ν_L, e_L`, three `d_R^c`, `e_R^c`, three `(u_L, d_L)`, three `u_R^c`). -/
noncomputable def chiralGenTrQSq {K : Type*} [Field K] : K :=
  1 * ((1 / 2 : K) + smHypercharge .LL) ^ 2 +
  1 * ((-1 / 2 : K) + smHypercharge .LL) ^ 2 +
  3 * (smHypercharge (K := K) .dRc) ^ 2 +
  1 * (smHypercharge (K := K) .eRc) ^ 2 +
  3 * ((1 / 2 : K) + smHypercharge .QL) ^ 2 +
  3 * ((-1 / 2 : K) + smHypercharge .QL) ^ 2 +
  3 * (smHypercharge (K := K) .uRc) ^ 2

/-- Canonical trace-normalized UV Weinberg angle
$\sin^2\theta_W^{\mathrm{UV}} = \frac{\mathrm{Tr}(T_3^2)}{\mathrm{Tr}(T_3^2) + \mathrm{Tr}(Y^2)}$. -/
noncomputable def weinbergSinSqUV {K : Type*} [Field K] : K :=
  chiralGenTrT3Sq / (chiralGenTrT3Sq + chiralGenTrYSq)

/-- **Canonical UV Weinberg Angle Theorem (`weinbergSinSqUV = 3 / 8`):**
over any characteristic-0 field $K$, the split exterior package $\mathcal{S}_{\mathrm{chiral}}$
satisfies $\mathrm{Tr}(T_3^2) = 2$, $\mathrm{Tr}(Y^2) = 10 / 3$, $\mathrm{Tr}(Q^2) = 16 / 3$, and
$\sin^2\theta_W^{\mathrm{UV}} = 3 / 8$ while `splitUnimodularSubmodule K` carries zero off-diagonal
$SU(5)$ proton-decay generators. -/
theorem canonical_uv_weinberg_angle_three_eighths {K : Type*} [Field K] [CharZero K] :
    chiralGenTrT3Sq (K := K) = 2 ∧
    chiralGenTrYSq (K := K) = 10 / 3 ∧
    chiralGenTrQSq (K := K) = 16 / 3 ∧
    chiralGenTrT3Sq (K := K) + chiralGenTrYSq (K := K) = chiralGenTrQSq (K := K) ∧
    weinbergSinSqUV (K := K) = 3 / 8 := by
  have hT3 : chiralGenTrT3Sq (K := K) = 2 := by
    unfold chiralGenTrT3Sq
    have huniv : (Finset.univ : Finset ChiralMultiplet) = {.LL, .dRc, .eRc, .QL, .uRc} := by decide
    rw [huniv]
    simp [multipletTrT3Sq, smColorDim]
    norm_num
  have hY : chiralGenTrYSq (K := K) = 10 / 3 := by
    unfold chiralGenTrYSq
    have huniv : (Finset.univ : Finset ChiralMultiplet) = {.LL, .dRc, .eRc, .QL, .uRc} := by decide
    rw [huniv]
    simp [smWeylMult, smColorDim, smWeakDim, smHypercharge, inducedExteriorHypercharge]
    norm_num
  have hQ : chiralGenTrQSq (K := K) = 16 / 3 := by
    unfold chiralGenTrQSq smHypercharge inducedExteriorHypercharge
    norm_num
  refine ⟨hT3, hY, hQ, ?_, ?_⟩
  · rw [hT3, hY, hQ]; norm_num
  · unfold weinbergSinSqUV
    rw [hT3, hY]
    norm_num

/-- Quantum-dimension-weighted quadratic weak-isospin trace replacing $(2, 3)$ by
$([2]_q, [3]_q)$: $\mathrm{Tr}_q(T_3^2) = (1 + [3]_q) \cdot \frac{[2]_q}{4}$. -/
noncomputable def trT3SqQ (q : ℝ) : ℝ :=
  (1 + qBracket3 q) * (qBracket2 q / 4)

/-- Quantum-dimension-weighted hypercharge trace replacing $(2, 3)$ by $([2]_q, [3]_q)$ across the
five multiplets of $\mathcal{S}_{\mathrm{chiral}}$. -/
noncomputable def trYSqQ (q : ℝ) : ℝ :=
  qBracket2 q * (-1 / 2 : ℝ) ^ 2 +
  qBracket3 q * (1 / 3 : ℝ) ^ 2 +
  1 * (1 : ℝ) ^ 2 +
  (qBracket3 q * qBracket2 q) * (1 / 6 : ℝ) ^ 2 +
  qBracket3 q * (-2 / 3 : ℝ) ^ 2

/-- Quantum-dimension-weighted Weinberg ratio
$\sin^2\theta_W(q) = \frac{\mathrm{Tr}_q(T_3^2)}{\mathrm{Tr}_q(T_3^2) + \mathrm{Tr}_q(Y^2)}$. -/
noncomputable def weinbergSinSqQ (q : ℝ) : ℝ :=
  trT3SqQ q / (trT3SqQ q + trYSqQ q)

/-- **`q`-Deformed Quantum-Dimension Weinberg Angle Bounds and Classical Limit:**
1. For every real $q > 0$, `[2]_q ≥ 2`, `[3]_q ≥ 3`, `0 < trT3SqQ q`, `0 < trYSqQ q`, and
   `0 < weinbergSinSqQ q < 1`.
2. For every $q \neq 0$, `weinbergSinSqQ q⁻¹ = weinbergSinSqQ q` (bar symmetry).
3. At the classical limit $q = 1$, `weinbergSinSqQ 1 = 3 / 8`. -/
theorem weinbergSinSqQ_bounds_and_limit :
    (∀ q : ℝ, 0 < q →
      2 ≤ qBracket2 q ∧ 3 ≤ qBracket3 q ∧
      0 < trT3SqQ q ∧ 0 < trYSqQ q ∧
      0 < weinbergSinSqQ q ∧ weinbergSinSqQ q < 1) ∧
    (∀ q : ℝ, q ≠ 0 → weinbergSinSqQ q⁻¹ = weinbergSinSqQ q) ∧
    weinbergSinSqQ 1 = 3 / 8 := by
  refine ⟨?_, ?_, ?_⟩
  · intro q hq
    have hq2 : 2 ≤ qBracket2 q := by
      unfold qBracket2
      have hsq : 0 ≤ (q - 1) ^ 2 / q := div_nonneg (sq_nonneg _) (le_of_lt hq)
      have hid : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by
        have hq0 : q ≠ 0 := ne_of_gt hq
        field_simp; ring
      linarith
    have hq3 : 3 ≤ qBracket3 q := by
      unfold qBracket3
      have hsq : 0 ≤ (q ^ 2 - 1) ^ 2 / q ^ 2 := div_nonneg (sq_nonneg _) (sq_nonneg _)
      have hid : q ^ 2 + 1 + (q⁻¹) ^ 2 - 3 = (q ^ 2 - 1) ^ 2 / q ^ 2 := by
        have hq0 : q ≠ 0 := ne_of_gt hq
        field_simp; ring
      linarith
    have hT : 0 < trT3SqQ q := by unfold trT3SqQ; nlinarith
    have hY : 0 < trYSqQ q := by unfold trYSqQ; nlinarith
    have hden : 0 < trT3SqQ q + trYSqQ q := by linarith
    refine ⟨hq2, hq3, hT, hY, div_pos hT hden, ?_⟩
    unfold weinbergSinSqQ
    rw [div_lt_one hden]
    linarith
  · intro q _hq0
    have hb2 : qBracket2 q⁻¹ = qBracket2 q := by unfold qBracket2; rw [inv_inv, add_comm]
    have hb3 : qBracket3 q⁻¹ = qBracket3 q := by unfold qBracket3; rw [inv_inv]; ring
    unfold weinbergSinSqQ trT3SqQ trYSqQ
    rw [hb2, hb3]
  · unfold weinbergSinSqQ trT3SqQ trYSqQ qBracket2 qBracket3
    norm_num

end WeinbergAngleUVAndQDeformed

end QOU.StandardModel.BringPushforwardAndGaugeGroupUnification
