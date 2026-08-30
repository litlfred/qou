---
# qou-br3w
title: 'Formalise Thue-Siegel-Roth: the one unformalised input the trajectory lane takes as a hypothesis'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T10:49:19Z
updated_at: 2026-08-30T07:27:59Z
---


Successor to `qou-bday`, whose formal lane is complete except for this one input.

## What is needed, exactly

`QOU/AppendixSurreals/DiophantineBirthdayTrajectory.lean` states it as an explicit
hypothesis, deliberately **not** a conjecture:

```lean
def RothExponent : Prop :=
  ∀ α : ℝ, IsAlgebraic ℚ α → Irrational α → ∀ p : ℝ, 2 < p → ¬ LiouvilleWith p α
```

Roth 1955 (Fields Medal). **Settled mathematics — what is missing is a formalisation, not a
proof.** Recording it as open would be the fourth epistemic mislabeling on
`conj:diophantine-birthday`; see `qou-bday` for the other three.

## Why it is worth having

It is the *only* thing between this corpus and a genuine algebraic/transcendental
separation by sign-expansion trajectory. Everything else is proved and sorry-free:

| have | statement |
|---|---|
| runs ⟹ Diophantine exponent | `approx_exponent_of_run` |
| frequent runs ⟹ `LiouvilleWith t` | `liouvilleWith_of_frequent_runs` |
| Roth ⟹ `LiouvilleWith 3` separates | `roth_separates` |

`roth_separates` is already written and proved *conditional on* `RothExponent`, so
discharging the hypothesis immediately upgrades a conditional separation to an
unconditional one. Nothing downstream needs rewriting.

## ⚠ Two name collisions that will mislead a search

1. **Mathlib has a `Roth.lean`** — `Mathlib/Combinatorics/Additive/Corner/Roth.lean`,
   proving **"Roth's theorem"** on three-term arithmetic progressions. Unrelated result,
   same name. So *"is Roth in Mathlib?"* answers **yes by name and no in fact**.
   Thue–Siegel–Roth appears only as a docstring aside in `LiouvilleWith.lean`.
2. **"Siegel" collides too.** Beans `qou-8p1c` and `qou-k7ad` match a search for *Siegel*
   and are about the **Siegel upper half-space** — nothing to do with this. Checked while
   opening this bean, precisely so it would not be filed as a duplicate of one of them.

## Scoping honestly before anyone starts

This is a **serious formalisation project**, not an increment on `qou-bday`. Roth's proof
needs an auxiliary polynomial in many variables, a Wronskian/index argument, and Roth's
lemma on the index of a polynomial at a rational point — none of which Mathlib has. There
is no partial-credit route that yields a useful weakening: Liouville's theorem (already in
Mathlib) is the degree-dependent predecessor, and it is *already* what
`liouville_trajectory_direction_settled` uses.

⚠ **Do not "make progress" by weakening `RothExponent` until it becomes provable.** The
temptation on an undischargeable hypothesis is to soften it; at any exponent `p ≤ 2` the
statement stops separating, and at `p = 1` it is outright vacuous
(`liouvilleWith_one` gives every real approximability to order 1). `qou-bday` already
carries a proved vacuity trap of exactly this shape, `slowApproximation_vacuous_at_one`,
kept so nobody walks into it.

**Better first move than starting the proof:** check whether Roth has landed in Mathlib
upstream, or in a community project (there has been periodic interest). Discharging
`RothExponent` from an upstream result is a one-line change here; proving it is a year.

---
**2026-08-16 — the upstream check this bean recommended: DONE, and the answer is no.**

The bean said the better first move than starting the proof is to check whether Roth has
landed upstream, since discharging from an upstream result is a one-line change here.
Checked, against **current Mathlib master**, not only the pinned revision:

| probe | result |
|---|---|
| `Mathlib/NumberTheory/DiophantineApproximation/Basic.lean` (master, 551 lines) | **no** Roth/Thue/Siegel content |
| `…/Transcendental/Liouville/LiouvilleWith.lean` (master, 340 lines) | line 27 **only** — the same docstring aside, not a theorem |
| `…/DiophantineApproximation/Roth.lean` | HTTP **404** |
| `…/Transcendental/Roth.lean` | HTTP **404** |
| `…/DiophantineApproximation/ThueSiegelRoth.lean` | HTTP **404** |
| local pinned Mathlib `f897ebcf` | same — docstring aside only |

(`Basic.lean` returning 200 is the control: the probe finds files that exist.)

**So the cheap route is foreclosed.** `RothExponent` stays a hypothesis, and
`roth_separates` stays conditional. Nothing to change in the corpus.

### ⚠ Mathlib's own 1000-theorem tracker says so too — but do NOT price work off it

`docs/1000.yaml` on master carries

```yaml
Q751120:
  title: Thue–Siegel–Roth theorem
```

with **no `decl` field**, where a formalised neighbour looks like

```yaml
Q752375:
  title: Extreme value theorem
  decl: IsCompact.exists_isMinOn
```

That agrees with the source grep — **but it is weak evidence on its own**, and this is worth
recording before anyone leans on it. `Q576478` *"Liouville's theorem (complex analysis)"*
also has **no `decl`**, and Mathlib certainly proves that. Of 1179 entries only ~192 carry a
declaration immediately after the title, so **absence of `decl` means "not recorded",
not "not formalised"**. The conclusion above rests on the source grep; the tracker merely
does not contradict it.

### ⚠ A third substring collision in this lane

`grep -i roth` matches **"zeroth"**. Three files under `Mathlib/NumberTheory/` appeared to
mention Roth and every hit was `zeroth convergent` / `zeroth Pythagorean triple`. Added to
the two already recorded here (Mathlib's *other* "Roth's theorem" on arithmetic
progressions; the *Siegel upper half-space* beans). **Three different ways to get a false
positive on this one name** — grep for `Thue` or `Siegel–Roth`, never bare `roth`.

### Status unchanged: still open, and still a project

Nothing here reduces the work; it removes the hope that the work might already be done.
The next real move is the one the bean scopes — auxiliary polynomial, Wronskian/index
argument, Roth's lemma — none of which Mathlib has.

---
**2026-08-16 — started. First prerequisite built; and this bean's own inventory was WRONG.**

### ⚠ Correcting this bean: Mathlib already has Siegel's lemma

The scoping section above says Roth's proof *"needs an auxiliary polynomial in many
variables, a Wronskian/index argument, and Roth's lemma on the index of a polynomial at a
rational point — **none of which Mathlib has**."*

**Siegel's lemma is in Mathlib**, in exactly the form the auxiliary-polynomial construction
needs:

```
Mathlib/NumberTheory/SiegelsLemma.lean
  exists_ne_zero_int_vec_norm_le :
    non-zero m × n integer matrix A with m < n ⟹ a non-zero integer solution t
    with ‖t‖ ≤ (n * ‖A‖) ^ (m / (n - m))
```

Authors Barroero, Capuano, Turchet — Diophantine-geometry people — with a docstring saying
it is *"a fundamental tool in diophantine approximation and transcendence"*. It was
contributed **toward** results of this kind. Measured inventory:

| prerequisite | status |
|---|---|
| Siegel's lemma | **present** |
| house of an algebraic number (`NumberField.house`) | **present** |
| Mahler measure | **present** |
| Hasse derivative, `MvPolynomial.pderiv` | **present** |
| Wronskian | present, **two polynomials only** |
| index of a polynomial at a point | **absent → built, this entry** |
| generalized Wronskians | absent |
| Roth's lemma, Roth's theorem | absent |

The estimate stands as a large project, but "none of which Mathlib has" was wrong and
would have led someone to rebuild Siegel's lemma.

### Built: `QOU/Mathlib/RothIndex.lean`

14 declarations, sorry-free, all standard axioms. Written in **Mathlib style with Mathlib
imports only** — no QOU dependency — so it lifts out verbatim.

