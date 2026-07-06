> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# Deferred workplan items — handoff 2026-05-02

**Pair**: [`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
+ [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md).

**Branch**: `claude/tier-4-math-audit-EkI7a` (PR #501).

This doc lists the workplan items that remain **open** after the
Tier-4 audit pass. Each is multi-day/week/research-grade work
that exceeds a single-session scope.

## What this branch closed (recap)

14 workplan items closed across 19 commits:

- **P0 fully closed**: P0.1, P0.2, P0.3, P0.4
- **P1 mostly closed**:
  - ✅ P1.2, P1.3 (BW-8/11 — Kerov → q-heat resolvent, compute-metadata)
  - ✅ P1.4 path-(b) (magic numbers — `conj:magic-numbers-bring`)
  - ✅ P1.5 (compound-shell audit, in PR #498)
  - ✅ P1.6 (neutrino unknot consistency)
  - ✅ P1.7 path-(b) (1/α 399 ppb as $k = 5$ truncation)
  - ✅ P1.1(b) (compute-side $q_0$ unification confirmed)
  - 🟡 P1.1(a) **open** (research-grade categorical chain)
- **P2 narrative side**:
  - ✅ P2.6 narrative + Lean class-field refactor
  - 🟡 P2.1–P2.5 **deferred** (compute infrastructure, see below)
- **P3 mostly closed**:
  - ✅ P3.1 partial + extended sweep
  - ✅ P3.2, P3.3, P3.4 path-(b)
  - 🟡 P3.4 path-(a), P3.5 **deferred** (research-grade)
- **P4 fully closed**: P4.1, P4.2, P4.3
- **algebraic-refactor Phase 1 fully landed** (3 conjectures + 3
  examples + 2 remarks + 4 bib + Lean stubs)
- **algebraic-refactor Phase 2 prose sweep** — null result
- **algebraic-refactor Phase 2 Lean proofs** — deferred (see below)

## Deferred items by category

### 1. Compute pipeline infrastructure (P2.1–P2.5)

Multi-week mechanical refactors of `computations/`.
None can be closed in a single session because each requires
running scripts, validating outputs, and iterating numerically.

| ID | Title | Effort | Status |
|:---|:------|:-------|:-------|
| **P2.1** | Full Wedderburn channels in `crt_markov.py` | 1 week | Blocked by P2.2 |
| **P2.2** | $H_{3A}$ Wedderburn coverage via CRT polynomial reconstruction | 1 week | Open; blocks P2.1 + P1.7(a) |
| **P2.3** | Word-shortcut undo functions L4–L7 | 4 weeks | Open; blocks molecular layer |
| **P2.4** | Multi-level quadratic SDP (L4–L7) | 2 weeks | Open; blocks shell-closure layer |
| **P2.5** | Symbolic-in-$q$ refactor across all `*_witness.py` | 1 week | Open; mechanical |

**Recommended ordering**: P2.5 first (mechanical, no dependencies,
unblocks all witness JSONs from "fitted-feeling" 50-digit floats);
then P2.2 (unblocks P2.1, P1.7(a)); then P2.1, P2.3, P2.4 in
parallel.

### 2. Research-grade open conjectures

| ID | Title | Effort | Status |
|:---|:------|:-------|:-------|
| **P1.1(a)** | Substrate-parameter-unique categorical chain | 1 week | Open; nice-to-have |
| **P3.4(a)** | Uniform $\Delta_{\max}$ proof via GS $E_2$-collapse | 1–2 weeks | Blocked on followups-branch GS infrastructure |
| **P3.5** | `family-4` motivic-substrate `instance` at $q_0$ | open-ended | Research-grade |
| **P1.4(a)** | Period-lattice proof of `conj:magic-numbers-bring` | 1+ weeks | Bounded research; the conjecture is path-(b) closed |

These are genuine research questions. Path-(b) closures (conjecture
+ empirical witness) are landed for P3.4 and P1.4; path-(a) proofs
are the long-term content goals.

### 3. Lean-side deferred

| ID | Item | Effort | Status |
|:---|:-----|:-------|:-------|
| **P2.6 def-side** | Replace `GBResidueSpectralSum` class fields with constructive `def`s | multi-week | Requires GS-filtration + Habiro-completion Mathlib infrastructure |
| **Phase 2 Lean** | Prove conditional Hecke fragments for the 3 algebraic-refactor Phase 1 conjectures | 1–2 weeks per fragment | Provable in pure Hecke combinatorics; no Mathlib infra blocker |

The Phase 2 Lean proofs are: (a) full-twist content-sum-zero ⇒
self-conjugate (for `conj:categorical-neutrality-saturated-shells`);
(b) BB stratification + Yekutieli rigidity ⇒ $E_\infty^{p, >0}(n)
= 0$ at magic $n$ (for `conj:homological-shell-condensation`);
(c) self-conjugate + content-sum-zero LR rigidity lemma (for
`conj:diagrammatic-double-magic-lr-fusion`).

### 4. P3.1 follow-up — per-block acknowledgement audit

The extended P3.1 sweep
([`2026-05-02-p3-1-extended-sweep-findings.md`](2026-05-02-p3-1-extended-sweep-findings.md))
identified ~3000 transitive provable blocks in 18 case-(3)
legitimate-dependency cones (definitions / remarks where the
conjecture is structurally essential to the named construction).

Per AGENTS.md §3b clarification, these are **not** propagation
violations — but a per-block acknowledgement audit would confirm
each prose body explicitly notes the conjectural upstream
dependency. Estimated **1–2 days, manual triage**, with most
blocks already correctly framed.

### 5. P0.1 follow-up — sweep heuristic refinement

The wall-violation sweep
([`wall_violations_sweep.py`](../../computations/sweeps/wall_violations_sweep.py))
over-flags 3 hits in `atom-knot-mass-derivation-proof.md` because
its triage heuristic doesn't recognise the
"Post-Archimedean naming (borrowed, not part of derivation)"
section header. A small heuristic refinement (look for the section
header before classifying as `proof-input`) would reduce the
false-positive rate. **0.25 day, mechanical**.

## Recommended next session priorities

If a follow-up session is scoped to **0.5–1 day**:

1. **P3.1 follow-up per-block acknowledgement audit** (1–2 days
   manual but tractable; pure documentation hygiene).
2. **P0.1 sweep heuristic refinement** (0.25 day; clean up the
   false-positive cluster).
3. **Review the 18 case-(3) cones** and decide whether some
   provable blocks should carry explicit "conditional on
   `conj:X`" prose (1 day spot-check).

If a follow-up session is scoped to **1+ weeks**:

1. **P2.5 symbolic-in-$q$ refactor** (1 week, mechanical, unblocks
   witness JSON readability).
2. **P2.2 + P2.1 Wedderburn coverage at $H_{3A}$** (2 weeks,
   compute infrastructure; closes the largest single source of
   compute-side mass error per `AUDIT-crt-k-level.md`).

If the goal is **research-grade content advancement**:

1. **Phase 2 Lean proofs** for the 3 magic-numbers conjectures
   (1–2 weeks per fragment, all in pure Hecke combinatorics).
2. **P1.4(a)** period-lattice proof of `conj:magic-numbers-bring`
   (1+ weeks).
3. **P3.4(a)** uniform $\Delta_{\max}$ proof via GS $E_2$-collapse
   (1–2 weeks, blocked on followups GS infra).

## Status of `DERIVATION-STATUS.md`

Updated in this branch: every previously-flagged empirical /
fitting flag is either resolved (CAL-0/1/2, SUB-1, NU-1, SHELL-1,
JSJ-link 8, BW-8, BW-11) or has a clear path forward (MAG-1
path-b landed, ALPHA-2 path-b landed). The "🟠 open" surface in
DERIVATION-STATUS.md is now **empty for empirical / numerology
flags**; the only 🟠 / 🟡 entries left are research-grade
follow-ups tracked above.
