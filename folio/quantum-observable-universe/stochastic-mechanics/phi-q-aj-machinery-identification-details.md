This note expands the [$\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification): the full AJ-conjecture statement, the significance of the unified context-sorting, and the logical decomposition of the conditional proposition.

## Statement

Let $K$ be a hyperbolic knot complement and $J_N(K; q) \in \mathbb{Z}[q^{\pm 1}]$ its $N$-colored Jones polynomial. The AJ Conjecture asserts the existence of a non-trivial $q$-difference operator $\hat{A}_K \in \mathcal{A}_q$ such that:

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) \;=\; 0$$

where $\hat{M}f(M) := M\cdot f(M)$ and $\hat{L}f(M) := f(qM)$, with $\hat{L}\hat{M} = q\hat{M}\hat{L}$.

The Kashaev-Murakami-Murakami Volume Conjecture for hyperbolic $K$ is governed in the asymptotic by the geometric component of the classical A-polynomial $A_K(L, M)$.

The dilogarithm regulators that appear in the aether-evaluation chain are exactly:
- $\Phi_q$: saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q = e^{2\pi i / N}$ (root-of-unity asymptotic).
- $\mathrm{Li}_2^q$: saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q \in (0, 1)$ (real asymptotic, via Stokes).

The two regimes are related by the modular S-transform $q \leftrightarrow \tilde{q} = e^{2\pi i / \tau}$ ([modular $S$-transform conjecture](#conj:modular-s-transform-q-q-tilde)).

## Significance

The framework distinguishes $\Phi_q$ and $\mathrm{Li}_2^q$ contexts as two archimedean saddle evaluations of a single algebraic object ($\hat{A}_K$). Making this explicit unifies the context-sorting into one algebraic statement over $\mathbb{Z}[q^{\pm 1}]$, through which the pre-archimedean / archimedean split passes. The concrete root-of-unity saddle for the figure-eight knot (the $\theta = \pi/3$ critical point of $\mathrm{Im}\,\mathrm{Li}_2(e^{i\theta})$, evaluating to $\mathrm{Vol}(4_1)$) is computed once in [the dilog saddle regime](#rem:dilog-saddle-regime).

## Logical decomposition

The conditional proposition separates an unconditional algebraic backbone (the $q$-Weyl relation $\hat{L}\hat{M} = q\hat{M}\hat{L}$, closure of the solution space under linear combinations, and disjointness of the root-of-unity and real saddle regimes) from the conjectural hypotheses carrying the AJ identity and the Faddeev/Rogers asymptotic identifications.
