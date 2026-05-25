**Proof.**
In Feynman's formulation, the transition amplitude between initial state
$|\psi_i\rangle$ and final state $|\psi_f\rangle$ is

$$
  \langle\psi_f|\psi_i\rangle
  =
  \int \mathcal{D}\phi\,e^{iS[\phi]/\hbar},
$$

where the integral runs over all paths in configuration space.  Now
suppose that $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ admits
the complete eigenbasis from
([eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition)).
Then every path $\phi$ factors
through a unique irreducible summand $V_\lambda \otimes S_\lambda$,
and the continuum integral collapses to a finite weighted sum over
irreducible summands.

No regularisation is needed: the sum has finitely many terms because
$V^{\otimes n}$ has finitely many irreducible summands (semisimplicity
of $H_n(R, q)$ at non-root-of-unity $q$).  $\square$
