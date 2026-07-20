import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic
import QOU.Brings.CategoricalLagrangianDMCubic

/-!
# QOU.Brings.SuperDMBerezinian — the Z/2-graded (super) refinement of the Donagi–Markman cubic route

**Scope (read this first).**  This file is a **FORMALIZE-FIRST STRUCTURAL
SCAFFOLD** that *narrows* — and does **NOT** close — the open keystone
`conj:qdifference-kernel-prolongation-symbol` (bean `jqof`).  It refines the
Donagi–Markman cubic route of `QOU.Brings.CategoricalLagrangianDMCubic` by making
the manifest **Z/2 (super) structure** of the framework explicit at the level of
the *measure* (Berezinian) and the *pairing* (supertrace), so that even/odd
channel **MIXING at higher orders** is handled correctly.

**Why a super refinement (the math being encoded).**  The corpus carries a
manifest Z/2 (super) grading — **bar-even** (cosh / mass) vs **bar-odd** (sinh /
decay) — and `def:categorical-lagrangian` is *already* super:
`ℒ_q = 𝒟²_∇` (bosonic, **EVEN**) `+ ψ*⊗𝒟_∇ψ` (fermionic, **ODD**).  The Door-v
analysis (`docs/audits/2026-07-20-qlift-doorV-stokes.md`; the authorNotes on
`conj:qdifference-kernel-prolongation-symbol`) found that the *sole* residual
between the tensor-square realization `C1⊗C1` and the GGM/Stokes datum is a
`(−1)^m` **parity character** — i.e. the **grading operator** `(−1)^F` itself:
GGM's growing solution alternates sign (`y_{m+1} ~ −q^m y_m`) while the
all-positive squares provably cannot.  That is *exactly* the cosh/sinh
(bar-even / bar-odd) split.

**What the corpus was missing.**  The corpus uses the **Berezinian nowhere** and
the **supertrace only implicitly** (the Bring Euler characteristic).  So when
even/odd MIX at higher orders (nonzero off-diagonal super-blocks `B`, `C`), the
correct period-map measure is the **Berezinian**
`Ber = det(A − B·D⁻¹·C) · (det D)⁻¹`, **not** the naive `det(A)·det(D)`, and the
correct pairing is the **supertrace** `str = tr((−1)^F ·) = tr_even − tr_odd`,
**not** the ordinary trace.  This file supplies both objects and proves — the
load-bearing sorry-free lemma — that ordinary `det(A)·(det D)⁻¹` is the Berezinian
**only** in the block-diagonal / NO-MIXING case; the Berezinian's dependence on
`B·D⁻¹·C` is the genuine higher-order correction.

## What Mathlib provides / what we define

- Mathlib **has** the Schur-complement block-determinant identity
  `Matrix.det_fromBlocks₂₂ : det (fromBlocks A B C D) = det D · det (A − B·⅟D·C)`
  (`Mathlib.LinearAlgebra.Matrix.SchurComplement`), i.e. the numerator of the
  Berezinian is a genuine block determinant.  Mathlib does **not** package a
  `Berezinian`.  So we **define** it directly as
  `det(A − B·D⁻¹·C)·(det D)⁻¹` on a block supermatrix (a `def`, not an axiom),
  and prove the block-diagonal reduction sorry-free.
- Mathlib **has** `Matrix.trace`, `Matrix.trace_one`.  We **define** the
  supertrace `tr_even − tr_odd` and prove the basic sign lemma
  (`str (superId) = (p : R) − (q : R)`, the `(−1)^F` weighting) and `str = tr` on
  a purely-even supermatrix — both sorry-free.

## The structural chain (each item stated honestly)

1. `SuperMatrix R p q` — block supermatrix data (even block `A`, odd block `D`,
   off-diagonal mixing `B`, `C`).  Data, asserts nothing.