`index d α P : WithTop ℚ`, the least weight `∑ⱼ iⱼ/dⱼ` over multi-indices occurring in
`P(x + α)`, with `index 0 = ⊤`.

**Two design choices worth keeping.**

*Translate rather than differentiate.* The textbook index minimises over `i` with
`∂ⁱP(α) ≠ 0`. Formalised directly that drags in iterated partials and, outside
characteristic zero, the factorials that make `∂ⁱ` the wrong object. Translating instead,
the same data is the **support** of `P(x + α)` — a `Finset` — with no derivative and no
characteristic hypothesis.

*`WithTop ℚ`, not `ℚ` with a junk value.* `index 0 = ⊤` is the honest value (the zero
polynomial vanishes to infinite order) and `Finset.inf` over the empty support returns it
unaided, so no `P ≠ 0` hypothesis threads through the API. A junk `0` would make the
product law `index P + index Q ≤ index (P*Q)` **false**.

Proved: `index_zero`, `index_nonneg`, `index_eq_top_iff`, `le_index_iff` (the workhorse —
lower bounds are checked on the support), `index_add_ge`, plus `translate_{zero,add,mul}`.

### ⚠ A validation the lemmas do not give

`index_nonneg` and `index_add_ge` both hold of a definition returning `0` everywhere, and
`index_eq_top_iff` of one returning `⊤` off zero. **None of the lemmas pins the value**, so
a wrong definition satisfies the whole API. `index_X_sq` pins it: `X²` at the origin with
unit weights has index exactly `2`, the order of vanishing.

This is the same discipline as the five vacuity checks in `qou-bday`, applied to a
*definition* rather than a theorem — and it is the more dangerous case, because a wrong
definition makes every downstream proof meaningless while all of them still typecheck.

### ⚠ Cannot open the Mathlib PR from here

GitHub access is scoped to `litlfred/qou`; there is no route to
`leanprover-community/mathlib4`. The file is staged in this repo and registered in
`QOU.lean` so the orphan gate covers it meanwhile. **Upstreaming needs someone with a
Mathlib fork** — the file is import-clean for that.

### Next, in order

1. `index_mul_ge` — the one load-bearing algebraic property, and the reason for `WithTop`.
2. Generalized Wronskians (`m × m` determinants of differential operators).
3. Roth's lemma — the induction on variable count. The hard core.
4. Roth's theorem, via the auxiliary-polynomial contradiction over Mathlib's Siegel lemma.

---
**2026-08-16 — `index_mul_ge` done. The index API is complete.**

```lean
index_mul_ge (d : σ → ℕ) (α : σ → R) (P Q : MvPolynomial σ R) :
  index d α P + index d α Q ≤ index d α (P * Q)
```

18 declarations in `QOU/Mathlib/RothIndex.lean`, sorry-free, all standard axioms.

The proof is three steps and no analysis: the weight `∑ⱼ iⱼ/dⱼ` is **additive** on
multi-indices (`idxWeight_add`, via `Finsupp.sum_add_index'`), every monomial of `P·Q` is a
sum of one from each factor (`support_mul`), so each product monomial's weight splits into
two, each bounded below by its factor's index.

### This is where the `WithTop` choice pays off

With a junk `index 0 = 0` the statement is **false**: `index 0 + index Q = index Q` would
have to bound `index 0 = 0`. The design note written when the definition landed predicted
exactly this, and the lemma is the check on it.

### ⚠ The bound is TIGHT, and that is stronger evidence than the lemma alone

`index_mul_ge` is an inequality, and an inequality can hold for a definition that is
systematically too small. Both sides are now computed on a case where it binds:

| | value |
|---|---|
| `index_X` | `index (X) = 1` |
| `index_X_sq` | `index (X²) = 2` |
| `index_mul_ge` at `X · X` | `1 + 1 ≤ 2` — **equality** |

So the definition is not merely consistent with the product law; it saturates it where the
mathematics says it should. A definition returning `0` everywhere would satisfy
`index_nonneg`, `index_add_ge` **and** `index_mul_ge`, and fail both computations.

### Remaining, unchanged in shape

2. **Generalized Wronskians** — `m × m` determinants of differential operators applied to
   `m` polynomials. Mathlib's `wronskian` is the two-polynomial case; this is the next
   genuinely new construction.
3. **Roth's lemma** — induction on variable count. The hard core, and the reason this bean
   is a project.
4. **Roth's theorem** — auxiliary-polynomial contradiction over Mathlib's existing
   `exists_ne_zero_int_vec_norm_le`.

Still cannot open the Mathlib PR from this session (scope: `litlfred/qou`). The file remains
import-clean — Mathlib imports only, no QOU dependency — so upstreaming is a file copy.

---
**2026-08-16 — generalized Wronskians. Second prerequisite done.**

`QOU/Mathlib/GenWronskian.lean`, sorry-free, standard axioms. Mathlib imports only.

```lean
wronskianMatrix (f : Fin m → R[X]) : Matrix (Fin m) (Fin m) R[X] := fun i j => derivative^[i] (f j)
genWronskian (f : Fin m → R[X]) : R[X] := (wronskianMatrix f).det

genWronskian_eq_zero_of_dependent [IsDomain R] (f) (c) (hc : c ≠ 0)
    (h : ∑ j, C (c j) * f j = 0) : genWronskian f = 0
```

The proof is short once framed right: a dependence differentiated `i` times says the
constant vector `c` lies in the kernel of the Wronskian matrix, and over a domain
`Matrix.exists_mulVec_eq_zero_iff` turns a kernel vector into a vanishing determinant.
No analysis, no induction.

**The direction Roth's lemma consumes is the contrapositive** — a non-zero generalized
Wronskian certifies linear independence.

### ⚠ Two pinning checks, because the theorem alone does not pin anything

`genWronskian_eq_zero_of_dependent` is satisfied by a definition returning `0` identically,
and every downstream use would still typecheck. Two computations rule that out:

| check | content |
|---|---|
| `genWronskian_two` | `genWronskian ![a, b] = wronskian a b` — **agrees with Mathlib's existing two-polynomial definition on the nose**, so this is a generalisation rather than a look-alike |
| `genWronskian_one_X` | `genWronskian ![1, X] = 1` — a **non-zero** Wronskian exists, so the contrapositive certifies something |

The first is the one I would not want to skip: without it the file defines *a* determinant
of derivatives, and nothing says it is the Wronskian.

### ⚠ The converse is NOT proved, and is not a formality

*Independence ⟹ some generalized Wronskian is non-zero* is the other half Roth needs, and
it is materially harder:

- **false in characteristic `p`** for the naive derivative — `1, xᵖ` are independent and
  every derivative of `xᵖ` vanishes — so it needs characteristic zero, or restating over
  Hasse derivatives;
- in several variables it needs *generalized* operators (products of partials of bounded
  total order), not the iterated single derivative used here, plus a choice of which `m`.

Stated in the file rather than assumed, so nothing downstream can quietly consume it.

### Progress against the original scoping

| prerequisite | status |
|---|---|
| Siegel's lemma | present in Mathlib (this bean's inventory was wrong) |
| **index at a point** | **done** — `RothIndex.lean`, 18 decls |
| **generalized Wronskians (vanishing direction)** | **done** — this file |
| generalized Wronskians (independence direction) | open, needs char 0 |
| Roth's lemma | open — the hard core |
| Roth's theorem | open |

---
**2026-08-16 — the Wronskian converse at `m = 2`, characteristic zero. Base case done.**

```lean
exists_dependence_of_wronskian_eq_zero {K} [Field K] [CharZero K] [DecidableEq K]
    {a b : K[X]} (ha : a ≠ 0) (hw : wronskian a b = 0) :
  ∃ c d : K, c ≠ 0 ∧ C c * b + C d * a = 0
```

Nine declarations in `GenWronskian.lean`, sorry-free, standard axioms.

