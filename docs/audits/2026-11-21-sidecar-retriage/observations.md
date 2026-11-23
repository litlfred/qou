# Sidecar re-triage: observations chapter (2026-11-21)

Umbrella issue #8766. 14 stale items: 5 statement checks (`proof-narrative-lean-equiv`) and 9 proof checks (`da-non-sequitur`). The census after the writes shows every Lean-backed statement (9) and every proof (13) in this chapter fresh.

Method: I read the word diff for each item since its last review. Items where only wording changed keep their earlier verdict, re-stamped with the diff cited. Items where the mathematics changed, or where a block conflicts with a current owner ruling (`docs/coordination/owner-rulings.md`), got a full review.

## Re-stamped (wording only, earlier verdict kept)

| block | criterion | verdict | what changed |
|---|---|---|---|
| local-substrate-q | stmt | fail | no change |
| eos-borromean-cfl | stmt | fail | voice |
| neutron-prediction-comparison | stmt | fail | voice |
| double-slit-massive-pattern | stmt | fail | voice |
| knot-volumes-verification | proof | fail | voice |
| neutron-proton-mass-splitting-proof | proof | warn | audit and producer pointers removed |
| algebraic-gns-embedding-proof | proof | fail | Lean names removed, voice |
| terminal-resolution-proof | proof | fail | label refs replaced by titles |
| local-substrate-q-proof | proof | warn | CAL-2 sentence clarified; the unsupported ±0.001 claim is still there |
| neutron-proton-mass-splitting | stmt | warn | probe paragraph and 2026-11-20 update added, consistent with the two-term trace ruling; Lean unchanged, `quarkPhi` still hard-codes literals |

## Full reviews

- **gravity-spectral-prefactor (stmt): fail, major.** The Lean is still a tautology. The md now says gravity uses "the same prefactor" as `conj:binding-scale-catalan`, so the proposition carries conjectural content. But `uses[]` does not list the conjecture, and the Lean has no class hypothesis for it. That breaks the §3b propagation rule.
- **skein-mass-relation-proof (proof): fail, major.** The earlier findings stand. It also conflicts with a ruling: the proof identifies the electron with the trefoil 3₁, but the 2026-11-21 ruling makes the electron σ₀σ₁σ₀ ∈ B₃ with Hopf-link closure. The Hopf link also has volume 0, so the zero-mass objection still applies.
- **brane-tower-q-laplacian-decay-proof (proof): fail, major.**
  - Fixed: the direct eigenvalue bound is now correct.
  - Still open: Step 5 uses only λ₁ to bound a general state.
  - Still open: the bound is called "exponential" but is geometric in the level index.
  - Still open: q* is never computed.
  - Still open: the sub-ppm claim for three jet levels is not checked.
- **centered-hecke-variance-positive-proof (proof): pass → warn, minor.** The derivation is correct, with minimum 3/4 at q = 1. The new closing paragraph says the minimum is 1 at q = 1, which contradicts it. The statement md has a similar new overclaim about tracial-state positivity for all q > 0.

## Ruling conflicts in this chapter

- Photon form: no block here uses it.
- Electron: skein-mass-relation-proof uses the trefoil. This is routed to the SM thread.
- Two-term Lagrangian trace: neutron-proton-mass-splitting is consistent with it.
