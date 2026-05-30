**Proposition (Hecke branching trace decomposition).**
*Let $H_{n+m}(q)$ act on its irreducible Hoefsmit seminormal module
$V_\lambda$ ($\lambda \vdash n+m$), and let $I \in H_{n+m}(q)$ be an
"interface" element (any product of generators that bridges the index
range $\{n, n+1\}$). For braid words $\beta_1 \in H_n(q)$,
$\beta_2 \in H_m(q)$ acting on the left/right $H_n \otimes H_m$
factors, the trace of $\beta_1 \cdot I \cdot \beta_2$ on $V_\lambda$
admits the block decomposition*

$$
\operatorname{tr}_{V_\lambda}\!\bigl(\rho_\lambda(\beta_1 \cdot I \cdot \beta_2)\bigr)
\;=\;
\sum_{\substack{\mu \vdash n \\ \nu \vdash m}}
\operatorname{tr}_{V_\mu \otimes V_\nu}\!
\Bigl(A^\lambda_{\mu,\nu}(I)\,\cdot\,
\bigl(\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)\bigr)\Bigr),
$$

*where $A^\lambda_{\mu,\nu}(I) \in \operatorname{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu,\nu}}$
is the operator-valued coefficient encoding the multiplicities given
by the Littlewood–Richardson coefficients $c^\lambda_{\mu,\nu}$, and
$\rho_\lambda, \rho_\mu, \rho_\nu$ are the Hoefsmit seminormal
representations of $H_\bullet(q)$.*

## Proof

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

## Corollary (the case used downstream)

Taking $\beta_1 = \beta_2 = 1$ recovers the simpler
$$
\chi^\lambda(I) \;=\; \sum_{\mu, \nu} \operatorname{tr}\,A^\lambda_{\mu,\nu}(I),
$$
which is the form consumed by the scalar-vs-operator Frobenius
budget in
[`rem:operator-valued-magnitude-budget`](operator-valued-magnitude-budget.md).
The Pythagorean orthogonality
$$
\bigl\| A^\lambda_{\mu,\nu}(I) - A^{\lambda,\mu,\nu}_{\mathrm{scalar}} \bigr\|_F^2
\;=\;
\bigl\| A^\lambda_{\mu,\nu}(I) \bigr\|_F^2
\;-\;
\frac{\bigl|\operatorname{tr}\,A^\lambda_{\mu,\nu}(I)\bigr|^2}{d_\mu \, d_\nu}
$$
is the standard scalar-vs-traceless decomposition of an operator
under the Hilbert–Schmidt inner product — no further hypothesis is
needed.

## Remarks

- The hypothesis $q^{1/2} + q^{-1/2} > 2$ is sharp for semisimplicity
  (Wenzl 1988, §1); below it, the Wedderburn decomposition fails and
  the $A^\lambda_{\mu,\nu}$ decomposition is not well-defined. The
  substrate value $q_0 > 1$ is comfortably inside the regime.
- Halverson–Ram 1998 give an explicit combinatorial Murnaghan–
  Nakayama-type rule for evaluating
  $\operatorname{tr}\,A^\lambda_{\mu,\nu}(I)$ when $I$ is a product
  of Murphy generators; this is the computational ingredient used by
  `probe_operator_valued_ansatze_from_mass_endo.py`.
- The same statement holds for any inclusion
  $H_{n_1}(q) \otimes \cdots \otimes H_{n_k}(q) \hookrightarrow
  H_{\sum n_i}(q)$ (iterate the branching).
