# 1ppQ Master Ledger — Q_β

> Single source of truth for the **1 ppQ (10⁻¹⁵) Q_β** goal.
>
> Per `STATUS.md`: this is the achievable arm of the 1ppQ target;
> absolute m_p / m_n / m_⁴He at 1ppQ remain Subgoal-2 territory
> (substrate-derivation of q_0 required, declined 2026-05-08).

## Why this ledger exists

The Q_β c_k Taylor coefficients have flip-flopped four times across
sessions. Each flip wasted ~1 session and produced contradictory
prose in the dashboard. This ledger:

1. **Pins the canonical status of each c_k** so the next session
   doesn't re-derive a "discovery" that was already retracted.
2. **Catalogues the retraction history** so the failure modes are
   visible (typically: conflating "near-match" with "Taylor-exact").
3. **Lists open probes** so multiple agents can fork distinct
   threads without stepping on each other.
4. **Logs session intent + results** so an interrupted thread can
   be picked up by another agent.

## c_k status (as of 2026-05-31)

| Coefficient | Status | Evidence | Open question |
|-------------|--------|----------|---------------|
| **c_2** | **Taylor-exact (derived)** ✓ | `f4930df95` ("honest c_k bar — only Taylor-exact c_2 wired") | none |
| **c_3** | **NOT derived** — near-match (J_Hopf(q=1)=-2), 2.98% cross-anchor swing >> 10⁻⁵⁰ compute precision | `b3c92844d`, `6ace8153e`, [verdict 2026-05-31](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md) (this PR) | **SETTLED** as near-match. Resolution path = identify Q_β Habiro element. |
| **c_4** | **NOT derived** — CAL-anchored tier | `453918755` ("CAL-anchored, honestly labeled") | derive canonically via Habiro recursion |
| **c_5** | **NOT derived** | — | extend Habiro recursion |
| **c_6** | **NOT derived** | — | extend Habiro recursion |
| **c_7** | **NOT derived** — target for 1ppQ | per `6ace8153e` truncation analysis: N=7 → 1ppQ | extend Habiro recursion |

**Reading:** the 1ppQ truncation analysis (`6ace8153e`) says N=7 is required.
The Habiro q-difference equation (`d6b6e0483`) gives a recursive
generator for c_k. If c_3 can be settled canonically, the same recursion
extends to c_4–c_7 with relative ease. **c_3 is the keystone.**

## Truncation-order math (reference, from `6ace8153e`)

Q_β = Q_base · Π_{k≥2} (1 + c_k · u^k)  where u = b · ℏ_q² ≈ 0.00852

- Each rung buys log₁₀(1/u) ≈ **2.07 digits**.
- N(ε) ≥ log₁₀(1/ε)/2.07 − 1.
- 100× exp target (≈ 8 ppb) → N=3
- 1 ppb → N=4
- 1 ppt → N=5
- **1 ppQ → N=7**

## Open probes (current queue)

