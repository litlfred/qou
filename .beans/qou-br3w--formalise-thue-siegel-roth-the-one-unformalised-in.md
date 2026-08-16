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
