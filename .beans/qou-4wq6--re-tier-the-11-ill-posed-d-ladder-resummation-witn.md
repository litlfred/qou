---
# qou-4wq6
title: Re-tier the 11 ill-posed D-ladder resummation witnesses as scope-(b) closed
status: todo
type: task
priority: normal
created_at: 2026-08-21T14:41:55Z
updated_at: 2026-08-21T14:42:32Z
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
