**Proposition (algebraic causal-action structure on $A_q$).**
*Let $R = \mathbb{Z}[q^{\pm 1/2}]$ with $q$ generic (away from
non-trivial roots of unity), $n \geq 1$, and let $A_q = H_n(R, q)$ be
the Iwahori–Hecke algebra. Write*

$$
  \tilde w_\lambda \;:=\; \frac{\dim_q^2(\lambda)}{[n]_q!}
  \quad (\lambda \vdash n)
$$

*for the q-deformed Wedderburn weight on the dual
$\widehat{A}_q = \{\lambda \vdash n\}$
([Wedderburn weight canonical form](#prop:wedderburn-weight-canonical)),
and let $\chi_\lambda \colon A_q \to R$ be the irreducible character
of the simple summand $\mathrm{End}_R(S^\lambda_q)$. Then the
following hold simultaneously, purely in $R\otimes\mathbb{Q}$:*

1. *(Trace as Plancherel integral.) The Markov trace
   $\mathrm{tr}_M \colon A_q \to R\otimes\mathbb{Q}$
   ([Jones–Markov trace](#thm:jones-markov-trace)) decomposes as*
   $$
     \mathrm{tr}_M(x) \;=\; \sum_{\lambda \vdash n}
       \tilde w_\lambda \cdot \chi_\lambda(x)
     \qquad \text{for all } x \in A_q.
   $$
   *Equivalently, $\mathrm{tr}_M$ is integration of the central
   character against the discrete measure $\tilde w_\lambda$ on
   $\widehat{A}_q$.*

2. *(Variational principle as LP.) Let
   $t \in R^{\widehat{A}_q}$ be a weight vector (Markov traces of
   basis elements),
   $G \in R^{\widehat{A}_q \times \widehat{A}_q}$ the Frobenius Gram
   matrix
   ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)), and
   $n_{\mathrm{target}} \in R_{>0}$ a target net value. The
   operator-selection primal–dual program
   ([operator-selection LP](#prop:operator-selection-lp))*
   $$
     \begin{aligned}
       \text{(P)}\quad &\min_{x \in R^{\widehat{A}_q}}
         \;\sum_\lambda t_\lambda \, x_\lambda
         &\text{s.t. } &
           \sum_\lambda x_\lambda = n_{\mathrm{target}},\;
           G\,x \geq 0,\; x \geq -M, \\
       \text{(D)}\quad &\max_{(y_0, y)}\;
         n_{\mathrm{target}} \, y_0
         &\text{s.t. } &
           y_0 \cdot \mathbf{1} + G^{\!\top} y \leq t,\;
           y_0 \in R,\; y \geq 0,
     \end{aligned}
   $$
   *admits an optimal pair
   $(x^\star, y^\star) = (x^\star,\, y_0^\star,\, y_\lambda^\star)$
   with zero duality gap*
   $$
     \sum_\lambda t_\lambda\, x^\star_\lambda
     \;=\;
     n_{\mathrm{target}}\,y_0^\star.
   $$
   *Here $y_0$ is the dual variable for the net (equality) constraint
   and is free in sign; $y_\lambda \geq 0$ are the dual shadow prices
   for the Frobenius positivity inequalities, coupled to the primal
   weights $t$ via the dual constraint
   $y_0 \cdot \mathbf{1} + G^{\!\top} y \leq t$. The active set*
   $$
     \widehat{A}_q^{\,\mathrm{active}}
     \;:=\;
     \bigl\{\lambda \vdash n \;:\; y^\star_\lambda > 0 \bigr\}
   $$
   *is non-empty whenever the primal is non-trivially feasible (some
   Frobenius constraint binds at $x^\star$), and by complementary
   slackness $G\,x^\star$ vanishes on
   $\widehat{A}_q^{\,\mathrm{active}}$.*

3. *(Mirror dictionary.) The triple
   $\bigl(A_q, \mathrm{tr}_M, \tilde w_\lambda\bigr)$ together with
   the LP duality of (2) constitute a discrete, $R\otimes\mathbb{Q}$-
   valued analogue of the Finster causal-action data
   $(\mathcal{F}, \rho, \mathcal{S}_{\mathrm{CFS}})$
   [`finster2021`, `finster2024`] under the dictionary*

   | CFS object | QOU algebraic-side analogue |
   |---|---|
   | Operator set $\mathcal{F} \subset L(H)$ | Hecke algebra $A_q = H_n(R, q)$ |
   | Universal measure $\rho$ on $\mathcal{F}$ | q-Plancherel weight $\tilde w_\lambda$ on $\widehat{A}_q$ |
   | Spectral projectors of $xy$ | Wedderburn idempotents $e_\lambda$ |
   | Lagrangian $\mathcal{L}(x,y)$ | Central-character polynomial $\chi_\lambda(x\,y)$ |
   | Causal action $\mathcal{S} = \iint \mathcal{L}\,d\rho\,d\rho$ | Markov trace $\sum_\lambda \tilde w_\lambda \chi_\lambda$ |
   | $\mathrm{supp}(\rho)$ (emergent spacetime) | LP active set $\widehat{A}_q^{\,\mathrm{active}}$ |
   | Stationarity of $\rho$ for $\mathcal{S}$ | LP optimality and strong duality |

*All four columns are statements over $R\otimes\mathbb{Q}$; no
Archimedean completion is invoked.*

**Status.** Part (1) is a rearrangement of the
Schur–Weyl Plancherel identity for $H_n(R, q)$; the q-deformed weight
$\tilde w_\lambda$ is the q-deformation of the Plancherel measure
matched to $\mathrm{tr}_M$ via the Wenzl–bridge construction
([Plancherel term-7 formulation](#prop:plancherel-term-7-formulation)).
Part (2) is the existing operator-selection LP infrastructure
(CLAUDE.md §"LP/SDP duals — first-class infra"), now interpreted as the
algebraic analogue of the CFS variational principle. Part (3) is
purely a dictionary: it asserts no new mathematics beyond (1) and (2),
but fixes the correspondence under which CFS literature can be
read against QOU.

**What part (3) does not assert.** It does *not* assert that
$\tilde w_\lambda$ converges to a Finster universal measure in any
limit (that is the conjectural
$\mu_{\mathrm{arch}}$
([μ_arch continuum limit](#conj:mu-arch-continuum-limit))),
nor that the LP Euler–Lagrange conditions match the CFS
Euler–Lagrange equations as differential PDEs. The dictionary holds
discretely, in $R\otimes\mathbb{Q}$, as a categorical mirror of the
CFS variational data; the Archimedean lift is a separate question.
