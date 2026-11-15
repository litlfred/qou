---
# qou-qs4c
title: 'Relations among colour x spin x flavour x chirality x momentum; settle the colour channel'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-15T09:30:00Z
parent: qou-qs0e
---

Physics: the factors are NOT independent. Known relations to map onto the substrate:
spin-statistics + colour antisymmetry (baryon spin-flavour-space symmetric, SU(6) 56, mu_p/mu_n = -3/2);
Lorentz (chirality = helicity when massless, mass mixes L/R); weak isospin acts on L only;
Q = T3 + Y with chirality-dependent Y; anomaly cancellation forces N_c = 3 from the quark charges; CKM; confinement.
Schur-Weyl: (3)<->10, (2,1)<->8 (x2), (1^3)<->1 for N = 3; convention D = Schur-Weyl at N = 2.
Settle: is the colour channel (1^3)? Only mu-bar_123 in the sign rep is established (`docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md:86-89`).
Scope (a)/(b) discipline on any exclusion.

## 2026-11-15 — partial (PR #7823); stays open (colour factor's existence is open)
`docs/audits/2026-11-15-quark-factor-relations-and-colour-channel.md` + `QOU/SchurWeyl/ColourChannelSpinStatistics.lean` (lean-direct exit 0, std axioms). Colour (1^3) forced given 4 S3 factors + Fermi + Delta++ (empirical); level 2 cannot host colour (wenzlWeight_eq_zero_iff). OPEN: does the substrate supply a separate colour factor (options A level-3 factor / B mu-bar / C none). Level-2 (2,1) = nucleon isospin channel, not a quark.
