**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with fibre functor $\tau$. For every braid $\beta \in H_n(R, q)$, the real-valued knot volume $\mathrm{Vol}(K_\beta)$ factors strictly through $\tau$:*

$$
  \mathrm{Vol}(K_\beta)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  (\pi_\infty \circ \tau)\bigl(\mathrm{Vol}_q(\beta)\bigr).
$$

*There is no other archimedean route.*

**Identification.**
On the algebraic quantum volume, $\tau_{\mathrm{arch}}$ coincides with $\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}$. The fibre functor $\tau$ is the exclusive bridge to the laboratory continuum. The realization functor defines its canonical computation rule.

**Sketch.**
By Tannaka-Krein rigidity, any composite mapping $\mathbf{C}$ to $\mathbb{R}$ that preserves tensor products and dualities is uniquely isomorphic to the fibre functor $\tau$. Conversely, restricting the composite $\tau \circ \mathrm{Vol}_q$ via $\pi_\infty$ recovers exactly $\ln |\mathrm{Vol}_{q_0}(\beta)|$. Every physical computation of a knot volume (e.g., Kashaev limit, Bloch-Wigner dilogarithm) evaluates this identical composite.

**Lean formalization.**
The Lean theorem `vol_through_tau_factors` currently holds an existence stub pending a faithful formal statement.
