---
# qou-p6tm
title: 'NS vector 2: vortex-line topology (helicity, linking, reconnection) via braid machinery'
status: todo
type: task
priority: normal
created_at: 2026-10-12T20:57:49Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-vo9t
---

Owner (2026-10-12): pursue NS attack vectors 1, 2, 3 and 5 (unforced NS). This bean is v2. Formalize first: a genuine Lean core lemma where one exists, honest conditional statements otherwise, and an audit doc.

## 2026-10-13 — v2 tranche result (branch `ns-v2`)

- **Lean:** `QOU/FluidDynamics/VortexLinkTopology.lean`, sorry-free, lean-direct exit 0; axioms are only propext/choice/Quot.sound. It builds a strand-labelled signed crossing matrix on braid words and proves: invariance under R2, the braid relation and far commutation (plus context propagation); a crossing change moves `C` by exactly `−2 sgn e` on its pair only, so `lk` moves by ∓1; mutual helicity moves by exactly `−2 sgn e Γₐ Γ_b`; Hopf `decide` checks.
- **Verdict:** this is a genuine Euler-level obstruction, conditional on the cited Helmholtz–Kelvin transport. It is scope-(a) negative for NS, because viscous reconnection changes linking smoothly (Kleckner–Irvine 2013; Scheeler et al. PNAS 2014 show link helicity is converted to coiling). The viscous version gives only a lower bound, `∫‖ω‖‖∇ω‖ ≥ |ΓₐΓ_b|/ν`, during reconnection. That is not a regularity route.
- **Audit:** `docs/audits/2026-10-12-ns-v2-vortex-topology.md`.
- **Still open (bean stays open):** Markov-I / non-pure component linking; `helicity-physical.md` wording ("smooth evolution cannot alter total helicity") is Euler-only and needs a scoping note from the block owner.

## 2026-10-13: Q2 done (owner "Q2 y"), commit 95b9e7719a on `ns-q2q3`

The three content blocks are now scoped to Euler. Minimal edits, in the existing voice:
- `helicity-physical.md`: "Smooth evolution cannot alter the total helicity" now reads *smooth inviscid (Euler)*. Added the NS identity `dH/dt = -2nu int omega . curl omega` and the smooth-NS reconnection result (`enciso2017`).
- `vortex-reconnection.md`: removed the presupposed "classical reconnection singularity". It now states the Euler obstruction and the smooth NS reconnection (Enciso-Luca-Peralta-Salas, Adv. Math. 309 (2017) 452-486). The helicity bullet cites the sorry-free Lean results (`QOU.FluidDynamics.VortexLink.crossingChange_lk`, `crossingChange_mutualHelicity`, `mutualHelicity_R2`, `mutualHelicity_braid`) and `scheeler2014` for the linking-to-coiling transfer.
- `helicity-conservation.md` item 3: the trefoil sentence is now a framing statement. A single tube gives `Gamma^2 (Wr + Tw) = Gamma^2 Lk`, which vanishes only for a zero-framed tube, and either knot admits one (`moffatt-ricca-helicity`).
- New refs: `enciso2017` (DOI 10.1016/j.aim.2017.01.025, checked by web search), `ebin-marsden1970` (no DOI recorded).
- Gate: render preflight balanced. One pre-existing defect is not mine and not fixed: the writhe/twist/linking display in `helicity-conservation.md` has `+` at the start of lines inside `$$`. run-validate shows no fluid-dynamics issue. qa-sweep run; the remaining fail/warn entries are pre-existing (dated 2026-07/08) and on unedited text.
- Still open, so the bean stays open: Markov-I / non-pure component linking.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch B):** in-progress → todo. Stale claim (session ended); work not finished — see docs/coordination/2026-11-20-dangling-claims-proposal.md.
