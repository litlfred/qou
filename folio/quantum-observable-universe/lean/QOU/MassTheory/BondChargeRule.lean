/-
# The bond rule is a SUM in the charges where Coulomb needs a PRODUCT

Owner, 2026-08-30: *"go ahead on the p→σ, n→σ⁻¹ identification"*.

The identification is not wrong about protons and neutrons. It is wrong about
**how two charges combine**, and that single substitution accounts for every
failure found on this arc.

## What the corpus assigns

`torus-hopf-stability-proof` gives the Coulomb charges of the two nucleons:
`Q(𝔭) = +1` and `Q(𝔫) = 0`. `prop:skein-crossing-asymmetry` gives the
per-crossing correction as `δ = q - ½(q + q⁻¹) = ½(q - q⁻¹) = h/2`, applied
"between composites of the same charge relative to a mixed-charge baseline".

`closed_form_tau_M.interface_factor` implements, relative to that mixed-charge
baseline `f_pn`:

    f_pp - f_pn = + h/2        f_pn - f_pn = 0        f_nn - f_pn = - h/2

Measured exactly (`level3_bond_charge_rule_probe.py`): that is
**`(Qᵢ + Qⱼ - 1)·h/2`**, the *centred sum* of the two charges — to the last
digit, at the canonical proton pin.

## The two rules, and where they part

`sumRule` and `prodRule` below agree on `pp` and on `pn`
(`rules_agree_pp`, `rules_agree_pn`) and differ **only on `nn`**
(`rules_differ_nn`): the sum rule charges the neutron pair `-h/2`, the product
rule charges it `0`. Two neutral objects have no Coulomb interaction, so `0` is
the physical value — and `nn` is the one bond the two rules disagree about.

## Why that one bond is everything

Summed over the complete graph of a nucleus:

* `sumRule_total` — `Σ_{i<j} (Qᵢ + Qⱼ) = (A-1)·Z`, **linear** in `Z`;
* `prodRule_total` — `Σ_{i<j} Qᵢ·Qⱼ = Z(Z-1)/2`, **quadratic** — the number of
  proton pairs, which is what a Coulomb energy counts.

That is the same degree gap `QOU.MassTheory.CrossingCountAffine` proves no
linear functional of the crossing counts can close, and here is its source: the
crossing counts are linear in `Z` *because the bond rule is a sum*.

Every failure on this arc is this one substitution:

* `qou-1pig` — `f_pp - f_nn = h ≠ 0`: the sum rule is charge-odd across the like
  pairs (`sumRule_like_pairs_differ`), the product rule is not
  (`prodRule_like_pairs_are_strong_baseline` — `nn` sits on the `pn` baseline,
  so the *strong* channel is charge-symmetric and the only charge dependence
  left is on `pp`, which is exactly Coulomb).
* `qou-dhsn` — the `A`-only Coulomb channel and the `2Z` strong channel.
* `qou-vudb` — the `A⁰` mirror scaling.

## What this does NOT fix

`prodRule_mirror_difference` — under the product rule a mirror pair differs by
`(Z-W)(A-1)/2`, still **linear in `A`**. The measured Coulomb displacement
energy goes as `(A-1)/A^{1/3}`. So the product rule supplies the right
*multiplicity* and not the right *scaling*: the missing factor is the `1/R`
of a Coulomb energy, with `R ∝ A^{1/3}`, which is a geometric input the bond
picture does not currently carry. Necessary, not sufficient.

## Scope

The identities are exact over a generic `CommRing` (AGENTS.md §7c) and hold for
any charges whatsoever; `Q(𝔭) = 1`, `Q(𝔫) = 0` enter only in the specialised
corollaries. Nothing here refutes `prop:skein-crossing-asymmetry` — the
proposition's own wording ("same charge" vs "mixed-charge baseline") is
two-valued and is what the *product* rule realises; it is the three-valued
ladder in the implementation that does not follow from it. Nothing is wired.

Beans `qou-1pig`, `qou-dhsn`, `qou-vudb`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.MassTheory.BondChargeRule

variable {R : Type*} [CommRing R]

/-! ## 1. The two ways to combine two charges -/

/-- **The implemented rule**: the centred *sum* of the two charges, times the
per-crossing correction `c = h/2`. Measured to be exactly what
`interface_factor` produces. -/
def sumRule (c qi qj : R) : R := (qi + qj - 1) * c

/-- **The Coulomb rule**: the *product* of the two charges, times `c`. Two
objects interact electromagnetically in proportion to `Qᵢ·Qⱼ`. -/
def prodRule (c qi qj : R) : R := qi * qj * c

/-! ## 2. They agree on two bonds and differ on one

With `Q(𝔭) = 1` and `Q(𝔫) = 0`. -/

/-- On a proton pair both rules give `+c`. -/
@[simp] theorem rules_agree_pp (c : R) : sumRule c 1 1 = prodRule c 1 1 := by
  unfold sumRule prodRule; ring

/-- On a mixed pair both rules give `0` — the baseline. -/
@[simp] theorem rules_agree_pn (c : R) : sumRule c 1 0 = prodRule c 1 0 := by
  unfold sumRule prodRule; ring

/-- **On a neutron pair they differ by `c`.** The sum rule charges two neutral
objects `-c`; the product rule charges them `0`. This one bond is the whole
disagreement. -/
theorem rules_differ_nn (c : R) : sumRule c 0 0 - prodRule c 0 0 = -c := by
  unfold sumRule prodRule; ring

