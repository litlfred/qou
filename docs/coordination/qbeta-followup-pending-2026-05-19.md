# Q_β precision-ladder follow-up — pending items from PR #777

**Date:** 2026-05-19
**Parent PR:** [#777](https://github.com/litlfred/qou/pull/777) (closing-summary entry in [`1ppb.md`](1ppb.md))

This branch tracks items deferred from #777 that were marked
"separate PR scope". Each item below is a candidate work unit;
pick one (or several) and develop on a sub-branch.

## Open research-grade items (c_4..c_7 first-principles derivation)

PR #777 established that c_3 = -2 = J_Hopf(q=1) is proved (Fact 3,
2-strand sub-braid argument), but c_4..c_7 remain **empirical
numerology** with categorical interpretations only at leading order.
Two viable research paths:

### Path A — Khovanov-Rozansky polynomial at finite q

- [ ] Identify the specific link L = closure of typed-B_3 braid for β_n / β_p (referenced in `chi-per-irrep-cyclotomic-closed-forms.md` cyclotomic-factor pattern)
- [ ] Compute Khovanov polynomial Kh(L)(q, t) at finite q (not just q=1 specialisation; not just rank). Requires either:
  - Tabulated Khovanov polynomials from Bar-Natan's KnotAtlas
  - Custom Khovanov cube-of-resolutions implementation
- [ ] Taylor-expand Kh(L)(q, t) around q=q_0 (substrate) with t=-1 (Jones-decategorification limit). The expansion coefficients should match the empirical c_4..c_7 if the cohomological-strata hypothesis holds.
- [ ] Cross-check at multiple q values to verify the closed forms (or refine them).

Estimated effort: ~1 week of focused compute.

### Path B — KLR canonical-basis Markov trace formula

- [ ] Per agent `a7e7c6fc5e9dcdd3f` survey (PR #777 background): framework has the Hecke-KLR bridge scaffolding (`kazhdan-lusztig-classical-limit.md`, `crystal-basis-resolves-mass-tower-open-problems.lean`) but the explicit per-block canonical-basis trace formula is the gap.
- [ ] Compute the per-block Markov traces on the canonical basis of each irrep V_(3), V_(2,1), V_(1,1,1) at orders ε^8, ε^10, ε^12 using existing `markov_trace_recursive.py` infrastructure.
- [ ] Extract per-block c_k^(λ) by fitting the per-irrep τ_M expansions.
- [ ] Identify the categorical source of each per-block coefficient (Hoefsmit b-power, Jones linkage, rational offset).

Estimated effort: research project scale.

### Path C — Spectral-sequence stratification

**Abandoned** per user direction in #777 (no good candidate spectral sequence in framework's content). Recorded for completeness; do NOT attempt without owner reversal.

## Downstream-validation TODOs (triggered by PR #777's TR_M[5] bug fix)

PR #777 fixed `pyhecke.gram.TR_M[5] = z³` → `h·z² + z`. The fix
propagated to 5 downstream witnesses + 2 latent shadowing-bug scripts
within PR #777. These additional items remain:

- [ ] **Verify content blocks** that quote pre-fix Gram values. Specifically:
  - `confinement-operator-selection.md` lines 17-93 (proton/neutron NF tables, candidate ranking, demand profile values)
  - `delta-max-uniform-bound.md` line 129, 135 (`0.49932` references)
  - `explicit-alpha-k-h4.md` line 121 (`0.5514` reference)
  - `q-beta-gamma-gamma-canonical-derivation.md` line 61 (`y_{(1,1,1)} = -0.5514`)
  - `q-beta-spectral-bridge.md` lines 180-181 (`0.20906`, `0.49932`)
  - `markov-trace-factorization.md` lines 140-144 (both `descartes-universe/` and `braids-and-knots/`)
  - `lp-dual-stability.md` lines 35-40 (LP-dual tables)
  - `deuterium-derived-binding.md` lines 94-95
- [ ] **Extend `:val[...]` anti-staleness coverage** — PR #777 added 8 registry entries + converted 4 high-impact files. The remaining ~12 candidate sites identified by the background agent should be converted to live witness references.
- [ ] **Verify PR #792's witnesses** post-rebase onto PR #777's TR_M[5] fix. PR #792 (merged 2026-05-19) repaired 3 LP-dual witnesses (`option_b_proton_mass_full_chain`, `probe_braid_word_basis_gram`, `probe_sdp_active_set_dominant_partition`) BEFORE the TR_M[5] fix. Their underlying Gram-derived numerical values may have shifted.

Estimated effort: 1-2 days of mechanical validation + content updates.

## Lean class refinement

- [ ] `defaultPerWedderburnBlockC5C6` instance in `per-wedderburn-block-c5-c6.lean` currently retains `0` placeholders for `c_{5,6}_from_V{3,21,111}` per PR #777's analysis (per-block c_k decomposition has no known non-trivial rule). The named ε^k coefficients added in #777 (`chiV3_eps5_coefficient = -1/2`, etc.) are informational. If Path A or Path B finds a substantive rule, this class instance becomes the natural integration point.

## Cross-PR coordination

- [ ] Merge order for #781 (canonical mass tables): #781 should land BEFORE this followup work picks up. Currently #781 is still open (state as of 2026-05-19 evening).
- [ ] When this follow-up branch develops, post intent comments on:
  - Open Q_β / Hecke-related PRs in `litlfred/qou` (recheck list at start of follow-up session)
  - Specifically watch `761` (combined Hoefsmit/GP stack) — overlap on Hoefsmit b computation infrastructure
