---
# qou-4cu3
title: 'EPIC: the q-integer convention axis — Gaussian bracket vs classical (q^n-1)/(q-1), and qInt naming both'
status: in-progress
type: epic
priority: normal
created_at: 2026-10-10T07:55:43Z
updated_at: 2026-11-18T07:54:48Z
parent: qou-10v9
---

## Why this epic exists

Split out of `qou-cdx1` on 2026-10-10 (bean `qou-am5t`, the C->D re-audit).

`qou-cdx1` is the **2026-08-15 three-ruling milestone**: R1 convention D
canonical / C excised, R2 proton pin canonical, R3 colour weighting canonical.
The q-integer question is none of those three. It is a *different convention*
that happens to share the word:

- the **Gaussian bracket** `[n]_q = (q^n - q^-n)/(q - q^-1)`, the q-deformation
  the Hecke/Markov layer uses;
- against the **classical** `(q^n - 1)/(q - 1)`, which appears in this corpus
  under the names `q_int` / `qint` / `qInt`.

Four beans were filed under the convention milestone because of that shared
word, and their presence is part of why the Markov-parameter question read as 57
beans deep when its live surface is one producer plus one research question.

## Children moved here

| bean | claim |
|---|---|
| `qou-qint` | `qInt` names TWO conventions — 8 definitions to reconcile |
| `qou-gl58` | 30 files use the classical form under `q_int`/`qint` names; its own worked note measures **0 of 363** files carrying both, i.e. no internal inconsistency found |
| `qou-b8vx` | coverage gap: 208 of 366 definitions are not symbolically evaluable |
| `qou-6p3b` | qfac/dim_q threading — 12 decisions, not 133 edits |

## What is NOT in scope

The Markov parameter `z` (convention C vs D) — that is `qou-cdx1` / `qou-cds1`,
and its measured state is
[`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md).
Keep the two apart: conflating them is the defect this epic exists to undo.

## Status

`todo`, unclaimed. No measurement taken here beyond the re-parenting — the four
children carry their own evidence, and `qou-gl58`'s "0 of 363 carry both" is the
most load-bearing figure among them and is worth re-measuring before anyone
plans work off it.

## Round 84 Progress (PR #8393)
- Branch: `feat/round84-colourdisc-fixedratio-comptrace-zeroslope-equidcap-43c1`
- Commit 1 (code + probe): `02a557115ca6d2779725ccfdca969ee6ef80dff4`
- Commit 2 (witness): `f21ac2e565e6a27158e92746366f1616c0d9fd98` (`scriptSha256 = 930736b7600cb1fb1ca87062021ff390088ea82549e2ac7bf6e2fad10cdf9749`)
