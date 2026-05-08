# 00 — Workplan and Scope

**Date:** 2026-05-08
**Branch:** `copilot/audit-mass-beta-decay-computation`

## 1. User request (verbatim, paraphrased)

> Thorough deep audit of all **mass**, **beta-decay**, and **binding-energy** computations. Every computation should be backed by an approved conjecture; any gap is an audit flag. Catalog inconsistent conventions/weights. Produce a full **pre-archimedean** derivation: categorical action → non-abelian Stokes → knot decomposition → Wedderburn → weights/partitions → Frobenius pairing → Gröbner-Shirshov filtration → jet order → Hecke energy. Step-by-step, to fill in places we are still **fitting / guessing / using numerology**. Review **crystal bases / new math** for compute optimization. Conduct a **baseline mass table** review, then re-evaluate each improvement (small regression OK). Produce a workplan to reach **1 ppb**.

## 2. Out-of-scope

- Re-litigating proofs already in flight (the user wants the audit, not a redo of recent compute work).
- Formal proof writing in this PR. The audit produces *flags* and *plans*; proofs are downstream PRs.
- Modifying any compute scripts in this PR. Code changes to `.py`/`.lean` are explicitly downstream.
- Re-derivations that go beyond an algebraic chain ending at the substrate parameter `q_0` and Vol(4₁) (the "pre-archimedean" boundary).

## 3. Deliverables (one file each, see [INDEX.md](INDEX.md))

| # | File | Status |
|---|------|--------|
| 00 | This workplan | ✅ |
| 01 | Baseline mass / β / B table | ✅ |
| 02 | Pre-archimedean derivation chain (13 links, status badges) | ✅ |
| 03 | Mass audit (per-script DERIVED/FITTED/HEURISTIC/EMPIRICAL_FIT) | ✅ |
| 04 | Beta-decay audit (g_A, V_ud, G_F, N_v, θ_W, Q) | ✅ |
| 05 | Binding-energy audit (JSJ, ρ_F, c_αα, Frobenius G) | ✅ |
| 06 | Convention/weight inconsistencies catalog | ✅ |
| 07 | Crystal-base compute-optimization review | ✅ |
| 08 | Revised 1-ppb workplan | ✅ |
| 09 | Baseline + per-improvement tracker | ✅ |

## 4. Audit flag schema

Every flag carries:
```
[AUDIT-FLAG severity=critical|high|medium|low id=DEEP-2026-05-08-NNN]
file:           folio-assistant/computations/<script>.py:LINE
description:    one line
backing:        conj:foo | prop:bar | NONE
remediation:    one line (link to detailed remediation in 08-1ppb-workplan-revised.md)
```

`id` is monotonic across the document set, prefixed `DEEP-2026-05-08-`. Cross-doc references use the bare id.

### 4.1 Classification taxonomy

For every numerical input in every compute script:

| Class | Definition |
|-------|------------|
| **DERIVED** | Chain ends at an *approved* conjecture/proposition (label exists in a content block; either Lean-proved or explicitly axiomatised as a class) |
| **FITTED** | Pulled from CODATA / PDG / AME — i.e. an experimental constant used as a calibration anchor |
| **HEURISTIC** | A "natural" choice (e.g. ρ_F = 2 for chirality; pick the closest census knot) that has *no* approved-conjecture backing |
| **EMPIRICAL_FIT** | A coefficient explicitly fit to data (polynomial regression, nearest-knot search, etc.) |
| **TOPOLOGICAL_HEURISTIC** | (new) Topologically natural but unproved (e.g. JSJ T(2,n) ↔ α-cluster mapping) — distinguishes from pure pattern-matching |

A `HEURISTIC` or `TOPOLOGICAL_HEURISTIC` input that **gates a paper claim** is automatically severity ≥ HIGH. A `HEURISTIC` input that is **circular** with an isotope used as an anchor is automatically CRITICAL.

## 5. Success criteria

This audit succeeds when:

- [x] Every mass / β / B compute script appears in §03/04/05 with every numerical input classified.
- [x] The pre-archimedean chain in §02 has a status badge for every link.
- [x] Every audit flag has an `id` and a remediation pointer.
- [x] §08 contains a phased plan (Tier-A gating, Tier-B follow-on) with a dependency DAG.
- [x] §09 lists every baseline number with the citation; future PRs amend this file with new rows.
- [x] §06 has a "canonical conventions" table that downstream PRs can cite as authority.
- [x] §07 names ≥ 1 high-payoff crystal-base optimization with effort/payoff estimate.

## 6. Triviality declaration

This PR adds **only documentation** (`docs/audits/2026-05-08-deep-mass-beta-binding-audit/*.md`). No `.py`, `.ts`, or `.lean` files are modified. CodeQL: trivial. Code review: applies (audit content reviewed for accuracy).

## 7. Predecessor audits explicitly read

The four parallel sub-agents read these audit threads in full to avoid re-litigating settled questions:

- `2026-05-06-frobenius-pairing-compute-audit.md` (cited in §05)
- `2026-05-06-refocused-1ppb-workplan-v2.md` (cited in §08)
- `2026-05-07-borromean-axial-coupling-fix.md` (cited in §04)
- `2026-05-07-lp-dual-backfill.md` (cited in §06)
- `2026-05-08-lp-dual-wired-audit.md` (cited in §06)
- `derivation-chain-mass-tower.md` (cited in §02)
- `categorical-vs-fitted-q-decay-ba.md` (cited in §03/04)
- `mass-beta-decay-derivation-audit-2026-04-29.md` (predecessor to this audit; cited in §08)
- `path-to-1ppb-04-plan.md` (cited in §08)

## 8. Done condition for this PR

Per the `report_progress` checklist in the PR description:
- All 10 docs (INDEX + 00..09) committed.
- `parallel_validation` run with `trivialChangeDeclaration.codeql.isTrivial = true` (docs only).
- PR title and body reflect the deep audit + plan.
- No compute scripts modified, no Lean files modified, no content blocks modified — those are explicit follow-on PRs gated by §08.
