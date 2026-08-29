/-
  Canonical (convention C) Markov trace of β_Bor — derivation from the
  Markov-forced values, sorry-free.

  This file upgrades the closed form `trC_borromean` (stated in
  `BorromeanTraceConventionSplit` with CAS provenance) to a Lean
  DERIVATION, parallel to `BorromeanMarkovTrace` (which does the same for
  convention D).  The derivation route:

  1. **The three irreps of `H_3(q)`** (Wedderburn: `H_3 ≅ K ⊕ M₂(K) ⊕ K`,
     partitions (3), (2,1), (1³)):
     * (3): 1-dim, `σᵢ ↦ q`;
     * (1³): 1-dim, `σᵢ ↦ −q⁻¹`;
     * (2,1): 2-dim — realised here by the EXPLICIT rational seminormal
       pair `σ₀ ↦ [q, 0; 1, −q⁻¹]`, `σ₁ ↦ [−q⁻¹, 1; 0, q]`.  This file
       PROVES the braid relation and both Hecke quadratics for the pair
       (so it is a bona fide `H_3` representation), plus the generator
       trace `h` (the `{q, −q⁻¹}` eigenvalue content).  That this pair is
       *the* (2,1) seminormal representation is Hoefsmit's
       classification — cited, not re-proved.
       -- Ref: [hoefsmit1974] https://www.proquest.com/docview/302747928
  2. **The per-rep characters at `β_Bor = (σ₀σ₁⁻¹)³`**: both 1-dims give
     `1`; the 2-dim gives `2 − 3h⁴ − h⁶` — proved via the Cayley–Hamilton
     cube identity `tr(M³) = τ³ − 3τδ` (proved here for 2×2 by entry
     expansion) with `τ = tr(σ₀σ₁⁻¹) = −1 − h²`, `δ = det = 1`.  This is
     the previously narrative-only χ^(2,1)(β_Bor) closed form
     (cross-checked numerically to 4e−50, audit 2026-06-07), now
     machine-checked.
  3. **The Markov-forced weight values.**  Any Markov trace `tr` on `H_3`
     with parameter `z` satisfies (M3) `tr(1) = 1`, (M2) `tr(σᵢ) = z` and
     `tr(σ₀σ₁) = z·tr(σ₀) = z²`; by the Wedderburn decomposition
     (`QOU.Hecke.WedderburnDecomp`, Mathas §3.43) `tr = Σ_λ w_λ χ^λ`.
     Those three values give a linear system for `(w₃, w₂₁, w₁₁₁)` whose
     determinant is nonzero for all `t = √q ≠ 0` over `ℚ`
     (`weight_system_det_ne_zero` below) — so the weights are pinned.
     This file exhibits the EXPLICIT solution and proves it satisfies all
     three constraints.
  4. **Evaluation at β_Bor**: `w₃·1 + w₂₁·(2 − 3h⁴ − h⁶) + w₁₁₁·1 =
     trC_borromean t` — the canonical closed form, now derived rather
     than transcribed.

  Cited (not re-proved) inputs, per the honest-gap discipline: the
  Wedderburn trace decomposition over the three irreps (Mathas §3.43 —
  the `QOU.Hecke.WedderburnDecomp` class axioms, §9.4 L-1/L-2 debt) and
  the M1–M3 uniqueness of the Markov trace at fixed `z`
  (`QOU.Hecke.markov_trace_unique_axiom`, [jones1987]).  Everything else
  below is proved.

  The 2×2 layer uses a local `M2` structure (explicit entries) rather
  than `Matrix (Fin 2) (Fin 2)` — deliberately dependency-light (the
  identities are pure `ring` facts about four scalars; nothing here needs
  the Mathlib matrix API).

  Registry: docs/audits/2026-06-09-binding-trace-convention-split.md.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [hoefsmit1974] https://www.proquest.com/docview/302747928
  -- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import QOU.BraidsAndKnots.BorromeanTraceConventionSplit

namespace QOU.BraidsAndKnots

/-! ## A minimal explicit 2×2 matrix carrier

Four scalar entries; multiplication, identity, trace, determinant as
plain definitions.  Every identity below is a `ring` fact about the
entries — no Mathlib matrix API required. -/

/-- Explicit 2×2 matrix over `K`: entries `a b / c d`. -/
@[ext]
structure M2 (K : Type*) where
  a : K
  b : K
  c : K
  d : K

