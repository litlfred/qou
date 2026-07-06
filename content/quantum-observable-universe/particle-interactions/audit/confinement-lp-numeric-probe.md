# Audit Probe: LP Numeric Target Fits and Vertex Values

**Target:** `prop:confinement-lp`

The model previously claimed that the confinement linear program uniquely relies on numeric target mass values ($n_{\mathrm{target}} \approx 1.000$ for the proton and $\approx 0.811$ for the neutron) which are ad-hoc curve fits to the proton and neutron mass ratio. Furthermore, the optimal vertex of the LP was stated to evaluate to specific coordinates $x^* = (+0.998, -0.010, +0.009, +0.046, -0.044, 0)$ evaluated specifically at a fitted parameter $q_0 \approx 1.1100$, with resulting evaluated eigenvalue of $\approx -0.956$.

**Divergence:**
These claims represent numerology and overfitting via arbitrary float64 value selection to align with physical constants. In a strict categorical derivation, numeric curve fitting breaks the formal rigor and independence from ad-hoc parameters. The framework relies purely on algebraic and categorical structures (e.g., Markov trace, Gram matrix positivity).

**Action Taken:**
These explicit numeric values, curve fitting parameters, and float64 dependencies have been removed from the core derivation `prop:confinement-lp` to maintain a rigorous categorical one-voice stance. The target mass constraint is now treated as abstractly requiring a given invariant net demand, without tying it to arbitrary fitted constants or $q_0 \approx 1.1100$. The algebraic topological conclusions (e.g., negative eigenvalues, Borromean solution) are presented formally without numerical evaluations.
