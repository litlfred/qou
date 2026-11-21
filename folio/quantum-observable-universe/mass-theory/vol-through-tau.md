**Proposition (conditional on the [Kashaev volume conjecture](#conj:kashaev-volume-conjecture)).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with fibre functor $\tau$. For every **braid** $\beta \in B_n$, with image $\rho(\beta) \in H_n(R, q)$ and closure $K_\beta$, the real-valued knot volume $\mathrm{Vol}(K_\beta)$ factors strictly through $\tau$:*

The quantifier is over braids. $\rho : B_n \to H_n(R,q)$ is neither injective nor surjective, and a Hecke element outside its image has no closure, so the statement assigns no volume to such an element. In particular the atomic words $c\,\sigma_g + d\,\mathbf{1}$ are general Hecke elements, not braids, and their volume is $0$.

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
The conjectural hypothesis is the Kashaev volume conjecture: the hyperbolic volume of the closure equals the Kashaev limit of the colored Jones polynomial ([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)). By Tannaka-Krein rigidity, any composite mapping $\mathbf{C}$ to $\mathbb{R}$ that preserves tensor products and dualities is uniquely isomorphic to the fibre functor $\tau$; the realization functor's computation rule evaluates $\tau_{\mathrm{arch}}$ on the algebraic quantum volume $\mathrm{Vol}_q(\beta)$ as exactly the Kashaev limit. Conditional on the conjecture, the two identifications compose to $\mathrm{Vol}(K_\beta) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(\beta))$ — this composition is the proved step, with the Kashaev identification taken as a hypothesis rather than asserted.
