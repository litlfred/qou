The classical Riemann hypothesis states that every non-trivial zero $\rho$ of the Riemann zeta function satisfies $\mathrm{Re}(\rho) = 1/2$ ([Riemann hypothesis](#conj:classical-riemann-hypothesis)). This remark expresses the QOU stability argument for that claim as a literal surreal inequality.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), so that $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The scaling laws of [surreal rate calculus](#prop:surreal-rate-calculus) hold:

$$
\Delta_q \asymp \varepsilon^3, \qquad \Omega_q \asymp \varepsilon^{-1}.
$$

Let $\rho$ be a hypothetical zero of $\zeta(s)$ with $\mathrm{Re}(\rho) = 1/2 + \delta$ for some $\delta \in \mathbb{R}$, $\delta > 0$. Call $\delta$ the rogue-zero drift.

By [collapse of the quantum gap](#thm:quantum-gap-collapse) and the Hasse--Weil alignment at every prime fibre, the energy required to relocate a zero from $\mathrm{Re}(\rho) = 1/2$ to $\mathrm{Re}(\rho) = 1/2 + \delta$ is

$$
E(\delta) \asymp \delta^2 \cdot \Omega_q \asymp \delta^2 \cdot \varepsilon^{-1},
$$

while the available dissipation from the mass gap is $\Delta_q \asymp \varepsilon^3$. Therefore

$$
\frac{E(\delta)}{\Delta_q} \asymp \frac{\delta^2 \cdot \varepsilon^{-1}}{\varepsilon^3} = \delta^2 \cdot \varepsilon^{-4} \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

By [surreal squeeze](#lem:surreal-squeeze), $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ in $\mathbb{R}(\varepsilon)$ whenever $\delta > 0$ is a standard real. Equivalently, $\ordw\bigl(E(\delta)\bigr) = 1 > -3 = \ordw(\Delta_q)$ in the $\omega$-adic order of [Big-O via $\ordw$](#rem:conway-normal-form): the cost sits at strictly higher $\omega$-order than the budget.

No configuration of the QOU aether can sustain a standard-real drift $\delta > 0$. The only value of $\delta$ with $E(\delta) \leq \Delta_q$ in the ordered field is $\delta = 0$, i.e., $\mathrm{Re}(\rho) = 1/2$. This realizes, at the level of surreal arithmetic, the equivalence [macroscopic stability $\Leftrightarrow$ RH](#conj:macroscopic-stability-equivalence).

The informal bound "as $q \to 1^+$, the energy cost $O(\delta^2 (q-1)^{-1})$ exceeds the closing mass gap $O((q-1)^3)$" becomes a single inequality $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ inside the ordered field $\mathbb{R}(\varepsilon) \subset \mathbf{No}$. No limit is taken; the argument is algebraic rather than analytic.

The phrase "almost everywhere on the critical line" in classical partial-RH results corresponds to the standard part $\mathrm{st}(\delta) = 0$ of a surreal-valued drift—a genuine, not asymptotic, vanishing. This bound upgrades this to $\delta = 0$ on the nose for any standard real $\delta > 0$, using only the ordering of $\mathbb{R}(\varepsilon)$.
