**Conjecture (Whipple–rotation intertwining).**
*The archimedean shadow of the fibre-level channel rotation
$(x, q) \mapsto (ix, q^{-1})$ acts on the toroidal channel family
$P^{\mu}_{\nu - 1/2}(\cosh\eta)\, e^{i\mu\theta} e^{i\nu\varphi}$ as the
Whipple degree–order exchange: it swaps the two winding gradings
$(\mu, \nu) \mapsto (\nu, \mu)$ and is involutive on the ladder data.*

## What is established and what is open

The following supporting facts are verified (witness
`computations/substrate/whipple-rotation-involution-probe.witness.json`):

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
  $C(\nu, \mu+1)/C(\nu,\mu) = 1/(\nu+\mu+\tfrac12)$ and
  $C(\nu+1, \mu)/C(\nu,\mu) = -1/(\nu+\mu+\tfrac12)$ carry a single
  $\Gamma(\nu+\mu+\tfrac12)$ with an alternating $\nu$-sign
  \cite{whipple1917};
- the order $\mu = \tfrac12$ and the half-integer degree are forced by the
  Hoefsmit mixing structure
  ([prop:hoefsmit-toroidal-ladder-locus](../braids-and-knots/hoefsmit-toroidal-ladder-locus.md)).

**Open** is the identification itself: that the channel rotation of the
Ismail–Masson pair \cite{ismail-masson1994} — the map carrying the bar-even
recurrence to the bar-odd one — descends to the toroidal family *as* the
Whipple exchange, i.e. that the two winding oscillations of a bound vortex
pair are swapped by the substrate bar involution. The Lean sibling
axiomatises exactly this as a primary conjecture class
(`WhippleRotationIntertwining`): the rotation swaps the two winding
gradings and is involutive on ladder data. Both fields are
parameter-quantified in the shape of the claim; no instance is provided
(the conjecture is open).
