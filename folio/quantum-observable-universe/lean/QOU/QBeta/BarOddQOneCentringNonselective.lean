import Mathlib.Tactic
import Mathlib.Algebra.Group.Invertible.Basic
import QOU.QBeta.FiveTwoDTSpectrumSplit

/-!
# QOU.QBeta.BarOddQOneCentringNonselective — "centred at q=1" selects no fibre element

**Formalize-first honest negative for the fibre-level survivor of the owner's
saddle-vector picture (`qou-q86o`).**

After the sibling gates:

* `IotaOddSaddleOffsetAmphichiral` (#4577) — the certified saddle offset
  `o = c⁺ − c⁻` vanishes iff the knot is (ι-fixed) *amphichiral*, modelling the
  **chirality** swap `(a,b) ↦ (b,a)` as the involution;
* `SaddleOffsetBarGrade` (#4583) — that certified offset is **not** a
  `q ↔ q⁻¹` bar-odd Laurent object (its `q→0` constant coefficient is the
  certified datum `chiralityOdd 4 3 = 1 ≠ 0`, whereas a genuinely `q↔q⁻¹`-odd
  object has zero constant coefficient),

the picture is **refuted as an archimedean / DT claim** but is said to *survive*
at the **fibre level**: a Habiro-ring / cyclotomic-completion element `F(q)`
whose `q ↔ q⁻¹` bar-odd part has forced-zero **bar-fixed coefficient degree**
(`n = 0` / constant term — the fibre reading of "centred at `q = 1`"; evaluation
at the involution's fixed points `q = ±1` is a distinct statement) **by
construction**, whose root-of-unity / substrate evaluations would reproduce the
certified `{3,4}` / DT data.

This file states, sorry-free, the **structural reason there is no DERIVED such
element — only a vacuous-or-fit dichotomy.**  The `q ↔ q⁻¹` involution acts on a
Laurent-coefficient sequence `g : ℤ → R` by `n ↦ -n`; its *only* fixed degree is
`n = 0` (the `q→0` / semiclassical datum).  Consequently:

* **Vacuous horn.**  "vanishes at the bar-fixed degree" is **implied by**
  bar-oddness for the *entire* class (`q1_centring_nonselective`): adding the
  "centred at `q=1`" constraint to bar-oddness selects **no** element, so it
  cannot single out *the knot's* saddle vector — the centring is content-free.
  And the fixed datum does not even pin the element
  (`centring_underdetermined`): distinct bar-odd sequences share it.
* **Fit horn.**  The certified `{3,4}` DT datum is `chiralityOdd 4 3 = 1 ≠ 0`,
  which **cannot** be the bar-fixed-degree coefficient of any bar-odd object
  (`certified_datum_not_barOdd_fixedDegree`) — so recovering it must come from
  the *non-fixed* degrees (root-of-unity evaluations), which bar-oddness leaves
  **free**.  That freedom is the Habiro-ring flexibility the anti-fit discipline
  forbids passing off as a derivation.

Neither horn is a derivation: a bar-odd element realising *only* `q=1` centring
is content-free (vacuous horn); one additionally reproducing the `{3,4}` datum
is a fit (fit horn).  See the audit doc for the four-pillar synthesis (this file
is pillar 1; #4583, `HabiroMagnitudeA3` substrate-wall, and the q-exact
`StokesSymmetryConstant` no-resurgent-tail keystone are pillars 2–4).

## What is proved (non-vacuous, sorry-free, falsifiable)

* `barAntisym_fixedDegree_zero` — generic `{R}[CommRing][Invertible 2]`: a
  `q↔q⁻¹`-odd object has zero coefficient at the *only* bar-fixed degree `n=0`
  (the mechanism the `q=1` centring rides on).  `_int` variant over `ℤ`.
* `barInvolution_fixedDegree_iff` — the coefficient action `n ↦ -n` fixes `n`
  iff `n = 0`: `q=1`-centring lives at a **single** degree.
* `q1_centring_nonselective` — **non-selectivity**: `BarAntisym g` is *equivalent*
  to `BarAntisym g ∧ g 0 = 0`.  The centring constraint adds nothing.
* `centring_underdetermined` — the fixed datum does not determine the element:
  two distinct bar-odd sequences share `g 0 = 0`.
* `certified_datum_not_barOdd_fixedDegree` — **headline**: no bar-odd object has
  bar-fixed-degree coefficient equal to the certified `{3,4}` datum
  `chiralityOdd (Splus0 0 1) (Sminus0 0 2) = 1`.

## Discipline

§7c: generic `{R}` theory, concrete grounding over `ℤ` (no archimedean
construct — no `Real.*`, no `q₀`, no ordering).  No `sorry`, no `True := trivial`,
no `native_decide`, no axiom substituting for a proof.  Scope-(a): a structural
*narrowing* (the centring is non-selective; the DT datum is not a bar-odd
fixed-degree coefficient) — invokes no proved invariant to exclude an ingredient,
derives no physical number, wires no `c_k`, inverts no `Q_β`/CODATA, adds nothing
to any dashboard.  Standalone library file (like its dependency
`FiveTwoDTSpectrumSplit`), verified `lean`-direct; **not** added to the `QBeta`
aggregator.

-- Ref: [leitner2026] docs/audits/2026-08-02-fibre-habiro-q1-centring-verdict.md
-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (5₂ DT spectrum, eqs 96/97/98)
-/

namespace QOU.QBeta.BarOddQOneCentringNonselective

open QOU.QBeta.FiveTwoDTSpectrumSplit

/-- A Laurent-coefficient sequence `g : ℤ → R` is **q↔q⁻¹-antisymmetric**
(bar-odd in the modulus): the bar involution `q ↦ q⁻¹`, acting on coefficients by
`n ↦ -n`, negates it. -/
def BarAntisym {R : Type*} [Neg R] (g : ℤ → R) : Prop := ∀ n : ℤ, g (-n) = - g n

/-! ## The bar involution fixes a single coefficient degree -/

/-- The coefficient action `n ↦ -n` of the bar involution `q ↦ q⁻¹` fixes `n`
**iff** `n = 0`.  The "centred at `q = 1`" datum therefore lives at a *single*
degree — the `q → 0` / semiclassical one. -/
theorem barInvolution_fixedDegree_iff (n : ℤ) : (-n = n) ↔ (n = 0) := by
  omega

/-! ## The bar-fixed-degree vanishing (the mechanism the centring rides on) -/

/-- **Bar-fixed-degree vanishing (generic).**  A `q↔q⁻¹`-odd Laurent object has
zero coefficient at the unique bar-fixed degree `n = 0` (its constant term).
This is the coefficient-level mechanism the centring rides on: the bar involution
acts on degrees by `n ↦ -n`, whose only fixed degree is `n = 0`, so bar-oddness
forces the constant term to zero.  (Evaluation of the Laurent object at the
involution's fixed points `q = ±1` is a *distinct* statement — not what is
proved here — so the docstring claims only the `n = 0` coefficient fact.) -/
theorem barAntisym_fixedDegree_zero {R : Type*} [CommRing R] [Invertible (2 : R)]
    {g : ℤ → R} (h : BarAntisym g) : g 0 = 0 := by
  have h0 : g 0 = - g 0 := by simpa using h 0
  have h2 : (2 : R) * g 0 = 0 := by linear_combination h0
  calc
    g 0 = ⅟(2 : R) * ((2 : R) * g 0) := by rw [← mul_assoc, invOf_mul_self, one_mul]
    _ = ⅟(2 : R) * 0 := by rw [h2]
    _ = 0 := mul_zero _

/-- **Bar-fixed-degree vanishing over `ℤ`** (a domain — no `Invertible 2`). -/
theorem barAntisym_fixedDegree_zero_int {g : ℤ → ℤ} (h : BarAntisym g) : g 0 = 0 := by
  have h0 : g 0 = - g 0 := by simpa using h 0
  omega

/-! ## Non-selectivity: "centred at q=1" adds nothing to bar-oddness -/

/-- **The centring is non-selective.**  For any bar-odd `g`, the constraint
"vanishes at the bar-fixed degree" (`g 0 = 0`, the `q = 1` centring) is *already
implied* — so `BarAntisym g` and `BarAntisym g ∧ g 0 = 0` are **equivalent**.
Imposing the owner's "origin-centred at `q = 1`" on a bar-odd fibre element
selects **no** element: the property is content-free, hence cannot pick out
*the knot's* saddle vector. -/
theorem q1_centring_nonselective {R : Type*} [CommRing R] [Invertible (2 : R)]
    (g : ℤ → R) : BarAntisym g ↔ (BarAntisym g ∧ g 0 = 0) := by
  constructor
  · intro h; exact ⟨h, barAntisym_fixedDegree_zero h⟩
  · intro h; exact h.1

/-- **Under-determination.**  The bar-fixed datum does not pin the element: two
**distinct** bar-odd sequences (`n ↦ n` and `n ↦ 2n`) share the same bar-fixed
coefficient `g 0 = 0`.  A fortiori the centring cannot determine *the* saddle
vector; the discriminating content must come from the non-fixed (root-of-unity)
degrees, which bar-oddness leaves free. -/
theorem centring_underdetermined :
    ∃ g₁ g₂ : ℤ → ℤ, BarAntisym g₁ ∧ BarAntisym g₂ ∧ g₁ 0 = g₂ 0 ∧ g₁ ≠ g₂ := by
  refine ⟨(fun n => n), (fun n => 2 * n), ?_, ?_, ?_, ?_⟩
  · intro n; rfl
  · intro n; show (2 : ℤ) * (-n) = -(2 * n); ring
  · norm_num
  · intro h
    have h1 : (1 : ℤ) = 2 * 1 := congrFun h 1
    omega

/-! ## Anti-vacuity: genuinely bar-odd objects exist -/

/-- **Anti-vacuity.**  A genuinely `q↔q⁻¹`-odd object exists (`g n = n`) and *does*
have zero bar-fixed coefficient, so the hypotheses above are satisfiable and the
non-selectivity is a real distinction, not a vacuous one. -/
theorem barAntisym_nontrivial : BarAntisym (fun n : ℤ => n) ∧ (fun n : ℤ => n) 0 = 0 :=
  ⟨fun _ => rfl, rfl⟩

/-! ## The fit horn: the certified {3,4} DT datum is not a bar-odd fixed coefficient -/

/-- The certified `q → 0` DT datum of the 5₂ saddle offset: the merged
distinguisher's ι-odd value `chiralityOdd 4 3 = 1` (reused, not a fresh number). -/
def dtDatum : ℤ := chiralityOdd (Splus0 0 1) (Sminus0 0 2)

@[simp] theorem dtDatum_eq_one : dtDatum = 1 := by
  unfold dtDatum; exact chirality_odd_datum_eq_one

/-- **Headline (fit horn).**  No bar-odd Laurent object has bar-fixed-degree
coefficient equal to the certified `{3,4}` DT datum.  Hence reproducing that
datum from a bar-odd fibre element cannot come from the (forced) bar-fixed
degree — it must come from the non-fixed root-of-unity degrees, which
bar-oddness leaves free (the Habiro flexibility a derivation may not exploit). -/
theorem certified_datum_not_barOdd_fixedDegree
    (g : ℤ → ℤ) (hbar : BarAntisym g) : g 0 ≠ dtDatum := by
  rw [barAntisym_fixedDegree_zero_int hbar, dtDatum_eq_one]
  exact zero_ne_one

end QOU.QBeta.BarOddQOneCentringNonselective
