import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Complex.Basic

/-!
# Hecke crossed module h² trace = dim(V) · χ(Bring)

The Q₈ crossed module for the Borromean braid (σ₁σ₂⁻¹)³ has h²
curvature trace = −12 = 2 · (−6) = dim(V) · χ(Σ₄), where Σ₄ is
Bring's surface (genus 4, Euler characteristic −6).

The proof is finite combinatorics: enumerate 15 pairwise products
of 6 quaternion matrices, sum, trace.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-/

open Matrix Complex

-- ── Pure ℤ computation (avoids noncomputable ℂ) ──────────────────
-- The Q₈ 2×2 matrices over ℤ[i] have entries in {0, ±1, ±i}.
-- We work over ℤ × ℤ (representing a + bi) to keep everything
-- computable / decidable.

/-- Gaussian integer a + bi as (a, b). -/
abbrev GaussInt := ℤ × ℤ

instance : Add GaussInt := ⟨fun ⟨a, b⟩ ⟨c, d⟩ => (a + c, b + d)⟩
instance : Neg GaussInt := ⟨fun ⟨a, b⟩ => (-a, -b)⟩
instance : Mul GaussInt := ⟨fun ⟨a, b⟩ ⟨c, d⟩ => (a*c - b*d, a*d + b*c)⟩
instance : Zero GaussInt := ⟨(0, 0)⟩
instance : One GaussInt := ⟨(1, 0)⟩

/-- The imaginary unit i = (0, 1). -/
def gi : GaussInt := (0, 1)

/-- 2×2 matrix over Gaussian integers. -/
abbrev M2 := Fin 2 → Fin 2 → GaussInt

def m2_mul (A B : M2) : M2 := fun i j =>
  A i 0 * B 0 j + A i 1 * B 1 j

def m2_add (A B : M2) : M2 := fun i j =>
  A i j + B i j

def m2_neg (A : M2) : M2 := fun i j =>
  -A i j

def m2_zero : M2 := fun _ _ => (0, 0)

def m2_smul (s : ℤ) (A : M2) : M2 := fun i j =>
  ((s, 0) : GaussInt) * A i j

def m2_trace (A : M2) : GaussInt :=
  A 0 0 + A 1 1

-- ── Q₈ matrices ──────────────────────────────────────────────────

/-- Quaternion i = [[i, 0], [0, -i]]. -/
def qi_m : M2 := fun
  | 0, 0 => gi
  | 0, 1 => (0, 0)
  | 1, 0 => (0, 0)
  | 1, 1 => -gi

/-- Quaternion j = [[0, 1], [-1, 0]]. -/
def qj_m : M2 := fun
  | 0, 0 => (0, 0)
  | 0, 1 => (1, 0)
  | 1, 0 => (-1, 0)
  | 1, 1 => (0, 0)

/-- The 6 Borromean crossing Q₈ images: [i, −j, i, −j, i, −j]. -/
def crossings : Fin 6 → M2
  | 0 => qi_m
  | 1 => m2_neg qj_m
  | 2 => qi_m
  | 3 => m2_neg qj_m
  | 4 => qi_m
  | 5 => m2_neg qj_m

/-- Crossing signs: [+1, −1, +1, −1, +1, −1]. -/
def signs : Fin 6 → ℤ
  | 0 => 1
  | 1 => -1
  | 2 => 1
  | 3 => -1
  | 4 => 1
  | 5 => -1

/-- Compute the h² curvature sum: Σ_{k<l} s_k s_l c_k c_l. -/
def h2Sum : M2 :=
  let pairs : List (Fin 6 × Fin 6) :=
    List.flatten (List.ofFn fun k =>
      List.ofFn fun l =>
        (k, l))
  pairs.foldl (fun acc ⟨k, l⟩ =>
    if k.val < l.val then
      m2_add acc (m2_smul (signs k * signs l) (m2_mul (crossings k) (crossings l)))
    else acc
  ) m2_zero

/-- The Euler characteristic of Bring's surface (genus 4). -/
def euler_bring : ℤ := 2 - 2 * 4  -- = −6

/-- The dimension of the fundamental representation V = ℂ². -/
def dim_V : ℤ := 2

-- ── The theorems ─────────────────────────────────────────────────

/-- The trace of the h² curvature sum equals (−12, 0) as a
    Gaussian integer, i.e. −12 ∈ ℤ ⊂ ℤ[i]. -/
theorem h2_curvature_trace :
    m2_trace h2Sum = ((-12 : ℤ), (0 : ℤ)) := by decide

/-- The main identity: tr(h² curvature) = dim(V) · χ(Σ₄).
    Both sides are −12 (as a real integer, imaginary part 0). -/
theorem crossed_module_euler_characteristic :
    m2_trace h2Sum = ((dim_V * euler_bring : ℤ), (0 : ℤ)) := by decide

/-- The first component of the curvature trace minus the product of dimension and genus-four Euler characteristic vanishes (`qou-j9yk`). -/
theorem h2_curvature_trace_fst_sub_eq_zero :
    (m2_trace h2Sum).1 - dim_V * euler_bring = 0 := by
  rw [crossed_module_euler_characteristic, sub_self]
