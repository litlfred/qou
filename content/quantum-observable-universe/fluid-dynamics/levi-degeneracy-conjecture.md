Let $\{q_\kappa\}_{\kappa \geq 2}$ be roots of unity converging to $q = 1$. Let $\mathcal{C}_L(\kappa)$ be the maximum Levi form condition number over the evolution of an anti-parallel vortex pair, and let

$$
  \beta
  =
  \limsup_{\kappa \to \infty}
  \frac{\log \mathcal{C}_L(\kappa)}{\log \kappa}
  \in [0, 1]
$$

be its growth exponent (the bounded-rate regime, in which $\mathcal{C}_L$ grows no faster than linearly).

**Conjecture (Levi degeneracy).**
Exactly one of the following three regimes holds:

**(A) $\beta = 0$: bounded growth, $\mathcal{C}_L(\kappa) = O(1)$ (NS blows up).** The condition number stays bounded. The Levi form remains non-degenerate at the collision locus. The observability axiom holds locally. Classical 3d Navier--Stokes admits finite-time blowup.

**(B) $\beta = 1$: linear growth, $\mathcal{C}_L(\kappa) \sim \kappa$ (NS is regular).** The Levi form degenerates in the $\parallel$ direction. The contact structure becomes partially integrable. The observability axiom fails locally. The vortex core flattens into a sheet. Classical 3d Navier--Stokes is globally regular.

**(C) $0 < \beta < 1$: marginal growth, $\mathcal{C}_L(\kappa) \sim \kappa^\beta$ (undetermined).** The core neither stays uniformly discrete nor flattens completely. Neither branch (A) nor branch (B) is triggered, and the regularity verdict is open.

The three regimes are mutually exclusive and, on the bounded-rate interval $\beta \in [0, 1]$, exhaustive; a two-way alternative between (A) and (B) alone would omit the marginal window (C). The framework argues for branch (A), but the value of $\beta$ — hence which regime obtains — is not established here; it is the open computation the conjecture names. See [`prop:core-levi-form`](#prop:core-levi-form) for the equivalence tying $\mathcal{C}_L$ to the core aspect ratio.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
