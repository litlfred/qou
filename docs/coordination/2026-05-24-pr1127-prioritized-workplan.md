# Prioritized workplan — PR #1127 Q_β / complex-q / ρ_q purge (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD` → [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: stacked owner directives (this session) — "fill gaps", "wire correct things in compute", "audit compute for legacy", "prove in lean and paper", "muon ID conflict", "make prioritized workplan and check tracks/rods"

## Tracks (the directive cascade decomposed)

| Track | What | Status | Cost |
|---|---|---|---|
| **T1** | New audit doc: corrected Im(q) framing + bar-decomp of n/p Markov traces | analysis done in chat; needs elevation to doc | 20 min |
| **T2** | Muon knot ID audit: 4_1 (skein-mass-relation.md) vs 5_1 (knot-volumes.py) | identified conflict; needs primary-source resolution | 30 min |
| **T3** | Phase 3 operator-level m_μ/m_e re-derivation | infrastructure exists (markov_peel); needs glue script | 1-2 h |
| **T4** | Lean formalization of bar-decomposition identities | sibling PR #1196 lands `BarSymmetricBarAntiSymmetricIdentities.lean` — overlap | 30 min via coordination (cite sibling) |
| **T5** | Full compute audit for legacy ρ_q / SUPERSEDED pattern | survey done (13 content + 2 compute); 3 content + 2 compute banner'd; 11 remaining | 1-2 h mechanical |
| **T6** | Wire canonical forms in compute (replace SUPERSEDED-ρ_q consumers) | not started; needs T5 first | 4-6 h |
| **T7** | Coordinate comment on PR #1196 (bar-decomposition Lean) | not started | 10 min |
| **T8** | Coordinate comment on sibling qa-arch-* PRs touching beta-decay scripts | not started; LOW overlap | optional |
| **T9** | Path B: direct Q_β from per-braid mass tower (canonical, non-ansatz) | requires T3 done; ~4-6 h | gated on T3 |
| **T10** | Path A: theoretical derivation `Q_β = \|Δ(net)\|·E_0` from per-braid mass tower at leading order | analytical 1-2 days; OUT of scope this session | DEFER |
| **T11** | Lean substrate-lift 123-file batch | needs `lake` (not available); DEFERRED | DEFER |
| **T12** | Im(q) physics writeup → audit doc | analysis done in chat (corrected via Q1/Q2/Q3) | 20 min |

## Priority dispatch order for THIS session

Highest information-per-minute first:

1. **T1 + T12** — single audit doc (combine; corrected Im(q) framing + bar-decomp finding is the same writeup) → 30 min
2. **T2** — muon ID resolution; cheap and unblocks T3 → 30 min
3. **T3** — Phase 3 compute (operator-level m_μ/m_e); the analytical heart → 1-2 h
4. **T7** — coordinate comment on PR #1196 → 10 min
5. **T5 (remaining)** — 11 SUPERSEDED-ρ_q banner files (mechanical) → 1 h

