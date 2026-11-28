import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# Flavour-typed letters of the γγ nucleon word give no second flavour factor

Beans `qou-myts`, `qou-99qc`. Owner ruling 2026-11-27 (ledger row "The nucleon mass split uses
the framing-corrected trace …"): a down-letter curl contributes 0, so *"the flavour split must
come from the flavour letters themselves"*. Question (thread "Derive the nucleon flavour
factor"): on the full tower, does a second flavour-letter contribution derive a factor of about
2 on top of the `K`-weight cell `τ_p/τ_n = q²` (`NucleonSplitFullTower`)?

## Setting

`NucleonFlavourIsDetermined` types every crossing by the flavours of the two strands that meet
there (corpus blocks `up-quark-properties`, `down-quark-properties`): a `uu` crossing is the
crossing itself, a `dd` crossing is the reversed crossing, a mixed crossing is the average
`(σ + σ⁻¹)/2` (`ud_letter_is_average`). On `V ⊗ V` (basis `u = 0`, `d = 1`) a typed letter is
therefore weight-preserving, with

* a scalar `α` on `uu`, a scalar `β` on `dd`,
* a `2 × 2` block `m` on the mixed states `ud, du`,

and **reversing the crossing swaps `α` and `β` and keeps `m`**. Both readings of the mass fit:

| reading | `α` (typed `σ`) | `β` (typed `σ`) | `m` |
|---|---|---|---|
| raw trace | `q` | `q⁻¹` | `(Ř + Ř⁻¹)/2` on `ud, du` |
| framing-corrected (`def:mass-identity`, ruling A) | `q⁻²·q = q⁻¹` | `q²·q⁻¹ = q` | `(q⁻²Ř + q²Ř⁻¹)/2` |

(the corrected weights `q^{∓2}` per signed crossing are those of `NucleonCurlFramingCancels`).
Everything below holds for **every** `α, β, m`, so it covers both readings at once.

## What is proved (generic `[Field R]`, no numerical value)

* `conj_gen0`, `conj_gen1`: the flavour flip composed with strand reversal,
  `φ(a, b, c) = (c̄, b̄, ā)`, carries a typed letter on the first crossing with scalars `(α, β)`
  to a typed letter on the second crossing with scalars `(β, α)` and the same mixed block — i.e.
  to the **reversed** typed letter on the other generator.
* `trW_two_eq_trW_one_conj`: `φ` exchanges the proton weight space `W_p` (one `d`) and the
  neutron weight space `W_n` (two `d`).
* `typed_V_pow_trW_eq`: for the typed γγ word `Vᵏ = (σ₀σ₁⁻¹)ᵏ`, every `k`, the plain traces on
  `W_p` and `W_n` are **equal**. Since `γγ` words on three strands are exactly the powers of the
  vertex `V = σ₀σ₁⁻¹`, this is every γγ word on `H₃`.
* `typed_V_pow_tau_ratio`: with the `K`-weight `K = diag(q, q⁻¹)` on each strand,
  `τ_p = q² · τ_n`. The typed letters contribute a factor **exactly 1**; the split stays the
  `K`-weight cell `2E₀·log q`.

## What is NOT claimed

* Extra quark letters placed by hand outside the γγ word (odd length, not γγ-producible,
  `NucleonDownQuarkStrand.quark_letter_not_gammaGamma`). Their placement is not ruled; the probe
  `computations/probes/nucleon_flavour_typed_letters/` measures them and finds the result
  depends on the placement.
* Interface letters between nucleon blocks on the tower (the nuclear word is not ruled, #7876).
-/

namespace QOU.Nuclear.NucleonFlavourTypedLetters

open Matrix

variable {R : Type*} [CommRing R]

/-- Two-strand states `(a, b)`, `0 = u`, `1 = d`. -/
abbrev S2 := Fin 2 × Fin 2
/-- Three-strand states `(a, b, c)`. -/
abbrev S3 := Fin 2 × Fin 2 × Fin 2

/-- A flavour-typed letter on `V ⊗ V`: scalar `α` on `uu`, `β` on `dd`, block `m` on the mixed
states (a mixed state `(a, ā)` is indexed by its first entry `a`). -/
def typed (α β : R) (m : Matrix (Fin 2) (Fin 2) R) : Matrix S2 S2 R :=
  fun s t =>
    if s.1 = s.2 then (if t = s then (if s.1 = 0 then α else β) else 0)
    else (if t.1 ≠ t.2 then m s.1 t.1 else 0)

/-- The letter on the first crossing (strands 0, 1). -/
def gen0 (T : Matrix S2 S2 R) : Matrix S3 S3 R :=
  fun s t => if s.2.2 = t.2.2 then T (s.1, s.2.1) (t.1, t.2.1) else 0

/-- The letter on the second crossing (strands 1, 2). -/
def gen1 (T : Matrix S2 S2 R) : Matrix S3 S3 R :=
  fun s t => if s.1 = t.1 then T s.2 t.2 else 0

/-- Flavour flip `u ↔ d` on one strand. -/
def fl (x : Fin 2) : Fin 2 := 1 - x

theorem fl_fl (x : Fin 2) : fl (fl x) = x := by fin_cases x <;> rfl

/-- Flavour flip composed with strand reversal, `(a, b, c) ↦ (c̄, b̄, ā)`; an involution. -/
def φ : S3 ≃ S3 where
  toFun s := (fl s.2.2, fl s.2.1, fl s.1)
  invFun s := (fl s.2.2, fl s.2.1, fl s.1)
  left_inv s := by simp [fl_fl]
  right_inv s := by simp [fl_fl]

/-- Conjugation by `φ`. -/
def conj (X : Matrix S3 S3 R) : Matrix S3 S3 R := X.submatrix φ φ

theorem conj_mul (X Y : Matrix S3 S3 R) : conj (X * Y) = conj X * conj Y := by
  unfold conj
  rw [Matrix.submatrix_mul_equiv]

theorem conj_pow (X : Matrix S3 S3 R) (k : ℕ) : conj (X ^ k) = conj X ^ k := by
  induction k with
  | zero =>
    ext s t
    simp only [conj, pow_zero, submatrix_apply, one_apply, EmbeddingLike.apply_eq_iff_eq]
  | succ k ih => rw [pow_succ, conj_mul, ih, pow_succ]

/-- **Flip ∘ reversal carries a typed first letter to the reversed typed second letter.** -/
theorem conj_gen0 (α β : R) (m : Matrix (Fin 2) (Fin 2) R) :
    conj (gen0 (typed α β m)) = gen1 (typed β α m) := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;> simp [conj, gen0, gen1, typed, φ, fl]

/-- The same for the second letter. -/
theorem conj_gen1 (α β : R) (m : Matrix (Fin 2) (Fin 2) R) :
    conj (gen1 (typed α β m)) = gen0 (typed β α m) := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;> simp [conj, gen0, gen1, typed, φ, fl]

/-- Number of down strands. -/
def nd (s : S3) : ℕ := s.1.val + s.2.1.val + s.2.2.val

/-- Projector on the weight space with `k` down strands. -/
def proj (k : ℕ) : Matrix S3 S3 R := Matrix.diagonal fun s => if nd s = k then 1 else 0

/-- Plain trace on the weight space with `k` down strands (`k = 1`: `W_p`, `k = 2`: `W_n`). -/
def trW (k : ℕ) (X : Matrix S3 S3 R) : R := (proj k * X).trace

theorem trW_two_eq_trW_one_conj (X : Matrix S3 S3 R) : trW 2 X = trW 1 (conj X) := by
  simp only [trW, proj, conj, Matrix.trace, Matrix.diag, Matrix.diagonal_mul,
    Matrix.submatrix_apply, Fintype.sum_prod_type, Fin.sum_univ_two, φ, nd, fl]
  simp
  ring

theorem proj_comm_gen0 (k : ℕ) (α β : R) (m : Matrix (Fin 2) (Fin 2) R) :
    proj k * gen0 (typed α β m) = gen0 (typed α β m) * proj k := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  simp only [proj, Matrix.diagonal_mul, Matrix.mul_diagonal]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;> simp [gen0, typed, nd]

theorem proj_comm_gen1 (k : ℕ) (α β : R) (m : Matrix (Fin 2) (Fin 2) R) :
    proj k * gen1 (typed α β m) = gen1 (typed α β m) * proj k := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  simp only [proj, Matrix.diagonal_mul, Matrix.mul_diagonal]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;> simp [gen1, typed, nd]

/-- Restricted trace is cyclic for a two-letter word when the letters preserve the weight. -/
theorem trW_pow_swap (k n : ℕ) (A B : Matrix S3 S3 R)
    (hA : proj k * A = A * proj k) :
    trW k ((B * A) ^ (n + 1)) = trW k ((A * B) ^ (n + 1)) := by
  have hsemi : B * (A * B) ^ n = (B * A) ^ n * B := by
    have : SemiconjBy B (A * B) (B * A) := by
      unfold SemiconjBy; simp [mul_assoc]
    exact (this.pow_right n).eq
  have h1 : (B * A) ^ (n + 1) = B * (A * B) ^ n * A := by
    rw [pow_succ, hsemi]; simp [mul_assoc]
  unfold trW
  rw [h1]
  calc (proj k * (B * (A * B) ^ n * A)).trace
      = (A * (proj k * (B * (A * B) ^ n))).trace := by
        rw [show proj k * (B * (A * B) ^ n * A) = (proj k * (B * (A * B) ^ n)) * A by
          simp [mul_assoc], Matrix.trace_mul_comm]
    _ = (proj k * (A * (B * (A * B) ^ n))).trace := by
        rw [← mul_assoc A, ← hA, mul_assoc]
    _ = (proj k * (A * B) ^ (n + 1)).trace := by
        rw [pow_succ']; simp [mul_assoc]

/-- The typed γγ vertex `V = σ₀ σ₁⁻¹`: typed `σ` on the first crossing (`α, β`), typed `σ⁻¹`
(scalars swapped, same mixed block) on the second. -/
def typedV (α β : R) (m : Matrix (Fin 2) (Fin 2) R) : Matrix S3 S3 R :=
  gen0 (typed α β m) * gen1 (typed β α m)

/-- **Main identity.** For every typed γγ word `Vᵏ` on three strands, the plain traces on the
proton and neutron weight spaces are equal, for every typing `α, β, m`. -/
theorem typed_V_pow_trW_eq (α β : R) (m : Matrix (Fin 2) (Fin 2) R) (k : ℕ) :
    trW 1 (typedV α β m ^ k) = trW 2 (typedV α β m ^ k) := by
  rw [trW_two_eq_trW_one_conj, conj_pow, typedV, conj_mul, conj_gen0, conj_gen1]
  cases k with
  | zero => simp
  | succ n =>
    exact (trW_pow_swap 1 n (gen0 (typed α β m)) (gen1 (typed β α m))
      (proj_comm_gen0 1 α β m)).symm

/-- `K`-weight of a state: `K = diag(q, q⁻¹)` on each strand for a unit `q : Rˣ`. -/
def kw (q : Rˣ) (s : S3) : R := (q : R) ^ (3 - nd s) * (↑q⁻¹ : R) ^ nd s

/-- `K`-weighted trace on the weight space with `k` down strands. -/
def tau (q : Rˣ) (k : ℕ) (X : Matrix S3 S3 R) : R :=
  (proj k * Matrix.diagonal (kw q) * X).trace

theorem tau_eq_kw_trW (q : Rˣ) (k : ℕ) (_hk : k ≤ 3) (X : Matrix S3 S3 R) :
    tau q k X = (q : R) ^ (3 - k) * (↑q⁻¹ : R) ^ k * trW k X := by
  simp only [tau, trW, proj, Matrix.diagonal_mul_diagonal, Matrix.trace, Matrix.diag,
    Matrix.diagonal_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun s _ => ?_
  by_cases h : nd s = k
  · simp [h, kw]
  · simp [h]

/-- **No second flavour factor.** For every typed γγ word on three strands and every typing
(raw or framing-corrected), `τ_p = q² · τ_n`: the typed letters contribute exactly `1`, and the
split is the `K`-weight cell alone. -/
theorem typed_V_pow_tau_ratio (q : Rˣ) (α β : R)
    (m : Matrix (Fin 2) (Fin 2) R) (k : ℕ) :
    tau q 1 (typedV α β m ^ k) = (q : R) ^ 2 * tau q 2 (typedV α β m ^ k) := by
  rw [tau_eq_kw_trW q 1 (by norm_num), tau_eq_kw_trW q 2 (by norm_num), typed_V_pow_trW_eq]
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := Units.mul_inv q
  calc
    (q : R) ^ (3 - 1) * (↑q⁻¹ : R) ^ 1 * trW 2 (typedV α β m ^ k)
        = (q : R) ^ 2 * (↑q⁻¹ : R) * ((q : R) * (↑q⁻¹ : R)) * trW 2 (typedV α β m ^ k) := by
          rw [hq]; ring
    _ = (q : R) ^ 2 * ((q : R) ^ (3 - 2) * (↑q⁻¹ : R) ^ 2 * trW 2 (typedV α β m ^ k)) := by
          ring

/-! ## The two readings are instances -/

/-- Raw-trace typing of `σ`: `uu ↦ q`, `dd ↦ q⁻¹` (`σ⁻¹` on `dd`). -/
def rawScalars (q : Rˣ) : R × R := ((q : R), (↑q⁻¹ : R))

/-- Framing-corrected typing of `σ` (writhe weight `q^{∓2}` per signed crossing):
`uu ↦ q⁻²·q`, `dd ↦ q²·q⁻¹`. -/
def corrScalars (q : Rˣ) : R × R := ((↑q⁻¹ : R) ^ 2 * (q : R), (q : R) ^ 2 * (↑q⁻¹ : R))

theorem corrScalars_eq (q : Rˣ) : corrScalars q = ((↑q⁻¹ : R), (q : R)) := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := Units.mul_inv q
  simp only [corrScalars, Prod.mk.injEq]
  exact ⟨by linear_combination (↑q⁻¹ : R) * hq, by linear_combination (q : R) * hq⟩

/-- The corrected typing swaps the raw scalars: the writhe weight turns the `uu`/`dd` diagonal
ratio `q²` of one typed letter into `q⁻²`. -/
theorem corrScalars_swap_raw (q : Rˣ) :
    corrScalars q = ((rawScalars q).2, (rawScalars q).1) := by
  rw [corrScalars_eq q]; rfl

end QOU.Nuclear.NucleonFlavourTypedLetters
