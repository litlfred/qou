Comparison between three-body and four-body nuclear binding energies is governed empirically by the triton–$\alpha$ correlation known in few-body physics as the *Tjon line*. Separating what external effective-field-theory theorems establish from finite-simplex inclusion–exclusion identities prevents conflating renormalisation-group universality with vanishing of a combinatorial four-simplex moment.

## External few-body results

Two results from short-range effective field theory frame the comparison:

1. **Leading-order three-body renormalisation of the four-nucleon system.** In pionless short-range effective field theory with two-body scattering length $|a| \gg \ell$ much larger than the interaction range $\ell$, Platter, Hammer, and Meißner show that a single $\mathrm{SU}(4)$-symmetric three-nucleon contact parameter suffices to renormalise the four-nucleon ground state at leading order in $\ell/|a|$, sweeping out the empirical triton–$\alpha$ trajectory \cite{platter2005tjon}. Anchoring on $B(^2\mathrm{H}) = 2.22\;\mathrm{MeV}$ and $B(^3\mathrm{H}) = 8.48\;\mathrm{MeV}$ yields $B(^4\mathrm{He}) \approx 29.5\;\mathrm{MeV}$ against the Coulomb-adjusted experimental value $29.0 \pm 0.1\;\mathrm{MeV}$.
2. **Zero-range four-to-three Yakubovsky ratio.** Solving the four-boson Yakubovsky equations in the strict zero-range limit without a four-body contact term, Hammer and Platter find that away from threshold the deepest four-body and three-body bound states satisfy $B_4 / B_3 \approx 5$ \cite{hammer2007fourbody}.

## Scope boundaries of the external theorems

Three distinctions delimit what those results imply:

1. **Renormalisability versus vanishing of four-body cumulants.** Leading-order renormalisation without an independent four-body counterterm does not imply vanishing of induced four-nucleon interactions: similarity-renormalisation-group evolution generates net four-nucleon contributions at $^4\mathrm{He}$ of tens to hundreds of keV \cite{jurgenson2009srg}.
2. **Short-range repulsion in the nuclear sector.** Sensitivity of four-body ground states to a four-body subtraction constant in general bosonic potentials (noted in \cite{hammer2007fourbody}) is suppressed in $^4\mathrm{He}$ by short-range repulsive cores that limit simultaneous four-body overlap.
3. **Finite-range shift from the zero-range ratio.** Experimental nuclear binding from AME2020 \cite{ame2020} gives a Coulomb-corrected ratio $B(^4\mathrm{He}) / B(^3\mathrm{H}) \approx 3.42$, substantially below the zero-range ratio $5$ because nuclear interactions have non-negligible effective range \cite{platter2005tjon}.

## Algebraic inequivalence with the $\mu_4 = 0$ simplex baseline

Expanding a few-body binding moment $M(A)$ ($2 \le A \le 4$) in the binomial simplex basis
$$
  M(A) \;=\; \sum_{k=2}^{4} \mu_k \binom{A}{k}
$$
identifies the three-point system at $A = 2, 3, 4$ invertibly with
$$
  \mu_2 \;=\; M(2),
  \qquad
  \mu_3 \;=\; M(3) - 3\,M(2),
  \qquad
  \mu_4 \;:=\; M(4) - 4\,M(3) + 6\,M(2).
$$
Over any linearly ordered commutative ring, imposing the truncated baseline $\mu_4 = 0$ ($M(4) = 4\,M(3) - 6\,\mu_2$) with $\mu_2 > 0$ forces the strict upper bound
$$
  M(4) \;<\; 4\,M(3),
$$
with exact deficit $M(4) - 4\,M(3) = -6\,\mu_2 < 0$. Consequently, the zero-range four-body ratio $M(4) = 5\,M(3)$ (obtained in \cite{hammer2007fourbody} with zero four-body input) lies strictly outside the $\mu_4 = 0$ simplex locus and instead forces
$$
  \mu_4 \;=\; 9\,\mu_2 + \mu_3.
$$
A non-zero binomial difference $\mu_4 = M(4) - 4\,M(3) + 6\,M(2)$ therefore measures departure of $M(4)$ from the two-body/three-body affine extrapolation on $K_4$ rather than an independent fitted four-body contact constant; in the simplicial functional of [Step 9b](#alg:per-isotope-binding) and [the $\Delta_\lambda$ structural sidecar](#alg:delta-lambda-closure), the tetrahedral weight $w_4 < 0$ is fixed directly by the parameter-free GPMT four-row cumulant on $H_4(q)$.
