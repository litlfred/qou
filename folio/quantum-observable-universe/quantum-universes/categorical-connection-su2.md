This example instantiates the [categorical connection](#def:categorical-connection) concretely on [SU(2)](#ex:quantum-universe-su2).

**Classical setup.** A connection on a Lie group $G$ is a $\mathfrak{g}$-valued 1-form on $G$. The canonical choice is the **Maurer--Cartan form** $\varTheta = g^{-1}  dg$, a left-invariant $\mathfrak{su}(2)$-valued 1-form.

**Explicit matrix form.** For $g \in \mathrm{SU}(2)$ written as

$$
g = \begin{pmatrix} \alpha & -\bar{\beta} \\ \beta & \bar{\alpha} \end{pmatrix}, \qquad |\alpha|^2 + |\beta|^2 = 1,
$$

the inverse is $g^{-1} = g^\dagger = \bigl(\begin{smallmatrix} \bar{\alpha} & \bar{\beta} \\ -\beta & \alpha \end{smallmatrix}\bigr)$. The Maurer--Cartan form evaluates to:

$$
\varTheta = g^{-1} dg
= \begin{pmatrix}
\bar{\alpha}  d\alpha + \bar{\beta}  d\beta &
\bar{\alpha}  d(-\bar{\beta}) + \bar{\beta}  d\bar{\alpha} \\
-\beta  d\alpha + \alpha  d\beta &
-\beta  d(-\bar{\beta}) + \alpha  d\bar{\alpha}
\end{pmatrix}.
$$

Using the constraint $\alpha  d\bar{\alpha} + \bar{\alpha}  d\alpha + \beta  d\bar{\beta} + \bar{\beta}  d\beta = 0$, one verifies that $\varTheta$ is traceless and skew-Hermitian: $\varTheta \in \Omega^1(G; \mathfrak{su}(2))$.

**Flatness.** The curvature of the Maurer--Cartan form is $F = d\varTheta + \varTheta \wedge \varTheta$. The **Maurer--Cartan equation** states that $F = 0$ identically. This follows from $d(g^{-1}) = -g^{-1} (dg)  g^{-1}$:

$$
d\varTheta = d(g^{-1} dg) = d(g^{-1}) \wedge dg
= -g^{-1} dg \wedge g^{-1} dg = -\varTheta \wedge \varTheta,
$$

so $F = d\varTheta + \varTheta \wedge \varTheta = 0$. The Maurer--Cartan form is a **flat** connection.

**Categorical interpretation.** The connection $\varTheta$ corresponds to the natural transformation implementing parallel transport in $\mathbf{Rep}(\mathrm{SU}(2))$. Flatness ($F = 0$) means parallel transport around any contractible loop is trivial. Since $\mathrm{SU}(2) \cong S^3$ is connected, all monodromy is trivial. The Maurer--Cartan connection has trivial holonomy.
