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
