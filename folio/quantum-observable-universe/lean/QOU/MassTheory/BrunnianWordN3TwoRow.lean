import Mathlib.Tactic
import QOU.MassTheory.GermRootVectorGaugeFixing

/-!
# QOU.MassTheory.BrunnianWordN3TwoRow — the concrete A=3 Brunnian word in the two-row sector

**Instance brick 3, minimal wedge (qou-v7ro).** The ∀A convention-D deficit recursion
`D_{A+1} = −h²(h²+2)D_A` is proved mathematically and certified
(`computations/deltalambda/milnor_recursion_forall_A_proof_probe.py`) and its field-algebra glue is
Lean (`QOU.MassTheory.DeficitRecursionReduction`). The **R2 crux** deferred by the brick-3 roast
(`docs/audits/2026-08-31-milnor-brick3-roast.md`, re-roast `2026-09-03-milnor-brick3-reroast.md`) is
a *concrete evaluable* `ρ(w_n)` for the Brunnian word `w_n`. This file supplies it at the base case
`n = 3` in the **surviving two-row sector**, and closes the loop to the certified deficit there.

## What is the object

The A=3 Brunnian word is `w₃ = [A₀₁, A₁₂]`, the band-commutator of the two adjacent pure-braid bands
`A₀₁ = σ₁²`, `A₁₂ = σ₂²` in `B₃` (the `W3_BAND = band_comm(A01, A12)` of
`computations/deltalambda/a4_brunnian_deficit_closed_form.py`; `b = A_{n-1,n} = σ²_{n-1}`). By
Schur–Weyl for `U_q(sl₂)` on `V^{⊗3}` (`V = K²`), only the `≤ 2`-row partitions of 3 survive the
two-row cap (`QOU.MassTheory.TwoRowCapDerived`): `(3)` and `(2,1)`. The `(2,1)` two-row irrep of
`H₃(q)` **is** the 2-dim reduced-Burau representation whose generators are the sorry-free
`QOU.MassTheory.GermRootVectorGauge.heckeGen1 / heckeGen2`. So `brunnianW3` below is the genuine,
concrete `ρ_{(2,1)}(w₃)`.

## What is PROVED here (sorry-free, generic `Field`)

* `heckeGen2_mul_inv` / `heckeGen2Inv_mul` — the missing second generator inverse (the first is in
  `GermRootVectorGaugeFixing`).
* `brunnianW3_eq` — the concrete `2×2` matrix of the word, entrywise.
* `brunnianW3_det = 1` — a commutator of `det = ±1` bands (the `(2,1)` word is `SL₂`).
* `brunnianW3_trace` — the **exact `(2,1)` two-row character** `χ^{(2,1)}(w₃)` as a rational in `q`.
* `deficitA3_eq_closed_form` — the payoff: feeding this concrete `(2,1)` trace through the Schur–Weyl
  reconstruction `qtr(ρ(w₃)) = [4]·χ^{(3)}(w₃) + [2]·χ^{(2,1)}(w₃)` (the two surviving rows) and the
  deficit `D₃ = 1 − qtr/[2]³` yields **exactly** the certified closed form
  `D_A = (−1)^{A−3} h^{2(A−1)} (h²+2)^{A−3} (h²+3)/(h²+4)` at `A = 3`, i.e. `D₃ = h⁴(h²+3)/(h²+4)`.

## What is CITED, not proved (the honest seam)

The **Schur–Weyl decomposition itself** — that `qtr` on `V^{⊗3}` factors as `Σ_λ qdim(V_λ)·χ^λ(w)`
with the `≤2`-row cap, the `sl₂` quantum dimensions `qdim(V_{(3)}) = [4]`, `qdim(V_{(2,1)}) = [2]`,
and the fact `χ^{(3)}(w₃) = 1` (a commutator in the 1-dim symmetric channel `σ_i ↦ q`) — is standard
representation theory, used here as the **definition** of `survivingQTrace`. Lean does **not** prove
Schur–Weyl duality. What Lean proves is that *given* that reconstruction, the concretely-computed
`(2,1)` trace reproduces the certified deficit at `A = 3`. This is the base-case verification of the
sharpened route (reduced Burau + two-row cap), not a proof of the ∀n instance — the position-indexed
`e_{n-1}` on the reduced space ∀n and the Brunnian-word spectrum recursion remain brick 3's general-n
body (still open, `qou-v7ro`; the `BrunnianDeficitRecursion` instance stays unfabricated).

