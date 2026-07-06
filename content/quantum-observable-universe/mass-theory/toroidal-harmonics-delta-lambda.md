# A toroidal-harmonic change of variables for the $z$-recursion

**Proposition.** *Let $x = \tfrac{1}{2w} - 1$. Under this change of
variables the half-integer-degree ($n-\tfrac12$) toroidal Legendre
equation*

$$ (1 - x^2)\,y'' - 2x\,y' + \left(n^2 - \tfrac14\right) y = 0 $$

*transforms, after clearing denominators, into the second-order
$w$-equation*

$$ (16w^3 - 4w^2)\,f'' + 16w^2\,f' + (4n^2 - 1)\,f = 0, \qquad y = f\circ w. $$

*The identity is exact (verified symbolically in
[`toroidal_harmonics.py`](#), `derive_bridge`).*

## Scope

The variable is $w = z^2$ with $z = \tfrac{\sqrt q}{1+q}$ the Markov
parameter and $q = e^{-\eta}$, $x = \cosh\eta$. The proposition is a
statement about **operators**: it places the $w$-form of the toroidal
Legendre operator on record.

It does **not** establish the following, which remain open:

- **The $w$-ODE is not yet identified with the proved $z$-recursion.**
  The pre-archimedean Markov recursion
  $4(n+1)a_{n+1} + 6n\,a_n + (2n-1)a_{n-1} = 0$
  ([`lem:interface-knot-markov-z`](#)) is written in the variable
  $w = q-1$ — a *different* $w$ from the $w = z^2$ here. Matching the two
  is part of the open $z \to c_k$ **f-map**; it is asserted, not proved.
- **No $c_k$ is made exact by this map.** In particular $c_3$ is
  cal-anchored and swings $\approx 2.375\%$ between the proton and muon
  substrate anchors; only $c_2 = -1$ is Taylor-exact
  (see the cross-anchor verdict audit).
- **The $\Delta_\lambda$ mass gap is not resolved here.** Evaluating a
  toroidal-harmonic ratio $P_{n-1/2}^m$ against the shell-filling fraction
  $c_\lambda$ is a separate, and currently **negative**, investigation:
  the $c_\lambda$ used empirically is defined circularly as
  $B_{\mathrm{AME}}/E_{\mathrm{gate}}$, and no parameter-free toroidal
  anchor reproduces it (the closest "pretty" constant, the golden ratio,
  is $\approx 0.12\%$ off, and the value that does reproduce $c_\lambda$ is
  $q_0 \approx 0.615$ — neither the golden ratio nor the substrate
  $q_0 \approx 1.10998$). That scan is recorded as a negative audit in
  `toroidal_harmonics.py::evaluate_c_lambda`, not as paper content, and
  does not meet the three-calibration discipline or the $\Delta_\lambda$
  gate.
