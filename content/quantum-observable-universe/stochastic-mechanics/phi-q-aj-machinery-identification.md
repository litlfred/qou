**Proposition (conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)).**

Let $K$ be a hyperbolic knot or link with cusp coordinates $(L, M)$ and quantum A-polynomial $\hat{A}_K \in \mathcal{A}_q$ (the q-Weyl algebra over $\mathbb{Z}[q^{\pm 1}]$). Then the $\Phi_q$ (Faddeev dilogarithm) and $\mathrm{Li}_2^q$ (Rogers dilogarithm) asymptotic regulators that appear in the framework's volume-conjecture and substrate-evaluation routes are specific saddle-point regimes of the AJ-conjecture machinery $\hat{A}_K \cdot J_N(K; q) = 0$. The identification is algebraic over $\mathbb{Z}[q^{\pm 1}]$ on both sides. The difference between $\Phi_q$ and $\mathrm{Li}_2^q$ contexts is the choice of archimedean saddle (real vs root-of-unity).

## Statement

Let $K$ be a hyperbolic knot complement and $J_N(K; q) \in \mathbb{Z}[q^{\pm 1}]$ its $N$-colored Jones polynomial. The AJ Conjecture (Garoufalidis 2004) asserts the existence of a non-trivial q-difference operator $\hat{A}_K \in \mathcal{A}_q$ such that

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) \;=\; 0$$

where $\hat{M}f(M) := M\cdot f(M)$ and $\hat{L}f(M) := f(qM)$, with $\hat{L}\hat{M} = q\hat{M}\hat{L}$.

The Kashaev-Murakami-Murakami Volume Conjecture for hyperbolic $K$ states

$$\lim_{N \to \infty} \frac{2\pi}{N} \log |J_N(K; e^{2\pi i / N})| \;=\; \mathrm{Vol}(K).$$

The geometric component of the classical A-polynomial $A_K(L, M)$ governs this asymptotic (Garoufalidis-Lê 2015; Hikami 2003).

We identify the dilogarithm regulators in the substrate-evaluation chain. The Faddeev regulator $\Phi_q$ drives the pre-archimedean derivation. The Rogers regulator $\mathrm{Li}_2^q$ drives the categorical Schur-Weyl path. We claim:

- $\Phi_q$ is the saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q = e^{2\pi i / N}$ (root-of-unity asymptotic).
- $\mathrm{Li}_2^q$ is the saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q \in (0, 1)$ (real asymptotic, via Stokes).

The modular S-transform $q \leftrightarrow \tilde{q} = e^{2\pi i / \tau}$ relates the two regimes ([`conj:modular-s-transform-q-q-tilde`](modular-s-transform-q-q-tilde.md), D14).

## Significance

The framework's [`canonical-derivation-cheat-sheet.md`](../../../docs/canonical-derivation-cheat-sheet.md) currently distinguishes $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically. We choose the regulator yielding the cleaner algebraic expression. The AJ identification guarantees that both regulators represent the same algebraic object $\hat{A}_K$ viewed through different archimedean lenses. Wiring this explicitly achieves three goals:

1. We unify the cheat-sheet's context-sorting into a single algebraic statement.
2. We provide the categorical-derivation target for the Path B closure question from PR [#1231](https://github.com/litlfred/qou/pull/1231) §11: "Why does the Markov-trace closed form have these coefficients?"
3. We ground the pre-archimedean structure. The AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$. The framework's pre-archimedean/archimedean split passes through this algebraic gate.

## Lean structure

The file [`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a conditional proposition under §3b-cond. We split it into a provable backbone and conjectural class inputs.

**Proved unconditionally:**

- `qWeyl_commutation` establishes the q-Weyl relation $\hat{L}\hat{M} = q\hat{M}\hat{L}$ on the function model.
- `Annihilates.add_smul` shows the solution space of a homogeneous q-difference operator is closed under superposition.
- `saddle_regimes_disjoint` proves the two archimedean regimes are genuinely distinct. A real $q \in (0,1)$ satisfies $q^N \neq 1$, so no parameter lies in both regimes.

**Conjectural class inputs:**

- `QuantumAPolynomial F K` carries the AJ conjecture's content. It provides the operator $\hat{A}_K$, the colored Jones tower, the annihilation relation, and non-triviality.
- `PhiQRegulator F K` carries the Faddeev identification. It asserts $\hat{A}_K$ annihilates the $\Phi_q$-generated saddle tower in the root-of-unity regime ($q^N = 1$, $q \neq 1$).
- `Li2QRegulator K` carries the Rogers identification. It asserts $\hat{A}_K$ annihilates the $\mathrm{Li}_2^q$-generated saddle tower in the real regime $q \in (0,1)$.

**Derived conditional theorems:**

- `phi_q_eq_aj_saddle_root_of_unity`: At every root-of-unity parameter, every linear combination of the Jones tower and the $\Phi_q$ saddle tower is annihilated by $\hat{A}_K$.
- `li2_q_eq_aj_saddle_real`: The analogous statement holds at real $q \in (0,1)$ for $\mathrm{Li}_2^q$.
- `phi_q_li2_q_unified_via_aj`: The regimes are disjoint, showing the two lenses on $\hat{A}_K$ are independent.

The framework contributes the identification at the algebraic-over-$\mathbb{Z}[q^{\pm 1}]$ level. The analytic asymptotic growth extraction remains an open class input.

## Conditional dependencies

The full identification is conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) and [`conj:dim-master-pentagon`](dim-master-pentagon.md) because it requires:

1. Proof of the AJ conjecture for $K$.
2. Exact matching between the framework's Faddeev/Rogers identifications and the literature.

For $\mathcal{B}_3$ specifically, the classical A-polynomials and Bloch invariants are established (Champanerkar 2003; Hikami). The open task is explicitly verifying that the framework's $\Phi_q$ and $\mathrm{Li}_2^q$ choices align with the AJ saddles.

**Cross-reference:** See [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §9 for full background.

**Archimedean specialisation (§7c).** The regulator identities are stated over real $q$ with the archimedean ordering $0 < q < 1$. This real-analytic regime is the archimedean side of the substrate wall for the generic quantum-$A$-polynomial machinery.
