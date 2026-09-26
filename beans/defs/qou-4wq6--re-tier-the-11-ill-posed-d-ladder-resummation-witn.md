---
# qou-4wq6
title: Re-tier the 11 ill-posed D-ladder resummation witnesses as scope-(b) closed
status: completed
type: task
priority: normal
created_at: 2026-08-21T14:41:55Z
updated_at: 2026-08-21T14:56:55Z
---

## Why this is untracked

`docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md` §6
adjudicated all 29 D-ladder / Borel witnesses and prescribed the fix:

> Re-tier them as **scope-(b) closed / ill-posed** rather than scope-(a)
> negative, so the next reader does not read "gate fails, needs more terms" as
> an open lever. That re-tiering is a registry edit and is **not made here**;
> it is tracked on bean `qou-qb8e`.

It is **not** tracked on `qou-qb8e` — that bean is "HH^1 carrier: the MAGNITUDE
channel", a different object. So the prescribed edit has no owner. Verified
2026-08-21: no bean mentions "ill-posed" or "re-tier"; no registry carries the
tier for these 11.

## The 11 (audit §6 list B)

ecalle-acceleration, ecalle-phib-resummation, single-instanton-extraction,
fibre-branch-stokes-ambiguity, fibre-two-action, jackson-qborel-acceleration,
qborel-leroy-resummation, parity-split-resummation,
parity-odd-singularity-even-order, barodd-borel-pade-laplace,
parity-adjudication.

Do **not** delete them (§6): they are the evidence the resummation arm was
pursued and exhausted, and their input (the exact `d_k`, k<=21) is live. Also
do not touch list A (6 unaffected: non-holonomicity, 2-adic grading), C (1
partial) or D (4 not assessed — deformed meridian / odd-channel Stokes, a
DIFFERENT object; Phi_b itself is genuinely resurgent, only `D(u)` is not).

## The cost that has to be decided first

Witness JSONs are machine-generated, so the only durable annotation point is
the producer docstring — and a comment-only producer edit drifts `scriptHash`,
flagging all 11 self-stale and inviting re-runs that cannot change a number
(AGENTS.md idle-backlog policy names this exact false-positive class). Options:
(a) a registry/ledger row that names the 11 and points at §6, no producer edit,
no drift; (b) producer docstring headers, accepting the drift, re-running each
(these are k<=21 exact-rational probes, cheap); (c) leave as-is and rely on §6.

Recommend (a). Four of the 11 came from my own arc (PRs #3818, #3857), whose
audit docs were corrected in #5347 — the witness layer is the remaining half.


## RESOLVED 2026-08-21 — option (a) executed

Ledger row landed in `docs/coordination/1ppq-qbeta.md`:

1. New §"Resummation arm — CLOSED (the D-ladder is convergent)", placed
   immediately **before** §"Open probes (current queue)" so it is read before
   anyone picks the next probe. Names all 11 as scope-(b) closed / ill-posed,
   states why their recorded failures are not obstructions, and carries the
   do-not-widen boundaries (6 arithmetic witnesses unaffected;
   extension-singularity's k=31 data stands; deformed-meridian / odd-channel
   Stokes not assessed; Phi_b genuinely resurgent, only D(u) is not).
2. Correction banner on the 2026-07-17 (PR #3818) sessions-log entry, which
   stated its results "conditional on the triple-confirmed divergence class"
   and framed A ~ 0.236 as a lever awaiting ORD-63 — both now scoped.

No producer touched, so no `scriptHash` drift and no spurious self-staleness
on the 11. No witness edited. Audit §6 remains the full classification.
