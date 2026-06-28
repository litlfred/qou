The bandwidth bound has an information-theoretic reading in terms of destructive interference and the per-Planck-step information budget.

## Interpretation

The class $\mathrm{P}$ consists of those
computations whose resolution trees admit sufficient destructive
interference — enough cancellation among the $3^c$ Skein
histories — that the Markov trace compresses the tree to
$O(\mathrm{poly}(c))$ surviving terms.  In each Planck step,
the $q$-connection $\nabla_q$ processes $n_R(q) = 1/\hbar_q$
iterations ([Reeb operations](#prop:reeb-operations-per-planck)),
each generating $\eta_q$ $q$-bits of entropy
([operational entropy](#def:operational-entropy)).  The total
information budget after $t$ Planck steps is

$$
  I(t) =  t \cdot \mathfrak{B}(q)
  =  t \cdot \frac{q\eta_q}{(q-1)^2}
  q\text{-bits.}
$$

A P-class computation is one where $I(\mathrm{poly}(c))$
suffices to determine $P_L(q_0)$.  The resolution tree has
$3^c$ leaves carrying $c \cdot \log 3$ $q$-bits of raw information,
but destructive interference reduces the effective information
content to $O(\mathrm{poly}(c) \cdot \log 3)$ $q$-bits — within
the polynomial bandwidth budget.
