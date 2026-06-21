# Compute wiring audit — PR #852 + 72-hr window

**Date:** 2026-05-20
**Trigger:** "is all math compute wired in?" + "thorough review on mass pipeline and knot atlas to use canonical only / no fitting"
**Scope:** all commits last 72 hrs touching mass-pipeline / knot-atlas / new-math (PR #852 + sibling PRs #843, #836, #847, #853 merged to main).

## TL;DR

**Mass pipeline + knot atlas are canonical-only. No fitting, no CAL-4, no numerology.**

The 6-tier consistent-negative Bring-Bloch search is itself the case against ad-hoc fitting: PSLQ is the canonical integer-relation engine for testing categorical decompositions; a negative is structurally informative.

## §1. Production mass pipeline — clean ✅

| Script | Anti-pattern check |
|--------|---------------------|
| `canonical_mass_table_extended.py` | no `scipy.optimize`, no `curve_fit`; reads 50-dps witness chain |
| `m_p_borromean_verification_50dps.py` | uses `VOL_B3 = 8 * mp.catalan` (canonical, not literal) |
| `markov_peel.py` | categorical Markov trace, no fits |
| `mass_tower_operator_valued_chain.py` | aggregator over PROVED A=2,3 + A=4 framework |

CODATA values appear only as **comparison targets** in PSLQ search (e.g. λ_p = 2.4599527843613... at line N of tier scripts) — not as fitted parameters.

## §2. Knot atlas — canonical-only ✅

| Layer | Status |
|-------|--------|
| Atomic-braid recipes (p, n, D, ⁴He) | 4 explicit `-canonical.derivation.json` files |
| Bring-Bloch tier-search basis | `mp.clsin(2, π/3)` for Vol(4_1); `8 * mp.catalan` for Vol(𝓑₃) — computed, not hardcoded |
| Tier 2-5 literal volumes | KnotInfo / SnapPy at 15-25 dps, sources cited in docstrings |

All 6 tier scripts (`bring_bloch_tier{0..5}_search_m_p.py`) use the same canonical computation for the structural volumes (4_1, 𝓑₃).

## §3. Three-calibration discipline — enforced ✅

- **157 live scripts** reference CAL-1 / CAL-2 / CAL-3
- **0 live scripts** reference CAL-4 / fourth-calibration / `fourth_cal`

Grep regex used:
```
CAL-1|CAL-2|CAL-3|CAL1|CAL2|CAL3     → 157 hits in live
CAL-4|CAL4|fourth_cal|cal_4_|calibration_4   → 0 hits in live
```

## §4. New props → witness wiring (PR #852)

| Prop / finding | Witness(es) | Status |
|----------------|-------------|--------|
| `conj:lambda-scale-bring-bloch-identity` (#843) | tier{0..5}-search-m-p witnesses | 6-tier NEGATIVE |
| `prop:li2q-phiq-bar-symmetrization` (corrected) | `li2q-phiq-bar-symmetry.witness.json` | falsification + correct identity verified to 1e-55 |
| `prop:mass-tower-operator-valued` (Stage 1) | chain aggregator + h9-tritium + h9-³He + h12 framework | A=2,3 PROVED; A=4 framework + deferred extract |
| Skein S(p) hypothesis | `skein-proton-canonical.witness.json` | 3 hypotheses; only S(p)=0 closes 1 ppb |
| Vol(𝓑₃) = 8G propagation | m_p-borromean-verification + canonical-mass-table-extended | p/n close to −0.32 ppb |

## §5. Falsifiability probes — allowed, not consumed ⚠️

These are explicit *ansatz probes*, not production:

| Script | Status |
|--------|--------|
| `branch_phase_fit_to_mass_tower.py` | docstring reference only (in `rho_prefactor_structural_verifier.py`); not invoked |
| `schrodinger_color_falsifiability_fit.py` | explicit `_fit` suffix; standalone probe |

The discipline is **"no fitting in the production mass pipeline"**, not "no fits anywhere ever". Falsifiability probes that test an ansatz and emit an audit-only witness are an allowed pattern under `prop:three-calibration-discipline`.

## §6. LP/SDP solvers — canonical infra ✅

7 live scripts use `scipy.optimize.linprog` for LP/SDP dual extraction per `prop:operator-selection-lp`:

- `compound_shift_nf.py`
- `derive_e_0_lp_dual_h3.py`
- `pn_alpha_lp_dual.py`
- `rho_k_h3a_lp_dual.py`
- `lp_dual_solver.py` (canonical entry point)
- (+ 2 others)

These are **LP solvers**, not regressions/fits. Per AGENTS.md §"LP/SDP duals — first-class infra", they emit primal + dual variables in their witnesses.

## §7. Open frontiers (queued, not blocking this PR)

1. H_{12} A-operator production extract for ⁴He — framework on disk, ~30-60 min compute deferred
2. ⁷Li mass-table extension — currently running in BG
3. Joint-tower SDP infrastructure
4. q-dilog tower direct λ_p_scale derivation (post-bar-anti-sym, given 6-tier negative Bring-Bloch)

## §8. PR #853 (notation refactor, 226 files) — no overlap conflicts

PR #853 landed on `main` mid-session. Auto-merge of `main` into `claude/lambda-p-followons` resolves cleanly:
- 2 files overlap (`bar-symmetric-three-layer-synthesis.md`, `li2q-phiq-bar-symmetrization.md`)
- Both auto-merge — my edits and the notation refactor edits are in non-conflicting sections
- `mergeable_state: clean` per `gh pr view 852`

## Conclusion

The mass pipeline + knot atlas + three-calibration discipline are wired correctly. The 72-hr commit window produced:
- 1 falsified-and-corrected boxed identity (bar-sym → bar-anti-sym)
- 1 substrate-pure m_p closure (Vol(𝓑₃) = 8G fix, p/n to −0.32 ppb)
- 6 tier-search negatives strengthening the structural-decomposition case
- 1 Stage-1 operator-valued mass-tower chain through A=3 + A=4 framework
- 0 fitting / numerology / CAL-4 introductions

Future audits: re-run `grep -rln "CAL-4\|CAL4\|curve_fit\|scipy.optimize" computations/*.py | grep -v _deprecated` as a smoke test before merging mass-pipeline changes.
