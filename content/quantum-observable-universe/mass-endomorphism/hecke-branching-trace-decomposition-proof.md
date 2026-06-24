By Wenzl 1988 (Theorem 1.4), $H_{n+m}(q)$ is semisimple with
Wedderburn decomposition
$$
H_{n+m}(q) \;\cong\; \bigoplus_{\lambda \vdash n+m} \operatorname{End}(V_\lambda)
$$
whenever $q$ is generic — in particular throughout the Wenzl
positivity regime $q^{1/2} + q^{-1/2} > 2$ (which holds at the
substrate value $q_0 \approx 1.11$).

The branching for the inclusion
$H_n(q) \otimes H_m(q) \hookrightarrow H_{n+m}(q)$ on irreducibles is
$$
\operatorname{Res}^{H_{n+m}}_{H_n \otimes H_m} V_\lambda
\;\cong\;
\bigoplus_{\substack{\mu \vdash n \\ \nu \vdash m}}
\bigl(V_\mu \boxtimes V_\nu\bigr)^{\oplus c^\lambda_{\mu,\nu}},
$$
where $c^\lambda_{\mu,\nu}$ are the Littlewood–Richardson coefficients
(Halverson–Ram 1998, §4; Hoefsmit 1974, Ch. III). Choose the
branching isomorphism that respects the Hoefsmit seminormal basis on
each $V_\mu \otimes V_\nu$ component.

An interface element $I \in H_{n+m}(q)$ acts on $V_\lambda$;
restricting to the $(\mu, \nu)$-isotypic component and writing the
resulting endomorphism in the LR-multiplied basis defines the
operator-valued matrix coefficient
$$
A^\lambda_{\mu,\nu}(I) \;\in\; \operatorname{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu,\nu}}.
$$

Since $\beta_1 \in H_n(q)$ commutes with the $(\mu,\nu)$-block
projection (the inclusion is an algebra map and the projection is
central in $H_n(q) \otimes H_m(q)$), and similarly for $\beta_2$, the
action of $\beta_1 \cdot I \cdot \beta_2$ on the $(\mu, \nu)$
isotypic component factors as
$$
A^\lambda_{\mu,\nu}(I) \cdot \bigl(\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)\bigr).
$$

The trace of $\rho_\lambda(\beta_1 \cdot I \cdot \beta_2)$ on
$V_\lambda$ is the sum of traces over the orthogonal $(\mu, \nu)$-
isotypic components, yielding the claimed identity. ∎
