Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe ([Definition](#def:quantum-observable-universe)) with substrate parameter $q$ ([Definition](#def:substrate-parameter)), categorical action $\mathfrak{S}_q$ ([Definition](#def:categorical-action)), and $q$-Hodge star $\star_q$ ([Definition](#def:q-hodge-star)).

Let $\varrho \colon S^1 \to \tau(A)$ be a smooth closed curve (a knot embedding) and let $\mathfrak{m}(\varrho)$ denote the categorical mass ([Theorem](#thm:topological-mass)).

The *categorical Möbius energy* is defined by

$$
  E_{\mathrm{cat}}(\varrho)
  = 
  \int_A \!\circ \mathrm{tr}_A \!\iint_{S^1 \times S^1 \setminus \mathrm{diag}}
  \!\!\Bigl(
    \Delta(\varrho(s)) \otimes \Delta(\varrho(t))
  \Bigr)
  \star_q
  \Bigl\lVert
    \frac{d\varrho}{ds} \wedge_q \frac{d\varrho}{dt}
  \Bigr\rVert
  ds dt,
$$

where $\Delta$ is the Hopf comultiplication, $\int_A$ is the Frobenius form ([Remark](#rem:frobenius-simplification)), and the integration excludes the diagonal $\mathrm{diag} \subset S^1 \times S^1$.

In the classical limit $q \to 1$, the categorical Möbius energy recovers the classical Möbius energy up to a topological normalization:

$$
  \lim_{q \to 1} E_{\mathrm{cat}}(\varrho)
  = 
  \frac{1}{4} E(\varrho)
  +  \text{const}.
$$

The additive constant is not determined by the construction. Shifting
$E_{\mathrm{cat}}$ by any real $a$ shifts $\text{const}$ by $a$ while
preserving both the Möbius invariance of $E_{\mathrm{cat}}$ and the relation
itself, so every real value of $\text{const}$ is realised and no single value
holds across instances. Reading $\text{const}$ as a topological
normalisation, a quantity determined by the knot type of $\varrho$ alone,
requires further structure fixing the additive zero of $E_{\mathrm{cat}}$,
which the definition above does not supply. What is established here is the
*shape* of the classical limit: the categorical energy is an affine function of
the classical Möbius energy with slope $1/4$.

Here $E(\varrho)$ is the classical Möbius energy

$$
  E(\varrho)
  = 
  \iint_{S^1 \times S^1}
  \Bigl(
    \frac{1}{\lvert \varrho(s) - \varrho(t) \rvert^2}
    - 
    \frac{1}{D(\varrho(s), \varrho(t))^2}
  \Bigr)
  \lvert \varrho'(s) \rvert  \lvert \varrho'(t) \rvert
  ds dt,
$$

where $D(\varrho(s), \varrho(t))$ denotes the intrinsic arc-length distance along $\varrho$.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
