---
# qou-5d0x
title: 'RT finding: 4 provable blocks whose lean.ref does not name a proof of the block (module name, structure, Prop def, def-as-proof)'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

Surfaced by scripts/roundtrip-blind-sample.py during qou-ncxf pass 1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md). Not a full scan: these are only the 15 lowest-hash eligible blocks.

- `prop:centered-hecke-variance-positive`: ref `QOU.Observations.centered_hecke_variance_positive` is a MODULE name. The proof is `centeredVariance_pos` in `folio/quantum-observable-universe/lean/QOU/Observations/centered_hecke_variance_positive.lean`.
- `thm:jones-markov-trace`: ref `QOU.Braiding.JonesMarkovTrace` is a `structure` (`braids-and-knots/jones-markov-trace.lean:99`), not a theorem. See qou-h9p8.
- `prop:curvature-rank-gb-stratification`: `def curvature_rank_gb_stratification [ctx] : ∀ r, … := …` (`lean/QOU/WedderburnMass/curvature_rank_gb_stratification.lean:52`). This is a Prop proof declared as `def`, and it is also a projection of class fields (`quotient_subset_rank`, `rank_subset_quotient`). That is the `def-disguised` shape of AGENTS.md §1a.
- `prop:box-braid-irreducibility`: ref names `noncomputable def BoxBraidIrreducibility : Prop` (`nuclear-interactions/box-braid-irreducibility.lean:150`), i.e. the proposition, not its proof.

(A fifth, `prop:quantum-observable-universe-exists`, was a sampler parser miss on a dotted theorem name, `theorem QuantumObservableUniverse.exists_instance`. It is not a corpus defect.)

Next step: a full scan of all 435 sampled-population refs for this class.
