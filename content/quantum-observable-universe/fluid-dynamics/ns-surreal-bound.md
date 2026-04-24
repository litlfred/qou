This remark expresses the blowup mechanism of
[blowup as Yekutieli lifting obstruction](#prop:blowup-yekutieli)
as a literal surreal inequality, matching the framing already
registered for Navier--Stokes in
[body asymptotics catalog](#rem:body-asymptotics-catalog).

**Setup.** Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb
infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and
$q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)).
In the $q > 1$ regime
([$q$-NS well-posedness](#thm:q-ns-wellposedness)), the mass gap
$\Delta_q \asymp \varepsilon^3$ serves as a quantum viscosity
$\nu_q$, and the fluid is globally regular.

**The classical limit.** Near $\varepsilon = 0$, two rates compete:

| Quantity | Surreal order | Role |
|---|---|---|
| Mass-gap dissipation $\Delta_q$ | $\asymp \varepsilon^3$ | energy the substrate can absorb |
| Enstrophy ceiling $\mathcal{Z}_q$ | $\asymp \varepsilon^{-4/3}$ | energy the vortex cascade produces |

By [surreal rate calculus](#prop:surreal-rate-calculus),
$\mathcal{Z}_q \cdot \varepsilon^{4/3} \asymp 1$ (standard-real order),
while $\Delta_q \asymp \varepsilon^3$ is a positive infinitesimal.
Comparing:

$$
  \frac{\mathcal{Z}_q}{\Delta_q}
    \;\asymp\; \varepsilon^{-4/3 - 3} \;=\; \varepsilon^{-13/3}
  \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

**Surreal-squeeze form.** The NS specialisation of
[surreal squeeze](#lem:surreal-squeeze) takes
$\delta^2 \cdot \varepsilon^{-1}$ on the left with
$\delta^2 = \varepsilon^{-4/3 + 1} \cdot c = c \cdot \varepsilon^{-1/3}$
for some standard-real prefactor $c > 0$.  Since $\delta^2$ would
have to be transfinite for the squeeze to fail, but the only
physically admissible drifts are standard-real, the inequality

$$
  \mathcal{Z}_q \;>\; \Delta_q
  \qquad (\text{strictly, in } \mathbb{R}(\varepsilon))
$$

is automatic whenever the initial data carries any standard-real
enstrophy.  Equivalently,
$\Ow(\mathcal{Z}_q) = -4/3 < 3 = \Ow(\Delta_q)$ in the $\omega$-adic
order of [Big-O via $\Ow$](#rem:big-o-surreal): the cascade sits at
**lower ω-order** than the dissipation, which is the
$\Ow$-formalisation of "faster-than-viscous growth".

**Conclusion.** As $\varepsilon \to 0$ (equivalently, as the substrate
becomes classical), the enstrophy transfinite strictly outruns the
mass-gap infinitesimal in the surreal ordering.  No cancellation is
available in $\mathbb{R}(\varepsilon)$, so the classical-limit
Navier--Stokes flow cannot absorb the vorticity cascade: the velocity
field develops a finite-time blow-up.  This is the surreal content of
[blowup as Yekutieli lifting obstruction](#prop:blowup-yekutieli).

**Relation to the $\Ow$-catalog entry.** The classical Biot--Savart
scaling $|j^n v|_\Sigma \sim \Gamma / d^{n+1}$ used by
[NS obstruction computation](#prop:ns-obstruction-computation)
has $\Ow(|j^n v|_\Sigma) = -(n + 1)\,\Ow(d)$.  Summing over the jet
tower gives the $\varepsilon^{-4/3}$ ceiling above (via
$d \asymp \varepsilon^{2/3}$ along the Leray profile); the squeeze
inequality then inherits its strict-inequality status from
[surreal squeeze](#lem:surreal-squeeze).
