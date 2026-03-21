
Since $\tau_n$ is an idempotent $*$-endomorphism of a $C^*$-algebra, the
splitting $\mathrm{im}\,\tau_n \oplus \ker\,\tau_n$ is an orthogonal direct
sum.

For item (1), let $\alpha \in \Gamma(J^1 E_{n+1})$ be a bosonic mode lifted
from level $n$: $[F_A, \alpha] = 0$ ([Remark](#rem:algebraic-filter)).
Bosonic modes take values in the Cartan subalgebra
$\mathrm{U}(1) \subset \mathfrak{su}(2)$
([Remark](#rem:weight-space-decomposition)).  Since $\alpha$ lies in the
image of the ascent $\ell_n$, we have $\alpha = \ell_n(\beta)$ for some
$\beta \in \Gamma(J^1 E_n)$.  Then
$\tau_n(\alpha) = \ell_n(\mathfrak{d}_{n+1}(\ell_n(\beta)))
= \ell_n(\beta) = \alpha$,
using $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$.  Hence
$\alpha \in \mathcal{A}_{n+1}^{\mathrm{desc}}$.

For item (2), the ladder modes $\omega^\pm \otimes E_\pm$ at level $n{+}1$
couple to the curvature $F_A$ through the covariant derivative $d_A$.  Those
that arise as lifts of level-$n$ modes lie in
$\mathcal{A}_{n+1}^{\mathrm{desc}}$ by the same argument as item (1).  The
remaining modes---genuinely new harmonic directions in $J^1 E_{n+1}$ with no
counterpart at level $n$---lie in $\mathcal{A}_{n+1}^{\mathrm{trans}}$ and
are annihilated by $\tau_n$: the descent $\mathfrak{d}_{n+1}$ maps them to
zero in the level-$n$ algebra, so $\tau_n = \ell_n \circ \mathfrak{d}_{n+1}$
sends them to zero.
