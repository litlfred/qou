Let $\langle \cdot, \cdot \rangle_\varTheta$ denote the inner product induced by the Webster metric $g_\varTheta$ on the horizontal distribution $H = \ker\varTheta$ and its exterior powers. For vector fields $X, Y$ and differential forms $\alpha, \beta$, we define:

$$
  \langle X, Y \rangle_\varTheta := g_\varTheta(X, Y),
  \qquad
  \langle \alpha, \beta \rangle_\varTheta := g_\varTheta(\alpha^{\sharp}, \beta^{\sharp}).
$$

This notation clarifies three dualities:

- **Reeb duality.** The Reeb vector field $\xi$ is the metric dual to the contact form $\varTheta$. For all $X$, $\varTheta(X) = \langle \xi, X \rangle_\varTheta$.

- **Adjoint definition.** The $q$-codifferential $\delta_q$ is uniquely characterised by $\langle d_q\alpha, \beta \rangle_\varTheta = \langle \alpha, \delta_q\beta \rangle_\varTheta$.

- **Substrate contraction.** The natural contraction $\langle L_\varTheta, F_A^+ \rangle$ in the [substrate parameter](#def:substrate-parameter) is the inner product $\langle \cdot, \cdot \rangle_\varTheta$ extended to bundle-valued $2$-forms.
