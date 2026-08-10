---
# bday
title: 'Audit what the birthday axioms actually establish — they admit a two-valued model'
status: todo
type: task
priority: high
tags:
    - lean
    - surreals
    - axiom-audit
    - stale-claim-corrected
parent: hypr
created_at: 2026-08-10T01:35:00Z
updated_at: 2026-08-10T01:35:00Z
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
