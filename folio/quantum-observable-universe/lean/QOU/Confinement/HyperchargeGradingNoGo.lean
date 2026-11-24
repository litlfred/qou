import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Tactic

/-!
# A second strand grading (hypercharge) cannot separate `n ⊗ ν` from `p ⊗ e⁻`

Bean `qou-99qc`. Pre-registered in `computations/probes/qbeta_hypercharge_grading/PREREGISTRATION.md`.

Owner question (2026-11-20): under premise L (the lepton is a fourth strand carrying the u/d
doublet, `ν` in the `T³ = +½` slot, `e⁻` in `−½`), can a second grading — hypercharge `q^{cY}`,
`Y_quark = 1/3`, `Y_lepton = −1` — put quarks and leptons at different `q` powers, so that the
β exchange `n ⊗ ν → p ⊗ e⁻` releases energy? The grading `K = q^{2T³}` alone cannot
(PR #8661, `CartanEnergyTransport`).

## Results (generic field `R`, §7c; an ordered field only in `split_hyper_eq_zero_iff`)

**Part A — conserved charges (scope (b)).** Strands are labelled by a type (quark / lepton) and a
flavour (u / d). The two four-strand states are `nNu = (q u)(q d)(q d)(ℓ u)` and
`pE = (q u)(q u)(q d)(ℓ d)`.
* `total_eq_iff` : an additive strand charge `χ` has equal totals on the two states iff
  `χ(q,d) + χ(ℓ,u) = χ(q,u) + χ(ℓ,d)` (no type–flavour interaction term).
* `total_separable` : every separable charge `α(type) + β(flavour)` has equal totals. `T³`
  depends only on flavour and `Y` only on type, so `a·T³ + c·Y` is separable for all `a, c`.
* `split_zero_of_total` : hence ANY function `F` of the total charge — in particular any
  character `q^{a·T³ + c·Y}` — gives a zero split, for every `c`.
* `grouplike_weight_eq` : the multiplicative form, with weights `g_type · k^{±1}` in `R`.

**Part B — matrices.** On a quark ⊗ lepton pair:
* `EF_commutes_dressed` : the charged-current term `E ⊗ F` commutes with the dressed grading
  `(g_q K) ⊗ (g_ℓ K)` for all scalars `g_q, g_ℓ`.
* `EF_commutes_charge` : `E ⊗ F` commutes with the primitive charge `2Q ⊗ 1 + 1 ⊗ 2Q`,
  `2Q = 2T³ + Y` on each strand (Gell-Mann–Nishijima, cleared). Total `Q` is conserved.
* `Rc_intertwines_dressed` : Jimbo's strand-tracked crossing `Ř` (which swaps the strands)
  intertwines `(g_q K) ⊗ (g_ℓ K)` with `(g_ℓ K) ⊗ (g_q K)`. So a per-strand scalar grading is
  braiding-compatible for any `g`.
* `weight_transport` : the general mechanism — an operator `X` commuting with a grading `D`
  carries a `D`-eigenvector of eigenvalue `a` to one of eigenvalue `a`, so no function of the
  grading eigenvalue separates `v` from `X v ≠ 0`.

**Part C — the ruled (Markov-normalised) trace is blind to a scalar dressing.**
* `normalised_trace_dressing_cancels` : `Tr(g•K * X)/Tr(g•K) = Tr(K * X)/Tr(K)` for `g ≠ 0`.

**Part D — the one functional that does separate (a NEW premise, not the ruled one).**
A per-strand, unnormalised, additive energy `Σ_strands g_type · κ(flavour)`, `κ(u) = q`,
`κ(d) = q⁻¹`, is not a function of the conserved totals.
* `split_eq` : its split is `(g_ℓ − g_q)(q − q⁻¹)`.
* `split_eq_zero_iff` : zero iff `g_ℓ = g_q` (given `q − q⁻¹ ≠ 0`).
* `split_hyper_eq` / `split_hyper_eq_zero_iff` : with `g_q = s`, `g_ℓ = s⁻³` (`s = q^{c/3}`),
  split `= (s⁻³ − s)(q − q⁻¹)`, and on an ordered field with `s > 0` it is zero iff `s = 1`
  (i.e. `c = 0`).
* `split_at_one` : at `q = 1` the split vanishes for every `s`.

## What is NOT claimed

* No value of `c` is derived or selected: nothing in the corpus fixes the normalisation of a
  `U(1)_Y` grading on strands (`eightfold-open-problems.md` lists `Y` as open). The Part D
  functional is not the convention-D trace the owner ruled for `ε`; adopting it is a premise.
* Nothing here identifies the Part D split with `Q_β`.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VII–VIII
-/

namespace QOU.QuarkState.HyperchargeGradingNoGo

open Matrix

/-! ## Part A: conserved additive charges -/

/-- Strand type. -/
inductive Ty | quark | lepton
  deriving DecidableEq

/-- Strand flavour (doublet slot). -/
inductive Fl | u | d
  deriving DecidableEq

/-- `n ⊗ ν = (q u)(q d)(q d)(ℓ u)`. -/
def nNu : List (Ty × Fl) := [(.quark, .u), (.quark, .d), (.quark, .d), (.lepton, .u)]

/-- `p ⊗ e⁻ = (q u)(q u)(q d)(ℓ d)`. -/
def pE : List (Ty × Fl) := [(.quark, .u), (.quark, .u), (.quark, .d), (.lepton, .d)]

/-- Total of an additive strand charge. -/
def total {G : Type*} [AddCommGroup G] (χ : Ty × Fl → G) (L : List (Ty × Fl)) : G :=
  (L.map χ).sum

theorem total_nNu {G : Type*} [AddCommGroup G] (χ : Ty × Fl → G) :
    total χ nNu = χ (.quark, .u) + χ (.quark, .d) + χ (.quark, .d) + χ (.lepton, .u) := by
  simp [total, nNu]; abel

theorem total_pE {G : Type*} [AddCommGroup G] (χ : Ty × Fl → G) :
    total χ pE = χ (.quark, .u) + χ (.quark, .u) + χ (.quark, .d) + χ (.lepton, .d) := by
  simp [total, pE]; abel

/-- **Equal totals iff no type–flavour interaction on the exchanged pair.** -/
theorem total_eq_iff {G : Type*} [AddCommGroup G] (χ : Ty × Fl → G) :
    total χ nNu = total χ pE ↔
      χ (.quark, .d) + χ (.lepton, .u) = χ (.quark, .u) + χ (.lepton, .d) := by
  rw [total_nNu, total_pE]
  constructor
  · intro h
    have : χ (.quark, .d) + χ (.lepton, .u) - (χ (.quark, .u) + χ (.lepton, .d)) =
        (χ (.quark, .u) + χ (.quark, .d) + χ (.quark, .d) + χ (.lepton, .u)) -
          (χ (.quark, .u) + χ (.quark, .u) + χ (.quark, .d) + χ (.lepton, .d)) := by abel
    rw [h, sub_self] at this
    exact sub_eq_zero.mp this
  · intro h
    have : (χ (.quark, .u) + χ (.quark, .d) + χ (.quark, .d) + χ (.lepton, .u)) -
          (χ (.quark, .u) + χ (.quark, .u) + χ (.quark, .d) + χ (.lepton, .d)) =
        χ (.quark, .d) + χ (.lepton, .u) - (χ (.quark, .u) + χ (.lepton, .d)) := by abel
    rw [h, sub_self] at this
    exact sub_eq_zero.mp this

/-- **Every separable charge `α(type) + β(flavour)` is conserved by the exchange.** -/
theorem total_separable {G : Type*} [AddCommGroup G] (α : Ty → G) (β : Fl → G) :
    total (fun s => α s.1 + β s.2) nNu = total (fun s => α s.1 + β s.2) pE := by
  rw [total_eq_iff]; abel

/-- `2T³`: depends on flavour only. -/
def twoT3 : Fl → ℤ
  | .u => 1
  | .d => -1

/-- Hypercharge, times 3 (`3Y`): depends on type only. Quark `3·(1/3) = 1`, lepton `3·(−1) = −3`. -/
def threeY : Ty → ℤ
  | .quark => 1
  | .lepton => -3

/-- **The `T³ ⊕ Y` charge with any coefficients `a, c` is conserved.** -/
theorem T3_Y_conserved {G : Type*} [AddCommGroup G] (a c : G) :
    total (fun s => twoT3 s.2 • a + threeY s.1 • c) nNu =
      total (fun s => twoT3 s.2 • a + threeY s.1 • c) pE := by
  have := total_separable (fun t => threeY t • c) (fun f => twoT3 f • a)
  simpa [add_comm] using this

/-- `3Y` totals vanish on both sides (hypercharge balance of the decay). -/
theorem threeY_total : total (fun s => threeY s.1) nNu = 0 ∧ total (fun s => threeY s.1) pE = 0 := by
  constructor <;> decide

/-- **No-go (scope (b)).** Any function of a separable total charge gives a zero split. In
particular every grading `q^{a·2T³ + c·3Y}`, for every `c`. -/
theorem split_zero_of_total {G : Type*} [AddCommGroup G] {E : Type*} [AddCommGroup E]
    (α : Ty → G) (β : Fl → G) (F : G → E) :
    F (total (fun s => α s.1 + β s.2) nNu) - F (total (fun s => α s.1 + β s.2) pE) = 0 := by
  rw [total_separable, sub_self]

variable {R : Type*} [Field R]

/-- Multiplicative (grouplike) weight of one strand: `g_type · k^{±1}`. -/
def gw (gq gl k : R) : Ty × Fl → R
  | (.quark, .u) => gq * k
  | (.quark, .d) => gq * k⁻¹
  | (.lepton, .u) => gl * k
  | (.lepton, .d) => gl * k⁻¹

/-- **The grouplike four-strand weight is equal on `n ⊗ ν` and `p ⊗ e⁻` for all dressings.** -/
theorem grouplike_weight_eq (gq gl k : R) :
    (nNu.map (gw gq gl k)).prod = (pE.map (gw gq gl k)).prod := by
  simp only [nNu, pE, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, gw]
  ring

/-! ## Part B: matrices -/

/-- `K = diag(q, q⁻¹)`. -/
def Kd (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 0, q⁻¹]
/-- `E = e₀₁` (d → u). -/
def Ed : Matrix (Fin 2) (Fin 2) R := !![0, 1; 0, 0]
/-- `F = e₁₀` (u → d). -/
def Fd : Matrix (Fin 2) (Fin 2) R := !![0, 0; 1, 0]
/-- `2T³ = diag(1, −1)`. -/
def Hd : Matrix (Fin 2) (Fin 2) R := !![1, 0; 0, -1]

theorem K_E (q : R) (hq : q ≠ 0) : Kd q * Ed = (q ^ 2) • (Ed * Kd q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Kd, Ed, Matrix.mul_apply, Fin.sum_univ_two]; try field_simp)

