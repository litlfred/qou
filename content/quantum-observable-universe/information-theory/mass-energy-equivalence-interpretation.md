**Content of the theorem.**
This relationship is not a unit convention. The crossing energy (the algebraic Skein weight from $R$-matrix braiding) equals the categorical mass (the analytic trace norm derived through the Frobenius pairing and comultiplication) multiplied by the **square of the information speed**. This factor $c_q^2$ is the square of the ratio of spatial coupling to temporal coupling in the $q$-connection.

The factor $c_q^2 = 1/(q-1)^2$ carries a direct information-theoretic interpretation. It converts the resistance to vertical (Reeb) transport (mass) into the horizontal (spatial) crossing weight (energy) by accounting for the mismatch between horizontal and vertical information rates in the $q$-connection.

**Regime behaviour of $E = \mathfrak{m} \cdot c_q^2$.**

| Regime          | $q$            | $c_q^2$         | Physics                                                          |
| --------------- | -------------- | --------------- | ---------------------------------------------------------------- |
| Deep-quantum    | $q \to \infty$ | $\to 0$         | Energy $\to 0$ for any mass: no spatial crossing weight          |
| Deep quantum    | $\varphi^2$    | $\approx 0.382$ | Sub-relativistic: mass dominates energy                          |
| Our universe    | $q_0$          | $\approx 83.2$  | $E \approx 83\mathfrak{m}$: large amplification                  |
| Near-classical  | $1.01$         | $10{,}000$      | Extreme amplification: tiny mass $\to$ large energy              |
| Classical limit | $q \to 1^+$    | $\to \infty$    | $E/\mathfrak{m} \to \infty$: classical $E = mc^2$ with $c$ large |

At $q = q_0$, a vortex with categorical mass $\mathfrak{m}$ carries crossing energy $E = \mathfrak{m}/(q-1)^2 \approx 83\mathfrak{m}$. This large amplification factor explains why nuclear energy ($E = mc^2$) releases vastly more energy than the rest mass implies in everyday units.

We work out the concrete electron consistency check ([electron consistency check](#rem:mass-energy-electron-check)) and the pair-creation reinterpretation ([pair creation reinterpreted](#rem:mass-energy-pair-creation)) separately.

**Archimedean realisation.**
Over $\mathbb{C}$, Yekutieli's nonabelian multiplicative integral \cite{yekutieli2015} realises the categorical mass ([mass over $\mathbb{C}$](#cor:mass-identity-C)). The relation $E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$ becomes:

$$
  \sum_{\text{crossings}} \epsilon_i
  = 
  \frac{1}{(q-1)^2}
  \bigl\lVert
  \mathrm{MI}\!\!\int_\Sigma
  (\nabla_A q, L \wedge F^+)
  \bigr\rVert,
$$

identifying the discrete Skein weight (spatial) with the rescaled continuous multiplicative-integral norm (temporal).
