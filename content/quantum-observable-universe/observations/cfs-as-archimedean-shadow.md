Combining the algebraic structure
([prop:algebraic-causal-action-structure](#prop:algebraic-causal-action-structure))
with the conjectural lift
([conj:mu-arch-continuum-limit](#conj:mu-arch-continuum-limit))
yields a clean picture of how the Finster program relates to QOU.

**The factorisation.** The QOU archimedean realisation already
factors through an operator algebra: the fibre functor $\tau$ lands in
vector spaces carrying the Schur–Weyl action of $H_n(R, q)$, the
Markov trace collapses that action to a Laurent polynomial in $R$, and
$\pi_\infty$ then projects to a real period. Schematically,

$$
  \tau_{\mathrm{arch}} \;:\;
  \mathbf{C}
  \;\xrightarrow{\;\tau\;}\;
  A_q
  \;\xrightarrow{\;\mathrm{tr}_M\;}\;
  R = \mathbb{Z}[q^{\pm 1/2}]
  \;\xrightarrow{\;\pi_\infty\;}\;
  \mathbb{R}.
$$

The operator-algebra layer $A_q$ is suppressed in the current
established statement of $\tau_{\mathrm{arch}}$ because its targets
(Kashaev volume, classical dilogarithm) are scalars. But the layer is
there, and it carries the q-Plancherel measure $\tilde w_\lambda$
that the scalar realisation integrates out.

**Two parallel routes out of $A_q$.**
The Hecke layer admits two natural Archimedean continuations:

$$
  \begin{array}{cccccc}
    A_q & \xrightarrow{\;\mathrm{tr}_M\;} & R
      & \xrightarrow{\;\pi_\infty\;} & \mathbb{R}
      & \quad\text{(scalar, established: $\tau_{\mathrm{arch}}$)} \\[2pt]
    A_q & \xrightarrow{\;\tilde w_\lambda\;} & \mathrm{Meas}(\widehat{A}_q)
      & \xrightarrow{\;\mu_{\mathrm{arch}}\;} & \mathrm{Meas}(\mathcal{F})
      & \quad\text{(measure-valued, conjectural)}
  \end{array}
$$

Under this picture, *CFS is the natural target of the second route*.
Finster's universal measure $\rho$ on $\mathcal{F}$ would arise as
$\mu_{\mathrm{arch}}(\tilde w_\lambda)$, and the Finster causal
action
$\mathcal{S}_{\mathrm{CFS}} = \iint \mathcal{L}\,d\rho\,d\rho$ would
arise as the post-wall image of the algebraic Markov-trace identity
$\mathrm{tr}_M = \sum_\lambda \tilde w_\lambda \chi_\lambda$. The
scalar route $\tau_{\mathrm{arch}}$ recovers periods (volumes,
dilogarithms); the measure route $\mu_{\mathrm{arch}}$ would recover
the universal measure of CFS.

**What this says about Gemini's framing.** A reading of the CFS
literature in which "CFS is the Archimedean realisation of QOU"
is correct only if "Archimedean realisation" refers to the
conjectural measure-valued route $\mu_{\mathrm{arch}}$ — *not* the
established scalar functor $\tau_{\mathrm{arch}}$, whose targets are
manifestly different (real numbers, not measures on operators). The
two functors share their factorisation through $A_q$ but project to
different categories of objects. Conflating them obscures the fact
that QOU's algebraic-side mirror of CFS
([prop:algebraic-causal-action-structure](#prop:algebraic-causal-action-structure))
is already proven, while the measure-valued continuum limit
remains an open analytic problem.

**Useful asymmetries.** Each side of the wall reveals data the other
hides.

- QOU's algebraic side sees the integral / cyclotomic structure of
  $A_q$, the bar-involution, and the Wedderburn–LP geometry of the
  active set. CFS sees none of these: the projection to $\mathbb{C}$
  via $\pi_\infty$ discards p-adic and root-of-unity information.
- CFS's continuum side sees the spectral measure $\rho$ on a
  continuous operator algebra, Borel sets in $\mathcal{F}$, and
  smooth families of Lagrangians. QOU pre-wall sees these only as the
  finitely-supported $\tilde w_\lambda$ and the polynomial central
  characters $\chi_\lambda$.

Each framework recovers genuinely different data; their proper
relationship is the pair $(\tau_{\mathrm{arch}}, \mu_{\mathrm{arch}})$
of parallel Archimedean projections sharing the operator-algebra
factorisation through $A_q$.