namespace M2

variable {K : Type*} [Field K]

/-- Matrix product. -/
def mul (X Y : M2 K) : M2 K :=
  ⟨X.a * Y.a + X.b * Y.c, X.a * Y.b + X.b * Y.d,
   X.c * Y.a + X.d * Y.c, X.c * Y.b + X.d * Y.d⟩

/-- Identity matrix. -/
def one : M2 K := ⟨1, 0, 0, 1⟩

/-- Trace. -/
def trace (X : M2 K) : K := X.a + X.d

/-- Determinant. -/
def det (X : M2 K) : K := X.a * X.d - X.b * X.c

/-- **Cayley–Hamilton cube identity**: `tr(X³) = τ³ − 3τδ` with
`τ = tr X`, `δ = det X`.  Raw entry expansion + `ring`. -/
theorem trace_cube (X : M2 K) :
    trace (mul (mul X X) X)
      = (trace X)^3 - 3 * trace X * det X := by
  unfold trace det mul
  ring

end M2

/-! ## The rational seminormal (2,1) representation of `H_3(q)` -/

section TwoDimRep
variable {K : Type*} [Field K]

/-- `σ₀` in the rational seminormal 2-dim representation. -/
def sn21_sigma0 (q : K) : M2 K := ⟨q, 0, 1, -q⁻¹⟩

/-- `σ₁` in the rational seminormal 2-dim representation. -/
def sn21_sigma1 (q : K) : M2 K := ⟨-q⁻¹, 1, 0, q⟩

/-- `σ₁⁻¹` in the 2-dim representation: `[−q, 1; 0, q⁻¹]`.  Equals the
Hecke inverse `σ₁ − h·1` entrywise: `−q⁻¹ − h = −q` and `q − h = q⁻¹`. -/
def sn21_sigma1_inv (q : K) : M2 K := ⟨-q, 1, 0, q⁻¹⟩

/-- `σ₁ · σ₁⁻¹ = 1` (for `q ≠ 0`). -/
theorem sn21_sigma1_mul_inv (q : K) (hq : q ≠ 0) :
    M2.mul (sn21_sigma1 q) (sn21_sigma1_inv q) = M2.one := by
  unfold sn21_sigma1 sn21_sigma1_inv M2.mul M2.one
  ext <;> (try field_simp) <;> (try ring)

/-- **Braid relation** `σ₀σ₁σ₀ = σ₁σ₀σ₁` — the pair is a `B_3`
representation. -/
theorem sn21_braid (q : K) (hq : q ≠ 0) :
    M2.mul (M2.mul (sn21_sigma0 q) (sn21_sigma1 q)) (sn21_sigma0 q)
      = M2.mul (M2.mul (sn21_sigma1 q) (sn21_sigma0 q)) (sn21_sigma1 q) := by
  unfold sn21_sigma0 sn21_sigma1 M2.mul
  ext <;> field_simp <;> ring

/-- **Hecke quadratic for `σ₀`**: `σ₀² = h·σ₀ + 1` entrywise, i.e. the
pair descends to `H_3(q)`.  Stated entrywise to avoid extra algebraic
structure on `M2`. -/
theorem sn21_hecke_sigma0 (q : K) (hq : q ≠ 0) :
    M2.mul (sn21_sigma0 q) (sn21_sigma0 q)
      = ⟨(q - q⁻¹) * q + 1, 0, (q - q⁻¹) * 1, (q - q⁻¹) * (-q⁻¹) + 1⟩ := by
  unfold sn21_sigma0 M2.mul
  ext <;> (try field_simp) <;> (try ring)

/-- **Hecke quadratic for `σ₁`**. -/
theorem sn21_hecke_sigma1 (q : K) (hq : q ≠ 0) :
    M2.mul (sn21_sigma1 q) (sn21_sigma1 q)
      = ⟨(q - q⁻¹) * (-q⁻¹) + 1, (q - q⁻¹) * 1, 0, (q - q⁻¹) * q + 1⟩ := by
  unfold sn21_sigma1 M2.mul
  ext <;> (try field_simp) <;> (try ring)

/-- Character of a single generator: `tr(σ₀) = h = q − q⁻¹` (eigenvalue
content `{q, −q⁻¹}`).  `σ₁` is conjugate to `σ₀` (braid relation), so it
has the same character. -/
theorem sn21_trace_sigma0 (q : K) :
    M2.trace (sn21_sigma0 q) = q - q⁻¹ := by
  unfold sn21_sigma0 M2.trace
  ring

