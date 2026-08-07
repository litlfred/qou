---
# qou-8p1c
title: 'qou-8pl1/c: period-matrix route — BLOCKED on infra, requirements recorded'
status: todo
type: task
created_at: 2026-08-07T00:00:00Z
updated_at: 2026-08-07T00:00:00Z
---

Parent: `qou-8pl1`. The decisive route, and the expensive one.

## The computation

Compute the period matrix of the pinched Bring surface's normalization and match
it against the Klein quartic's known period matrix (equivalently, compare points
in the genus-3 Siegel upper half-space modulo Sp(6,Z)). This SETTLES the
conjecture either way — confirm or refute — where the discrete invariants of
`qou-8p1b` can only ever give necessary conditions.

## Infra status in this sandbox (probed 2026-08-07) — BLOCKED

| package | status |
|---|---|
| `sympy` | **installs** (1.14.0 via pip) — symbolic only, no period machinery |
| `numpy` | absent, not installed by pip in this environment |
| `scipy` | absent |
| `abelfunctions` | **not on PyPI at all** — GitHub-only (`abelfunctions/abelfunctions`), and it requires numpy + scipy + Cython |
| `sage` | absent; not pip-installable |

So the period route **cannot run here as-is**. Do not attempt it without first
resolving the stack.

## What would unblock it

Roughly in increasing order of effort:

1. Get `numpy` + `scipy` installed, then clone `abelfunctions` from GitHub
   (egress to github.com is available) and build its Cython extensions.
   `abelfunctions` computes Riemann matrices of plane algebraic curves directly,
   which is exactly the primitive needed.
2. A Sage environment (Docker or conda). Sage has
   `RiemannSurface` / `period_matrix` natively and would make this a short
   script, but installing Sage in this sandbox is a project in itself.
3. Hand-roll it: numerical integration of a basis of holomorphic differentials
   over a homology basis. Feasible in mpmath (which IS available) but the
   homology-basis bookkeeping for a pinched genus-4 → genus-3 degeneration is
   error-prone and is really what `abelfunctions` exists to handle.

## Recommendation

**Do `qou-8p1a` and `qou-8p1b` first.** They need no stack, and if the
competitor set turns out to be small and a cheap discrete invariant separates
it, the period computation may never be necessary. Only escalate here if the
discrete invariants prove insufficient.
