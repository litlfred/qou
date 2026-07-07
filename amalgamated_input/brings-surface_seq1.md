<!-- FILE_START: physical-regimes-intro.md -->
This section develops physical regimes and limiting context. The blocks below trace the construction from `brings-surface-unit-circle` onward.
<!-- FILE_END: physical-regimes-intro.md -->

<!-- FILE_START: brings-surface-unit-circle.md -->
Let $S$ denote Bring's surface (genus $4$, $\chi = -6$).  The CR geometry
lives on the unit circle bundle $M_S \subset T^*S$: the Liouville
$1$-form restricts to a contact form $\varTheta$ on $M_S$.  The natural
projection $\pi \colon S \to \mathbb{P}^1(\mathbb{C})$ (degree-$4$
branched covering with $6$ branch points) lifts to a principal
$\mathrm{SU}(2)$-bundle $P \to M_S$, giving an archimedean QOU
$(\mathbf{C}, \varTheta, G, \mathcal{S})$.
<!-- FILE_END: brings-surface-unit-circle.md -->

<!-- FILE_START: primordial-vortex.md -->
As $r\to 0$ the spectral resolvents converge toward the
*primordial vortex*:

- The quantum Planck constant
  $\hbar_q\to 1$ ([quantum planck constant](#def:quantum-planck-constant)).
- The $q$-torsion leaves
  ([$q$-torsion leaf](#ex:q-torsion-leaf)) collapse to the zero-dimensional
  stratum $M_0=\{\pm 1\}$.
- The $\omega_0$ coordinate, although identically zero in the
  balanced state, formally blows up in the jet prolongation, representing
  the concentration of energy at a singular spatial point.

Space-like energy is trapped because the time-like rotation becomes infinite
in frequency but zero in displacement, effectively turning the
$\mathrm{SU}(2)$ holonomy into a localised topological charge.
<!-- FILE_END: primordial-vortex.md -->

<!-- FILE_START: geometric-drag.md -->
The Levi form $L$ ([substrate parameter](#def:substrate-parameter)) must be
preserved under the $\mathrm{Sp}(1)$ conjugation.  Since

$$
  \lVert\boldsymbol{\omega}'\rVert^2
  =\lVert\boldsymbol{\omega}\rVert^2
  =\omega_1\bar{\omega}_1+\omega_2\bar{\omega}_2+\omega_3\bar{\omega}_3,
$$

the quadric constraint remains satisfied and
the horizontal self-duality $F_A|_H={*_H}F_A|_H$ is preserved.  The mass of a stable vortex is
recovered as the residue of the interaction between the growth profiles:

```tex
\begin{equation}\label{eq:mass-residue}
  m  \propto 
  \oint_{\varrho}
  \lVert\nabla_A q\rVert\cdot
  \lVert\Omega_1\wedge\Omega_{2,3}\rVert,
\end{equation}
```

where $\Omega_k$ denotes the curvature form restricted to the $\omega_k$
sector.  This heuristic is made rigorous by the nonabelian multiplicative
integral of the ([mass identity](#def:mass-identity)).
When $q=1$ (trivial bundle), the $\omega_k$ commute and $m=0$;
when $q\to 0$ (maximal twist), energy is trapped in the $\omega_1$ spatial
filament.
<!-- FILE_END: geometric-drag.md -->