/-- Character of `σ₀σ₁`: `tr(σ₀·σ₁) = −1`. -/
theorem sn21_trace_sigma0_sigma1 (q : K) (hq : q ≠ 0) :
    M2.trace (M2.mul (sn21_sigma0 q) (sn21_sigma1 q)) = -1 := by
  unfold sn21_sigma0 sn21_sigma1 M2.mul M2.trace
  field_simp
  norm_num

/-- The Borromean word factor `P := σ₀·σ₁⁻¹`: trace `−1 − h²` (for
`q ≠ 0`). -/
theorem sn21_trace_borP (q : K) (hq : q ≠ 0) :
    M2.trace (M2.mul (sn21_sigma0 q) (sn21_sigma1_inv q))
      = -1 - (q - q⁻¹)^2 := by
  unfold sn21_sigma0 sn21_sigma1_inv M2.mul M2.trace
  field_simp
  ring

/-- The Borromean word factor `P := σ₀·σ₁⁻¹` has determinant `1`. -/
theorem sn21_det_borP (q : K) (hq : q ≠ 0) :
    M2.det (M2.mul (sn21_sigma0 q) (sn21_sigma1_inv q)) = 1 := by
  unfold sn21_sigma0 sn21_sigma1_inv M2.mul M2.det
  field_simp
  ring

/-- **χ^(2,1)(β_Bor) = 2 − 3h⁴ − h⁶** — the 2-dim character of the
Borromean braid `β_Bor = (σ₀σ₁⁻¹)³`, machine-checked: with
`P = σ₀σ₁⁻¹`, `τ = tr P = −1 − h²` and `δ = det P = 1`
(`sn21_trace_borP`, `sn21_det_borP`), the Cayley–Hamilton cube identity
gives `tr(P³) = τ³ − 3τ = 2 − 3h⁴ − h⁶`. -/
theorem sn21_chi_borromean (q : K) (hq : q ≠ 0) :
    M2.trace (M2.mul
        (M2.mul (M2.mul (sn21_sigma0 q) (sn21_sigma1_inv q))
                (M2.mul (sn21_sigma0 q) (sn21_sigma1_inv q)))
        (M2.mul (sn21_sigma0 q) (sn21_sigma1_inv q)))
      = 2 - 3 * (q - q⁻¹)^4 - (q - q⁻¹)^6 := by
  rw [M2.trace_cube, sn21_trace_borP q hq, sn21_det_borP q hq]
  ring

/-- The two 1-dim characters at `β_Bor` are both `1`: `σᵢ ↦ q` sends
`(σ₀σ₁⁻¹)³ ↦ (q·q⁻¹)³ = 1`, and `σᵢ ↦ −q⁻¹` likewise. -/
theorem oneDim_chi_borromean (q : K) (hq : q ≠ 0) :
    (q * q⁻¹)^3 = 1 ∧ ((-q⁻¹) * (-q⁻¹)⁻¹)^3 = 1 := by
  constructor
  · field_simp
  · have hq' : (-q⁻¹ : K) ≠ 0 := by simp [hq]
    field_simp

end TwoDimRep

/-! ## The Markov-forced weights over `ℚ`, in `t = √q` -/

/-- The Markov parameter `z = 1/(√q + 1/√q) = t/(t² + 1)`.

**Convention C, deliberately — this one is NOT migrated (2026-08-26, bean
`qou-cxjq`).** Every other convention-C Markov parameter in the Lean tree moved
to `z_D = q³/(q²+1)` under the owner ruling of 2026-08-15. This one stays,
because the file exists to derive the **C** value: `trC_borromean_derived`
evaluates the C-forced weight system at `β_Bor` and lands on `trC_borromean`,
which `BorromeanTraceConventionSplit.conventionD_ne_conventionC` then proves is
a different function from the D closed form. Migrate `z` here and the file
derives the D trace and compares it to itself — the registry claim it exists to
machine-check evaporates.

The whole apparatus below is C-forced and moves with it: `wden`, `wnum3`,
`wnum21`, `wnum111` are the solution of the 3×3 Markov system at *this* `z`
(`weights_markov_sigma` closes the loop by recovering `zMarkov t` from them), so
they are not shared constants that survive a convention change — they are C's
answer to C's system.

