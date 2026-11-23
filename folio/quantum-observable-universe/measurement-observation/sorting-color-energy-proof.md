*Proof.*
Sorting deposits energy because a disordered pair sits in the
antisymmetric eigenspace at eigenvalue $-q^{-1}$, and sorting lifts
it to the symmetric eigenspace at eigenvalue $q$; the exchange must
therefore pay the gap between the two.  This is made precise by
computing the projections onto each eigenspace.

(1) The Hecke relation $\sigma_i^2 - (q - q^{-1})\sigma_i - 1 = 0$
has roots $q$ and $-q^{-1}$ by the quadratic formula.  The
corresponding idempotents are:

$$
  e_+ = \frac{\sigma_i + q^{-1}}{q + q^{-1}}, \qquad
  e_- = \frac{q - \sigma_i}{q + q^{-1}}
$$

with $e_+ + e_- = 1$ and $e_+ e_- = 0$.  The image of $e_+$
is $\mathrm{Sym}^2(V)$ (the symmetric representation,
eigenvalue $q$); the image of $e_-$ is $\bigwedge^2(V)$
(the antisymmetric representation, eigenvalue $-q^{-1}$).

(2) A disordered pair occupies $\bigwedge^2(V)$: the two
items are in the wrong order, so the state is antisymmetric
under exchange.  Sorting swaps them into the correct order,
moving the state to $\mathrm{Sym}^2(V)$.  This is the
projection $e_+$.  In the observation
([observation](#def:observation)), $e_+$ is the
$\mathrm{Ad}$ component: it acts on the colour fibre by
conjugation, rotating the antisymmetric state to the
symmetric eigenspace.

(3) The energy deposited is the eigenvalue difference:
$q - (-q^{-1}) = q + q^{-1}$.

(4) Each adjacent transposition in the sorting algorithm
corresponds to one braid crossing $\sigma_i$.  The standard
result from combinatorics: the minimum number of adjacent
transpositions to realise $\pi$ equals $\mathrm{inv}(\pi)$,
the number of pairs $(i, j)$ with $i < j$ and
$\pi(i) > \pi(j)$.  Each crossing deposits
$q + q^{-1}$ in the colour fibre.  $\square$

**Example: three socks.**

See [Table](#tbl:sorting-color-energy-table-data).

At $q = q_0$: sorting three fully reversed socks costs
$3 \times 2.011 = 6.033$ action units in the colour fibre.
