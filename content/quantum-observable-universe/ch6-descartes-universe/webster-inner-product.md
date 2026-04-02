We denote the inner product induced by the Webster metric $g_\theta$
on the horizontal distribution $H = \ker\theta$ and its exterior
powers as $\langle \cdot, \cdot \rangle_\theta$. For vector fields
$X, Y$ and differential forms $\alpha, \beta$:

$$
  \langle X, Y \rangle_\theta := g_\theta(X, Y),
  \qquad
  \langle \alpha, \beta \rangle_\theta := g_\theta(\alpha^{\sharp}, \beta^{\sharp}).

$$

This notation makes several dualities visually transparent:

- **Reeb duality.** The Reeb vector field $\xi$ is the metric dual
  to the contact form $\theta$:
  $\theta(X) = \langle \xi, X \rangle_\theta$ for all $X$.

- **Adjoint definition.** The $q$-codifferential $\delta_q$ is
  uniquely characterised by
  $\langle d_q\,\alpha, \beta \rangle_\theta =
  \langle \alpha, \delta_q\,\beta \rangle_\theta$.

- **Substrate contraction.** The natural contraction
  $\langle L_\theta, F_A^+ \rangle$ appearing in the substrate
  parameter ([substrate parameter](#def:substrate-parameter)) is
  exactly the inner product $\langle \cdot, \cdot \rangle_\theta$
  extended to bundle-valued $2$-forms.
