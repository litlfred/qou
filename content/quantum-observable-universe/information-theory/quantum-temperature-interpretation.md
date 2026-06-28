In classical statistical mechanics, temperature is defined
implicitly through the Boltzmann distribution
$\rho \propto e^{-\beta H}$, where $\beta = 1/(k_B T)$ is
a Lagrange multiplier enforcing energy conservation.  In the
QOU, $\beta_q$ has a direct operational meaning: it is the
**number of discrete Reeb operations** (Julia set iterations
$f_q$ on the exceptional divisor) that compose one macroscopic
time unit.  Temperature is not a statistical average over
kinetic energies — it is the **tick rate** of the quantum
substrate.

**Surface character of temperature.**
The entropy $S_q(U)$ is defined as a surface integral over
$\partial U$, not a bulk integral over $U$.  This follows
from two ingredients:

1. The non-abelian Stokes theorem
   ([Yekutieli triple](#def:yekutieli-triple)) converts the
   bulk curvature integral to a boundary holonomy.  The
   flatness conditions ($c_1 = 0$, $c_2 = 0$) make the
   boundary integral independent of the choice of bounding
   surface — the entropy is a **boundary datum**.

2. The Frobenius pairing
   ([Frobenius pairing](#def:frobenius-pairing)) is
   non-degenerate, so internal degrees of freedom are
   fully determined by boundary data via the categorical
   trace.  This is the content-object version of the
   holographic principle: the number of distinguishable
   states in $U$ is controlled by $\partial U$, not by
   $U$ itself.

Temperature, as the derivative of entropy with respect to
energy, inherits this boundary character.

**Classical limit.**
As $q \to 1$: $T_q \to 0$, $\beta_q \to \infty$, and
$S_q(U) \to S_{\mathrm{classical}}(U)$.  The non-abelian
Stokes integral degenerates to the classical Gauss law,
and the Frobenius trace becomes the ordinary matrix trace.
The Boltzmann constant emerges as
$k_B = \hbar_q / T_{\mathrm{phys}}$ in the correspondence
limit where physical temperature $T_{\mathrm{phys}}$ is
measured in SI units.
