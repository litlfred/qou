> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# Tier 3 — final state

**Branch**: `claude/tier3-math-audit-B0wyO`
**PR**: [#499](https://github.com/litlfred/qou/pull/499)
**Parent**: `claude/audit-math-framework-FXlp2` (PR #498)
**Workplan**:
[`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)

This doc closes out the audit-and-fix pass on
`claude/tier3-math-audit-B0wyO`. The branch grew well beyond its
original P3 scope into a multi-phase audit covering P0, P1, P2,
P3 items. As of the current commit, the empirical-flag
inventory is closed (modulo MAG-1's pending numerical
verification) and the principal compute-pipeline correctness
issue (H_3-at-H_{3A} weights) is fixed at the descended-carrier
level via P2.2a + P2.2b wiring.

## Empirical-flag scoreboard — final

| Flag | Status | Notes |
|------|--------|-------|
| **CAL-1** ($m_e$) | 🟢 approved | leptonic mass scale |
| **CAL-2** ($m_\mu/m_e \to q_0$) | 🟢 approved | dimensionless ratio (substrate parameter) |
| **CAL-3** ($Q_\beta(n) \to E_0$) | 🟢 approved | hadronic energy scale |
| **NU-1** | 🟢 resolved | neutrino = unknot, $\mathfrak{m}(\mathbf{1}) = 0$ |
| **SHELL-1** | 🟢 resolved | no hidden AME fits; quarantines explicit |
| **BW-8** (Hook coeff) | 🟢 resolved | q-hook product $H_q((2,2)) = [3]_q[2]_q^2$ via wigner-np-pairing |
| **BW-11** (pn corr) | 🟢 resolved | Wenzl-bridge $y_{(4,1)} + y_{(2,1,1,1)}$ at $n=5$ |
| **ALPHA-2** ($1/\alpha$) | 🟢 resolved | live form $45[3]_q(1+\delta_{CS}+8q\delta_{CS}^2)$ at 6.7 ppb < CODATA 21 ppb |
| **MAG-1** (magic numbers) | 🟡 framework path | PR #500 (full-twist + BB-stratification + LR-fusion); numerical verification on $\{50, 82, 126\}$ pending |

**8 of 9 flags closed; 1 has a concrete homological framework awaiting numerical verification.**

## Workplan items — final

### Closed on this branch

| Task | Resolution |
|------|------------|
| P0.1 Wall-violation sweep | [`2026-05-01-wall-violations-sweep.md`](2026-05-01-wall-violations-sweep.md); 4 real risks (all P0.2-discharged); pipeline tool |
| P0.3 JSJ algebraic reformulation | `prop:phi-q-tower-algebraic-stratification` triple |
| P0.4 Three-calibration-inputs block | `prop:three-calibration-inputs` triple aligned to Wedderburn channels |
| P1.5 Compound-shell base-case audit | [`2026-05-01-base-cases-audit.md`](2026-05-01-base-cases-audit.md); SHELL-1 resolved |
| P1.6 Neutrino mass | NU-1 resolved (neutrino = unknot) |
| P1.7 1/α residual | ALPHA-2 resolved (6.7 ppb < CODATA) |
| P2.2a Wedderburn at $H_{3A}$ — descended | `tower_mass_symbolic_eval` calls `global_wedderburn_sum_symbolic` |
| P2.2b Wedderburn at $H_{3A}$ — Φ_q tower | per-stratum sums (this branch) + per-nucleon (parent's per-braid tower, cherry-picked) |
| P2.6 GS-filtration narrative blocks | `prop:graded-markov-trace-from-gs-filtration` + `prop:residue-at-root-from-gs-filtration` triples |
| P3.1 Conjectural-propagation sweep | Pipeline tool + report; cones 259 → 119; 6 demotions + bridge cleanup |
| P3.6 BW pathway equivalence | [`2026-05-01-bw-pathway-comparison.md`](2026-05-01-bw-pathway-comparison.md) (scoping; keep all three pathways) |

### Open / queued

| Task | Status | Next-step |
|------|--------|-----------|
| **P0.2** algebraic-quantum-volume recast | 🟡 cherry-pick needed | Wall-sweep candidates `geom-yekutieli-alignment.md`, `geom-universality.md`, `eos-borromean-cfl.md` need recast to use `algebraic-quantum-volume` instead of `Vol(K)`. The recast itself is on a sibling branch (TBD); once located, cherry-pick + caller update closes 4 wall-violations |
| **P1.1(a)** Substrate parameter algebraic upgrade | 🟡 research-grade | Close the `q-from-epsilon → substrate-parameter-unique → vacuum-substrate-compatibility` chain. Optional upgrade — paper's three-calibration position is correct as-is. ~1 week of theory |
| **P1.4** Magic numbers from Bring (MAG-1 numerical) | 🟡 framework cherry-picked | PR #500 cherry-picked here as the framework. Numerical witnesses on $\{50, 82, 126\}$ via BB-spectral-sequence collapse computation — separate branch / PR |
| **P2.1** Full Wedderburn channels in `crt_markov.py` | 🟢 assessed; SW extension queued | [`2026-05-02-p2-1-migration-assessment.md`](2026-05-02-p2-1-migration-assessment.md). The descended carrier and Φ_q tower terms now use proper SW (P2.2a/b). Remaining 9 callers of legacy `markov_trace_symbolic_eval` are mostly diagnostics or use dressed-quark differentiation that the SW path doesn't yet wire. Migration blocked on extending SW char_kind to accept `m_pp/m_pn/m_nn`; tracked as follow-up |
| **P2.3** Word-shortcut undo functions L4–L7 | ✅ done | All 7 levels implemented in [`confinement_shortcuts.py`](../../computations/confinement_shortcuts.py). Self-test exercises every level (¹⁶O at L4 → 191 crossings; H₂ at L7 → 23 crossings) |
| **P2.4** Multi-level SDP | 🟡 unblocks shell-closure | Current `sdp_cross_channel.py` is generic-(Z, N) but only pair-coupling granularity. L4–L7 constraint families still needed. ~2 weeks; out of scope for audit pass |
| **P2.5** Symbolic-in-q paper-wide | 🟡 5/125 migrated; codemod plan documented | [`2026-05-02-p2-5-symbolic-in-q-migration.md`](2026-05-02-p2-5-symbolic-in-q-migration.md). Exemplar `alpha_k_via_wenzl_bridge.py` migrated this branch; 51 trivial-tier scripts codemod-able; 37 moderate; 33 complex. Phase plan documented |
| **P3.2** Pentagon $uv = q\,vu$ lemma | 🟡 needs author scope | Workplan formula has trace-level vs operator-level ambiguity (see Tier 3 progress §P3.2). Recommend author confirm intended scope before proceeding |
| **P3.3** Pair descent sharpness | 🟡 depends on P3.2 | Empirical evidence in `adjacent-vs-full-probe.witness.json` shows $\mathcal{P}_n = \{(i,j)\}$ all-pairs gives sub-1% on light atoms; formal sharpness proof open |
| **P3.4** Uniform $\Delta_{\max}$ bound | 🟡 compute prereq missing | `multi-level-jet-sum.witness.json` reports `multi_level_implemented: false`. Path-(b) numerical evidence blocked behind P2.1 / P2.3 |
| **P3.5** family-4 motivic instance | 🟡 research-grade | Derive local Frobenius eigenvalues from the brane tower. Open-ended |

## Branch state

- **Commits ahead of `claude/audit-math-framework-FXlp2`**: ~44
- **New `.ts` / `.md` / `.lean` triples**: 5+ on this branch (three-calibration-inputs, phi-q-tower-algebraic-stratification, graded-markov-trace-from-gs-filtration, residue-at-root-from-gs-filtration, n-v-leading-order-derivation demoted) plus those cherry-picked from PR #500 + mass-units-bridge-followups (~12 more)
- **New audit docs**: 8
  - `2026-05-01-conjectural-propagation-sweep.md`
  - `2026-05-01-tier3-progress.md`
  - `2026-05-01-calibration-inputs-addendum.md`
  - `2026-05-01-bw-pathway-comparison.md`
  - `2026-05-01-wall-violations-sweep.md`
  - `2026-05-01-base-cases-audit.md`
  - `2026-05-02-p2-5-symbolic-in-q-migration.md`
  - this doc
- **New pipeline tools**: `content/pipeline/conjectural-propagation-sweep.ts`, `content/pipeline/wall-violations-sweep.ts`
- **Compute artifacts**: P2.2a wiring witness, P2.2b verification, refreshed per-braid-tower witness, refreshed sweep reports

## Recommendation

The branch is in a stable, mergeable state. The empirical-flag
closure (8 of 9) and the H_{3A} weight-bug fix at the descended
carrier are the two highest-impact deliverables; both are landed.

The remaining workplan items split cleanly into:

1. **Bookkeeping** (P2.5 codemod, P0.2 cherry-pick) — mechanical,
   needs separate focused branches.
2. **Compute work** (P2.1 sweep, P2.3 undo functions, P2.4
   multi-level SDP, MAG-1 numerical) — substantial implementation
   in separate branches.
3. **Research** (P1.1, P3.2, P3.3, P3.4, P3.5) — open-ended,
   needs author input or new mathematical results.

None of these block merging the current PR; they're follow-ups
that can be sequenced after the audit-and-fix pass lands.
