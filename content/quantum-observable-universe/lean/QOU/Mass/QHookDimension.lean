/-
  QOU.Mass — F1 q-lift, first brick: the q-hook dimension and its q = 1 collapse.

  The binding q-deformation of the na-Stokes period is
  `S(n) = Σ_{λ ⊢ n} dim_q(λ)`, whose q = 1 shadow is the involution
  (telephone) number `I(n)` (OEIS A000085) via the Frobenius–Schur / RSK
  identity `Σ_{λ ⊢ n} f^λ = I(n)`. See
  `content/quantum-observable-universe/mass-theory/cyclotomic-boundary-at-keystone.md`
  and `binding-period-involution-statistic.md`; the q = 1 shadow `I(n)` is
  formalized in `QOU.Mass.involutionNumber` (PR #4294,
  `card_involutions_eq_involutionNumber`).

  This file builds the reusable q-combinatorics machinery those blocks
  invoke only implicitly (the sibling `binding-period-involution-statistic.lean`
  works with explicit polynomials, not reusable `qInt`/`qFact`/`dimQ`
  functions) and proves the load-bearing q = 1 SPECIALIZATIONS, which are the
  facts that make `S(n)|_{q=1}` collapse:

  * `qIntPoly q n = Σ_{i<n} q^i` — the polynomial (Gaussian) q-integer
    `[n]_q = (q^n − 1)/(q − 1)`, over a generic `CommRing`;
  * `qFactPoly q n = ∏_{i<n} qIntPoly q (i+1)` — the q-factorial `[n]_q!`;
  * `dimQ q n hooks = qFactPoly q n / ∏_{h ∈ hooks} qIntPoly q h` — the
    q-hook dimension of a shape of size `n` with hook multiset `hooks`, over
    a `Field`;
  * their q = 1 collapses: `qIntPoly 1 n = n`, `qFactPoly 1 n = n!`,
    `dimQ 1 n hooks = n! / ∏_{h ∈ hooks} h` — the ordinary hook-length value
    `f^λ = n! / ∏ h(c)`.

  ## Normalization note (why the polynomial, not the balanced, q-integer)

  Corpus canon (`binding-period-involution-statistic.md`) uses the BALANCED
  quantum integer `[k]_bal = (q^k − q^{−k})/(q − q^{−1})`. At literal `q = 1`
  the balanced form is the `0/0` indeterminate (Lean's junk division makes it
  `0`, not `k`), so its q = 1 shadow is only a q → 1 LIMIT statement. The
  polynomial form `qIntPoly q k = Σ_{i<k} q^i` used here is the standard
  rescaling `[k]_bal = q^{−(k−1)} · qIntPoly (q^2) k`; it agrees with the
  balanced form up to an overall `q`-monomial twist (which cancels in the
  hook-length RATIO `dimQ`) and, unlike the balanced form, has a clean LITERAL
  value `qIntPoly 1 k = k` at `q = 1`. This is exactly the collapse the brick
  needs, so the reusable machinery is stated in the polynomial normalization
  and the balanced/twist relation is recorded here in prose.

  ## The documented RSK gap (NOT a sorry — a genuinely open Lean gap)

  This brick does NOT prove `Σ_{λ ⊢ n} f^λ = I(n)`. That identity is the
  Frobenius–Schur / RSK theorem (involutions of `Sₙ` ↔ standard Young tableaux
  of size `n`), which requires a partitions-of-`n` `Fintype` and the RSK
  bijection — machinery ABSENT from Mathlib. It is stated here in prose only;
  there is no `sorry`-claimed theorem asserting it. Likewise the `Σ_{λ ⊢ n}`
  sum over all partitions of `n` needs that same partitions `Fintype`; the
  brick therefore works on a single explicitly-given shape (its hook multiset)
  and on an explicitly-given LIST of shapes, leaving the intrinsic
  `Σ_{λ ⊢ n}` and the RSK count as the documented next bricks.

  ## References
  - [stanley1999] Enumerative Combinatorics 2 (q-hook / fake degrees)
  - [sagan2001] The Symmetric Group (RSK, hook-length formula)
  - [manuscript] §mass-theory/cyclotomic-boundary-at-keystone,
    §mass-theory/binding-period-involution-statistic

  Ground ring (§7c): `qIntPoly`/`qFactPoly` are pure polynomial combinatorics
  over a generic `CommRing`; `dimQ` carries a hook-length division and so uses
  a generic `Field` (algebraic inverse — NOT archimedean; no `ℝ` appears).
