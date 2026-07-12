import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.BringsSurface.OctonionAlgebra

**The octonions as an explicit Cayley–Dickson tower over `ℝ` — self-contained.**

Mathlib (as restored in the qou olean cache) carries no `Octonion`, no
`CayleyDickson`, and no `G₂`. This file builds the tower `ℝ → ℂ → ℍ → 𝕆` by hand
from the Cayley–Dickson doubling `(a,b)·(c,d) = (a·c − conj d·b, d·a + b·conj c)`,
`conj(a,b) = (conj a, −b)`, so the octonion product is a concrete real-coordinate
object every downstream lemma can compute with (`ring` / `norm_num`).

The tower is the classical **degradation ladder**: each doubling drops one
property.

| level | doubling | commutative | associative |
|---|---|---|---|
| `ℝ` | — | ✓ | ✓ |
| `Cplx = CD ℝ` | ✓ | ✓ | ✓ |
| `Quat = CD Cplx` | ✓ | **✗** | ✓ |
| `Oct = CD Quat` | ✓ | ✗ | **✗** |

This file (commit 1) builds `Cplx` and `Quat` and proves the **non-commutativity
of `ℍ`** witness `quat_mul_i_j_ne_j_i` (`i·j = k ≠ −k = j·i`). `Oct`, its
non-associativity witness, the norm / imaginary part / `S⁶` sphere, and the
`Aut(𝕆)` (`= G₂`) scaffold follow in later commits. Everything over `ℝ` (the
norm and `S⁶` are archimedean; §7c), sorry-free.

-- Ref: [albuquerque-majid1999] https://arxiv.org/abs/math/9802116
-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionAlgebra

/-! ## Level 1 — `Cplx = CD ℝ` (the complex numbers) -/

/-- Complex numbers as the Cayley–Dickson double of `ℝ` (conjugation on `ℝ` is the
identity). -/
structure Cplx where
  re : ℝ
  im : ℝ

namespace Cplx

/-- The additive unit `0`. -/
def zero : Cplx := ⟨0, 0⟩
/-- The multiplicative unit `1`. -/
def one : Cplx := ⟨1, 0⟩
/-- The imaginary unit `i`. -/
def I : Cplx := ⟨0, 1⟩
/-- Componentwise addition. -/
def add (x y : Cplx) : Cplx := ⟨x.re + y.re, x.im + y.im⟩
/-- Componentwise negation. -/
def neg (x : Cplx) : Cplx := ⟨-x.re, -x.im⟩
/-- Cayley–Dickson conjugation: `(a, b) ↦ (a, −b)`. -/
def conj (x : Cplx) : Cplx := ⟨x.re, -x.im⟩
/-- Complex multiplication `(a,b)·(c,d) = (ac − bd, ad + bc)`. -/
def mul (x y : Cplx) : Cplx := ⟨x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re⟩

end Cplx

/-! ## Level 2 — `Quat = CD Cplx` (the quaternions `ℍ`) -/

/-- Quaternions as the Cayley–Dickson double of `Cplx`. An element `⟨x, y⟩`
represents `x + y·j` with `x, y : Cplx`. -/
structure Quat where
  fst : Cplx
  snd : Cplx

namespace Quat

/-- The additive unit. -/
def zero : Quat := ⟨Cplx.zero, Cplx.zero⟩
/-- The multiplicative unit `1`. -/
def one : Quat := ⟨Cplx.one, Cplx.zero⟩
/-- The quaternion unit `i` (the imaginary unit of the base `Cplx`). -/
def qi : Quat := ⟨Cplx.I, Cplx.zero⟩
/-- The quaternion unit `j` (the Cayley–Dickson doubling generator). -/
def qj : Quat := ⟨Cplx.zero, Cplx.one⟩
/-- The quaternion unit `k = i·j`. -/
def qk : Quat := ⟨Cplx.zero, Cplx.I⟩
/-- Componentwise addition. -/
def add (p q : Quat) : Quat := ⟨Cplx.add p.fst q.fst, Cplx.add p.snd q.snd⟩
/-- Componentwise negation. -/
def neg (q : Quat) : Quat := ⟨Cplx.neg q.fst, Cplx.neg q.snd⟩
/-- Cayley–Dickson conjugation `(x, y) ↦ (conj x, −y)`. -/
def conj (q : Quat) : Quat := ⟨Cplx.conj q.fst, Cplx.neg q.snd⟩
/-- Cayley–Dickson multiplication over the base `Cplx`:
`(x,y)·(z,w) = (x·z − conj w·y, w·x + y·conj z)`. -/
def mul (p q : Quat) : Quat :=
  ⟨Cplx.add (Cplx.mul p.fst q.fst) (Cplx.neg (Cplx.mul (Cplx.conj q.snd) p.snd)),
   Cplx.add (Cplx.mul q.snd p.fst) (Cplx.mul p.snd (Cplx.conj q.fst))⟩

/-- **`ℍ` is non-commutative.** `i·j = k` but `j·i = −k`, and `k ≠ −k`; concretely
the `.snd.im` coordinate is `1` on `i·j` and `−1` on `j·i`. This is the first
degradation of the Cayley–Dickson ladder (commutativity lost at `ℍ`). -/
theorem quat_mul_i_j_ne_j_i : mul qi qj ≠ mul qj qi := by
  intro h
  have hcoord := congrArg (fun q => q.snd.im) h
  simp only [mul, qi, qj, Cplx.mul, Cplx.conj, Cplx.add, Cplx.neg, Cplx.I,
    Cplx.zero, Cplx.one] at hcoord
  norm_num at hcoord

end Quat

end QOU.BringsSurface.OctonionAlgebra
