**$\mathfrak{Q}_\beta$ cos-resummation (conditional on the $\beta$-decay transfer matrix).**
*Let $z = q^3/(q^2+1)$ be the Markov parameter and $h = q - q^{-1}$. The cos-resummation dresses a $\mathfrak{Q}_\beta$ base by the classical cosine of the half eigenphase:*
$$
  \mathfrak{Q}_\beta^{\mathrm{cos}}
  \;:=\;
  \mathfrak{Q}_\beta^{\mathrm{base}} \cdot \cos\alpha,
  \qquad
  \alpha = \tfrac{(z-1)\,h}{2},
  \quad
  z = \tfrac{q^3}{q^2+1},
  \quad
  h = q - q^{-1}.
$$
*Since $|\cos\alpha| \le 1$, the factor is a contraction: it can only lower $|\mathfrak{Q}_\beta^{\mathrm{base}}|$.*

The transfer matrix $M_\beta$ is posited to have spectrum $\{e^{+i\alpha},\, e^{-i\alpha}\}$ on the $2$-dimensional irreducible representation $V_{(2,1)}$ of $H_3(q)$. Under that identification the Markov trace symmetrizes the two eigenphases:
$$
  \tfrac12\,\mathrm{tr}\bigl(M_\beta|_{V_{(2,1)}}\bigr)
  \;=\;
  \cos\alpha
  \;=\;
  \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr).
$$

Its numerical evaluation at the proton-anchored $q_0$ and comparison with CODATA are recorded in [the comparison remark](#rem:q-beta-cos-resummation-comparison).

**Non-invariance under the bar involution.** Deriving an even resummation factor from $q \mapsto q^{-1}$ would require $z(q^{-1}) = z(q)$ so that $\alpha \mapsto -\alpha$. For $z(q) = q^3/(q^2+1)$, however, $z(q^{-1}) = 1/(q^3+q) \neq z(q)$ whenever $q \neq 1$ (unlike bar-symmetric expressions such as $1/(q^{1/2}+q^{-1/2})$). Consequently, the bar involution does not negate $\alpha$ at $z = q^3/(q^2+1)$, and the cosine factor is stated as a tested definition rather than a consequence of bar symmetry.

