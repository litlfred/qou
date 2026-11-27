---
# qou-o8lo
title: 'G2 A-scaling: T(T+1) coefficient is writhe/(N(N-1)) (PR #9747)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T21:52:11Z
updated_at: 2026-11-27T21:52:18Z
parent: qou-myts
---

Follow-up to qou-tcl2 (G2). PR #9747, branch claude/isospin-writhe-scaling-2026-11-27.

Lean QOU/Nuclear/IsospinTwistWrithe.lean (sorry-free, lean-direct exit 0): any multiplicative block invariant sees a braid word only through its writhe; the Murphy product is a word of N(N-1) letters; on a block det rho(w)^{N(N-1)} = (q^{2c})^{d e}. So the T(T+1) coefficient is writhe/(N(N-1)). Full twist (#9706) has none; chain word e = A-1 gives Theta(1/A), in [1/(9A), 2/(9A)].

Probe isospin_twist_writhe_scaling_probe (comparison only): Table 3.4b median Q_beta error 315.8% (full twist) -> 92.36% (chain), 92.19% (T3); no term 92.69%. The term is then ~0.2 MeV at 208Pb, ~1000x below the classical symmetry energy: scope-(a) negative for this channel with alpha.

Second 1/A: block dimension, ln d_T - ln d_0 = ln(2T+1) - 2T^2/N; not wired (no corpus energy map for multiplicity).

Open: bond-letter signs (G5); quark-level T3 writhe (#4618) would add an odd-in-T_z piece; block functional; scale alpha (scale-unification thread). Wiring choice put to Carl on a card.
