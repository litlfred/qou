---
# qou-x09k
title: 'W7: Bridge A without hL (n-body connection of D_nabla, local monodromy, colour singlets)'
status: completed
type: task
priority: normal
created_at: 2026-11-22T22:17:23Z
updated_at: 2026-11-23T20:54:24Z
parent: qou-ywyq
---

Workstream W7 of the L2 1-ppQ plan (docs/coordination plan 2026-11-22). New Lean file QOU/Mass/BridgeAStokesNBody.lean: P1-P3 n-body form = KZHolonomy.kzForm (kappa = beta/2, c = -alpha/beta); its generator monodromy = kzBraidRep, conjugate to Jimbo, Hecke quadratic; lagrangian_gauge_to_KZ_of_stokes replaces hL by the named assumption StokesToBraiding; colour singlets: (X+1)(X-q^-2)=0 and singlet_exterior_iff under named ColourTubeBraided. Sorry-free, axioms propext/choice/Quot.sound only.



2026-11-23: gaps 1–2 advanced on #9163 (a091ea296). Drinfeld–Kohno for C^d is proved, and the colour-tube assumption is reduced to the no-mixed-term residue condition. Gaps 3 (StokesToBraiding) and 4 (Deligne/P1–P3) are in sibling threads.

2026-11-23 (WS2 consolidation): Consolidated #9163 (Gaps 1-3: BridgeAStokesNBody, KohnoAssemblyGL, BridgeAColourSplit, BridgeAStokesAlgebraic, kohno1987 DOI fix) + stacked #9170 (Gap 4: BridgeAP2Regular + p2_triple_collision_probe.py + deligne1971 ref) into READY PR https://github.com/litlfred/qou/pull/9187 (consolidate/ws2-bridge-a-stokes-nbody, 76a0d2e6187). Verified 65/65 theorems clean via lean-axiom-guard.py and lean-overlay-env.sh (-DautoImplicit=false -s 65536).


## Resolution Verified on origin/main (2026-11-23)

Verified resolved on `origin/main` via PR #9187 (`37b46202b9`): Closed by #9187 (Bridge A W7 non-circular n-body KZ monodromy, `KohnoAssemblyGL`, `BridgeAColourSplit`, `BridgeAStokesAlgebraic`, `BridgeAP2Regular`).
