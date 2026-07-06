**Lemma (Jones polynomial = Möbius contact term).**
*Let*
$$
  K_q(s,t) \;=\; \operatorname{tr}\bigl(\Delta(\varrho(s)) \otimes \Delta(\varrho(t))\bigr)
$$
*be the categorical Möbius two-point kernel of [$\operatorname{prop:mobius-energy}$](#prop:mobius-energy), collapsing to the repulsive $1/\lvert\varrho(s)-\varrho(t)\rvert^2$ as $q \to 1$ ([Frobenius–Hopf kernel](#lem:mobius-energy-frobenius-kernel)). By excising the singular diagonal, we obtain the Hadamard finite-part decomposition of the categorical Möbius energy:*
$$
  E_{\mathrm{cat}}(\varrho)
  \;=\;
  \underbrace{T_{\mathrm{reg}}(\varrho)}_{\text{regularized two-point}}
  \;-\;
  \underbrace{C(\varrho)}_{\text{diagonal contact}}.
$$
*The contact coefficient $C(\varrho)$ equals the fundamental ($N=2$) Markov trace, whose braid closure is the Jones polynomial ([Jones–Markov trace](#thm:jones-markov-trace)):*
$$
  C(\varrho) \;=\; \operatorname{tr}_M(\rho(\beta_K)) \;=\; J_K(q).
$$
*Consequently,*
$$
  J_K(q) \;=\; T_{\mathrm{reg}}(\varrho) \;-\; E_{\mathrm{cat}}(\varrho).
$$
*The fundamental Jones polynomial acts strictly as the self-energy subtracted by the Möbius renormalization. It embeds into the Möbius two-point data as the diagonal contact term. The converse mapping fails, as it discards the off-diagonal fusion content $\Delta(e_\lambda) = \sum_{\mu\nu} N^\lambda_{\mu\nu}\, e_\mu \otimes e_\nu$.*
