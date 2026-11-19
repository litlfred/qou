**Conjecture (Whipple–rotation intertwining).**
*The archimedean shadow of the fibre-level channel rotation
$(x, q) \mapsto (ix, q^{-1})$ acts on the toroidal channel family
$P^{\mu}_{\nu - 1/2}(\cosh\eta)\, e^{i\mu\theta} e^{i\nu\varphi}$ as the
Whipple degree–order exchange: it swaps the two winding gradings
$(\mu, \nu) \mapsto (\nu, \mu)$ and is involutive on the ladder data.*

## Established results and open questions

The following supporting facts are verified:

- the interpolating ladder is bar-even, $[d]_{q^{-1}} = [d]_q$ (exact);
- the Whipple argument exchange $\cosh\eta \leftrightarrow \coth\eta$ is an
  exact involution, and the $\zeta_4$ quarter-period shift
  $\cosh(t + i\pi/2) = i\sinh t$ maps the bar-even to the bar-odd channel;
- numerically at 50 digits, the toroidal pair obeys

$$
P^{-\mu}_{\nu-1/2}(\coth a)
= C(\nu, \mu)\, \sqrt{\sinh a}\;\, Q^{\nu}_{\mu-1/2}(\cosh a),
$$

  with $a$-independent $C$ whose shift laws
  $C(\nu, \mu+1)/C(\nu,\mu) = 1/(\nu+\mu+\tfrac{1}{2})$ and
  $C(\nu+1, \mu)/C(\nu,\mu) = -1/(\nu+\mu+\tfrac{1}{2})$ carry a single
  $\Gamma(\nu+\mu+\tfrac{1}{2})$ with an alternating $\nu$-sign
  \cite{whipple1917};
- the constant's full Gamma structure is a symbolic-exact structural
  identity, grid-verified (not one-point): solving the two shift
  recurrences forces
  $C(\nu,\mu) = \sqrt{2/\pi}\;e^{-i\pi\nu}/\Gamma(\nu+\mu+\tfrac{1}{2})$,
  which matches the direct $60$-digit compute to $\sim 10^{-40}$ across a
  grid of generic non-integer, non-half-integer $(\nu,\mu)$ points;
- the order $\mu = \tfrac{1}{2}$ and the half-integer degree are forced by the
  Hoefsmit mixing structure
  ([prop:hoefsmit-toroidal-ladder-locus](../braids-and-knots/hoefsmit-toroidal-ladder-locus.md));
- the exchange holds *at the physical forced windings themselves*: at
  $(\mu, \nu) = (\tfrac{1}{2}, d - \tfrac{1}{2})$ for axial distances $d \in \{2, 3, 4\}$
  (the meson is $d = 2$) the same $\Gamma$-constant identity is exact to
  $\sim 10^{-50}$ — not only at the generic grid points, which deliberately
  avoided the $\mu = \tfrac{1}{2}$ order — and the order-ladder factor reproduces
  the mixing numerator $d^2 - 1$ at each $d$. This
  is numerical evidence for the modeling layer, not a proof.

**Open** is the identification itself: that the channel rotation of the
Ismail–Masson pair \cite{ismail-masson1994} — the map carrying the bar-even
recurrence to the bar-odd one — descends to the toroidal family *as* the
Whipple exchange, i.e. that the two winding oscillations of a bound vortex
pair are swapped by the substrate bar involution. This conjecture is formulated
as an explicit intertwining hypothesis: the rotation swaps the two winding
gradings and is involutive on ladder data. Both conditions are
parameter-quantified in the shape of the claim, and the conjecture remains open.

Two consequences follow directly from the intertwining hypothesis:

- **Along-loop winding restoration** — the along-loop winding is restored after a double
  rotation, so the winding pair $(\mu, \nu)$ is fixed by $\mathrm{rot}^2$
  (the categorical shadow of the exact $\cosh\eta \leftrightarrow \coth\eta$
  involution);
- **Winding-grading intertwining** — the winding-grading map
  $x \mapsto (\mu(x), \nu(x))$ intertwines the channel rotation with the
  coordinate swap: $(\mu(\mathrm{rot}\,x), \nu(\mathrm{rot}\,x)) =
  \mathrm{swap}(\mu(x), \nu(x))$. This is the exact discrete shadow of the
  Whipple degree–order exchange $(\mu, \nu) \mapsto (\nu, \mu)$, and a
  genuine consequence of the two swap-component conditions (not a restatement).

The archimedean *amplitude* of that exchange is fixed independently of the
open identification: the grid-verified constant
$C(\nu,\mu) = \sqrt{2/\pi}\,e^{-i\pi\nu}/\Gamma(\nu+\mu+\tfrac{1}{2})$ above is
the symbolic-exact shadow the intertwining must carry.

The grading-swap condition is moreover *not primitive*: it follows
from the even$\leftrightarrow$odd channel flip that
[the channel rotation](binding-qbeta-complex-volume.md)
establishes. A channel-indexed ladder carries the two
recurrence-channel indices, the rotation that flips them, and a single shared
winding function $\mathrm{windOf}$; the swap
$\mathrm{windOf}(\mathrm{evenIdx}(\mathrm{rot}\,x)) =
\mathrm{windOf}(\mathrm{oddIdx}\,x)$ then follows from the flip, not from an
assumption. This does not close the conjecture: it
moves the open content off the swap and onto (i) identifying the abstract
channel flip with the odd-step $\leftrightarrow$
even-step recurrence rotation, and (ii) the residual involutivity — the order-2
Whipple $\cosh\eta \leftrightarrow \coth\eta$ exchange, a *different* map from
the order-4 $\zeta_4$ recurrence rotation, hence genuinely open.