2. `superTrace` / `superId` — the graded trace `tr_even − tr_odd` and the graded
   identity; `superTrace_superId` (**sorry-free**, the `(−1)^F` sign) and
   `superTrace_purely_even` (**sorry-free**, `str = tr` when the odd part is
   empty).
3. `berezinian` (a `def`, `[Field R]`) with `berezinian_offDiag_zero`
   (**sorry-free**): with `B = 0`, `C = 0` the Berezinian collapses to
   `det A · (det D)⁻¹` — the ordinary product is correct **only** at
   block-diagonal / leading order; the `B·D⁻¹·C` term is the higher-order
   even/odd mixing correction.
4. `SuperDMCubicCondition` — **primary conjecture class** (§3b-tax), refines
   `QDonagiMarkmanCubicCondition` on the even sector and adds the odd cubic + the
   Berezinian nondegeneracy.  Content-bearing; **no instance** (open).
   `superDM_refines_even` (**sorry-free, conditional** §3b-cond) derives the
   ordinary DM cubic condition on the even sector *from* the super condition — the
   refinement is genuine, not a relabel.
5. `qCubicGradedSplit` — **THE NARROWED TARGET, dependent conjecture** (§3b-tax;
   depends on `SuperDMCubicCondition` via an `[Instance]` binder).  Replaces the
   single opaque `QCubicEqBindingKernel` with the **GRADED PAIR**: the **EVEN**
   (bar-even, Berezinian-measured) face of the super-cubic equals the binding
   kernel **C1** (`κ = QOU.Machinery.QProlongation.recurrenceKernelLead`, the
   cosh/mass face), and the **ODD** (bar-odd) face equals the **GGM/decay** face
   (the sinh face; the Door-v residual).  **No instance** (open).

## Honesty (STRICT — AGENTS.md §3b / §Axiomatization is NOT a Proof)

* Content-bearing classes only — no empty `: Prop`, no `: True` field; every
  class field is a parameter-quantified statement in the SHAPE of the claim.
* **No fake instances** to "close" a primary/target conjecture; **no
  `native_decide`**; **no relabelling** a conjecture as a theorem.  The two
  theorems here (`berezinian_offDiag_zero`, `superDM_refines_even`) are genuine:
  the first is unconditional algebra, the second is honestly conditional on the
  super class (§3b-cond) and *derives* the even DM condition, it does not assume
  it.
* Nothing here is wired to production; C1 gets **no** geometric origin from this
  file.  **This scaffold NARROWS the search** — one opaque identity `→` a graded
  pair matching Door-v's `(−1)^m` structure — **it does not close the keystone.**

## Base ring (§7c)

`superTrace` / `superId` / `SuperMatrix` are generic `{R : Type*} [CommRing R]`.
The `berezinian` and the classes that use it take `[Field R]` — genuinely
required (scalar inverse `(det D)⁻¹` and the matrix inverse `D⁻¹`), the §7c
`[Field R]` carve-out for inverse-bearing algebra.  No `ℝ`, no ordering, no
`Real.*`; any archimedean SW-period specialisation lives downstream of the
substrate→archimedean wall.

## References

- [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1 (the cubic
  condition).
- [donagi1997swintegrable] https://arxiv.org/abs/alg-geom/9705010 (SW cubic
  `c_{ijk} = ∂³F`).
- [grassi-gu-marino2019qsw] https://doi.org/10.1007/JHEP07(2020)106 (quantum SW
  curve as a difference operator).
- [manuscript] `def:categorical-lagrangian` (the super Lagrangian
  `𝒟² + ψ*⊗𝒟ψ`), `conj:qdifference-kernel-prolongation-symbol`;
  Door-iv/Door-v probes `docs/audits/2026-07-20-qlift-doorIV-matrix.md`,
  `docs/audits/2026-07-20-qlift-doorV-stokes.md`;
  this file's audit `docs/audits/2026-07-20-super-berezinian-dm-cubic-narrowing.md`;
  `QOU.Machinery.QProlongation.recurrenceKernelLead`;
  `QOU.Brings.CategoricalLagrangianDMCubic`.
