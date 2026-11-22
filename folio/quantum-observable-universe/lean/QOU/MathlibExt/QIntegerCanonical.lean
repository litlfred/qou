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

  ## Census status (`qou-qint`)

  Of the 55 q-integer declarations, **48 are now tied to this module** by an
  alias or a proved equation, and the remaining 7 are accounted for rather than
  outstanding:

  | # | disposition |
  |---|---|
  | 3 | the canonical definitions themselves (`QHookDimension{,Balanced}`) |
  | 2 | continuous index — no equation exists (below) |
  | 2 | `StokesConstantQDimCategoricity`'s deliberate `Polynomial ℤ` pair |

  The census carries **no blocked row**.  `surreal_enstrophy_finite_modes` held
  one — the file was red on `main` (`qou-xo1e`) — and it was fixed upstream by
  the `Infinitesimal.*` / `IsFinite.*` namespacing commit, exactly the repair the
  bean proposed.  Re-verified `exit 0` before migrating, so the tie rests on a
  compiling file rather than on the bean's assumption.  Its site is geometric and
  goes to `qIntGeo`, not `qIntBal`.

  **The two genuinely-different sites** are the continuous-index brackets:
  `climax-volume-mass/q-angular-momentum.qNumber`, whose index is a ring element
  (it is evaluated at half-integer spins), and
  `q-geometric-langlands/explicit-formula.qInteger`, whose index is a real Reeb
  eigenvalue under `rpow`.  Both `qIntBal` (ℕ) and `qIntBalZ` (ℤ) are discretely
  indexed, so for these there is *no equation to state* — not merely none
  convenient.

  **Two sites that looked genuinely different and were not.**  An earlier census
  set aside `Interactions.HeckeEnergyPositivity.qIntegerRescaled` (`∑ q^{2j}`)
  and `HeckeAlgebra.JonesMarkovWenzl.qInteger` (half-powers `q^{k/2}`) as
  separate conventions.  They are the same convention twisted: the first is
  `qIntGeo` at `q²`, the second `qIntBal` at `q^{1/2}` — mirror images across
  `qIntBal_eq_twist_canonical`, both now proved at their sites.  A third,
  `Archimedean.GroundRing.qInt`, cannot be `qIntBal` at all (`ℤ[q,q⁻¹]` is not a
  field), but carries `qInt_eq_geo_twist`: the same twist stated division-free,
  which survives the drop to a `CommRing` because `qIntGeo` needs only that.

  The lesson worth keeping: **a site that looks like a different convention
  deserves a proof attempt before it is recorded as one.**  Three of five
  write-offs did not survive one.

  -- Ref: [leitner2026] docs/audits/2026-08-08-q-integer-convention-derived.md
  -- Ref: [leitner2026] AGENTS.md §7a (Hecke–Skein convention)
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
  QOU.Mass.QHookDimensionBalanced.qIntPoly q n

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

**The gap, and its closure.** The *balanced* form is singular at `q = −1` as
well (`q − q⁻¹ = 0` there too).  This was first recorded here as an open gap —
"the two-sided variant is left to whoever needs `q = −1`" — on the belief that
the guarded-balanced sites all guard only `q = 1`.  A closer census found that
belief wrong: **three sites guard the singular locus itself**, writing
`if q − q⁻¹ = 0` (`unified-iterative-correction`, `QSchurYLambdaClosedForm`) or
the equivalent `if q = q⁻¹` (`zeta8-witness-level2-su2`), and a fourth
(`QOU.IwahoriHecke.Hoefsmit.qBracket`) guards `q ≠ 1 ∧ q ≠ −1` explicitly.  So
the two-sided variant had four users already.  It is `qIntBalClSing` below, and
the two guarded families are now separated by name rather than conflated:

| form | guard | value on the guard |
|---|---|---|
| `qIntBalCl` | `q = 1` | `n` |
| `qIntBalClSing` | `q − q⁻¹ = 0` (i.e. `q = ±1`, and `q = 0`) | `n` |

They are **not** interchangeable: away from characteristic `2`,
`qIntBalCl (−1) n = 0` while `qIntBalClSing (−1) n = n`.
`qIntBalClSing_eq_qIntBalCl` states exactly where they do agree, and
`qIntBalCl_neg_one_eq_zero` carries the `(-1 : R) ≠ 1` hypothesis that separates
them — in characteristic `2` the locus `{1, −1}` is a single point and the two
forms coincide, so the distinction this module draws is a
characteristic-`≠ 2` phenomenon. -/

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

