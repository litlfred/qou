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
