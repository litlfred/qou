The brane-tower regularization of the Habiro series
([conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro)) requires a
canonical level-selection rule $n_\star : \{\text{confined particles}\} \to \mathbb{N}$
derivable from the QOU substrate data alone.  Currently $n_\star$ is
chosen empirically for each particle class.  This conjecture proposes
a structural formula for $n_\star$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom with confinement level
$\ell$ and strand count $n_0$.  Let $T_w \in H_{n_0}(q_0)$ be the
canonical Hecke element in GB normal form, and let $k = \ell(w)$ be
its Coxeter length (GB filtration grade).  Then the canonical
brane-tower truncation level is*

$$
  n_\star(\mathfrak{H}) \;=\; \ell \cdot n_0 + k,
$$

*where $\ell$ is the confinement level and $k$ is the GB filtration
grade of $T_w$.  Equivalently, $n_\star$ is the total number of
elementary crossing insertions in the finite-slice Yekutieli picture.*

## Evidence

- For the electron ($\ell = 0$, $n_0 = 2$, $k = 3$): $n_\star = 3$.
  This matches the $H_2(q)$ trefoil structure.
- For the proton/neutron ($\ell = 1$, $n_0 = 3$, $k = 3$): $n_\star = 6$.
  Matches the 6-dimensional $H_3(q)$ structure and the 6 GB-NF basis elements.
- For $^2$H ($\ell = 2$, $n_0 = 6$, $k \approx 5$): $n_\star = 17$.
  Consistent with the Habiro series truncation depth used in the witness.

## Relationship to GAP-A-3

This conjecture directly addresses GAP-A-3 of the
[derivation audit report](#prose:derivation-audit-report).
A proof would replace the empirical level-selection with a derived formula.
