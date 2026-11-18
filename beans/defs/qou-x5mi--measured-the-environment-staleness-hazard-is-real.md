---
# qou-x5mi
title: 'MEASURED: the environment staleness hazard is REAL here — 4 producers do not reproduce in this container'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T19:45:51Z
updated_at: 2026-10-04T15:21:33Z
parent: qou-5vkl
---

Parent: qou-fl0a. Found trying to declare `q0Anchor: comparison` on the five
two-pin producers — a LABEL change requiring a re-run to take effect. The
re-runs were contaminated, so the tranche is blocked on the environment, not on
any ruling.

## AGENTS.md says this class is unconfirmed. It is now confirmed.

The witness-staleness section reads: *"Environment (hazard, not yet measured
here). A producer MAY branch on what is installed. I originally reported the
binding_canonical 48 % as an instance of this; that was wrong ... this corpus
has not yet produced a confirmed case."*

Here is a confirmed case, four of them, measured 2026-08-29 by re-running each
producer with NO source change and diffing against its committed witness.

## The gap

    committed witnesses   mpmath 1.3.0   (environment block)
    this container        mpmath 1.4.1
    plus: pyhecke_native_build 47b406d9ba6e343f -> 825fe60e51bf0442

## What moved

  qbeta_ck_basis_constrained_pslq
      c3_reproduced_canonical
        committed  -2.02018812814143945582016855395
        re-run     -974.382476607697851630950275826
      Not a precision shift. A different number, and one that would have
      replaced the corpus's c_3 readout.

  qbeta_habiro_integrality_kill_test
      an assertion flipped  passed: true -> FALSE
        computed  1.8111358157653425e-71  ->  2.280110649365846e-12
      59 orders of magnitude, and the witness would have landed asserting its
      own failure.

  tau_dictionary_hauptmodul_validator   pyhecke_native_build changed
  tau_dictionary_fricke_spin_probe      pyhecke_native_build changed

So at least TWO independent environment axes (mpmath minor version; the native
build), and I am NOT claiming which one causes which move — only that a re-run
here does not reproduce the committed values.

## The near-miss, which is the point

Every one of these was a one-line LABEL change. Adding `q0Anchor: comparison`
alters no arithmetic. But a label declared at the producer only reaches the
witness through a re-run, and the re-run brings the whole environment with it.
I was one `git add` from committing a -974 where the corpus has -2.02, and a
flipped assertion, inside a commit whose message would have said "declare the
anchor".

GENERALISES: **a producer-side declaration is not a cheap change.** It costs a
full re-run and inherits every environment difference. Prefer the manifest route
where the value permits it (muon/proton), which needs no re-run at all. Reserve
producer-side declarations for the values only a producer can assert
(`independent`, `comparison`, `ambiguous`) — and then verify the re-run's diff
field by field before staging, not just the anchor you were aiming at.

## Consequence for qou-fl0a

The four `comparison` declarations and the one `proton` manifest move are
CORRECT (determination recorded in qou-fl0a) but CANNOT BE LANDED FROM THIS
CONTAINER. They need an environment matching the committed witnesses — mpmath
1.3.0 and the 47b406d9ba6e343f native build — or a deliberate decision to accept
the new numbers, which is a separate question from labelling and would need the
moved values understood first.

Also note qbeta_ck_qholonomic_recurrence_test is BROKEN ON MAIN independently of
all this: `TypeError: cannot create mpf from None` at :359, `ext[f"c_{k}"]` is
None. Verified by running main's version with my patch stashed. It cannot be
re-run at all, in any environment, until that is fixed.
