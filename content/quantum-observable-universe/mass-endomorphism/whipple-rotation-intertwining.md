**Conjecture (Whipple–rotation intertwining).**
*The archimedean shadow of the fibre-level channel rotation
$(x, q) \mapsto (ix, q^{-1})$ acts on the toroidal channel family
$P^{\mu}_{\nu - 1/2}(\cosh\eta)\, e^{i\mu\theta} e^{i\nu\varphi}$ as the
Whipple degree–order exchange: it swaps the two winding gradings
$(\mu, \nu) \mapsto (\nu, \mu)$ and is involutive on the ladder data.*

## Established results and open questions

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
- the constant's full Gamma structure is a symbolic-exact structural
  identity, grid-verified (not one-point): solving the two shift
  recurrences forces
  $C(\nu,\mu) = \sqrt{2/\pi}\;e^{-i\pi\nu}/\Gamma(\nu+\mu+\tfrac12)$,
  which matches the direct $60$-digit compute to $\sim 10^{-40}$ across a
  grid of generic non-integer, non-half-integer $(\nu,\mu)$ points (witness
  `computations/substrate/whipple-gamma-constant-gridverify.witness.json`);
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

Two consequences are *derived from* the class (provable modulo it, no
instance):

- `nuGrade_square` — the along-loop winding is restored after a double
  rotation, so the winding pair $(\mu, \nu)$ is fixed by $\mathrm{rot}^2$
  (the categorical shadow of the exact $\cosh\eta \leftrightarrow \coth\eta$
  involution);
- `gradingPair_intertwines_swap` — the winding-grading map
  $x \mapsto (\mu(x), \nu(x))$ intertwines the channel rotation with the
  coordinate swap: $(\mu(\mathrm{rot}\,x), \nu(\mathrm{rot}\,x)) =
  \mathrm{swap}(\mu(x), \nu(x))$. This is the exact discrete shadow of the
  Whipple degree–order exchange $(\mu, \nu) \mapsto (\nu, \mu)$, and a
  genuine consequence of the two swap-component fields (not a restatement).

The archimedean *amplitude* of that exchange is fixed independently of the
open identification: the grid-verified constant
$C(\nu,\mu) = \sqrt{2/\pi}\,e^{-i\pi\nu}/\Gamma(\nu+\mu+\tfrac{1}{2})$ above is
the symbolic-exact shadow the intertwining must carry.