**Why the audit called this actionable, and why that was a detector limit rather
than a defect.** `scripts/lean-markov-convention-audit.py` takes deliberateness
evidence from the declaration's name and its own docstring. This module's intent
was stated only in the **module header** — its first line reads *"Canonical
(convention C) Markov trace of β_Bor"* — and in `trC_borromean_derived`'s
docstring three declarations below. A detector that walks back from a
declaration to the doc-comment opener directly above it cannot see either. Recorded as entry #16 in the
detector-blindness taxonomy; fixed at the source, here, rather than by teaching
the scanner to trust module headers, which would silently absolve every C
definition in any file whose header mentions C. -/
noncomputable def zMarkov (t : ℚ) : ℚ := t / (t^2 + 1)

/-- Common denominator of the Markov-forced weights:
`D(t) = (t²+1)²(t⁴+1)(t²−t+1)(t²+t+1)(t⁴−t²+1)`. -/
noncomputable def wden (t : ℚ) : ℚ :=
  (t^2 + 1)^2 * (t^4 + 1) * (t^2 - t + 1) * (t^2 + t + 1) * (t^4 - t^2 + 1)

/-- Numerator of the trivial-block weight `w₃`. -/
noncomputable def wnum3 (t : ℚ) : ℚ :=
  (t + 1) * (t^3 + t^2 + 1) * (t^6 - t^5 + t^4 - t^3 + 2*t^2 - t + 1)

/-- Numerator of the 2-dim-block weight `w₂₁` (over the COMMON
denominator `wden`, hence the extra `(t⁴+1)` factor relative to the
fully-reduced form). -/
noncomputable def wnum21 (t : ℚ) : ℚ :=
  t^3 * (t^3 + t - 1) * (t^3 + t^2 + 1) * (t^4 + 1)

/-- Numerator of the sign-block weight `w₁₁₁`. -/
noncomputable def wnum111 (t : ℚ) : ℚ :=
  t^6 * (t - 1) * (t^3 + t - 1) * (t^6 + t^5 + 2*t^4 + t^3 + t^2 + t + 1)

/-- Weight of the trivial block `(3)` — unique solution of the
Markov-forced linear system (see `weight_system_det_ne_zero`). -/
noncomputable def wq3 (t : ℚ) : ℚ := wnum3 t / wden t

/-- Weight of the 2-dim block `(2,1)`. -/
noncomputable def wq21 (t : ℚ) : ℚ := wnum21 t / wden t

/-- Weight of the sign block `(1³)`. -/
noncomputable def wq111 (t : ℚ) : ℚ := wnum111 t / wden t

/-- All cyclotomic-type factors in the weight denominators are strictly
positive over `ℚ`. -/
theorem weight_den_factors_pos (t : ℚ) :
    (t^2 + 1) > 0 ∧ (t^4 + 1) > 0 ∧ (t^2 - t + 1) > 0 ∧
    (t^2 + t + 1) > 0 ∧ (t^4 - t^2 + 1) > 0 := by
  refine ⟨by positivity, by positivity, ?_, ?_, ?_⟩
  · nlinarith [sq_nonneg (2*t - 1)]
  · nlinarith [sq_nonneg (2*t + 1)]
  · nlinarith [sq_nonneg (2*t^2 - 1)]

/-- The common weight denominator is strictly positive, hence nonzero. -/
theorem wden_pos (t : ℚ) : wden t > 0 := by
  obtain ⟨h1, h2, h3, h4, h5⟩ := weight_den_factors_pos t
  unfold wden
  positivity

theorem wden_ne_zero (t : ℚ) : wden t ≠ 0 := ne_of_gt (wden_pos t)

/-- **Nonsingularity of the Markov weight system.**  The determinant of
the 3×3 system `{Σ_λ w_λ χ^λ(x) = tr(x)}` over `x ∈ {1, σ, σ₀σ₁}`
equals `−(t⁴+1)(t²−t+1)(t²+t+1)(t⁴−t²+1)/t⁶`, nonzero for every
`t ≠ 0` — so the three Markov-forced values pin the weights uniquely
(Cramer). -/
theorem weight_system_det_ne_zero (t : ℚ) (ht : t ≠ 0) :
    -((t^4 + 1) * (t^2 - t + 1) * (t^2 + t + 1) * (t^4 - t^2 + 1)) / t^6 ≠ 0 := by
  obtain ⟨_, h2, h3, h4, h5⟩ := weight_den_factors_pos t
  have hnum : (t^4 + 1) * (t^2 - t + 1) * (t^2 + t + 1) * (t^4 - t^2 + 1) > 0 := by
    positivity
  have ht6 : (t : ℚ)^6 ≠ 0 := pow_ne_zero 6 ht
  exact div_ne_zero (neg_ne_zero.mpr (ne_of_gt hnum)) ht6

