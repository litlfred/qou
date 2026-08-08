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

/-! ## The integer-index sibling

Six definitions in the corpus carry a **ℤ** index with a byte-identical body,
under five different names: `qNumberSym` (twice), `qIntZ`, `qIntSym`, `qInt`,
`qBracket`.  They are not a separate convention — `qIntBalZ_natCast` below shows
the ℤ form *restricts* to `qIntBal` on ℕ.  What the ℤ index buys is the one
structural fact ℕ cannot state: the q-integer is **odd in its index**
(`qIntBalZ_neg`), which is what makes `[k−3]_q`-style shifted indices
(`volume_perturbation`) and negative `sl₂` weights expressible at all. -/

section IntegerIndex

variable {R : Type*} [Field R]

/-- **The canonical quantum integer at integer index**,
`[k]_q = (q^k − q^{−k})/(q − q⁻¹)` for `k : ℤ`.

Restricts to `qIntBal` on `ℕ` (`qIntBalZ_natCast`), so this is one object with
`qIntBal`, not a third convention.  Use it when the index is genuinely signed —
a shifted Hecke level `[k−3]_q`, or a weight running over `n−1, n−3, …, −(n−1)`. -/
noncomputable def qIntBalZ (q : R) (k : ℤ) : R :=
  (q ^ k - q ^ (-k)) / (q - q⁻¹)

/-- Defining equation, exposed for the same `simp`-after-migration reason as
`qIntBal_def`. -/
@[simp] theorem qIntBalZ_def (q : R) (k : ℤ) :
    qIntBalZ q k = (q ^ k - q ^ (-k)) / (q - q⁻¹) := rfl

/-- **The compatibility theorem**: the ℤ form restricts to the ℕ form.

This is what makes `qIntBalZ` an *extension* of `qIntBal` rather than a rival
definition, and it is the lemma a migration needs when a ℤ-indexed site meets an
ℕ-indexed lemma. -/
@[simp] theorem qIntBalZ_natCast (q : R) (n : ℕ) :
    qIntBalZ q (n : ℤ) = qIntBal q n := by
  simp [qIntBalZ, qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, zpow_neg, inv_pow]

/-- **Oddness in the index** — the fact the ℕ index cannot state, and the reason
this sibling exists. -/
theorem qIntBalZ_neg (q : R) (k : ℤ) : qIntBalZ q (-k) = -qIntBalZ q k := by
  simp only [qIntBalZ, neg_neg]
  rw [← neg_div, neg_sub]

@[simp] theorem qIntBalZ_zero (q : R) : qIntBalZ q 0 = 0 := by
  simp [qIntBalZ]

/-- **The ℤ form is bar-even too** — the defining property survives the
extension, so a signed index does not break the bar-parity bookkeeping. -/
theorem qIntBalZ_bar_even (q : R) (k : ℤ) : qIntBalZ q⁻¹ k = qIntBalZ q k := by
  simp only [qIntBalZ, inv_zpow, inv_inv, ← zpow_neg, neg_neg]
  rw [← neg_div_neg_eq, neg_sub, neg_sub]

end IntegerIndex

/-! ## The classical-extended (guarded) forms — policy

Eight further definitions guard the singularity, `if q = 1 then n else …`.  They
were previously lumped together as one bucket; they are **two**, because the
guard is orthogonal to the convention: three are guarded-*balanced*
(`H3HeckeIdempotents`, `ZeqNRhoCorrection`, `FeynmanPathIntegrals`) and three are
guarded-*geometric* (`jacksonInt` in two chapters, `quantum-dilogarithm`,
`TopologicalMass`).

**The policy is: keep the guard, but define it through the unguarded form.**  A
guarded definition really is a different function — Lean's `x / 0 = 0` makes the
unguarded form take value `0` at `q = 1`, whereas the guarded one takes the
removable-singularity value `n`.  So a blanket guarded → unguarded sweep would
silently change behaviour at `q = 1`, exactly the way a blanket geometric →
balanced sweep would.  But that difference is confined to a single point, and
stating it as a *theorem* (`qIntBalCl_of_ne_one`) rather than a comment is what
lets a site migrate and keep its `q = 1` case.

The substrate sits at `q₀ ≈ 1.11 ≠ 1`, so production evaluation never sees the
guard; it exists for the classical limit `q → 1`, which several sites take
deliberately (`q-casimir-classical-limit`, `Hoefsmit.qBracket_at_one`).

**Known gap, deliberately not papered over.** The *balanced* form is singular at
`q = −1` as well (`q − q⁻¹ = 0` there too), and the three guarded-balanced sites
guard only `q = 1`.  `QOU.IwahoriHecke.Hoefsmit.qBracket` is the one definition
that guards both.  `qIntBalCl` below reproduces the corpus's prevailing
one-sided guard rather than silently changing three call sites' behaviour at
`q = −1`; the two-sided variant is left to whoever needs `q = −1`. -/

section ClassicalExtended

variable {R : Type*} [Field R]

open scoped Classical in
/-- **Classical-extended balanced q-integer**: `qIntBal` away from `q = 1`, and
its removable-singularity value `n` at `q = 1`. -/
noncomputable def qIntBalCl (q : R) (n : ℕ) : R :=
  if q = 1 then (n : R) else qIntBal q n

open scoped Classical in
/-- **Classical-extended geometric q-integer** (the Jackson bracket): `qIntGeo`
away from `q = 1`, and `n` at `q = 1`. -/
noncomputable def qIntGeoCl (q : R) (n : ℕ) : R :=
  if q = 1 then (n : R) else qIntGeo q n

@[simp] theorem qIntBalCl_one (n : ℕ) : qIntBalCl (1 : R) n = (n : R) := by
  simp [qIntBalCl]

@[simp] theorem qIntGeoCl_one (n : ℕ) : qIntGeoCl (1 : R) n = (n : R) := by
  simp [qIntGeoCl]

/-- **Away from the singularity the guard is invisible** — the bridge a guarded
site needs in order to reuse any unguarded `qIntBal` lemma. -/
theorem qIntBalCl_of_ne_one {q : R} (h : q ≠ 1) (n : ℕ) :
    qIntBalCl q n = qIntBal q n := by
  simp [qIntBalCl, h]

theorem qIntGeoCl_of_ne_one {q : R} (h : q ≠ 1) (n : ℕ) :
    qIntGeoCl q n = qIntGeo q n := by
  simp [qIntGeoCl, h]

/-- The guard is not cosmetic: at `q = 1` the unguarded balanced form evaluates
to `0` (Lean's `x / 0 = 0`), not to `n`.  This is the lemma that makes
"guarded → unguarded is a behaviour change" checkable rather than asserted. -/
theorem qIntBal_one_eq_zero (n : ℕ) : qIntBal (1 : R) n = 0 := by
  simp [qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal]

/-- **Closed form of the guarded geometric bracket.**

`qIntGeo` is the `Finset.sum`, but every guarded-geometric site in the corpus
writes the closed form `(qⁿ − 1)/(q − 1)`.  Migrating such a site onto
`qIntGeoCl` therefore replaces the body by a *propositionally* — not
definitionally — equal one, and a clean compile does **not** by itself witness
that: it only shows nothing downstream constrained the body.  This lemma is the
missing witness, so the substitution is checked rather than assumed. -/
theorem qIntGeoCl_eq_closed_form {q : R} (h : q ≠ 1) (n : ℕ) :
    qIntGeoCl q n = (q ^ n - 1) / (q - 1) := by
  rw [qIntGeoCl_of_ne_one h, qIntGeo_def, geom_sum_eq h]

end ClassicalExtended

end QOU.QInteger
