Interactive visualization of the valley of stability as a
Diophantine approximation problem.

**Controls:**
- **$q$ slider**: Varies the substrate parameter from $1.0$
  (classical, no Coulomb) to $2.0$ (deep quantum).
  Default: $q = 1.1097$.
- **View**: Toggle between $(p, n)$-plane and $(A, n/p)$-plane.

**Display:**
- **Blue curve**: Continuous beta-stability line
  $p^*(A) = A/(2 + cA^{2/3})$ from the Skein binding Lagrangian.
- **Green dots**: Integer lattice points $(p_{\mathrm{stab}}, n_{\mathrm{stab}})$
  — the observed stable isotopes.
- **Red segments**: Diophantine error $\varepsilon(A)$ —
  vertical distance from each lattice point to the curve.
- **Gold diamonds**: Stability pairs (shell closures).
- **Shaded band**: Valley width — the range of $p$ values within
  one beta-decay half-life of the stable isotope.

As $q \to 1$, the curve straightens to $p = A/2$ (the diagonal),
all lattice points fall on the curve, and the Diophantine problem
becomes trivial.  As $q$ increases, the curve bends, the lattice
points scatter, and the stability-pair structure emerges.