**The route, once the right Mathlib pieces were found:** divide by the gcd to reach coprime
`a₁, b₁`; the new `wronskian_mul_mul` (`W(ga, gb) = g²·W(a, b)`) kills the `g²`, so
`W(a₁, b₁) = 0`; Mathlib's `IsCoprime.wronskian_eq_zero_iff` turns that into
`a₁' = b₁' = 0`; `eq_C_of_derivative_eq_zero` makes both constant in characteristic zero;
and `b₁ · a − a₁ · b = 0` is the dependence.

Both of the hard steps were **already in Mathlib** — the coprime criterion and the
char-zero constancy. Only the scaling identity was missing, and it is two lines.

### ⚠ Three instance/API traps, each costing a build cycle

1. **`EuclideanDomain K[X]` does not synthesize from the Wronskian imports** — it needs
   `Mathlib.Algebra.Polynomial.FieldDivision` transitively. The error reads as a missing
   *instance argument*, which sends you to add `[DecidableEq K]`; the real fix is an
   **import**.
2. **`isCoprime_div_gcd_div_gcd` uses `GCDMonoid.gcd`, not `EuclideanDomain.gcd`**, and
   requires the **second** argument non-zero. My hypothesis was `a ≠ 0`, so the proof had to
   split on `b = 0` instead — the degenerate branch is `1·b + 0·a = 0`.
3. **`GCDMonoid K[X]` still does not synthesize** after that: the instance is
   `Polynomial.normalizedGcdMonoid` in `RingTheory/Polynomial/Content.lean`, a third import.

None of these is visible from the statement, and each presents as a different problem than
it is.

### ⚠ What is NOT proved, restated so the file cannot be over-read

General `m` — the statement Roth's lemma actually consumes. The induction step needs the
ratio argument in the function field and is materially harder than the base case.

Characteristic zero is **not a convenience**: in characteristic `p` the converse is
outright **false** for the naive derivative, since `xᵖ` has every derivative zero, so
`1, xᵖ` are linearly independent with vanishing Wronskian. The file's header said the
converse was "not proved here"; corrected to say which case is and which is not.

### Standing

| prerequisite | status |
|---|---|
| Siegel's lemma | already in Mathlib |
| index at a point | **done** (18 decls) |
| generalized Wronskian, vanishing direction | **done** |
| generalized Wronskian, converse at `m = 2`, char 0 | **done** |
| generalized Wronskian, converse at general `m` | open |
| Roth's lemma | open — the hard core |
| Roth's theorem | open |

---
**2026-08-16 — the crux of the general-`m` induction, isolated and proved.**

The full general-`m` converse needs rank arguments over `RatFunc K` and is a multi-day
development. Rather than start it and leave it half-built, I isolated its **mathematical
content** and proved that:

```lean
sum_derivative_of_forall_sum_eq_zero (f c : Fin m → R[X]) (k : ℕ)
    (h : ∀ i ≤ k, ∑ j, c j * derivative^[i] (f j) = 0) :
  ∀ i < k, ∑ j, derivative (c j) * derivative^[i] (f j) = 0
```

**Derivative descent.** Differentiating the `i`-th relation gives
`∑ cⱼ′ fⱼ⁽ⁱ⁾ + ∑ cⱼ fⱼ⁽ⁱ⁺¹⁾ = 0`, and the second sum *is* the `(i+1)`-st relation, hence
zero. That asymmetry is why the hypothesis must reach **one row further** than the
conclusion, and it is the whole reason the classical proof works.

This is the step that upgrades a `K(X)`-dependence to the `K`-dependence actually wanted:
iterating it forces every coefficient to be constant. Everything else in the induction —
getting the kernel vector from the vanishing determinant, the minimality set-up making the
`(m−1) × (m−1)` minor invertible — is rank and minor bookkeeping.

**Proved over a plain commutative ring.** No field, no characteristic hypothesis: the
argument is only the product rule plus re-indexing. That is worth noting because the
*surrounding* induction does need char 0 — so this piece is reusable in settings where the
rest is not.

### ⚠ Non-vacuity, again with teeth

At `k = 0` the conclusion quantifies over `i < 0` and says nothing, so all content is at
`k ≥ 1`. And a reader might reasonably doubt the hypothesis can hold that far with `c`
**non-constant** — for *independent* `f` it cannot. It can when the `f` are dependent, which
is exactly the situation the induction is in. `sum_derivative_descent_witness`:
`f = ![X, X]`, `c = ![X, −X]` annihilates every derivative row, and the lemma applies.

### ⚠ Honest scoping of what "remains"

The file's `Next` section previously called the rest "materially harder" without saying
what it is. Now enumerated: kernel vector from vanishing determinant; the minimality
set-up; iterating the descent lemma. **These are bookkeeping in the sense of "not
conceptually new", not in the sense of "short"** — the distinction matters, and conflating
them is how a multi-day job gets scheduled as an afternoon.

### Standing

11 declarations in `GenWronskian.lean`, sorry-free, standard axioms. Combined with
`RothIndex.lean` (18), that is **29 declarations of Roth prerequisites**, none of which
existed in Mathlib.

---

## Progress, 2026-08-19

Four of the prerequisites are now done and merged or in review.

| prerequisite | status |
|---|---|
| Siegel's lemma | present in Mathlib (`exists_ne_zero_int_vec_norm_le`) |
| index at a point, product law | done — `QOU/Mathlib/RothIndex.lean` |
| generalized Wronskians, univariate | done, **with the full dependence iff** `genWronskian_eq_zero_iff` |
| generalized Wronskians, several variables | done — `QOU/Mathlib/MvGenWronskian.lean` |
| index under differentiation | done — PR #5316 |
| several-variable Wronskian converse | **open** |
| Roth's lemma | **open — the hard core** |
| Roth's theorem | **open** |

Merged in #4907: the general-`m` univariate converse and the multivariate Wronskian.
In review as #5316: `index_le_index_pderiv_add` and its iterate.

### Two recorded predictions this arc falsified — both mine

**The `RatFunc` route was avoidable.** This file and `GenWronskian.lean` both recorded that
the general-`m` converse "needs the ratio argument in the function field and is materially
harder". It does not. `sum_wronskian_combo_eq_zero` multiplies by `c_l` where the classical
proof divides by it, which keeps the entire argument inside `K[X]` — and the resulting
entries are literally `wronskian (c l) (c j)`, so the `m = 2` converse applies directly.
The "materially harder" estimate was wrong, and the scoping note above that called the
remainder "bookkeeping in the sense of not conceptually new, not in the sense of short"
was right on the first half and pessimistic on the second: steps 1, 2 and 5 needed no new
mathematics and landed in one sitting.

**The differentiation step needed no support filter.** The recorded note predicted the
bound "is rescued only because `pderiv_monomial` carries a factor `s_i` that kills exactly
those monomials" with `s_i = 0`. No rescue was needed: the statement is an *inequality*, so
the degenerate case where truncated subtraction gives `s - e_i = s` is simply slack. Only
the sharper equality would have forced the filter.

### One real defect this arc caught in its own work

The 5-step route committed for the converse had step 5 as "substituting,
`c_m * (sum_j lam_j f_j) = 0`, and `c_m /= 0` in a domain gives the constant dependence".
That yields the sum but establishes **nothing about `lam /= 0`** — and `lam = 0` satisfies
the conclusion vacuously, so as written it would have licensed a proof of nothing. Repaired
from a step already proved: applying the `m = 2` converse at `j = l` forces `lam_l = 1`.

### Standing

`RothIndex.lean` 27 declarations, `GenWronskian.lean` 18, `MvGenWronskian.lean` 8 — **53
declarations of Roth prerequisites**, all sorry-free on the standard axiom set, none of
which existed in Mathlib.

---

## Progress, 2026-08-21 — all prerequisites done

**Every Thue–Siegel–Roth prerequisite is now formalised.** What remains is Roth's lemma
itself and then the theorem.

