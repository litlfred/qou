Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)) with substrate
parameter $q$ ([Definition](#def:substrate-parameter)),
categorical action $\mathfrak{S}_q$
([Definition](#def:categorical-action)), and $q$-Hodge star
$\star_q$ ([Definition](#def:q-hodge-star)).

Let $\varrho \colon S^1 \to \tau(A)$ be a smooth closed curve
(a knot embedding) and let $\mathfrak{m}(\varrho)$ denote the categorical mass
([Theorem](#thm:topological-mass)).

Define the *categorical Möbius energy* by

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

where $\Delta$ is the Hopf comultiplication, $\int_A$ is the
Frobenius form ([Remark](#rem:frobenius-simplification)), and the
integration excludes the diagonal $\mathrm{diag} \subset S^1 \times S^1$.

Then in the classical limit $q \to 1$, the categorical Möbius energy
recovers the classical Möbius energy up to a topological normalization:

$$
  \lim_{q \to 1} E_{\mathrm{cat}}(\varrho)
  = 
  \frac{1}{4} E(\varrho)
  +  \text{const}.
$$

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
  ds dt.
$$

Here $D(\varrho(s), \varrho(t))$ denotes the intrinsic arc-length distance
along $\varrho$.