theorem K_F (q : R) (hq : q ≠ 0) : Kd q * Fd = (q⁻¹ ^ 2) • (Fd * Kd q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Kd, Fd, Matrix.mul_apply, Fin.sum_univ_two]; try field_simp)

/-- **The charged-current exchange commutes with the hypercharge-dressed grading**, for all
`g_q, g_ℓ`. -/
theorem EF_commutes_dressed (q gq gl : R) (hq : q ≠ 0) :
    kroneckerMap (· * ·) (gq • Kd q) (gl • Kd q) * kroneckerMap (· * ·) Ed Fd =
      kroneckerMap (· * ·) Ed Fd * kroneckerMap (· * ·) (gq • Kd q) (gl • Kd q) := by
  rw [Matrix.smul_kronecker, Matrix.kronecker_smul, smul_smul, Matrix.smul_mul,
    Matrix.mul_smul, ← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul,
    K_E q hq, K_F q hq, Matrix.smul_kronecker, Matrix.kronecker_smul, smul_smul,
    Matrix.mul_kronecker_mul]
  rw [smul_smul]
  congr 1
  field_simp

/-- The cleared Gell-Mann–Nishijima charge `2Q = 2T³ + Y` on a strand of hypercharge `y`. -/
def twoQ (y : R) : Matrix (Fin 2) (Fin 2) R := !![1 + y, 0; 0, -1 + y]

