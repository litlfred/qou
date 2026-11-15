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

**Comparison with measurement at the proton pin $q_0 \approx 1.1099785827513808$.** At $q_0$ one has $z_D \approx 0.6126880371$, $h \approx 0.2090602988$, $\alpha \approx -0.0404857773$ and $\cos\alpha \approx 0.9991805629$. Two bases are recorded side by side; neither is selected by its residual.

1. **Ruled base** (owner ruling 2026-09-08: $\varepsilon$ is the Markov trace at $z_D$), $\mathfrak{Q}_\beta^{z_D} = \bigl|h^2/2 - h\,z_D\bigr|\,E_0$ with $E_0 = m_e/(q(q-1))$: $\mathfrak{Q}_\beta^{z_D} \approx 0.4447004085$ MeV, residual $\approx -431571.8$ ppm against CODATA $0.78233341$ MeV. The cos factor gives $\mathfrak{Q}_\beta^{z_D,\cos} \approx 0.4443360045$ MeV, residual $\approx -432037.5$ ppm. **The refinement moves this residual away from zero.** This is forced, not tuned: the base lies below CODATA, so the required factor exceeds $1$, while $\cos\alpha \le 1$ for every real $\alpha$.
2. **Form A** (retired as the base; historical cross-check only), $\mathfrak{Q}_\beta^A = m_e\,|q^2-2q-1|(q+1)/(2q^3) \approx 0.7836458274$ MeV, residual $\approx +1677.6$ ppm. With the convention-D phase, $\mathfrak{Q}_\beta^{A,\cos} \approx 0.7830036789$ MeV, residual $\approx +856.8$ ppm, a $1.96\times$ tightening.

**Status of the structural justification under D.** The original argument for the cosine was Markov cyclicity: the bar involution $q \mapsto q^{-1}$ was taken to send $\alpha \mapsto -\alpha$, forcing an even resummation. That step used the bar-invariance $z(q^{-1}) = z(q)$, which holds for convention C and **fails** for $z_D$, since $z_D(q^{-1}) = 1/(q^3+q) \neq z_D(q)$. Under D the bar involution therefore does not map $\alpha$ to $-\alpha$, and evenness of the resummation is no longer derived; the cosine form is retained here as the definition being tested, not as a consequence.

The resummation lives in the real-$q$ (archimedean) regime of the framework's dilogarithm context-sorting, fixed once by the [$\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification).
