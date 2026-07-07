The bar-involution $\sigma$ defined by $q \mapsto q^{-1}$ and $\sigma^2 = \mathrm{id}$ ([`def:bar-involution`](#def:bar-involution)) splits any element $x$ into a $\sigma$-fixed even part and a $\sigma$-anti odd part:
$$
\mathrm{even}(x) = x + \sigma x, \qquad
\mathrm{odd}(x) = x - \sigma x, \qquad
\mathrm{even}(x) + \mathrm{odd}(x) = 2x.
$$

Applying this to the fibre Habiro element $F$ that controls the substrate separates the two observables:

- **even ($\cosh$, bar-symmetric)**: The binding trace $\tau = \operatorname{tr} B$ from [`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence). This is the curvature-free transport, $(q+q^{-1})/2 = \cosh\lambda$.
- **odd ($\sinh$, bar-antisymmetric)**: The $\mathfrak{Q}_\beta$ residue-A / $c_k$ ladder. This is the curvature defect, $(q-q^{-1})/2 = \sinh\lambda$, representing the bar-odd Habiro dual of $\alpha_{\mathrm{EM}}$.

Binding (mass-average) and $\beta$-decay ($\mathfrak{Q}_\beta$) represent the even and odd parities of a single bar-graded element. Pinning either parity constrains the other. The Lean witnesses [`QOU.Mass.evenPart_add_oddPart`](#prop:bar-parity-split), `evenPart_fixed`, and `oddPart_anti` prove this decomposition.

The bar-even/bar-odd split corresponds to the real/imaginary split of the complex volume $\mathfrak{V}$ ([`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume)). The continuation $\lambda \mapsto i\theta$ sends $\cosh\lambda \mapsto \cos\theta$ and $\sinh\lambda \mapsto i\sin\theta$. The bar-even part becomes $\operatorname{Re}\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}}$ and the bar-odd part becomes $\operatorname{Im}\mathfrak{V} = \mathfrak{Q}_\beta$. The additive projections $x \mapsto x \pm \sigma x$ permit a single identity on $\mathfrak{V}$ to descend to both channels simultaneously.

Mapping this algebraic decomposition to the physical dichotomy of binding and decay provides a rigorous interpretive framework for the Quantum Observable Universe.
