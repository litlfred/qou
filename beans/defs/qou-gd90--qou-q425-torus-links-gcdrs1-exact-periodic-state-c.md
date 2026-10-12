---
# qou-gd90
title: 'qou-q425 torus links gcd(r,s)>1: exact periodic-state correction to MiddleWeightTraces, then prove'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:13:10Z
updated_at: 2026-10-12T18:27:26Z
parent: qou-xhci
---

Owner order: (1) gcd>1 torus links, (2) Schur–Weyl trace split under q not a root of unity, (3) W_{r,j}.


## 2026-10-12: torus links PROVED (branch claude/rosso-jones-torus-links-2026-10-12, PR #7737)
The torus-link formula holds for every gcd(r,s). Proof in QOU/Archimedean/RossoJonesTorusLink.lean, sorry-free; the only axioms are propext, Classical.choice and Quot.sound. Full details are in the 2026-10-12 append on qou-q425. Main declarations: T_gam_eq_sum, card_fixSet, T_gam_pow, rossoJones_torusLink, markov_rossoJones_torusLink. The probe computations/probes/rj_torus_link_periodic_probe.py runs 1350 exact checks and all pass.
Item (1) is done. Items (2), the Schur–Weyl trace split, and (3), the modules W_{r,j}, are still open.
