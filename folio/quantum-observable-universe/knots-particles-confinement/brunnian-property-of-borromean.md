**Proposition (Brunnian property of $\mathcal{B}_3$).** *Let $\mathcal{B}_3 \subset \mathbb{R}^3$ be the Borromean link ([Borromean baryon](#def:borromean-baryon)), presented as the Markov closure $\overline{\beta_{\mathrm{Bor}}}$ of the three-strand braid $\beta_{\mathrm{Bor}} = (\sigma_0 \sigma_1^{-1})^3 \in B_3$. Then $\mathcal{B}_3$ is a non-trivial three-component Brunnian link \cite{kawauchi1996}:*

1. *$\beta_{\mathrm{Bor}}$ induces the identity strand permutation on $\{0, 1, 2\}$, so $\mathcal{B}_3$ has three components $K_0, K_1, K_2$ with vanishing pairwise linking numbers;*
2. *for every $c \in \{0, 1, 2\}$, the two-component sub-link $\mathcal{B}_3 \setminus K_c$ obtained by deleting $K_c$ is isotopic to the trivial two-component unlink $U_2$;*
3. *$\beta_{\mathrm{Bor}}$ is non-trivial in $B_3$ (and not conjugate in $B_3$ to the identity braid).*

*Proof.* Label the three strands by their initial horizontal slots $(0, 1, 2)$. Reading $\beta_{\mathrm{Bor}} = \sigma_0 \sigma_1^{-1} \sigma_0 \sigma_1^{-1} \sigma_0 \sigma_1^{-1}$ from left to right updates the slot occupancy through the six-step cycle

$$
  (0, 1, 2) \;\xrightarrow{\sigma_0}\; (1, 0, 2) \;\xrightarrow{\sigma_1^{-1}}\; (1, 2, 0) \;\xrightarrow{\sigma_0}\; (2, 1, 0) \;\xrightarrow{\sigma_1^{-1}}\; (2, 0, 1) \;\xrightarrow{\sigma_0}\; (0, 2, 1) \;\xrightarrow{\sigma_1^{-1}}\; (0, 1, 2),
$$

returning the identity permutation on $\{0, 1, 2\}$. Markov closure therefore joins each strand to itself in three distinct components $K_0, K_1, K_2$, and each unordered pair $\{s, t\} \subset \{0, 1, 2\}$ crosses once positively and once negatively, giving signed crossing sum $0$.

Fix $c \in \{0, 1, 2\}$ and erase component $K_c$ from the closed-braid diagram. At the four crossings incident to $K_c$, removing the arc of $K_c$ leaves the left-to-right order of the two surviving strands unchanged and introduces no crossing between them. At the two crossings disjoint from $K_c$, the crossing strands occupy adjacent slots ($(0, 1)$ for $\sigma_0$ with $K_c$ in outer slot $2$, and $(1, 2)$ for $\sigma_1^{-1}$ with $K_c$ in outer slot $0$), so $K_c$ never lies between them. Order-preserving planar projection onto $B_2$ therefore presents $\mathcal{B}_3 \setminus K_c$ as the Markov closure of the two-strand braid word

$$
  d_0(\beta_{\mathrm{Bor}}) \;=\; \sigma_0 \sigma_0^{-1}, \qquad
  d_1(\beta_{\mathrm{Bor}}) \;=\; \sigma_0^{-1} \sigma_0, \qquad
  d_2(\beta_{\mathrm{Bor}}) \;=\; \sigma_0 \sigma_0^{-1}.
$$

In each case the two surviving strands return to their initial slots, and a single Reidemeister II cancellation reduces $d_c(\beta_{\mathrm{Bor}})$ to the empty two-strand word $1 \in B_2 \cong F_1$, whose Markov closure is the trivial two-component unlink $U_2$ \cite{kawauchi1996}.

For three-strand non-triviality, evaluate the $2 \times 2$ reduced Burau representation $\rho_q \colon B_3 \to \mathrm{GL}_2(\mathbb{Z}[q, q^{-1}])$ \cite{birman1974} defined by

$$
  \rho_q(\sigma_0) \;=\; \begin{pmatrix} -q & 1 \\ 0 & 1 \end{pmatrix}, \qquad
  \rho_q(\sigma_1) \;=\; \begin{pmatrix} 1 & 0 \\ q & -q \end{pmatrix}.
$$

A single alternating period has matrix $M = \rho_q(\sigma_0 \sigma_1^{-1}) = \begin{pmatrix} 1 - q & -q^{-1} \\ 1 & -q^{-1} \end{pmatrix}$, and cubing gives $\rho_q(\beta_{\mathrm{Bor}}) = M^3$ with lower-left entry and conjugation-invariant trace shift

$$
  \bigl(\rho_q(\beta_{\mathrm{Bor}})\bigr)_{1,0} \;=\; \frac{(q - 1)^2(q^2 + 1)}{q^2}, \qquad
  \mathrm{tr}\bigl(\rho_q(\beta_{\mathrm{Bor}})\bigr) - 2 \;=\; -\frac{(q - 1)^4(q^2 + q + 1)}{q^3}.
$$

For every real $q > 1$, $\bigl(\rho_q(\beta_{\mathrm{Bor}})\bigr)_{1,0} > 0$ and $\mathrm{tr}\bigl(\rho_q(\beta_{\mathrm{Bor}})\bigr) < 2 = \mathrm{tr}(I_2)$, so $\rho_q(\beta_{\mathrm{Bor}}) \neq I_2$ and $\beta_{\mathrm{Bor}}$ is neither equal nor conjugate in $B_3$ to the identity braid. Removing any single component therefore dissolves the three-strand binding into $U_2$, realizing [topological color confinement](#rem:borromean-topological-confinement). $\square$
