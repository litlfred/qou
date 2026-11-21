---
# qou-5d0x
title: 'RT finding: 4 provable blocks whose lean.ref does not name a proof of the block (module name, structure, Prop def, def-as-proof)'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-ncxf
---

Surfaced by scripts/roundtrip-blind-sample.py during qou-ncxf pass 1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md). Not a full scan: these are only the 15 lowest-hash eligible blocks.

- `prop:centered-hecke-variance-positive`: ref `QOU.Observations.centered_hecke_variance_positive` is a MODULE name. The proof is `centeredVariance_pos` in `folio/quantum-observable-universe/lean/QOU/Observations/centered_hecke_variance_positive.lean`.
- `thm:jones-markov-trace`: ref `QOU.Braiding.JonesMarkovTrace` is a `structure` (`braids-and-knots/jones-markov-trace.lean:99`), not a theorem. See qou-h9p8.
- `prop:curvature-rank-gb-stratification`: `def curvature_rank_gb_stratification [ctx] : ∀ r, … := …` (`lean/QOU/WedderburnMass/curvature_rank_gb_stratification.lean:52`). This is a Prop proof declared as `def`, and it is also a projection of class fields (`quotient_subset_rank`, `rank_subset_quotient`). That is the `def-disguised` shape of AGENTS.md §1a.
- `prop:box-braid-irreducibility`: ref names `noncomputable def BoxBraidIrreducibility : Prop` (`nuclear-interactions/box-braid-irreducibility.lean:150`), i.e. the proposition, not its proof.

(A fifth, `prop:quantum-observable-universe-exists`, was a sampler parser miss on a dotted theorem name, `theorem QuantumObservableUniverse.exists_instance`. It is not a corpus defect.)

Next step: a full scan of all 435 sampled-population refs for this class.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Full-population run of pass-1 §7 item 1: `scripts/roundtrip-blind-sample.py --ref-audit` (new, commit 24c44167e), output `docs/audits/2026-11-21-lean-ref-target-audit.json`.
- 717 provable blocks with a `qou:` ref. 569 name a theorem/lemma. **148 (20.6 %) do not**: Prop-valued def 27, other def 41, structure 22, class 19, instance 16 (all `*-exists`), module/file 10, not found 11, abbrev 1, axiom 1 (`prop:tannaka-krein-reconstruction`).
- Regex classifier over source, no elaboration: a candidate list, not verdicts. Per-block readings and any ref change wait for an owner yes (it is a sweep).
- The 4 pass-1 cases are all still in the list on main.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
