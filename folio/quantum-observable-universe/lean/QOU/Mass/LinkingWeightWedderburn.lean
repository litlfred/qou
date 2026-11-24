/-
QOU.Mass.LinkingWeightWedderburn — `lw` is a Wedderburn object: its cusp pole is a
dimension SUM and its regular part a partition COUNT.

Bean `qou-brng`, residual (ii). Companion to
`computations/probes/lw_cusp_pole_is_classical_probe.py` (11/11 exact checks over ℚ(q)),
which measures the same identities symbolically; this file proves them.

WHY THIS FILE EXISTS. `QOU.Mass.BindingMassRung` carries the mass/binding ℏ_q-rung
dichotomy with `lw` as an OPAQUE real parameter — its docstring says only
"lw = linking_weight, O(1) at the classical point". Nothing in Lean said what `lw`
IS. `lw_is_framing_independent_probe.py` established it is not a diagrammatic
quantity at all (not writhe-, not self-linking-valued; no knot, no diagram, no
framing in its signature) but the normalised sum of quantum dimensions
`(1/4)·Σ_{λ⊢4} dim_q V_λ`. This file formalises that, and the consequence.

WHAT IS PROVED (all sorry-free; `#print axioms` gives only `propext`,
`Classical.choice`, `Quot.sound` on every theorem below).

  lw/ℏ_q²  =  (Σ_{λ⊢4} dim V_λ)/4 · ℏ_q⁻²  +  (#{λ⊢4 : dim V_λ > 1})/4 · (q+1)²
           =  (10/4)·ℏ_q⁻²                 +  (3/4)·(q+1)²

so BOTH pieces count partitions of 4: the singular coefficient is a quarter of the
ordinary DIMENSION SUM, the regular tail a quarter of the COUNT of partitions whose
q-dimension actually deforms. The mechanism is per-partition,

  `dimQ_eq_classical_add_defMult_mul_hSq` :  dim_q λ = dim V_λ + m_λ·h²,   h = q − q⁻¹

with `m = (0, 1, 1, 1, 0)`, and `defMult_eq_zero_iff` : `m_λ = 0 ↔ dim V_λ = 1`. So
the one-dimensional irreducibles `(4)` and `(1⁴)` have `dim_q = 1` identically and
contribute POLE ONLY; the three higher-dimensional ones carry the whole regular tail.
`defMult_sum_eq_card_nontrivial` is the identification that makes the headline
`lw_eq_dimSum_add_count` content-bearing rather than a restatement of the closed form:
the corpus records 3/4 as a bare rational, and it is a quarter of that count.

`mass_multiplier_split` is also the POLE-PURITY statement in closed form — a pure
double pole plus a polynomial, with no simple-pole term — and `lw_bar_even` is why:
`h²` is bar-even under `q ↦ q⁻¹` while `h` is bar-odd, so the ℏ_q⁻¹ coefficient has
nothing to come from.

CONSEQUENCE FOR RESIDUAL (ii). The bean asks why the binding channel enters as a bare
integer count while the mass channel "keeps the full q-dimension". The split above
shows the regular part is not a different KIND of object from the pole — it is the
non-abelian part of the same Wedderburn spectrum, counted instead of summed. So the
asymmetry between the two channels is one of PROVENANCE (`lw` a Wedderburn q-dimension
sum, `M` a topological coordination count), not of where in the ℏ_q-expansion to look:
`lw/ℏ_q²` is representation-theoretic in BOTH its singular and regular parts. That
provenance question is untouched here and remains the open item.

NOT PROVED, and recorded so it is not assumed. (1) This file does not derive residual
(ii). (2) It does not touch the bean's title claim (saturated binding fraction = ℏ_q²),
which AGENTS.md records as suspect numerology with the volume-defect route refuted.
(3) The clean form `dim_q λ = dim V_λ + m_λ h²` with `m_λ` a CONSTANT is special to
n ∈ {2, 4}; it FAILS at n = 3, 5, 6, where some `dim_q` needs `h⁴` or higher, so at
other n the regular part is not a multiple of `(q+1)²` and this two-term split does
not exist. Do not carry it up a tower on the strength of n = 4 (measured in the
companion probe, check A10).

CONVENTIONS. `dimQ` is the SYMMETRIC convention, `[k]_q = (q^k − q^{−k})/(q − q^{−1})`.
The fake-degree convention gives `(1/4)Σ dim_q = 3q²/4 + q/2 + 5/4`, a DIFFERENT
function, and would change every number here — cf. the AGENTS.md note that `dim_q`
alone is ambiguous. Verified against `lw`'s recorded closed form by `lw_eq_closed`.

BASE RING (§7c). Everything is stated over a generic `{R : Type*} [Field R]`: these are
rational-function identities with no archimedean content, so no ordering, no `Real.sqrt`,
no `ℝ`. `BindingMassRung` specialises to `ℝ` for the archimedean limit statements; that
is the correct side of the substrate→archimedean wall and this file stays generic.

No empirical input of any kind enters: there is no CODATA value, no anchor, no `q₀`.
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Algebra.BigOperators.Fin

namespace QOU.Mass.LinkingWeightWedderburn

variable {R : Type*} [Field R]

/-- `h = q - q⁻¹`, the bar-odd deformation parameter. -/
noncomputable def hDef (q : R) : R := q - q⁻¹

/-- `ℏ_q = 1 - q⁻¹`. -/
noncomputable def hbarQ (q : R) : R := 1 - q⁻¹

/-- Quantum dimensions of the five irreducibles of `H_4(q)`, SYMMETRIC convention. -/
noncomputable def dimQ (q : R) : Fin 5 → R
  | 0 => 1                      -- (4)
  | 1 => q^2 + 1 + (q⁻¹)^2      -- (3,1)
  | 2 => q^2 + (q⁻¹)^2          -- (2,2)
  | 3 => q^2 + 1 + (q⁻¹)^2      -- (2,1,1)
  | 4 => 1                      -- (1^4)

/-- Classical dimensions `dim V_λ`. -/
def dimClassical : Fin 5 → ℕ
  | 0 => 1 | 1 => 3 | 2 => 2 | 3 => 3 | 4 => 1

/-- Deformation multiplicity `m_λ` with `dim_q λ = dim V_λ + m_λ h²`. -/
def defMult : Fin 5 → ℕ
  | 0 => 0 | 1 => 1 | 2 => 1 | 3 => 1 | 4 => 0

theorem dimQ_eq_classical_add_defMult_mul_hSq (q : R) (hq : q ≠ 0) (i : Fin 5) :
    dimQ q i = (dimClassical i : R) + (defMult i : R) * hDef q ^ 2 := by
  fin_cases i <;> simp [dimQ, dimClassical, defMult, hDef] <;> field_simp <;> ring

theorem defMult_eq_zero_iff (i : Fin 5) : defMult i = 0 ↔ dimClassical i = 1 := by
  revert i; decide

theorem dimClassical_sum : (∑ i : Fin 5, dimClassical i) = 10 := by decide

theorem defMult_sum : (∑ i : Fin 5, defMult i) = 3 := by decide

theorem card_nontrivial :
    (Finset.univ.filter fun i : Fin 5 => 1 < dimClassical i).card = 3 := by decide

theorem defMult_sum_eq_card_nontrivial :
    (∑ i : Fin 5, defMult i)
      = (Finset.univ.filter fun i : Fin 5 => 1 < dimClassical i).card := by decide

/-- `lw = (1/4) Σ_λ dim_q λ`. -/
noncomputable def lw (q : R) : R := (∑ i : Fin 5, dimQ q i) / 4

theorem lw_eq_closed (q : R) (hq : q ≠ 0) :
    lw q = (10 + 3 * hDef q ^ 2) / 4 := by
  simp only [lw, Fin.sum_univ_five, dimQ, hDef]
  field_simp
  ring

theorem lw_eq_dimSum_add_count (q : R) (hq : q ≠ 0) :
    lw q = (((∑ i : Fin 5, dimClassical i : ℕ) : R)
            + (((Finset.univ.filter fun i : Fin 5 => 1 < dimClassical i).card : ℕ) : R)
              * hDef q ^ 2) / 4 := by
  rw [dimClassical_sum, card_nontrivial, lw_eq_closed q hq]
  norm_num

theorem hDef_factors (q : R) (hq : q ≠ 0) : hDef q = hbarQ q * (q + 1) := by
  simp [hDef, hbarQ]; field_simp; ring

theorem mass_multiplier_split (q : R) (hq : q ≠ 0) (hb : hbarQ q ≠ 0) :
    lw q / hbarQ q ^ 2 = (10 / 4) / hbarQ q ^ 2 + (3 / 4) * (q + 1) ^ 2 := by
  rw [lw_eq_closed q hq, hDef_factors q hq]
  field_simp

theorem lw_bar_even (q : R) (hq : q ≠ 0) : lw q = lw q⁻¹ := by
  rw [lw_eq_closed q hq, lw_eq_closed q⁻¹ (inv_ne_zero hq)]
  simp [hDef]
  field_simp
  ring

end QOU.Mass.LinkingWeightWedderburn
