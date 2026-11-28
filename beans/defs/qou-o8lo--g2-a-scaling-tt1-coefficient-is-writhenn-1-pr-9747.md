---
# qou-o8lo
title: 'G2 A-scaling: T(T+1) coefficient is writhe/(N(N-1)) (PR #9747)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T21:52:11Z
updated_at: 2026-11-28T10:56:30Z
parent: qou-myts
---

Follow-up to qou-tcl2 (G2). PR #9747, branch claude/isospin-writhe-scaling-2026-11-27.

Lean QOU/Nuclear/IsospinTwistWrithe.lean (sorry-free, lean-direct exit 0): any multiplicative block invariant sees a braid word only through its writhe; the Murphy product is a word of N(N-1) letters; on a block det rho(w)^{N(N-1)} = (q^{2c})^{d e}. So the T(T+1) coefficient is writhe/(N(N-1)). Full twist (#9706) has none; chain word e = A-1 gives Theta(1/A), in [1/(9A), 2/(9A)].

Probe isospin_twist_writhe_scaling_probe (comparison only): Table 3.4b median Q_beta error 315.8% (full twist) -> 92.36% (chain), 92.19% (T3); no term 92.69%. The term is then ~0.2 MeV at 208Pb, ~1000x below the classical symmetry energy: scope-(a) negative for this channel with alpha.

Second 1/A: block dimension, ln d_T - ln d_0 = ln(2T+1) - 2T^2/N; not wired (no corpus energy map for multiplicity).

Open: bond-letter signs (G5); quark-level T3 writhe (#4618) would add an odd-in-T_z piece; block functional; scale alpha (scale-unification thread). Wiring choice put to Carl on a card.

2026-11-27 (13b375fb0, PR #9747): sign-independent bound. |writhe| <= letters (abs_writhe_wordOf_le); core (σaσb⁻¹)³ writhe 0 (writhe_core); with one bridge letter per nucleon boundary (StrandLayoutForcesChain) |coeff| <= 2κ/(9A) for any bond signs (abs_ttCoeff_le_of_chain). Still assumed: sign of the term, block log-det energy map, one bridge per boundary, scale α. Nothing wired (Carl hold).

2026-11-27 (c1f3f7c5a): on γγ-selected words (cores (σ0σ1⁻¹)³, bond (σ2σ3⁻¹)³) the writhe is 0 (GammaGammaWordSelection.writhe_eq_zero), so det^{N(N-1)} = 1 on every block: the braid-channel T(T+1) term is exactly 0 at any A (seminormal_det_gammaGamma_pow). Symmetry energy must come from block multiplicity, another functional, or non-γγ words. Not covered: nuc11_interleaved quark block.

2026-11-27 (335b6c7e2, PR #9747): multiplicity term. Lean IsospinWeightMultiplicity: d(N,k)=C(N,k)-C(N,k-1), Σ_{j≤k} d = C(N,k) (weight count = sum of blocks T≥|Tz|), log-free Gaussian bound C(2M,M-s)(M+s+s²) ≤ C(2M,M)(M+s). Weight count has no ln(2T+1); shape (N-Z)²/A from counting. Open: the energy map (count→energy); probe with ASSUMED B += α ln(count): share tracks -α·2Tz²/N to 1%, ~37x below classical; Table 3.4b median 92.7→84.3% (comparison only). Nothing wired; #9706 closed by Carl.

2026-11-27 (21058a2b1): Carl 'use qCLT'. q-CLT m2=1 at every q (qGaussMoment_two) so -2Tz^2/N coefficient unchanged; q enters at m4=2+q. Markov (conv D quantum trace) sector weight C(N,k)q^{N-k}qi^k: sum=(q+qi)^N (markov_sector_sum), mirror product = C(N,k)^2 no q (markov_sector_mirror). q-weighting adds only odd q^{2Tz}; even part classical. 37x stays in scale/energy map.

2026-11-28 (merge-steward): PR #9747 landed on `origin/main` (`e04d18bbd9dfd54f3104d451997ce6d86b992d9a`, 9/9 commits replayed); bean stays open on the count->energy map and scale items above.
