*For a closed braid knot with Hecke normal form $T_w \in H_n(R, q)$, the categorical mass admits the symbolic decomposition:*

$$
  \mathfrak{m}_{q_0, \mathcal{K}}
  \;=\;
  \bigl|\int_A T_w(q_0)\bigr|
  \;+\;
  \sum_{\ell = 1}^{\ell(\mathcal{K}, q_0)}
    r_\ell(T_w; q_0),
  \qquad
  r_\ell(T_w; q_0)
    \;=\;
    \frac{\mathrm{Res}_{q = \zeta_\ell}\!
      \bigl[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)\bigr]}
    {q_0 - \zeta_\ell}.
$$

*The numerators are the stratum residues feeding the cyclotomic coefficients $a_m$ of the Habiro expansion.*

The confinement filtration makes $H_n(R, q)$ a filtered differential algebra. The residue $r_\ell(T_w; q_0)$ is the pairing of the trace integral with the level-$\ell$ filtration stratum. The sum evaluated across all strata constructs the total mass.

The Cauchy-kernel factor $1/(q_0 - \zeta_\ell)$ is a formal symbol. The expression is an identity in the Grothendieck group of the filtered algebra rather than a convergent complex-analytic equality. The primitive roots of unity densely pack $S^1$, destroying any meromorphic neighborhood. The Habiro cyclotomic completion supplies the rigorous convergent framework.

Under the fibre functor $\tau$, the categorical filtration stratum maps to the geometric jet bundle on the elliptic curve. The cyclotomic residues map to Picard-Lefschetz residues at the discriminant locus off $S^1$, forcing convergent evaluation on the archimedean side.
