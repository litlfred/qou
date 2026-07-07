<!-- FILE_START: stochastic-mechanics-orphan-reconnect-intro.md -->
Blocks in this section were reconnected during the Phase 7 orphan audit. They address supplementary stochastic-mechanics content awaiting thematic placement.
<!-- FILE_END: stochastic-mechanics-orphan-reconnect-intro.md -->

<!-- FILE_START: lusztig-canonical-basis-q-eq-1.md -->
**Conjecture (D24 Lusztig canonical basis closure, conditional on [`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)).**

*At the classical limit $q = 1$, the Kashiwara crystal of $H_n(q)$ ([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy), D12 at $q \to 0$) **decategorifies** to the Lusztig canonical basis of the group algebra $\mathbb{Z}[S_n]$. The Kazhdan–Lusztig basis polynomials $\{P_{y, w}(q)\}$ are the structure constants of this decategorification. At $q = 1$, they reduce to integer multiplicities of canonical-basis elements.*

*Combined with the $q \to 0$ Kashiwara limit (D12) and the $q \to \infty$ reverse limit ([D13](reverse-limit-q-to-infinity.md)), D24 completes the Cluster D limit-duality picture for $H_n(q)$:*

$$
  \begin{array}{c}
    q \to 0 \text{ (Kashiwara crystal)} \\
    \updownarrow \text{ bar} \\
    q \to \infty \text{ (reverse crystal, D13)} \\
    \\
    q = 1 \text{ (Lusztig canonical basis, this conjecture)} \\
    \updownarrow \text{ specialise} \\
    q = q_0 \text{ (substrate, framework production)} \\
  \end{array}
$$

## The full Cluster D limit-duality picture

| Limit | Categorical structure | Tracker row |
|-------|----------------------|-------------|
| $q = 1$ (classical) | Lusztig canonical basis / KL polynomials | **D24** (this conjecture) |
| $q = q_0$ (substrate $\approx$ 1.11) | full Hecke algebra | (production, all rows) |
| $q \to 0$ (Kashiwara) | crystal basis / 0-Hecke | D12 |
| $q \to \infty$ (reverse) | bar-image of Kashiwara | D13 |

D24 ties D12 (Kashiwara) to D1 (bar) via the decategorification functor: the Lusztig canonical basis at $q = 1$ is the bar-invariant Kazhdan–Lusztig basis of the group algebra. The Kashiwara crystal at $q \to 0$ is its quantum lift via canonical-basis-preserving deformation.

## Connection to D9 (isospin) and D22 (Type-B folding)

- The isospin $\mathbb{Z}/2$ swap (D9) acts on the Lusztig canonical basis as the sign character of the abelianised $S_n$. This provides a classical-limit picture of the canonical isospin.
- Type-B folding (D22) provides the symmetric-crystal structure that descends to a bar-invariant Lusztig basis at $q = 1$. This closes the Cluster A (CPT) story at the decategorification level.

## Diagnostics

- **GB filtration**: KL polynomials are filtered by length $\ell(w)$, the same filtration as the Hecke algebra.
- **Jet order**: evaluated at $q = 1$, the KL polynomials are integers (the canonical-basis multiplicities).
- **Bar-symmetry**: bar-symmetric by construction.
<!-- FILE_END: lusztig-canonical-basis-q-eq-1.md -->

<!-- FILE_START: phi-q-aj-machinery-identification.md -->
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

The framework previously distinguished $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically. Per the AJ identification, both are the same algebraic object ($\hat{A}_K$) viewed through different archimedean lenses. Wiring this explicitly unifies the context-sorting into a single algebraic statement. It provides the categorical-derivation target for the Path B closure question. The AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$; the framework's Pre-Archimedean / Archimedean split passes through this algebraic gate.

## Lean structure

[`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a conditional proposition. The backbone is proved unconditionally: the $q$-Weyl relation, closure of the solution space under linear combinations, and disjointness of the saddle regimes. The conjectural class inputs carry the AJ conjecture's content and the Faddeev/Rogers identifications.

The classes encode literature statements. The framework's contribution is the identification at the algebraic level.

**Archimedean specialisation (§7c).** The $\Phi_q$ / $A_J$ regulator identities are stated over real $q$ with the archimedean ordering $0 < q < 1$. This real-analytic regime is the archimedean side of the substrate wall.
<!-- FILE_END: phi-q-aj-machinery-identification.md -->

<!-- FILE_START: reverse-limit-q-to-infinity.md -->
**Theorem (D13 reverse-limit closure — algebraic fragment).**

*The Kashiwara crystal limit $q \to 0$ ([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy), D12) has a structural counterpart at $q \to \infty$, related to the $q \to 0$ limit by the bar involution $q \mapsto q^{-1}$ ([`def:bar-involution`](#def:bar-involution), D1).*

*The $q \to \infty$ limit produces a "reverse crystal" whose combinatorial structure is the bar-image of the Kashiwara crystal, with the same combinatorial invariants but inverted $q$-character orderings. Together, the pair $(q \to 0, q \to \infty)$ + the classical limit $q = 1$ + the substrate $q = q_0$ form the complete picture of limit dualities on $H_n(q)$.*

## The four canonical limits of $H_n(q)$

| Limit | Categorical content | Pairing via bar |
|-------|---------------------|-----------------|
| **$q = 1$** (classical) | Lusztig canonical basis / KL polynomials | self-paired (bar fixes $q = 1$) |
| **$q = q_0$** (substrate) | full Hecke at the framework's calibration point | bar-paired with $q = q_0^{-1}$ |
| **$q \to 0$** (Kashiwara) | crystal basis, 0-Hecke quotient | bar-paired with $q \to \infty$ (this conjecture) |
| **$q \to \infty$** (reverse limit) | reverse crystal | bar-paired with $q \to 0$ |

## The structural content

Per [`def:bar-involution`](#def:bar-involution), $q \mapsto q^{-1}$ swaps $q = 0$ with $q = \infty$. The Kashiwara crystal structure at $q \to 0$ has a mirror at $q \to \infty$:
- Crystal nodes $\leftrightarrow$ reverse-crystal nodes.
- Crystal arrows of weight $i$ $\leftrightarrow$ reverse-crystal arrows of weight $-i$.

The conjecture is that this is a true categorical duality. Every Kashiwara crystal construction has a reverse-crystal analogue at $q \to \infty$, related by bar.

## Significance

If matter is identified with Kashiwara crystal fixed points (at $q \to 0$), antimatter corresponds to reverse-crystal fixed points (at $q \to \infty$), and the bar involution swaps them. This gives a structural source for matter-antimatter conjugation orthogonal to the color-tube C action of [D6](c-from-color-flavor-swap.md).

## Diagnostics

- **GB filtration level**: same as the Kashiwara crystal at $q \to 0$.
- **Jet order**: $h^0$.
- **Bar-symmetry status**: bar-paired by construction.
<!-- FILE_END: reverse-limit-q-to-infinity.md -->

<!-- FILE_START: outro-stochastic-mechanics.md -->
This closes the stochastic-mechanics chapter. The Markov closure map, $\varphi_q$ AJ machinery, Lusztig canonical basis at $q = 1$, and reverse limit $q \to \infty$ assembled here give the substrate-level stochastic content that the classical-limit and information-theoretic chapters consume as input. The reconnected orphan blocks land the bridge between the Markov closure map and the classical-limit construction explicitly, closing the stochastic-mechanics narrative arc.

The next chapter extracts the hyperbolic-volume content that pairs with the substrate-level mass spectrum. The subsequent chapters specialise the duality to atomic isotopes and the $\beta$-decay $Q$-value predictions.
<!-- FILE_END: outro-stochastic-mechanics.md -->