## References

- Ref: [leitner2026] `docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md` — the certified ∀A
  recursion and the `D_A` closed form.
- Ref: [leitner2026] `docs/audits/2026-09-03-milnor-brick3-reroast.md` — the sharpened residual gap and
  the reduced-Burau + esymm route this brick instantiates at `n = 3`.

**Base ring (§7c).** Generic `Field` (needed only for `q⁻¹`); no `ℝ`, no ordering, no `Real.*`, no
archimedean evaluation.
-/

namespace QOU.MassTheory.BrunnianWordN3

open QOU.MassTheory.GermRootVectorGauge
open Matrix

variable {K : Type*} [Field K]

/-- The inverse of `ρ(σ₂)` in the 2-dim reduced-Burau rep (`det heckeGen2 = -1`). The `σ₁` inverse
    is `QOU.MassTheory.GermRootVectorGauge.heckeGen1Inv`; this supplies the missing `σ₂` one. -/
def heckeGen2Inv (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q, 0; -q, q⁻¹]

@[simp] theorem heckeGen2_mul_inv (q : K) (hq : q ≠ 0) :
    heckeGen2 q * heckeGen2Inv q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen2, heckeGen2Inv, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp

@[simp] theorem heckeGen2Inv_mul (q : K) (hq : q ≠ 0) :
    heckeGen2Inv q * heckeGen2 q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen2, heckeGen2Inv, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

/-- The pure-braid band `A₀₁ = σ₁²`. -/
def band01 (q : K) : Matrix (Fin 2) (Fin 2) K := heckeGen1 q * heckeGen1 q

/-- The pure-braid band `A₁₂ = σ₂²`. -/
def band12 (q : K) : Matrix (Fin 2) (Fin 2) K := heckeGen2 q * heckeGen2 q

/-- `A₀₁⁻¹ = σ₁⁻²`. -/
def band01Inv (q : K) : Matrix (Fin 2) (Fin 2) K := heckeGen1Inv q * heckeGen1Inv q

/-- `A₁₂⁻¹ = σ₂⁻²`. -/
def band12Inv (q : K) : Matrix (Fin 2) (Fin 2) K := heckeGen2Inv q * heckeGen2Inv q

/-- **The concrete A=3 Brunnian word** `ρ_{(2,1)}(w₃)`, `w₃ = [A₀₁, A₁₂] = A₀₁ A₁₂ A₀₁⁻¹ A₁₂⁻¹`, in
    the 2-dim reduced-Burau / `(2,1)` two-row representation of `B₃`. -/
def brunnianW3 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  band01 q * band12 q * band01Inv q * band12Inv q

