---
# qou-d7h1
title: 'GAP: Eightfold Way flavor SU(3) from QOU components — distinguish from colour SU(3), then derive octet/decuplet organization'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T17:29:24Z
updated_at: 2026-08-02T17:30:46Z
parent: qou-a0gr
---

Near term: inventory the existing I3/Q/Y, strange-quark, and three-strand colour ingredients; prove the corpus already has the right state labels for u,d,s-level organization.

Medium term: build a flavor-SU(3) candidate action on the hadron state space and test baryon-octet / meson-octet / decuplet decomposition without conflating it with the colour module.

Long term: connect the flavor action, if it exists, to the Bring/icosahedral side (A5 / S5 / W-plane geometry) as a derivation route rather than a one-number analogy.
2026-08-02 concrete inventory.

- `sm-gauge-truncation.md` already separates the three roles cleanly: `Q` is derived, `I_3` is matched by the writhe ladder on the nucleon doublet, and `Y` remains open because proton and neutron share `Y=+1` while their writhes differ.
- `strand-twist-datum.md` gives the best current candidate for the missing second invariant: twist is independent of writhe, and the candidate hypercharge is `Y_t = 2(Q_twist - I_3)`, but only as a battery candidate.
- `strangelet-crossing-energy-proof.md` and `strangelet-intro.md` already carry usable flavor labels: `d = T_{2,3}^σ`, `s = T_{2,5}^σ`, and baryonic `(u,d,s)` units use the `{+,-,-}` charge partition.
- Colour SU(3) is partially closed elsewhere: `sm-colour-stabilizer-action` plus `OctonionColourActionBaseModule.lean` already realize the abstract colour-action class on `O = C ⊕ C^3`; the open piece there is the action on QOU's own Hecke three-strand state space.