| prerequisite | status |
|---|---|
| Siegel's lemma | present in Mathlib |
| index at a point, product law | done |
| index under differentiation | done — PR #5316 |
| generalized Wronskians, univariate, **both directions** | done — merged #4907 |
| generalized Wronskians, several variables, **both directions** | done — PR #5316 |
| Roth's lemma | **open — the hard core** |
| Roth's theorem | **open** |

### The converse came out of linear algebra, not analysis

The several-variable converse looked like the hardest remaining piece and was not. Its
content is a statement with no derivatives in it at all:

    LinearIndependent K f  ↔  ∃ α, det (coeffMatrix α f) ≠ 0

Mathlib has no "some m × m minor is non-singular" lemma — `Rank.lean` carries the rank
inequalities but no existence statement — so it is proved from `det_succ_row` by induction,
expanding along the **new** row. The expansion must be along the *last* row: deleting it
removes every entry the new index occurs in, which is what makes the cofactors independent
of it. Any other row leaves it in the minors and the argument does not close.

The bridge to derivatives is then a diagonal rescaling by positive integers, and the
Wronskian is non-zero because it is non-zero **at the origin**.

### ⚠ A gap the criterion does NOT close

Roth's lemma needs the operator family to have **bounded order** (total order below the
index, or bounded by `m`). `exists_mvGenWronskian_ne_zero` produces a family from arbitrary
multi-indices with no such bound. Supplying it is where the degree hypotheses on the
auxiliary polynomial enter — a real step, not bookkeeping. Recorded in both files' `Next`
sections, because the criterion now *reads* as complete and this is easy to consume as
though the bound were already there.

### Running tally of falsified predictions — three, all mine

1. The general-`m` univariate converse "needs the ratio argument in the function field".
   It does not; multiplying by `c_l` where the classical proof divides keeps it in `K[X]`.
2. The differentiation bound "is rescued only because `pderiv_monomial` carries a factor
   `s_i`". No rescue needed — it is an *inequality*, so the degenerate case is slack. The
   same rescue **is** needed in `coeff_pderiv`, which is an equality; the two cases resolve
   opposite ways and the notes now say which is which.
3. The several-variable converse as "materially harder". It is a cofactor induction.

### Standing

`RothIndex.lean` 27 declarations, `GenWronskian.lean` 18, `MvGenWronskian.lean` 21 — **66
declarations of Roth prerequisites**, all sorry-free on the standard axiom set, none of
which existed in Mathlib.

## 2026-08-30 -- the shortcut assembly would have been dishonest, so it was not taken

Steps 1-4 are individually done (qou-qi0t, qou-86j4 + qou-jm52, qou-4lbh, qou-ujl8). The obvious
next move was a theorem composing all four. I did not write it, and the reason is worth recording
because the result would have LOOKED complete.

THE TRAP. Step 2's O_K entry point, le_index_of_norm_lt, takes the per-embedding smallness of the
translated coefficients as a hypothesis -- exactly as its Z sibling takes |coeff| < 1/prod q^r. An
assembly that supplies that hypothesis from outside would type-check, would chain steps 2, 3 and 4,
and would NEVER USE STEP 1. Step 1's only output is a lower bound on the index at alpha, and the
sole path from that to step 2's conclusion runs through the analytic estimate that produces the
smallness. Take the smallness as given and step 1 becomes decorative: the composed theorem would
be true, axiom-clean, and silently missing a quarter of the proof.

That is the same failure mode as correction 24 (a weaker-but-true statement that costs an exponent
and passes every check) except worse, because the missing piece would be an entire step rather
than a factor.

WHAT WAS ACTUALLY BLOCKING. The analytic estimate (RothTaylorBound) was stated for |.| on R, and
the O_K case needs it at a COMPLEX embedding: smallness at phi_0, and only the house bound at the
other conjugates. So the Z chain could not feed the O_K vanishing criterion at all.

FIXED BY GENERALISING, NOT COPYING. The peeling induction was already generic over a
SubmultSeminorm; only the four abs_ wrappers were R-specific. They are now
seminorm_coeff_translate_add_le_prod, seminorm_coeff_translate_le and
seminorm_coeff_translate_add_le_index over an arbitrary SubmultSeminorm, with the abs_ statements
one line each, plus SubmultSeminorm.sum_le (the iterated form of add_le, which the structure
carries only in binary form). submultSeminorm_norm_complex is the C instance, and it is the whole
cost of the C case. Every downstream module -- RothIndexGap, RothContradiction, RothNormalisation
-- rebuilds unchanged.

NEXT, and now unblocked: run the C-valued Taylor estimate at phi_0 against step 1's house bounds
at the other conjugates, feed le_index_of_norm_lt, and only then compose with steps 3 and 4. The
assembly is worth writing once it carries step 1 rather than stepping around it.

STILL OUT OF SCOPE after that: the parameter SELECTION -- choosing q_1 large then q_2, ..., q_m
from an infinite sequence of good approximations with q_{h+1} >> q_h. That is what turns a
contradiction into "finitely many solutions", and it is what step 5 (not LiouvilleWith) needs.

## 2026-08-30 -- the composition that carries step 1

embedding_coeff_translate / norm_embedding_coeff_translate_le /
norm_embedding_coeff_translate_le_index (RothAlgebraicInteger), axiom-clean, .olean deleted first.

embedding_coeff_translate is the structural fact the whole O_K case rests on: an embedding phi
FIXES Q, so the rational point does not move under phi -- only the coefficients do. That is why
the same beta serves at every conjugate and why the d-1 "other" bounds are about the same
polynomial evaluated the same way.

norm_embedding_coeff_translate_le_index is the composition the previous entry said was the honest
next move, and it is honest for one specific reason: its hidx argument IS step 1's index at alpha,
and that is what restricts the sum. The estimate consumes step 1 rather than assuming its
consequence. norm_embedding_coeff_translate_le is the trivial companion at the other d-1
embeddings -- no smallness, just the height budget against the point's own size.

Both go through the seminorm_ generalisation from the previous entry with f = ||.|| on C; nothing
new about the peeling was needed, which is the payoff of having generalised instead of copied.

REMAINING on this bean: assemble these two into le_index_of_norm_lt's hypothesis (mechanical --
M is the d-1 bound, the phi_0 bound is the Taylor one), then compose with steps 3 and 4. After
that, the parameter SELECTION, which is what turns a contradiction into "finitely many solutions".

## 2026-08-30 -- step 2 over O_K runs end to end. QOU/Mathlib/RothAssembly.lean

le_index_of_taylor_house composes the two embedding bounds into le_index_of_norm_lt's hypothesis,
so step 2 over O_K now runs from step 1's auxiliary polynomial to a lower bound on the index at
the rational point, with only a numeric comparison (hfinal) left. Axiom-clean, .olean deleted
first, registered in QOU.lean.

THE ASYMMETRY IS THE CONTENT, and it is why conjBound is a named definition rather than an inline
expression. eq_zero_of_norm_mul_pow_lt_one needs ||phi_0 x|| * M^{d-1} < 1, so the two estimates
enter the final inequality DIFFERENTLY: the phi_0 bound linearly, the conjugate bound raised to
the d-1. A factor wasted in conjBound costs d-1 times as much as one wasted at phi_0, and the two
must not be tuned as if interchangeable.

Over Z the asymmetry disappears because d = 1 and M^{d-1} = 1. That is a fact about the SHAPE of
the two statements, not a route from one to the other -- the vanishing criteria remain different
theorems with different hypotheses, as qou-86j4 recorded.

hidx is load-bearing here, which was the whole point of the previous entry: it is what restricts
the sum in the phi_0 estimate. The draft that would have taken the smallness directly as a
hypothesis is now definitively not what got built.

