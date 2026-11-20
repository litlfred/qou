Let $\mathbf{C}$ be a $K$-linear category over a field $K$, let $U, X$ be objects, and let

$$
  \varrho \colon U \to X, \qquad \varrho^{*} \colon X \to U, \qquad
  \varrho^{*} \circ \varrho \;=\; t \cdot \mathrm{id}_U, \quad t \in K^{\times}
$$

be a point / copoint pair with invertible pairing. Define

$$
  e \;:=\; t^{-1}\, \varrho \circ \varrho^{*} \colon X \to X,
  \qquad
  r \;:=\; \mathrm{id}_X - e .
$$

**(a) Vacuum idempotent and residual.**

1. $e \circ e = e$, $\;e \circ \varrho = \varrho$, $\;\varrho^{*} \circ e = \varrho^{*}$.
2. $r \circ r = r$, $\;e \circ r = r \circ e = 0$, $\;e + r = \mathrm{id}_X$.
3. $r \circ \varrho = 0$ and $\varrho^{*} \circ r = 0$: the residual annihilates the vacuum.

**(b) Symmetric / antisymmetric split of the two-vacuum residual.** Let $\sigma \colon Y \to Y$ satisfy $\sigma \circ \sigma = \mathrm{id}_Y$ and let $c \in K$ with $c + c = 1$ (so $\operatorname{char} K \neq 2$ and $c = \tfrac12$). Put $P_{+} = c\,(\mathrm{id}_Y + \sigma)$ and $P_{-} = c\,(\mathrm{id}_Y - \sigma)$. Then $P_\pm$ are idempotent, $P_{+} + P_{-} = \mathrm{id}_Y$, $P_{-} \circ P_{+} = 0$, $\sigma \circ P_{+} = P_{+}$, $\sigma \circ P_{-} = -P_{-}$, and $P_\pm$ commute with every endomorphism that commutes with $\sigma$.

Now let $\mathbf{C}$ be symmetric monoidal and monoidal-preadditive, $Y = X \otimes X$, $\sigma = \beta_{X,X}$, and let $R := \mathrm{id}_{X \otimes X} - e \otimes e$ be the residual of the two-vacuum idempotent. Then:

4. $e \otimes e$ and $R$ are idempotent, and both commute with $P_{\pm}$ (naturality of $\beta$).
5. $R = P_{+} \circ R + P_{-} \circ R$, where $P_{\pm} \circ R$ are idempotents and $(P_{-} \circ R) \circ (P_{+} \circ R) = 0$.
6. $R = r \otimes e + e \otimes r + r \otimes r$.
7. $P_{+} \circ (r \otimes r)$ is an idempotent: the symmetric square of the residual.

**(c) Traces.** Let $\mathrm{tr}$ assign to each endomorphism a scalar in $K$, additively, $K$-homogeneously and cyclically: $\mathrm{tr}(g \circ f) = \mathrm{tr}(f \circ g)$ for $f \colon Y \to Z$, $g \colon Z \to Y$. Then

8. $\mathrm{tr}(e) = \mathrm{tr}(\mathrm{id}_U)$ and $\mathrm{tr}(r) = \mathrm{tr}(\mathrm{id}_X) - \mathrm{tr}(\mathrm{id}_U)$. In particular, for $U = \mathbf{1}$ and $\mathrm{tr}(\mathrm{id}_{\mathbf{1}}) = 1$, $\mathrm{tr}(e) = 1$, whatever $X$ is.

Items 1–7 use no rigidity, trace or pivotal structure. Item 8 takes the trace as a hypothesis with the three stated properties; it does not construct the pivotal trace of a particular category. In a rigid category $\varrho^{*}$ would come from $\varrho$ through a self-duality of $X$; the statements above need only the scalar identity $\varrho^{*} \circ \varrho = t \cdot \mathrm{id}_U$.

*Proof.* Each item is a short computation. For example, $e \circ e = t^{-2}\,\varrho\,(\varrho^{*}\varrho)\,\varrho^{*} = t^{-2} t\,\varrho\varrho^{*} = e$. For $P_{+}$: $(\mathrm{id} + \sigma)^2 = 2(\mathrm{id} + \sigma)$, so $P_{+}^2 = c^2 \cdot 2(\mathrm{id} + \sigma) = c(c+c)(\mathrm{id} + \sigma) = P_{+}$. Item 5 is the general fact that commuting idempotents compose to an idempotent. Item 8: $\mathrm{tr}(e) = t^{-1}\,\mathrm{tr}(\varrho \circ \varrho^{*}) = t^{-1}\,\mathrm{tr}(\varrho^{*} \circ \varrho) = t^{-1}\,\mathrm{tr}(t\,\mathrm{id}_U) = \mathrm{tr}(\mathrm{id}_U)$. Item 6 follows from $\mathrm{id}_{X\otimes X} = (e + r) \otimes (e + r)$ and bilinearity of $\otimes$.
