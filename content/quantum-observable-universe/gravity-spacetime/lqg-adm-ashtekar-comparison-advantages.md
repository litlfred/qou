## Three structural advantages

The QOU/LQG dictionary
([QOU as categorical resolution of canonical QG](#rem:lqg-adm-ashtekar-comparison))
tightens around three points where QOU avoids
well-known obstructions of the canonical programmes:

1. **No "problem of time".** ADM presupposes a continuous time
   coordinate to define the lapse $N$; quantising the Hamiltonian
   constraint $\hat H \Psi = 0$ then freezes the state. QOU has no
   inbuilt time: what emerges as macroscopic time is the
   [Reeb flow](#thm:categorical-reeb-exists), driven by the
   $q$-anomaly $d_q^2 \neq 0$ in the categorical action. The
   variational constraint $\delta \mathfrak{S}_q / \delta \nabla = 0$ is
   solved categorically without needing an external clock; transition
   amplitudes between algebraic states are the
   [Frobenius pairings](#def:frobenius-hopf-substrate), not
   Wheeler–DeWitt evolution operators.

2. **No Barbero–Immirzi fudge factor.** The continuous Ashtekar
   connection $A = \Gamma + \gamma K$ has $\gamma$ as a free
   parameter, conventionally tuned to make $S_{LQG} = A / 4 \ell_p^2$
   match black-hole entropy ($\gamma \approx 0.2740$ for the full
   $\mathrm{SU}(2)$ horizon count, $\gamma \approx 0.2375$ for the
   $U(1)$ reduction). The corresponding parameter in QOU is the
   substrate $q_0$, derived from the categorical Reeb flow and locked
   by the algebraic structure of Bring's surface ($\chi = -6$). The
   quantisation scale is fixed by the substrate, not back-solved from
   thermodynamics.

3. **Native self-duality, no reality conditions.** Ashtekar's
   original $\gamma = \pm i$ formulation made the Hamiltonian
   constraint polynomial via complex self-duality, but the resulting
   complex metric required intractable "reality conditions". QOU
   recovers exact self-duality $\star_q F_\nabla = F_\nabla$
   ([categorical instanton](#def:categorical-instanton)) as the
   $\delta \mathfrak{S}_q / \delta \nabla = 0$ output, and the
   [adelic product](#def:adelic-substrate) plus continuous
   $\mathbb{Z}_2 \to U(1)_{\xi}$ deformation (chart-swap–Reeb
   identification, [`prop:reeb-u1-chart-swap`](#prop:reeb-u1-chart-swap))
   produces the real Lorentzian archimedean projection without
   imposing reality conditions by hand.
