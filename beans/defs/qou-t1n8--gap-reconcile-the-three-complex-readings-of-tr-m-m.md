---
# qou-t1n8
title: 'GAP: reconcile the three complex readings of tr_M (modulus/phase, Re/Im binding-Q_beta, Re/Im mass-width)'
status: todo
type: task
priority: normal
tags:
    - compute-accuracy
created_at: 2026-11-22T10:47:44Z
updated_at: 2026-11-27T14:18:46Z
parent: qou-wxhi
---

Owner 2026-11-22 (thread "Derive the n-p cell's E0 and eps->MeV map", PR #8955): "Is the mass the real part of something? And the EM the imaginary part? And the braid words intertwine these things?" Owner asked that every issue uncovered be beaned.

FINDING (corpus grep of content/ + docs/audits only; computations/ and beans not searched for this): the corpus carries THREE inequivalent complex readings, none reconciled with the others:
1. rem:mass-modulus-em-phase-color-grading (mass-endomorphism/): POLAR. mass = |tr_M|, EM = arg tr_M (U(1) framing / Chern-Simons phase via the ribbon twist q^{2w c(lambda)}), color = S3 irrep grading. A remark interpreting prop:color-spacetime-s5-factorization; no Lean.
2. conj:binding-qbeta-complex-volume + sec:complex-volume-intro: ADDITIVE. V = E0 tr_M((Pi_free - 1) o M); binding = Re V, Q_beta = Im V. Algebraic reconstruction Lean-proved; physical match conjectural. The intro says "there is no complex mass" (Im q0 = 0; complex structure is fibre-level only).
3. conj:complex-mass-constituent-functional: ADDITIVE, different pair. mass = Re Vol_C, Im = CS = decay width; CS named as the partner "already used for alpha_EM". Scaffold class, no instance.

OPEN: state whether these are one object in three coordinates or three different objects. Specifically (a) modulus/phase vs Re/Im are not the same split unless one is a log of the other (log tr_M = log|tr_M| + i arg tr_M would make reading 1 the Re/Im of log tr_M); (b) readings 2 and 3 assign Im to different observables (Q_beta vs width) and Re to different ones (binding vs mass). (c) at the archimedean level q0 is real, so tr_M at q0 is real and arg is 0 or pi: say where the phase lives (fibre q, root of unity, framing).

Not started. Related: alpha_EM thread "Settle which alpha_em form is canonical"; bean for the electron-word test (sibling of this one).



2026-11-22, from thread 'Settle which alpha_em form is canonical' (PR #8987): under convention D the iota-odd part (iota: sigma -> -sigma^-1) of the Markov trace is exactly (y3/2)*tau with tau = chi_3 - chi_111 the alpha_em functional; tau(w) = q^e - (-q^-1)^e depends only on the writhe e. Sorry-free Lean: QOU/AlphaEM/TauExponentSum.lean. Electron sigma0 sigma1 sigma0: tau = q^3 + q^-3. At q = 1, tau = 1 - (-1)^e (not yet compared with -m_e/720). Consistent with the writhe-phase reading of rem:mass-modulus-em-phase-color-grading; does NOT show mass is the iota-even part.
