<!-- FILE_START: alpha-k-procedure-atom-knot-mass-intro.md -->
We now derive the atom-knot mass. We assemble the joint-tower SDP confinement constraints and identify the $y_\lambda$ closed-form Wenzl bridge. This yields the per-atom-knot mass coefficient table.
<!-- FILE_END: alpha-k-procedure-atom-knot-mass-intro.md -->

<!-- FILE_START: joint-tower-sdp-confinement.md -->
**Proposition (joint mass-tower confinement SDP).**
*Let $\mathcal{U}$ be a quantum observable universe at substrate parameter $q_0$. The joint mass-tower confinement SDP is:*

$$
\boxed{\quad
\begin{aligned}
& \text{find} && \big( c_{\mathfrak{H}, w}(q_0) \big)_{\mathfrak{H} \in \mathcal{R}, \, w \in S_{n_0(\mathfrak{H})}} \in \mathbb{Q}, \\
& \text{such that} && \forall \, \mathfrak{H} \in \mathcal{R}: \\
& && \quad T_w(\mathfrak{H}) := \sum_{w \in S_{n_0(\mathfrak{H})}} c_{\mathfrak{H}, w}(q_0) \cdot T_w \;\in\; H_{n_0(\mathfrak{H})}(q_0) \\
& && \quad \rho_\lambda(T_w(\mathfrak{H})) \succeq 0 \text{ for all Wedderburn blocks } \lambda \vdash n_0(\mathfrak{H}) \\
& && \quad \text{(GB-filtration grading: } c_{\mathfrak{H}, w} \neq 0 \Rightarrow \ell(w) \in \mathrm{Filt}(\mathfrak{H})\text{)} \\
& && \quad \text{(jet-order ordering: SDP variable indexing respects jet order)} \\
& \text{cross-level constraints:} && \forall \, \mathfrak{H} \to \mathfrak{H}' \text{ in tower:} \\
& && \quad \pi_{\mathfrak{H} \to \mathfrak{H}'} \big( T_w(\mathfrak{H}) \big) \;=\; T_w(\mathfrak{H}')
\end{aligned}
\quad}
$$

*The solution is a structured certificate containing the canonical Hecke element per atom, its filtration grading, and its jet-order log.*

The per-atom SDP alone cannot enforce cross-level consistency. The joint formulation guarantees that the filtration grading and jet ordering remain consistent across confinement levels. The output provides the precise coefficients $M(\mathfrak{H}) = \rho(\mathfrak{H}) \cdot \mathrm{tr}_M(T_w(\mathfrak{H}))$ for the mass evaluation.
<!-- FILE_END: joint-tower-sdp-confinement.md -->

<!-- FILE_START: y-lambda-closed-form-wenzl-bridge.md -->
**Proposition (closed form for $y_\lambda$ via Wenzl bridge).**
*Let $\sigma_i$ be the symmetric Hecke generators with eigenvalues $q, -q^{-1}$. The central coefficients $y_\lambda$ in the Jones-Markov trace admit the closed form:*

$$
  \boxed{\;
    y_\lambda \;=\; \frac{s_\lambda(1, Q, Q^2, \ldots, Q^{r-1})}
                        {\sum_{\mu \,\vdash\, n} d_\mu \cdot s_\mu(1, Q, Q^2, \ldots, Q^{r-1})}
  \;}
$$

*where $Q = q^2$, $d_\mu$ is the hook-length dimension, and $r$ is the unique solution to:*

$$
  q \cdot z \;=\; \frac{Q^r (1 - Q)}{1 - Q^r}.
$$

*This resolves the convention mismatch between the symmetric Hecke formulation and the standard Wenzl formulas.*

The Wenzl-bridge identifies $y_\lambda$ symbolically. We substitute $Q=q^2$ and $z_{\mathrm{GL}}=q \cdot z$ into the principal-specialisation Schur element. This avoids explicit linear-system solves and delivers polynomial q-rational forms in fraction of the computation time.
<!-- FILE_END: y-lambda-closed-form-wenzl-bridge.md -->
