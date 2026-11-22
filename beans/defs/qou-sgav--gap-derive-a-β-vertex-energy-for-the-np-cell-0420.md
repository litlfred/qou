---
# qou-sgav
title: 'GAP: derive a β-vertex energy for the n–p cell (0.420 MeV under placement B)'
status: todo
type: task
created_at: 2026-11-22T09:18:20Z
updated_at: 2026-11-22T09:18:20Z
parent: qou-wxhi
---

Open: no derived β-decay vertex energy exists for the n–p cell. Recorded 2026-11-22 from PR #8955
(branch `claude/crossing-weights-from-trace-2026-11-21`), audit
`docs/audits/2026-11-21-qbeta-energy-map-spectator.md` §27–§29.

**What is derived (Lean, sorry-free).** Under premise G (nucleon Gibbs weight = trace of
K^{⊗3}β_Bor on its weight space), n − p = 2E₀ ln q with E₀ = m_e/(q(q−1)); at the proton q₀ that
is 0.873537 MeV. Vertex budget (`BetaVertexBudget.lean`):
- placement C (active lepton): the lepton cancels the cell, so the vertex must supply all of
  Q_β = 0.78233 MeV;
- placement B (E(e⁻) = m_e by CAL-1, E(ν̄) ≥ 0): Q_β < m_e(2/q − 1) < m_e without a vertex term, so
  the vertex must add 0.41979 MeV at q₀.

**What was tried (both scope-(a) negatives, i.e. "alone, as-is").**
- §28 `YoungChannelVertex.lean`: Hecke-channel split of the quark–lepton strand pair,
  ΔE = E₀ ln((q²+q⁻²)/2) = 0.0905 MeV.
- §29 `H4VertexEnergy.lean` + `h4_young_channel_vertex.py`: Young-channel split of all four
  strands in H₄, ΔE₄ = 0.1987 MeV.
Both are O(h²) against an O(h) cell, and in both the sign flips with tensor order, so the sign is
a convention. Closing the gap inside these families needs a free factor (≈2.1 for B), which would
be a fit.

**Not excluded / next honest step.** A vertex weight that is not a function of the Young channel
alone, for example one built from β_Bor on the quark strands (premise G) together with the lepton
strand, or an O(h) vertex term. Any candidate must be preregistered
(`computations/probes/qbeta_energy_map/PREREGISTRATION.md`) and must fix its sign by derivation,
not by tensor-order choice.
