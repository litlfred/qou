---
# qou-amon
title: 'GAP: which premise selects the pure-vertex Borromean photon pair among the 8 two-photon factorisations of V^3'
status: completed
type: task
priority: normal
created_at: 2026-11-25T11:44:28Z
updated_at: 2026-11-25T16:15:20Z
parent: qou-y2o9
---

Singular (2026-11-25, PR #9415 audit §11.2): V^3 = gamma(phi)gamma(psi) has 8 points over Q(h)-bar (corpus pair + irreducible degree-6 component); at proton q0 there are 2 real non-vertex factorisations besides the corpus pair. The corpus weights qh, -q^-1 h are forced only if both factors are pure vertex photons (phi0 = phi1 = 0) -- proved on the line R.V in Lean (HeckeH3Model.borromean_weights_forced_model). The 2026-11-21 linking-neutrality ruling dropped the V-only letter cut, so the selecting premise is currently unruled. Candidates to test: linking neutrality applied to each factor; reading-3 Frobenius positivity of each factor; minimal support. Owner decision may be needed.

2026-11-25: TESTED existing rules (owner: 'Test whether an existing rule already forces it'). Term-wise linking neutrality (formal expansion in Z[B3]) selects exactly the corpus pair — Singular symbolic over Q(h), Lean QOU.PhotonNeutralSelection.neutral_selects_corpus (sorry-free). Whole-product neutrality cannot select; reading-3 positivity does not. Remaining owner decision: term-wise vs whole-product reading of neutrality (PhotonU1NeutralCut scope note). PR #9427.


2026-11-25: OWNER RULING 'Term-by-term, same scope as now'. Term-wise linking neutrality is the selecting premise; the weights qh, -q^-1 h are derived (neutral_selects_corpus). Recorded in owner-rulings.md, prop:borromean-photon-factorisations, audit §15; PR #9431 head f9e57513981. The anti-fit flag (reading chosen with the result known) is in the ruling row. The rule itself is a working conjecture per the ledger; this bean's question (which premise) is answered.
