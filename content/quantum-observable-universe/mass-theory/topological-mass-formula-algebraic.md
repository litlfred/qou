The companion proposition
[`prop:topological-mass-formula`](#prop:topological-mass-formula)
states the topological mass identity in its **Archimedean** form

$$
  \mathfrak{m}(K) \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^{2}}
$$

where $\mathrm{Vol}(K)$ is the hyperbolic volume of $S^3 \setminus K$
under the archimedean fibre functor. Audit §4.B flagged that
identity as a **wall risk** for callers that treat it as an
algebraic-side input. This block supplies the **algebraic-side
restatement** in $\mathbb{Q}(q)$ via $\mathrm{Vol}_q(K)$
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)),
with the Archimedean form recovered as a specialisation under
$\tau_{\mathrm{arch}}$.

## Statement

**Proposition (algebraic topological mass formula).**
*Let $\beta \in H_n(R, q)$ be the Hecke normal form of a closed
braid $K = \widehat{\beta}$, and let
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ be the
algebraic quantum volume
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)).
Then the categorical mass of the vortex $\varrho_\beta$ admits the
$\mathbb{Q}(q)$-valued closed form*

$$
  \mathfrak{m}_{\mathrm{alg}}(\beta)
  \;=\;
  \frac{\Phi_1(\beta)}{\hbar_q^{2}},
\qquad
  \Phi_1(\beta) \;=\; \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\; \ln\!\bigl\lvert\mathrm{Vol}_{q_0}(\beta)\bigr\rvert,
$$

*where $\hbar_q = (q-1)/q$ is the quantum Planck constant
([`def:quantum-planck-constant`](#def:quantum-planck-constant)) and
the symbol $\tau_{\mathrm{arch}}$ is the archimedean specialisation
$q \mapsto q_0$ followed by the absolute logarithm
([`def:archimedean-realization-functor`](#def:archimedean-realization-functor)).
The identity holds in $\mathbb{Q}(q)$ before the
$\tau_{\mathrm{arch}}$ application.*

*Equivalently, the descended-trace + brane-tower decomposition*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl|\,\mathrm{tr}_M(\rho(\beta))\,\bigr|
  \;+\;
  \sum_{i = 1}^{N} \Phi_q\!\bigl(\bigl|\hat V_i(q)\bigr|\bigr)
  \;+\;
  z^2 \sum_{(i, j) \in \mathcal{P}}
    \Phi_q\!\bigl(\bigl|\hat V_i(q) \hat V_j(q)\bigr|\bigr)
$$

*([`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified) +
[`lem:tower-pair-equality-fixed-level`](#lem:tower-pair-equality-fixed-level))
is an equality in $\mathbb{Q}(q)$ at every term: the descended
piece is the Markov trace of the braid word; the singleton
sum is the level-$0$ singleton contribution; the pair sum is the
level-$0$ pair contribution. Every $\hat V_i(q)$ is an element of
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$.*

## Why this is the algebraic-side statement

The archimedean version
[`prop:topological-mass-formula`](#prop:topological-mass-formula)
goes through the Chern–Simons / hyperbolic-volume correspondence,
which is post-$\tau$ — hyperbolic volume is the imaginary part of
the Chern–Simons functional, and the equality with $\mathrm{Vol}(K)$
is the volume conjecture
\cite{kashaev1997, murakami-murakami2001}. Both ingredients require
the archimedean fibre functor.

The algebraic version above replaces $\mathrm{Vol}(K)$ with
$\mathrm{Vol}_q(\beta)$, which is *defined* as a finite product in
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)).
The $\tau_{\mathrm{arch}}$ specialisation $q \mapsto q_0$ then
recovers the numerical Archimedean value $\Phi_1(\beta)$, but
**every step of the derivation up to the specialisation is in
$\mathbb{Q}(q)$**. There is no analytic continuation, no roots-of-
unity limit, no asymptotic, and no volume-conjecture borrowing.

## Compatibility with the Archimedean form

The archimedean topological mass formula
[`prop:topological-mass-formula`](#prop:topological-mass-formula)
is the **specialisation** of this algebraic version at $q = q_0$
under $\tau_{\mathrm{arch}}$:

$$
  \tau_{\mathrm{arch}}\bigl(\mathfrak{m}_{\mathrm{alg}}(\beta)\bigr)
  \;=\;
  \frac{\tau_{\mathrm{arch}}(\Phi_1(\beta))}{\hbar_q^{2}\big|_{q = q_0}}
  \;=\;
  \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^{2}},
$$

where the last equality uses the volume conjecture as a τ-side
identification (not as a derivation step).  Equivalently, the
Archimedean prop is **post-$\tau$**; the algebraic prop is
**pre-$\tau$**. Callers that need a $\mathbb{Q}(q)$-side mass
identity must cite this proposition; callers that need an
Archimedean numerical value of $\mathrm{Vol}(K)$ may cite either.
