*Let $\mathrm{tr}_M$ be any Markov trace on $H_3(q)$, expanded in the Wedderburn basis
as $y_{(3)}\chi^{(3)} + y_{(2,1)}\chi^{(2,1)} + y_{(1^3)}\chi^{(1^3)}$ and normalised
by $\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(\sigma) = z$. Then the two isospin scalars
are sums over the $H_2(q) \subset H_3(q)$ branching,*

$$
  \mu_+ \;=\; y_{(3)} + y_{(2,1)},
  \qquad
  \mu_- \;=\; y_{(2,1)} + y_{(1^3)},
$$

*identically in $z$ and in $q$. Under convention D, where $y_{(1^3)} = 0$, the singlet
weight is therefore $\mu_- = y_{(2,1)}$ exactly.*

## Origin of the two character sums

Restriction along $H_2(q) \subset H_3(q)$ branches each Young diagram of $3$ into the
diagrams of $2$ obtained by removing a box. The totally symmetric shape $(3)$
restricts entirely to the symmetric shape $(2)$; the totally antisymmetric shape
$(1^3)$ restricts entirely to $(1^2)$; and the mixed shape $(2,1)$, being
two-dimensional, reaches both. Reading the Bratteli diagram off in that order gives
exactly the two displayed sums, with $y_{(2,1)}$ appearing on each side for the plain
reason that $\dim(2,1) = 2$.

The two normalisations are all that is needed to prove them. Writing out
$\mathrm{tr}_M(1) = 1$ and $\mathrm{tr}_M(\sigma) = z$ against the character values
$\chi(1) = (1,2,1)$ and $\chi(\sigma) = (q,\, q-q^{-1},\, -q^{-1})$, the combination
$-\mathrm{tr}_M(\sigma) - q^{-1}\mathrm{tr}_M(1)$ cancels $y_{(1^3)}$ and yields
$z + q^{-1} = (q+q^{-1})(y_{(3)} + y_{(2,1)})$, while
$\mathrm{tr}_M(\sigma) - q\,\mathrm{tr}_M(1)$ cancels $y_{(3)}$ and yields
$q - z = (q+q^{-1})(y_{(2,1)} + y_{(1^3)})$. No convention is chosen, no value of $q$
is fixed, and no fit enters; both are instances of
[the three-term branching recursion](#prop:markov-branching-three-term).

A corollary of the same reading is that $\mu_+ + \mu_- = 1$ carries no information
about isospin. On the $\mu$ side the sum is vacuous --- the $z$ cancels with no
hypotheses at all --- and on the branch side it is
$y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = \mathrm{tr}_M(1) = 1$, the normalisation restated.
Any Markov trace whatever satisfies it.

## The radical is observationally inert

Under convention D the antisymmetric weight vanishes identically, so the second sum
collapses to a single term and the isospin singlet draws its entire weight from the
mixed-symmetry block. Quotienting $H_3(q)$ by its radical deletes a summand that was
already contributing zero. More generally a term with $y_\lambda = 0$ can be removed
from $\sum_\lambda y_\lambda \chi^\lambda$ without changing any value, so the radical
is invisible to every trace and hence to every observable the framework computes from
one.

That is what makes the repair demanded by
[the degeneracy obstruction](#prop:gram-degeneracy-blocks-connes) free. The
obstruction is real --- a degenerate form gives the Lipschitz seminorm a kernel and
the Connes distance is unbounded --- and the quotient that removes it costs no
physics.

## The isospin weights are the two-strand weights

One further identification falls out of the same branching. Under convention D the
two isospin scalars are the Wedderburn weights of $H_2(q)$ itself,

$$
  \mu_+ \;=\; y_{(2)}\bigl[H_2\bigr],
  \qquad
  \mu_- \;=\; y_{(1,1)}\bigl[H_2\bigr],
$$

and the two numbers the nucleon-pair sector runs on are therefore not new data
attached to $H_3(q)$ but the weights of the two-strand algebra seen one level up.
This is the edge that fixes where the Temperley--Lieb characterisation belongs: it is a statement
about the tower, and it is developed with the algebra rather than with the physics
that consumes it.

At $q_0$ the three
descriptions of the singlet weight agree to every digit carried:
$\mu_- = (q_0-z)/(q_0+q_0^{-1})$, $y_{(2,1)} = 1/[2]_{q_0}^{2}$, and the product
$\mu_{pp}\,\mu_{nn} = 1/(q_0+q_0^{-1})^{2}$ all evaluate to
$0.24729788674803459841$.
