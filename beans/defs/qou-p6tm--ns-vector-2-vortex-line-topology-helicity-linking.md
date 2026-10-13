---
# qou-p6tm
title: 'NS vector 2: vortex-line topology (helicity, linking, reconnection) via braid machinery'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:57:49Z
updated_at: 2026-10-13T00:00:00Z
parent: qou-vo9t
---

Owner (2026-10-12): pursue NS attack vectors 1, 2, 3 and 5 (unforced NS). This bean is v2. Formalize first: a genuine Lean core lemma where one exists, honest conditional statements otherwise, and an audit doc.

## 2026-10-13 — v2 tranche result (branch `ns-v2`)

- **Lean:** `QOU/FluidDynamics/VortexLinkTopology.lean`, sorry-free, lean-direct exit 0; axioms are only propext/choice/Quot.sound. It builds a strand-labelled signed crossing matrix on braid words and proves: invariance under R2, the braid relation and far commutation (plus context propagation); a crossing change moves `C` by exactly `−2 sgn e` on its pair only, so `lk` moves by ∓1; mutual helicity moves by exactly `−2 sgn e Γₐ Γ_b`; Hopf `decide` checks.
- **Verdict:** this is a genuine Euler-level obstruction, conditional on the cited Helmholtz–Kelvin transport. It is scope-(a) negative for NS, because viscous reconnection changes linking smoothly (Kleckner–Irvine 2013; Scheeler et al. PNAS 2014 show link helicity is converted to coiling). The viscous version gives only a lower bound, `∫‖ω‖‖∇ω‖ ≥ |ΓₐΓ_b|/ν`, during reconnection. That is not a regularity route.
- **Audit:** `docs/audits/2026-10-12-ns-v2-vortex-topology.md`.
- **Still open (bean stays open):** Markov-I / non-pure component linking; `helicity-physical.md` wording ("smooth evolution cannot alter total helicity") is Euler-only and needs a scoping note from the block owner.