**Total session budget**: ~3-4 h work. Items T6, T9, T10, T11 explicitly deferred to follow-up sessions (per "combine one PR / work only on one" mode this should still ride on #1127 if it's a continuing session, otherwise new branches).

## Rods / tracks check

The user's "tracks/rods" check (per session-policy §4 idle-trigger queue):

| Queue | Item | Action |
|---|---|---|
| Session todos (this) | The 12 tracks above | walking T1 → T2 → T3 first |
| PR #1127 todos | Test plan in PR body | Path B (T9) is the major unchecked item |
| Watcher queues | proof / canonical / compute / detangler / one-voice | NOT polled this session; standing assumption is sibling PRs cover their own watcher hits |
| Cross-cutting cleanups | SUPERSEDED ρ_q purge (T5 + T6) | partially in progress |

## What's already deferred (won't be done this session)

- **T10** Path A theoretical derivation — 1-2 days analytical, multi-session
- **T11** Lean 123-file substrate-lift batch — needs `lake build` per AGENTS.md §0 (`lake exe cache get && lake build`); no toolchain in container; deferred
- **T6** wiring canonical forms in production compute consumers — depends on T3 outcome (what IS canonical for leptons?)

## Queue status after this session (2026-05-24 end-of-burst)

**Completed this session (PR #1127, 16+ commits)**:
- ✓ T1 + T12 (Im(q) correction + bar-decomp finding → folded into Phase 3 audit)
- ✓ T2 (muon ID conflict audit + fix in `knot-volumes.py`)
- ✓ T3 (Phase 3 m_μ/m_e operator-level re-derivation audit + `conj:lepton-mass-tower-canonical` content block setup)
- ✓ T4 (Lean stubs for trefoil reduction + lepton mass formula scaffolding — pending lake verification)
- ✓ T5 (SUPERSEDED-ρ_q banner sweep: 15 content + 2 compute files total)
- ✓ T7 (coordinate comment on PR #1196)

**Explicitly queued (NOT done; user-confirmed scope)**:
- **T6** wire canonical forms in production compute — depends on T3 outcome (lepton-mass-tower formula must be derived first); MULTI-DAY
- **T9 (Path B)** direct Q_β from per-braid mass tower — Phase 3 finding shows per-braid mass tower itself uses SUPERSEDED ρ_q at some level; "direct compute" needs the canonical (non-ρ_q) lepton-mass-tower formula first (T6 prerequisite). NOT deprecated, but **gated on T6**
- **T10 (Path A)** theoretical derivation `Q_β = |Δ(net)| · E_0` at leading order — similarly depends on canonical (non-ρ_q) per-braid mass tower. NOT deprecated, but **gated on T6**
- **T11** Lean 123-file lift batch — lake-deferred (no toolchain in container); independent of T6

**Is T9 / T10 deprecated?** **NO** — both are still meaningful and necessary for the Q_β fitting concern. The Phase 3 finding **refines** their prerequisites:
- Before Phase 3: T9 / T10 could be done "directly" using the existing per-braid mass tower (which embeds SUPERSEDED ρ_q)
- After Phase 3: T9 / T10 should be done using the **canonical (non-ρ_q) per-braid mass tower**, which itself requires the lepton-sector variant of `prop:rho-k-graded-expansion` (T6)
- So T9 / T10 are downstream of T6, not deprecated

**Dependency chain**: T6 (lepton canonical) → T9 (Q_β direct compute) → T10 (theoretical leading-order derivation) → Q_β fitting concern resolution
**Independent**: T11 (Lean lift batch) — does not gate on Q_β work

## Audit / file inventory snapshot

Audits landed this branch: 7 docs in `docs/audits/2026-05-24-*.md`.
Coordination ledgers: 2 docs in `docs/coordination/2026-05-24-*.md`.
Content blocks modified: 7 (in particle-interactions, braids-and-knots, archimedean-universe).
Content blocks created: 2 (q-zero-complex-extension, lusztig-vs-hermitian-bar).
Lean files modified: 1 (symbolic-character-table — §7c lift).
Compute scripts: 2 created (q_beta_complex_q_test1_phaseA + v2), 2 modified (q_pinning_50_digit, rho_f_categorical_probe), 1 SUPERSEDED-ρ_q-banner added.

## Cross-references

- PR #1127 (this branch)
- PR #1196 (sibling — bar-decomp Lean infra)
- PR #1153 (sibling — sinh Q_m torus-knot identity)
- Audits: `2026-05-24-q-beta-net-ansatz-fitting-finding.md`, `2026-05-24-complex-q-historical-trajectory.md`, `2026-05-24-superseded-rho-q-purge.md`, `2026-05-24-q-beta-droppability-cohomology.md`, `2026-05-24-q-zero-reality-audit.md`, `2026-05-24-real-star-lift-inventory.md`
- Coordination: `2026-05-24-q-beta-fitting-and-complex-q.md`, `2026-05-24-q-beta-pr1127-queued-work.md` (this session's text-up)
