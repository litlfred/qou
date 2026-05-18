# 1ppb workplan v6 — refreshed (post-PR#708 + Borromean tower landing)

**Date:** 2026-05-18
**Author:** Claude (refresh after rebasing PR #708 onto post-#695 / post-#729 main)
**Supersedes:** v5 (`2026-05-17-1ppb-workplan-v5.md`)

## TL;DR

Main has shipped two **major** results since v5:

1. **Borromean tower formula closes the m_p 1700× scale gap to 0.25 ppm**
   (commit `dc3a85500` "Scale-gap §11 RESOLUTION"). The m_p / mass-formula
   path is now structurally complete to sub-ppm at the canonical anchor;
   1 ppb is achievable in principle.

2. **y_λ at n=2..30** (sibling #695 merged) — the canonical Σ_λ y_λ · χ^λ
   pipeline now has weights cached through ⁷Li (n=21) AND beyond up
   through ¹⁰Be range (n=30). Subsumes my n=2..21 extension.

The remaining gap to 1 ppb on the per-isotope mass table is concentrated
in **the χ^λ side** (Hoefsmit at H_n for n ≥ 15) and **the residual
m_p tower terms** (T5 double-counting, T6 residue depth).

## What changed on main

| Commit | Impact |
|---|---|
| `dc3a85500` Borromean tower formula at 0.25 ppm | **m_p scale-gap resolution** (was 1700×) — critical |
| `df3bfffec` λ_scale = 5/2 - h²·G hypothesis at 5.6 ppm | λ_scale substrate-derivation |
| `11e0cb56a` Wire Borromean tower into m_p chain | ¹H lifts to `derived` |
| `2c902dba4` y_λ extension via Wenzl bridge (#695) | n=2..30 cached |
| `dc0f9394f` Cherry-pick #683 Rust canonical-chi | merged into main |
| `7f0fa726e` Remove bw-coefficient-shadow-price + LP-dual siblings | Item B BW framework deprecated |
| Multiple integration-watcher skill commits | Conjecture wiring infrastructure |

## What PR #708 contributes (this branch)

| Contribution | Status |
|---|---|
| `markov_peel` as primary fast path | ✓ shipped — unblocks ⁵Li (89s) / ⁶Li (22 min) canonical \|tr_M\| |
| Operator-valued Wenzl branching combiner | ✓ verified for A=2 at 7×10⁻¹⁵; A≥3 needs recursive ρ_ξ |
| `A_operator_extract_at_level.py` infrastructure | ✓ shipped — any (H_n, interface) |
| H_9 pp + H_9 pn A^λ_{ξν} extracts | ✓ shipped — H_9 trio complete |
| H_12 trio (pp, pn, nn) | ⏳ in flight (`bjq5agc02`, ~3-4 hrs) |
| `IsotopeRecord` schema (Python + Lean) | ✓ shipped |
| Atlas auto-render from canonical witness | ✓ shipped — atlas shows live p..⁶Li |
| `_precision` integration + active-set pruning | ✓ shipped — paper-floor-verified |

## Error budget at current main+PR #708 state

| Lever | State | Gap to 1 ppb |
|---|---|---|
| **m_p chain** | Borromean tower at 0.25 ppm (sub-ppm) | structurally closed at anchor |
| **CAL-2 propagation** | Hard floor ~780 ppb (\|∂lnE_0/∂lnq_0\|=11.09) | unfixable without sharper q_0 |
| **\|tr_M\| precision at q_0** | MPFR-50dps default; markov_peel symbolic-q | already below 1 ppb |
| **y_λ precision** | n=2..30 cached at 50 dps | already below 10⁻⁵⁰ |
| **χ^λ at H_n ≥ 15** | markov_peel feasible to H_18 (~22 min); H_21+ requires branching combiner | the binding constraint |
| **Per-isotope mass formula** | Borromean tower closes m_p; needs extension to A>1 | open |

## Active sibling-PR critical path (last 48 hrs)

| PR | Scope | My branch relationship |
|---|---|---|
| **#710** Hoefsmit per-partition audit (Geck-Pfeiffer "sleeping 10-50× win") | Optimization roadmap: G (block fusion, 3-5×, 1-2 days) → C-gate (Geck-Pfeiffer validate) → C-full (10-50× at H_12+) → D (Rust port) | **GATING** for ⁶Li/⁷Li Layer 1 feasibility |
| **#704 + #709** m_p chain Items A/B/C closure | T2+T3 at A=1 ✓; T5 double-counting; T6 divergent at A≥3 | Downstream of Borromean tower; refines m_p tower |
| **#679** ρ_K wire + Li extend | LR-derived \|tr_M\|, witness drift validator, ⁶Li/⁷Li live y_λ | **Cherry-pick candidate** — already coordinated via comment |
| **#700** χ-cache substrate cross-check | ρ_K · \|tr_M\| = m_n / m_p identity at 50 dps | Validates the canonical pipeline I'm building |
| **#702** ¹H closure via C2 inflection | Feeds m_p closure target | Downstream |

## Refreshed 1 ppb critical path

```
Borromean tower (LANDED on main, dc3a85500)
  └─ closes m_p scale gap to 0.25 ppm
     └─ enables atom-formula extension to A>1

Optimization track (parallel):
  PR #710 Candidate G (block fusion)         [1-2 days, 3-5×]
    └─ PR #710 Candidate C-gate              [1-2 days, validate Geck-Pfeiffer]
       └─ if valid: C-full (10-50× at H_12+) [1-2 weeks]
          └─ unlocks ⁶Li/⁷Li Layer 1
       └─ if invalid: pivot to Layer 2 α-cluster recursion

Operator-valued Wenzl branching track (this branch):
  H_9 trio (DONE)
    └─ enables A=2 verification (D verified at 7e-15)
  H_12 trio (IN FLIGHT, ~3-4 hrs)
    └─ enables A=3 (T, ³He) via branching combiner with recursive ρ_ξ
       └─ recursive ρ_ξ implementation needed (~100 lines)
          └─ unlocks A≥4 (⁴He via branching: <1s expected vs 22 min markov_peel)

Mass-formula track:
  T5 double-counting hunt (PR #704/#709)     [2-3 days]
    └─ refines per-atom T5 contribution at 0.1 ppb
  T6 residue-depth sweep                     [compute-heavy, lower priority]
  C2 inflection wiring (PR #702)             [feeds m_p production formula]
```

## Concrete next-action queue

1. **Finish /prepare-merge for PR #708** (in progress)
   - Steps 2+ (content integration, Lean build, final rebase + push)
   - Get Gemini + Copilot reviews
   - Estimated: 30 min foreground + CI

2. **H_12 A^λ_{ξν}(I) extraction** (background, `bjq5agc02`)
   - ~3-4 hrs wall; produces three witness files
   - Unblocks ⁴He end-to-end via branching combiner

3. **Implement recursive ρ_ξ(β_inner) in branching combiner**
   - Currently A=2 only; A≥3 needs ρ_ξ at H_{3(A-1)} via inner branching
   - Estimated: ~100 lines + tests against markov_peel reference
   - High-value (turns branching combiner from prototype → production)

4. **Coordinate with PR #710** (sleeping Geck-Pfeiffer win)
   - Their Candidate C-gate is the H_18+ unblock
   - My markov_peel covers H_18 at 22 min; GP would be ~minutes
   - Synergistic with my branching combiner

5. **Cross-check m_p via Borromean tower formula** (post-#708 merge)
   - Validate the 0.25 ppm number against the (now merged) commit `dc3a85500`
   - Confirm the formula extends to ²H..⁴He, identify the closure point for A=5+

## Out of scope for this session

- Geck-Pfeiffer Rust port (PR #710 owner's track)
- Layer 2 α-cluster recursion (research-grade, weeks)
- Full Borromean tower formula derivation (sibling thread)

## Updates to v5

- v5 framed 1ppb as gated by χ^λ precision. v6 reframes: **m_p scale gap
  is now CLOSED** by Borromean tower; the remaining work is per-isotope
  extension and operator-valued branching at scale.
- y_λ extension (was a v5 R&D item) is **SHIPPED on main** at n=2..30.
- v5's "Layer 1 canonical for A>5" remains open; v6 splits the path
  into (a) markov_peel + branching combiner (this branch) vs (b)
  Geck-Pfeiffer optimization (PR #710) as parallel approaches.
