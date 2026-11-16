---
# qou-ihtw
title: 'OBS: GW170817 kilonova Sr II — is the r-process path a nuclear-chart probe? (masses + beta-rates far from stability under shifted alpha)'
status: in-progress
pr: 8203
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-obs
created_at: 2026-09-07T13:44:34Z
updated_at: 2026-10-10T07:16:27Z
parent: qou-8lxd
---

---

## 2026-09-13 — sibling note: the alpha route is dead, THIS one is not

`qou-ultb` (actinide cosmochronometry) is now measured: a bound on
`|d(alpha)/alpha|` converts to a bound on `|dq/q|` by dividing by
`S = |d ln alpha / d ln q| = 6.86193302278`, and at its asserted 2.08e-3 that
is **2.5e5x LOOSER than sigma(q0)** — so the alpha-variation programme cannot
constrain q0 at any achievable precision, formation site or not.

**That negative does NOT carry over to this bean, and should not be quoted as
if it did.** This bean proposes constraining the framework through a DIFFERENT
quantity — nuclear masses and beta-rates far from stability / isotope-vs-
element discrimination — which has its own sensitivity to the substrate and is
untouched by the alpha calculation. Scope (a) on `qou-ultb`'s route only.

Still a title with an empty body; the task needs scoping before it can be
worked.

## Progress (2026-11-16, PR #8203)
- [x] Formalized `orderedProtonPairs` and `isobaric_beta_proton_pair_increment` in `folio/quantum-observable-universe/lean/QOU/Eightfold/RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots.lean` + 50-dps mpmath witness (`qou_ihtw_isobaric_beta_coulomb_pair_increment`) in PR #8203 (`74a091a53fd300f6f906db42c72c6a5e3e84e7b3`).
