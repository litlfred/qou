# Δ_λ closure (Option-E) — master ledger

> Single source of truth for the **Δ_λ closure / per-isotope binding**
> goal. Per CLAUDE.md L2 Subgoal-1: this is the closure path
> ("per-isotope Borromean-tower extension + operator-valued branching
> combiner") that unlocks the 100× targets above the CAL-2 floor.

## Why this ledger exists

Six prior Δ_λ ansätze failed (Frobenius co-Casimir, Demazure-fibre,
LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov). CLAUDE.md
§Precision goals records that any 7th fit-based ansatz "will be caught
by the three-calibration discipline review". The productive direction
is **Option-E** (Kashiwara crystal) — the §L2 Δ_λ-gate context doc
explicitly endorses it as a non-fit-based attack.

Like the c_k flip-flop saga (`docs/coordination/1ppq-qbeta.md`),
Option-E has cycled through versions v1..v9 with progressively-closer
near-matches. v9 hit 0.11% on the A=3 mirror pair via a `(1+q)/2`
correction factor selected from substrate candidates — concerningly
similar to the "search for a clean-looking formula" pattern that
flip-flopped c_3 four times.

This ledger pins the current state so the next session doesn't
re-discover already-tried directions.

## Status (as of 2026-05-31)

| Sub-goal | Status | Evidence | Open question |
|----------|--------|----------|---------------|
| **Deuteron Δ_λ closure** | **CLOSED** (+0.91% via E₀ × q⁻¹) | PR #1367, audit `2026-05-26-delta-lambda-binding-formula-closure.md` | none — the only honestly-closed light nucleus |
| **Per-nucleon binding (T, ³He, ⁴He, ⁶Li+)** | NOT derived | retraction PR #1386 documents the backhanded-fit attempt | structural derivation required |
| **A=3 mirror pair (T − ³He)** | NEAR-MATCH at 0.11% | v9 commit `30c5393b7` | is `(1+q)/2` correction Taylor-exact / structurally-derived, or another near-match? |
| **A=4 (⁴He)** | NOT derived | various probes 2026-05-25 thread | requires multi-nucleon extension of the v9 mirror-pair formula |
| **A ≥ 5 (⁶Li, etc.)** | NOT derived | — | depends on lower-A closures |

**Reading:** the deuteron is closed by a STRUCTURAL formula
(`B(D) = m_e × |Σ_λ y_λ · χ^λ(β_D) · sgn(w_0^{S_{λ'}}) · f^λ|` with
`f^λ = dim(V_λ)`, the regular-rep dimension). The A=3 mirror pair is
near-matched but not closed. **Critical:** the v9 (1+q)/2 factor was
selected from a substrate-candidate list, NOT derived. Treat as
near-match per CLAUDE.md "Don't propose a seventh fit-based ansatz"
discipline.

## v1..v9 progression (DO NOT REPEAT failed paths)

| v | Approach | Best residual | Verdict |
|---|----------|---------------|---------|
| v1 | simple stats | 65.6% (D-only) | refuted |
| v2 | BK content sum | 17.4% (D-only) | refuted (coincidence) |
| v3 | multi-isotope content | 70-87% | refuted |
| v4 | naive q-Reeb | ~95% (all) | refuted |
| v5 | canonical free-vs-atom | ~99% (growth missing) | refuted |
| v6 | mirror-pair + μ₀ | 81% | refuted |
| v7 | transpose + m_π | 58% | refuted |
| v8 | transpose + Z↔N + m_π·ℏ_q | 6.15% | partial — within 10% |
| **v9** | **+ (1+q)/2 correction** | **0.11% (stale) → +0.12% (canonical q₀, PR #1707)** | **NEAR-MATCH (fit) — PROBE 1 tested; structural derivation REFUTED; A=3 closure OPEN** |

Each version's witness lives at
`folio-assistant/computations/option-e-v{N}-*.witness.json`.
The witness commitSha pins which session produced the value.

## v9 canonical closure formula (NEAR-MATCH, not yet derived)

```
B_T − B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2
```

| Component | Source | Status |
|-----------|--------|--------|
| `m_π` | CAL-3 pion mass | derived (input) |
| `ℏ_q = (q-1)/q` | substrate q₀ | derived |
| `(1+q)/2` | **NEAR-MATCH** | selected from substrate candidates; 0.11% off the required closure factor 1.05605 |
| `y_λ · χ^λ(β_T)` | Markov weights × Hoefsmit characters | computed (on disk) |
| `(χ^λ(β_T) + χ^{λᵀ}(β_³He))/2` | bar-symmetric (transpose-pair) | structural — partition transpose is the right family |

**Failure-mode signature for v10+**: if a new "substrate candidate"
matches the closure factor at the proton-pin q₀ but moves on re-pinning
to muon-pin q₀ (see `q_muon_at()` cross-check in
`tools/qou-substrate/python/qou_substrate/constants.py`), it's another
near-match. Do NOT wire as a derivation.

## Open probes

- [x] **PROBE 1 — Derive `(1+q)/2` structurally** from the categorical
  action. **TESTED → NEAR-MATCH (fit)** (PR #1707, audit
  `2026-06-02-option-e-derive-1plusq-over-2.md`). Verdict: `(1+q)/2` is
  NOT structurally forced. All four hypotheses fail: the σ_1 standard-rep
  trace (= h, −80%), its half (h/2, −90%), the Hoefsmit seminormal
  diagonal `1/[2]_q` (−53%) and off-diagonal `√([3][1])/[2]` (−18%), and
  the (2,1)-block symmetric-channel projector `q/[2]_q` (−48%) all land
  18–90% away. The only "matches" are `[2]_q/2` (unbalanced) and
  `(q+1)/2` — tautologies (literally `(1+q)/2` renamed), not independent
  derivations. The DECISIVE test: the required closure factor
  `R = target/(m_π·ℏ_q·S) = 1.05372` ≠ `(1+q)/2 = 1.05499` by **+0.12%**
  at the SAME pin — not an algebraic identity. Staleness: the published
  0.11% used the stale muon-anchor literal `1.1097090249`; at canonical
  proton q₀ the residual is **+0.12%, sign-flipped**. Corroborates the
  prior PARTIAL record (#1579 chirality-odd narrative; #1581 33-candidate
  scan). `(1+q)/2` stays un-wired; A=3 closure OPEN. No v10 ansatz.

- [ ] **PROBE 2 — A=4 extension** of the v9 mirror-pair formula. The
  mirror-pair symmetry collapses at A=4 (no canonical mirror partner
  for ⁴He). Need a different categorical operation. Per audit
  `2026-05-26-delta-lambda-binding-formula-closure.md`: ⁴He requires
  the multi-nucleon interface operator, not just the mirror.

- [ ] **PROBE 3 — Lean §3b-cond class for the v9 closure** if it
  becomes Taylor-exact. Pattern: `class OptionEV9MirrorPairClass : Prop`
  with field axiomatising the formula. NO instance until PROBE 1 closes.

- [ ] **PROBE 4 — `Δ_λ` from Kashiwara crystal** (the original
  Option-E motivation). The v9 substrate-search may have empirically
  hit the crystal weight without deriving it. Worth tracing
  `(1+q)/2` against known Kashiwara-crystal coefficients (Lecouvey,
  Brundan-Kleshchev).

## Anti-patterns (DO NOT repeat)

- ❌ Q-factorial ratio (`q⁻^A · δ_tr · A(A-1)/2`) — RETRACTED per PR #1386 as backhanded fit. The actual `Δtr(⁴He)/Δtr(D) = 0.67`, not the 12.7 the q-factorial implied.
- ❌ Single-nucleon Δ_λ derivation (audit `2026-05-26-...`): misses the multi-nucleon interface operator.
- ❌ q-dependent algebraic Δ_λ at the Cat layer (audit ibid): mixes Cat and Alg layers. The Cat-layer Δ_λ is q-independent (sign × dim).
- ❌ Seventh fit-based ansatz (CLAUDE.md §L2 explicit ban). The v9
  `(1+q)/2` factor is borderline — it's clean enough to look canonical
  but was SEARCHED for, not derived. Treat as near-match.

## Active PRs

| PR | Scope | Status |
|----|-------|--------|
| #1516 | Option-E Phase 2 entry-point probe + Phase 1 doc update (pivoted to H_n generalisation) | open |
| #1697 | **Option-E Phase 1 H_n generalisation** — per-block Hoefsmit-seminormal ρ_λ(σ_k) and ρ_λ(w_0) at H_3 + H_6 (deuteron); 11 partition blocks; 4 assertions pass | open |
| #1698 | Subgoal-1 m_avg operator-valued combiner (Wenzl branching) — touches `BraidKnot/OperatorValuedCombiner.lean`; no file overlap with #1697 but shares Markov-trace path | open |
| #1707 | **Option-E PROBE 1** — derive `(1+q)/2` structurally or falsify as near-match; just opened, stub-only audit doc | open |
| (this PR) | Option-E master ledger backfill | open |

## Sessions log

| Date | Agent / branch | Intent | Results |
|------|----------------|--------|---------|
| 2026-05-31 (cont. 3) | Claude / `claude/coord-ledgers-option-e-followup-2026-05-31` | (1) backfill this ledger from v1..v9 commits + existing audits, (2) document v9 near-match status honestly with failure signature for v10 | landed (1) + (2); did NOT propose v10 to avoid 7th-ansatz trap; PROBE 1 (derive (1+q)/2 structurally) is the next-session keystone. |
| 2026-06-02 | Claude / `claude/option-e-derive-1plusq-over-2-2026-06-02` (PR #1707) | PROBE 1: DERIVE-OR-FALSIFY the v9 (1+q)/2 — refresh at canonical q₀, test 4 structural hypotheses, proton-vs-muon discriminator | **VERDICT NEAR-MATCH (fit)**. (1+q)/2 NOT forced: 4 independent hypotheses 18–90% off; only tautological [2]_q/2 / (q+1)/2 "match". Required factor R=1.05372 ≠ (1+q)/2=1.05499 by +0.12% same-pin. Published 0.11% was stale (muon literal); canonical-q₀ residual +0.12%, sign-flipped. No v10. (1+q)/2 stays un-wired; A=3 closure OPEN. |
| 2026-06-02 | Claude / `claude/option-e-phase1-gram-h6-2026-06-02` | Phase 1 H_n Gram-matrix generalisation at H_6 (deuteron) — deliver the per-block Hoefsmit-seminormal infrastructure that #1516's doc update identified as missing. Pure-Python, no pyhecke_native dep. | landed (PR #1697); 11 H_6 partition blocks with σ_k matrices + ρ_λ(w_0) at q_0; 4 assertions pass (χ_λ cross-check residual 2.22e-16 at H_6, Σ dim_λ² = n! at both n=3,6). Witness `option-e-phase1-gram-h6.witness.json` carries the data needed to test **PROBE 1** ("`(1+q)/2` = half-trace of σ_1 in standard rep") on the (5,1) standard rep of H_6 — not run in this PR (scope = infrastructure). |
| 2026-06-02 | Claude / `claude/option-e-derive-1plusq-over-2-2026-06-02` | Open **PROBE 1** — derive `(1+q)/2` structurally or falsify as near-match. Per ledger §"Open probes" line 85. | in flight (PR #1707, stub-only commit; coord posts cross-published on #1697 and #1707; canonical q_0 confirmed not stale; can consume #1697's `option-e-phase1-gram-h6.witness.json::data.h6.blocks["5_1"]` data for the half-trace hypothesis test). |
| 2026-06-02 | Claude / `claude/option-e-probe4-closure-deuteron-2026-06-02` (PR #1719, stacked on #1714 KL scaffold) | **PROBE 4 closure test on deuteron** — exhaustively test Δ_λ closure ansätze: KL-cell trivial-multiplicity (Step A) + quantum-dim weighted (Step B-2) + W-graph edge-weight μ(y,w) (Step B-1) + measure-level pivot to \|content_λ\| per sibling triage (Step C). | **REFUTED (all 4 + 5 = 9 variants):** Step A v1/v2: +6.007/+1.162 (238% / 127% miss, wrong sign). B-2 qdim a/b: +7.902/+2.122 (282% / 149%). B-1 W-graph a/b/c: +26.285/+26.285/+5.968 (704% / 704% / 237%). Step C 1-5: +411/+2258/+11.2/+4.11/+109 (9552% / 51987% / 357% / 194% / 2602%). **Best: Step C-4 (y_λ·χ·\|content\|) at 194 % miss, still wrong sign.** Combined with cumulative refutation pile (cheap-pass #1516, `rho_w_crystal_vertex_trace.py`, #1709 volume-Wedderburn, sibling commits d7c56c17e1/5e388f598b/d59bcb79de/ba7af156cb on main): **Option-E is structurally exhausted on the deuteron within the standard categorical framework**. Pivot recommended: GAP-A-3/A-4 per CLAUDE.md §L2 (categorical brane-tower level selection / ρ general rule). Step B-3 (Type-B folded crystal) queued but unlikely to close given the cumulative magnitude of the miss. |

### Cumulative refutation pile on deuteron Δ_λ closure (2026-06-02)

For the next session orienting on Option-E: **don't re-run these probes** — the verdict is firm.

| Probe | Variant | S (vs target −4.353) | rel_err | Witness |
|-------|---------|----------------------|---------|---------|
| #1516 cheap-pass | C: sgn·dim_λ | best of 4 | **66%** | `probe-option-e-phase2-crystal-vertex-candidates.witness.json` |
| Upstream main | `rho_w_crystal_vertex_trace.py` (regular-multiplicity Σ_w ρ_w = χ^λ trace identity) | does_not_close | n/a | `rho-w-crystal-vertex-trace.witness.json` |
| #1709 volume-Wedderburn | clausen_content | best of 5 | **99.7%** | `volume-wedderburn-delta-lambda.witness.json` |
| #1719 Step A | v2 (single left cell, Δ_λ = χ^λ) | +1.162 | **127%** | `probe-option-e-step-a-kl-cell-collapse.witness.json` |
| #1719 Step C-4 | y_λ · χ · \|content_λ\| | +4.11 | **194%** ← best Step C | `probe-option-e-step-c-content-weighted.witness.json` |
| #1719 Step A | v1 (whole 2-sided cell, Δ_λ = f^λ · χ^λ) | +6.007 | **238%** | (same as Step A) |
| #1719 Step B-1c | per-w direct μ-degree | +5.968 | **237%** | `probe-option-e-step-b1-wgraph-weight.witness.json` |
| #1719 Step B-2a | qdim_λ(q_0) replaces f^λ | +7.902 | **282%** | `probe-option-e-step-b2-quantum-dim-weighted.witness.json` |
| sibling main d7c56c17e1 | abs_content A-growth ratio | matches D/T/³He/⁴He growth | 5% on **ratio** (not absolute) | `probe-binding-measure-search.witness.json` |
| sibling main 5e388f598b | full-order θ_λ, y_λ wrong-measure diagnosis | n/a | n/a | `probe-full-theta-binding.witness.json` |

**Convergent verdict across 10+ structural variants from 4 independent sessions/PRs**: standard Option-E (KL cells + Kashiwara crystal + canonical-basis trace) cannot close Δ_λ(D) on the deuteron under any of: trivial / multiplicative-cell / quantum-dim / W-graph-edge-weight / |content_λ|-weighted assemblies. The Δ_λ-structure variants and the outer-measure variants are BOTH refuted independently. Closure requires either:

1. A **fundamentally different structural object** beyond the standard categorical framework (e.g., 6j-symbol quantum volume per #1709's remaining direction), or
2. **GAP-A-3 / GAP-A-4 pivot** per CLAUDE.md §L2: categorical brane-tower level selection / ρ general rule (not in the H_n / S_n algebra at all).

## Cross-refs

- `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md` — deuteron closure (PR #1305 + #1367)
- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — the §L2 Δ_λ-gate context (Track A blocker)
- `docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md` — original Option-E motivation (Kashiwara crystal)
- `docs/audits/2026-05-19-delta-lambda-phase4-z4N-closure.md` — early Z⊕N closure attempts
- `docs/audits/2026-05-19-delta-lambda-thread-closure.md` — six-ansatz failure record
- `folio-assistant/computations/option-e-v9-all-symmetries.witness.json` — v9 witness
- `folio-assistant/computations/option_e_v9_all_symmetries.py` — v9 source
- CLAUDE.md §Precision goals (L2 Δ_λ gate; Track A blocker; Subgoal-1 closure path)
- `docs/coordination/1ppq-qbeta.md` — parallel flip-flop saga (c_k near-matches)
