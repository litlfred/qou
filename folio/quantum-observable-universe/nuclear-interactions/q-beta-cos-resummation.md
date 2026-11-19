**$\mathfrak{Q}_\beta$ cos-resummation (conditional on the $\beta$-decay transfer matrix; convention D).**
*Let $z = z_D = q^3/(q^2+1)$ be the convention-D Markov parameter and $h = q - q^{-1}$. The cos-resummation dresses a $\mathfrak{Q}_\beta$ base by the classical cosine of the half eigenphase:*
$$
  \mathfrak{Q}_\beta^{\mathrm{cos}}
  \;:=\;
  \mathfrak{Q}_\beta^{\mathrm{base}} \cdot \cos\alpha,
  \qquad
  \alpha = \tfrac{(z_D-1)\,h}{2},
  \quad
  z_D = \tfrac{q^3}{q^2+1},
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
  \cos\!\bigl(\tfrac{(z_D-1)\,h}{2}\bigr).
$$

Its evaluation under the proton calibration and the comparison with CODATA are recorded in [the comparison remark](#rem:q-beta-cos-resummation-comparison).

**Bar-involution parity under convention D.** Expressing the resummation as an even function $\cos\alpha$ originally rested on bar-invariance $z(q^{-1}) = z(q)$, which sends $\alpha \mapsto -\alpha$ under $q \mapsto q^{-1}$. That symmetry holds for convention C and **fails** for $z_D$, since $z_D(q^{-1}) = 1/(q^3+q) \neq z_D(q)$. Under convention D the bar involution therefore does not map $\alpha$ to $-\alpha$, and evenness of the resummation is no longer derived; the cosine form is stated here as the ansatz under test rather than as a symmetry consequence.

The resummation lives in the real-$q$ (archimedean) regime of the framework's dilogarithm context-sorting, fixed once by the [$\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification).
