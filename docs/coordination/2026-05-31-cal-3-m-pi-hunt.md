# CAL-3 = m_π — coordination ledger

**Branch:** `claude/brave-mendel-FPxFl`
**PR:** [#1579](https://github.com/litlfred/qou/pull/1579)
**Status:** in flight — empirical corroboration committed, content block update deferred to post-#1581 merge
**Goal:** corroborate the framework's already-adopted `CAL-3 = m_π` assignment via two independent empirical paths and coordinate with the active sibling PRs working in adjacent scope.

**Cross-links into master ledgers (post-rebase 2026-05-31):**
- [`STATUS.md`](../../STATUS.md) — folio dashboard; this session contributes to L2 + CAL-3 + Option-E rows
- [`docs/coordination/1ppq-qbeta.md`](1ppq-qbeta.md) — 1ppQ-Q_β master ledger; my c_3 negative result is a parallel-arrival corroboration (PR #1579 row added)
- Canonical c_3 SETTLED on main: commit [`ced5e2830`](https://github.com/litlfred/qou/commit/ced5e2830) + audit [`2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md)

## Context

The framework's compute layer ([`codata_constants.py` line 22](../../computations/substrate/codata_constants.py)) and content layer ([`three-calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/three-calibration-inputs.md)) both already declare `CAL-3 = m_π` (pion decay width → pion mass scale; replaces the older `CAL-3 = Q_β` framing). This session noticed the older framing via stale context, hunted for the "missing CAL-3", and produced two empirical probes that corroborate the canonical assignment from independent directions.

## Work items in this PR

| # | Item | Status | Commit |
|---:|---|---|---|
| 1 | m_π Hecke probe — test derivability from (m_e, q_0) alone | ✅ done | `c98033d63` |
| 2 | Address 3 gemini reviews (H_3 Markov trace bug, comment typo, codata import) | ✅ done | `88964a164` |
| 3 | c_3 categorical derivation attempt — NEGATIVE | ✅ done | `01891c3ad` |
| 4 | Cross-ref note on c_3 audit citing #1581 Finding B | this commit | — |
| 5 | CAL-3 corroboration audit doc | this commit | — |
| 6 | This coordination ledger | this commit | — |
| 7 | Update `three-calibration-inputs.md` content block | deferred | — |
| 8 | Land v9 stress-test on broader mirror pairs (blocked on chi-witnesses) | deferred | — |
| 9 | Add `M_PI_*` to `codata_constants.py` | ✅ already on main | (no commit) |
| 10 | Final prepare-merge-auto pipeline | follow-up | — |

## Empirical findings (one-paragraph summary per probe)

### Probe A — m_π Hecke prediction (negative)

[`m_pi_hecke_prediction_probe.py`](../../computations/probes/m_pi_hecke_prediction_probe.py)
tested ~100 candidate categorical formulas for m_π from (m_e, q_0,
m_μ) alone, using the same Lean-proved building blocks that close
m_p to 0.24 ppm under the substrate identity. **Best miss = 19,938 ppm**
(formula `m_μ · (|tr_M(𝓜_+)| + 5h)`), i.e. 1.4 × 10⁷ × the PDG
experimental precision of 1.3 ppb. The 35,000× gap in derivability
between m_p (0.24 ppm) and m_π (19,938 ppm) under the same compute
infrastructure is structural, not numerical noise — m_π carries
information that (m_e, q_0) does not encode.

### Probe B — c_3 categorical derivation (negative)

[`c_3_categorical_derivation_attempt.py`](../../computations/c_3_categorical_derivation_attempt.py)
tested 15 single-formula categorical candidates (bar-symmetrization,
Hopf-Jones at q₀, Wedderburn-weighted block traces, Habiro binomial)
against BOTH muon-pin and m_p-pin q₀ anchors. None match to ≤ 10 ppm
at both anchors (Taylor-exact threshold). The negative result is
**consistent with sibling [#1581](https://github.com/litlfred/qou/pull/1581) Finding B**
which reframed the apparent q₀-swing as `c_4·u⁴` truncation error
rather than a genuine c_3 q-dependence. Open path: Q_β Habiro
generating function (parallel α_EM PR #1511).

## Sibling scope map

| PR | Branch | Overlap class | Action taken |
|---|---|---|---|
| [#1516](https://github.com/litlfred/qou/pull/1516) | `claude/option-e-phase2-gram-probe-2026-05-30` | DIRECT — Option E foundation (H_n Gram + Phase 2 entry); v9 stress-test downstream | intent ping posted; v9 generalization deferred until H_n chi-witnesses land |
| [#1581](https://github.com/litlfred/qou/pull/1581) | `claude/three-dashboard-probes-2026-05-31` | DIRECT — independent audits of v9 (1+q)/2 uniqueness + c_3 Rule A reframing | cross-reference posted; findings convergent (no escalation needed) |
| [#1475](https://github.com/litlfred/qou/pull/1475) | `claude/qbeta-ck-interpretations-2026-05-30` | DIRECT — Q_β c_k interpretation taxonomy | intent ping posted on c_3 attempt menu |
| [#1577](https://github.com/litlfred/qou/pull/1577) | `claude/eloquent-heisenberg-HGLUF` | ADJACENT — canonical-watcher Q_β c_k flip-flop prevention | intent ping posted confirming watcher rule shape works for both positive AND negative c_3 outcomes |
| [#1556](https://github.com/litlfred/qou/pull/1556) | `claude/m-mu-chain-audit-2026-05-31` | ADJACENT — m_μ thread routing | intent ping posted noting m_π=CAL-3 may add a parallel sibling node to the routing diagram |

## Convergent vs inconsistent findings

Per [`local/coordinate.md` §6](../../.claude/skills/local/coordinate.md), all flagged
findings are **convergent** with sibling work. No §6 escalations.

| Finding (this PR) | Sibling finding | Status |
|---|---|---|
| m_π not derivable from (m_e, q_0) at any reasonable precision | Framework already adopts CAL-3 = m_π (codata_constants.py + three-calibration-inputs.md) | **Corroborating, not novel** |
| c_3 not closeable by single-formula categorical candidate | #1581 Finding B: apparent q-swing is c_4·u⁴ truncation, not c_3 q-running | **Same conclusion, complementary explanation** |
| v9 (1+q)/2 was found by search → potential fit concern | #1581 Finding C: (1+q)/2 unique within 0.11% across 33 candidates | **Concern partially addressed** (still: categorical *derivation* of (1+q)/2 open) |

## CI status

PR #1579 hit the documented [AGENTS.md billing-pattern failure](../../AGENTS.md)
across `validate`, `Content pipeline`, `Build all papers + sidecar`,
`copilot-setup-steps` — all completing in 2-4 seconds setup-phase.
Local content validate is exit 0. Not pushing retrigger commits per
the canonical billing-skip rule.

## After this PR

1. Wait for sibling [#1581](https://github.com/litlfred/qou/pull/1581)
   to merge (their v9 uniqueness + c_3 Rule-A audits are the cleaner
   authority; my work corroborates and cross-references).
2. When `chi-{Li7,Be7,B11,C11,…}-h*-at-q0-50dps.witness.json` land
   from H_n Gram work on [#1516](https://github.com/litlfred/qou/pull/1516),
   re-run v9 stress-test on broader mirror pairs to confirm
   `(1+q)/2` generalizes.
3. If v9 generalizes: file an audit confirming the structural
   robustness; if not, file the per-pair correction factors and
   flag the categorical *derivation* of `(1+q)/2` as the truly load-
   bearing open problem.
4. Categorical derivation of c_3 remains an open work item, but
   reframed: it is NOT a single-coefficient closure (this PR's
   probe B + #1581 Finding B both rule that out), it is a Q_β Habiro
   generating function in the α_EM PR #1511 mold.
