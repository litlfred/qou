*Let $H_{n+m}(q)$ act on its irreducible Hoefsmit seminormal module $V_\lambda$ ($\lambda \vdash n+m$) \cite{hoefsmit1974}, \cite[(2.3), Thm.~2.4]{halverson_ram_1998}. Let $I \in H_{n+m}(q)$ be an interface element (any product of generators bridging the index range $\{n, n+1\}$). For braid words $\beta_1 \in H_n(q)$ and $\beta_2 \in H_m(q)$ acting on the left and right $H_n \otimes H_m$ factors respectively, the trace of $\beta_1 \cdot I \cdot \beta_2$ on $V_\lambda$ admits the block decomposition:*

$$
\mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda(\beta_1 \cdot I \cdot \beta_2)\bigr)
\;=\;
\sum_{\substack{\mu \vdash n \\ \nu \vdash m}}
\mathrm{tr}_{V_\mu \otimes V_\nu}\!
\Bigl(A^\lambda_{\mu,\nu}(I)\,\cdot\,
\bigl(\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)\bigr)\Bigr),
$$

*where $A^\lambda_{\mu,\nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu,\nu}}$ is the operator-valued coefficient encoding the multiplicities given by the Littlewood–Richardson coefficients $c^\lambda_{\mu,\nu}$, and $\rho_\lambda, \rho_\mu, \rho_\nu$ are the Hoefsmit seminormal representations of $H_\bullet(q)$.*

## Corollary (the case used downstream)

Taking $\beta_1 = \beta_2 = 1$ recovers the simpler sum:
$$
\chi^\lambda(I) \;=\; \sum_{\mu, \nu} \mathrm{tr}\,A^\lambda_{\mu,\nu}(I),
$$
This form supplies the scalar-vs-operator Frobenius budget in [Magnitude budget: operator-valued vs scalar approximation of $A^\lambda_{\mu\nu}(I)$](operator-valued-magnitude-budget.md). The Pythagorean orthogonality:
$$
\bigl\| A^\lambda_{\mu,\nu}(I) - A^{\lambda,\mu,\nu}_{\mathrm{scalar}} \bigr\|_F^2
\;=\;
\bigl\| A^\lambda_{\mu,\nu}(I) \bigr\|_F^2
\;-\;
\frac{\bigl|\mathrm{tr}\,A^\lambda_{\mu,\nu}(I)\bigr|^2}{d_\mu \, d_\nu}
$$
provides the standard scalar-vs-traceless decomposition of an operator under the Hilbert–Schmidt inner product. No further hypothesis remains needed.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