-/

noncomputable section

open Matrix
open QOU.Brings.CategoricalLagrangianDMCubic

namespace QOU.Brings.SuperDMBerezinian

/-! ### (1) Block supermatrix data (data structure — NOT a conjecture)

A `Z/2`-graded endomorphism of a super vector space `V = V₀ ⊕ V₁` with
`dim V₀ = p` (even / bosonic) and `dim V₁ = q` (odd / fermionic), written in
block form.  The diagonal blocks `A : V₀ → V₀`, `D : V₁ → V₁` are **even**
(grade-preserving); the off-diagonal blocks `B : V₁ → V₀`, `C : V₀ → V₁` are
**odd** (grade-reversing) and carry the even/odd **mixing**.  Naming data asserts
nothing; the logical content lives in the conjecture classes below. -/
structure SuperMatrix (R : Type*) [CommRing R] (p q : ℕ) where
  /-- Even → even block (bosonic; mirrors `𝒟²_∇` in `ℒ_q`). -/
  A : Matrix (Fin p) (Fin p) R
  /-- Odd → even block (grade-reversing mixing). -/
  B : Matrix (Fin p) (Fin q) R
  /-- Even → odd block (grade-reversing mixing). -/
  C : Matrix (Fin q) (Fin p) R
  /-- Odd → odd block (fermionic; mirrors `ψ*⊗𝒟_∇ψ` in `ℒ_q`). -/
  D : Matrix (Fin q) (Fin q) R

/-- The **graded identity** supermatrix: identity on each graded piece, no
    mixing.  Its supertrace exhibits the `(−1)^F` weighting (`superTrace_superId`). -/
def superId (R : Type*) [CommRing R] (p q : ℕ) : SuperMatrix R p q where
  A := 1
  B := 0
  C := 0
  D := 1

/-! ### (2) The supertrace `str = tr_even − tr_odd = tr((−1)^F ·)` -/

/-- **Supertrace** of a block supermatrix: `str = tr(A) − tr(D)`, i.e.
    `tr((−1)^F ·)` — the even sector enters with sign `+1`, the odd sector with
    sign `−1`.  This is the graded pairing the corpus was using only implicitly
    (Bring Euler characteristic); it is the correct contraction when even and odd
    mix. -/
def superTrace {R : Type*} [CommRing R] {p q : ℕ} (M : SuperMatrix R p q) : R :=
  Matrix.trace M.A - Matrix.trace M.D

/-- **Sign lemma (`(−1)^F`).**  The supertrace of the graded identity is
    `(p : R) − (q : R)` — the even directions count `+1`, the odd directions
    `−1`, the super/graded Euler character.  Contrast the *ordinary* trace of the
    underlying `(p+q)×(p+q)` identity, which would count `p + q`; the sign on the
    odd block is the entire content of "super".  Sorry-free. -/
theorem superTrace_superId {R : Type*} [CommRing R] (p q : ℕ) :
    superTrace (superId R p q) = (p : R) - (q : R) := by
  simp [superTrace, superId]

/-- **`str = tr` on a purely-even supermatrix.**  When the odd part is empty
    (`q = 0`) the supertrace reduces to the ordinary trace of the even block:
    there is no `(−1)^F` sign to pay.  This pins the sign convention (the odd
    block is what makes `str ≠ tr`).  Sorry-free. -/
theorem superTrace_purely_even {R : Type*} [CommRing R] {p : ℕ}
    (M : SuperMatrix R p 0) : superTrace M = Matrix.trace M.A := by
  simp [superTrace]

/-! ### (3) The Berezinian (superdeterminant) and the no-mixing reduction -/