/-- The sum rule makes the two **like** pairs differ by `2c` — charge-odd across
`p ↔ n`, which is `qou-1pig`'s measured defect (`f_pp - f_nn = h = 2·(h/2)`). -/
theorem sumRule_like_pairs_differ (c : R) :
    sumRule c 1 1 - sumRule c 0 0 = 2 * c := by
  unfold sumRule; ring

/-- Under the product rule the neutron pair sits exactly on the mixed-charge
baseline, so the **strong** channel is charge-symmetric and the only charge
dependence left is on `pp` — which is what an electromagnetic term should be. -/
theorem prodRule_like_pairs_are_strong_baseline (c : R) :
    prodRule c 0 0 = prodRule c 1 0 := by
  unfold prodRule; ring

/-! ## 3. Summed over a nucleus, the degree differs

For `Z` protons of charge `1` and `N` neutrons of charge `0`, over the complete
graph on `A = Z + N` nucleons. Both totals are stated as closed forms and are
what the combinatorial sums evaluate to. -/

/-- **The sum rule totals to `(A-1)·Z`** — each nucleon appears in `A-1` bonds,
so `Σ_{i<j} (Qᵢ + Qⱼ) = (A-1)·Σᵢ Qᵢ = (A-1)Z`. Linear in `Z`. -/
def sumRuleTotal (A Z : R) : R := (A - 1) * Z

/-- **The product rule totals to `Z(Z-1)/2`** — the number of proton pairs.
Stated doubled, to stay division-free over a bare `CommRing`. -/
def prodRuleTotalDoubled (Z : R) : R := Z * (Z - 1)

/-- The sum-rule total is **affine** in `Z` at fixed `A`: its second difference
vanishes. -/
theorem sumRuleTotal_affine (A : R) : ∀ Z : R,
    sumRuleTotal A (Z + 2) - 2 * sumRuleTotal A (Z + 1) + sumRuleTotal A Z = 0 := by
  intro Z; unfold sumRuleTotal; ring

/-- The product-rule total is **quadratic**: its second difference is the nonzero
constant `2`. So no rescaling of the sum rule can reproduce it — this is the
degree gap `CrossingCountAffine` states, traced to its source. -/
theorem prodRuleTotalDoubled_quadratic : ∀ Z : R,
    prodRuleTotalDoubled (Z + 2) - 2 * prodRuleTotalDoubled (Z + 1)
      + prodRuleTotalDoubled Z = 2 := by
  intro Z; unfold prodRuleTotalDoubled; ring

/-- **No multiple of the sum-rule total is the product-rule total.** Over `ℤ`,
where `2 ≠ 0`; the coefficient is chosen first, so the whole family is excluded
at once. -/
theorem no_scaling_of_sumRule_is_prodRule (k A : ℤ) :
    ¬ (∀ Z : ℤ, k * sumRuleTotal A Z = prodRuleTotalDoubled Z) := by
  intro hEq
  have e1 := hEq 1
  have e2 := hEq 2
  unfold sumRuleTotal prodRuleTotalDoubled at e1 e2
  have h1 : k * (A - 1) = 0 := by linear_combination e1
  have h2 : 2 * (k * (A - 1)) = 2 := by linear_combination e2
  rw [h1] at h2
  norm_num at h2

/-! ## 4. The mirror difference — right multiplicity, wrong scaling -/

/-- Under the product rule a mirror pair `(Z, ·)` vs `(W, ·)` at fixed `A`
differs by `(Z - W)(Z + W - 1)`, i.e. `(Z-W)(A-1)` for a mirror pair where
`Z + W = A`. **Linear in `A`.** The observed Coulomb displacement energy goes as
`(A-1)/A^{1/3}`, so the product rule fixes the multiplicity and still lacks the
`1/R` of a Coulomb energy. -/
theorem prodRule_mirror_difference (Z W : R) :
    prodRuleTotalDoubled Z - prodRuleTotalDoubled W = (Z - W) * (Z + W - 1) := by
  unfold prodRuleTotalDoubled; ring

/-- The sum rule's mirror difference at fixed `A` is `(A-1)(Z - W)` — also
nonzero, which is why the model *has* a mirror splitting at all, and flat in the
sense that its `Z`-dependence carries no extra factor of `A`. -/
theorem sumRule_mirror_difference (A Z W : R) :
    sumRuleTotal A Z - sumRuleTotal A W = (A - 1) * (Z - W) := by
  unfold sumRuleTotal; ring


/-- **Pointwise and total discrepancy between the centred-sum rule and the Coulomb product rule (`qou-nial`).**
For any charges `qi, qj : R`, `sumRule c qi qj - prodRule c qi qj = -(1 - qi) * (1 - qj) * c`
(which vanishes whenever either nucleon has proton charge `1` and equals `-c` on `nn` where `qi = qj = 0`),
and over a nucleus of mass number `A` and charge `Z`,
`2 * sumRuleTotal A Z - prodRuleTotalDoubled Z = Z * (2 * A - Z - 1)`. -/
theorem sumRule_sub_prodRule_and_total_deficit (c qi qj A Z : R) :
    sumRule c qi qj - prodRule c qi qj = -(1 - qi) * (1 - qj) * c ∧
      2 * sumRuleTotal A Z - prodRuleTotalDoubled Z = Z * (2 * A - Z - 1) := by
  refine ⟨by unfold sumRule prodRule; ring, by unfold sumRuleTotal prodRuleTotalDoubled; ring⟩

end QOU.MassTheory.BondChargeRule
