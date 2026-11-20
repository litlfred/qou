---
# qou-ccst
title: 'FINDING: BW ''no pair for parallel polarizations'' contradicts tree-level QED'
status: todo
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:24:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u (owner D1 item 3), PR #7825, computations/probes/breit_wheeler_qed_linear_polarization_probe.py. Exact spin-summed tree |M|^2 for gamma gamma -> e+e- (m=1, E=5/4, rational on-shell momenta) is NONZERO for parallel linear polarizations at every point tested (e.g. along z: par 9/2, perp 25/2; x-z plane: par(x,x) 1590912/231361). So the selection rule <v_ee, sigma_i sigma_i>_F = 0 in mass-theory/breit-wheeler-vertex.md fails at the comparison point if its sigma_i sigma_i is read as parallel linear polarization. Only the near-threshold dominance of the perpendicular channel is consistent with QED (para-positronium 1S0). Content NOT edited (owner decision). Options: scope the rule to a model statement, re-read sigma_i sigma_i as something other than parallel linear polarization, or record it as a failed comparison.

## 2026-11-15: owner F1 = (a), explore (b) (PR #7825)

(a) done; the paper no longer claims agreement:
- `mass-theory/breit-wheeler-vertex.md`: selection rule re-scoped as a model statement; QED comparison added (9/2 vs 25/2); the horizontal/vertical labels are qualified as model names (Bloch 120°, no automorphism to an orthogonal pair). The labels are not replaced, because F2 is open.
- `observations/breit-wheeler-observation.md`: the "consistent with / follows from" claim is removed; the STAR datum is corrected to cos 4Δφ = (16.8 ± 2.5) % (lowest-order QED 16.5 %); the false decomposition E₀ = 2m_e + ℏ_q·(1.25 MeV) is removed (ℏ_q ≈ 0.0991 is dimensionless).
- `mass-theory/calibration-inputs.md`: the "prediction" entry is qualified.
- Grepped and left unchanged (internal model, no comparison with nature): `computations/breit_wheeler_filtration_chain_probe.py`, `predicted-spectra/breit-wheeler-pair-production-derivation.md`, `mass-theory/breit-wheeler-vertex-literature.md`. No Lean docstring states the rule.
- QA sidecars NOT refreshed: qa-sweep at the pinned folio-assistant fails (`Cannot find module ../../cat-harness/schemas/kg/cat-harness`). Render QA was a grep battery only (balanced $, braces, no list hijack); not machine-validated.

(b) explored as a derivation: σᵢσᵢ = hσᵢ + 1 is diagonal in σᵢ's own eigenline pair, so "same-letter helicity content" means a photon pair of definite helicity in one circular basis. `breit_wheeler_qed_circular_polarization_probe.py` shows QED is nonzero for both J_z = 0 and J_z = ±2. J_z = 2 is suppressed toward threshold (ratio 0.106 at β = 5/13 vs 0.279 at β = 3/5, beam-x-z point). So reading (b) also fails as a strict vanishing rule. It survives only as a threshold suppression, and only if σᵢσᵢ is the J_z = ±2 pair.

Side findings, not fixed:
- `predicted-spectra/breit-wheeler-pair-production-derivation.md` fixes φ by "setting E_pair = 2m_e". That is a fit.
- The `star2021bw` title may not match PRL 127, 052302.
- The ATLAS sentence was not re-checked against the paper.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8472, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
