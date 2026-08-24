---
# qou-1ngr
title: Gluon stabiliser feasible set is restricted to L± without stating why
status: todo
type: task
priority: normal
created_at: 2026-08-24T19:08:20Z
updated_at: 2026-08-24T19:08:21Z
---

Found while closing the antiquark channel (rem:antiquark-channel-ledger, 2026-08-24). Smaller than that one, and the same shape: a restriction that is correct but unjustified in the text.

`categorical-proton-properties.md:10` — "The integer LP dual enumerates all feasible gluon combinations and selects the configuration minimizing |tr_M|." The feasible set is never defined.

It is in fact well-defined. Line 4 of the same block says "The Hopf link terms L± manifest the gluon field", so the candidates are the L+ = σ₀σ₁ and L− = σ₁σ₀ elements of the six-word Gröbner–Shirshov basis of H_3(q) — not arbitrary knots. Enumeration over combinations of those IS exhaustive.

What is missing is WHY the stabiliser may not be e⁻ = σ₀σ₁σ₀, the trefoil, which is equally a basis word and equally Vol = 0. The answer looks like a conservation law rather than a choice: e⁻ is the lepton channel, so admitting it as a stabiliser would change lepton number. Note that the same block says the Hopf gluon "redistributes normal-form weight from σ₁ into the trefoil channel" — e⁻ is the OUTPUT of stabilisation, so admitting it as an INPUT would also double-count.

Worth writing down because it is load-bearing for the mass split. The proton takes one Hopf link (2 gluon crossings), the neutron two (4 crossings), and that difference is what makes the neutron heavier — which feeds Q_β = m_n − m_p − m_e, i.e. CAL-2. If the feasible set were wrong the mass split would be wrong.

Task: state the conservation argument in the proton/neutron blocks, or in a remark interpreting def:derived-atom step 4, and say explicitly that the enumeration ranges over L± combinations. Check the neutron block for the same omission.
