---
# qz9k
title: 'Session: koide-tau / Q_β kernel Stage C / categorical binding wiring (no fitting)'
status: completed
type: milestone
priority: high
created_at: 2026-06-16T02:14:00Z
updated_at: 2026-06-21T19:39:07Z
---

## Session results (2026-06-16) — all three children delivered (pending human close)

PR [#2345](https://github.com/litlfred/qou/pull/2345). Each child produced a tiered,
grounded, non-fitting finding (verified against source, not just the corpus-map agents):

| Child | Verdict | Artifact |
|-------|---------|----------|
| `k9td` Koide | **refuted against a fit** — Koide forces m_τ to 62 ppm but QOU has no Z/3 democracy / √m-amplitude / categorical 2/3 ⇒ CAL-4 import, out of scope | `docs/audits/2026-06-16-koide-tau-forcing-assessment.md` |
| `qkhc` Q_β Stage C | **scoped + pruned** — Stage C = target fibre kernel R(q,ξ); c_k are q-holonomic (argument recurrence), NOT the C-finite order recurrence (binding ladder) — kills the q-Lommel conflation on paper | `docs/scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md` |
| `cbnf` binding | **state pinned + direction sharpened** — (1+q)/2 is a refuted near-match (no re-chase); GAP-A-3 is the non-fit direction; P_λ≡1 ⇒ tr_M, so P_λ = binding's deviation from the flat trace distribution | `docs/audits/2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md` |

Common thread: each corrected/sharpened a tempting-but-wrong path
(torus-Vol=0 overstatement; q-Lommel order-recurrence conflation; re-chasing
(1+q)/2) rather than running a blind probe. Two probes (Q_β fibre kernel,
GAP-A-3 P_λ) are infra-gated (no pyhecke_native) + owner-gated — next steps
recorded, not run. No fitting, no CAL-4, no production wire/un-wire.

## Follow-up (2026-06-16) — user picked options 1+2+3

Two more children added; the corpus-grep on options 2/3 produced a **redirect**
(both turned out already-run / underdetermined):

| Child | Verdict | Artifact |
|-------|---------|----------|
| `mtxi` m_τ Path A (opt 2) | **underdetermined** (ξ_ℓ unpublished; "FAR >50%"; constraints insufficient) → live framing is operator-valued ℓ=3 branching, gated on `conj:s5-so3-fiber-action` | shared synthesis doc |
| `g3pl` GAP-A-3 binding (opt 3) | **already run + axis closed** (spin channel refuted PR #1870; 22 GAP-A-4 closures) → do NOT re-run; same keystone | shared synthesis doc |

Synthesis: `docs/audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`
— m_τ + binding Δ_λ + mass λ(K) are **one problem**: the open S₅↔SO(3) geometric
fibre map (`conj:s5-so3-fiber-action`). Plus a critical-distance flag on the
2026-06-13 §5 "closes" overstatement, and a link of its "(1,1,1,1) sign-block"
c_k idea to `qkhc` Stage C (must clear the formalize-first gate).

Option 1 (`/prepare-merge` PR #2345) running last over the whole tranche; merge
held for explicit owner "merge it".

Consolidated work-plan from user request (2026-06-16): "work on beans"
1. `k9td` — koide-tau-forcing-derivation
2. `qkhc` — qbeta-kernel-hunt-stage-c
3. `cbnf` — categorical-binding-wiring-no-fitting

Branch: `claude/jolly-newton-h434ml`. Tracking via beans per owner directive
"use beans for coordination and workplanning". beans CLI absent in sandbox;
records managed directly in the documented `.beans/*.md` format (per `w5q7`).

## Discipline guardrails (STRICT — apply to all three children)

- **Corpus-grep first** (done at session start via 3 background Explore
  agents): map what already exists before declaring anything "open".
- **Formalize-first**: state the hypothesis class, find the invariant that
  prunes it, formalize, THEN (and only then) run any wide numerical probe.
- **No fitting** (esp. `cbnf`): do NOT add a 7th Δ_λ fit-ansatz or a CAL-4.
  Report TIERED — proved / near-match / fitted — never binary.
- **Fibre vs observable** (esp. `qkhc`): c_k Taylor coeffs live in the
  fibre (formal q); Im(q_0)=0 only at the observable level.

## Maps to STATUS.md goals

| Child | Goal / ledger |
|-------|---------------|
| `k9td` | mass theory (charged-lepton masses) — greenfield (no `koide` in corpus) |
| `qkhc` | `1 ppQ — Q_β only` / `docs/coordination/1ppq-qbeta.md` |
| `cbnf` | `Δ_λ closure (Option-E)` / `docs/coordination/option-e.md` |
