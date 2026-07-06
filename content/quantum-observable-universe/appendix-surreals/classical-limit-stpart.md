**Conjecture (Archimedean QOU as standard part of surreal QOU — single-functor).**

The $q \to 1$ classical limit is addressed in three blocks:
1. [Classical limit functor](#def:classical-limit-functor): Topological definition $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$ (with obstruction).
2. **This block**: Single-functor surreal replacement, $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$ (Conjecture).
3. [Archimedean QOU is standard-part of surreal](#conj:archimedean-stpart): Whole-tuple surreal replacement on $(\mathbf{C}, \varTheta, G, \mathcal{S})$ (Conjecture).

The classical limit functor $\mathrm{cl} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ captures the $q \to 1$ limit of categorical structures parametrized by the substrate parameter $q$. Classically, this requires either a topological limit on the parameter space (which fails for surreal-valued $q$) or a Hochschild-cohomology construction ([classical limit obstruction](#def:classical-limit-obstruction)). 

This conjecture asserts that the classical-limit functor equals the standard-part of evaluation at $q = 1 + \varepsilon$.

### Conjecture

Let $\mathbf{C}_q$ be a $K$-linear :refterm[monoidal category]{#monoidal-category} whose structure constants are rational functions of $q \in K$. Let $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ be the topological classical-limit functor (when it exists). Set $K = \mathbf{No}$, fix an infinitesimal $\varepsilon \in \mathbf{No}$, and let $\mathrm{ev}_{1 + \varepsilon} : \mathbf{C}_q \to \mathbf{C}_{\mathbf{No}}$ be evaluation at $q = 1 + \varepsilon$.

There is a natural isomorphism of functors:

$$
  \mathrm{cl}_{\mathrm{top}}
   \;\cong\;
  \mathrm{St} \circ \mathrm{ev}_{1 + \varepsilon},
$$

whenever the left-hand side is defined. The right-hand side is defined more generally, existing wherever the structure constants are rational expressions in $\varepsilon$.

### Eliminating the Obstruction

This natural isomorphism demands agreement on objects (the standard part of an infinitesimal-shifted object is the archimedean object) and on morphisms (the standard part of a Jackson derivative is the classical derivative; the standard part of a $q$-shifted matrix entry is its $q = 1$ value).

Crucially, the right-hand side exists whenever structure constants are rational in $\varepsilon$, even if the left-hand side is obstructed. The classical-limit obstruction ([classical limit obstruction](#def:classical-limit-obstruction)) $\mathrm{HH}^2(\mathcal{U}_q, \mathrm{Ad})$ manifests on the right-hand side as a non-zero finite surreal in $\mathbf{No}_{\mathrm{fin}}$. Its standard part vanishes exactly when the obstruction itself vanishes. The obstruction is always detected in the surreal lift as a first-order $\varepsilon$-term, but it is only "felt" classically when the standard part is non-zero.

### Motivating Example

Berarducci and Mantova [@berarducci-mantova2018] construct a derivation $D : \mathbf{No} \to \mathbf{No}$ extending $d/dx$ on $\mathbb{R}$. The standard part of $D(f(1 + \varepsilon))$ recovers $f'(1)$ for analytic $f$. Promoting this from a single function to a functor on $\mathbf{C}_q$ requires functoriality of the standard part. This is known classically [@robinson1966] in model theory but remains open categorically. A natural first step is proving this for $\mathbf{C}_q = \mathrm{Rep}(\mathrm{SU}_q(2))$.

### Significance

The main paper treats the $q \to 1$ classical limit topologically. Under the surreal lift, this limit becomes a literal evaluation at a specific surreal, requiring no topology. If this conjecture holds, the paper's classical-limit discussions (Möbius energy comparison, experimental benchmarks, $\hbar_q \to 0$) can be cleanly re-stated as standard-part identities. This eliminates reliance on archimedean analytic machinery.

### Proof Strategy

The conjecture splits into a single-morphism case and a naturality case.

**Single-Morphism Case (Single-Element Ground Field)**:
1. **Specialize** to $\mathbf{C} = \mathrm{Vect}_{\mathbb{Q}(q)}$ and a morphism $f : V \to V$ given by $f_q(x) = p(q, x) / r(q, x)$ in $\mathbb{Q}(q, x)$.
2. **Show** that $\lim_{q \to 1} f_q$ equals $\mathrm{st}(f_{1+\varepsilon})$. Taylor expanding yields $f_{1+\varepsilon} = f_1 + \varepsilon \cdot g + O(\varepsilon^2)$. The standard part recovers $f_1 = \lim_{q \to 1} f_q$.
3. **Lemma needed**: The standard part commutes with rational arithmetic on finite surreals (via `QOU.AppendixSurreals.standardPart_add` and `standardPart_mul`).

**Naturality Case**:
1. **Generalize** to a functor $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$. This requires functoriality of $\mathrm{St}$ on the $K$-linear category $\mathbf{C}_K$. This follows from the ring-homomorphism property of $\mathrm{St}$ on the finite subring, provided $\mathbf{C}$ is enriched over $K$-modules.

**Required Infrastructure**:
- `QOU.AppendixSurreals.standardPart_add`, `_mul` (proved up to `IsFinite_decomposition`).
- A Lean decision procedure for "rational in $\varepsilon$".

**Falsification Path**: Produce a categorical structure $\mathbf{C}_q$ where a morphism's $q \to 1$ topological limit exists but fails to match the standard part of evaluation at $1 + \varepsilon$. This requires a discontinuous-but-classically-limit-existing function, which is impossible for rational structure constants.
