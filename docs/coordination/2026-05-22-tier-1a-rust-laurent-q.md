# Coordination ledger — Tier 1.A (Rust LaurentQ reduce + MPFR pipeline)

**Goal:** Land the Tier 1.A Rust port (Markov-peel reduce loop with
exact BigRational coefficients) + end-to-end MPFR substitution,
per [`docs/audits/2026-05-20-compute-optimization-roadmap.md`].

**Owner:** @litlfred

## Scope map (2026-05-22)

| PR | branch | author | state | classification |
|----|--------|--------|-------|----------------|
| **#886** | `claude/vibrant-heisenberg-Mrjtn` | claude | open, ready | **active** — Tier 1.A delivered |
| #871 | `copilot/optimize-compute-pipeline` | Copilot | open, **draft** | superseded by #886 (same 8 files, same architecture; #886 is a strict superset) |

Other PRs evaluated and declined as scope siblings per the
2026-05-22 `/coordinate` ask (single-select on #871 only):

- #807 (compute-audit P33-P34 skill addition) — no file conflict;
  my new `ffi-roundtrip-audit.md` is a complement to the parent
  `compute-audit.md`.
- #889 (1ppb compute-precision + speed audit) — same day, same
  author, but it is a planning / audit doc (199 additions, no
  code touched in the Tier 1.A area); item #6 "Rust LR convention
  adapter wire-up to `atomic_tr_m_helium4.py`" is an orthogonal
  speedup direction targeting a different consumer.
- #872 (qa-pipeline script-quality axis) — additive to the
  CI QA infra; my `ffi-roundtrip-audit` skill could be folded
  in as a future criterion, but no immediate coordination needed.

## Coordination actions taken

1. **2026-05-22**: Posted single supersession comment on #871
   listing the file-set delta (`laurent_rational_q.rs` 558 vs 395,
   `laurent_hecke_element.rs` 281 vs 257, `reduce_laurent.rs` 410
   vs 341, plus #886-only files: `tr_m_atomic_mpfr.rs`, Tier 1.C
   cyclic-canonical cache key in `tr_m_word_lq.rs`, the
   `ffi-roundtrip-audit.md` skill).  Recommended close in favor
   of #886 — owner decides.
2. **2026-05-22**: Created this ledger entry per coordinate §9.

## Open questions for the owner

- **Close #871?** It's a draft with a strict-subset of #886's
  scope (verified by file-set comparison + line-count delta).
  Closing avoids duplicate review attention.

## Bench snapshot at coordination time

⁶Li (cold cache, 50 dps, vs `laurent_q_trace.tr_M_atomic_lq`
baseline 234 s):

| commit on #886 | wall | speedup |
|----------------|-----:|--------:|
| all-Rust + MPFR (`22e3c1cd`) | 94.6 s | 2.38× |
| + R1 fast-path (`52940b5f`) | 84.5 s | 2.65× |
| + FxHashMap (`aee27a81`) | **79.2 s** | **2.96×** |

4× / 60-s gate is open by ~19 s; next lever per
[`docs/audits/2026-05-22-rust-laurent-q-reduce-results.md`] §
"Follow-ups" is `Ratio::new_raw` GCD deferral (1.5-3× estimated,
risk: must verify denominators stay bounded).

## Cross-references

- [`docs/audits/2026-05-20-compute-optimization-roadmap.md`] —
  Tier 1.A scope and 4× gate definition.
- [`docs/audits/2026-05-22-rust-laurent-q-reduce-results.md`] —
  Tier 1.A delivery doc (commit progression + follow-up plan).
- [`.claude/skills/local/ffi-roundtrip-audit.md`] — companion
  audit skill catalogues 7 similar ping-pong patterns elsewhere.
- [`.claude/skills/local/coordinate.md`] — protocol followed.
