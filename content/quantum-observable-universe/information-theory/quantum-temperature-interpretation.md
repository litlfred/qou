Classical statistical mechanics defines temperature implicitly through the Boltzmann distribution $\rho \propto e^{-\beta H}$. Here $\beta = 1/(k_B T)$ is a Lagrange multiplier enforcing energy conservation. In the QOU, $\beta_q$ holds direct operational meaning. It is the number of discrete Reeb operations (Julia set iterations $f_q$ on the exceptional divisor) that compose one macroscopic time unit. Temperature is not a statistical average over kinetic energies. It is the tick rate of the quantum substrate.

**Surface character of temperature.**
The entropy $S_q(U)$ is defined as a surface integral over $\partial U$, rather than a bulk integral over $U$. This structure follows from two ingredients.

First, the non-abelian Stokes theorem ([Yekutieli triple](#def:yekutieli-triple)) converts the bulk curvature integral to a boundary holonomy. The flatness conditions ($c_1 = 0$, $c_2 = 0$) render the boundary integral independent of the choice of bounding surface. The entropy is entirely a boundary datum.

Second, the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)) is non-degenerate. Internal degrees of freedom are fully determined by boundary data via the categorical trace. This encodes the content-object version of the holographic principle. The boundary $\partial U$—not the bulk $U$—controls the number of distinguishable states in $U$.

Temperature is the derivative of entropy with respect to energy. It strictly inherits this boundary character.

**Classical limit.**
As $q \to 1$, we find $T_q \to 0$, $\beta_q \to \infty$, and $S_q(U) \to S_{\mathrm{classical}}(U)$. The non-abelian Stokes integral degenerates to the classical Gauss law. The Frobenius trace becomes the ordinary matrix trace. The Boltzmann constant emerges as $k_B = \hbar_q / T_{\mathrm{phys}}$ in the correspondence limit, where physical temperature $T_{\mathrm{phys}}$ is measured in SI units.
