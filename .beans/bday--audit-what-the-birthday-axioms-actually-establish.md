---
# bday
title: 'Audit what the birthday axioms actually establish — they admit a two-valued model'
status: in-progress
type: task
priority: high
tags:
    - lean
    - surreals
    - axiom-audit
    - stale-claim-corrected
parent: hypr
created_at: 2026-08-10T01:35:00Z
updated_at: 2026-08-10T04:15:00Z
---

Follows from the finding proved in `QOU/AppendixSurreals/HyperrealLimitTransfer.lean`
(bean `hypr`):

> `flatBirthday x := if x = 0 then 0 else 1` — **two-valued** — satisfies **all six**
> birthday axioms of `SurrealField` (`QOU/AppendixSurreals/Basic.lean:54`).
> `surrealFieldHyperreal : SurrealField ℝ*` is a sorry-free term over it.

**The consequence, which is the reason for this bean.** Any theorem proved from those
axioms *alone* is true in the flat model too. So for every birthday-derived result in the
corpus, there is a sharp question with a mechanical answer:

> instantiate it at `flatBirthday`. If it degenerates to something trivial, the theorem
> carries **no birthday content**, whatever its statement looks like.

`birthday_avg_le` is the worst case already known: `Basic.lean` documents it as "exactly
Conway's `{L | R}` recipe", "genuinely independent of `birthday_add_le`", with a "narrow
kernel rationale" — and it is satisfied *vacuously* under any bounded birthday, since its
RHS is `≥ 0 + 1 = 1` and its LHS is `≤ 1`.

## Surface to audit

11 modules mention `birthday`. Not all reason *from* the axioms; separate those that do:

- `QOU/AppendixSurreals/Basic.lean` — the axioms themselves
- `QOU/AppendixSurreals/SignSequence.lean` — 20 mentions, 22 decls; includes
  `birthday_gonshorIn_le_omega`, and `Basic.lean` says the sharper
  `birthday (gonshorIn K s) ≤ s.length` bound is *reserved for future induction proofs*
  — check whether the `≤ ω` form proved today is anything more than `flatBirthday ≤ 1`
