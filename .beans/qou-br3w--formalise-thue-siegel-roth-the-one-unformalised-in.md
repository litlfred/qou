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