/-- The concrete `2×2` matrix of `ρ_{(2,1)}(w₃)`, entrywise. -/
theorem brunnianW3_eq (q : K) (hq : q ≠ 0) :
    brunnianW3 q =
      !![(-q^10 + 3*q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / q^4,
           (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / q^6;
         (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / q^4,
           (q^6 - q^4 + 2*q^2 - 1) / q^6] := by
  unfold brunnianW3 band01 band12 band01Inv band12Inv
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen1, heckeGen2, heckeGen1Inv, heckeGen2Inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **The `(2,1)` word is `SL₂`.** `det ρ_{(2,1)}(w₃) = 1` — a commutator of `det = ±1` bands. -/
theorem brunnianW3_det (q : K) (hq : q ≠ 0) : (brunnianW3 q).det = 1 := by
  rw [brunnianW3_eq q hq, Matrix.det_fin_two_of]
  field_simp
  ring

/-- **The exact `(2,1)` two-row character** `χ^{(2,1)}(w₃) = tr ρ_{(2,1)}(w₃)`. -/
theorem brunnianW3_trace (q : K) (hq : q ≠ 0) :
    (brunnianW3 q).trace
      = -(q^4 - q^2 + 1) * (q^8 - 2*q^6 - 2*q^2 + 1) / q^6 := by
  rw [brunnianW3_eq q hq, Matrix.trace_fin_two_of]
  field_simp
  ring

/-- `[2] = q + q⁻¹`, the `sl₂` quantum dimension of the spin-½ block `V_{(2,1)}`. -/
def qBracket2 (q : K) : K := q + q⁻¹

/-- `[4] = q³ + q + q⁻¹ + q⁻³`, the `sl₂` quantum dimension of the spin-3/2 block `V_{(3)}`. -/
def qBracket4 (q : K) : K := q^3 + q + q⁻¹ + q⁻¹^3

/-- **Schur–Weyl reconstruction of the surviving quantum trace on `V^{⊗3}`** (cited, not proved):
    `qtr(ρ(w₃)) = qdim(V_{(3)})·χ^{(3)}(w₃) + qdim(V_{(2,1)})·χ^{(2,1)}(w₃) = [4]·1 + [2]·tr(w₃)`.
    Only the two `≤2`-row partitions `(3), (2,1)` contribute (the two-row cap); `χ^{(3)}(w₃) = 1`
    because `w₃` is a commutator in the 1-dim symmetric channel. -/
def survivingQTrace (q : K) : K := qBracket4 q * 1 + qBracket2 q * (brunnianW3 q).trace

/-- The convention-D deficit at `A = 3`, `D₃ = 1 − qtr(ρ(w₃))/[2]³`, built from the concrete word. -/
def deficitA3 (q : K) : K := 1 - survivingQTrace q / (qBracket2 q)^3

/-- `h = q − q⁻¹`, the recursion variable. -/
def hval (q : K) : K := q - q⁻¹

/-- **THE BASE-CASE PAYOFF.** The concrete `(2,1)` Brunnian-word trace, fed through the Schur–Weyl
    two-row reconstruction and the deficit definition, reproduces **exactly** the certified closed
    form `D_A = (−1)^{A−3} h^{2(A−1)} (h²+2)^{A−3} (h²+3)/(h²+4)` at `A = 3`:

      `D₃ = h⁴ (h²+3)/(h²+4)`.

    This verifies the sharpened brick-3 route (reduced Burau + two-row cap) at the base case: the
    concrete `ρ(w₃)` — not an abstract or assumed trace — closes to the certified recursion.

    The hypothesis `q² + 1 ≠ 0` is the non-degeneracy `[2] = q + q⁻¹ ≠ 0` required to normalise the
    Markov trace by `[2]³` (it holds at the substrate anchor `q₀ ≈ 1.11` and, more generally, off the
    roots `q² = −1`); it is algebraic, not archimedean — no ordering or `Real.*` is used. -/
theorem deficitA3_eq_closed_form (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    deficitA3 q = (hval q) ^ 4 * ((hval q) ^ 2 + 3) / ((hval q) ^ 2 + 4) := by
  have hbr2 : q + q⁻¹ ≠ 0 := by
    have e : q + q⁻¹ = (q ^ 2 + 1) * q⁻¹ := by field_simp
    rw [e]; exact mul_ne_zero h2 (inv_ne_zero hq)
  have hden : (q - q⁻¹) ^ 2 + 4 ≠ 0 := by
    have e : (q - q⁻¹) ^ 2 + 4 = (q + q⁻¹) ^ 2 := by field_simp; ring
    rw [e]; exact pow_ne_zero 2 hbr2
  -- `field_simp` clears `(q+q⁻¹)^n` denominators via `h2` (their normal form `(q²+1)ⁿ/qⁿ` keeps
  -- the `q²+1` factor) but NOT the sum form `(q-q⁻¹)²+4` (it expands that to `q⁴+2q²+1` and will
  -- not factor it back). Rewrite the RHS denominator into the power form first so it clears too.
  have hrw : (q - q⁻¹) ^ 2 + 4 = (q + q⁻¹) ^ 2 := by field_simp; ring
  unfold deficitA3 survivingQTrace qBracket4 qBracket2 hval
  rw [brunnianW3_trace q hq, hrw]
  field_simp
  ring
