---
# qou-8q0u
title: 'Rust hecke-engine: stale muon q0 in doc-comments + gp_cross_validate bin (f64 Q_0 already proton; NO production muon literal)'
status: todo
type: task
priority: normal
created_at: 2026-08-15T21:27:22Z
updated_at: 2026-08-15T21:28:18Z
---

Follow-up to qou-m7py (merged, PR #5088). The Rust f64 production constant gram::Q_0 is ALREADY proton (1.1099785827513808) and the hecke.rs CLI resolves its default to it (q.unwrap_or(gram::Q_0)). NO production muon literal remains.

Actual scope (small doc/bin hygiene, NOT a migration):
- hecke.rs:36 — stale doc comment says 'default: q_0 = 1.1099785955541805' (muon); code returns proton Q_0. Fix the comment.
- gp_cross_validate.rs:254 — live q_str_50dps is the muon 50-dps; exploratory bin, cross-validates at the wrong anchor. Flip to proton 50-dps (matrix_m_mpfr.rs:403 has it: 1.1099785827513808075916690956107688798744991218736).
- hecke_canonical_chi.rs:24, hecke_gram.rs:7 — muon in doc examples; refresh.

DO NOT TOUCH (churn, not migration; gram.rs scope note): the muon 50-dps strings in #[cfg(test)] modules — tr_m_atomic_mpfr.rs:227, laurent_rational_q.rs:618, laurent_poly_q.rs:418, precision_scalar.rs:141. They are anchor-agnostic rounding/precision test inputs; precision_scalar.rs:124 even asserts .starts_with(muon), so flipping the input forces flipping the assertion for zero gain.

Fresh branch needed (5088 merged; main advanced 60+ commits).
