import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.Ring

/-!
# Q_β residue-A Habiro element: the bar-ODD dual of α_EM

The α_EM next-order factor `H = [2]_q·(1 − h²α)` (`alpha-em-habiro-bar-involution`,
PR #1511) is **bar-EVEN** — a fixed point of the bar involution — with a modular
**zero at ζ₄**. The α_EM block records that the **Q_β analogue** "whose trace
difference is *not* a bar fixed point … required a separate cancellation
analysis", and that it carries a modular **pole at ζ₄** — "the exact structural
dual" of α_EM's zero.

Two independent results this session pin the Q_β residue (the `c_3` source) to
the **bar-ANTIsymmetric** sector:
- PR #1900: the c_k-recursion kernel's leading coefficient `a_1 = −c_3 = √2·Φ₂`
  is bar-odd;
- PR #1907: the on-main `α_eff = (z−1)·h/2` is bar-odd (`h = q − q⁻¹` bar-odd).

## What is (and is NOT) formalised here — the 2-variable picture

Exactly as in the α_EM file, the bar involution is modelled at the **fibre
level** by treating `q` and its inverse `qi` as **independent** ring variables
and taking "bar" to be the **swap** `q ↔ qi` (generic `CommRing`; no reality, no
archimedean evaluation — per AGENTS.md "Im(q) fibre vs observable"). The
genuine `q ↦ q⁻¹` involution, the ζ₄ root of unity, and the literal `q + q⁻¹ = 0`
condition are all recovered **only after specialising `qi = q⁻¹`** (a
group-of-units / field structure). The lemmas below are therefore stated in the
swap picture; the ζ₄/pole reading is the interpretation under that specialisation
and is flagged as such, not proved as a complex-analytic pole (that would need a
localisation / fraction field).

The bar-EVEN generator is `[2]_q = q + qi`; the bar-ODD generator is
`h = q − qi`. The residue **numerator** is `N = h·(1 − h²α)` (bar-odd); the
residue element is `F = N / [2]_q`, singular at the `[2]_q` zero locus.

This is a **structural** statement (parity + zero/non-vanishing at the
bar-antifixed locus). It does NOT claim the full `F`, the archimedean evaluation
`τ(F) = c_3`, or any `c_3` value — those remain the KLR/SW-residue kernel
frontier (`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`).

LaTeX label: `prop:qbeta-residue-habiro-dual`

## References
- α_EM bar-even Habiro element (the dual partner): `alpha-em-habiro-bar-involution` (PR #1511)
- bar-odd kernel parity: PR #1900; bar-odd `α_eff`: PR #1907
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot.QBetaResidueDual

variable {R : Type*} [CommRing R]

/-- bar-EVEN generator `[2]_q = q + qi` (the α_EM prefactor; its zero locus is
the bar-antifixed locus, which is the ζ₄ pole locus of the dual after
specialising `qi = q⁻¹`). -/
def bracketTwo (q qi : R) : R := q + qi

/-- bar-ODD Hecke differential `h = q − qi`. -/
def heckeDiff (q qi : R) : R := q - qi

/-- The Q_β residue-A **numerator** `N = h·(1 − h²α)` — the bar-ODD dual of the
α_EM factor `[2]_q·(1 − h²α)`. The residue element is `F = N / [2]_q` (singular
at the `[2]_q` zero). -/
def residueNum (q qi α : R) : R := heckeDiff q qi * (1 - heckeDiff q qi ^ 2 * α)

/-- **`[2]_q` is bar-EVEN** — invariant under the swap `q ↔ qi`. -/
theorem bracketTwo_bar_even (q qi : R) :
    bracketTwo qi q = bracketTwo q qi := by
  unfold bracketTwo; ring

/-- **`h` is bar-ODD** — flips sign under the swap `q ↔ qi`. -/
theorem heckeDiff_bar_odd (q qi : R) :
    heckeDiff qi q = -(heckeDiff q qi) := by
  unfold heckeDiff; ring

/-- **The Q_β residue numerator is bar-ODD under the swap**:
`N(qi, q, α) = −N(q, qi, α)` (recovering `N(q⁻¹) = −N(q)` after specialising
`qi = q⁻¹`). This is the structural complement of α_EM's
`alphaEmHabiro_bar_invariant` (bar-EVEN, `H(qi,q) = H(q,qi)`): the Q_β residue
lives in the bar-ANTIsymmetric sector (PR #1900, PR #1907), which is exactly why
it required a separate cancellation analysis rather than a Habiro-fixed-point
identification. -/
theorem residueNum_bar_odd (q qi α : R) :
    residueNum qi q α = -(residueNum q qi α) := by
  unfold residueNum heckeDiff; ring

/-- **`[2]_q` vanishes at the bar-antifixed locus `qi = −q`.** After specialising
`qi = q⁻¹` this is the ζ₄ condition `q + q⁻¹ = 0`; since `[2]_q` is a *factor* of
α_EM, the same locus is α_EM's modular **zero**. -/
theorem bracketTwo_zero_at_bar_antifixed (q : R) :
    bracketTwo q (-q) = 0 := by
  unfold bracketTwo; ring

/-- **Evaluation of the residue numerator at the bar-antifixed locus**:
`N(q, −q, α) = 2q·(1 − 4q²·α)`. (A `ring` identity; the non-vanishing and pole
readings are separate — see `residueNum_ne_zero_at_bar_antifixed` and the
docstring's pole caveat.) -/
theorem residueNum_at_bar_antifixed (q α : R) :
    residueNum q (-q) α = (2 * q) * (1 - (2 * q) ^ 2 * α) := by
  unfold residueNum heckeDiff; ring

/-- **The residue numerator is genuinely NON-zero at the bar-antifixed locus**,
under explicit non-vanishing hypotheses on its two factors (stated over a domain
so `mul_ne_zero` applies). Combined with `bracketTwo_zero_at_bar_antifixed`
(`[2]_q = 0` there), this is the rigorous content of "`F = N/[2]_q` has a pole":
the denominator vanishes while the numerator does not — a genuine singularity in
any localisation inverting `[2]_q`. (We do not formalise the pole as a fraction-
field object; this `≠ 0` + `= 0` pair is the CommRing-level statement.) -/
theorem residueNum_ne_zero_at_bar_antifixed {R : Type*} [CommRing R] [IsDomain R]
    (q α : R) (h2q : (2 * q) ≠ 0) (hfac : (1 - (2 * q) ^ 2 * α) ≠ 0) :
    residueNum q (-q) α ≠ 0 := by
  rw [residueNum_at_bar_antifixed]
  exact mul_ne_zero h2q hfac

/-- **Zero/non-vanishing duality at the bar-antifixed locus, packaged.** At
`qi = −q`: the α_EM factor `[2]_q` is zero, while the Q_β residue numerator `N`
equals `2q(1 − 4q²α)` (non-zero under `residueNum_ne_zero_at_bar_antifixed`'s
hypotheses). So `[2]_q`'s vanishing is α_EM's **zero** in the bar-even sector and
the **pole** of `F = N/[2]_q` in the bar-odd sector — two faces of the same
factor. (Equalities only; non-vanishing/pole are the separate lemma + caveat.) -/
theorem residue_vs_alphaEm_at_bar_antifixed (q α : R) :
    bracketTwo q (-q) = 0 ∧
      residueNum q (-q) α = (2 * q) * (1 - (2 * q) ^ 2 * α) :=
  ⟨bracketTwo_zero_at_bar_antifixed q, residueNum_at_bar_antifixed q α⟩

end QOU.BraidKnot.QBetaResidueDual
