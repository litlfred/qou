# Numerical probe: LP target fits and vertex values

**Target:** `prop:confinement-lp`

We previously claimed the confinement linear program requires numeric target mass values ($n_{\mathrm{target}} \approx 1.000$ for the proton, $\approx 0.811$ for the neutron) curve-fit to the proton-neutron mass ratio. We stated the optimal vertex evaluates to $x^* = (+0.998, -0.010, +0.009, +0.046, -0.044, 0)$ at a fitted parameter $q_0 \approx 1.1100$, yielding an eigenvalue of $\approx -0.956$.

These claims represent overfitting via arbitrary float64 selection. Numeric curve fitting breaks formal rigor. The framework relies strictly on algebraic and categorical structures (e.g., Markov trace, Gram matrix positivity).

We remove these explicit numeric values and curve-fitting dependencies from `prop:confinement-lp`. We treat the target mass constraint as an abstract invariant net demand, untethered from fitted constants or $q_0 \approx 1.1100$. We present the algebraic topological conclusions (e.g., negative eigenvalues, Borromean solution) formally without numerical evaluations.
