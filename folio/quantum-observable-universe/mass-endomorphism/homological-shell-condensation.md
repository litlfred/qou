## Setup

Fix a level $n \in \mathbb{N}$ in the brane tower, with associated
:refterm[descent]{#descent}-graded jet algebra $A_n = A_{n-1} \otimes \Omega^1(A_{n-1})$
([def:direct-limit-algebra](#def:direct-limit-algebra)). The
Białynicki-Birula stratification of $\mathrm{Spec}(A_n)$ under the
$\mathbb{C}^\times$-action induced by the :refterm[descent]{#descent} involution
$\hat\tau$ \cite{bialynicki1973} produces a filtration

$$
  F^0 A_n \supset F^1 A_n \supset \cdots \supset F^p A_n \supset \cdots
$$

with associated graded $\mathrm{gr}_F A_n$. The Gröbner–Shirshov
spectral sequence
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence)) on this
filtration converges to the :refterm[descent]{#descent}-graded algebra:

$$
  E_1^{p,q} \;=\; H^q\bigl(\mathrm{gr}_F^p A_n\bigr)
  \;\Longrightarrow\;
  H^{p+q}\bigl(A_n\bigr).
$$

The strict-positive part $E_\infty^{p, >0}(n)$ measures the
non-trivial cohomology supported above the $E_2$-collapse line.
Operationally, it measures the obstruction to reading the :refterm[descent]{#descent}-graded trace
purely from the diagonal.

## Statement

**Proposition (Conjecture — homological shell condensation).**
*For every $n \in \mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$, the
Białynicki-Birula spectral sequence on $A_n$ collapses entirely above
the $E_2$ line:*

$$
  E_\infty^{p, q}(n) \;=\; 0
  \qquad\text{for all } p \in \mathbb{N}, \; q > 0,
  \quad n \in \mathfrak{M}.
$$

*Equivalently, the :refterm[descent]{#descent}-graded trace
$\mathrm{tr}_{M, \ell}$ on $J^\ell / J^{\ell+1}$
([prop:graded-trace-residue-split](#prop:graded-trace-residue-split))
is supported entirely on the diagonal at saturated $n$, and the
brane-tower :refterm[descent]{#descent} residues vanish for $\ell \geq 2$.*
