/-
  # The canonical q-integer — one home, two explicitly-named conventions

  **Use this module.  Do not define another `qInt`.**

  A census on 2026-08-08 found **55** q-integer definitions across the corpus
  under ~15 aliases (`qInt`, `qIntBal`, `qIntPoly`, `qIntReal`, `qIntSym`,
  `qIntZ`, `qInt2`, `qInt3`, `qBracket`, `qBracket2`, `qNum`, `qNumber`,
  `qNumberSym`, `qInteger`, `qIntegerRescaled`) — 43 balanced, 10 geometric,
  1 geometric-in-`q²`, 1 ℤ-polynomial.  The *convention* was never really in
  dispute: 43 of 55 are already balanced.  The problem is that the **bare name
  `qInt` is defined locally in 18 files and means BOTH conventions**, so reading
  a call site tells you nothing.

  This module fixes that by giving each convention a name that says which it is,
  and by collecting the bridge theorems in one place.

  ## Which one do I want?

  **`qIntBal` — the canonical `[n]_q`.**  Use this unless you have a specific
  reason not to.  It is forced, not chosen, by three independent routes:

  * **bar parity** — `[n]_{q⁻¹} = [n]_q`, so it is compatible with the corpus's
    bar-even / bar-odd channel decomposition.  The geometric form is *not*
    bar-even (it transforms with weight `−(n−1)`), so a geometric `[n]` inside a
    bar-even quantity breaks the parity bookkeeping silently.
    (`QOU.Mass.QIntegerBarParity`.)
  * **the Hecke relation** — AGENTS.md §7a adopts `(σ−q)(σ+q⁻¹) = 0`, whose
    structure constant is `q − q⁻¹`, the balanced denominator.
  * **the quantum dimension** — it is the sum over the *symmetric* `sl₂` weight
    string `n−1, n−3, …, −(n−1)`.

  **`qIntGeo` — the geometric form, `∑_{i<n} q^i`.**  Legitimate in exactly one
  situation: **when your variable means `q²`.**  By `qIntBal_eq_twist`,

      qIntBal q n = q⁻¹^(n−1) · qIntGeo (q²) n

  so geometric-in-`Q` and balanced-in-`q` agree precisely when `Q = q²`.  A live
  example is `QOU.Interactions.HeckeEnergyPositivity.qIntegerRescaled`
  (`∑_{j<k} q^{2j}`), which is geometric, correct, and named for it.

  **This is why a blanket geometric → balanced sweep is a bug, not a cleanup.**
  Converting a `q²` site would introduce an error where none existed.

  ## Migration

  Both names below are `abbrev`s onto the already-proved definitions in
  `QOU.Mass.QHookDimension{,Balanced}` — *no new definition is introduced*, so
  every existing lemma about `qIntBal` / `qIntPoly` applies unchanged and
  `simp`/`unfold` see through them.  To migrate a file: delete its local
  `def qInt …`, import this module, and use `qIntBal` or `qIntGeo` by the rule
  above.

  -- Ref: [manuscript] docs/audits/2026-08-08-q-integer-convention-derived.md
  -- Ref: [manuscript] AGENTS.md §7a (Hecke–Skein convention)
-/

import QOU.Mass.QHookDimension
import QOU.Mass.QHookDimensionBalanced
import QOU.Mass.QIntegerBarParity

namespace QOU.QInteger

/-- **The canonical quantum integer** `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`.

Bar-even, the `U_q(sl₂)` quantum dimension, and the form matching AGENTS.md §7a's
Hecke normalisation.  Use this unless your variable means `q²` — see `qIntGeo`. -/
noncomputable abbrev qIntBal {R : Type*} [Field R] (q : R) (n : ℕ) : R :=
  QOU.Mass.QHookDimensionBalanced.qIntBal q n

/-- **The geometric quantum integer** `∑_{i<n} qⁱ = (qⁿ − 1)/(q − 1)`.

Correct **only where the variable means `q²`** (see `qIntBal_eq_twist_canonical`).
It is *not* bar-even, so it must not carry a bar-even quantity. -/
abbrev qIntGeo {R : Type*} [CommRing R] (q : R) (n : ℕ) : R :=
  QOU.Mass.QHookDimension.qIntPoly q n

/-- **Defining equation**, exposed as `simp`/`rw` fodder.

Consolidating a local duplicate onto `qIntBal` otherwise breaks every downstream
proof that did `unfold <local>` — the unfold now stops at the alias.  With this
lemma `simp [<local>]` reaches the formula again, so a migration needs no edits
to existing proofs. -/
@[simp] theorem qIntBal_def {R : Type*} [Field R] (q : R) (n : ℕ) :
    qIntBal q n = (q ^ n - q⁻¹ ^ n) / (q - q⁻¹) := rfl

/-- Defining equation for the geometric form, same purpose. -/
@[simp] theorem qIntGeo_def {R : Type*} [CommRing R] (q : R) (n : ℕ) :
    qIntGeo q n = ∑ i ∈ Finset.range n, q ^ i := rfl

section Bridge

variable {R : Type*} [Field R]

/-- **The twist**: the two conventions are one object, related by `q ↦ q²` and a
monomial.  Restated here so the bridge is visible from the canonical module. -/
theorem qIntBal_eq_twist_canonical (q : R) (n : ℕ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qIntBal q n = q⁻¹ ^ (n - 1) * qIntGeo (q ^ 2) n :=
  QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist q n hq hq2

/-- **The canonical form is bar-even** — the property that forces it. -/
theorem qIntBal_bar_even_canonical (q : R) (n : ℕ) :
    qIntBal q⁻¹ n = qIntBal q n :=
  QOU.Mass.QIntegerBarParity.qIntBal_bar_even q n

/-- **The geometric form is bar-COVARIANT, not invariant** — weight `−(n−1)`.
This is the separating fact: it is why a geometric `[n]` cannot carry a bar-even
quantity. -/
theorem qIntGeo_bar_covariant (q : R) (n : ℕ) (hq : q ≠ 0) :
    qIntGeo q⁻¹ n = q⁻¹ ^ (n - 1) * qIntGeo q n :=
  QOU.Mass.QIntegerBarParity.qIntPoly_bar_covariant q n hq

end Bridge

end QOU.QInteger