open scoped Classical in
/-- **Singular-locus-guarded balanced q-integer**: `qIntBal` away from the whole
locus where the balanced denominator vanishes, and `n` on it.

This is the two-sided companion to `qIntBalCl`, and the form four corpus sites
actually use.  Two honesty notes on the guard, since `q − q⁻¹ = 0` is *not* the
same set as `q = ±1`:

* **`q = −1` is a genuine removable singularity** and `n` is its correct value,
  which is why the guard is worth having: `qIntBalCl` returns `0` there.
* **`q = 0` is caught too**, because Lean's `0⁻¹ = 0` makes `q − q⁻¹ = 0` hold
  at zero.  The value `n` there is *not* a limit of anything — it is junk from a
  junk input.  The guard is stated on the denominator rather than on `q = ±1`
  because that is what the call sites wrote; nothing downstream evaluates at
  `q = 0`, and the substrate sits at `q₀ ≈ 1.11`. -/
noncomputable def qIntBalClSing (q : R) (n : ℕ) : R :=
  if q - q⁻¹ = 0 then (n : R) else qIntBal q n

/-- Away from the singular locus the guard is invisible — the bridge a
singular-locus-guarded site needs to reuse any unguarded `qIntBal` lemma. -/
theorem qIntBalClSing_of_ne {q : R} (h : q - q⁻¹ ≠ 0) (n : ℕ) :
    qIntBalClSing q n = qIntBal q n := by
  simp [qIntBalClSing, h]

@[simp] theorem qIntBalClSing_one (n : ℕ) : qIntBalClSing (1 : R) n = (n : R) := by
  simp [qIntBalClSing]

