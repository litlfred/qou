**Lemma (Jones polynomial = Möbius contact term).**
*Let*
$$
  K_q(s,t) \;=\; \operatorname{tr}\bigl(\Delta(\varrho(s)) \otimes \Delta(\varrho(t))\bigr)
$$
*be the categorical Möbius two-point kernel of
[$\operatorname{prop:mobius-energy}$](#prop:mobius-energy), which collapses to
the repulsive $1/\lvert\varrho(s)-\varrho(t)\rvert^2$ as $q \to 1$
([Frobenius–Hopf kernel](#lem:mobius-energy-frobenius-kernel)). Write the
Hadamard finite-part decomposition of the categorical Möbius energy obtained by
excising the diagonal,*
$$
  E_{\mathrm{cat}}(\varrho)
  \;=\;
  \underbrace{T_{\mathrm{reg}}(\varrho)}_{\text{regularized two-point}}
  \;-\;
  \underbrace{C(\varrho)}_{\text{diagonal contact}} ,
$$
*excising the singular diagonal. Then the contact coefficient $C(\varrho)$ is the
fundamental ($N=2$) Markov trace, whose braid closure is the Jones polynomial
([Jones–Markov trace](#thm:jones-markov-trace))*
$$
  C(\varrho) \;=\; \operatorname{tr}_M(\rho(\beta_K)) \;=\; J_K(q).
$$
*Consequently*
$$
  J_K(q) \;=\; T_{\mathrm{reg}}(\varrho) \;-\; E_{\mathrm{cat}}(\varrho):
$$
*the fundamental Jones polynomial is exactly the self-energy that the Möbius
renormalization subtracts. The fundamental Jones data embeds into the Möbius
two-point data as its contact / diagonal term; the converse map loses the
off-diagonal fusion content $\Delta(e_\lambda) = \sum_{\mu\nu} N^\lambda_{\mu\nu}\,
e_\mu \otimes e_\nu$.*

**Proof.** The kernel collapse
([Frobenius–Hopf kernel](#lem:mobius-energy-frobenius-kernel)) gives
$K_q(s,t) \to 1/r^2$ on the diagonal; its coincidence residue is the fundamental
two-point contact $C(\varrho)$, which by the Jones–Markov identity
([Jones–Markov trace](#thm:jones-markov-trace)) is the single-element Markov
trace $\operatorname{tr}_M(\rho(\beta_K)) = J_K(q)$. The categorical Möbius
energy is, by definition, the regularized two-point integral with this contact
removed — the O'Hara / Freedman–He–Wang Hadamard finite part. Rearranging the
renormalization identity $E_{\mathrm{cat}} = T_{\mathrm{reg}} - C$ gives
$C = T_{\mathrm{reg}} - E_{\mathrm{cat}}$, that is $J_K = T_{\mathrm{reg}} -
E_{\mathrm{cat}}$. The off-diagonal remainder retains the comultiplication's
fusion coefficients $N^\lambda_{\mu\nu}$, which the single-element trace does not
resolve; hence the embedding is strict. $\qquad\blacksquare$

**Surreal reading.** Under the surreal lift
([Möbius renormalization](#rem:mobius-surreal-renormalization)) the regularized
two-point $I_1$ and the contact term $I_2$ are both infinite surreals of
$\operatorname{ord}_\omega = +1$ with the *same* leading coefficient; the shared
$\omega^{+1}$ divergence **is** this contact / self-energy, and $E_{\mathrm{cat}}
= \operatorname{std}(I_1 - I_2)$ is the appreciable remainder. The lemma
identifies that shared divergence with $J_K(q)$.

**Scope.** This is the fundamental ($N=2$) base of the embedding. The
$N$-coloured contacts form the coloured-Markov-trace family
$\operatorname{tr}_M^{(N)}(\rho(\beta_K))$ whose $N \to \infty$ logarithmic
growth rate is the hyperbolic volume
([Kashaev volume–density](#rem:kashaev-volume-density)); the present lemma is the
$N=2$ rung on which that tower is built, not a claim about the limit.
