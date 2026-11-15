---
# qou-sl3f
title: 'G5 colour-factor 2: it is the u1 part of gl_N; sl_N framing q^(-1/N) is forced by singlet transparency. Owner: adopt SU(N) frame for colour observables?'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - colour
created_at: 2026-11-15T09:00:00Z
updated_at: 2026-11-15T09:00:00Z
parent: qou-qs4c
---

**Finding (verified, sorry-free Lean pending verification):**
`level_three_colour_channel_probe` A4 misses the QCD ratio |C(3bar)/C(6)| = 2 by exactly 2.
Cause: the Hecke generator (eigenvalues q, -1/q) is the **gl_N** braiding. Its exponents are
2c_R + 1/N, where c_R = (C2(R) - 2C_F)/2 is the one-gluon colour factor. The u1 part adds the
same 1/N to both channels, and that is what makes L_sym + L_anti = 0 (|det T| = 1). The SU(N)
braiding q^(-1/N) sigma has exponents exactly 2c_R, so the ratio is (N+1)/(N-1) = 2 at N=3.

**Forced, not fitted:** in gl_N the monodromy of V around Lambda^N_q (the colour singlet /
quantum determinant) is q^2. This was shown on explicit Jimbo matrices for N=2,3 and from Young
contents for all N. Requiring the singlet to braid trivially (the SU vs U condition) gives
c^(2N) q^2 = 1, so c = q^(-1/N). The level-3 probe's A6 "e = e_max/3 exactly" is this value at N=3.

Probe: computations/probes/sl_n_framing_colour_factor_probe.py (5/5).
Lean: QOU/Braiding/SlNFramingColourFactor.lean.

**Re-scope of the probe's attribution (scope a):** "det T = -1 caps colour" is right as
arithmetic, but det T = -1 is itself the gl_N (u1-carrying) normalisation and not a structural
obstruction. It is NOT the same mechanism as the nuclear cap in any sense that matters: sl_2
framing gives the nuclear ratio 3, not 33.7. That nuclear negative is scope (a).

**OPEN (owner decision):** should colour observables be read in the SU(N) frame (sigma_sl = q^(-1/N) sigma)?
Default if no ruling: nothing changes, the probe keeps reporting ratio 1, and the new probe records both arms.
Applying it universally would shift the Markov parameter z -> q^(-1/N) z and every unnormalised
tr_M(w) by q^(-writhe(w)/N). Writhe-0 words (Borromean) are untouched. Words with nonzero writhe
are touched, including the convention-D decay channel. So it must not be applied outside colour
observables without a separate ruling.

**Hypothesis only, not tested:** the stripped u1 factor q^(1/N) per crossing reads as charge
(1/N)(1/N)·N, i.e. baryon number 1/N per quark.