/-- **Exactly where the two guarded forms agree.**  Off `q ∈ {0, −1}` they are
the same function; on those two points they differ (`qIntBalCl` falls through to
`qIntBal`, which is `0` there, while `qIntBalClSing` returns `n`).  This is the
lemma that makes "one-sided vs two-sided guard is a behaviour change" checkable
rather than asserted — the same service `qIntBal_one_eq_zero` performs for
guarded vs unguarded. -/
theorem qIntBalClSing_eq_qIntBalCl {q : R} (h0 : q ≠ 0) (hm : q ≠ -1) (n : ℕ) :
    qIntBalClSing q n = qIntBalCl q n := by
  by_cases h1 : q = 1
  · subst h1; simp [qIntBalClSing, qIntBalCl]
  · have hne : q - q⁻¹ ≠ 0 := by
      intro h
      have hqq : q = q⁻¹ := by linear_combination h
      have hsq : q * q = 1 := by
        field_simp at hqq
        linear_combination hqq
      have hfac : (q - 1) * (q + 1) = 0 := by ring_nf; linear_combination hsq
      rcases mul_eq_zero.mp hfac with h' | h'
      · exact h1 (by linear_combination h')
      · exact hm (by linear_combination h')
    rw [qIntBalClSing_of_ne hne, qIntBalCl_of_ne_one h1]

/-- The separating instance, stated so the difference is a theorem and not a
remark: at `q = −1` the one-sided guard falls through to `0`, the two-sided one
returns `n`.

**The hypothesis is not boilerplate.** In characteristic `2` we have `−1 = 1`,
so `qIntBalCl (−1) n = qIntBalCl 1 n = n` and this statement is *false* — the
two guarded forms coincide there because the two-point locus `{1, −1}` has
collapsed to one point.  `(-1 : R) ≠ 1` says exactly "the characteristic is not
`2`", which is what makes the one-sided guard genuinely one-sided. -/
theorem qIntBalCl_neg_one_eq_zero (h : (-1 : R) ≠ 1) (n : ℕ) :
    qIntBalCl (-1 : R) n = 0 := by
  rw [qIntBalCl_of_ne_one h]
  simp [qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal]

@[simp] theorem qIntBalClSing_neg_one (n : ℕ) :
    qIntBalClSing (-1 : R) n = (n : R) := by
  simp [qIntBalClSing]

/-! ### Small-index shorthands

Five corpus sites write `[2]_q` and `[3]_q` out longhand as `q + q⁻¹` and
`q² + 1 + q⁻²` under local names (`qInt2`, `qBracket2`, `qInt3`).  They cannot
be aliased — the longhand *is* their body and their proofs use it — but they can
be tied to the canonical bracket by these two identities.

Note both are **conditional**, and on more than the obvious: `[2]_q` needs only
`q − q⁻¹ ≠ 0`, but `[3]_q` additionally needs `q ≠ 0`, because the middle term
`1` is `q · q⁻¹`.  A shorthand site is therefore equal to the canonical bracket
*away from the degenerate locus*, not everywhere — which is exactly the kind of
thing a body swap would have hidden. -/

theorem qIntBal_two {R : Type*} [Field R] (q : R) (h : q - q⁻¹ ≠ 0) :
    qIntBal q 2 = q + q⁻¹ := by
  rw [qIntBal_def, div_eq_iff h]; ring

theorem qIntBal_three {R : Type*} [Field R] (q : R) (hq : q ≠ 0)
    (h : q - q⁻¹ ≠ 0) : qIntBal q 3 = q ^ 2 + 1 + q⁻¹ ^ 2 := by
  rw [qIntBal_def, div_eq_iff h]
  field_simp
  ring

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

section QFactorial

variable {R : Type*} [Field R]

/-- **The canonical q-factorial** `[n]_q! = ∏_{i=1}^{n} [i]_q`, balanced convention.

Worth having as a named object rather than as ad-hoc bracket products: the corpus
already carries `[3]_q!` in two load-bearing places — the Borromean observable
`F_Bor = |tr_M(β_Bor)| · [3]_q! / q³`, and the q-Schur Markov weight of the
trivial partition, `y_{(3)}(q) := q³ / [3]_q!`.  A bracket product written out
long-hand hides that identification. -/
noncomputable def qFactBal (q : R) (n : ℕ) : R :=
  ∏ i ∈ Finset.range n, qIntBal q (i + 1)

/-- `[1]_q = 1` — away from the singular locus, where it is `0/0`.

The hypothesis is the same `q − q⁻¹ ≠ 0` that `qIntBalClSing` guards, and it is
not removable: at `q = ±1` (and at `q = 0`, via Lean's `0⁻¹ = 0`) the quotient is
`0/0 = 0`, so `[1]_q = 0` there and every q-factorial below collapses. -/
theorem qIntBal_one_of_ne_sing {q : R} (h : q - q⁻¹ ≠ 0) : qIntBal q 1 = 1 := by
  rw [qIntBal_def, pow_one, pow_one, div_self h]

/-- **`[3]_q! = [2]_q · [3]_q`** — the identity that reframes a two-index product
as a one-index q-factorial.

This is the whole content of the observation about `conj:magic-shell-coupling-kappa`'s
normaliser: what reads as "the LR fusion of two magic-shell channels `V_2 ⊗ V_3`"
is `[3]_q!`, hence `q³ / y_{(3)}(q)` — the inverse Markov weight of the trivial
partition `(3) ⊢ 3`.  A rule for *two* channel indices has many readings that
agree at `A = 3`; a q-factorial has *one* index, so the question of how the
normaliser continues off `A = 3` is correspondingly narrower. -/
theorem qFactBal_three {q : R} (h : q - q⁻¹ ≠ 0) :
    qFactBal q 3 = qIntBal q 2 * qIntBal q 3 := by
  rw [qFactBal, Finset.prod_range_succ, Finset.prod_range_succ,
    Finset.prod_range_succ, Finset.prod_range_zero, one_mul,
    qIntBal_one_of_ne_sing h, one_mul]

/-- **The content-shifted Markov weight of the trivial partition** `(n) ⊢ n`:
`y_{(n)}(q) = qⁿ / [n]_q!`.

The corpus states this identification at `n = 3` in `f-bor-borromean-observable`
(`y_{(3)}(q) := q³ / [3]_q!`), where it turns the Borromean observable into
`F_Bor = |tr_M(β_Bor)| / y_{(3)}(q)`.  Named here so the relation to `qFactBal`
is machine-checked rather than carried in prose. -/
noncomputable def yTrivial (q : R) (n : ℕ) : R := q ^ n / qFactBal q n

/-- **`[n]_q! = qⁿ / y_{(n)}(q)`** — the q-factorial *is* the inverse trivial
Markov weight, content-shifted.

Only `q ≠ 0` is needed — the content shift must be invertible.  A first draft also
carried `[n]_q! ≠ 0`, on the reasoning that the singular locus collapses the
product; writing the proof showed that hypothesis is not used.  The identity
survives `[n]_q! = 0`, because Lean's `x / 0 = 0` sends both sides to `0` there. -/
theorem qFactBal_eq_pow_div_yTrivial {q : R} {n : ℕ} (hq : q ≠ 0) :
    qFactBal q n = q ^ n / yTrivial q n := by
  rw [yTrivial, div_div_eq_mul_div, mul_comm, mul_div_assoc,
    div_self (pow_ne_zero n hq), mul_one]

end QFactorial

end QOU.QInteger
