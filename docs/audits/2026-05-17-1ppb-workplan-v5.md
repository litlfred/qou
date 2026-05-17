# Refocused 1-ppb workplan v5 — post Wenzl LR + chi-cache (2026-05-17)

> **Predecessor:** [`2026-05-17-1ppb-workplan-v4.md`](2026-05-17-1ppb-workplan-v4.md)
> **Coordination ledger:** [`docs/coordination/1ppb.md`](../coordination/1ppb.md)

## 1. Reframe (user direction, this session)

**1 ppb = compute-precision target** (internal cross-method
agreement at substrate `q_0`). Distinct from the **experimental
~780 ppb CODATA `Q_β` floor** on absolute mass predictions.

| Target | Status (post-#682 + #683) |
|--------|---------------------------|
| **1 ppb compute precision** for `|tr_M|` | **4-way cross-check passes** for p/n/D at 1e-15 (Hoefsmit / markov_peel / chi-cache Python / canonical-chi Rust) |
| ~780 ppb experimental floor | unchanged — `Q_β` substrate-derivation declined |

User direction (PR #683 review):
> *why f64 ---> only do arbitrary precision w/ ≥ 50 dps*

The canonical-chi-rust path was upgraded from f64 default to
MPFR-50dps default (this PR). f64 retained as `--dps 0` fallback.

## 2. Status snapshot

### Merged during the session
- **PR #674** Wenzl LR Rust producer (canonical-crossing aware, rayon)
- **PR #678** ρ_K consumer using LR
- **PR #664** c_3 = J_Hopf(q=1) = -2 categorical (Story A falsified)
- **PR #680** k=3 staircase EW probe (negative finding)
- Various Lean axiom-discharges, gemini fixes

### Open at v5 time

| PR | Status | Layer | Relation to this workplan |
|----|--------|-------|--------------------------|
| **#683** (mine) | open, in-flight | canonical-χ Rust (MPFR-50dps default) | Step 2 Rust path; companion to #682 |
| **#682** | open | canonical-χ chi-cache (Python sympy reader) + Li₂^q | Step 2 Python path; closes #681 |
| **#681** (mine) | open | Step 1 audit | predecessor for #682/#683 |
| **#679** (mine) | open | ρ_K → LR wiring + ⁶Li/⁷Li | consumer side; cherry-picks #663's drift validator |
| **#671** | open (docs) | m_p chain closure gap | identifies Items A/B/C |
| **#663** | open | anti-staleness infra | drift validator + ¹H tautology fix |

## 3. Critical-path graph (v5)

```
                  ┌──── Tier 1 (compute 1 ppb) — ACHIEVABLE ────┐
                  │                                              │
                  ▼                                              ▼
  4-way |tr_M| cross-check at q_0                      Wenzl LR producer (#674)
  (Hoefsmit / peel / chi-cache / Rust)                          │
  PASSES at 1e-15 for p/n/D                                     ▼
            │                                          chi-cache combiner (#682)
            │                                          Rust canonical-χ MPFR (#683)
            ▼                                                   │
  T/³He/⁴He chi caches + canonical |tr_M|◄─────────────────────┘
            │
            ▼
   ρ_K^LO tautology exposed (#678/#679 merged)
            │
            ▼
   ρ_K^full second-order Δ_λ correction ────► Tier 4 (open R&D)


   ┌──── Tier 2 (m_p chain closure) — UNCLOSED (#671) ────┐
   │                                                       │
   ▼                                                       ▼
   Item A: T2+T3 at A=1 KeyError      Item C: full Habiro residue
   (cheap probe, days)                 (cheap probe, days)
            │                                       │
            └──────────────┬─────────────────────────┘
                           ▼
                Item B: T5 categorical attribution
                (open R&D, weeks)
                           │
                           ▼
              ¹H lifts from `derivation_pending` → `derived`
              (M_P_DERIVED_MAX_REL_DIFF: 1% → 1 ppb)


   ┌──── Tier 3 (Q_β precision ladder) — STRUCTURALLY FORCED ────┐
   │                                                              │
   ▼                                                              ▼
   c_2 = b²  ✓ (merged)         c_3 = J_Hopf(q=1) = -2  (#664 open)
                                       │
                                       ▼
                                c_4 = b² + 1/2  ✓ (merged)
                                       │
                                       ▼
                                c_5, c_6  — no known closed form (open)
```

## 4. What's closeable NOW

Ordered by yield × tractability (compute-precision side first since
that's the 1 ppb gate per user's reframe):

1. **MPFR-50dps end-to-end agreement audit** for the 4-way `|tr_M|`
   cross-check on p/n/D. PRs #682 and #683 both claim 1 ppb but
   need a single witness emitter that runs all four paths at MPFR
   50 dps and asserts pairwise relative diff < 1e-9. Half-day after
   #682 + #683 merge.

2. **`per_irrep_pole_atom.py` chi-cache continuation for T/³He/⁴He**
   via the Rust canonical-χ MPFR binary (#683). The Rust path
   produces 50-dps decimal strings per partition; the Python
   `per_irrep_pole_atom` cache format is sympy-symbolic. Adapter
   needed. Day to write + days of compute for ⁴He at H_12.

3. **Investigate the ~14-digit precision floor in
   `seminormal_mpfr` internals** (PR #683 finding). The Rust
   binary at `--dps 50` should produce 50-dps |tr_M| but currently
   agrees with Hoefsmit only to ~14 sig figs. Suspected: a `sqrt`
   or eigenvalue in `build_blocks_mpfr` evaluated at lower
   precision. Tracked as a focused Rust internals issue.

4. **m_p chain Item A** (T2+T3 KeyError at A=1). Cheap probe,
   blocks #671's ¹H closure path. The structural question is whether
   T2+T3 are zero at A=1 by construction (which would explain the
   KeyError) or whether `mass_endomorphism.py` has a coverage gap.

5. **m_p chain Item C** (full Habiro residue at A=1). Probe whether
   the existing T6 ~ 0.68 is a truncation of a larger series; if
   so, extending the series may close part of the m_p gap.

6. **Witness drift gate hardening** (cherry-pick from #663). My
   #679 cherry-picked `witness_dependency_drift.py` standalone;
   adopting it across the four routinely-drifting audit witnesses
   would catch upstream-dependency staleness in CI.

## 5. Not closeable without more work

| Item | Blocker |
|------|---------|
| m_p Item B (T5 categorical attribution) | No known ansatz; open R&D, weeks |
| c_5 / c_6 categorical formulas | No known closed form (Story B's open frontier) |
| ρ_K^full Δ_λ second-order correction | Δ_λ derivation racing across PRs #602/#603/#613 |
| `BlochSuslinUniqueness` instance | Mathlib `Real.dilog` + Suslin map upstream |
| ⁶Li/⁷Li canonical \|tr_M\| | y_λ cache only covers n=2..12; need numerical-q live compute (~minutes/atom) OR cache extension |

## 6. Open governance questions

| # | Question | Carry-forward from |
|---|----------|-------------------|
| Q1 | Promote substrate `Q_β = 0.7825728 MeV` to CAL-3 = output? | v3, v4 |
| Q2 | Staged tightening of `M_P_DERIVED_MAX_REL_DIFF` (1% → 1 ppm → 1 ppb) | v4 |
| Q3 | Tier-3 PSLQ scope (defer or pursue?) | v4 |
| Q5 | Python vs Rust for ⁴He chi cache | **resolved (this session)**: both, complementary |
| Q6 (NEW) | What's the right MPFR precision floor in `seminormal_mpfr` for QOU's 1 ppb gate? PR #683 finds the chain agrees with Hoefsmit only to ~14 digits despite `--dps 50` request. Is this an actual `seminormal_mpfr` precision bug, or a difference of conventions (e.g. different `n` strands, sign of trace)? | v5 |
| Q7 (NEW) | The Wenzl LR producer (#674) ships a tensor-product χ^λ binary that's correct for tensor-product braids but wrong for canonical atomic braids. Should the binary be renamed (`hecke-tr-m-wenzl-lr` → `hecke-chi-tensor-product`) to avoid future misuse? | v5 |

## 7. Coordination map (open PRs vs this workplan)

| Tier | Driving PRs (open) | Driving PRs (merged) |
|------|--------------------|----------------------|
| 1 (compute 1 ppb) | **#682, #683** + finishing-caches | #674, #678 |
| 2 (m_p closure) | **#671** (audit-only), Items A/B/C pending separate PRs | — |
| 3 (Q_β ladder) | **#664** (c_3) | #661 (c_2), c_4 (merged earlier) |
| 4 (ρ_K^full) | — (Δ_λ race) | #564 (ρ_K^LO) |

## 8. Next-session high-value moves

1. **Push #683 to merge** — Rust MPFR path is the compute-precision floor.
2. **Coordinate #682 ↔ #683 merge** — both deliver Step 2 from different angles. They don't conflict (disjoint files). Either order works; #682 first is more natural since it includes the 3-way cross-check witness; my Rust then adds the 4th path on top.
3. **Investigate Q6** (MPFR floor) — focused Rust-internals work; may need a `seminormal_mpfr::build_blocks_mpfr` audit.
4. **Item A probe** (m_p T2+T3 KeyError) — single-script repro then a localised fix.
