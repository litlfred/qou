# ns57 I1 triage correction — the compute-integration sweep's I1 list is partly stale

**Date:** 2026-06-28
**Bean:** `ns57` ("Integration: I1-proven-no-probe deep math gaps (9 blocks)")
**Supersedes (corrects):** the I1 table in
[`docs/audits/2026-06-28-compute-integration-sweep.md`](2026-06-28-compute-integration-sweep.md) §"I1 — PROVED, NOT PROBED"

## Why this correction exists

The sweep classified a block as **I1** ("proved, not probed") when a
consumer-grep found no witness `contentBlock` pointing at its label. That
grep **missed witnesses living in `computations/` subdirectories** (notably
`computations/qbeta/`), so several blocks that *do* have a probe witness were
listed as I1. Writing fresh probes off the stale list would duplicate
existing compute — the same class of error as the `t6ba` duplicate
(`PR #2995`, closed as superseded).

Method for this correction: collect **every** `"contentBlock"` value across
`computations/**/*.witness.json` (198 distinct pointers) and cross-check the
sweep's 29 high-value I1 candidates against that set.

## Already probed — REMOVE from the I1 set (7)

These carry a committed probe witness; the sweep's "none/none" was stale:

| Block | Probe witness (evidence) |
|-------|--------------------------|
| `prop:q-beta-c-2-eq-neg-one-structural` | `qbeta/qbeta_symbolic_chain_alpha_b.py` → `qbeta-symbolic-chain-alpha-b.witness.json` (asserts `simplify(N2_factor − (1−u²))==0`, i.e. c_2=−1) |
| `prop:q-beta-c-k-recursion-from-habiro-q-difference` | `qbeta/qbeta-ck-genfunc-bounded-vs-factorial-probe.witness.json` (also wired by `c3-hopf-habiro-analysis` per PR #2977) |
| `prop:q-beta-bar-even-kernel-invariant` | `qbeta/qbeta-bar-even-kernel-invariant-probe.witness.json` |
| `prop:markov-trace-ratio-exact` | `probe-markov-trace-ratio-exact.witness.json` (PR #2978) |
| `thm:markov-trace-factorization` | `probe-markov-trace-factorization.witness.json` (PR #2978) |
| `prop:topological-mass-formula` | `probe-topological-mass-formula.witness.json` (PR #2978) |
| `prop:binding-error-amplification` | `probes/difference-knot-jsj-classification.witness.json` |

## Genuinely open I1 — the real `ns57` scope (22)

No witness `contentBlock` points at any of these as of this commit:

**Q_β c_k family (5):**
`prop:q-beta-c-k-leading-bias-correction-identity`,
`prop:qbeta-c4-from-c3-c8-product-identity`,
`prop:qbeta-c8-c10-silver-rationals`,
`prop:qbeta-z-recursion-to-ck-recursion-bridge`,
`prop:q-beta-over-e0-classical-vanishing`.

**Mass / binding (10):**
`prop:neutron-proton-mass-splitting`,
`prop:derived-mass-formula-light-isotopes`,
`prop:hoefsmit-binding-amplitude`,
`prop:mass-tower-coefficient-stratification`,
`prop:per-braid-mass-tower`,
`prop:tower-binding-energy`,
`prop:torus-knot-shell-binding`,
`prop:unified-curvature-rank-mass-formula`,
`prop:mass-formula-regime-switching`,
`prop:binding-scale-catalan`.

**Markov / topological / residue (7):**
`prop:markov-trace-recursive-reducer`,
`prop:gram-weighted-qvalue`,
`prop:topological-mass-formula-algebraic`,
`prop:chirality-residue-mass-term`,
`prop:residue-at-root`,
`prop:sw-period-residue-sum`,
`prop:plancherel-term-7-formulation`.

## Recommended next steps (do NOT re-probe the 7 above)

1. **Cheapest:** several "open" entries may just need an existing
   witness's `contentBlock` re-pointed (verify per-block before writing
   new compute — the c_k family is the likely candidate, mirroring the
   c_2 case above).
2. **Genuine probes** for the mass/binding family should route through the
   canonical `computations/canonical_mass.py` facade (not the deprecated
   `vol_density_*` for absolute mass), per the AGENTS.md mass guardrail.
3. **`prop:neutron-proton-mass-splitting`** — Δ_pn is a *failing* L2
   observable; a probe should report the residual honestly, not assert a
   pass.

## Scope honesty

This is a **triage correction**, not a probe. It removes 7 false-I1
entries and pins the genuine 22-block `ns57` scope so the next agent
probes real gaps instead of duplicating committed witnesses.
