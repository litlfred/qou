**Categorical determination of the rank.**
The rank $r_q$ of the categorical Mordell--Weil group ([categorical Mordell--Weil](#def:categorical-mordell-weil)) is the multiplicity of the trivial representation $\mathbf{1}$ in the $G$-module $H^1(\mathcal{E}_q)$. This depends critically on the categorical axioms:

| Axioms | Gauge group | $H^1(\mathcal{E}_q)$ as $G$-rep | $r_q$ |
| --------------------------- | --------------------------------- | ------------------------------------------ | -------- |
| QU only | unconstrained | may contain $\mathbf{1}$ | $\geq 0$ |
| QOU (+ observability) | semisimple ($\mathfrak{g}^G = 0$) | non-trivial if color-charged | $= 0$ |
| Descartes QOU ($\chi = -6$) | $\mathrm{SU}(2)$ | $V_{1/2} \cong \mathbb{C}^2$ (fundamental) | $= 0$ |

**Proof that $r_q = 0$ in the Descartes QOU.**
The Descartes elliptic curve $\mathcal{E}_q$ is a color fiber of the color fibration ([color elliptic](#prop:color-elliptic)), so $\mathrm{SU}(2)$ acts non-trivially on it. The first cohomology $H^1(\mathcal{E}_q) \cong \mathbb{C}^2$ is two-dimensional. The only two-dimensional irreducible representation of $\mathrm{SU}(2)$ is the fundamental $V_{1/2}$. Since

$$
V_{1/2}^{\mathrm{SU}(2)} = 0,
$$

no nonzero vector in $\mathbb{C}^2$ is fixed by $\mathrm{SU}(2)$. Thus the categorical Mordell--Weil group is trivial: $\mathcal{E}_q(\mathbf{1}) = 0$ and $r_q = 0$.

The QOU axioms force this vanishing. The observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ forces $G$ to be semisimple. For any semisimple $G$, every non-trivial irreducible representation $V$ satisfies $V^G = 0$. The elliptic fiber carries a non-trivial representation because it lies in the color directions. A QU without observability could have $G$ with a center (e.g. $\mathrm{U}(2)$), but even then $V_{1/2}^{U(2)} = 0$ since the center scales all vectors. The only way to achieve $r_q > 0$ is via an elliptic curve in the spacetime directions, but $\mathcal{E}_q$ is categorically determined as a color fiber.
