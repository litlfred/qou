# Preregistration: gamma-gamma bonds that enter BOTH nucleons (issue #8960, item 3)

Written 2026-11-22, before any value in this directory was computed.

## Setup (fixed, copied from the existing probes)

- Hecke algebra H_6(q), sigma^2 = h sigma + 1, h = q - q^-1. Markov trace at
  convention D, z_D = q^3/(q^2+1), tr 1 = 1 (the trace of
  `gamma_gamma_bond_markov_crosscheck_probe.py`, reused).
- Nucleon 1 on strands 0,1,2 (generators 0,1). Nucleon 2 on strands 3,4,5
  (generators 3,4). Generator 2 is the interface crossing.
- Nucleon words: `nucleon_block(kind, offset)` of
  `gamma_gamma_bond_is_pair_independent_probe.py`, unmodified (offset 0 and 3).
- Free word W_free = X Y^(3). Atom word W_atom = X Y^(3) B (bond appended on
  the right, as in the existing probe).
- mu_xy = tr(W_atom) / tr(W_free), for (x,y) in {pp, pn, np, nn}.

## Class (fixed in advance)

The gamma-gamma (pair-production) words of `QOU.Mass.GammaGammaWordSelection`:
products of vertices `vertex(i) = sigma_i sigma_{i+1}^-1`.

- Length bound: at most 6 letters, i.e. 1, 2 or 3 vertices.
- Vertex positions: i in {0,1,2,3} (so i+1 <= 4 stays in H_6).
- That gives 4 + 16 + 64 = 84 words. All 84 are computed.
- "Enters both nucleons": the set of generators the word uses meets {0,1}
  AND meets {3,4}. This is the subclass item 3 asks about. The other words
  are reported as controls (they fall under the already-proved disjoint or
  overlap theorems).

No word is added, removed or reordered after seeing values.

## What counts as the pattern

"pn binds, pp and nn do not":  mu_pn < 1 AND mu_np < 1 AND mu_pp > 1 AND
mu_nn > 1. A weak form (at least one of mu_pn, mu_np < 1, with mu_pp > 1 and
mu_nn > 1) is also reported, labelled weak. Every word, every pair is in the
table whatever it says.

## Evaluation points

- Proton pin q = Fraction(Q_50_DIGIT_STR) from qou_substrate.constants
  (exact rational arithmetic, no float).
- q = 1 (h = 0, z_D = 1/2). Expected by construction: the p and n words
  coincide at h = 0, so all four mu are equal at q = 1 for every word, and
  the pattern cannot hold there. This agrees with the working assumption
  m_p = m_n at q = 1 (bean qou-az9l).
- Symbolic q only if it runs in reasonable time; otherwise not claimed.

---

## Results (added AFTER the run; nothing above was changed)

- Class counts at q0: both 56, nuc1_only 14, nuc2_only 14.
- Strong pattern (pn, np < 1; pp, nn > 1): **0 of 56** (0 of 84).
- Weak pattern: 1 word, `[3,1,2]` = sigma3 sigma4^-1 sigma1 sigma2^-1 sigma2 sigma3^-1
  (mu_pp 1.1013, mu_pn 0.8941, mu_np 1.3018, mu_nn 1.0569). It binds pn but not np,
  so it is order-dependent; it is not the pattern.
- q = 1: all four mu equal for every word, pattern nowhere (as expected).
- Structure found (not preregistered): a bond with no gap letter (sigma_2), or one,
  gives mu_xy = f(x) g(y), hence mu_pp mu_nn = mu_pn mu_np, which excludes the strong
  pattern whenever mu > 0. Proved sorry-free: `towerTr_gapBond`,
  `towerTr_singleGapBond`, their cross-ratio corollaries, `not_both_lt_one_of_crossRatio`
  (shadow file MassEndomorphism/MarkovTraceGapBond.lean). Cross-ratio holds exactly for
  47 of the 56 "both" words; it fails for 9 words with 2 or 3 gap letters, and none
  of those 9 shows the pattern either.
