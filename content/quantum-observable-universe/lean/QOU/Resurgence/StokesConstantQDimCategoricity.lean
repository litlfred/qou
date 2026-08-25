import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.Resurgence.StokesConstantQDimCategoricity

**Horn 2 (bean `qou-nkm1`, epic `qou-r2nh`): are the descent-scaffold bar-orbit
magnitudes categorical q-dimensions?**  Companion to
`QOU.Resurgence.StokesMatrixDescent` / `WardFiltrationCounting` (PR #4525), whose
Ward↔filtration counting forced `|Δ_λ| = |Δ_{λ'}|` and *relocated* the residual
gap to two categoricity questions — the *sign* (horn 1) and the *magnitude*
(horn 2, this file).

The established datum is the GGM state-integral Stokes constant of the
figure-eight `4₁`: the integer `3` (off-diagonal of `S⁺(q→0) = [[1,3],[0,1]]`),
with descendant `q`-series `S⁺_{σ₁σ₁}(1;q̃) = 1 − 8q̃ − 9q̃² + 18q̃³ + 46q̃⁴ + …`
(GGM 2012.00062 eq 21, proven for `4₁`; the per-winding integer family of
`2026-07-31-awpk-perwinding-stokes-41.md`).

**Result — honest NEGATIVE.**  The direct "orbit magnitudes = q-dimensions"
identification fails, for two proved reasons:

1. **The `3 = [3]_{q=1}` match is vacuous.**  `[n]_q|_{q=1} = n` (`qInt_at_one`),
   so the `q=1` quantum-integer spectrum is *all of* `ℕ`; every integer `k` is
   `[k]_1`.  A `q=1` match carries no information.

2. **At `q ≠ 1` the Stokes `q`-series is structurally excluded** from being a
   categorical q-dimension: a q-dimension lies in `ℕ[q,q⁻¹]` (non-negative
   integer coefficients — the KL/crystal positivity, the same invariant the
   PROBE-4 prune used on the *sign*), while the Stokes descendant series has
   `coeff₁ = −8 < 0`.  Hence no non-negative-coefficient polynomial — no
   q-dimension, no `ℕ`-combination of them — equals it.

All statements are proved sorry-free over a generic `[Field K]` (the q-integer
facts) or `Polynomial ℤ` (the coefficient-positivity exclusion); no archimedean
input, no `c_k`, no `Δ_λ` wired, nothing to production (§7c).

Ref: manuscript, mass-theory/stokes-orbit-magnitude-qdim; GGM arXiv:2012.00062.
-/

namespace QOU.Resurgence

open Finset

/-- The **quantum integer** `[n]_q = ∑_{i<n} qⁱ = 1 + q + ⋯ + q^{n-1}`.  Mirrors
the corpus `QOU.MathlibExt.qInt` (`QIntegerFactorial.lean`); reproduced locally
so this refutation verifies against Mathlib alone. -/
noncomputable abbrev qInt {K : Type*} [Field K] (q : K) (n : ℕ) : K :=
  QOU.QInteger.qIntGeo q n

/-! ## 1. The `q = 1` vacuity engine — every integer is a `q=1` quantum integer -/

section Vacuity

variable {K : Type*} [Field K]

/-- **`q = 1` quantum-integer spectrum is all of `ℕ`.**  `[n]_q|_{q=1} = n`.
This is the vacuity engine: since *every* natural number `n` equals `[n]_1`, a
match "integer `k` = `[k]_{q=1}`" (as for the Stokes constant `3 = [3]_1`)
carries **no** categorical information — it holds for `8`, `46`, `90` alike. -/
theorem qInt_at_one (n : ℕ) : qInt (1 : K) n = n := by
  simp [qInt]

/-- `[3]_q = 1 + q + q²` — genuinely `q`-dependent (over any field). -/
theorem qInt_three (q : K) : qInt q 3 = 1 + q + q ^ 2 := by
  simp [qInt, Finset.sum_range_succ]

/-- The observed match `[3]_1 = 3`, exhibited as the **vacuous** `q=1`
coincidence (a special case of `qInt_at_one`). -/
theorem qInt_three_at_one : qInt (1 : K) 3 = 3 := by
  rw [qInt_at_one]; norm_num

end Vacuity

/-! ## 2. Off `q = 1`: the constant `3` is not the polynomial `[3]_q`

The categorical content, if any, must live at `q ≠ 1`.  As polynomials the
`q`-independent constant `3` differs from `[3]_q = 1 + q + q²`; they agree only
at the vacuous point `q = 1`. -/

section OffOne

open Polynomial

/-- `[3]_q` as a polynomial in `ℤ[q]`. -/
noncomputable def qIntThreePoly : Polynomial ℤ := 1 + X + X ^ 2

/-- **The match fails off `q = 1`.**  `[3]_q ≠ 3` as polynomials — the degree-1
coefficient is `1 ≠ 0`.  So the geometric Stokes constant `3` equals `[3]_q`
*only* at the vacuous point `q = 1`, never as a `q`-series identity. -/
theorem qIntThreePoly_ne_const_three : qIntThreePoly ≠ (3 : Polynomial ℤ) := by
  intro h
  have h1 : qIntThreePoly.coeff 1 = (3 : Polynomial ℤ).coeff 1 := by rw [h]
  simp [qIntThreePoly, coeff_one, coeff_X, coeff_X_pow] at h1

end OffOne

/-! ## 3. The positivity exclusion (scope-(b), proved invariant)

A categorical q-dimension is a non-negative integer combination of quantum
integers, hence lies in `ℕ[q,q⁻¹]`: its coefficients are `≥ 0`.  The GGM Stokes
descendant series has a **negative** coefficient, so it is excluded. -/

section Positivity

open Polynomial

/-- The quantum-integer polynomial `[n]_q = ∑_{i<n} qⁱ` over `ℤ`. -/
noncomputable def qIntPoly (n : ℕ) : Polynomial ℤ := ∑ i ∈ range n, X ^ i

/-- Its `k`-th coefficient is `1` if `k < n`, else `0`. -/
theorem qIntPoly_coeff (n k : ℕ) :
    (qIntPoly n).coeff k = if k < n then 1 else 0 := by
  simp only [qIntPoly, finset_sum_coeff, coeff_X_pow]
  rw [Finset.sum_ite_eq (range n) k (fun _ => (1 : ℤ))]
  simp [Finset.mem_range]

/-- **Positivity invariant.**  Every coefficient of a quantum-integer polynomial
is non-negative (indeed `∈ {0,1}`).  The categorical q-dimensions inherit this:
they are `ℕ`-combinations of such objects. -/
theorem qIntPoly_coeff_nonneg (n k : ℕ) : 0 ≤ (qIntPoly n).coeff k := by
  rw [qIntPoly_coeff]; split <;> norm_num

/-- The GGM `4₁` Stokes **descendant series** (leading terms, exact integers):
`1 − 8q̃ − 9q̃² + 18q̃³ + 46q̃⁴`. -/
noncomputable def stokesDesc : Polynomial ℤ :=
  1 - C 8 * X - C 9 * X ^ 2 + C 18 * X ^ 3 + C 46 * X ^ 4

/-- **The Stokes series carries a negative coefficient:** `coeff₁ = −8`. -/
theorem stokesDesc_coeff_one_neg : stokesDesc.coeff 1 = -8 := by
  simp [stokesDesc, coeff_one, coeff_X, coeff_X_pow]

/-- **Structural exclusion (scope-(b)).**  No polynomial with non-negative
coefficients equals the Stokes descendant series — because that series has
`coeff₁ = −8 < 0`.  In particular **no categorical q-dimension, and no
`ℕ`-combination of q-dimensions, is the Stokes series.**  This is the magnitude
analogue of the KL-positivity prune that excluded the *sign*. -/
theorem stokes_not_nonneg_combination {p : Polynomial ℤ}
    (hp : ∀ k, 0 ≤ p.coeff k) : p ≠ stokesDesc := by
  intro h
  have : (0 : ℤ) ≤ stokesDesc.coeff 1 := h ▸ hp 1
  rw [stokesDesc_coeff_one_neg] at this
  norm_num at this

/-- In particular the Stokes series is **not** any quantum integer `[n]_q`. -/
theorem stokesDesc_ne_qIntPoly (n : ℕ) : stokesDesc ≠ qIntPoly n :=
  fun h => stokes_not_nonneg_combination (qIntPoly_coeff_nonneg n) h.symm

end Positivity

/-! ## 4. The horn-2 positive hypothesis — OPEN carrier (no instance)

The claim "the bar-orbit magnitude spectrum *is* a categorical q-dimension
spectrum" is the horn-2 positive.  Per anti-fit / anti-laundering discipline it
is **not** instantiated (the §3 obstruction shows the direct identification
fails); it is recorded as a content-bearing open carrier with **no instance**. -/

section OpenCarrier

/-- **OPEN (bean `qou-nkm1`).**  Hypothesis that a family of bar-orbit Stokes
magnitudes `mag : ι → Polynomial ℤ` is a categorical q-dimension spectrum: each
magnitude coincides, *as a `q`-series* (not merely at the vacuous `q=1`), with a
quantum-integer polynomial `[n(i)]_q`.  Deliberately **no instance** — the
figure-eight datum refutes the direct route (`stokesDesc_ne_qIntPoly`,
`qIntThreePoly_ne_const_three`), so instantiating this would launder a refuted
identification.  Content-bearing: the field is a genuine `q`-series equality, not
`True`. -/
structure OrbitMagnitudesAreQDims {ι : Type*} (mag : ι → Polynomial ℤ) : Prop where
  /-- Each orbit magnitude is *some* quantum integer as a full `q`-series. -/
  isQDim : ∀ i, ∃ n : ℕ, mag i = qIntPoly n

end OpenCarrier

end QOU.Resurgence