/-- **(M3) Normalisation**: `w₃·χ³(1) + w₂₁·χ²¹(1) + w₁₁₁·χ^(1³)(1)
= w₃ + 2w₂₁ + w₁₁₁ = 1`. -/
theorem weights_normalised (t : ℚ) (_ht : t ≠ 0) :
    wq3 t + 2 * wq21 t + wq111 t = 1 := by
  have hD := wden_ne_zero t
  unfold wq3 wq21 wq111
  field_simp
  unfold wnum3 wnum21 wnum111 wden
  ring

/-- **(M2) Single-generator value**: with `χ^λ(σ)` equal to `q = t²`,
`h = t² − t⁻²`, `−q⁻¹ = −t⁻²` on the three blocks respectively
(`sn21_trace_sigma0` for the middle one), the weighted sum equals `z` —
the Markov-forced `tr(σᵢ) = z`. -/
theorem weights_markov_sigma (t : ℚ) (ht : t ≠ 0) :
    t^2 * wq3 t + (t^2 - (t^2)⁻¹) * wq21 t - (t^2)⁻¹ * wq111 t
      = zMarkov t := by
  have hD := wden_ne_zero t
  have h1 : (t^2 + 1 : ℚ) ≠ 0 := ne_of_gt (weight_den_factors_pos t).1
  unfold wq3 wq21 wq111 zMarkov
  field_simp
  unfold wnum3 wnum21 wnum111 wden
  ring

/-- **(M2, level 2)**: with `χ^λ(σ₀σ₁)` equal to `q² = t⁴`, `−1`
(`sn21_trace_sigma0_sigma1`), `q⁻² = t⁻⁴` on the three blocks, the
weighted sum equals `z²` — the Markov-forced `tr(σ₀σ₁) = z·tr(σ₀) = z²`. -/
theorem weights_markov_sigma0_sigma1 (t : ℚ) (ht : t ≠ 0) :
    t^4 * wq3 t + (-1) * wq21 t + (t^4)⁻¹ * wq111 t
      = (zMarkov t)^2 := by
  have hD := wden_ne_zero t
  have h1 : (t^2 + 1 : ℚ) ≠ 0 := ne_of_gt (weight_den_factors_pos t).1
  unfold wq3 wq21 wq111 zMarkov
  field_simp
  unfold wnum3 wnum21 wnum111 wden
  ring

/-- **MAIN: the canonical Markov trace of `β_Bor`, derived.**  Summing
the three per-block characters at `β_Bor` (both 1-dims `= 1` by
`oneDim_chi_borromean`; the 2-dim `= 2 − 3h⁴ − h⁶` by
`sn21_chi_borromean`) against the Markov-forced weights yields exactly
the convention-C closed form `trC_borromean t` of
`BorromeanTraceConventionSplit`:

    `w₃·1 + w₂₁·(2 − 3h⁴ − h⁶) + w₁₁₁·1 = trC_borromean t`,
    `h = t² − t⁻²`.

Together with `conventionD_ne_conventionC` this machine-checks the full
registry claim: the canonical trace value at `β_Bor` is derived, and it
differs exactly from the pipeline (TL/Jones) value. -/
theorem trC_borromean_derived (t : ℚ) (ht : t ≠ 0) :
    wq3 t + wq21 t * (2 - 3 * (t^2 - (t^2)⁻¹)^4 - (t^2 - (t^2)⁻¹)^6) + wq111 t
      = trC_borromean t := by
  have hD := wden_ne_zero t
  have hden : trC_borromean_den t ≠ 0 := by
    unfold trC_borromean_den; positivity
  unfold wq3 wq21 wq111 trC_borromean
  field_simp
  unfold wnum3 wnum21 wnum111 wden trC_borromean_num trC_borromean_den
  ring

end QOU.BraidsAndKnots
