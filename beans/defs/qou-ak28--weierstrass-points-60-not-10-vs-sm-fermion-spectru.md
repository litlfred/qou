---
# qou-ak28
title: Weierstrass points (60, not 10) vs SM fermion spectrum — explore S₅-orbit decomposition
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-04T17:32:48Z
updated_at: 2026-10-10T07:15:48Z
parent: qou-8lxd
---

Source: Braden & Disney-Hogg, "Bring's curve: old and new" (2024)

Bring's curve (genus 4) has EXACTLY g³-g = 60 Weierstrass points.
S₅ acts TRANSITIVELY on all 60 (each has weight 1, not maximal weight 6
as would give only 10 points). 60 = 120/2, so the stabilizer of each
Weierstrass point has order 2 (a single involution fixes each point).

NOT 10 fermion slots. The 10-fermion numerology is dead.

EXPLORATION: What S₅ orbit decomposition DO the 60 points have?
- Single transitive orbit of size 60 → stabilizer Z/2
- Could 60 = 3 generations × 20 something?
- Could 60 = 12 chiral states × 5 (S₅ index)?
- Could 60 = |A₅| = 60 (icosahedral orbit)?

Sources: Braden-DH §theta characteristics; standard AG (g³-g formula).

ANTI-FITTING: Don't force-fit 60 to any SM count. If it doesn't
match naturally, document the non-match. The Weierstrass points are
a mathematical invariant, not necessarily a particle dictionary.

## Progress Note (2026-11-16)
- Formalized Bring curve 60 Weierstrass points S_5-orbit decomposition (24 + 36 = 60 = g^3 - g) and Weierstrass gap weights ([1,2,3,6] weight 2 on 24-orbit, [1,2,3,5] weight 1 on 36-orbit, quadric-cubic weight 24*2 + 36*1 = 84) in `QOU/Eightfold/BringThetaBruhatAndMesonH3.lean` (`bring_weierstrass_60_orbit_and_weight_certificate`) + 50-dps probe `bring_theta_bruhat_and_meson_h3_probe.py` (PR `litlfred/qou#8163`, head `bc5c91877bf9516be8cbcc8cd12c1a6501a5e983`).
