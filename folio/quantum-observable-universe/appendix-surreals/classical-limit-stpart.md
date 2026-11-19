Three blocks address the $q \to 1$ classical limit:

| Block | Scope | Status |
|---|---|---|
| [classical limit functor](#def:classical-limit-functor) | Topological definition $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$ | Definition (with obstruction) |
| **This result** | Single-functor surreal replacement: $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$ | Conjecture (open) |
| [archimedean QOU is standard-part of surreal](#conj:archimedean-stpart) | Whole-tuple surreal replacement on $(\mathbf{C}, \varTheta, G, \mathcal{S})$ | Conjecture (open) |

The current block provides the single-functor version; the whole-tuple version is the appendix companion. Both are likely equivalent modulo functoriality.

The [classical limit functor](#def:classical-limit-functor) $\mathrm{cl} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ takes the $q \to 1$ limit of categorical structures parametrised by the aether parameter $q$. Classically, this requires a topological notion of limit on the parameter space or a careful Hochschild-cohomology construction ([classical limit obstruction](#def:classical-limit-obstruction)). This conjecture proposes a clean replacement: the classical-limit functor is the standard-part of evaluation at $q = 1 + \varepsilon$.

**Conjecture.** Let $\mathbf{C}_q$ be a $K$-linear :refterm[monoidal category]{#monoidal-category} whose structure constants are rational functions of $q \in K$, and let $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ be the topological classical-limit functor (defined when it exists). Set $K = \mathbf{No}$, fix an infinitesimal $\varepsilon \in \mathbf{No}$, and let $\mathrm{ev}_{1 + \varepsilon} : \mathbf{C}_q \to \mathbf{C}_{\mathbf{No}}$ be evaluation at $q = 1 + \varepsilon$. There is a natural isomorphism of functors

$$
  \mathrm{cl}_{\mathrm{top}} \cong \mathrm{St} \circ \mathrm{ev}_{1 + \varepsilon},
$$

whenever the left-hand side is defined. The right-hand side is defined more generally—wherever the structure constants make sense as rational expressions in $\varepsilon$.

The right-hand side always exists as long as the structure constants are rational in $\varepsilon$, even when the left-hand side has obstructions. The classical-limit obstruction $\mathrm{HH}^2(\mathcal{U}_q, \mathrm{Ad})$ becomes a non-zero finite surreal in $\mathbf{No}_{\mathrm{fin}}$ whose standard-part vanishes only when the obstruction itself vanishes. The obstruction is always detected in the surreal lift (as a non-trivial first-order $\varepsilon$-term), but it is "felt by the classical observer" only when the standard-part is non-zero.

The conjecture is open. It is partly motivated by Berarducci--Mantova's derivation construction (2018), which extends $d/dx$ on $\mathbb{R}$. Promoting this from a single function to a functor on $\mathbf{C}_q$ requires functoriality of the standard-part. A first step would be to prove the conjecture for $\mathbf{C}_q = \mathrm{Rep}(\mathrm{SU}_q(2))$.

The paper treats the $q \to 1$ classical limit archimedean-topologically. Under the surreal lift, the limit becomes a literal evaluation at a specific surreal—no topology required. Whether the two formulations give the same answer is the conjecture above. If true, the entire classical-limit discussion could be re-stated as standard-part identities, eliminating one source of analytic machinery.

The proof strategy splits into a single-morphism case and a naturality case. For the single-morphism case, specialise to $\mathbf{C} = \mathrm{Vect}_{\mathbb{Q}(q)}$ and a morphism given by a single rational function $f_q(x)$. Show that $\lim_{q \to 1} f_q$ equals $\mathrm{st}(f_{1+\varepsilon})$. This requires standard-part commuting with rational arithmetic on finite surreals. For naturality, generalise to a functor $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$. This requires functoriality of $\mathrm{St}$ on the $K$-linear category $\mathbf{C}_K$. Falsification requires a discontinuous-but-classically-limit-existing function, which is impossible for rational structure constants.