/-- **Total electric charge is conserved by `E ⊗ F`** for any strand hypercharges `y_q, y_ℓ`:
`E ⊗ F` commutes with the primitive charge `2Q ⊗ 1 + 1 ⊗ 2Q`. -/
theorem EF_commutes_charge (yq yl : R) :
    (kroneckerMap (· * ·) (twoQ yq) 1 + kroneckerMap (· * ·) 1 (twoQ yl)) *
        kroneckerMap (· * ·) Ed Fd =
      kroneckerMap (· * ·) Ed Fd *
        (kroneckerMap (· * ·) (twoQ yq) 1 + kroneckerMap (· * ·) 1 (twoQ yl)) := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, kroneckerMap_apply,
      twoQ, Ed, Fd, Matrix.add_apply, Matrix.one_apply]
  all_goals ring

/-- Jimbo `Ř` on `V ⊗ V`, basis `uu, ud, du, dd` (as in #8638 / #8673). -/
def Rc (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- Dressed grading `(g₁ K) ⊗ (g₂ K)` in the basis `uu, ud, du, dd`. -/
def Kdr (q g₁ g₂ : R) : Matrix (Fin 4) (Fin 4) R :=
  (g₁ * g₂) • diagonal ![q ^ 2, 1, 1, q⁻¹ ^ 2]

/-- **The strand-tracked crossing intertwines the dressed gradings with the labels swapped.** -/
theorem Rc_intertwines_dressed (q gq gl : R) :
    Rc q * Kdr q gq gl = Kdr q gl gq * Rc q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, Kdr, Matrix.mul_apply, diagonal] <;> ring

/-- **Weight transport.** If `X` commutes with a grading `D` and `D v = a v`, then
`D (X v) = a (X v)`; if moreover `X v ≠ 0` and `D (X v) = b (X v)`, then `a = b`. -/
theorem weight_transport {M : Type*} [AddCommGroup M] [Module R M] (D X : M →ₗ[R] M)
    (hDX : D ∘ₗ X = X ∘ₗ D) (v : M) (a b : R) (hv : D v = a • v)
    (hXv : D (X v) = b • X v) (hne : X v ≠ 0) : a = b := by
  have h1 : D (X v) = a • X v := by
    have := congrArg (fun f => f v) hDX
    simp only [LinearMap.comp_apply] at this
    rw [this, hv, map_smul]
  have h2 : (a - b) • X v = 0 := by rw [sub_smul, ← h1, ← hXv, sub_self]
  rcases smul_eq_zero.mp h2 with h | h
  · exact sub_eq_zero.mp h
  · exact absurd h hne

/-! ## Part C: the Markov-normalised trace is blind to a scalar dressing -/

/-- **A scalar per-strand dressing cancels in the normalised trace.** -/
theorem normalised_trace_dressing_cancels {n : Type*} [Fintype n] [DecidableEq n]
    (K X : Matrix n n R) (g : R) (hg : g ≠ 0) :
    trace (g • K * X) / trace (g • K) = trace (K * X) / trace K := by
  rw [Matrix.smul_mul, Matrix.trace_smul, Matrix.trace_smul, smul_eq_mul, smul_eq_mul]
  by_cases hK : trace K = 0
  · simp [hK]
  · field_simp

/-! ## Part D: the per-strand unnormalised additive energy (a new premise) -/

/-- `K`-eigenvalue of a flavour: `κ(u) = q`, `κ(d) = q⁻¹`. -/
def kappa (q : R) : Fl → R
  | .u => q
  | .d => q⁻¹

/-- Per-strand energy `g_type · κ(flavour)`. -/
def eps (q gq gl : R) : Ty × Fl → R
  | (.quark, f) => gq * kappa q f
  | (.lepton, f) => gl * kappa q f

/-- Released energy `E(n ⊗ ν) − E(p ⊗ e⁻)` of the additive per-strand energy. -/
def split (q gq gl : R) : R := total (eps q gq gl) nNu - total (eps q gq gl) pE

/-- **`split = (g_ℓ − g_q)(q − q⁻¹)`.** -/
theorem split_eq (q gq gl : R) : split q gq gl = (gl - gq) * (q - q⁻¹) := by
  unfold split
  rw [total_nNu, total_pE]
  simp only [eps, kappa]
  ring

/-- **Zero iff quark and lepton strands carry the same dressing.** -/
theorem split_eq_zero_iff (q gq gl : R) (hh : q - q⁻¹ ≠ 0) :
    split q gq gl = 0 ↔ gl = gq := by
  rw [split_eq]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h | h
    · exact sub_eq_zero.mp h
    · exact absurd h hh
  · intro h; rw [h, sub_self, zero_mul]

/-- With `g_q = s = q^{c/3}` and `g_ℓ = s⁻³ = q^{−c}` (hypercharges `1/3` and `−1`). -/
theorem split_hyper_eq (q s : R) : split q s (s⁻¹ ^ 3) = (s⁻¹ ^ 3 - s) * (q - q⁻¹) :=
  split_eq q s _

/-- At `q = 1` the split vanishes for every dressing. -/
theorem split_at_one (gq gl : R) : split 1 gq gl = 0 := by
  rw [split_eq]; simp

/-- **On an ordered field, with `s > 0` and `q − q⁻¹ ≠ 0`, the hypercharge split is zero iff
`s = 1`, i.e. iff `c = 0`.** -/
theorem split_hyper_eq_zero_iff {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]
    (q s : L) (hs : 0 < s) (hh : q - q⁻¹ ≠ 0) :
    split q s (s⁻¹ ^ 3) = 0 ↔ s = 1 := by
  rw [split_eq_zero_iff q s _ hh]
  constructor
  · intro h
    have h4 : s ^ 4 = 1 := by
      have : s ^ 3 * s⁻¹ ^ 3 = s ^ 3 * s := by rw [h]
      rw [← mul_pow, mul_inv_cancel₀ hs.ne', one_pow] at this
      linear_combination -this
    exact (pow_eq_one_iff_of_nonneg hs.le (by norm_num)).mp h4
  · intro h; subst h; simp

end QOU.QuarkState.HyperchargeGradingNoGo
