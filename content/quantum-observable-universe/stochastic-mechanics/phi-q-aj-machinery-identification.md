**Proposition (conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)).**

*Let $K$ be a hyperbolic knot or link with cusp coordinates $(L, M)$ and quantum A-polynomial $\hat{A}_K \in \mathcal{A}_q$ (the q-Weyl algebra over $\mathbb{Z}[q^{\pm 1}]$). Then the $\Phi_q$ (Faddeev dilogarithm) and $\mathrm{Li}_2^q$ (Rogers dilogarithm) asymptotic regulators that appear in the framework are specific saddle-point regimes of the AJ-conjecture machinery $\hat{A}_K \cdot J_N(K; q) = 0$. The identification is algebraic over $\mathbb{Z}[q^{\pm 1}]$ on both sides. The difference between $\Phi_q$ and $\mathrm{Li}_2^q$ contexts is the choice of archimedean saddle (real vs root-of-unity).*

## Statement

Let $K$ be a hyperbolic knot complement and $J_N(K; q) \in \mathbb{Z}[q^{\pm 1}]$ its $N$-colored Jones polynomial. The AJ Conjecture asserts the existence of a non-trivial $q$-difference operator $\hat{A}_K \in \mathcal{A}_q$ such that:

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) \;=\; 0$$

where $\hat{M}f(M) := M\cdot f(M)$ and $\hat{L}f(M) := f(qM)$, with $\hat{L}\hat{M} = q\hat{M}\hat{L}$.

The Kashaev-Murakami-Murakami Volume Conjecture for hyperbolic $K$ is governed in the asymptotic by the geometric component of the classical A-polynomial $A_K(L, M)$.

The dilogarithm regulators that appear in the substrate-evaluation chain are exactly:
- $\Phi_q$: saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q = e^{2\pi i / N}$ (root-of-unity asymptotic).
- $\mathrm{Li}_2^q$: saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q \in (0, 1)$ (real asymptotic, via Stokes).

The two regimes are related by the modular S-transform $q \leftrightarrow \tilde{q} = e^{2\pi i / \tau}$ ([`conj:modular-s-transform-q-q-tilde`](modular-s-transform-q-q-tilde.md), D14).

## Significance

The framework previously distinguished $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically. Per the AJ identification, both are the same algebraic object ($\hat{A}_K$) viewed through different archimedean lenses. Wiring this explicitly unifies the context-sorting into a single algebraic statement. It provides the categorical-derivation target for the Path B closure question. The AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$; the framework's Pre-Archimedean / Archimedean split passes through this algebraic gate. The concrete root-of-unity saddle for the figure-eight knot — the $\theta = \pi/3$ critical point of $\mathrm{Im}\,\mathrm{Li}_2(e^{i\theta})$, evaluating to $\mathrm{Vol}(4_1)$ — is computed once in [the dilog saddle regime](#rem:dilog-saddle-regime).

## Lean structure

[`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a conditional proposition. The backbone is proved unconditionally: the $q$-Weyl relation, closure of the solution space under linear combinations, and disjointness of the saddle regimes. The conjectural class inputs carry the AJ conjecture's content and the Faddeev/Rogers identifications.

The classes encode literature statements. The framework's contribution is the identification at the algebraic level.

**Archimedean specialisation (§7c).** The $\Phi_q$ / $A_J$ regulator identities are stated over real $q$ with the archimedean ordering $0 < q < 1$. This real-analytic regime is the archimedean side of the substrate wall.
