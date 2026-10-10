---
# qou-5843
title: Reduce c_3 Faddeev contour integral to combinatorics via tetraplectic form
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-07T19:14:43Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

That is a profound insight. If we can apply the same tetraplectic form machinery to the Faddeev modular double contour integral for c₃, we can completely bypass the need for brute-force numerical quadrature or analytic limits.

By reducing the contour integral to combinatorics—just as was done for that other integral—we map the continuous complex analysis problem directly into the discrete algebraic domain (like Kashiwara crystal operators, quantum integer combinations, or Hecke algebra traces). This means the "arbitrary precision numerical evaluator" wouldn't be a floating-point integration script at all; it would be an exact algebraic combinatorial expansion that we can compute cleanly in Python and formally prove in Lean.

Goal: Find the tetraplectic combinatorial reduction for the c₃ Faddeev contour integral.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: SUPERSEDED.** The reduction supplies the e_k coefficients and does not supply c_3: the argument map z(q0) is the remaining piece (see 82w7/qiw9). The general-k closed form is verified as series only for k≤6 and is not in Lean. Scrap as superseded by qou-0gdn and qou-82w7.

Evidence: `qou-0gdn` (completed) plus `docs/audits/2026-07-11-phib-lean-route-memo.md` chose the combinatorial/product route. The structural reduction landed: `QOU/QBeta/EkParitySplit.lean` (generic σ-projections) and `TetraplecticProductRecurrence.lean` (recurrence, functional equation, e_1 only). The closed form `e_k=q^{k²}/(q²;q²)_k` is checked only as q-series to O(q^60) for k≤6 (`qbeta_ek_qpochhammer_closed_form.py`, re-run exit 0, reproduces). There is no general-k Lean proof. `qou-82w7` records that the remaining piece, the argument z(q0), is not combinatorial.

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
