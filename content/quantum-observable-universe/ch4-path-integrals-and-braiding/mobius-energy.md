Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)) with substrate
parameter $q$ ([Definition](#def:substrate-parameter)),
categorical action $\mathcal{S}_q$
([Definition](#def:categorical-action)), and $q$-Hodge star
$\star_q$ ([Definition](#def:q-hodge-star)).

Let $\gamma \colon S^1 \to \tau(A)$ be a smooth closed curve
(a knot embedding) and let $m(\gamma)$ denote the categorical mass
([Theorem](#thm:topological-mass)).

Define the *categorical Möbius energy* by

$$
  E_{\mathrm{cat}}(\gamma)
  \;=\;
  \int_A \!\circ\, \mathrm{tr}_A \!\iint_{S^1 \times S^1 \setminus \mathrm{diag}}
  \!\!\Bigl(
    \Delta(\gamma(s)) \otimes \Delta(\gamma(t))
  \Bigr)
  \;\star_q\;
  \Bigl\lVert
    \frac{d\gamma}{ds} \wedge_q \frac{d\gamma}{dt}
  \Bigr\rVert\,
  ds\, dt\,,
$$

where $\Delta$ is the Hopf comultiplication, $\int_A$ is the
Frobenius form ([Remark](#rem:frobenius-simplification)), and the
integration excludes the diagonal $\mathrm{diag} \subset S^1 \times S^1$.

Then in the classical limit $q \to 1$, the categorical Möbius energy
recovers the classical Möbius energy up to a topological normalization:

$$
  \lim_{q \to 1}\; E_{\mathrm{cat}}(\gamma)
  \;=\;
  \frac{1}{4}\, E(\gamma)
  \;+\; \text{const}\,.
$$

Here $E(\gamma)$ is the classical Möbius energy

$$
  E(\gamma)
  \;=\;
  \iint_{S^1 \times S^1}
  \Bigl(
    \frac{1}{\lvert \gamma(s) - \gamma(t) \rvert^2}
    \;-\;
    \frac{1}{D(\gamma(s), \gamma(t))^2}
  \Bigr)
  \lvert \gamma'(s) \rvert \, \lvert \gamma'(t) \rvert\,
  ds\, dt\,.
$$

Here $D(\gamma(s), \gamma(t))$ denotes the intrinsic arc-length distance
along $\gamma$.
