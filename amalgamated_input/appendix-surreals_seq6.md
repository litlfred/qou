<!-- FILE_START: standard-part-classical-limits-intro.md -->
The standard-part functor projects surreal-valued observables to their real shadows, recovering classical limits.
<!-- FILE_END: standard-part-classical-limits-intro.md -->

<!-- FILE_START: valuation-ring-finite-surreals.md -->
The [standard-part functor](#def:standard-part-functor) $\mathrm{st} : \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}$ admits a clean ring-theoretic reading: it is the quotient map of a valuation ring.

The finite surreals form a convex subring of $\mathbf{No}$:

$$
  \mathcal{O} = \{ x \in \mathbf{No} : \exists n \in \mathbb{N},\, -n < x < n \} = \{ x \in \mathbf{No} : \mathrm{IsFinite}(x) \}.
$$

The infinitesimals form its unique maximal ideal:

$$
  \mathfrak{m} = \{ x \in \mathcal{O} : \mathrm{IsInfinitesimal}(x) \}.
$$

The quotient $\mathcal{O} / \mathfrak{m} \xrightarrow{\sim} \mathbb{R}$ is canonically isomorphic to the real numbers, and the projection $\mathcal{O} \twoheadrightarrow \mathcal{O}/\mathfrak{m}$ is exactly $\mathrm{st}$.

The appendix's functorial constructions (point-evaluation of schemes, categorical enrichments, surreal-coefficient sheaves) all need a set-sized coefficient ring to avoid proper-class pathologies. The valuation ring $\mathcal{O}$ is set-sized; the ambient $\mathbf{No}$ is a proper class. By restricting to $\mathcal{O}$ before point-evaluation, we stay inside standard set-theoretic foundations.

The infinite surreals $\mathbf{No} \setminus \mathcal{O}$ are not in the domain of $\mathrm{st}$. Any arithmetic involving $\omega, \omega^2, \omega^\omega$ must be restricted to $\mathcal{O}$ before projecting. This matches the archimedean-observability boundary already implicit in the main paper's treatment of physical observables.

The main paper develops the points-and-topology framework for QOU in its categorical-foundations chapters. In that framework, points of a categorical structure live in an $R$-algebra for some coefficient ring $R$. For the surreal setting, the natural choice is $R = \mathcal{O}$ (finite surreals), with the archimedean quotient recovering $R = \mathbb{R}$. No new framework is introduced here; the Robinson standard-part construction fits the existing categorical framework.
<!-- FILE_END: valuation-ring-finite-surreals.md -->

<!-- FILE_START: classical-limit-stpart.md -->
Three blocks address the $q \to 1$ classical limit:

| Block | Scope | Status |
|---|---|---|
| [classical limit functor](#def:classical-limit-functor) | Topological definition $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$ | Definition (with obstruction) |
| **This block** | Single-functor surreal replacement: $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$ | Conjecture (open) |
| [archimedean QOU is standard-part of surreal](#conj:archimedean-stpart) | Whole-tuple surreal replacement on $(\mathbf{C}, \varTheta, G, \mathcal{S})$ | Conjecture (open) |

The current block provides the single-functor version; the whole-tuple version is the appendix companion. Both are likely equivalent modulo functoriality.

The [classical limit functor](#def:classical-limit-functor) $\mathrm{cl} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ takes the $q \to 1$ limit of categorical structures parametrised by the substrate parameter $q$. Classically, this requires a topological notion of limit on the parameter space or a careful Hochschild-cohomology construction ([classical limit obstruction](#def:classical-limit-obstruction)). This conjecture proposes a clean replacement: the classical-limit functor is the standard-part of evaluation at $q = 1 + \varepsilon$.

**Conjecture.** Let $\mathbf{C}_q$ be a $K$-linear :refterm[monoidal category]{#monoidal-category} whose structure constants are rational functions of $q \in K$, and let $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ be the topological classical-limit functor (defined when it exists). Set $K = \mathbf{No}$, fix an infinitesimal $\varepsilon \in \mathbf{No}$, and let $\mathrm{ev}_{1 + \varepsilon} : \mathbf{C}_q \to \mathbf{C}_{\mathbf{No}}$ be evaluation at $q = 1 + \varepsilon$. There is a natural isomorphism of functors

$$
  \mathrm{cl}_{\mathrm{top}} \cong \mathrm{St} \circ \mathrm{ev}_{1 + \varepsilon},
$$

whenever the left-hand side is defined. The right-hand side is defined more generally—wherever the structure constants make sense as rational expressions in $\varepsilon$.

The right-hand side always exists as long as the structure constants are rational in $\varepsilon$, even when the left-hand side has obstructions. The classical-limit obstruction $\mathrm{HH}^2(\mathcal{U}_q, \mathrm{Ad})$ becomes a non-zero finite surreal in $\mathbf{No}_{\mathrm{fin}}$ whose standard-part vanishes only when the obstruction itself vanishes. The obstruction is always detected in the surreal lift (as a non-trivial first-order $\varepsilon$-term), but it is "felt by the classical observer" only when the standard-part is non-zero.

The conjecture is open. It is partly motivated by Berarducci--Mantova's derivation construction (2018), which extends $d/dx$ on $\mathbb{R}$. Promoting this from a single function to a functor on $\mathbf{C}_q$ requires functoriality of the standard-part. A first step would be to prove the conjecture for $\mathbf{C}_q = \mathrm{Rep}(\mathrm{SU}_q(2))$.

The paper treats the $q \to 1$ classical limit archimedean-topologically. Under the surreal lift, the limit becomes a literal evaluation at a specific surreal—no topology required. Whether the two formulations give the same answer is the conjecture above. If true, the entire classical-limit discussion could be re-stated as standard-part identities, eliminating one source of analytic machinery.

The proof strategy splits into a single-morphism case and a naturality case. For the single-morphism case, specialise to $\mathbf{C} = \mathrm{Vect}_{\mathbb{Q}(q)}$ and a morphism given by a single rational function $f_q(x)$. Show that $\lim_{q \to 1} f_q$ equals $\mathrm{st}(f_{1+\varepsilon})$. This requires standard-part commuting with rational arithmetic on finite surreals. For naturality, generalise to a functor $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$. This requires functoriality of $\mathrm{St}$ on the $K$-linear category $\mathbf{C}_K$. Falsification requires a discontinuous-but-classically-limit-existing function, which is impossible for rational structure constants.
<!-- FILE_END: classical-limit-stpart.md -->

<!-- FILE_START: archimedean-stpart.md -->
An archimedean QOU $(\mathbf{C}, \varTheta, G, \mathcal{S})$ ([quantum observable universe](#def:quantum-observable-universe)) uses $K = \mathbb{R}$, a real Lie group $G$, and a real vector bundle $\mathcal{S}$. A surreal QOU uses $K = \mathbf{No}$ with all axioms relaxed to hold up to an infinitesimal $\varepsilon$:

| Axiom | Archimedean | Surreal |
|---|---|---|
| Frobenius pairing | $\int_A \circ \mu = \mathrm{id}$ | $= \mathrm{id} + O(\varepsilon)$ |
| Observability | $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ | $\leq \varepsilon$ |
| Volume | $g_{\mathbf{1}} = \mathrm{id}$ | $= (1 + \varepsilon) \mathrm{id}$ |
| Vacuum | $\mathrm{Geom}(\unicode{9737}) = 0$ | $= \varepsilon$ |

**Conjecture.** The standard-part functor $\mathrm{St}$ sends every surreal QOU to an archimedean QOU.

More precisely, there is a functor $\mathrm{St}_{\mathrm{QOU}} : \mathbf{QOU}_{\mathbf{No}}^{\varepsilon} \longrightarrow \mathbf{QOU}_{\mathbb{R}}$ defined by applying $\mathrm{St}$ to all hom-spaces. The functor is essentially surjective, and the composition $\mathrm{St}_{\mathrm{QOU}} \circ \iota$ is the identity.

If the conjecture holds, the surreal lift carries strictly more information than the archimedean theory. Each archimedean QOU has a fibre of surreal QOUs above it. The additional information is infinitesimal physics: first-order quantum corrections to the Frobenius pairing, observability cohomology, volume normalisation, and vacuum. Whether such corrections are physical or only mathematical is open.

This conjecture is the categorical counterpart of [classical limit as standard-part](#conj:classical-limit-stpart). The two conjectures are likely equivalent modulo functoriality.

If true, the $\varepsilon$-relaxation is a strict generalisation of the main paper. The main paper's QOU axioms are recovered via $\mathrm{St}_{\mathrm{QOU}}$. Every theorem in the main paper has a surreal counterpart, potentially with non-trivial first-order corrections that vanish under $\mathrm{St}$.

We reduce the proof to [classical-limit-stpart](#conj:classical-limit-stpart). First, show $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St}, \mathrm{St})$. Second, reduce each component: $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$, $\varTheta$ acts entry-wise, $G$ is the standard-part of an algebraic group object, and $\mathcal{S}$ is the standard-part of the fibre. Third, verify each $\varepsilon$-relaxed axiom becomes strict under $\mathrm{St}$. Finally, essential surjectivity is automatic by setting $\varepsilon = 0$. Falsification requires an $\varepsilon$-relaxed surreal QOU whose standard-part violates a strict QOU axiom.
<!-- FILE_END: archimedean-stpart.md -->

<!-- FILE_START: archimedean-stpart-strategy.md -->
Proof strategy for [archimedean QOU is the standard-part of surreal QOU](#conj:archimedean-stpart). The conjecture is the category-level counterpart of [classical-limit-stpart](#conj:classical-limit-stpart). Reduce to that conjecture via:

1. **Functorial reduction.** Show $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St}, \mathrm{St})$.
2. **Reduce each component**:
   - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at $q = 1 + \varepsilon$: $\mathrm{St}$ recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by [classical-limit-stpart](#conj:classical-limit-stpart).
   - $\varTheta : \mathbf{1} \to A$: $\mathrm{St}$ acts entry-wise.
   - $G = \mathrm{Aut}(A)$: standard-part of an algebraic group object. This is the categorical counterpart of the archimedean realization $\tau$ of [fibre functor rigidity](#rem:fibre-functor-rigidity).
   - $\mathcal{S}$: standard-part of fibre.
3. **Verify axioms.** Each $\varepsilon$-relaxed axiom becomes the strict axiom under $\mathrm{St}$.
4. **Essential surjectivity.** Every archimedean QOU lifts (set $\varepsilon = 0$).

Falsification requires an $\varepsilon$-relaxed surreal QOU whose standard-part image violates a strict QOU axiom. This would require an infinitesimal that becomes non-infinitesimal under standard-part, which is impossible by the definition of $\mathrm{st}$.
<!-- FILE_END: archimedean-stpart-strategy.md -->

