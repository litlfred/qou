This note expands [$\Phi_q$ / $\mathrm{Li}_2^q$ machinery is the AJ-conjecture machinery](#prop:phi-q-aj-machinery-identification): the full AJ-conjecture statement, the significance of the unified context-sorting, and the logical structure of the conditional proposition.

## Statement

Let $K$ be a hyperbolic knot complement and $J_N(K; q) \in \mathbb{Z}[q^{\pm 1}]$ its $N$-colored Jones polynomial. The AJ Conjecture asserts the existence of a non-trivial $q$-difference operator $\hat{A}_K \in \mathcal{A}_q$ such that:

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) \;=\; 0$$

where $\hat{M}f(M) := M\cdot f(M)$ and $\hat{L}f(M) := f(qM)$, with $\hat{L}\hat{M} = q\hat{M}\hat{L}$.

The Kashaev-Murakami-Murakami Volume Conjecture for hyperbolic $K$ is governed in the asymptotic by the geometric component of the classical A-polynomial $A_K(L, M)$.

The dilogarithm regulators that appear in the substrate-evaluation chain are exactly:
- $\Phi_q$: saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q = e^{2\pi i / N}$ (root-of-unity asymptotic).
- $\mathrm{Li}_2^q$: saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q \in (0, 1)$ (real asymptotic, via Stokes).

The two regimes are related by the modular S-transform $q \leftrightarrow \tilde{q} = e^{2\pi i / \tau}$ ([modular $S$-transform $q \leftrightarrow \tilde q$](../q-geometric-langlands/modular-s-transform-q-q-tilde.md)).

## Significance

The framework previously distinguished $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically. Per the AJ identification, both are the same algebraic object ($\hat{A}_K$) viewed through different archimedean lenses. Wiring this explicitly unifies the context-sorting into a single algebraic statement. It provides the categorical-derivation target for the closure question. The AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$; the framework's Pre-Archimedean / Archimedean split passes through this algebraic gate. The concrete root-of-unity saddle for the figure-eight knot — the $\theta = \pi/3$ critical point of $\mathrm{Im}\,\mathrm{Li}_2(e^{i\theta})$, evaluating to $\mathrm{Vol}(4_1)$ — is computed once in [the dilog saddle regime](#rem:dilog-saddle-regime).

## Logical structure

The proposition is conditional. The backbone is proved unconditionally: the $q$-Weyl relation, closure of the solution space under linear combinations, and disjointness of the saddle regimes. The conjectural inputs carry the AJ conjecture's content and the Faddeev/Rogers identifications.

The conjectural inputs are statements from the literature. The framework's contribution is the identification at the algebraic level.

**Archimedean specialisation.** The $\Phi_q$ / $A_J$ regulator identities are stated over real $q$ with the archimedean ordering $0 < q < 1$. This real-analytic regime is the archimedean side of the substrate wall.

**Modularity across $|q| = 1$.** Garoufalidis and Wheeler call a linear $q$-difference equation *modular* when, for every $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, the cocycle $\Omega_\gamma$ built from its fundamental solutions at $0$ and $\infty$ extends meromorphically from $\tau \in \mathbb{C}\setminus\mathbb{R}$ to a cut plane, so that its restrictions to $\mathrm{Im}\,\tau > 0$ and $\mathrm{Im}\,\tau < 0$ determine each other \cite[\S1, Def.~1.1 and comment~1]{garoufalidis-wheeler-modular}. Here $q = e^{2\pi i\tau}$, so the real line in $\tau$ is the circle $|q| = 1$ on which the root-of-unity regime of $\Phi_q$ sits, while the regime $0 < q < 1$ lies inside the disc. Checking the monodromy relation at the generators $S$ and $T$ suffices for all of $\mathrm{SL}_2(\mathbb{Z})$ \cite[Thm.~1.2(a)]{garoufalidis-wheeler-modular}. The source proves modularity for the generalised $q$-hypergeometric equation, whose two natural cocycles coincide \cite[Thm.~1.4]{garoufalidis-wheeler-modular}, and for three modules of complex Chern--Simons theory whose cocycles are the Faddeev quantum dilogarithm, the Appell--Lerch sums and the Andersen--Kashaev state integral of $4_1$ \cite[\S1.5, Thms.~1.5--1.7]{garoufalidis-wheeler-modular}. For the operator $\hat A_K$ of the AJ statement above, modularity is the source's conjecture, not its theorem (comment~5 after Def.~1.1), so it adds no unconditional input to the proposition.