-/

import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Ring

namespace QOU.Mass
namespace QHookDimension

open Finset

/-! ## The polynomial q-integer `[n]_q = Σ_{i<n} q^i` -/

/-- The polynomial (Gaussian) q-integer `[n]_q = Σ_{i<n} q^i = 1 + q + … + q^{n−1}`.
Over a generic commutative ring. -/
def qIntPoly {R : Type*} [CommRing R] (q : R) (n : ℕ) : R :=
  ∑ i ∈ Finset.range n, q ^ i

@[simp] theorem qIntPoly_zero {R : Type*} [CommRing R] (q : R) :
    qIntPoly q 0 = 0 := by simp [qIntPoly]

@[simp] theorem qIntPoly_one {R : Type*} [CommRing R] (q : R) :
    qIntPoly q 1 = 1 := by simp [qIntPoly]

/-- Numerator identity: `(q − 1) · [n]_q = q^n − 1`. This is the standard
geometric-sum relation `[n]_q = (q^n − 1)/(q − 1)` in multiplicative form
(valid over any commutative ring, no division). -/
theorem sub_one_mul_qIntPoly {R : Type*} [CommRing R] (q : R) (n : ℕ) :
    (q - 1) * qIntPoly q n = q ^ n - 1 := by
  unfold qIntPoly
  rw [mul_comm]
  exact geom_sum_mul q n

/-- **q = 1 collapse of the q-integer**: `[n]_1 = n`. Since `Σ_{i<n} 1^i = n`,
the polynomial q-integer specializes to the ordinary integer at `q = 1` — the
load-bearing fact that collapses every `[m]_q` inside `S(n)|_{q=1}`. -/
@[simp] theorem qIntPoly_one_eq {R : Type*} [CommRing R] (n : ℕ) :
    qIntPoly (1 : R) n = (n : R) := by
  simp [qIntPoly]

/-! ## The q-factorial `[n]_q! = ∏_{i<n} [i+1]_q` -/

/-- The q-factorial `[n]_q! = [1]_q · [2]_q · … · [n]_q = ∏_{i<n} [i+1]_q`.
Over a generic commutative ring. -/
def qFactPoly {R : Type*} [CommRing R] (q : R) (n : ℕ) : R :=
  ∏ i ∈ Finset.range n, qIntPoly q (i + 1)

@[simp] theorem qFactPoly_zero {R : Type*} [CommRing R] (q : R) :
    qFactPoly q 0 = 1 := by simp [qFactPoly]

theorem qFactPoly_succ {R : Type*} [CommRing R] (q : R) (n : ℕ) :
    qFactPoly q (n + 1) = qFactPoly q n * qIntPoly q (n + 1) := by
  unfold qFactPoly
  rw [Finset.prod_range_succ]

/-- **q = 1 collapse of the q-factorial**: `[n]_1! = n!`. Follows from the
q-integer collapse `[i+1]_1 = i+1` term-by-term; the product of `1..n`
is the ordinary factorial. -/
@[simp] theorem qFactPoly_one_eq {R : Type*} [CommRing R] (n : ℕ) :
    qFactPoly (1 : R) n = ((Nat.factorial n : ℕ) : R) := by
  induction n with
  | zero => simp
  | succ k ih =>
      rw [qFactPoly_succ, ih, qIntPoly_one_eq, Nat.factorial_succ, Nat.cast_mul]
      ring

/-! ## The q-hook dimension `dim_q(λ) = [n]_q! / ∏_{c} [h(c)]_q` -/

/-- The q-hook dimension of a shape of size `n` with hook-length multiset
`hooks`: `dim_q(λ) = [n]_q! / ∏_{h ∈ hooks} [h]_q`. Over a `Field` (the
hook-length ratio needs an inverse; §7c algebraic, not archimedean).

