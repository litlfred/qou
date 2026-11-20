Let $\mathbf{C}$ be a monoidal category that is preadditive and $R$-linear over a commutative ring $R$, and let $A^\vee, A$ be objects with an exact pairing $A^\vee \dashv A$ in the sense of a [rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category), with coevaluation $\eta \colon \mathbf{1} \to A^\vee \otimes A$. The **field space** of [Frobenius pairings](#def:frobenius-pairing) is the $R$-module $\mathcal{P} = \mathrm{Hom}_{\mathbf{C}}(A^\vee \otimes A, \mathbf{1})$. For a linear functional $\varepsilon \colon \mathrm{End}(\mathbf{1}) \to R$, the **contraction action** is the quadratic form

$$
  S_{\eta,\varepsilon}(T) \;=\; \varepsilon(\eta \circ T)^2 ,
  \qquad
  \frac{\delta S_{\eta,\varepsilon}}{\delta T}(\delta) \;=\; 2\,\varepsilon(\eta\circ T)\,\varepsilon(\eta\circ\delta),
$$

on $\mathcal{P}$, where the variational derivative is defined by the exact Taylor identity $S(T+\delta) = S(T) + \frac{\delta S}{\delta T}(\delta) + S(\delta)$.

For $f \in \mathrm{End}(A^\vee)$ with right adjoint mate $f^{\vee} \in \mathrm{End}(A)$, the **pure-gauge fluctuation** of a background pairing $\lambda \in \mathcal{P}$ is

$$
  \delta_f \lambda \;=\; \lambda \circ \bigl( f \otimes \mathrm{id}_A \;-\; \mathrm{id}_{A^\vee} \otimes f^{\vee} \bigr).
$$

**Proposition.** For every $f$, every background $\lambda$ and every field $T \in \mathcal{P}$:

$$
  S_{\eta,\varepsilon}(\delta_f\lambda) = 0,
  \qquad
  \frac{\delta S_{\eta,\varepsilon}}{\delta T}(\delta_f\lambda) = 0,
  \qquad
  S_{\eta,\varepsilon}(T + \delta_f\lambda) = S_{\eta,\varepsilon}(T).
$$

More generally, for any quadratic action $S$ on an $R$-module, invariance under translation by a direction $g$ holds **if and only if** $S(g) = 0$ and $g$ lies in the radical of $\delta S/\delta T$ for every $T$; such directions form a submodule. No hypothesis on $2 \in R$ is used.

The argument is one line: $\eta \circ (f \otimes \mathrm{id}_A) = \eta \circ (\mathrm{id}_{A^\vee} \otimes f^{\vee})$ is the defining property of the mate, so $\eta \circ \delta_f\lambda = 0$, and the contraction action sees $\delta_f \lambda$ only through $\eta \circ \delta_f\lambda$.

*Scope.* The contraction action has rank at most one, so its radical contains far more than the pure-gauge directions; the proposition says that gauge directions are *among* the zero modes, not that they exhaust them. The exact pairing used here has coevaluation $\mathbf{1} \to A^\vee \otimes A$, the opposite handedness to the non-degeneracy condition on the Frobenius pairing; no braiding is assumed to identify the two.