REMAINING on this bean:
  1. compose le_index_of_taylor_house with steps 3 and 4 -- mechanical, the O_K analogue of
     roth_contradiction, whose Z version already exists;
  2. discharge hfinal from a parameter record -- the O_K analogue of RothNormalisation, and note
     it must budget for the d-1 exponent that the Z case does not have;
  3. the parameter SELECTION -- choosing q_1 large then q_2, ..., q_m from an infinite sequence of
     good approximations. This is what turns a contradiction into "finitely many solutions" and is
     what step 5 (not LiouvilleWith) needs. It is the only remaining piece that is not bookkeeping.

## 2026-08-30 -- ITEM 1 IS NOT MECHANICAL: steps 1 and 3 do not compose

I said the O_K analogue of roth_contradiction was mechanical. It is not there to be written,
because the chain has a break I had not looked at, and it is not where I had been looking.

THE GAP, verified by reading both signatures rather than assumed:
  * step 1, exists_auxiliary_polynomial (RothAuxiliary):
        exists P : MvPolynomial (Fin m) (O K), ...
  * step 3, index_le_rothBound (RothRealLadder):
        {A : MvPolynomial sigma Z} ... (hA : InRothPolySet a r A)
    and InRothPolySet is defined only for MvPolynomial sigma Z.

So the arc holds TWO HALF-CHAINS that share step 2 and not a coefficient ring:
    Z:    step 2 (Z)  ->  step 3  ->  step 4      complete
    O K:  step 1      ->  step 2 (O K)            complete
and there is no path from step 1 to step 4. Nothing downstream of either half fixes it; the join
has to be made at the coefficient ring.

WHY IT HAPPENED. Step 1 was built on Mathlib's exists_ne_zero_int_vec_house_le, whose solution
vector lies in O K. Step 3 was built (in the merged PR) on Mahler's Roth's Lemma, which is about
rational-integer coefficients throughout -- including the finiteness of R(a;r)
(RothLemmaStatement:331), which is a box count over Z and would become a Northcott statement over
O K. The two were each correct and were never put in the same room, which is correction 26's shape
at the scale of a whole arc rather than two lemmas.

TWO ROUTES, and route A is much cheaper.
  A. Build the auxiliary polynomial over Z instead: Siegel over Z is Mathlib's
     Mathlib/NumberTheory/SiegelsLemma.lean (exists_ne_zero_int_vec_norm_le), and the K-linear
     vanishing conditions expand in a Q-basis of K into deg(alpha) times as many Z-linear ones.
     Everything from step 2 (Z) onward already works.
  B. Re-prove Roth's Lemma over O K -- including replacing the R(a;r) box count with Northcott.
     A much larger job for no gain I can see.

AND ROUTE A RESTORES deg(alpha) TO THE COUNTING, which corrects my own note. RothAuxiliaryPolynomial's
header carried a triumphant "the degree of alpha does not appear ... the degree cancels out of the
counting condition entirely". That is TRUE OF MATHLIB'S ENGINE and describes the branch that does
not reach step 3. On route A the classical condition deg(alpha) * #conditions < #unknowns is exactly
what is needed. The note is now corrected in place with the reason.

DELIVERED THIS TURN -- route A's counting prerequisite:
  * nsmul_card_lt_card_idxBox, nsmul_card_lt_card_idxBox_of_eps -- the variance bound with a
    multiplicity, so the system is underdetermined as soon as n < 4 eps^2 m;
  * nsmul_card_idxWeight_lt, nsmul_fintypeCard_idxWeight_lt -- the multi-index and Fintype.card
    forms, the latter being what Siegel over Z consumes;
  * nsmul_fintypeCard_idxWeight_lt_witness -- non-vacuous at eps = 1/2, m = 5, n = 4, and chosen
    so the threshold visibly BITES: 4 < 5 holds, 5 < 5 does not, so the same m that justifies a
    degree-4 alpha does not justify a degree-5 one. deg(alpha) is not decoration.
"take m large" is therefore m > deg(alpha)/(4 eps^2), not m > 1/(4 eps^2).

REVISED REMAINING WORK, replacing the three-item list above:
  1. Build the auxiliary polynomial over Z (route A). Needs: the Q-basis expansion of the K-linear
     conditions, an integral basis for O K (Mathlib has NumberField.integralBasis), and Siegel
     over Z. This is the real work and it is where deg(alpha) enters.
  2. Then step 1 -> step 2 (Z) -> step 3 -> step 4 composes, and roth_contradiction takes it.
  3. Then the parameter selection, unchanged: choosing q_1 large then q_2, ..., q_m from an
     infinite sequence of good approximations. Still the only piece that is not bookkeeping.
The O K half (le_index_of_taylor_house, le_index_of_norm_lt, RothAlgebraicInteger) is NOT wasted --
it is the honest step 2 for an O K-coefficient polynomial, and it is what route B would consume --
but it is off the critical path until route B is chosen, and route B should not be.

## 2026-08-30 -- ITEM 1 DONE: the auxiliary polynomial over Z. QOU/Mathlib/RothAuxiliaryInt.lean

Six declarations, all axiom-clean, .olean deleted first, registered in QOU.lean.

exists_auxiliary_polynomial_int is route A's step 1: a NON-ZERO Z-coefficient polynomial of
bounded degree whose index at (alpha_1,...,alpha_m) is at least mu, with Siegel's height bound on
its coefficients. So step 1 now produces the coefficient ring Roth's Lemma actually requires, and
the break between steps 1 and 3 is closed.

