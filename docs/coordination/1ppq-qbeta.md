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
| **c_3** | **NOT derived** — near-match (J_Hopf(q=1)=-2), 2.98% cross-anchor swing >> 10⁻⁵⁰ compute precision | `b3c92844d`, `6ace8153e`, [verdict 2026-05-31](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md); **structural reason** [order audit 2026-05-31](../audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md) (PR #1593) | **SETTLED** as near-match. The block `-2` is at order √u (ε¹); ladder c_3 is at u³ (ε⁶) — accidental coincidence. Resolution path = the scaling map f (Habiro element), not a c_3 value. |
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
  - **Sub-attack result (symbolic q-difference solve, PR #1593, 2026-05-31):** ORDER AUDIT — the per-block `Δtr_M` contributions are O(√u) (ε¹, leading −2/−1/−2) while ladder c_3 is O(u³) (ε⁶). The shared `−2` is an **accidental cross-order coincidence (5 ε-orders apart)**, not a structural identity — the root cause of the flip-flop. Sharpens the target: the Habiro element is the **scaling/eigenphase map f: Δtr_M(√u) ↦ Q_β(c_3 at u³)**, NOT a value for c_3. q₀-independence confirmed (per-block coeffs fixed rationals). Audit: [`docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](../audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md). No fitted form proposed.
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
| **6 (ruled out, not a flip)** | 2026-05-31 | claude/phi-q-spectral-combiner-2026-05-31 | Li_2^q × spectral combiner: c_3 candidate = Σ μ_λ · c_3^(λ) where μ_λ = Li_2^q(-|χ_λ|) / Σ Li_2^q(-|χ_λ'|). Σ μ_λ = 1 by construction (cures mech #6 defect). Result: c_3 cand = -1.797 vs empirical -2.07 ⟹ **REFUTED by 13%** at q_proton. | new mechanism #7 added to b502b9b83 list — not a flip-flop, never claimed as derivation |

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
| 2026-05-31 | Claude / `claude/coord-infra-1ppq-2026-05-31` | (1) create this ledger + STATUS.md, (2) coord with #1577, (3) ask user about queue-schema formalization, (4) probe c_3 q_0-stability if scope permits | (1) ✓ STATUS.md + 1ppq-qbeta.md committed; PR #1580 MERGED. (2) ✓ intent comment on #1577 (subsequently merged independently). (3) ✓ user chose: TodoItem JSON, no explicit claim, intent at branch-open, pre-work main sweep, new skills `/session-intent` + `/pending-show` + SessionStart hook. (4) ✓ **probe-c3-q0-stability SETTLED** — verdict: NEAR-MATCH, not Taylor-exact. 2.98% cross-anchor swing >> 10⁻⁵⁰ compute precision; J_Hopf(q=1)=-2 nominal mismatches empirical c_3 at both anchors by 0.48% (muon) / 3.46% (m_p). Q_β Habiro element search added as new keystone probe. Audit doc: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md). Also addressed 4 Gemini review comments on PR #1580. |
| 2026-05-31 (cont.) | Claude / `claude/qbeta-habiro-element-search-2026-05-31` | claim `probe-qbeta-habiro-element-search` after #1580 merge; structural attack on Q_β Habiro element | PARTIAL — consolidation only. Synthesized state from b502b9b83 (6 mechanisms ruled out, 1 left), d6b6e0483 (recursive pair-rules same near-match gap), qbeta_habiro_taylor_investigation (categorical f missing), qbeta_habiro_tower_1ppq (form-fitting iterative peel). Added 5 untested-but-not-falsified attack candidates to queue with pre-stated failure-mode signatures (non-uniform multi-block PRODUCT decomp, exponentiated per-block, symbolic q-diff solve, modular bootstrap, Galois descent). Queue status: in_progress (awaiting next session/sibling agent for symbolic attack). NO 7th near-match candidate proposed (avoiding flip-flop trap). PR #1585 MERGED. |
| 2026-05-31 (cont. 2) | Claude / `claude/qbeta-ck-lean-3bcond-classes-2026-05-31` | claim `probe-ck-lean-3bcond-classes`; add Lean §3b-cond classes for c_4–c_7 mirroring c_3 pattern | IN PROGRESS — added classes + axioms + Q_beta_nk_categorical + q_beta_nk_structural_form for k=4,5,6,7 to content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.lean (~188 lines added). Closed forms taken verbatim from existing canonical instance; no instances of new classes provided (matching c_3 discipline). PR #1587 opened. Lean LSP couldn't start locally (toolchain install blocked); CI verification pending. |
| 2026-05-31 (cont. 3) | Claude / `claude/qbeta-habiro-symbolic-solve-2026-05-31` | pick up the **symbolic q-difference solve** sub-attack deferred by #1585 (cont.) | CHARACTERIZATION (no closure) — ORDER AUDIT via exact symbolic ε-series of the per-block `Δtr_M` closed forms vs the ladder variable u=b·ℏ². Found: per-block forms are O(√u) (ε¹, leading −2/−1/−2) while ladder c_3 is O(u³) (ε⁶) — the shared `−2` is an **accidental cross-order coincidence (5 ε-orders apart)**, not a structural identity, which is the **root cause of the 4-session flip-flop**. q₀-independence diagnostic: per-block coeffs are fixed rationals (anchor-invariant) ⇒ the empirical c_3 swing lives entirely in the open categorical map f. Sharpens the open problem: the Habiro element is the **scaling/eigenphase map f: Δtr_M(√u) ↦ Q_β(c_3 at u³)**, NOT a c_3 value. No fitted form proposed. Probe `qbeta_multiblock_order_audit.py`; audit `docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`; PR #1593. |

## Cross-refs

- CLAUDE.md §Precision goals (L1 / L2 / Subgoal-1 / Subgoal-2)
- CLAUDE.md §Q_β c_k truncation order framing
- `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`
- `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`
- `docs/audits/2026-05-30-klr-dialog-assessment.md` (recurrent re-pitch failure modes)
