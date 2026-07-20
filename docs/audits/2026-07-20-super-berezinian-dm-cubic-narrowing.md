# Super / Berezinian refinement of the Donagi–Markman cubic route — narrowing `jqof`

**Date:** 2026-07-20
**Branch:** `claude/argument-principle-residue-sum-2026-07-20`
**Lean:** [`QOU.Brings.SuperDMBerezinian`](../../content/quantum-observable-universe/lean/QOU/Brings/SuperDMBerezinian.lean)
**Block:** [`conj:qdifference-kernel-prolongation-symbol`](../../content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.md) (bean `jqof`, tier:keystone)
**Builds on:** [`QOU.Brings.CategoricalLagrangianDMCubic`](../../content/quantum-observable-universe/lean/QOU/Brings/CategoricalLagrangianDMCubic.lean) (commit `adbf8153`)

> **This scaffold NARROWS the open keystone. It does NOT close it.** No fit is
> wired to production; the graded target has no instance and must be *derived*,
> never fitted.

## 1. The gap this closes at the *scaffolding* level (not the math level)

The framework's Z/2 (super) structure is manifest and load-bearing:

- **bar-even** (`cosh`) ↔ **mass**; **bar-odd** (`sinh`) ↔ **decay**.
- `def:categorical-lagrangian` is *already* super:
  `ℒ_q = 𝒟²_∇` (bosonic, **EVEN**) `+ ψ*⊗𝒟_∇ψ` (fermionic, **ODD**).
- The Door-v probe ([`2026-07-20-qlift-doorV-stokes.md`](2026-07-20-qlift-doorV-stokes.md))
  reduced the *entire* residual between the tensor square `C1⊗C1` and the
  GGM/Stokes datum to a **single `(−1)^m` parity character** — the grading
  operator `(−1)^F` itself. GGM's growing solution alternates sign
  (`y_{m+1} ~ −q^m y_m`); the all-positive squares `f₊², f₋²` provably cannot
  (parity). That `(−1)^m` **is** the cosh/sinh (bar-even / bar-odd) split.

Yet the corpus used:

- the **Berezinian** (superdeterminant) **nowhere**, and
- the **supertrace** only *implicitly* (as the Bring Euler characteristic).

**Consequence of the omission.** As long as the even and odd sectors are treated
by ordinary linear algebra, one silently uses the block-diagonal measure
`det(A)·det(D)` and the ordinary trace `tr(A)+tr(D)`. Those are correct **only
when the off-diagonal blocks `B`, `C` vanish** — i.e. only at leading /
block-diagonal order, before even and odd **mix**. The moment mixing turns on
(higher orders of the period map / the second jet), the correct objects are the
**Berezinian** and the **supertrace**, which the corpus had no carrier for. This
scaffold supplies them.

## 2. What Mathlib provides, and what we defined

| Object | Mathlib v4.24.0 | This file |
|---|---|---|
| Schur-complement block determinant `det(fromBlocks A B C D) = det D · det(A − B·⅟D·C)` | **YES** — `Matrix.det_fromBlocks₂₂` (`Mathlib.LinearAlgebra.Matrix.SchurComplement`) | cited; it is the numerator of the Berezinian |
| `Matrix.trace`, `Matrix.trace_one` | **YES** | used in `superTrace_superId` |
| `Berezinian` (packaged superdeterminant `det(A−B·D⁻¹·C)·(det D)⁻¹`) | **NO** | **defined** (`berezinian`, a `def` over `[Field R]`, not an axiom) |
| supertrace `tr((−1)^F·)` | **NO** | **defined** (`superTrace = tr_even − tr_odd`) |

Mathlib has the Schur-complement determinant lemma but **not** a packaged
Berezinian; per the task's "define rather than axiomatize where feasible", the
Berezinian is a concrete `def` computing `det(A − B·D⁻¹·C)·(det D)⁻¹` on the
block supermatrix, and its key reduction is proved sorry-free.

## 3. What is proved sorry-free (verified `lean`-direct, exit 0)

Verified with `lean`-direct over the restored `lake-cache/qou-v4-24-0` oleans
(toolchain `leanprover/lean4:v4.24.0`); LSP `leansearch`/`loogle` were firewalled
(403) so lemma discovery used Mathlib knowledge + `lean`-direct iteration.

1. **`berezinian_offDiag_zero`** (the load-bearing lemma):
   with `B = 0` and `C = 0`,
   `berezinian M = det(A) · (det D)⁻¹`.
   *Reading:* the corpus's implicit ordinary-determinant measure is the Berezinian
   **only** in the no-mixing / block-diagonal case; the `B·D⁻¹·C` term the
   Berezinian carries is exactly the higher-order even/odd **mixing correction**
   the corpus dropped. This is the honest statement that the super refinement is a
   genuine correction, not a relabel.

2. **`superTrace_superId`**: `superTrace (superId R p q) = (p : R) − (q : R)`.
   *Reading:* the graded/super Euler character — even directions count `+1`, odd
   directions `−1`. Contrast the ordinary trace of the underlying `(p+q)`-identity,
   which counts `p + q`. The sign on the odd block is the whole content of "super"
   — the Lean encoding of Door-v's `(−1)^F`.

