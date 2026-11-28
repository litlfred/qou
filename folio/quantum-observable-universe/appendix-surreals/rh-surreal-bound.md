The classical Riemann hypothesis states that every non-trivial zero $\rho$ of the Riemann zeta function satisfies $\mathrm{Re}(\rho) = 1/2$ ([Riemann hypothesis](#conj:classical-riemann-hypothesis)). This remark writes the QOU stability heuristic for that claim as a surreal inequality. It is a heuristic and not a proof, for the reasons given at the end.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), so that $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The scaling laws of [surreal rate calculus](#prop:surreal-rate-calculus) hold:

$$
\Delta_q \asymp \varepsilon^3, \qquad \Omega_q \asymp \varepsilon^{-1}.
$$

Let $\rho$ be a hypothetical zero of $\zeta(s)$ with $\mathrm{Re}(\rho) = 1/2 + \delta$ for some $\delta \in \mathbb{R}$, $\delta > 0$. Call $\delta$ the rogue-zero drift.

Suppose, as a modelling assumption, that the energy required to relocate a zero from $\mathrm{Re}(\rho) = 1/2$ to $\mathrm{Re}(\rho) = 1/2 + \delta$ is

$$
E(\delta) \asymp \delta^2 \cdot \Omega_q \asymp \delta^2 \cdot \varepsilon^{-1},
$$

while the available dissipation from the mass gap is $\Delta_q \asymp \varepsilon^3$. Therefore

$$
\frac{E(\delta)}{\Delta_q} \asymp \frac{\delta^2 \cdot \varepsilon^{-1}}{\varepsilon^3} = \delta^2 \cdot \varepsilon^{-4} \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

By [surreal squeeze](#lem:surreal-squeeze), $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ in $\mathbb{R}(\varepsilon)$ whenever $\delta > 0$ is a standard real. Equivalently, $\ordw\bigl(E(\delta)\bigr) = 1 > -3 = \ordw(\Delta_q)$ in the $\omega$-adic order of [Big-O via $\ordw$](#rem:conway-normal-form): the cost sits at strictly higher $\omega$-order than the budget.

Under that assumption, and the further assumption that a configuration whose cost exceeds $\Delta_q$ cannot occur, a standard-real drift $\delta > 0$ is excluded and $\delta = 0$ remains. No limit is taken: the comparison is an inequality in the ordered field $\mathbb{R}(\varepsilon) \subset \mathbf{No}$.

**Why this is not a proof.** Neither assumption is derived. Nothing in the book relates the position of a zero of $\zeta$ to an energy, and the formula $E(\delta) \asymp \delta^2 \Omega_q$ is posited, not computed; the Hasse--Weil alignment cannot supply it, because the local Frobenius exponents of Bring's curve belong to $L(E,s)$ for the elliptic curve 50a1 and not to $\zeta(s)$. More decisively, the inequality $\delta^2 \varepsilon^{-1} > \varepsilon^3$ holds for every standard real $\delta > 0$ whatever $\delta$ measures. It uses no property of $\zeta$, so the same lines would exclude a zero off the line for a function that has one, such as the Davenport--Heilbronn function. An argument that cannot tell the Riemann hypothesis from its negation carries no evidence for either. The Riemann hypothesis remains [open](#conj:classical-riemann-hypothesis).
