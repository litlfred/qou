**Status: an analogy, not an argument. Its conclusion is withdrawn.** This remark used to end with "all orbits terminate at $1$", which would be a proof of the classical Collatz conjecture. It is not one. The scalings $V(\delta) \asymp \delta^2 \varepsilon^{-1}$ and $\Delta_q \asymp \varepsilon^3$ are asserted and not derived from the map $\mathcal{C}_q$. No quantity attached to an orbit is shown to satisfy them. The squeeze compares two monomials in $\varepsilon$, which says nothing about any orbit. The step from the $q$-orbit to the classical orbit through the standard part assumes the conclusion. For what is actually known, see the [section introduction](#sec:collatz-intro). The text below is kept so that the analogy with the other surreal bounds can still be read.

This translates the contact-boundary argument of the $q$-Collatz conjecture ([$q$-Collatz](#conj:q-collatz), [Collatz no cycles](#prop:collatz-no-cycles)) into a literal surreal inequality in $\mathbb{R}(\varepsilon)$.

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

*If* these scalings held for some orbit invariant, no rogue orbit with standard-real drift $\delta > 0$ could persist. The Reeb period sweeps a contact-volume transfinite larger than the mass-gap infinitesimal. No budget exists to dissipate the accumulated excess. This is the surreal-arithmetic form of the [$q$-Collatz](#conj:q-collatz) conjecture, consistent with [Collatz no cycles](#prop:collatz-no-cycles).

The classical Collatz orbit on $\mathbb{N}$ is the standard part $\mathrm{st}\bigl(\cdot \,|_{q = 1 + \varepsilon}\bigr)$ of the $q$-deformed skein resolution ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)). Every infinitesimal drift vanishes under $\mathrm{st}$. Every standard-real drift is prohibited by the squeeze above. No such orbit invariant is known, so no conclusion about orbits follows.

The surreal inequality is a statement about $\varepsilon$-monomials. It does not rule out any orbit. The classical conjecture is recovered only by assuming the $q$-Collatz skein-module resolution admits a well-defined standard part.
