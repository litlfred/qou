*Let $R$ be a field of characteristic zero and let $\alpha, \beta \in R$ be
constants. If the associated-Legendre order-ladder factor at degree
$n = d + \alpha$ and order $\mu = \beta$ reproduces the squared Hoefsmit
channel-mixing numerator identically in the axial distance $d$,*

$$
(d + \alpha - \beta)(d + \alpha + \beta + 1) \;=\; d^2 - 1
\qquad \text{for all } d \in R,
$$

*then*

$$
\alpha = -\tfrac{1}{2},
\qquad
\beta \in \bigl\{ \tfrac{1}{2},\; -\tfrac{3}{2} \bigr\},
$$

*i.e. $(n, \mu) = \bigl(d - \tfrac{1}{2}, \tfrac{1}{2}\bigr)$ up to the
Legendre reflection $\mu \mapsto -\mu - 1$. The half-integer degree shift —
the signature of the toroidal harmonic family $P^\mu_{\nu - 1/2}$ — is
forced by the Hoefsmit mixing structure, not imposed.*

## Context

The Hoefsmit seminormal block at axial distance $d$ mixes the two lepton
channels with amplitude $b$ satisfying
$b^2 = [d-1]_q [d+1]_q / [d]_q^2$
([prop:hoefsmit-binding-amplitude](#prop:hoefsmit-binding-amplitude) is the
$d = 2$ meson case $b^2 = [3]_q/[2]_q^2$). At $q \to 1$ the squared mixing
numerator is $d^2 - 1$. The associated-Legendre order-ladder factor is
$(n - \mu)(n + \mu + 1)$, and the toroidal harmonics — the separated
eigenfunctions around a vortex ring \cite{lebedev1965} — are exactly the
Legendre family at half-integer degree $\nu - \tfrac{1}{2}$
\cite{whipple1917}. The proposition says the match between the two
structures admits no freedom: the degree shift $-\tfrac{1}{2}$ and the
order $\tfrac{1}{2}$ are the unique solution.

Because the $q$-bracket identity $[d-1]_q[d+1]_q = [d]_q^2 - 1$ holds for
all $q$, the same forcing computation runs verbatim at the $q$-deformed
level (the coefficient matching gives $q^{2\alpha + 1} = 1$); the
half-integer shift survives $q$-deformation. The $q$-layer statement has been verified by direct computation.

The physical reading: the two windings $(\mu, \nu)$ of a toroidal harmonic
$P^\mu_{\nu-1/2}(\cosh\eta)\, e^{i\mu\theta} e^{i\nu\varphi}$ are the two
local one-dimensional channel oscillations of a bound vortex pair, and the
forced $-\tfrac{1}{2}$ is the zero-point offset of the interpolating
channel ladder.
