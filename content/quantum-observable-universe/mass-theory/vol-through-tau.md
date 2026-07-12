**Proposition (conditional on [`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture)).**
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

**Sketch (conditional).**
The conjectural hypothesis is the Kashaev volume conjecture: the hyperbolic volume of the closure equals the Kashaev limit of the colored Jones polynomial ([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture), Lean class `VolumeConjecture`, field `kvc_holds`). By Tannaka-Krein rigidity, any composite mapping $\mathbf{C}$ to $\mathbb{R}$ that preserves tensor products and dualities is uniquely isomorphic to the fibre functor $\tau$; the realization functor's computation rule evaluates $\tau_{\mathrm{arch}}$ on the algebraic quantum volume $\mathrm{Vol}_q(\beta)$ as exactly the Kashaev limit. Conditional on the conjecture, the two identifications compose to $\mathrm{Vol}(K_\beta) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(\beta))$ — this composition is the Lean-derived step (`vol_through_tau_of_volumeConjecture`), with the Kashaev identification consumed as the class hypothesis rather than asserted.
