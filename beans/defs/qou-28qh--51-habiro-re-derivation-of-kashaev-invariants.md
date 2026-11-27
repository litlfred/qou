---
# qou-28qh
title: 5.1 Habiro re-derivation of Kashaev invariants
status: in-progress
type: task
priority: normal
tags:
    - constructive
created_at: 2026-11-27T19:01:13Z
updated_at: 2026-11-27T19:34:40Z
parent: qou-dk7p
---

Child of qou-gfsr (item 5, option 5.1). Option 5.1 of qou-gfsr (owner pick 2026-11-27, "full habiro rederivation"). Restate the Kashaev invariants and the related Ohtsuki/dilog content as algebraic objects in the Habiro completion R^[q] = lim R[q]/((q;q)_n), so the analytic modules shrink rather than move. Generic CommRing, sorry-free, no analytic API outside QOU/Transcendental/, no empirical value in any proof.

## Plan
- P1 (this thread, first PR): QCalculus/HabiroCyclotomicSeries.lean. Habiro ring over any CommRing R; series Sum a_n (q;q)_n with coefficients in the ring itself; q is a unit; trefoil (Kontsevich-Zagier, a_n = 1) and figure-eight (a_n = (q^-1;q^-1)_n) elements; evaluation at any root of Phi_N in any R-algebra truncates at N and equals the finite Kashaev sum; bridge to TarskiSignKashaev.kashaevFigureEight (c = z + z^-1).
- P2: twist knots K_p via Masbaum's cyclotomic coefficients; all colors, Kashaev = colour N at zeta_N.
- P3 (strangler): FigureEightVolume.kashaev (Real.cos form) becomes the archimedean reading of the P1 element; the |1-zeta^j|^2 = 2-2cos comparison goes behind QOU/Transcendental/; shrink the boundary baseline.
- P4: the map R^[q] -> R[[h]], q = 1+h (Ohtsuki series of the Habiro element), compared with QOU/BringsSurface/OhtsukiKappaFormal and QOU/Nuclear/OhtsukiKappaSign.
- P5: bar involution q -> q^-1 on R^[q]; 4_1 bar-invariant, 3_1 maps to its mirror. Algebraic, so KashaevReflection-type facts move off the analytic side.

Overlaps: Coev strangler thread (QCalculus/HabiroBracket, HabiroCyclotomicOddLocus, #9552/#9569); dilog-Bloch / knot-volume thread (qou-pc7n Hermitian certificates). Existing ZZ-only ring: BraidKnotOctonion/QHabiroCompletion (could later become the R = ZZ instance).

## Owner scope (2026-11-27 19:05Z, "A C")
A then C: cyclotomic-series constructor + 3_1, 4_1, then twist knots via Masbaum (P1-P2) now; the general cyclotomic expansion for every knot (Habiro's theorem, quantum-group setup) is the long-run goal, added as P6.

## Progress
- 2026-11-27: P1, P2 and P3 step 1 in PR #9592. P3 step 1 = QOU/Transcendental/BraidKnotOctonion/FigureEightKashaevHabiroReading (kashaev N = evalRoot zeta_N figureEight). Consumer moves wait for #9567/#9569 and the knot-volume thread (coordinate via coordinator). P4 (HabiroOhtsukiExpansion, trivial-connection expansion q=1+h) also in #9592. P5 (HabiroBarInvolution: bar, bar_bar, bar_figureEight, bar_trefoil) merged via #9604. P1-P3step1 merged via #9592 2026-11-27. P3 plan agreed with Coev thread: they move FigureEightVolume* whole to QOU/Transcendental/BraidKnotOctonion/ (same names); then this bean redefines kashaev as the archimedean instance of figureEight at the new path. Coordinator will signal.
