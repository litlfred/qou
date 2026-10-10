*Proof of (2).* In the archimedean realisation the tower is a sequence of bundles over the fixed base $M_0$. By the explicit construction of the [recursive brane tower](#def:recursive-brane-tower), $\mathcal{S}_{n+1}$ is the bundle of orthonormal frames of the first jet bundle $J^1 \mathcal{S}_n$ ([jet prolongation](#prop:jet-prolongation)), projectivised; its typical fibre is $\mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$.

The Euler characteristic of a fibre bundle $F \hookrightarrow E \to B$ whose fibre has the homotopy type of a finite CW complex and whose monodromy acts trivially on $H^*(F; \mathbb{Q})$ is multiplicative, $\chi_{\mathrm{eu}}(E) = \chi_{\mathrm{eu}}(F) \cdot \chi_{\mathrm{eu}}(B)$ (the Leray–Serre spectral sequence collapses at $E_2$). The observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is what makes the monodromy of $\pi_1(\mathcal{S}_n)$ on $H^*(S^2; \mathbb{Z})$ trivial: the adjoint bundle has no invariant sections to twist the fibre cohomology. Since $\chi_{\mathrm{eu}}(S^2) = 2$,

$$
  \chi_{\mathrm{eu}}(\mathcal{S}_{n+1}) = 2\,\chi_{\mathrm{eu}}(\mathcal{S}_n),
$$

so the Euler characteristic of the total space doubles at every level and is not the stable quantity.

What is stable is the base. Each level of the tower replaces a bundle over $M_0$ by a bundle over $M_0$ and never alters $M_0$; therefore $\chi_{\mathrm{eu}}(M_0) = 2 - 2g(M_0)$ persists at every level. $\square$
