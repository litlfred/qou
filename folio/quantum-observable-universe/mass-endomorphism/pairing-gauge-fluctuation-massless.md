Let $\mathbf{C}$ be a :refterm[monoidal category]{#monoidal-category} that is preadditive and $R$-linear over a commutative ring $R$, and let $A^\vee, A$ be objects with an exact pairing $A^\vee \dashv A$ (so that $A$ is a right dual of $A^\vee$ in the sense of a [rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category)), with coevaluation $\eta \colon \mathbf{1} \to A^\vee \otimes A$. The **field space** of [Frobenius pairings](#def:frobenius-pairing) is the $R$-module $\mathcal{P} = \mathrm{Hom}_{\mathbf{C}}(A^\vee \otimes A, \mathbf{1})$. For a co-pairing $\eta$ and a linear functional $\varepsilon \colon \mathrm{End}(\mathbf{1}) \to R$, the **contraction action** is the quadratic form

$$
  S_{\eta,\varepsilon}(T) \;=\; \varepsilon(T \circ \eta)^2 ,
  \qquad
  \frac{\delta S_{\eta,\varepsilon}}{\delta T}(\delta) \;=\; 2\,\varepsilon(T\circ \eta)\,\varepsilon(\delta\circ\eta),
$$

on $\mathcal{P}$, where the variational derivative is twice the symmetric bilinear form of $S_{\eta,\varepsilon}$; it satisfies the exact Taylor identity $S(T+\delta) = S(T) + \frac{\delta S}{\delta T}(\delta) + S(\delta)$.

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

The argument is one line: $(f \otimes \mathrm{id}_A) \circ \eta = (\mathrm{id}_{A^\vee} \otimes f^{\vee}) \circ \eta$ is a standard property of the mate, so $\delta_f\lambda \circ \eta = 0$, and the contraction action sees $\delta_f \lambda$ only through $\delta_f\lambda \circ \eta$.

**The handedness of the Frobenius pairing.** The exact pairing above has evaluation $A \otimes A^\vee \to \mathbf{1}$, which is not the Frobenius pairing $A^\vee \otimes A \to \mathbf{1}$. A non-degenerate Frobenius pairing instead makes $A \dashv A^\vee$ exact, with the Frobenius pairing as evaluation and a coevaluation $\tilde\eta \colon \mathbf{1} \to A \otimes A^\vee$. If $\mathbf{C}$ is a :refterm[braided monoidal category]{#braided-monoidal-category}, with braiding $\beta$, then $\beta_{A,A^\vee} \circ \tilde\eta \colon \mathbf{1} \to A^\vee \otimes A$ is a co-pairing, and the same three conclusions hold for it, with the gauge fluctuation now $\lambda \circ ( f \otimes \mathrm{id}_A - \mathrm{id}_{A^\vee} \otimes {}^{\vee}\! f)$, where ${}^{\vee}\! f \in \mathrm{End}(A)$ is the left adjoint mate of $f$ for $A \dashv A^\vee$. The argument is the same, with the mate identity transported through the naturality of $\beta$.

*Scope.* The contraction action has rank at most one, so its radical contains far more than the pure-gauge directions; the proposition says that gauge directions are *among* the zero modes, not that they exhaust them. Without a braiding, a non-degenerate Frobenius pairing supplies no co-pairing $\mathbf{1} \to A^\vee \otimes A$, and that case is not covered.
