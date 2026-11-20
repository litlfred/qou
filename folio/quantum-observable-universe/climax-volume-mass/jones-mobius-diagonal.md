*Let*
$$
  K_q(s,t) \;=\; \mathrm{tr}\bigl(\Delta(\varrho(s)) \otimes \Delta(\varrho(t))\bigr)
$$
*be the categorical Möbius two-point kernel of [prop:mobius-energy](#prop:mobius-energy), which collapses to the repulsive $1/\lvert\varrho(s)-\varrho(t)\rvert^2$ as $q \to 1$ ([Frobenius–Hopf kernel](#lem:mobius-energy-frobenius-kernel)). Write the Hadamard finite-part decomposition of the categorical Möbius energy obtained by excising the diagonal,*
$$
  E_{\mathrm{cat}}(\varrho)
  \;=\;
  \underbrace{T_{\mathrm{reg}}(\varrho)}_{\text{regularized two-point}}
  \;-\;
  \underbrace{C(\varrho)}_{\text{diagonal contact}} ,
$$
*Then the contact coefficient $C(\varrho)$ is the fundamental ($N=2$) Markov trace, whose braid closure is the Jones polynomial ([Jones–Markov trace](#thm:jones-markov-trace))*
$$
  C(\varrho) \;=\; \mathrm{tr}_M(\rho(\beta_K)) \;=\; J_K(q).
$$
*Consequently*
$$
  J_K(q) \;=\; T_{\mathrm{reg}}(\varrho) \;-\; E_{\mathrm{cat}}(\varrho):
$$
*The fundamental Jones polynomial is exactly the self-energy that the Möbius renormalization subtracts. The fundamental Jones data embeds into the Möbius two-point data as its contact / diagonal term; the converse map loses the off-diagonal fusion content $\Delta(e_\lambda) = \sum_{\mu\nu} N^\lambda_{\mu\nu}\, e_\mu \otimes e_\nu$.*