- [x] **PROBE 1 — c_3 q_0-stability** (DONE this session, 2026-05-31): verdict NEAR-MATCH. The 2.98% cross-anchor swing exceeds 10⁻⁵⁰ compute precision by 48 orders of magnitude — c_3 = -2 is NOT Taylor-exact at the value level, and J_Hopf(q) − ℏ_q²(q) is not the right q-dependent function either. Audit: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md).
- [ ] **PROBE NEW — Q_β Habiro element search** (the actual blocker — parallel α_EM PR #1511). High priority; this is the keystone for all c_k≥3.
- [ ] **PROBE 2 — c_4 coefficients** from the Habiro element (renamed from c_4 Habiro recursion). Blocked on the search.
- [ ] **PROBE 3 — c_5 / c_6 / c_7 coefficients** from the Habiro element. Blocked on c_4.
- [ ] **PROBE 4 — Lean §3b-cond classes for each c_k** mirroring `QbetaC3StructuralFormClass` (`441c291fc`).
- [ ] **PROBE 5 — _precision.py headroom bump** to 70 dps compute / 60 dps output (for safe 10⁻¹⁵ arithmetic).

## Active PRs

| PR | Scope | Relation to 1ppQ-Q_β |
|----|-------|----------------------|
| #1577 | canonical-watcher: automate Q_β c_k flip-flop prevention | **direct overlap** — infrastructure to prevent the bug this ledger documents |
| #1521 | Habiro element [2]_q·(1-h²α) categorical 1-loop | **direct upstream** — the canonical c_k source |
| #1543 | ⁴He magic-A binding | adjacent (binding side) |
| #1580 | coord infrastructure + 1ppQ kickoff (THIS PR) | sets up this ledger + STATUS.md + queue file + /session-intent + /pending-show + SessionStart hook |

## Flip-flop history (DO NOT REPEAT)

| # | Date | Commit | What flipped | Why (failure mode) |
|---|------|--------|--------------|---------------------|
| 1 | 2026-05-26 | `b2f908731` | c_3 = J − ℏ_q² "0.004% sub-leading" | over-claimed near-match as Taylor-exact |
| 2 | 2026-05-29 | `41b8d4a4c` | wire(Q_β) restore derived c_3 = J(q=1) = −2 | same conflation, different prose |
| 3 | 2026-05-30 | `f4930df95` | wire(Q_β) honest c_k bar — revert c_3 | corrected |
| 4 | 2026-05-30 | `c1f7487df` → `b3c92844d` | deep-audit re-wired c_3, then "stale-q₀ artifact" | conflated FACT A (N=3 beats 100×) with FACT B (c_3 = −2 is NOT Taylor-exact) |
| **5 (settled)** | 2026-05-31 | this PR #1580 | **probe-c3-q0-stability verdict: NEAR-MATCH, not Taylor-exact. Habiro element identification is the resolution path.** | (no flip — settled) |

**Failure mode pattern:** every flip used a fresh canonical-looking formula
(`J − ℏ_q²`, `J_Hopf(q=1)`) and matched it numerically near the substrate
q_0. The "match" became "derivation" became "wired". On re-pinning q_0
(`c1f7487df` → `b3c92844d`) the "match" moved and revealed the original
formula was q_0-dependent — i.e. not Taylor-exact, just a near-match at
one anchor.

**Anti-pattern signature:** if a c_k "derivation" reports < 1% match at
muon-pin AND at proton-pin AND at any other q_0 cross-anchor — and the
match is < the difference between those anchors — it's likely
Taylor-exact. Otherwise, it's a near-match.

## Sessions log

| Date | Agent / branch | Intent | Results |
|------|----------------|--------|---------|
| 2026-05-31 | Claude / `claude/coord-infra-1ppq-2026-05-31` | (1) create this ledger + STATUS.md, (2) coord with #1577, (3) ask user about queue-schema formalization, (4) probe c_3 q_0-stability if scope permits | (1) ✓ STATUS.md + 1ppq-qbeta.md committed; PR #1580. (2) ✓ intent comment on #1577. (3) ✓ user chose: TodoItem JSON, no explicit claim, intent at branch-open, pre-work main sweep, new skills `/session-intent` + `/pending-show` + SessionStart hook. (4) ✓ **probe-c3-q0-stability SETTLED** — verdict: NEAR-MATCH, not Taylor-exact. 2.98% cross-anchor swing >> 10⁻⁵⁰ compute precision; J_Hopf(q=1)=-2 nominal mismatches empirical c_3 at both anchors by 0.48% (muon) / 3.46% (m_p). Q_β Habiro element search added as new keystone probe; old c_4/c_5-c_7 entries renamed `*-coefficients` and re-blocked on Habiro search. Audit doc: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md). Also addressed 4 Gemini review comments on PR #1580 (STATUS.md link, hook simplification x2, queue assignee). |

## Cross-refs

- CLAUDE.md §Precision goals (L1 / L2 / Subgoal-1 / Subgoal-2)
- CLAUDE.md §Q_β c_k truncation order framing
- `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`
- `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`
- `docs/audits/2026-05-30-klr-dialog-assessment.md` (recurrent re-pitch failure modes)
