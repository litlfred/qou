For physicists the most recognisable resonance line-shape is the
**Breit--Wigner (Lorentzian)** distribution
$$
  L_\Gamma(E) \;=\; \frac{1}{\pi}\,\frac{\Gamma/2}{(E - E_0)^2 + (\Gamma/2)^2}.
$$
We show it arises as a *uniform scale-mixture* of the substrate
$q$-Gaussians $G_q(t,x)$
([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)),
so no new kinematics is required to talk about resonances in the QOU.

**Notation.**  To avoid a clash with the substrate parameter
$q_0$, write $q_{\mathrm T}$ for the **Tsallis index** — a *separate*
scalar that parameterises a one-parameter line-shape family below.

**One-parameter deformation family.**  Define
$$
  P_{q_{\mathrm T}}(E; E_0, \Gamma)
  \;\propto\;
  \bigl[\,1 + (q_{\mathrm T} - 1)(E - E_0)^2/\Gamma^2\,\bigr]^{1/(1 - q_{\mathrm T})},
  \qquad q_{\mathrm T} \in (1, 3).
$$
Direct calculation gives three regimes:

| $q_{\mathrm T}$ regime | Distribution | Physical use |
|---|---|---|
| $q_{\mathrm T} \to 1$ | Gaussian $\exp(-(E-E_0)^2/\Gamma^2)$ | thermal / diffusive |
| $q_{\mathrm T} = 2$ | Lorentzian = **Breit--Wigner** | resonance line-shape |
| $1 < q_{\mathrm T} < 2$ | heavy-tailed interpolant | intermediate averaging |

Thus $q_{\mathrm T} = 2$ *exactly* reproduces the textbook
Breit--Wigner resonance, and $q_{\mathrm T} \to 1$ recovers the
Gaussian.

**Derivation as a scale mixture.**  Every $P_{q_{\mathrm T}}$ with
$q_{\mathrm T} \in (1, 3)$ admits the representation
$$
  P_{q_{\mathrm T}}(E)
  \;=\;
  \int_0^\infty G_\sigma(E - E_0)\,
  \mu_{q_{\mathrm T}}(\mathrm{d}\sigma^2),
$$
where $G_\sigma$ is the ordinary Gaussian of variance $\sigma^2$ and
$\mu_{q_{\mathrm T}}$ is an inverse-Gamma measure with shape
$\alpha = \tfrac{1}{q_{\mathrm T} - 1} - \tfrac{1}{2}$.  At
$q_{\mathrm T} = 2$ this collapses to the classical identity
*"Lorentzian = inverse-Gamma scale mixture of Gaussians"*; at
$q_{\mathrm T} \to 1$ the measure concentrates on a single scale
and recovers the Gaussian.

**Physical content.**  The substrate $q$-Gaussian has Reeb-flow
scale $\sigma^2 = t/q^2$
([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)).
Integrating over this scale with the inverse-Gamma weight
$\mu_{q_{\mathrm T}}$ is exactly how a physicist would *average
over lifetimes of intermediate states* in a resonance calculation.
The resulting line-shape is Breit--Wigner **by construction**: no
new axioms, just the substrate heat-kernel plus a uniform scale
weight.  This is the recovery statement — the QOU does not
replace Breit--Wigner, it *derives* it from the $q$-Gaussian
family.

**Relationship to the substrate value.**  The substrate parameter
$q_0 \approx 1.11$ controls the Reeb-flow scale $\sigma^2 = t/q_0^2$
that is *integrated over*; it does not play the role of the Tsallis
index $q_{\mathrm T}$.  The QOU intrinsic single-scale distribution
is Gaussian ($q_{\mathrm T} \to 1$ limit), and a fully-averaged
observable line-shape is Lorentzian ($q_{\mathrm T} = 2$ endpoint);
real experiments see a Voigt-like interpolant, matching
$1 < q_{\mathrm T} < 2$.
