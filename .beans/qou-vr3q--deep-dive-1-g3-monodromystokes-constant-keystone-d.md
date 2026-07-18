---
# qou-vr3q
title: 'Deep-dive 1: G3 monodromy/Stokes-constant keystone — derive A_ω (odd-face Q_β/Φ_b) as GGM 3d-index integer count'
status: in-progress
type: task
priority: high
tags:
    - alien-habiro
created_at: 2026-07-18T17:08:37Z
updated_at: 2026-07-18T17:20:36Z
parent: qou-89f9
---

CORRECTED FRAMING (2026-07-18): A_ω≈3.8884 (=4√2·e^{-3/8}) is the EVEN-face, q=1 BINDING-period Stokes constant (co-equational, bar-even, binding a_D only) — NOT the odd-face keystone. Do not conflate.

G3 keystone = the bar-ODD (Q_β/Φ_b) monodromy datum z(q0)→S whose archimedean eval must reproduce S(muon)=+0.00968298, S(proton)=-0.03945936. UN-MEASURED. It is a categorical Stokes/monodromy datum (irregular q-difference connection), NOT a resummation constant.

Derivation candidate (not fit): the exact GGM 4₁ Stokes matrix integer 3 (S⁰=[[1,0],[-3,1]]), singularity at ω=Vol(4₁)/π≈0.646. computations/probes/qbeta_g3_ggm_stokes_41.py certifies det W_m=2, q-diff eq 49, eq-59a sandwich EXACT. Open 'step 3': identify that integer's substrate eval with Im 𝔙→N_odd (falsifiable). Trace-field H1 (qou-t3jv): Stokes -3 = disc(ℚ(√-3))=-3 unifying even(√3)/odd(√-3) via ℚ(ζ12) — NOT verified.

Lean scaffold ALREADY present: CyclicDilogPentagon.lean faddeevPhi_unique_of_pentagon (sorry-free), MonodromyDatumRigidity.lean monodromy_datum_rigidity (sorry-free) ⇒ A_ω carries NO fitting freedom IF pentagon holds. SINGLE open input = PentagonRigidity.uniqueUpToScalar (Faddeev-Volkov 'doubly-periodic⇒constant' Liouville step, Mathlib gap, no instance).

FORMALIZE-FIRST target: prove PentagonRigidity (Liouville step) → discharges uniqueness leg, converts G3 from 'find a function' to 'verify pentagon pins the proved inversion/unitarity/self-duality bundle'. k=21 singularity now CONFIRMED structurally unresolvable by fixed-order Borel-Leroy through k=31 (gap persists 0.172); needs Φ_b state-integral/GGM route. Full memo: docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md