3. **`superTrace_purely_even`**: on a `SuperMatrix R p 0`, `str = tr(A)`.
   Pins the sign convention (the odd block is what makes `str ≠ tr`).

4. **`superDM_refines_even`** (§3b-cond conditional theorem): given
   `[SuperDMCubicCondition SF]`, the ordinary `QDonagiMarkmanCubicCondition` holds
   on the even sector `SF.toEven`. The super condition **genuinely refines** the
   ordinary DM cubic condition (derives it, does not assume it); it consumes a
   super instance, of which none exists, so it discharges neither conjecture.

## 4. What is OPEN — no instance, content-bearing conjecture classes

- **`SuperDMCubicCondition`** — primary conjecture class (`[Field R]`). Three
  content-bearing fields: a totally-symmetric **even** cubic realising the
  bar-even period differential (the ordinary DM condition on the bosonic sector),
  a totally-symmetric **odd** cubic realising the bar-odd (sinh/decay) period
  differential (a face the corpus had no carrier for), and Berezinian
  nondegeneracy `berezinian SF.mixing ≠ 0` (the correct measure, not
  `det A · det D`). **No instance.**

- **`qCubicGradedSplit`** — **THE NARROWED TARGET**, dependent conjecture class
  (depends on `SuperDMCubicCondition` via an `[Instance]` binder — the derived
  §3b-tax dependency edge). It **replaces** the single opaque
  `QCubicEqBindingKernel` (one cubic = C1) with the **GRADED PAIR**:
  - **EVEN** (bar-even, cosh/mass) face `= C1`: distinguished self-contraction
    `= κ = QOU.Machinery.QProlongation.recurrenceKernelLead ≠ 0` (top-shift of the
    proved depth-2 kernel `[n+2]_q b_{n+2} = b_{n+1} + b_n`);
  - **ODD** (bar-odd, sinh/decay) face `=` the GGM/decay face: self-contraction
    `= γ ≠ 0` (the `(−1)^m`-alternating growing GGM solution — the Door-v
    residual).

  `κ`, `γ` carried abstractly (documented contract, naming the exact decls),
  mirroring `QJetBundle`'s light-import discipline. **No instance.**

## 5. Why this is a NARROWING (the honest accounting)

**Before.** The open target was one opaque identity: "the DM q-cubic of the Bring
fibration equals the binding kernel C1" (`QCubicEqBindingKernel`), with no handle
on why C1 (mass) and GGM (decay) are different objects.

**After.** The target is a **graded pair** whose even/odd split is *forced* to
match a **proved** fact — Door-v's machine-measured `(−1)^m` parity character. The
super grading is not decorative: `berezinian_offDiag_zero` shows the corpus's
measure was the leading term of a genuinely graded object, and the target now
carries the even = C1/cosh, odd = GGM/sinh structure explicitly. That strictly
constrains any future closure attempt (it must respect the grading), which is the
definition of a narrowing.

**What remains the wall.** `qCubicGradedSplit` has **no instance**. The graded
identity must be **derived** — from the Bring hyperkähler geometry plus the graded
Lagrangian `ℒ_q = 𝒟² + ψ*⊗𝒟ψ` — **never fitted** (per the anti-laundering rule,
the standing `Δ_λ`/anti-fit discipline, and AGENTS.md §"Axiomatization is NOT a
Proof"). Deriving it de-tautologizes QDM-3 and gives C1 an independent origin; the
scaffold does not do this and does not claim to.

## 6. Honesty checklist (§3b-tax, §Axiomatization is NOT a Proof)

- [x] Content-bearing classes only — every class field is a parameter-quantified
      statement in the shape of the claim; no empty `: Prop`, no `: True` field,
      no vacuous definitional-tautology field.
- [x] No fake instance for any primary/target conjecture.
- [x] No `native_decide`, no `sorry` (docstrings mention the word only to describe
      the sorry-free lemmas), no relabelling conjecture → theorem.
- [x] Dependent conjecture (`qCubicGradedSplit`) wears its hypothesis
      (`[SuperDMCubicCondition SF]`) in the type — the derived dependency edge.
- [x] The two theorems are genuine (`berezinian_offDiag_zero` unconditional;
      `superDM_refines_even` honestly conditional and *derives* its conclusion).
- [x] `[Field R]` only where inverses are genuinely needed (§7c carve-out); no
      `ℝ`, no ordering, no `Real.*`.
- [x] Nothing wired to production.

## References

- [`2026-07-20-qlift-doorV-stokes.md`](2026-07-20-qlift-doorV-stokes.md) — the
  `(−1)^m` parity residual (the motivation for the grading operator).
- [`2026-07-20-qlift-doorIV-matrix.md`](2026-07-20-qlift-doorIV-matrix.md) — the
  tensor-square `C1⊗C1` anisoclinic realization.
- [`2026-07-20-qlift-gauge-gap-synthesis.md`](2026-07-20-qlift-gauge-gap-synthesis.md)
  — the five convergent module-inequivalence routes.
- `[donagi-markman1996cubics]` alg-geom/9408004 §1; `[donagi1997swintegrable]`
  alg-geom/9705010; `[grassi-gu-marino2019qsw]` JHEP07(2020)106.
- Mathlib `Matrix.det_fromBlocks₂₂`, `Matrix.trace_one`.
