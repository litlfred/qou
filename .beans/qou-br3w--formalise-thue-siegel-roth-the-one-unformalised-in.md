---
# qou-br3w
title: 'Formalise Thue-Siegel-Roth: the one unformalised input the trajectory lane takes as a hypothesis'
status: todo
type: task
created_at: 2026-08-16T10:49:19Z
updated_at: 2026-08-16T10:49:19Z
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