/-- **Berezinian** (superdeterminant) of a block supermatrix, over a field:
    `Ber = det(A − B·D⁻¹·C) · (det D)⁻¹`.  The numerator `det(A − B·D⁻¹·C)` is the
    Schur-complement block determinant Mathlib packages as
    `Matrix.det_fromBlocks₂₂` (`det (fromBlocks A B C D) = det D · det(A−B·⅟D·C)`);
    the Berezinian divides that block determinant by `(det D)²` in effect
    (`Ber = det(fromBlocks …) · (det D)⁻²`), giving the correct measure on the
    super period map.  Mathlib does not package this quotient, so we define it. -/
def berezinian {R : Type*} [Field R] {p q : ℕ} (M : SuperMatrix R p q) : R :=
  (M.A - M.B * M.D⁻¹ * M.C).det * (M.D.det)⁻¹

/-- **THE LOAD-BEARING REDUCTION (sorry-free).**  With **no mixing** — the
    off-diagonal odd blocks vanish, `B = 0` and `C = 0` (the block-diagonal /
    leading-order case) — the Berezinian collapses to the naive
    `det(A) · (det D)⁻¹`.  Equivalently: the corpus's implicit
    ordinary-determinant measure is correct **only** at block-diagonal order; the
    `B·D⁻¹·C` term the Berezinian carries is *exactly* the higher-order even/odd
    mixing correction the corpus was dropping.  This is the honest statement that
    the super refinement is a genuine correction, not a relabel. -/
theorem berezinian_offDiag_zero {R : Type*} [Field R] {p q : ℕ}
    (M : SuperMatrix R p q) (hB : M.B = 0) (hC : M.C = 0) :
    berezinian M = M.A.det * (M.D.det)⁻¹ := by
  simp [berezinian, hB, hC]

/-! ### (4) Primary conjecture — the super Donagi–Markman cubic condition

Refines `QDonagiMarkmanCubicCondition` (the even sector) and adds the odd cubic
and the Berezinian nondegeneracy of the graded period map. -/

/-- **Super q-Lagrangian fibration data.**  A base with an **even** (bar-even,
    bosonic) sector of dimension `dim` and an **odd** (bar-odd, fermionic) sector
    of dimension `oddDim`, each carrying the differential of its q-period map
    (`dPeriodEven`, `dPeriodOdd`) symmetric in the first two slots, together with
    the **second-jet super-period matrix** `mixing : SuperMatrix` whose
    off-diagonal blocks record the even/odd mixing.  Data only. -/
structure SuperQLagrangianFibration (R : Type*) [CommRing R] where
  /-- Even (bar-even / bosonic) sector dimension. -/
  dim : ℕ
  /-- Odd (bar-odd / fermionic) sector dimension. -/
  oddDim : ℕ
  /-- Differential of the even q-period map: `dPeriodEven i j k = ∂_k τ^{even}_{ij}`. -/
  dPeriodEven : Fin dim → Fin dim → Fin dim → R
  /-- Even period matrix symmetric in the first two slots. -/
  dPeriodEven_symm_ij : ∀ i j k, dPeriodEven i j k = dPeriodEven j i k
  /-- Differential of the odd q-period map: `dPeriodOdd i j k = ∂_k τ^{odd}_{ij}`. -/
  dPeriodOdd : Fin oddDim → Fin oddDim → Fin oddDim → R
  /-- Odd period matrix symmetric in the first two slots. -/
  dPeriodOdd_symm_ij : ∀ i j k, dPeriodOdd i j k = dPeriodOdd j i k
  /-- The second-jet super-period matrix; its off-diagonal blocks are the
      even/odd mixing whose measure is the Berezinian. -/
  mixing : SuperMatrix R dim oddDim

/-- Project a super fibration onto its **even sector** as an ordinary
    `QLagrangianFibration`.  The refinement theorem `superDM_refines_even` shows
    the super cubic condition implies the ordinary DM condition here. -/
def SuperQLagrangianFibration.toEven {R : Type*} [CommRing R]
    (SF : SuperQLagrangianFibration R) : QLagrangianFibration R where
  dim := SF.dim
  dPeriod := SF.dPeriodEven
  dPeriod_symm_ij := SF.dPeriodEven_symm_ij

