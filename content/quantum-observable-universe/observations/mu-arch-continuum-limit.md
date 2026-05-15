**Conjecture ($\mu_{\mathrm{arch}}$ continuum limit).**
*There exists a measure-valued Archimedean realisation functor*
$$
  \mu_{\mathrm{arch}}
  \colon
  \bigl\{(A_q, \mathrm{tr}_M, \tilde w_\lambda)\bigr\}_{n, q}
  \;\longrightarrow\;
  \bigl\{(\mathcal{F}, \rho, \mathcal{S}_{\mathrm{CFS}})\bigr\}
$$
*sending the pre-Archimedean algebraic causal-action structure of
[`prop:algebraic-causal-action-structure`](#prop:algebraic-causal-action-structure)
to a Finster causal fermion system [`finster2021`], under the joint
Faddeev scaling $n \to \infty$, $q \to 1$, $n\lvert 1 - q\rvert \to
\infty$ used in
[dilogarithm archimedean limit](#conj:dilogarithm-archimedean-limit).
Specifically:*

1. *(Operator algebra limit.) The Hecke algebra $A_q = H_n(R, q)$
   embeds into a limiting bounded-operator algebra
   $\mathcal{F} \subset L(H)$ on a separable Hilbert space $H$, with
   the bar-involution converging to the adjoint and the regular
   representation converging to a faithful representation.*

2. *(Measure convergence.) The q-Plancherel weight $\tilde w_\lambda$,
   pushed forward along the embedding of (1), converges weakly to a
   Borel measure $\rho$ on $\mathcal{F}$. The limit measure $\rho$ has
   finite total mass on every compact subset of $\mathcal{F}$.*

3. *(Trace as causal action.) Under (1)–(2), the Markov trace
   evaluated at fixed-degree elements satisfies*
   $$
     \lim \mathrm{tr}_M(x \cdot y)
     \;=\;
     \iint_{\mathcal{F}\times\mathcal{F}}
       \mathcal{L}(\xi, \eta)\,d\rho(\xi)\,d\rho(\eta),
   $$
   *where $\mathcal{L}$ is the Finster causal Lagrangian
   [`finster2024`, §2] for the pair $(\xi, \eta)$. Equivalently, the
   discrete categorical action of QOU converges to the continuous
   causal action of CFS.*

4. *(Active set as $\mathrm{supp}(\rho)$.) The LP active sets
   $\widehat{A}_q^{\,\mathrm{active}}$ converge, after pushforward, to
   the support of $\rho$. Under (3), $\mathrm{supp}(\rho)$ is the
   emergent CFS spacetime; on the QOU side it is the LP analogue of
   the same locus.*

**Why this is conjectural.** Each of (1)–(4) packages a non-trivial
analytic result:

- (1) is an asymptotic embedding theorem for Hecke algebras into
  bounded operators on a Hilbert space. The free-probability framework
  of Biane [`biane1998`] gives an embedding for $S_n$
  (the $q = 1$ specialisation) into the free group factor; the
  q-deformed version is not in the literature in the form needed.

- (2) is an asymptotic Plancherel theorem in the spirit of
  Kerov–Vershik [`kerov1981`] and Féray–Méliot [`feray2010`]. At
  $q = 1$ the limit measure on the Thoma simplex is known
  (Vershik–Kerov 1981); at $q \neq 1$ the corresponding limit is
  conjectured to exist with the same Kerov-bound regularity, but a
  full proof is open.

- (3) is the action-matching statement and is the *content* of the
  $\mu_{\mathrm{arch}}$ functor. It requires (1)–(2) plus a
  uniform-convergence control on $\mathrm{tr}_M$ comparable to the
  control needed for
  [dilogarithm archimedean limit](#conj:dilogarithm-archimedean-limit).

- (4) requires LP stability under the limit, i.e. that the discrete
  active set does not collapse or explode in the joint scaling.

**Distinction from $\tau_{\mathrm{arch}}$.** The conjectural functor
$\mu_{\mathrm{arch}}$ is *measure-valued* (target =
$\mathrm{Meas}(\mathcal{F})$); the established functor
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor))
is *scalar-valued* (target = $\mathbb{R}$). The two functors share the
factorisation through $A_q$ but project differently: $\tau_{\mathrm{arch}}$
integrates the Markov trace down to a single real period (e.g. the
Kashaev volume); $\mu_{\mathrm{arch}}$ would retain the measure data
on operators before any single-number contraction. Both are
asymptotic projections, but only one of them (the scalar one) is
established in QOU.

**Lean encoding.** Stated as a `class` carrying the four limit
fields above; instances of the class are the conjectural input. The
class allows downstream Lean theorems to be stated *conditionally* on
$\mu_{\mathrm{arch}}$ — for example, "if $\mu_{\mathrm{arch}}$ holds,
the CFS effective collapse equation [`finster2024`] is the small-slack
limit of the LP shadow-price update" — without sorry-ing the
upstream conjecture.