THE PIECE THAT MAKES IT WORK is sum_smul_eq_zero_iff_repr: one O_K-linear vanishing condition is
finrank Q K integer-linear ones. Expand in an integral basis (Mathlib's RingOfIntegers.basis); the
element vanishes exactly when all its coordinates do, and the coordinates of a Z-combination are
the Z-combinations of the coordinates. That single equivalence is where deg(alpha) enters, and it
is why the counting condition becomes the classical deg(alpha) * #conditions < #unknowns.

card_prod_lt_card_idxBoxF discharges that condition from last entry's variance lemma via
card_chooseBasisIndex_eq_finrank, so hcount is PROVED from eps and m rather than assumed:
    finrank Q K < 4 eps^2 m   ==>   #conditions * deg(alpha) < #unknowns.

Both Mathlib engines turned out to need no adaptation. Int.Matrix.exists_ne_zero_int_vec_norm_le
is indexed by arbitrary Fintypes, so the equation index type
({low-weight multi-indices} x {basis coordinates}) and the unknown index type {box} go in
directly -- no Fin reindexing, which is the usual tax on this kind of call. The only wiring needed
was `attribute [local instance] Matrix.seminormedAddCommGroup`, the same local instance Mathlib's
own SiegelsLemma file sets, because the bound is stated against the sup norm.

STILL A HYPOTHESIS in exists_auxiliary_polynomial_int: hpos (the system has at least one
equation). Trivially true whenever the low-weight set and the basis are both non-empty, but it is
Siegel's hypothesis and is left where Siegel puts it.

REVISED REMAINING WORK:
  1. DONE -- auxiliary polynomial over Z.
  2. Compose: step 1 (Z) -> step 2 (Z) -> step 3 -> step 4. Now genuinely mechanical, in the sense
     that the coefficient rings agree; roth_contradiction is waiting and takes InRothPolySet,
     so the remaining glue is turning Siegel's real-valued height bound into the integer bound a
     that InRothPolySet wants (a ceiling) and checking the degree/nonvanishing clauses line up.
  3. The parameter selection -- choosing q_1 large then q_2, ..., q_m from an infinite sequence of
     good approximations. Unchanged, and still the only piece that is not bookkeeping.
The O_K half (RothAlgebraicInteger, RothAssembly) remains correct and off the critical path.

## 2026-08-30 -- THE CHAIN CLOSES. QOU/Mathlib/RothIntegerChain.lean

roth_contradiction_int runs step 1 -> step 2 -> step 3 -> step 4 with the coefficient rings
agreeing throughout. Five declarations, axiom-clean, .olean deleted first, registered in QOU.lean.

TWO PIECES OF GLUE, both small enough to be invisible and large enough to be wrong:

  * inRothPolySet_of_real_bound. Siegel states its bound over R; InRothPolySet wants an integer a.
    The CEILING is forced -- it is the only integer bound that follows from |coeff| <= X, and
    rounding down would be an assertion rather than a consequence.
  * index_real_of_index_field. Step 1 proves the index over K; step 2 consumes it over R. They
    transport along a real embedding psi : K ->+* R, and that embedding is a GENUINE HYPOTHESIS,
    not a technicality: it says the alpha_h are REAL algebraic numbers, which is what Roth's
    theorem is about. A number field with no real embedding has nothing to say here, and the
    composition correctly refuses to typecheck without one. Worth stating because it is exactly
    the kind of hypothesis that gets silently discharged with a `sorry`-free but wrong instance.

A SHAPE CORRECTION I MADE TO MY OWN FIRST DRAFT. It stated the remaining hypotheses as
`forall (P) (a), InRothPolySet a r P -> Gamma_m for a /\ ...`, quantified over every polynomial in
R(a;r). That is a strictly STRONGER hypothesis and therefore a weaker theorem, and it would have
asked a caller to verify Gamma_m for polynomials the construction never produces. Naming Siegel's
bound (siegelHeight, in RothAuxiliaryInt) lets the hypotheses land on the a the construction
ACTUALLY produces -- ceil(siegelHeight r alpha mu) -- so hg, hCpos and hlog are now about one
concrete quantity. The over-strong version compiled fine; nothing but reading it would have caught
that it was asking for too much.

WHAT roth_contradiction_int STILL TAKES, and it is only what earlier stages already isolated:
Gamma_m's clauses (hg), the approximation quality (hclose, hT, hGT), and the two numeric
comparisons (hlog, hgap). Nothing new was introduced by the composition, which is the outcome
worth having: the chain did not turn out to need a bridging lemma nobody had budgeted for.

REMAINING -- ONE ITEM, and it is the only piece of Roth's theorem that is not bookkeeping:
  THE PARAMETER SELECTION. Choose q_1 large, then q_2, ..., q_m from an infinite supply of good
  approximations with q_{h+1} >> q_h, and r_h from the q_h, so that hg, hlog and hgap all hold
  simultaneously. This is what turns a contradiction into "finitely many solutions", and it is
  what step 5 (not LiouvilleWith) needs. Everything else in the arc is now proved.

## 2026-08-30 -- the parameter selection, started. QOU/Mathlib/RothSelection.lean

Six declarations, axiom-clean, .olean deleted first, registered in QOU.lean.

THIS IS THE ONLY PIECE OF THE ARC THAT CONSTRUCTS DATA rather than composing hypotheses a caller
supplies, and the only place the "infinitely many solutions" assumption is consumed. growSeq is
the greedy recursion: pick a denominator past a threshold, raise it to a power, pick another past
THAT. exists_heights_growing turns an unbounded supply into m heights satisfying Gamma_m's growth
clause, which is where the informal proof's "sufficiently large" actually lives.

THE max AGAINST A FLOOR IS LOAD-BEARING, and it took writing the two_le clause to see why. Without
it the growth function's output is the only lower bound on the next term, so a later height can
land below the floor whenever f returns something small -- and Gamma_m's two_le would then hold at
index 0 and fail everywhere else. Carrying the floor through the recursion makes le_growSeq
uniform in n, which is what two_le needs.

THE GROWTH FUNCTION IS FORCED BY THE CLAUSE. rothGammaFull_of_heights wants
H j ^ (2q) <= H k ^ p on consecutive indices. Choosing the next height beyond H j ^ (2q) gives
H j ^ (2q) <= H k, and H k <= H k ^ p because p >= 1 and H k >= 2. So x |-> x^(2q) is not a choice,
it is what the clause reads off.

TWO CLAUSES, NOT ONE. Making the floor a parameter rather than the constant 2 means
exists_heights_growing_floor discharges Gamma_m's clause 3 as well, at N_0 = 2^F. That clause is
the one that bites hardest -- RothRealLadder's witness needed H = 1024 at m = 2 purely because of
it -- so having it fall out of the same construction is worth the extra parameter.

REMAINING for the selection:
  * hlarge (p + 2q <= p * rothDegrees H N h): needs N chosen large RELATIVE TO THE SELECTED
    HEIGHTS, so it comes after the selection, not before. The dependency order is heights -> N ->
    degrees, and rothDegrees already computes the degrees from (H, N).
  * hbound (b^(mq) <= H_0^(rothDegrees H N 0 * p)): needs H_0 large relative to b, the auxiliary
    polynomial's height bound -- which is ceil(siegelHeight), itself a function of the degrees. So
    this one is genuinely circular-looking and is the piece to think about carefully: the standard
    resolution is that b depends on the degrees only through explicit constants, so H_0 can be
    chosen last.
  * then assemble with slack_pos's condition on eps, delta and m, and step 5 (not LiouvilleWith).

## 2026-08-30 -- investigated the two remaining Gamma_m clauses. hbound is NOT circular

ISSUE 1, hlarge (p + 2q <= p * rothDegrees H N h). RESOLVED AND PROVED. It constrains N relative
to the ALREADY-CHOSEN heights, so the dependency runs one way and there was never a difficulty:
hlarge_of_pow_le derives it from (H h)^{p+2q} <= N for every h, and exists_pow_le constructs such
an N from the heights as (prod_h H h)^{p+2q}. Order: heights -> N -> degrees, never the reverse.

ISSUE 2, hbound (b^{mq} <= H_0^{r_0 p} where b = ceil(siegelHeight r alpha mu)). It READS as
circular: b depends on r, r = rothDegrees H N depends on H_0, and H_0 is what the clause
constrains. IT IS NOT CIRCULAR, and the reason is a cancellation.

  (a) From the TYPES: siegelHeight r alpha mu depends on H only through r. So raising H_0 while
      holding r fixed leaves b alone and raises the right-hand side. That is hbound_mono, proved.
      It is the formal content of the informal proof's "choose q_1 large".
  (b) Holding r fixed while raising H_0 means raising N too, and the asymptotics close it.
      r_0 log H_0 ~ log N, so RHS ~ p log N. On the left, log b ~ rho log(#box * ||A||) with
      rho = #E/(#box - #E), and both #box and ||A|| grow like exp(c sum_h r_h) while
      sum_h r_h ~ log N * sum_h 1/log H_h. So LHS ~ m q rho c log N sum_h 1/log H_h, and LOG N
      CANCELS. The growth clause makes H_0 the smallest height, so sum_h 1/log H_h <= m/log H_0,
      and the clause reduces to a condition on H_0 ALONE: log H_0 >~ m^2 q rho c / p.

WHAT IS PROVED AND WHAT IS NOT. (a) is proved (hbound_mono). (b) is an asymptotic estimate and is
NOT formalised -- it needs bounds on #box and ||auxMatrixInt|| in terms of sum_h r_h, which this
arc has not written down. Recorded explicitly in the module, because with hlarge proved and
hbound_mono proved next to it, the untouched half would otherwise look discharged by association.

hbound_mono was written with 0 <= b; the linter reported it unused and it is -- only the BASE H j
needs to be non-negative, and it is a natural number. Stronger statement kept.

REVISED REMAINING WORK:
  1. The #box and ||A|| estimates in terms of sum_h r_h -- the missing half of (b). #box is
     prod_h (r_h + 1), so that half is easy; ||auxMatrixInt|| needs a bound on the integral-basis
     coordinates of translateMatrix alpha i n, which is a house-style estimate the arc already has
     the shape of (seminorm_translateMatrix_le) but not over an integral basis.
  2. Assemble: heights (exists_heights_growing_floor) -> N (exists_pow_le) -> degrees
     (rothDegrees) -> Gamma_m (rothGammaFull_of_heights) -> roth_contradiction_int, with eps,
     delta, m from slack_pos.
  3. Step 5, not LiouvilleWith.

## 2026-08-30 -- hbound's missing half, written down. QOU/Mathlib/RothSiegelBound.lean

Four declarations, axiom-clean, .olean deleted first, registered in QOU.lean. The previous entry
flagged an asymptotic estimate as NOT formalised; this closes it.

  * card_idxBoxF_le_two_pow: #box <= 2^{sum r_h}. Immediate from prod_succ_le_two_pow_sum.
  * norm_auxMatrixInt_le: ||auxMatrixInt|| <= C (2B)^{sum r_h}, with the coordinate-vs-norm
    comparison as a hypothesis hC.
  * abs_basis_repr_le: hC DISCHARGED from Mathlib's basis_repr_norm_le_const_mul_house, so the arc
    assumes nothing about K. The constant is Mathlib's private c, reached the same way
    RothAuxiliary reaches c_1.
  * norm_auxMatrixInt_le_house: the two composed, unconditional.

WHY THIS IS THE HALF THAT MATTERED. Both constants are INERT IN r. Taking logs,
log #box <= (sum r_h) log 2 and log ||A|| <= log c(K) + (sum r_h) log(2B), so log b is LINEAR in
sum r_h. That linearity is precisely what makes the log N cancel on the two sides of
b^{mq} <= H_0^{r_0 p}: sum r_h ~ log N sum_h 1/log H_h against r_0 log H_0 ~ log N.

Splitting norm_auxMatrixInt_le from abs_basis_repr_le was deliberate rather than tidy. The growth
in sum r_h is the arc's business and is proved unconditionally; hC is a fact about K alone. Had
they been one theorem, a reader could not tell which half was doing the work, and the K-fact would
have looked like an arc assumption.

API friction worth recording: Basis is now in the Module namespace, so the reindex lemma is
Module.Basis.repr_reindex_apply -- Basis.reindex_repr and Basis.repr_reindex_apply both fail with
"unknown identifier", which reads like the lemma is missing rather than moved.

REMAINING on this bean, unchanged in substance:
  1. Assemble: heights (exists_heights_growing_floor) -> N (exists_pow_le) -> degrees
     (rothDegrees) -> Gamma_m (rothGammaFull_of_heights) -> roth_contradiction_int, with eps,
     delta, m from slack_pos. Every input now exists; this is arithmetic bookkeeping over the
     named quantities.
  2. Step 5, not LiouvilleWith.

## 2026-08-30 -- the selection assembled: four of Gamma_m's six inputs from the supply alone

Three declarations added to RothSelection, axiom-clean, .olean deleted first.

exists_heights_and_N produces the data and four of rothGammaFull_of_heights's six inputs from an
unbounded supply: the heights, N, and the two_le / floor / growth / hlarge clauses. The order is
forced and IS the content -- heights first (the growth recursion), then N from the heights, then
the degrees from both. Nothing here can be reordered.

exists_rothGammaFull_of_supply states it as an IMPLICATION, and that shape is the honest one.
hbound is a statement ABOUT THE PRODUCED DATA, so it cannot be a hypothesis of the existential;
quantifying it over all possible (H, N) would demand far more than the argument needs -- the same
over-strength I had to correct in roth_contradiction_int's first draft. hbound_mono is what makes
the implication dischargeable: the clause improves as H_0 grows and the supply is unbounded.

exists_rothGammaFull_of_supply_witness discharges every hypothesis at m = 2, p = q = 1, F = 10,
b = 1 over Set.univ, so the machinery is applicable and not vacuous. Worth noting what pins F:
hfloorExp at m = 2 reads 1*(1*2*5) <= F, so F = 10 is the smallest that works -- the same
arithmetic that forced H = 1024 in RothRealLadder's witness. The two are one constraint seen from
opposite ends, which is the sort of thing only shows up when both witnesses exist.

REMAINING:
  1. Discharge hbound for a concrete parameter family. Everything needed is now proved --
     hbound_mono for the monotonicity, card_idxBoxF_le_two_pow and norm_auxMatrixInt_le_house for
     the size estimates, slack_pos for eps/delta/m -- so this is arithmetic over named quantities.
  2. Feed the result to roth_contradiction_int.
  3. Step 5, not LiouvilleWith.

## 2026-08-30 -- Siegel's EXPONENT, and a threshold that had to be doubled

Three declarations added to RothSiegelBound, axiom-clean, .olean deleted first.

A GAP I HAD NOT SEEN, found by trying to use the two size estimates. siegelHeight is
(#box * ||A||)^rho with rho = #E/(#box - #E). The estimates make the BASE well behaved -- both
factors are C^{sum r} -- and that is worth nothing while rho is unbounded. The counting condition
proved so far gives only #E < #box, hence #box - #E >= 1 and rho <= #E; and #E is itself
exponential in sum r, so that bound makes siegelHeight DOUBLY exponential and the argument dies.

Last entry said the size estimates were "the missing half" of hbound. They were a missing half,
not the missing half. The exponent was a second one, and it was invisible until the first was in
hand -- exactly the pattern main's own taxonomy row about draining a residue describes.

THE FIX IS A FACTOR OF TWO IN THE THRESHOLD. Asking 2 deg(alpha) < 4 eps^2 m instead of
deg(alpha) < 4 eps^2 m gives 2#E <= #box (two_card_prod_le_card_idxBoxF), hence rho <= 1 and
siegelHeight <= #box * ||A|| (siegelHeight_le_base). So "take m large" is m > deg(alpha)/(2 eps^2),
not m > deg(alpha)/(4 eps^2). A factor of two in m, bought to avoid a double exponential. The
weaker threshold is the one the variance argument naturally produces and it is NOT ENOUGH, which
is worth stating because nothing in the variance argument hints at it.

siegelHeight_le_pow is the explicit conclusion:
    siegelHeight <= 2^{sum r} * max(1, c(K) (2B)^{sum r}),
so log(siegelHeight) is LINEAR in sum r_h with every constant independent of r. That is what
Gamma_m's height clause needs and what made hbound look circular when absent.

REMAINING:
  1. Instantiate: choose eps, delta, m from slack_pos with the DOUBLED threshold, then H_0 large
     enough that 2^{sum r} max(1, c(K)(2B)^{sum r}) raised to mq is below H_0^{r_0 p}. The
     ingredients are all named now.
  2. Feed roth_contradiction_int.
  3. Step 5, not LiouvilleWith.

## 2026-08-30 -- the two concrete pieces the instantiation needs

sum_rothDegrees_le (RothSelection) and hbound_of_ceil_le (RothSiegelBound), axiom-clean, .oleans
deleted first.

sum_rothDegrees_le: sum_h rothDegrees H N h <= m (log_b N + 1) for any b below every height. The
mechanism is that Nat.log is ANTITONE in its base, so the smallest height gives the largest degree
-- which is why the bound is in terms of H_0 and not of the H_h individually. This is the concrete
form of the asymptotic sum r_h ~ log N sum_h 1/log H_h <= m log N / log H_0 that hbound's
cancellation runs on: it puts the left side of the height clause at N^{c m / log H_0} against a
right side of N^p.

hbound_of_ceil_le: Gamma_m's height clause is about ceil(siegelHeight), which is opaque. This
replaces it by siegelHeight_le_pow's explicit bound, so what a parameter choice must verify is an
inequality between NAMED quantities.

⚠ AND THE REPLACEMENT IS ONE-DIRECTIONAL. siegelHeight <= Y gives ceil(siegelHeight) <= ceil(Y), so
the explicit inequality is SUFFICIENT and not necessary. A parameter family that fails hY might
still satisfy the clause. Stated in the docstring because otherwise a future reader hitting a
failure of hY would read it as a failure of the argument, and it is not.

REMAINING -- and it is now a single arithmetic obligation with every ingredient named:
    ceil(2^{sum r} max(1, c(K)(2B)^{sum r}))^{mq}  <=  H_0^{r_0 p}
with sum r <= m(log_{H_0} N + 1) from sum_rothDegrees_le and r_0 = log_{H_0} N. Taking logs this is
    m q (m (log_{H_0} N + 1) log(4B) + log c(K))  <=  p log_{H_0} N log H_0,
i.e. log H_0 >~ m^2 q log(4B) / p once N is large. So the shape of the final choice is: m and eps
from slack_pos with the DOUBLED threshold (2 deg alpha < 4 eps^2 m), then H_0 past that log
threshold, then the rest of the heights by growth, then N.
Then feed roth_contradiction_int, and step 5 (not LiouvilleWith).

## 2026-08-30 -- the obligation, WITHOUT real logarithms

ceil_siegelHeight_le and pow_le_pow_of_height (RothSiegelBound), axiom-clean, .olean deleted first.

I had written the remaining obligation in logs -- log H_0 >~ m^2 q log(4B)/p -- and set out to
formalise it that way. Exponentiating throughout removes the analysis entirely and leaves a purely
INTEGER inequality:

    C_0^{mq} * W^{2 m^2 q}  <=  H_0^p

with C_0 any integer above c(K) and W any integer above 4B. Both are constants of K and alpha;
neither involves r, N or the heights. So "choose H_0 large" is one arithmetic condition a parameter
family can be checked against with no real-log reasoning anywhere.

  * ceil_siegelHeight_le: ceil(siegelHeight) <= C_0 * W^{sum r}. The real-side chain is
    2^{sum r} max(1, c(K)(2B)^{sum r}) <= C_0 (4B)^{sum r} <= C_0 W^{sum r}, then Int.ceil_le.
  * pow_le_pow_of_height: the arithmetic. sum r <= 2m r_0 (from sum_rothDegrees_le once r_0 >= 1)
    puts the exponent sum r * mq under 2 m^2 q r_0, which the H_0 condition dominates once raised
    to r_0.

THE LOG FORM WAS A DETOUR, and worth recording as one. It is how the informal proof states the
condition and it is how I stated it in the previous two entries, but nothing in the formal chain
needs a logarithm: every quantity in sight is already an integer power, and taking logs only to
exponentiate again adds Real.log's junk-value cases and monotonicity side conditions for nothing.

REMAINING:
  1. Choose the family: m and eps from slack_pos with the doubled threshold, H_0 from the supply
     past C_0^{mq} W^{2m^2q} (p-th root), the rest of the heights by growth, N from the heights.
     Every condition is now arithmetic.
  2. Feed roth_contradiction_int.
  3. Step 5, not LiouvilleWith.

## 2026-08-30 -- hbound follows from the SELECTION'S OWN FLOOR. The near-circularity is closed.

Three declarations (growSeq_mono, le_pow_of_le, hbound_of_height_floor) plus a threading pass
through the selection. All axiom-clean, .oleans deleted first.

hbound_of_height_floor reduces Gamma_m's height clause to

    C_0^{mq} * W^{2 m^2 q}  <=  H_0

-- not H_0^p, just H_0, because le_pow_of_le turns a floor on the height into a floor on its p-th
power. And that threshold is a constant of K, alpha, m, p, q: NOTHING IN IT REFERS TO N, r, OR THE
AUXILIARY POLYNOMIAL. So it can be passed to exists_heights_growing as its floor parameter, which
the selection already accepts.

THAT CLOSES THE NEAR-CIRCULARITY IN THE FORMAL CHAIN, not just in the argument. Two entries ago I
showed hbound was not circular by an asymptotic cancellation; then formalised the two size
estimates; then found the exponent gap; then removed the logarithms. The result is that the clause
is discharged by a parameter the selection takes as INPUT, so there is no fixed point to solve.

WHAT THE THREADING NEEDED, and it was not free. sum_rothDegrees_le bounds sum r using the SMALLEST
height, so it needs the heights to increase -- which they do, but that had to be proved:
growSeq_mono, from each term being at least its predecessor's k-th power with the floor keeping
every term at least 1. That in turn forced 0 < q into exists_heights_growing's signature and out
through exists_heights_growing_floor, exists_heights_and_N, exists_rothGammaFull_of_supply and the
witness. A monotonicity nobody had needed until the smallest height had to be named.

REMAINING:
  1. Assemble: pick m, eps from slack_pos (doubled threshold), set the selection's floor to
     max(2^F, C_0^{mq} W^{2m^2q}), take the heights and N, and feed roth_contradiction_int. Every
     hypothesis is now either produced or a named arithmetic condition.
  2. Step 5, not LiouvilleWith.


## 2026-08-30 -- Steps 1->2->3->4 assembled. Nothing assumed that the chain produces.

roth_contradiction_selected (QOU/Mathlib/RothFinalAssembly.lean) produces the heights, N, the
degrees, the auxiliary polynomial and the approximations, and derives False. Axiom-clean.

WHAT THE PREVIOUS ENTRY GOT WRONG ABOUT b. exists_rothGammaFull_of_supply took b : Z as a CONSTANT
and I called the implication shape "honest". It was honest about hbound and WRONG ABOUT b: the b it
must be applied at is ceil(siegelHeight (rothDegrees H N) alpha mu), a function of the H and N the
theorem itself produces. A constant b cannot be instantiated with it. Generalised to
bOf : (Fin m -> N) -> N -> Z, and exists_rothGammaFull_auxiliary now DISCHARGES the height clause
rather than assuming it -- the threshold mentions none of the produced data, so it goes in as the
selection's floor T and comes back out of T <= H j.

THE NORMALISATION SLACK HAD NO SOURCE. hT and hL' both need a two-sided estimate on r_h log H_h,
and rothDegrees_log_bounds is two-sided only to within log H_h. Nothing in the selection bounded
that against log N, so eta was a free constant with no way to make it small. Fixed by adding an
exponent parameter k to the selection with the clause (H h)^k <= N; then log H_h <= (1/k) log N and
eta = 1/k. That is the formal content of "let N be large compared with the heights".

A FLOOR ON THE HEIGHTS IS NOT A FLOOR ON THE DENOMINATORS -- a rational of height 10^9 can have
denominator 1 -- and hpt constrains the denominators. height_le_mul_den closes it: a rational
bounded by B has max(|num|,den) <= B den. Without that lemma the theta clause is unreachable from
anything the selection can impose.

THE SLACK BUDGET IS NOT slack_pos's. This chain produces K = (2+delta)(1-eta) log N against
L' = (1+eta) log N, so eta appears TWICE WITH OPPOSITE SIGNS -- it inflates the denominators' total
size and deflates the approximation exponent. slack_pos's additive form sees only the first.
fin_of_slack is the right budget: four slacks below a common t with t(16+5 delta) < delta, tight to
that threshold (surplus t + t^2(3+2 delta)). Equivalently, the excess paid from is not delta but
delta - eta(2+delta).

New/changed: exists_rothGammaFull_auxiliary, card_prod_pos, selection_normalisation,
log_pow_le_log, height_le_mul_den, hpt_of_floor, roth_contradiction_selected, fin_of_slack,
hfin_of_slack, exists_slack_bound; k and T threaded through exists_heights_and_N and
exists_rothGammaFull_of_supply. index_real_of_index_field dropped [NumberField K] (linter).

REMAINING:
  1. The parameter existence lemma: exhibit m, p, q, F, k, T, eps, nu, theta satisfying every
     hypothesis of roth_contradiction_selected EXCEPT app. This is the non-vacuity check and it is
     the only thing standing between the assembly and step 5. Order: delta -> t (exists_slack_bound)
     -> eps, theta, k -> m (from hm2 AND nu/m <= t) -> T (from hTtheta) -> p, q, nu, F (hgap needs
     q/p large, hfloorExp then needs F large; both are free).
  2. Step 5: the supply app from a Liouville-type hypothesis, and hence not LiouvilleWith.