For a genuine partition `λ ⊢ n`, `hooks` is the multiset of hook lengths of
its cells and `hooks.card = n`, so the q → 1 limit reproduces the ordinary
hook-length formula `f^λ = n! / ∏ h(c)`. This brick states `dimQ` on the hook
multiset directly (leaving the intrinsic construction of the hook multiset
from a Young diagram, and the sum over all `λ ⊢ n`, as documented next
bricks). -/
noncomputable def dimQ {R : Type*} [Field R] (q : R) (n : ℕ) (hooks : Multiset ℕ) : R :=
  qFactPoly q n / (hooks.map (qIntPoly q)).prod

/-- Multiplicative form of the q-hook dimension, valid when the hook product
is nonzero (e.g. `q` not a root of the relevant cyclotomic factors):
`dim_q(λ) · ∏_{h} [h]_q = [n]_q!`. -/
theorem dimQ_mul_prod_hooks {R : Type*} [Field R] (q : R) (n : ℕ)
    (hooks : Multiset ℕ) (hne : (hooks.map (qIntPoly q)).prod ≠ 0) :
    dimQ q n hooks * (hooks.map (qIntPoly q)).prod = qFactPoly q n := by
  unfold dimQ
  exact div_mul_cancel₀ _ hne

/-- **q = 1 collapse of the q-hook dimension**: `dim_1(λ) = n! / ∏_{h} h`,
the ordinary hook-length-formula value `f^λ`. Derived purely from the
q-integer / q-factorial collapses `[h]_1 = h`, `[n]_1! = n!` — NOT axiomatized.
No nonzero hypothesis is needed: it is a term-by-term substitution `q ↦ 1`. -/
@[simp] theorem dimQ_one_eq {R : Type*} [Field R] (n : ℕ) (hooks : Multiset ℕ) :
    dimQ (1 : R) n hooks = ((Nat.factorial n : ℕ) : R) / (hooks.map (fun (h : ℕ) => (h : R))).prod := by
  unfold dimQ
  rw [qFactPoly_one_eq]
  have hmap : hooks.map (qIntPoly (1 : R)) = hooks.map (fun (h : ℕ) => (h : R)) := by
    refine Multiset.map_congr rfl ?_
    intro h _
    exact qIntPoly_one_eq h
  rw [hmap]

/-! ## The period sum `S` over an explicit list of shapes, and its q = 1 collapse

The intrinsic `S(n) = Σ_{λ ⊢ n} dim_q(λ)` needs a partitions-of-`n` `Fintype`
(a documented next brick). Here `S` sums `dimQ` over an explicitly-supplied
list of shapes (each given by its hook multiset) of a common size `n`, which
suffices to exhibit the period-sum shape and prove its q = 1 collapse. -/

/-- The q-deformed period sum over an explicit list of shapes of size `n`
(each a hook multiset): `S = Σ_{λ ∈ shapes} dim_q(λ)`. -/
noncomputable def periodSum {R : Type*} [Field R] (q : R) (n : ℕ)
    (shapes : List (Multiset ℕ)) : R :=
  (shapes.map (dimQ q n)).sum

/-- **q = 1 collapse of the period sum**: each summand collapses to the
ordinary `f^λ = n! / ∏ h`, so `S|_{q=1} = Σ_{λ} f^λ`.

The remaining identity `Σ_{λ ⊢ n} f^λ = I(n)` (involution / telephone number)
is the Frobenius–Schur / RSK theorem — NOT proved here (Mathlib lacks the
partitions `Fintype` and the RSK bijection); see the module docstring. -/
@[simp] theorem periodSum_one_eq {R : Type*} [Field R] (n : ℕ)
    (shapes : List (Multiset ℕ)) :
    periodSum (1 : R) n shapes
      = (shapes.map (fun hooks => ((Nat.factorial n : ℕ) : R) / (hooks.map (fun (h : ℕ) => (h : R))).prod)).sum := by
  unfold periodSum
  congr 1
  refine List.map_congr_left ?_
  intro hooks _
  exact dimQ_one_eq n hooks

end QHookDimension
end QOU.Mass
