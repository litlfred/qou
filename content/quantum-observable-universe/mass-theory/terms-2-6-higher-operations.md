**Two structural identifications for Terms 2 and 6.**
*Of the two remaining open identifications in the spectral-sequence
framework
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications)),
the unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) carries the
following structural readings:*

1. **Term 2 (single-generator brane tower) is an infinite
   Wedderburn / Habiro-cyclotomic sum.** *The Cauchy kernel
   $\Phi_q(z) = \sum_n z^n / (q; q)_n$ is the $k \to \infty$ limit of
   the level-$k$ Jones–Wenzl trace*

   $$
     \Phi_q(z)
     \;=\;
     \lim_{k \to \infty}
       \sum_{\lambda : |\lambda| \leq k}
       w_\lambda^{(k)} \cdot z^{|\lambda|},
     \qquad
     w_\lambda^{(k)} = \dim_q(\lambda)^2 / [k]_q!,
   $$

   *with the same Wedderburn weights
   ([three-parameters Wedderburn](#prop:three-parameters-wedderburn))
   that enter at finite level. Equivalently the $(q; q)_m$
   denominator is the cyclotomic basis of Habiro's unified quantum
   invariant ([Habiro ring](#def:habiro-ring)). No new homological
   source is required: $\Phi_q$ is an infinite Wedderburn sum, not a
   Hochschild cup-product tower (see historical note).*

2. **Term 6 (jet-level prefix correction) is the GB root-of-unity
   residue sum.** *Term 6 is not a prefix-word product (all four
   tested prefix conventions fail —
   [jet-prefix GB filtration](#prop:jet-prefix-gb-filtration)); it is
   the cyclotomic residue contribution already captured by
   [GB residue spectral sum](#prop:gb-residue-spectral-sum):*

   $$
     \text{Term 6}(K)
     \;=\;
     \sum_{\ell \geq 2}
       \frac{\mathrm{Res}_{q = \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]}
            {q_0 - \zeta_\ell},
   $$

   *summed over roots of unity $\zeta_\ell$ for $\ell \geq 2$ (the
   $\zeta_1 = 1$ pole is absorbed into Terms 2, 3).*

*Both identifications are structural proposals consistent with the
algebraically-derived Wedderburn / Habiro / GB-residue machinery
already in the corpus; the dead-end Hochschild cup-product and
deformation-cohomology routes are recorded in the historical note as
closed.*
