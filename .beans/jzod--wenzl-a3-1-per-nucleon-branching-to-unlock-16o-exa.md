---
# jzod
title: 'Wenzl A>=3 #1: per-nucleon branching to unlock 16O exact tr_M (multi-day; rank-deficient extracts)'
status: todo
type: task
priority: normal
created_at: 2026-06-20T00:58:14Z
updated_at: 2026-06-20T00:58:54Z
parent: qfzy
---

Scoped (prior session): A=2-only recursion in canonical_tr_m_via_branching.py; blocker = rank-deficient H_9+ A-operator extracts (21-42% err at A=3) + missing H_12 pp/pn, H_15/H_18. Multi-day; NOT a session win.

TRIAGE (2026-06-20, deep Explore): DEFER — genuinely multi-day Rust work, NOT a single-session task, and NOT a correctness blocker.
- The "16O exact tr_M" is ALREADY unlocked: production routes A≥3 through the fine-Bratteli transfer matrix (canonical_tr_m_via_branching.py:225-275), which is CORRECT (no fit) and fast enough for 16O (~1-3h). The math is PROVED — fusion identity verified at A=3 (1e-12, wenzl_a3_cross_check.py) and A=4 (1e-49, a_operator/a_operator_recursive.py).
- The rank-deficiency (canonical_tr_m_via_branching.py:232-243; audit 2026-06-16-unjustified-least-squares-fitting-audit.md) was diagnosed as a FITTING ARTEFACT of the old least-squares H_9+ extracts, NOT a math defect. The categorical (non-fitted) combiner is merged (PRs #2353/#2360/#2372/#2376/#2380), covering 26/30 λ⊢9.
- The ONLY open piece: a Rust algorithmic-intertwiner refactor (O(r⁶) nullspace → O(r³) cyclic-vector, lib.rs §1191-1331 per docs/workplans/2026-06-16-wenzl-a3-rust-combiner-handover.md), ~150 lines + 1e-25 verification gate, to clear 4 OOM λ⊢9 (r=64, ~5.4GB). This is a SPEEDUP/cross-check (~10×), not a correctness unlock. ~1 day, needs a built Rust env (pyhecke-native + dense_la_mpfr).
VERDICT: not worth a rushed single-session attempt (high risk MPFR-linalg refactor, low ROI since transfer already gives the correct value). Recommend a dedicated multi-day session with Rust env. Left status=todo.
