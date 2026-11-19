# Numerical probe: LP target fits and vertex values

**Target:** the confinement linear-program proposition.

A naive numerical formulation of the confinement linear program prescribes explicit target mass values ($n_{\mathrm{target}} \approx 1.000$ for the proton, $\approx 0.811$ for the neutron) curve-fit to the proton-neutron mass ratio, evaluating the optimal vertex to $x^* = (+0.998, -0.010, +0.009, +0.046, -0.044, 0)$ at a fitted parameter $q_0 \approx 1.1100$ with eigenvalue $\approx -0.956$.

These claims represent overfitting via arbitrary float64 selection. Numeric curve fitting breaks formal rigor. The framework relies strictly on algebraic and categorical structures (e.g., Markov trace, Gram matrix positivity).

Explicit numeric values and curve-fitting dependencies are therefore excluded from the confinement linear-program proposition. The target mass constraint enters instead as an abstract invariant net demand, untethered from fitted constants or $q_0 \approx 1.1100$, and the algebraic topological conclusions (negative eigenvalues and the Borromean solution) hold formally without numerical evaluations.
