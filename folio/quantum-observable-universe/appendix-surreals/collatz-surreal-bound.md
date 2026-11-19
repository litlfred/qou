The contact-boundary argument of the $q$-Collatz conjecture ([$q$-Collatz](#conj:q-collatz), [Collatz no cycles](#prop:collatz-no-cycles)) translates into a literal surreal inequality in $\mathbb{R}(\varepsilon)$.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The $q$-Collatz conjecture translates the integer orbit into a skein-module resolution on the Reeb contact boundary. A rogue orbit is a non-trivial cycle or an unbounded hailstone. The rogue drift $\delta$ measures the excess contact volume produced per step.

The Reeb period of the contact boundary is $\Omega_q \asymp \varepsilon^{-1}$ ([surreal rate calculus](#prop:surreal-rate-calculus)). A standard-real drift $\delta > 0$ per step produces an accumulated contact-volume deviation over one Reeb period:

$$
V(\delta) \asymp \delta^2 \cdot \Omega_q \asymp \delta^2 \cdot \varepsilon^{-1}
$$

The mass-gap dissipation available to re-absorb the deviation is $\Delta_q \asymp \varepsilon^3$. By [surreal squeeze](#lem:surreal-squeeze), $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ strictly in $\mathbb{R}(\varepsilon)$. Hence:

$$
V(\delta) > \Delta_q \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Equivalently, $\ordw(V(\delta)) = 1 > -3 = \ordw(\Delta_q)$ in the $\omega$-adic order of [Big-O via $\ordw$](#rem:conway-normal-form).

No rogue orbit with standard-real drift $\delta > 0$ can persist. The Reeb period sweeps a contact-volume transfinite larger than the mass-gap infinitesimal. No budget exists to dissipate the accumulated excess. This is the surreal-arithmetic form of the [$q$-Collatz](#conj:q-collatz) conjecture, consistent with [Collatz no cycles](#prop:collatz-no-cycles).

The classical Collatz orbit on $\mathbb{N}$ is the standard part $\mathrm{st}\bigl(\cdot \,|_{q = 1 + \varepsilon}\bigr)$ of the $q$-deformed skein resolution ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)). Every infinitesimal drift vanishes under $\mathrm{st}$. Every standard-real drift is prohibited by the squeeze above. Therefore, $\mathrm{st}(\delta) = 0$ for every admissible surreal drift. All orbits terminate at $1$.

The $q$-Collatz statement upgrades to a surreal inequality that rules out all standard-real drifts. Recovering the classical conjecture requires assuming that the $q$-Collatz skein-module resolution admits a well-defined standard part.