- `QOU/AppendixSurreals/BirthdayGrading.lean` — 7 mentions, 7 decls
- `QOU/AppendixSurreals/DiophantineBirthday.lean` — carries
  `conj:diophantine-birthday` ("algebraic vs transcendental separated by birthday
  trajectory"). **If the axioms admit the flat model, this conjecture cannot be
  approached from them at all** — the flat model separates nothing. Highest-priority
  entry in this list.
- `QOU/AppendixSurreals/HoefsmitBridge.lean` — 2 mentions
- `QOU/AppendixSurreals/Conjectures.lean` — 4 mentions
- `QOU/Information/{PNeqNpWallUnification, MagnitudeAxisBoundary,
  MagnitudeTraceCommutator, SkeinSurrealGrade}.lean` — **not previously noted as
  birthday-dependent.** Check whether any *claim outside the surreals appendix* rests on
  birthday axioms that turn out to be vacuous. This is where a real correction is most
  likely to be needed.

## Method (mechanical, and provable in Lean)

For each birthday-concluding theorem `T`, specialise to `surrealFieldHyperreal` via
`attribute [local instance]` and check whether the specialised statement follows from
`flatBirthday_le_one` alone. If it does, `T` is vacuous and should be re-labelled.
Ship the vacuity as a Lean theorem, not a comment.

## Then fix the cause, not just the symptom

Two options, and the choice belongs to whoever picks this up:

1. **Strengthen the axioms** so a bounded function no longer satisfies them. The obvious
   missing constraint is a *lower* bound tying birthday to arithmetic complexity — e.g.
   `birthday` of a dyadic of denominator `2^k` is `≥ k`, or `birthday (n : K) = n` for
   naturals. Note `birthday_one = 1` plus `birthday_add_le` already forces
   `birthday n ≤ n`; adding the matching `≥` would kill the flat model outright.
2. **Split the class** — a birthday-free base carrying `Field`/`LinearOrder`/
   `IsStrictOrderedRing`/`ofReal`/`ofReal_strictMono`, plus a birthday mixin. Checked:
   nothing in `StandardPart.lean` uses `birthday` and `isFinite_decomposition`
   (`Basic.lean:382`) is birthday-free, so the whole standard-part theory moves down
   unchanged, and `ℝ*` becomes a genuine instance of the base with no degeneracy.
   `BlowupCalculus.lean` already demonstrates this pattern with a real
   `instBlowupFieldHyperreal`. ~38 modules use `SurrealField`; 6 genuinely touch
   `birthday`.

These are complementary, not alternatives: (2) makes the limit-transfer content honest,
(1) makes the birthday content non-vacuous.

⚠ **Do not promote `surrealFieldHyperreal` or `surrealLimitTransferHyperreal` to global
instances** while doing this. They are `def`s deliberately; a global instance would make
every `SurrealField`-generic theorem silently apply to `ℝ*` under a two-valued birthday.

---
**2026-08-10 — audit run. One relief, one real correction, one sharp principle.**

### 1. RELIEF: no claim outside the surreals appendix is affected

The four `QOU/Information` modules flagged as highest-risk — `PNeqNpWallUnification`,
`MagnitudeAxisBoundary`, `MagnitudeTraceCommutator`, `SkeinSurrealGrade` — **do not
import `QOU.AppendixSurreals` at all.** Every "birthday" occurrence in them is *prose*:
motivational language in docstrings, not term-level dependence on `SurrealField.birthday`.
`SkeinObservationBridge` does import the appendix but never mentions birthday.

So the worry that a live claim outside the appendix rests on vacuous axioms is
**unfounded**. Good news, and it narrows the blast radius to `AppendixSurreals/`.

### 2. THE SHARP PRINCIPLE, which is what the flat model actually buys

`flatBirthday ≤ 1` always. Therefore:

> **No lower bound on birthday is derivable from the current axioms.** Any statement of
> the form `birthday x ≥ f(x)` with `f` unbounded is refuted by the flat model.

Upper bounds are unaffected — which is why `SignSequence.birthday_gonshorIn_le_omega`
(`≤ ω`) survives: it is an upper bound, proved directly from
`birthday_ofReal_le_omega`. It is true, weak, and consistent with the flat model. The
sharper `birthday (gonshorIn K s) ≤ s.length` that `Basic.lean` reserves "for future
induction proofs" is *also* an upper bound and *also* satisfied by the flat model — so
the flat model neither refutes it nor helps prove it.

This is the precise statement to carry forward: **the axioms constrain birthday only
from above, and the interesting content is all below.**

### 3. THE CORRECTION: `DiophantineBirthday` is trivially inhabited

`QOU/AppendixSurreals/DiophantineBirthday.lean` carries, in comments:

> *"**No instance is provided — that is the honest open state** (AGENTS.md §3b-tax)"*
> *"The `sorry` represents the **open conjecture** per §3b — not a missing proof."*

But the class's actual fields are

```lean
class DiophantineBirthday where
  residual : ℝ
  residual_eq_zero : residual = 0
```

**Verified in Lean: `example : DiophantineBirthday := ⟨0, rfl⟩` typechecks, exit 0.**

So the class is **trivially inhabited**, and withholding the instance encodes *nothing*.
Any downstream result taking `[DiophantineBirthday]` as a hypothesis is **unconditional
in disguise** — the hypothesis can be discharged in one line by anyone who tries.

Note the file's own docstring admits the shape is provisional — *"Field schema below is a
structural placeholder; refine per §3b to match the conjecture's actual content"* — so
this is a known-incomplete formalisation whose **epistemic labelling overstates it**. The
history comment records that an `axiom`-asserted global instance was removed as
dishonest; removing it did not achieve what the comment claims, because the class was
trivially satisfiable either way.

Note also: the class does **not** mention `birthday` in its formal content, so it is not
a victim of the vacuous axioms — it is a separate, and worse, problem.

**Fix required (not done here):** give `DiophantineBirthday` content that is actually the
conjecture — a separation statement of the form "for algebraic `α` of degree `d`, the
birthday trajectory satisfies … while for transcendental it does not" — which by §2 above
will need a **lower** bound on birthday, hence strengthened axioms. Until then the class
should be labelled a placeholder, not an open conjecture, because a reader cannot tell
the difference and the comment actively misleads.

---
**2026-08-10 (later) — reconciled with the sibling vacuity campaign.**

Merging `origin/main` brought in `docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md`
(branch `claude/issue-2472-analysis-qgqk7u`), which is directly on point and **sharpens
the `DiophantineBirthday` finding above rather than contradicting it**. Its conclusion:

> the useful test is not *"is the carrier inhabited?"* but **"is the instance
> non-degenerate?"**

with four named degeneracies that each satisfy inhabitation on a technicality: the
reflexive diagonal, the trivial index, the empty constraint index, and **"stipulates the
answer"**.

`DiophantineBirthday` is a clean instance of the last one — `residual := 0` with
`residual_eq_zero := rfl` stipulates exactly what the conjecture is supposed to assert,
the same shape their ledger marks `genuine` for
`rogers_correction_leading_h_order` (`leading_h_order := 4; … := rfl`).

**Adopt their vocabulary, not mine.** The finding is not "trivially inhabited, therefore
the label is false" — inhabitation alone is a weak discriminator, which is their point.
It is: *the only available instance is degenerate (stipulates the answer), so withholding
it encodes nothing.*

**Checked: `DiophantineBirthday` is NOT in `docs/audits/lean-vacuity-review-ledger.json`**
(178 entries, 0 birthday/diophantine hits). The campaign's queue is reported drained
(`--check-ledger` exits 0), so this is a **new entry**, not a duplicate — and it suggests
the campaign's scan did not reach `AppendixSurreals/`. Worth checking whether
`scripts/lean-carrier-inhabitation-scan.mjs` covers that directory at all; if it does not,
the "drained" status is scoped narrower than it reads.

---
**2026-08-10 — the recommended fix, built and its independence PROVED.**

`QOU/AppendixSurreals/BirthdayFaithful.lean`, sorry-free, standard axioms. This turns the
bean's "strengthen the axioms" recommendation from a suggestion into verified content,
without touching the ~38 modules that use `SurrealField`.

### §1 — the asymmetry, made concrete

`birthday_natCast_le : ∀ n : ℕ, birthday ((n:ℕ) : K) ≤ n` is **already a theorem** from
the existing axioms — induction on `birthday_one` and `birthday_add_le`, via
`nadd_one : a ♯ 1 = succ a`. No new axiom needed.

So the axioms give the `≤` and nothing gives the `≥`. That is the whole defect in one
pair of statements, and it is now visible in the corpus rather than only in this bean.

### §2 — `BirthdayFaithful`, a MIXIN not a class change

    class BirthdayFaithful (K) [SurrealField K] where
      birthday_natCast : ∀ n : ℕ, birthday ((n:ℕ) : K) = (n : Ordinal)

Opt-in, deliberately, for three reasons recorded in the module: ~38 modules use
`SurrealField` and most never mention birthdays; a mixin makes the dependency **visible**
in the hypotheses of anything that needs real birthday content; and the corpus already
demonstrates the pattern with `BlowupField`.

Combined with §1 the mixin pins `birthday n` exactly — it supplies only the missing half.

### §3 — the independence is a THEOREM, not a remark

`flatBirthday_not_faithful : ¬ (∀ n : ℕ, flatBirthday ((n:ℕ) : ℝ*) = n)` — the flat model
fails at `n = 2`, since `flatBirthday 2 = 1`.

Since `flatBirthday` **does** satisfy all six birthday axioms
(`surrealFieldHyperreal`), this proves `BirthdayFaithful` is **not derivable** from them.
Packaged as `birthdayFaithful_independent_of_surrealField_axioms`: the six axioms are
satisfiable together with the *negation* of the mixin.

Earlier entries in this bean asserted "adding the matching ≥ would kill the flat model
outright". That assertion is now checked.

### ⚠ NOT claimed

That `BirthdayFaithful` is **sufficient** to characterise Conway's birthday. It rules out
*the flat model*; it does not rule out every degenerate model, and whether the axiom set
is now categorical is open and untouched. Stated in the module so a reader cannot take
this for more than it is.

### Still open on this bean

- `DiophantineBirthday` — the separate and worse problem: its only available instance is
  degenerate (`residual := 0`, `rfl`), so its "honest open state" label is false. Not
  fixed here; needs the class to be given content that is actually the conjecture, which
  by §1–§3 above will require the mixin.
- Whether `SignSequence`'s bounds should now be re-stated over `[BirthdayFaithful K]` to
  say something non-vacuous. Not attempted.

---
**2026-08-10 — `DiophantineBirthday`: the second defect is worse than the first, and it is
about the conjecture's SHAPE.**

`QOU/AppendixSurreals/DiophantineBirthdayScope.lean`, sorry-free, standard axioms.

The degenerate-instance problem recorded earlier is real but secondary. Looking at what
the conjecture would have to *say* turned up something sharper.

### Birthday-of-the-number cannot separate algebraic from transcendental

`SurrealField`'s own axiom `birthday_ofReal_le_omega` puts **every** real — algebraic and
transcendental alike — at birthday `≤ ω`. So any separation already has to fit inside
`[0, ω]` for both classes.

In **Conway's actual surreals** it collapses entirely: the reals are exactly the surreals
born on or before day `ω`, with dyadic rationals born strictly earlier and **every other
real born exactly on day `ω`**. So

    birthday(√2) = ω = birthday(π)

— an algebraic irrational and a transcendental at the *same* birthday.

Proved here: `no_birthday_only_separation` — if two reals have equal birthday then **every**
predicate `P : Ordinal → Prop` gives the same verdict on both, so no criterion phrased in
terms of `birthday ∘ ofReal` can separate them, however cleverly chosen. Trivial to prove;
the point is what it rules out.

⚠ The Conway fact is **cited, not proved** — nothing in `SurrealField` pins the birthday
of an irrational. That is the same gap `BirthdayFaithful` closes for the naturals and
nobody has closed for the irrationals, and the module says so.

### So the conjecture's own gloss was right and its formalisation was not

The gloss says *"separated by birthday **trajectory**"*. That word is load-bearing and was
not taken literally. Liouville/Roth are about *how fast rationals approximate `α`*, which
in surreal terms is the shape of the **sign expansion** — the path `gonshor` traces — not
the ordinal it terminates at. The corpus already has that infrastructure
(`SignSequence.gonshor : List Sign → ℚ`, `gonshorIn`).

A faithful statement would compare *prefixes* — the rate at which `gonshor` on length-`n`
prefixes approaches `α` — against the Liouville exponent. **Not attempted.** This module
fixes the target, not the theorem.

### Status of the two defects

| defect | status |
|---|---|
| only available instance stipulates the answer (`⟨0, rfl⟩`) | recorded, not fixed |
| separation cannot be by birthday-of-the-number | **proved here** |
| a trajectory-level statement | open, unformalised, and now the correct target |

The class should be **relabelled a placeholder** until it carries the trajectory
statement. Its current "honest open state" comment claims an epistemic status it does not
have, in two independent ways.

---
**2026-08-15 — the trajectory statement, drafted. `DiophantineBirthdayTrajectory.lean`.**

Sorry-free, all five declarations on standard axioms. Branch
`claude/fivetwo-level7-ladder-numerators`.

The previous entry fixed the target ("a faithful statement compares *prefixes* against the
Liouville exponent") and left it unwritten. Taking it up produced two findings that change
how the whole conjecture should be read, and one honest limit.

### 1. The obstruction does NOT transfer — and it very nearly did

`no_birthday_only_separation` killed birthday-of-the-number because the criterion is
constant on the irrationals. The trajectory version faces a structurally similar threat,
and I expected it to die the same way: two reals whose sign expansions **share a tail**
differ by a dyadic rational, so any trajectory criterion must be **invariant under adding
a rational** to be well defined at all. That is exactly the kind of blanket invariance
that flattened the birthday version.

It survives, because the criterion Mathlib already has is invariant *without* being
constant:

| criterion | invariant under the ambiguity | constant on the irrationals |
|---|---|---|
| `birthday ∘ ofReal` | — | **yes** — separates nothing |
| `LiouvilleWith p` | yes (`add_rat_iff`) | **no** — separates |

Proved as `liouvilleWith_rat_shift_invariant` and `liouvilleWith_separates` (witnesses:
`liouvilleNumber 2` satisfies `LiouvilleWith 2`, `0` does not). So the redirection to
trajectories was not a change of wording — it moves to a criterion that survives the
invariance its own encoding forces.

### 2. One direction of the conjecture is ALREADY A MATHLIB THEOREM

`Liouville.transcendental` — Liouville's theorem — is in Mathlib, with
`transcendental_liouvilleNumber` as a concrete witness. Discharged here as
`liouville_trajectory_direction_settled`.

**So labelling `conj:diophantine-birthday` wholly open overstates what is open.** The
fast-approximation ⟹ transcendental direction is closed, in the corpus's own toolchain.
This is a third defect in that conjecture's labelling, independent of the two already
recorded (degenerate instance; wrong shape).

### 3. Roth does not help, and the conjecture's gloss implies it does

Worth stating because the gloss cites Roth alongside Liouville. Roth sharpens the
**settled** direction — algebraic irrationals have exponent exactly 2, so `LiouvilleWith p`
with `p > 2` already forces transcendence, improving Liouville's degree-dependent bound. It
says nothing about reals that approximate *slowly*. Citing Roth buys a better exponent on
the direction already closed, not progress on the open one.

The naive converse is named as `SlowApproximationImpliesAlgebraic` and marked **false at
every `p`** (almost every real is transcendental with exponent exactly 2). It is not
asserted, instanced, or used as a hypothesis.

### 4. A vacuity trap, shipped as a theorem so it cannot be walked into

`slowApproximation_vacuous_at_one : SlowApproximationImpliesAlgebraic 1` — **proved**.
Because `liouvilleWith_one` makes every real approximable to order 1, the hypothesis is
never satisfied and the implication is vacuous. Instantiating the target at a convenient
exponent yields a *proved Lean theorem* that reads like the conjecture and says nothing —
worse than the false version, since it carries a proof. Same failure mode as
`birthday_avg_le` and as `DiophantineBirthday`'s stipulated field.

### ⚠ What is NOT done — the actual open work

**This module does not connect `gonshor` to `LiouvilleWith`.** Nothing here proves that
`gonshor`'s length-`n` prefix value is the dyadic approximant of `α` at denominator `2ⁿ`.
That needs the induction on `GonshorState` which `SignSequence.lean` explicitly reserves
— the halving step wants a per-step birthday bound that is not among the axioms and is not
implied by them.

So the state of the conjecture is now precisely: the target is **unobstructed** (§1), part
is **already proved** (§2), Roth is a **red herring** (§3), and the surreal bridge — the
only genuinely novel content — is **unbuilt**. That is a much sharper description than
"open conjecture", which is what the corpus said.

Design note: the open content is a `def` of a `Prop`, deliberately **not** a class. A
`Prop` cannot be inhabited by stipulation, which is exactly how `DiophantineBirthday`'s
`residual := 0; rfl` went wrong.

`DiophantineBirthday.lean`'s relabelling note updated to point at all of this; the class
itself is untouched and still degenerate.

### Remaining on this bean

- The `gonshor` ↔ dyadic-approximant bridge (above). This is now the *only* thing between
  the corpus and a faithful formalisation, and it is a real piece of mathematics.
- Whether `SignSequence`'s bounds should be re-stated over `[BirthdayFaithful K]` to say
  something non-vacuous. Still not attempted.

---
**2026-08-15 (later) — the RATE half of the gonshor bridge is built.
`GonshorConvergence.lean`.** Sorry-free, 5 declarations on standard axioms.

The previous entry named the missing bridge as "the only genuinely novel content left".
Half of it turns out to be available immediately, and the reason is worth recording
because it is the same mistake this bean has caught twice before.

### The blocker did not apply, and I nearly assumed it did

`SignSequence.lean` says Gonshor's sharper `birthday ≤ s.length` is **not derivable** from
the `SurrealField` axioms: the induction wants a per-step bound on `birthday (x / 2)` — the
halving move — which is not among them. I had been reading that as blocking the bridge.

**It blocks the lift to `birthday`, not the arithmetic.** `gonshor : List Sign → ℚ` never
leaves `ℚ`, so the convergence *rate* is ordinary rational arithmetic and needs no axiom at
all:

| half of the bridge | status |
|---|---|
| rate of the rational approximants | **proved**, axiom-free |
| lifting the rate to surreal birthday | blocked, wants a `birthday (x/2)` axiom |

Conflating those is what made this look harder than it is.

### What is proved

`GonshorState.step` has two regimes: integer stepping until a bound exists, then bisection.
`Bracketed` names the bisection regime, and its load-bearing clause is
**`value = (lo + hi) / 2`** — the value is the midpoint of its own bracket. Without that
clause the new bracket `[value, hi]` has no fixed relation to the old one and nothing
halves.

- `Bracketed.step` — one sign preserves the regime and **halves the bracket**.
- `Bracketed.foldl_gap` — `n` signs give `gap₀ / 2ⁿ`.
- `Bracketed.gap_pos` — the bracket stays positive, so this is a real contraction.

That is the exponential-in-prefix-length denominator a Liouville exponent is measured
against, which is exactly what the trajectory statement needed.

### ⚠ Non-vacuity, because everything above is conditional on `Bracketed`

If no reachable state satisfied `Bracketed`, all of it would be vacuously true — the
degeneracy `docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md` catalogues, and
the same failure this bean already found in `DiophantineBirthday` and in
`slowApproximation_vacuous_at_one`. **Three times now in one bean's territory**, so it is
checked rather than assumed:

- `bracketed_plus_minus` — `[+, -]` reaches the regime (`+` steps to 1 unbounded above,
  `-` then finds `hasLo` and bisects to `1/2` inside `(0, 1)`).
- `gap_after_plus_minus` — concretely, `[+, -] ++ l` leaves a bracket of width `2^-|l|`.

Computed values confirm it independently: gap `1 → 1/2 → 1/4` over `[+,-]`, `[+,-,+]`,
`[+,-,+,-]`.

### ⚠ What is still missing, and it is NOT more of the same

The rate is about `gonshor`'s **own** bracket. Turning it into `|α − …|` needs the sign
sequence to be *the sign expansion of a given `α`* — a map `ℝ → (ℕ → Sign)` that
`SignSequence.lean` **does not define**. Until it does, there is no `α` in the statement to
approximate. That is a construction, not a lemma, and it is now the next real step.

The birthday lift remains blocked as described above.

### Trap recorded

`simpa [hg, …] using h` failed where `rw [hg] at h; simpa using h` works: `simpa`
normalises the `foldl` on both sides *first*, after which `hg`'s literal
`[Sign.plus, Sign.minus].foldl` no longer matches anything. Rewrite with a specific
equation **before** letting `simp` normalise the term it mentions.

`DiophantineBirthdayTrajectory.lean`'s §3 note updated to say precisely which half is built.

---
**2026-08-15 (later still) — the bridge is BUILT. `expansion_approximates`.**

The entry above said the missing piece was "a map `ℝ → (ℕ → Sign)` that `SignSequence.lean`
does not define — a construction, not a lemma", and predicted it would be real work. It was
about two hours of it, and it is done:

```lean
expansion_approximates (α : ℝ) (n : ℕ) (hb : Bracketed (expandState α n)) (k : ℕ) :
  |α − ((expandState α (n + k)).value : ℝ)| ≤ ((expandState α n).gap / 2 ^ k : ℚ)
```

For **any** real `α`. Ten declarations, sorry-free, all standard axioms.

### The construction

`expandState α` is the greedy rule, which is `GonshorState.step` read backwards: emit `+`
when the current value undershoots `α`, `-` otherwise. Noncomputable, because comparing a
real to a rational is not decidable — that is a fact about `ℝ`, not a weakness of the
construction.

- `expandState_brackets` — the expansion **brackets `α` at every step**, for every real.
  Proved by induction; the base case is vacuous (no bounds set) and each step
  re-establishes the invariant *by construction*, since `+` moves the lower bound to a
  value known to undershoot and `-` moves the upper bound to one known not to.
  Deliberately **weak** inequalities, so a rational `α` landing exactly on a bound is
  covered rather than excluded.
- `dist_le_gap` — bracketing plus the bisection regime gives `|α − value| ≤ gap`, because
  both `α` and `value` lie in `[lo, hi]`.
- `expandState_gap` — the connecting lemma. `Bracketed.foldl_gap` is stated for
  `List.foldl` while `expandState` recurses on `ℕ`; they join through `Bracketed.step`
  directly, with **no list bookkeeping**, because `expandState α (n+1)` is literally one
  `step` applied to `expandState α n`. I expected this to be the fiddly part and it was
  three lines.

### ⚠ Non-vacuity, a fourth time

Every statement here is conditional on `Bracketed`, and `Brackets` is two implications
*guarded* by `hasLo`/`hasHi`. Unexhibited, the whole section would hold vacuously.
`expandState_half_bracketed` and `expandState_half_flags` settle it on `α = 1/2`: step 0
has value `0 < 1/2` so emits `+`, reaching `1` with a lower bound only; step 1 has value
`1`, which does not undershoot, so emits `-`, finds `hasLo`, and bisects into `(0, 1)`.
The headline was also instantiated at that `α` to confirm the hypothesis is dischargeable.

That is **four** vacuity checks this bean's territory has now required
(`DiophantineBirthday`'s stipulated field, `slowApproximation_vacuous_at_one`,
`Bracketed`, `Brackets`). At this point it should be treated as the default failure mode
for anything in this area, not a precaution.

### What remains

1. **The birthday lift** — still blocked, and now clearly the *only* structural blocker.
   `SignSequence.lean`: Gonshor's `birthday ≤ s.length` is not derivable from the
   `SurrealField` axioms because the halving step wants a `birthday (x / 2)` bound that is
   not among them. It never blocked the rational-side rate, which is why the bridge could
   be built at all.
2. **The Liouville comparison itself** — nothing yet compares `expansion_approximates`'
   rate against `LiouvilleWith`. That is exponent bookkeeping over existing pieces, not new
   infrastructure, and is the natural next increment.

`DiophantineBirthdayTrajectory.lean`'s §3 updated: it no longer claims the bridge is
missing, and names precisely what is.

---
**2026-08-15 — the Liouville mechanism, and a correction to my own "next step is bookkeeping".**

I said the Liouville comparison would be "exponent bookkeeping over existing pieces, not new
infrastructure, so I'd expect it to go quickly". **Half right.** The mechanism was quick;
the bookkeeping it needs turns out not to exist yet, and that is the more useful finding.

### ⚠ First, a trap the bracket rate sets

`expansion_approximates` gives error `gap / 2ᵏ` at a state whose denominator has *also*
grown by `2ᵏ`. That is error `≈ 1/q` — approximation **exponent 1** — and
`LiouvilleWith.liouvilleWith_one` gives exponent 1 for **every** real for free. So the
bracket rate on its own **certifies nothing about any Liouville exponent**, and it would be
very easy to read the previous entry's result as progress toward one. It is not; it is the
denominator, not the discriminator.

### Where the exponent actually lives: runs

A `+` step keeps `hi` and raises `lo`; a `-` keeps `lo` and lowers `hi`. So a **run of `k`
identical signs freezes one endpoint** while the bracket keeps halving. Proved:

```lean
run_plus_approximates (k : ℕ) (hb : Bracketed st)
    (hbr : Brackets α ((List.replicate k Sign.plus).foldl GonshorState.step st)) :
  |α − (st.hi : ℝ)| ≤ ((st.gap / 2 ^ k : ℚ) : ℝ)
```

`st.hi` is fixed **before the run begins**. So the denominator is whatever it already had,
while accuracy improves by `2ᵏ` — error `1/q^{(n+k)/n}` rather than `1/q`. That decoupling
of accuracy from denominator *is* what an approximation exponent above 1 means, and it is
supplied by the run structure rather than by the bisection rate.

Supporting: `step_plus_hi` (a `+` leaves `hi` alone) and `foldl_replicate_plus_hi` (a run
preserves both `hi` and the bisection regime).

### ⚠ What a real `LiouvilleWith` instance still needs — and it is NOT bookkeeping

`LiouvilleWith p x` is `∃ C, ∃ᶠ n in atTop, ∃ m : ℤ, x ≠ m/n ∧ |x − m/n| < C/n^p`. To
produce one from the above I need `st.hi` **as `m/q` with `q` known as a function of the
step count**. `GonshorState` records `lo`, `hi`, `value` as bare `ℚ` and **tracks no
denominator at all**. So the missing piece is a denominator invariant — something like
"after `n` steps every bound is a dyadic with denominator dividing `2ⁿ`" — which is a new
induction over `step`, not a rearrangement of existing lemmas.

That is a genuine correction to my estimate: the pieces I said were all present were not.

### Trap recorded

`linarith` **cannot divide**. Given `hg : st.hi − lo_k = (st.hi − st.lo) / 2 ^ k` and a goal
mentioning `st.gap / 2 ^ k`, it treats the two quotients as unrelated atoms even with
`st.gap = st.hi − st.lo` in context — because folding that identity in requires dividing.
`simp only [GonshorState.gap]` had helpfully unfolded the *right* side too, creating the
mismatch. Fix: `rw [← hgd] at hg` to fold the subtraction back into `gap` **before** calling
`linarith`. Same shape as the earlier `simpa`-normalises-first trap: a tactic that
canonicalises both sides can destroy the very match a later step depends on.

### Standing

13 declarations in `GonshorConvergence.lean`, sorry-free, all standard axioms.

---
**2026-08-15 — the denominator invariant, which the entry above named as the blocker.**

`expandState_dyadic (α : ℝ) (n : ℕ) : DyadicState n (expandState α n)` — **every bound of
`α`'s expansion after `n` steps is a dyadic with denominator dividing `2ⁿ`.** Sorry-free,
standard axioms. 23 declarations in `GonshorConvergence.lean` now.

That was the piece the previous entry identified as missing and (correctly) said was a new
induction rather than bookkeeping. Both regimes preserve it for different reasons: the
unbounded `±1` moves keep the denominator exactly, and the two bisecting moves average two
level-`n` dyadics, landing at level `n + 1`.

Combined with `run_plus_approximates`, the corpus now has the Liouville-shaped statement
with a **named denominator**:

    |α − m/2ⁿ| ≤ gapₙ / 2ᵏ        after a run of k signs at step n

— accuracy `2⁻ᵏ` better against a denominator fixed at `2ⁿ`.

### ⚠ Trap: state the invariant multiplicatively, not as a quotient

`IsDyadicAt n x := ∃ m : ℤ, x = m / 2ⁿ` is the natural reading and it **defeats `ring`**.
Closing the step cases then needs `2ⁿ / 2ⁿ = 1`, which `ring` cannot do without knowing
`2ⁿ ≠ 0`, so all twelve subgoals would want `field_simp` plus a side condition. Restated as

    IsDyadicAt n x := ∃ m : ℤ, (2 : ℚ) ^ n * x = m

every case is a plain `linear_combination` over `ring`. Measured: the quotient form failed
on the two unbounded cases with "the `ring` tactic failed to close the goal"; the
multiplicative form went through on the first attempt.

This is the third tactic-shape trap in this bean and they share a moral — **`ring`,
`linarith` and `simp` all fail on division in their own way** (`ring` cannot cancel,
`linarith` cannot divide at all, `simp` normalises the quotient into a shape a later `rw`
no longer matches). Keep denominators out of statements that tactics have to close.

### What remains for an actual `LiouvilleWith` instance

The pieces are now genuinely all present, and what is left is a **quantifier**, not
infrastructure. `LiouvilleWith p x` needs `∃ᶠ n in atTop` — *infinitely many* `n` with a
run long enough to beat exponent `p`. That is a property of the particular `α`'s expansion,
not something derivable in general: for an algebraic irrational Roth says the runs are
bounded, and for a Liouville number they are not. So the honest next statement is
conditional —

> if `α`'s expansion has runs of length `≥ (p−1)·n` infinitely often, then `LiouvilleWith p α`

— and proving *that* hypothesis for any specific `α` is the hard number theory the
conjecture was always about. **The formalisation gap is now closed; the mathematics gap is
where it always was.** That is worth stating plainly, because the bean's original framing
suggested the surreal side was the obstacle, and it is not.

The birthday lift is unchanged and still blocked (`SignSequence.lean`'s missing
`birthday (x/2)` bound).

---
**2026-08-15 — "should the remaining input be a conjecture?" Asked, and the answer is NO —
it is a 1955 theorem.**

I had been calling the last gap "the undischargeable number theory", which invites
recording it as a conjecture class. Checked before doing so, and it is the wrong move.

**The remaining input is Thue–Siegel–Roth** (Roth 1955, Fields Medal): an algebraic
irrational has approximation exponent exactly `2`, hence is not approximable to any order
`p > 2`. That is settled mathematics. Recording it as a conjecture would label a proved
theorem as open — **the same class of error this bean exists to correct**, and it would be
the *fourth* epistemic mislabeling attached to `conj:diophantine-birthday`, after:

1. "no instance is provided — that is the honest open state", which encoded nothing;
2. a separation that was impossible as stated;
3. a direction already proved in Mathlib.

So it is stated as an explicit **hypothesis**, `RothExponent`, with the label saying
"known theorem, not formalised in Mathlib". Consequences take it as an argument:

```lean
roth_separates (hR : RothExponent) :
  (∀ α : ℝ, IsAlgebraic ℚ α → Irrational α → ¬ LiouvilleWith 3 α)
    ∧ LiouvilleWith 3 (liouvilleNumber 2)
```

Conditional on Roth, `LiouvilleWith 3` is a **genuine separator** — it fails on every
algebraic irrational and holds on an exhibited transcendental. The second conjunct is
unconditional, straight from Mathlib. Contrast `no_birthday_only_separation`, where the
criterion provably *cannot* take different values.

### ⚠ A name collision that answers the wrong question

Mathlib **does** contain `Mathlib/Combinatorics/Additive/Corner/Roth.lean`, proving
**"Roth's theorem"** — the additive-combinatorics one about three-term arithmetic
progressions. Unrelated result, same name. Thue–Siegel–Roth appears in Mathlib only as a
docstring aside in `LiouvilleWith.lean`.

**So "is Roth in Mathlib?" returns yes by name and no in fact.** Anyone pricing this work
by grepping for the name will conclude the input is available. It is not.

### Also corrected: the exposition block said the wrong thing

`diophantine-birthday-trajectory.md` read that what remains is "the hard Diophantine
mathematics the conjecture was always about" and that it needs "proving it for any
particular `α`". Both wrong in the same direction — Roth already covers *every* algebraic
irrational, so no per-`α` work is needed and the mathematics is not the obstacle. Block
updated to say the missing thing is a formalisation, and to record the name collision.
Validator baseline unchanged at 42.

`RothExponent` is deliberately a `def` of a `Prop`, not a class — a `Prop` taken as a
hypothesis cannot be discharged by stipulating a field, which is exactly how
`DiophantineBirthday` went wrong.

---
**2026-08-16 — the run assembly, done; plus an independence statement that was weaker than
its name.**

### 1. `expansion_run_approximates` — the assembly I had called "bookkeeping"

```lean
expansion_run_approximates (α : ℝ) (n k : ℕ)
    (hb : Bracketed (expandState α n))
    (hrun : ∀ j < k, ((expandState α (n + j)).value : ℝ) < α) :
  ∃ m : ℤ, |α − (m : ℝ)/2ⁿ| ≤ ((expandState α n).gap / 2ᵏ : ℚ)
```

For a **given** real, an **explicit** rational, denominator fixed by `n`, accuracy set by
the run length `k`. That is the Diophantine shape, and it is the first statement in this
lane where all three earlier pieces (accuracy, denominator, run) actually meet.

Two bridging lemmas were needed and neither was hard: `expandState_succ_plus` (a step whose
value undershoots `α` *is* a `+` step — the definition of the greedy rule) and
`expandState_plus_run` (a window of undershoots is a `List.replicate k Sign.plus` fold,
which is the shape `run_plus_approximates` consumes).

### ⚠ 2. Vacuity check number five — and this one had real teeth

`expansion_run_approximates` is conditional on the run hypothesis. **At `k = 0` that
hypothesis is vacuously true** and the theorem degenerates to `dist_le_gap`. So all of the
content is in whether a *positive* `k` is ever satisfied.

`expandState_nineTenths_runs`: `α = 9/10` reaches the bisection regime at step 2 and then
undershoots twice (`1/2`, `3/4` both below `9/10`), so the expansion emits `+` twice more.
`nineTenths_run_approximates` instantiates the headline there, discharging **every**
hypothesis — which is what makes it applicable rather than merely true.

### ⚠ 3. `birthdayFaithful_independent_of_surrealField_axioms` did not say what it is named

Reading it via `#check` while wiring an exposition block:

```
(∃ x, True) ∧ ¬∀ (n : ℕ), flatBirthday ↑n = ↑n
```

My first reading — that the left conjunct is vacuous — was **wrong**: the pretty-printer
elides the binder type, and the source says `∃ _ : SurrealField.{0,0} ℝ*, True`, which does
assert the axioms are satisfiable on `ℝ*`.

**But the real defect is next to it.** The two conjuncts are **not linked**. The first says
*some* `SurrealField` structure exists on `ℝ*`; the second says `flatBirthday` fails the
mixin. Nothing says these concern the **same** structure — read literally, an unrelated
witness for each half satisfies it, and that is not independence.

Added `birthdayFaithful_independent_witnessed`:

```lean
∃ S : SurrealField.{0,0} ℝ*, ¬ ∀ n : ℕ, S.birthday ((n : ℕ) : ℝ*) = (n : Ordinal)
```

**One** structure, satisfying all six axioms, whose *own* birthday fails the mixin. The
proof is unchanged — `surrealFieldHyperreal.birthday` **is** `flatBirthday` by definition —
so the content was always present and only the statement was loose. Worth tightening rather
than commenting: a reader checking the theorem, not the field assignment, could not have
known. The old form is kept so nothing downstream breaks.

This is the seventh loose or degenerate statement this bean's territory has produced. The
pattern is now unmistakable: in this area, **read the statement, not the name**.

---
**2026-08-16 — the run becomes an EXPONENT. `approx_exponent_of_run`.**

```lean
approx_exponent_of_run (α : ℝ) (n k t : ℕ)
    (hb : Bracketed (expandState α n)) (hg : (expandState α n).gap ≤ 1)
    (hrun : ∀ j < k, ((expandState α (n + j)).value : ℝ) < α) (hk : n * t ≤ k) :
  ∃ m : ℤ, |α − (m : ℝ)/2ⁿ| ≤ 1 / (2ⁿ)ᵗ
```

The Diophantine form outright: an explicit rational of denominator `q = 2ⁿ` with error at
most `1/qᵗ`. **The run length measured against `n` is what supplies `t`** — `k ≥ n·t` is the
whole content, and it is why the bisection rate alone can only ever give `t = 1`.

30 declarations in `GonshorConvergence.lean`, sorry-free, all standard axioms.

### `gapₙ ≤ 1` is a hypothesis, deliberately

It is always true at the first bracketed step: an unbounded `+` sets `lo := value` and
`value := value + 1`, so the following `-` bisects an interval of width exactly `1`, and
every later gap is smaller. Proving *"the first bracketed step"* needs an induction on when
the bounds first appear — a separate lemma the statement does not need. Taken as a
hypothesis and discharged at the witness by `norm_num`.

### ⚠ The witness only reaches `t = 1`, and that is the honest limit

`nineTenths_exponent_one` discharges every hypothesis at `n = 2, k = 2, t = 1`. But `t = 1`
is the exponent **every** real has for free — `9/10` is rational and has no long runs to
give more. So the witness shows the theorem *applies*; it does not show this `α` is
interesting.

A witness with `t ≥ 2` needs a real chosen for its run structure, and exhibiting one is the
Diophantine work this lane deliberately does not attempt. Recorded because a reader could
otherwise take a proved `t = 1` instance as evidence the machinery detects something, when
`liouvilleWith_one` already gives that for nothing — the same trap the bracket rate sets,
one level up.

### Trap: `gcongr` closes more than expected

`gcongr` discharged **both** side conditions (`1 ≤ 2`, and `n·t ≤ k` from context), so
supplying them as follow-up bullets failed with **"No goals to be solved"**. Identical
shape to the cofactor-`0` case in the gluing generator: a tactic that closes more than
anticipated reads as a broken proof rather than a finished one. Also cost one cycle to a
guessed lemma name (`div_le_div_of_nonneg_right'`, which does not exist) — `gcongr` is the
robust move for monotonicity goals precisely because it removes the guessing.

### What is left for a literal `LiouvilleWith p α`

Only the quantifier now: `∃ᶠ n in atTop` needs *infinitely many* `n` carrying a run of
length `≥ n·t`, plus the `α ≠ m/q` clause (which wants `α` irrational). Both are properties
of the individual `α` — precisely the Thue–Siegel–Roth territory recorded above, and not
reachable by more machinery.

---
**2026-08-16 — THE BRIDGE IS CLOSED. `liouvilleWith_of_frequent_runs`.**

```lean
liouvilleWith_of_frequent_runs (α : ℝ) (t : ℕ) (hirr : Irrational α)
    (hfreq : ∀ N, ∃ n ≥ N, Bracketed (expandState α n) ∧ (expandState α n).gap ≤ 1
                ∧ ∀ j < n * t, ((expandState α (n + j)).value : ℝ) < α) :
  LiouvilleWith (t : ℝ) α
```

The trajectory picture's central assertion — **run structure in the sign expansion controls
the Diophantine exponent** — is now a proved implication rather than a slogan, and it is
stated in **Mathlib's** vocabulary, so the lane's claim is checkable against the literature
instead of only internally consistent.

Chain, end to end, all sorry-free on standard axioms:

| step | statement |
|---|---|
| bracket halves per sign | `Bracketed.step` |
| expansion of a real brackets it | `expandState_brackets` |
| bounds are dyadic over `2ⁿ` | `expandState_dyadic` |
| a run freezes an endpoint | `run_plus_approximates` |
| run of `n·t` ⟹ exponent `t` | `approx_exponent_of_run` |
| **frequent runs ⟹ `LiouvilleWith t`** | **`liouvilleWith_of_frequent_runs`** |

`Irrational α` is not a technicality: a rational `α` eventually **is** one of its own dyadic
approximants, and `LiouvilleWith`'s `x ≠ m/n` clause excludes that case by definition.

### ⚠ What this is and is not

It is a **bridge**, not a decision procedure. The hypothesis quantifies over infinitely many
`n`, which is `LiouvilleWith`'s own `∃ᶠ` and cannot be removed — whether a given `α`
satisfies it is a fact about that `α` (bounded runs for an algebraic irrational by
Thue–Siegel–Roth, unbounded for a Liouville number). **No amount of further machinery
reaches it**, which is the same wall recorded two entries above and not a new one.

### A placement correction

First written into `GonshorConvergence.lean`, which does not import the Liouville files —
`Unknown identifier LiouvilleWith`. Moved to `DiophantineBirthdayTrajectory.lean`, which
already had them, with `GonshorConvergence` added as an import. Better architecturally too:
`GonshorConvergence` stays about the expansion machinery and dependency-light, and the
Liouville statement lives beside the other Liouville statements.

The exposition block was updated to state the implication; it previously stopped at the
decoupling and left the conclusion implicit.

**The formal lane is complete.** What remains is Thue–Siegel–Roth, which is a formalisation
project of its own, not an increment here.

---
**2026-08-16 — the `DiophantineBirthday` sub-finding is CLOSED upstream, by `qou-ffwk`.**

Merging `origin/main` (`cbb49a1a35`) into `claude/fivetwo-level7-ladder-numerators`
brought in `f92876c99c` (*"ffwk: make DiophantineBirthday assert something"*, #5238),
which is the *"Fix required (not done here)"* named above, done. The class is now

```lean
class DiophantineBirthday (trajectory : ℝ → ℕ → ℕ) : Prop where
  algebraic_logarithmic :
    ∀ α : ℝ, IsAlgebraic ℚ α →
      ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 1 ≤ n → (trajectory α n : ℝ) ≤ C * Real.log n + C
```

— the trajectory is a parameter rather than something the class picks, so the
"stipulates the answer" degeneracy is gone, and `not_of_quadratic` **refutes** the class
at `fun _ n => n ^ 2`, which is the property the old schema could not have: under it no
choice of anything could fail. `nonempty_of_const_zero` records that it is not
over-corrected into emptiness. Neither is an `instance`, so nothing discharges a
downstream `[DiophantineBirthday]` by resolution.

It also took the redirection this bean argued for: the separation is not by the birthday
of the number (finding 2 below, `DiophantineBirthdayScope.no_birthday_only_separation`) —
`trajectory` enters as caller-supplied data precisely because nothing in the library
constructs it from the birthday.

**Scope of this closure.** Only the `DiophantineBirthday` sub-finding closes. This bean's
main claim — that the six `SurrealField` birthday axioms admit the two-valued
`flatBirthday` model, so birthday-derived results prove less than they read as — is
untouched and stays `in-progress`.

Stale prose corrected in the same integration: `DiophantineBirthdayScope.lean` §1 and
`DiophantineBirthdayTrajectory.lean` §3 both described the old field schema in the
present tense.