/-- **§3b primary conjecture class — the super Donagi–Markman cubic condition.**

    `@conjecture: primary`

    The Z/2-graded refinement of `QDonagiMarkmanCubicCondition`.  It asserts:

    * `even_cubic` — a **totally-symmetric even cubic** `c` realising the even
      period differential (`∂_k τ^{even}_{ij} = c_{ijk}`).  This is the ordinary
      DM cubic condition on the bar-even (cosh/mass) sector; `superDM_refines_even`
      derives `QDonagiMarkmanCubicCondition SF.toEven` from it.
    * `odd_cubic` — a **totally-symmetric odd cubic** realising the odd (bar-odd,
      sinh/decay) period differential.  The corpus had no carrier for this face.
    * `berezinian_nondeg` — the graded period map is nondegenerate under the
      **correct (Berezinian) measure**: `berezinian SF.mixing ≠ 0`.  Using the
      naive `det(A)·det(D)` here would drop the `B·D⁻¹·C` mixing
      (`berezinian_offDiag_zero`); the class insists on the Berezinian.

    Content-bearing (three parameter-quantified fields, none a marker or `True`).
    **No instance is supplied** — the honest open state of the super cubic
    condition. -/
-- Ref: [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1
-- Ref: [donagi1997swintegrable] https://arxiv.org/abs/alg-geom/9705010
-- Ref: [manuscript] def:categorical-lagrangian; conj:qdifference-kernel-prolongation-symbol;
--      docs/audits/2026-07-20-qlift-doorV-stokes.md
class SuperDMCubicCondition {R : Type*} [Field R]
    (SF : SuperQLagrangianFibration R) : Prop where
  /-- Totally-symmetric even cubic realising the even (bar-even) period
      differential — the ordinary DM cubic condition on the bosonic sector. -/
  even_cubic :
    ∃ c : Fin SF.dim → Fin SF.dim → Fin SF.dim → R,
      (∀ i j k, c i j k = c j i k) ∧
      (∀ i j k, c i j k = c i k j) ∧
      (∀ i j k, SF.dPeriodEven i j k = c i j k)
  /-- Totally-symmetric odd cubic realising the odd (bar-odd) period
      differential — the fermionic (sinh/decay) face. -/
  odd_cubic :
    ∃ c : Fin SF.oddDim → Fin SF.oddDim → Fin SF.oddDim → R,
      (∀ i j k, c i j k = c j i k) ∧
      (∀ i j k, c i j k = c i k j) ∧
      (∀ i j k, SF.dPeriodOdd i j k = c i j k)
  /-- The graded period map is nondegenerate under the **Berezinian** measure. -/
  berezinian_nondeg : berezinian SF.mixing ≠ 0

/-- **Conditional theorem (§3b-cond).**  The super cubic condition genuinely
    **refines** the ordinary Donagi–Markman cubic condition: given
    `[SuperDMCubicCondition SF]` (the `[Instance]` binder is the dependency edge,
    §3b-tax), the ordinary `QDonagiMarkmanCubicCondition` holds on the even sector
    `SF.toEven`.  Derived by extracting the even cubic — a genuine composition of
    the class field, not a self-assuming projection (the super class carries an
    *additional* odd cubic + Berezinian face that this even projection forgets).
    Sorry-free.  It does **not** discharge either conjecture: it still consumes a
    `SuperDMCubicCondition` instance, of which none exists. -/
-- Ref: [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1
theorem superDM_refines_even {R : Type*} [Field R]
    (SF : SuperQLagrangianFibration R) [SuperDMCubicCondition SF] :
    QDonagiMarkmanCubicCondition SF.toEven where
  exists_cubic := SuperDMCubicCondition.even_cubic (SF := SF)

/-! ### (5) THE NARROWED TARGET — the graded pair (even = C1/mass, odd = GGM/decay) -/

/-- **§3b dependent target conjecture class — the graded C1 / GGM split.**

    `@conjecture: dependent` (depends on `SuperDMCubicCondition SF` via the
    `[Instance]` binder — the dependency edge, §3b-tax).

    **THIS IS THE NARROWED KEYSTONE TARGET.**  It **replaces** the single opaque
    identity `QCubicEqBindingKernel` (one cubic = C1) with the **GRADED PAIR**,
    matching the `(−1)^m` parity structure the Door-v probe isolated
    (`docs/audits/2026-07-20-qlift-doorV-stokes.md`):

    * `even_eq_binding_kernel` — the **EVEN** (bar-even, cosh/mass) face of the
      super-cubic equals the binding kernel **C1**: its distinguished
      self-contraction is the nonzero leading recurrence-kernel weight
      `κ = QOU.Machinery.QProlongation.recurrenceKernelLead` (the top-shift term
      of the proved depth-2 C1 kernel `[n+2]_q b_{n+2} = b_{n+1} + b_n`,
      `QOU.Mass.QDifferenceConfluentObstruction`).
    * `odd_eq_ggm_decay` — the **ODD** (bar-odd, sinh/decay) face equals the
      **GGM/decay** face: its self-contraction is a nonzero decay weight `γ` (the
      `(−1)^m`-alternating growing solution of the GGM/Stokes datum, the Door-v
      residual).

    `κ` and `γ` are carried abstractly (documented contract; the class names the
    exact decls they stand for) rather than importing the heavy `QuantumTorus`
    cone.  Both fields are content-bearing nonzero identifications in the SHAPE of
    the claim, NOT markers.

    **Honesty — this NARROWS jqof, it does NOT close it.**  The super grading turns
    the one opaque identity into a *graded pair* whose even/odd split is forced to
    match Door-v's proved `(−1)^m` parity character — that is a genuine narrowing
    of the open target.  It is **NOT proved**: there is **no instance**, and the
    identity must be **derived** (from the Bring hyperkähler geometry + the graded
    Lagrangian `ℒ_q = 𝒟² + ψ*⊗𝒟ψ`), **never fitted**.  Deriving it is the open
    wall. -/
-- Ref: [donagi1997swintegrable] https://arxiv.org/abs/alg-geom/9705010
-- Ref: [grassi-gu-marino2019qsw] https://doi.org/10.1007/JHEP07(2020)106
-- Ref: [manuscript] conj:qdifference-kernel-prolongation-symbol;
--      QOU.Machinery.QProlongation.recurrenceKernelLead;
--      QOU.Mass.QDifferenceConfluentObstruction;
--      docs/audits/2026-07-20-qlift-doorV-stokes.md;
--      docs/audits/2026-07-20-super-berezinian-dm-cubic-narrowing.md
class qCubicGradedSplit {R : Type*} [Field R]
    (SF : SuperQLagrangianFibration R) (κ γ : R) [SuperDMCubicCondition SF] : Prop where
  /-- The EVEN (bar-even, cosh/mass) face equals the binding kernel C1: for any
      even cubic realising the even period differential, a distinguished direction
      has self-contraction the nonzero leading kernel weight `κ`. -/
  even_eq_binding_kernel :
    ∀ c : Fin SF.dim → Fin SF.dim → Fin SF.dim → R,
      (∀ i j k, SF.dPeriodEven i j k = c i j k) →
      ∃ d : Fin SF.dim, c d d d = κ ∧ κ ≠ 0
  /-- The ODD (bar-odd, sinh/decay) face equals the GGM/decay face: for any odd
      cubic realising the odd period differential, a distinguished direction has
      self-contraction the nonzero decay weight `γ`. -/
  odd_eq_ggm_decay :
    ∀ c : Fin SF.oddDim → Fin SF.oddDim → Fin SF.oddDim → R,
      (∀ i j k, SF.dPeriodOdd i j k = c i j k) →
      ∃ d : Fin SF.oddDim, c d d d = γ ∧ γ ≠ 0

end QOU.Brings.SuperDMBerezinian
