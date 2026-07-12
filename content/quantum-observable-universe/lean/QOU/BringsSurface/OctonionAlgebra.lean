import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Module.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.BringsSurface.OctonionAlgebra

**The octonions as an explicit Cayley–Dickson tower over `ℝ` — self-contained.**

Mathlib (as restored in the qou olean cache) carries no `Octonion`, no
`CayleyDickson`, and no `G₂`. This file builds the tower `ℝ → ℂ → ℍ → 𝕆` by hand
from the Cayley–Dickson doubling `(a,b)·(c,d) = (a·c − conj d·b, d·a + b·conj c)`,
`conj(a,b) = (conj a, −b)`, so the octonion product is a concrete real-coordinate
object every downstream lemma can compute with.

The tower is the classical **degradation ladder**: each doubling drops one
property.

| level | doubling | commutative | associative | typeclass |
|---|---|---|---|---|
| `ℝ` | — | ✓ | ✓ | `CommRing` |
| `Cplx = CD ℝ` | ✓ | ✓ | ✓ | `CommRing` |
| `Quat = CD Cplx` | ✓ | **✗** | ✓ | `Ring` |
| `Oct = CD Quat` | ✓ | ✗ | **✗** | `AddCommGroup` + `Mul` |

**Typeclass strategy (per Gemini review on PR #3671).** Each level carries the
strongest *standard* Mathlib algebraic instance it honestly supports, so `+`,
`*`, `0`, `1`, `-` are the ordinary notation and `ring` discharges the
associative/commutative levels: `Cplx` is a `CommRing`, `Quat` is a
(non-commutative) `Ring`. `Oct` is genuinely **non-associative**, so `Ring` is
*impossible* — it gets the full additive `AddCommGroup` (this is the `ℝ`-vector
space structure the Tier-3 `Der(𝕆)` linear algebra needs) plus a bare `Mul`/`One`
for the product. The instances are built in the standard Mathlib idiom (separate
`Add`/`Mul`/… instances, `@[simp]` `rfl` component lemmas, then the algebraic
instance whose axioms fall to `ext <;> simp <;> ring`).

This file (PR #3671, Tier 1) builds the tower with the two ladder witnesses:
`Quat.quat_noncomm` (ℍ non-commutative, `i·j = k ≠ −k = j·i`) and
`Oct.oct_nonassoc` (`(e_i·e_j)·e_ℓ ≠ e_i·(e_j·e_ℓ)`, the non-associativity whose
sign structure is the `det3` cocycle of `OctonionCocycle`). The norm / imaginary
part / `S⁶` sphere (Tier 2) and the `Aut(𝕆) = G₂` / `Der(𝕆)` linear algebra
(Tier 3) follow. The norm and `S⁶` are archimedean; everything here is over `ℝ`
(§7c), sorry-free.

-- Ref: [albuquerque-majid1999] https://arxiv.org/abs/math/9802116
-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionAlgebra

/-! ## Level 1 — `Cplx = CD ℝ` (the complex numbers) -/

/-- Complex numbers as the Cayley–Dickson double of `ℝ` (conjugation on `ℝ` is the
identity). -/
@[ext] structure Cplx where
  re : ℝ
  im : ℝ

namespace Cplx

/-- The imaginary unit `i`. -/
def I : Cplx := ⟨0, 1⟩
/-- Cayley–Dickson conjugation `(a, b) ↦ (a, −b)`. -/
def conj (x : Cplx) : Cplx := ⟨x.re, -x.im⟩
/-- The squared norm `|x|² = a² + b²` (the base of the composition-algebra norm). -/
def normSq (x : Cplx) : ℝ := x.re ^ 2 + x.im ^ 2

instance : Zero Cplx := ⟨⟨0, 0⟩⟩
instance : One Cplx := ⟨⟨1, 0⟩⟩
instance : Add Cplx := ⟨fun x y => ⟨x.re + y.re, x.im + y.im⟩⟩
instance : Neg Cplx := ⟨fun x => ⟨-x.re, -x.im⟩⟩
instance : Sub Cplx := ⟨fun x y => ⟨x.re - y.re, x.im - y.im⟩⟩
/-- Complex multiplication `(a,b)·(c,d) = (ac − bd, ad + bc)`. -/
instance : Mul Cplx := ⟨fun x y => ⟨x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re⟩⟩

@[simp] theorem zero_re : (0 : Cplx).re = 0 := rfl
@[simp] theorem zero_im : (0 : Cplx).im = 0 := rfl
@[simp] theorem one_re : (1 : Cplx).re = 1 := rfl
@[simp] theorem one_im : (1 : Cplx).im = 0 := rfl
@[simp] theorem add_re (x y : Cplx) : (x + y).re = x.re + y.re := rfl
@[simp] theorem add_im (x y : Cplx) : (x + y).im = x.im + y.im := rfl
@[simp] theorem sub_re (x y : Cplx) : (x - y).re = x.re - y.re := rfl
@[simp] theorem sub_im (x y : Cplx) : (x - y).im = x.im - y.im := rfl
@[simp] theorem neg_re (x : Cplx) : (-x).re = -x.re := rfl
@[simp] theorem neg_im (x : Cplx) : (-x).im = -x.im := rfl
@[simp] theorem mul_re (x y : Cplx) : (x * y).re = x.re * y.re - x.im * y.im := rfl
@[simp] theorem mul_im (x y : Cplx) : (x * y).im = x.re * y.im + x.im * y.re := rfl
@[simp] theorem conj_re (x : Cplx) : (conj x).re = x.re := rfl
@[simp] theorem conj_im (x : Cplx) : (conj x).im = -x.im := rfl
@[simp] theorem I_re : I.re = 0 := rfl
@[simp] theorem I_im : I.im = 1 := rfl

/-- `Cplx` is a commutative ring — the base of the tower is fully associative and
commutative, so `ring` discharges every `Cplx` identity. -/
instance : CommRing Cplx where
  add := (· + ·); zero := 0; neg := (- ·); sub := (· - ·); one := 1; mul := (· * ·)
  nsmul := nsmulRec; zsmul := zsmulRec
  add_assoc a b c := by ext <;> simp <;> ring
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  add_comm a b := by ext <;> simp <;> ring
  neg_add_cancel a := by ext <;> simp
  sub_eq_add_neg a b := by ext <;> simp <;> ring
  mul_assoc a b c := by ext <;> simp <;> ring
  one_mul a := by ext <;> simp
  mul_one a := by ext <;> simp
  mul_comm a b := by ext <;> simp <;> ring
  left_distrib a b c := by ext <;> simp <;> ring
  right_distrib a b c := by ext <;> simp <;> ring
  zero_mul a := by ext <;> simp
  mul_zero a := by ext <;> simp

/-- Real scalar multiplication, componentwise. -/
instance : SMul ℝ Cplx := ⟨fun r x => ⟨r * x.re, r * x.im⟩⟩
@[simp] theorem smul_re (r : ℝ) (x : Cplx) : (r • x).re = r * x.re := rfl
@[simp] theorem smul_im (r : ℝ) (x : Cplx) : (r • x).im = r * x.im := rfl

/-- `Cplx` is an `ℝ`-module (the vector space `ℝ²`). -/
instance : Module ℝ Cplx where
  smul := (· • ·)
  one_smul a := by ext <;> simp
  mul_smul r s a := by ext <;> simp <;> ring
  smul_zero r := by ext <;> simp
  smul_add r a b := by ext <;> simp <;> ring
  add_smul r s a := by ext <;> simp <;> ring
  zero_smul a := by ext <;> simp

end Cplx

/-! ## Level 2 — `Quat = CD Cplx` (the quaternions `ℍ`) -/

/-- Quaternions as the Cayley–Dickson double of `Cplx`. An element `⟨x, y⟩`
represents `x + y·j` with `x, y : Cplx`. -/
@[ext] structure Quat where
  fst : Cplx
  snd : Cplx

namespace Quat

/-- The quaternion unit `i` (the imaginary unit of the base `Cplx`). -/
def qi : Quat := ⟨Cplx.I, 0⟩
/-- The quaternion unit `j` (the Cayley–Dickson doubling generator). -/
def qj : Quat := ⟨0, 1⟩
/-- Cayley–Dickson conjugation `(x, y) ↦ (conj x, −y)`. -/
def conj (p : Quat) : Quat := ⟨Cplx.conj p.fst, -p.snd⟩
/-- The squared norm `|p|² = |x|² + |y|²` of a quaternion `⟨x, y⟩`. -/
def normSq (p : Quat) : ℝ := Cplx.normSq p.fst + Cplx.normSq p.snd

instance : Zero Quat := ⟨⟨0, 0⟩⟩
instance : One Quat := ⟨⟨1, 0⟩⟩
instance : Add Quat := ⟨fun p q => ⟨p.fst + q.fst, p.snd + q.snd⟩⟩
instance : Neg Quat := ⟨fun p => ⟨-p.fst, -p.snd⟩⟩
instance : Sub Quat := ⟨fun p q => ⟨p.fst - q.fst, p.snd - q.snd⟩⟩
/-- Cayley–Dickson multiplication over `Cplx`:
`(x,y)·(z,w) = (x·z − conj w·y, w·x + y·conj z)`. -/
instance : Mul Quat :=
  ⟨fun p q => ⟨p.fst * q.fst - Cplx.conj q.snd * p.snd, q.snd * p.fst + p.snd * Cplx.conj q.fst⟩⟩

@[simp] theorem zero_fst : (0 : Quat).fst = 0 := rfl
@[simp] theorem zero_snd : (0 : Quat).snd = 0 := rfl
@[simp] theorem one_fst : (1 : Quat).fst = 1 := rfl
@[simp] theorem one_snd : (1 : Quat).snd = 0 := rfl
@[simp] theorem add_fst (p q : Quat) : (p + q).fst = p.fst + q.fst := rfl
@[simp] theorem add_snd (p q : Quat) : (p + q).snd = p.snd + q.snd := rfl
@[simp] theorem sub_fst (p q : Quat) : (p - q).fst = p.fst - q.fst := rfl
@[simp] theorem sub_snd (p q : Quat) : (p - q).snd = p.snd - q.snd := rfl
@[simp] theorem neg_fst (p : Quat) : (-p).fst = -p.fst := rfl
@[simp] theorem neg_snd (p : Quat) : (-p).snd = -p.snd := rfl
@[simp] theorem mul_fst (p q : Quat) :
    (p * q).fst = p.fst * q.fst - Cplx.conj q.snd * p.snd := rfl
@[simp] theorem mul_snd (p q : Quat) :
    (p * q).snd = q.snd * p.fst + p.snd * Cplx.conj q.fst := rfl
@[simp] theorem conj_fst (p : Quat) : (conj p).fst = Cplx.conj p.fst := rfl
@[simp] theorem conj_snd (p : Quat) : (conj p).snd = -p.snd := rfl

/-- `Quat` is a (non-commutative) ring: the Cayley–Dickson double of a commutative
ring is associative but no longer commutative. -/
instance : Ring Quat where
  add := (· + ·); zero := 0; neg := (- ·); sub := (· - ·); one := 1; mul := (· * ·)
  nsmul := nsmulRec; zsmul := zsmulRec
  add_assoc a b c := by ext <;> simp <;> ring
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  add_comm a b := by ext <;> simp <;> ring
  neg_add_cancel a := by ext <;> simp
  sub_eq_add_neg a b := by ext <;> simp <;> ring
  mul_assoc a b c := by ext <;> simp <;> ring
  one_mul a := by ext <;> simp
  mul_one a := by ext <;> simp
  left_distrib a b c := by ext <;> simp <;> ring
  right_distrib a b c := by ext <;> simp <;> ring
  zero_mul a := by ext <;> simp
  mul_zero a := by ext <;> simp

/-- **`ℍ` is non-commutative** (first degradation of the ladder). `i·j = k` but
`j·i = −k`: the `.snd.im` coordinate is `+1` on `i·j` and `−1` on `j·i`. -/
theorem quat_noncomm : qi * qj ≠ qj * qi := by
  intro h
  have hc := congrArg (fun p => p.snd.im) h
  simp [qi, qj] at hc
  norm_num at hc

/-- Real scalar multiplication, componentwise. -/
instance : SMul ℝ Quat := ⟨fun r p => ⟨r • p.fst, r • p.snd⟩⟩
@[simp] theorem smul_fst (r : ℝ) (p : Quat) : (r • p).fst = r • p.fst := rfl
@[simp] theorem smul_snd (r : ℝ) (p : Quat) : (r • p).snd = r • p.snd := rfl

/-- `Quat` is an `ℝ`-module (the vector space `ℝ⁴`). -/
instance : Module ℝ Quat where
  smul := (· • ·)
  one_smul a := by ext <;> simp
  mul_smul r s a := by ext <;> simp <;> ring
  smul_zero r := by ext <;> simp
  smul_add r a b := by ext <;> simp <;> ring
  add_smul r s a := by ext <;> simp <;> ring
  zero_smul a := by ext <;> simp

end Quat

/-! ## Level 3 — `Oct = CD Quat` (the octonions `𝕆`) -/

/-- Octonions as the Cayley–Dickson double of `Quat`. An element `⟨p, q⟩`
represents `p + q·ℓ` with `p, q : Quat` and `ℓ` the doubling generator. -/
@[ext] structure Oct where
  fst : Quat
  snd : Quat

namespace Oct

/-- `e_i` — the quaternion unit `i` embedded in `𝕆`. -/
def ei : Oct := ⟨Quat.qi, 0⟩
/-- `e_j` — the quaternion unit `j` embedded in `𝕆`. -/
def ej : Oct := ⟨Quat.qj, 0⟩
/-- `e_ℓ` — the Cayley–Dickson doubling generator (`= (0, 1)`). -/
def el : Oct := ⟨0, 1⟩
/-- Cayley–Dickson conjugation `(p, q) ↦ (conj p, −q)`. -/
def conj (a : Oct) : Oct := ⟨Quat.conj a.fst, -a.snd⟩

instance : Zero Oct := ⟨⟨0, 0⟩⟩
instance : One Oct := ⟨⟨1, 0⟩⟩
instance : Add Oct := ⟨fun a b => ⟨a.fst + b.fst, a.snd + b.snd⟩⟩
instance : Neg Oct := ⟨fun a => ⟨-a.fst, -a.snd⟩⟩
instance : Sub Oct := ⟨fun a b => ⟨a.fst - b.fst, a.snd - b.snd⟩⟩
/-- Cayley–Dickson multiplication over `Quat`:
`(p,q)·(r,s) = (p·r − conj s·q, s·p + q·conj r)`. Non-associative. -/
instance : Mul Oct :=
  ⟨fun a b => ⟨a.fst * b.fst - Quat.conj b.snd * a.snd, b.snd * a.fst + a.snd * Quat.conj b.fst⟩⟩

@[simp] theorem zero_fst : (0 : Oct).fst = 0 := rfl
@[simp] theorem zero_snd : (0 : Oct).snd = 0 := rfl
@[simp] theorem one_fst : (1 : Oct).fst = 1 := rfl
@[simp] theorem one_snd : (1 : Oct).snd = 0 := rfl
@[simp] theorem add_fst (a b : Oct) : (a + b).fst = a.fst + b.fst := rfl
@[simp] theorem add_snd (a b : Oct) : (a + b).snd = a.snd + b.snd := rfl
@[simp] theorem sub_fst (a b : Oct) : (a - b).fst = a.fst - b.fst := rfl
@[simp] theorem sub_snd (a b : Oct) : (a - b).snd = a.snd - b.snd := rfl
@[simp] theorem neg_fst (a : Oct) : (-a).fst = -a.fst := rfl
@[simp] theorem neg_snd (a : Oct) : (-a).snd = -a.snd := rfl
@[simp] theorem mul_fst (a b : Oct) :
    (a * b).fst = a.fst * b.fst - Quat.conj b.snd * a.snd := rfl
@[simp] theorem mul_snd (a b : Oct) :
    (a * b).snd = b.snd * a.fst + a.snd * Quat.conj b.fst := rfl
@[simp] theorem conj_fst (a : Oct) : (conj a).fst = Quat.conj a.fst := rfl
@[simp] theorem conj_snd (a : Oct) : (conj a).snd = -a.snd := rfl

/-- `𝕆` is an additive commutative group. This is the `ℝ`-vector-space structure
(`𝕆 ≅ ℝ⁸`) that the Tier-3 `Der(𝕆)` linear algebra will use. `𝕆` is **not** a
`Ring` — its multiplication is non-associative (`oct_nonassoc`). -/
instance : AddCommGroup Oct where
  add := (· + ·); zero := 0; neg := (- ·); sub := (· - ·)
  nsmul := nsmulRec; zsmul := zsmulRec
  add_assoc a b c := by ext <;> simp <;> ring
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  add_comm a b := by ext <;> simp <;> ring
  neg_add_cancel a := by ext <;> simp
  sub_eq_add_neg a b := by ext <;> simp <;> ring

/-- **`𝕆` is non-associative** (final degradation of the ladder). On the classic
triple `e_i, e_j, e_ℓ`: `(e_i·e_j)·e_ℓ` and `e_i·(e_j·e_ℓ)` differ by a sign
(the `.snd.snd.im` coordinate is `+1` versus `−1`). This is exactly the
non-associativity whose `(ℤ/2)³` sign structure is the `det3` cocycle of
`OctonionCocycle`. -/
theorem oct_nonassoc : (ei * ej) * el ≠ ei * (ej * el) := by
  intro h
  have hc := congrArg (fun a => a.snd.snd.im) h
  simp [ei, ej, el, Quat.qi, Quat.qj] at hc
  norm_num at hc

/-! ### Tier 2 — norm, imaginary part, and the unit imaginary sphere `S⁶` -/

/-- The squared norm `|a|² = |p|² + |q|²` of an octonion `⟨p, q⟩` — the sum of the
squares of all eight real coordinates. -/
def normSq (a : Oct) : ℝ := Quat.normSq a.fst + Quat.normSq a.snd

/-- The real part `Re(a)` of an octonion — its coefficient of `1` (the first of the
eight coordinates). -/
def re (a : Oct) : ℝ := a.fst.fst.re

/-- **The squared norm is non-negative** (a sum of eight real squares). Positivity
of `|·|²` is what makes `S⁶` a genuine sphere. -/
theorem normSq_nonneg (a : Oct) : 0 ≤ normSq a := by
  simp only [normSq, Quat.normSq, Cplx.normSq]
  positivity

/-- **An octonion is imaginary iff `conj a = −a`** — the structural (basis-free)
characterization of `Im 𝕆`, the `7`-dimensional orthogonal complement of `1`.
Equivalently `Re(a) = 0`. -/
def IsImaginary (a : Oct) : Prop := conj a = -a

/-- The **unit imaginary sphere** `S⁶ = {x ∈ Im 𝕆 : |x|² = 1}` — the round
`6`-sphere of unit imaginary octonions. `G₂ = Aut(𝕆)` acts on it (Tier 3/4:
transitively, with stabilizer `SU(3)`, so `S⁶ = G₂/SU(3)`). -/
def S6 (a : Oct) : Prop := IsImaginary a ∧ normSq a = 1

/-- `e_i` is a unit imaginary octonion (`conj e_i = −e_i`, `|e_i|² = 1`): it lies on
`S⁶`. -/
theorem ei_mem_S6 : S6 ei := by
  refine ⟨?_, ?_⟩
  · show conj ei = -ei
    ext <;> simp [conj, ei, Quat.conj, Quat.qi, Cplx.conj, Cplx.I]
  · simp [normSq, ei, Quat.normSq, Quat.qi, Cplx.normSq, Cplx.I]

/-- `e_ℓ`, the Cayley–Dickson doubling generator, is a unit imaginary octonion: it
too lies on `S⁶`. -/
theorem el_mem_S6 : S6 el := by
  refine ⟨?_, ?_⟩
  · show conj el = -el
    ext <;> simp [conj, el, Quat.conj, Cplx.conj]
  · simp [normSq, el, Quat.normSq, Cplx.normSq]

/-- **`1` is not imaginary** — `Re(1) = 1 ≠ 0`, so the multiplicative unit is not
on `S⁶`. (A sanity check that `IsImaginary` really cuts out the complement of the
real line.) -/
theorem one_not_imaginary : ¬ IsImaginary (1 : Oct) := by
  intro h
  have hc := congrArg (fun a => a.fst.fst.re) h
  simp [conj, Quat.conj, Cplx.conj] at hc
  norm_num at hc

/-- Real scalar multiplication, componentwise. -/
instance : SMul ℝ Oct := ⟨fun r a => ⟨r • a.fst, r • a.snd⟩⟩
@[simp] theorem smul_fst (r : ℝ) (a : Oct) : (r • a).fst = r • a.fst := rfl
@[simp] theorem smul_snd (r : ℝ) (a : Oct) : (r • a).snd = r • a.snd := rfl

/-- **`𝕆` is an `ℝ`-module** — the vector space `ℝ⁸` on which `Der(𝕆)` (Tier 3)
lives as a linear subspace of `𝕆 →ₗ[ℝ] 𝕆`. This is the structure that makes the
`dim 𝔤₂ = dim Der(𝕆) = 14` computation a finite linear-algebra problem. -/
instance : Module ℝ Oct where
  smul := (· • ·)
  one_smul a := by ext <;> simp
  mul_smul r s a := by ext <;> simp <;> ring
  smul_zero r := by ext <;> simp
  smul_add r a b := by ext <;> simp <;> ring
  add_smul r s a := by ext <;> simp <;> ring
  zero_smul a := by ext <;> simp

/-! ### Bilinearity of the octonion product

`𝕆`'s multiplication is `ℝ`-bilinear (it distributes over `+` and commutes with
the scalar action on either side) — even though it is not associative. These are
the facts the Tier-3 `Der(𝕆)` submodule-closure proofs need. -/

theorem mul_add (a b c : Oct) : a * (b + c) = a * b + a * c := by ext <;> simp <;> ring
theorem add_mul (a b c : Oct) : (a + b) * c = a * c + b * c := by ext <;> simp <;> ring
theorem zero_mul (a : Oct) : 0 * a = 0 := by ext <;> simp
theorem mul_zero (a : Oct) : a * 0 = 0 := by ext <;> simp
theorem smul_mul (r : ℝ) (a b : Oct) : (r • a) * b = r • (a * b) := by ext <;> simp <;> ring
theorem mul_smul (r : ℝ) (a b : Oct) : a * (r • b) = r • (a * b) := by ext <;> simp <;> ring

end Oct

end QOU.BringsSurface.OctonionAlgebra
