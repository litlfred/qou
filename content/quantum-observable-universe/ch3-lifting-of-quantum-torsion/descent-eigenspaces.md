The descent involution $\tau_n$ ([Definition](#def:descent-involution))
decomposes the level-$(n{+}1)$ endomorphism algebra into a direct sum
$$
  \mathrm{End}_{\mathcal{C}}(A_{n+1})
  \;=\;
  \mathcal{A}_{n+1}^{\mathrm{desc}} \;\oplus\; \mathcal{A}_{n+1}^{\mathrm{trans}},
$$
where $\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\,\tau_n$ is the
descended subalgebra (endomorphisms that factor through level $n$) and
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\,\tau_n$ is the *transient
complement* (genuinely new endomorphisms at level $n{+}1$).  The algebraic filter
([Remark](#rem:algebraic-filter)) refines this decomposition:

1. The bosonic (longitudinal) modes lifted from level $n$ lie entirely in
   $\mathcal{A}_{n+1}^{\mathrm{desc}}$: they commute with the curvature
   and survive every round-trip through the tower.
2. The fermionic (ladder) modes at level $n{+}1$ split between the two
   summands; those in $\mathcal{A}_{n+1}^{\mathrm{trans}}$ are the modes
   created by the jet prolongation that have no pre-image at level $n$.

---

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
