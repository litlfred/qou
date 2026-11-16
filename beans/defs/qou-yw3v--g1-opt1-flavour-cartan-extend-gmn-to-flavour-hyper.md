---
# qou-yw3v
title: 'G1-opt1 (flavour Cartan): extend GMN to flavour hypercharge Y_f=B+S+C; derive strangeness S and charm C as KNOT CHARGES (higher Milnor / additional linking invariants) completing Q=I3+(B+S+C)/2. Builds on Y=B=mu-bar_123 (#4597) + T3 (#4618). FLAVOUR SU(3)/SU(4), not colour.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-02T20:19:12Z
updated_at: 2026-11-16T18:56:59Z
parent: qou-8lxd
---


## Progress Update — 2026-11-16 (`litlfred/qou#8155`, `f3af82fd1d99fc5eb05c0bd46bbd812b46330432`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/FlavourCartanOctetDecuplet.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Formalizes `FlavourState` in cleared integer coordinates (`twoI3 = 2 I_3`, `threeB = 3 B`, `S`, `C`, `threeYf = 3 Y_f = threeB + 3 S + 3 C`, `sixQ = 6 Q`) and proves linearity of `sixQFromCartan` under composite hadron formation (`sixQFromCartan_combine`, `sixQFromCartan_anti`);
  - Proves exact satisfaction of $Q = I_3 + (B + S + C)/2$ across:
    * the 4 fundamental quarks $(u, d, s, c)$ (`quarks_flavour_cartan_exact`, where $s \sim T(2,5)$ carries $S = -1, C = 0$ and $c \sim T(2,7)$ carries $S = 0, C = +1$ alongside $B = 1/3$),
    * all 8 baryon octet states $(p, n, \Sigma^+, \Sigma^0, \Sigma^-, \Lambda^0, \Xi^0, \Xi^-)$ (`baryonOctet_flavour_cartan_exact`, $B = 1 = \bar{\mu}_{123}$),
    * all 10 baryon decuplet states $(\Delta^{++}, \Delta^+, \Delta^0, \Delta^-, \Sigma^{*+}, \Sigma^{*0}, \Sigma^{*-}, \Xi^{*0}, \Xi^{*-}, \Omega^-)$ (`baryonDecuplet_flavour_cartan_exact`),
    * all 8 pseudoscalar meson octet states $(K^+, K^0, \pi^+, \pi^0, \eta_8, \pi^-, \bar{K}^0, K^-)$ (`mesonOctet_flavour_cartan_exact`), and
    * 6 charmed baryons $(\Lambda_c^+, \Sigma_c^{++}, \Sigma_c^+, \Sigma_c^0, \Xi_{cc}^{++}, \Omega_c^0)$ (`charmedBaryons_flavour_cartan_exact`).
- **Probe & Witness (`computations/probes/flavour_cartan_octet_decuplet_degeneration_probe.py` + `flavour-cartan-octet-decuplet-degeneration.witness.json`)**: `allPassed: true` (`36/36` states verified, `q0Anchor: "independent"`).
