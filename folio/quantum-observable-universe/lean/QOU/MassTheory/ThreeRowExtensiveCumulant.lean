/-
# The q₀-free ≥3-row extensive cumulant: forward from the proved Δ_λ

Forward, q₀-free companion to `QOU.MassTheory.AdditiveResidualSimplex`.  There the
coordination-simplex `C(A,k)` cluster basis is fed the **q₀-dependent** residual
`M(A) = ρ_strong(A) − ρ_grad(A)` and the cumulants come out `μ₂ = 0`,
`μ₃ = +0.4708`, `μ₄ = −4.591` (q₀-evaluated MeV).  Here we feed the *same* basis
the **proved, purely combinatorial** ≥3-row content of the per-partition binding
value

    Δ_λ = (−1)^{n(λ)}·dim V_λ = (−1)^{n(λ)}·f^λ

(`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, sorry-free, general-n),
restricted to the **≥3-row stratum** `ℓ(λ) ≥ 3` — the stratum measured in PR #4664
to *dominate* the binding sum (26 % → 100 % of `B` as `A: 2 → 4`, opposite to the
two-row-dominated `tr_M`).  Summed over partitions of each cluster size `k`:

| k | ≥3-row `λ` | `f^λ` | `n(λ)` | `Δ_λ` | `s_k` |
|---|---|---|---|---|---|
| 1 | — | | | | 0 |
| 2 | — | | | | 0 |
| 3 | `(1³)` | 1 | 3 | −1 | −1 |
| 4 | `(2,1,1)`,`(1⁴)` | 3,1 | 3,6 | −3,+1 | −2 |

`s₁ = s₂ = 0` is structural (no partition of `k ≤ 2` has `≥ 3` rows).  Values
Python-verified in the companion probe
`computations/deltalambda/threerow_extensive_cumulant_forward_probe.py`.

## What is formalised (all sorry-free, base ring `ℤ` — pure combinatorics, no `ℝ`,
no `q₀`, per §7c)

* **Irreducibly ≥3-body / extensive (general):** `clusterF w S`, the size-consistent
  cluster functional summing a per-cardinality weight `w` (supported on `k ≥ 3`)
  over every `≥3`-element subset of a nucleon set `S`, **vanishes** on any `S` with
  `S.card ≤ 2` (`clusterF_eq_zero_of_card_le_two`).  This is the deuteron structural
  fact for *any* weight: `A = 2` carries no ≥3-body cluster content.
* **Concrete extensive values + ratio (Reading Y):** `Bext 2 = 0`, `Bext 3 = −1`,
  `Bext 4 = −6`, hence `Bext 4 = 6 · Bext 3` (`Bext_ratio_four_three`).
* **Forward cumulants (Mayer inversion, Reading X):** `ν₂ = 0`, `ν₃ = −1`, `ν₄ = +2`.
  - `forward_edge_coeff_zero : ν₂ = 0` — the 0-fit match to the derived `μ₂ = 0`,
    obtained here combinatorially and q₀-free.
  - `forward_sign_window_opposite : ν₃ < 0 ∧ 0 < ν₄` — the honest NEGATIVE: the
    signed-Springer-dimension *parity* gives the `(−,+)` order, the **opposite** of
    the derived `(+,−)` residual window (#4316, `κ ∈ (3/2,3)`).  So the many-body
    binding sign-change is **not** supplied by `Δ_λ` parity.
  - `forward_ratio_two : ν₄ = −2 · ν₃` — the forward 4-body/3-body magnitude ratio
    is exactly `2`, not the derived `≈ 9.75`.

**Derivation seam (sorry-free ≠ derived).** `sRow3` below is a *hand-entered table*
of the values `s_k`; the identity `sRow3 k = Σ_{λ⊢k, ℓ(λ)≥3} (−1)^{n(λ)}·f^λ` is
verified in the companion Python probe (exact integer hook-length arithmetic), **not
proved in Lean**.  Every theorem here is therefore Lean-proved *for this table*.  A
citing block must say "the ≥3-row table `sRow3` gives the (−,+) order", not "Lean
proves the ≥3-row Δ_λ stratum has (−,+) order".  This does not weaken the scope-(a)
negative (a negative is not strengthened by formalising the table), and closing the
seam would need SYT/hook-length combinatorics in Lean — out of scope here.

**Anti-fit (STRICT).** No AME value and no `q₀` appears in any statement or proof.
The AME binding ratios enter only the companion probe/audit as fixed *targets*,
never inverted.  This records a **scope-(a)** result (per AGENTS.md
§before-declaring-refuted): the q₀-free ≥3-row content, *alone*, does not reproduce
the many-body sign+magnitude — it is not a structural exclusion of the
extensive-cumulant program.  Nothing is wired to production.

Companion: `QOU.MassTheory.AdditiveResidualSimplex` (q₀ residual twin),
audit `docs/audits/2026-08-08-threerow-extensive-cumulant-forward-qfree.md`.
-/
import Mathlib.Tactic

namespace QOU.MassTheory
namespace ThreeRowExtensiveCumulant

open Finset

/-! ### The proved ≥3-row signed-Springer-dimension content `s_k` (combinatorial) -/

/-- `s_k = Σ_{λ⊢k, ℓ(λ)≥3} (−1)^{n(λ)}·f^λ`, the Δ_λ of
`dtEuler_eq_deltaLambda_unconditional` restricted to the ≥3-row stratum.  Concrete
integer values at `k ≤ 5` (Python-verified in the companion probe); `0` for
`k ≤ 2` because no partition of `k ≤ 2` has `≥ 3` rows. -/
def sRow3 : ℕ → ℤ
  | 3 => -1
  | 4 => -2
  | 5 => 4
  | _ => 0

/-! ### Irreducibly ≥3-body: the general cluster functional and its deuteron zero -/

/-- The extensive (size-consistent) cluster functional over a nucleon set `S`,
built from a per-cardinality weight `w` supported on cardinalities `≥ 3`: it sums
`w |T|` over every subset `T ⊆ S` with `|T| ≥ 3`.  Additive over disjoint subsets
by construction; irreducibly ≥3-body because subsets of size `< 3` contribute `0`. -/
def clusterF {ι : Type*} [DecidableEq ι] (w : ℕ → ℤ) (S : Finset ι) : ℤ :=
  ∑ T ∈ S.powerset, (if 3 ≤ T.card then w T.card else 0)

/-- **Irreducibly ≥3-body.**  On any set of `≤ 2` nucleons the cluster functional
vanishes identically, for *any* weight `w` — no `≥3`-element subset exists.  This is
the deuteron structural fact: `A = 2` carries no many-body cluster term. -/
theorem clusterF_eq_zero_of_card_le_two {ι : Type*} [DecidableEq ι]
    (w : ℕ → ℤ) (S : Finset ι) (hS : S.card ≤ 2) : clusterF w S = 0 := by
  unfold clusterF
  refine Finset.sum_eq_zero ?_
  intro T hT
  have hTS : T.card ≤ S.card := Finset.card_le_card (Finset.mem_powerset.mp hT)
  have : ¬ (3 ≤ T.card) := by omega
  simp [this]

/-! ### Concrete extensive values (Reading Y: `Bext A = Σ_{k≥3} C(A,k)·s_k`) -/

/-- The homogeneous evaluation of the extensive cluster functional at `A` nucleons:
`Bext A = Σ_k C(A,k)·s_k` (terms with `k < 3` vanish since `s_k = 0` there). -/
def Bext (A : ℕ) : ℤ := ∑ k ∈ Finset.range (A + 1), (A.choose k : ℤ) * sRow3 k

theorem Bext_two   : Bext 2 = 0  := by
  norm_num [Bext, Finset.sum_range_succ, Finset.sum_range_zero, sRow3, Nat.choose]
theorem Bext_three : Bext 3 = -1 := by
  norm_num [Bext, Finset.sum_range_succ, Finset.sum_range_zero, sRow3, Nat.choose]
theorem Bext_four  : Bext 4 = -6 := by
  norm_num [Bext, Finset.sum_range_succ, Finset.sum_range_zero, sRow3, Nat.choose]

/-- **The extensive `A=4 / A=3` ratio identity is exactly `6`** (⁴He / ³H skeleton):
`Bext 4 = 6 · Bext 3`.  Contrast the AME ratio `B(⁴He)/B(³H) ≈ 3.336` (probe): the
extensive reading overshoots by `+80 %`, 0-fit. -/
theorem Bext_ratio_four_three : Bext 4 = 6 * Bext 3 := by
  have h4 : Bext 4 = -6 := Bext_four
  have h3 : Bext 3 = -1 := Bext_three
  omega

/-- The deuteron extensive value is `0`: consistent with the general
`clusterF_eq_zero_of_card_le_two`.  The deuteron binding is a separate 2-body
object, not a ≥3-body cluster term. -/
theorem Bext_deuteron_zero : Bext 2 = 0 := Bext_two

/-! ### Forward cumulants (Reading X: Mayer inversion of `S(A) = s_A`) -/

/-- Single-algebra reading: `S(A) = s_A`. -/
def Salg (A : ℕ) : ℤ := sRow3 A

/-- Forward 2-body (edge) cumulant `ν₂ = S(2)`. -/
def nu2 : ℤ := Salg 2
/-- Forward 3-body (triangle) cumulant `ν₃ = S(3) − 3·ν₂`. -/
def nu3 : ℤ := Salg 3 - 3 * nu2
/-- Forward 4-body (tetrahedron) cumulant `ν₄ = S(4) − 6·ν₂ − 4·ν₃`. -/
def nu4 : ℤ := Salg 4 - 6 * nu2 - 4 * nu3

theorem nu_values : nu2 = 0 ∧ nu3 = -1 ∧ nu4 = 2 := by
  refine ⟨by decide, by decide, by decide⟩

/-- **0-fit structural match.**  The forward edge cumulant vanishes, `ν₂ = 0`,
matching the derived `μ₂ = 0` of `AdditiveResidualSimplex` — but derived here
combinatorially (`s₁ = s₂ = 0`), q₀-free and independent of the graded-ladder
deuteron self-reference. -/
theorem forward_edge_coeff_zero : nu2 = 0 := by decide

/-- **Honest NEGATIVE — wrong sign-change order.**  The forward ≥3-row cumulants
satisfy `ν₃ < 0 ∧ 0 < ν₄`, i.e. the `(−,+)` order.  The derived residual cumulants
are `(μ₃, μ₄) = (+, −)` (the #4316 sign window `κ ∈ (3/2,3)`).  So the proved `Δ_λ`
chirality parity produces the **opposite** 3-body/4-body sign change; it does not
supply the many-body binding sign-change window.  Scope-(a). -/
theorem forward_sign_window_opposite : nu3 < 0 ∧ 0 < nu4 := by
  refine ⟨by decide, by decide⟩

/-- **Honest NEGATIVE — wrong magnitude ratio.**  The forward 4-body/3-body
magnitude ratio is exactly `2` (`ν₄ = −2·ν₃`), whereas the derived residual needs
`|μ₄/μ₃| ≈ 9.75`.  The ≥3-row combinatorial content does not supply the derived
magnitude ratio (miss ≈ 4.9×). -/
theorem forward_ratio_two : nu4 = -2 * nu3 := by decide

/-- The forward cumulants are NOT the derived residual cumulants: their sign
pattern is `(−,+)`, not the derived `(+,−)`.  Recorded as a single conjunction for
downstream citation. -/
theorem forward_cumulants_not_derived_pattern :
    nu2 = 0 ∧ (nu3 < 0 ∧ 0 < nu4) ∧ nu4 = -2 * nu3 :=
  ⟨forward_edge_coeff_zero, forward_sign_window_opposite, forward_ratio_two⟩

/-- **Five-body extensive value `Bext 5 = -16` and Mayer cluster reconstruction (`qou-3exu`).**
At `A = 5`, `Bext 5 = C(5,3) s₃ + C(5,4) s₄ + C(5,5) s₅ = -10 - 10 + 4 = -16`, and
the Mayer cumulants `(ν₂, ν₃, ν₄) = (0, -1, 2)` reconstruct `Salg 3` and `Salg 4` exactly. -/
theorem Bext_five_and_mayer_reconstruct :
    Bext 5 = -16 ∧
    Bext 4 - 4 * Bext 3 = sRow3 4 ∧
    3 * nu2 + nu3 = Salg 3 ∧
    6 * nu2 + 4 * nu3 + nu4 = Salg 4 := by
  refine ⟨?_, by decide, by decide, by decide⟩
  norm_num [Bext, Finset.sum_range_succ, Finset.sum_range_zero, sRow3, Nat.choose]

end ThreeRowExtensiveCumulant
end QOU.MassTheory
