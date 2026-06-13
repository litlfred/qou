**Proposition (conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)).**

*Let $K$ be a hyperbolic knot or link with cusp coordinates $(L, M)$ and quantum A-polynomial $\hat{A}_K \in \mathcal{A}_q$ (the q-Weyl algebra over $\mathbb{Z}[q^{\pm 1}]$). Then the $\Phi_q$ (Faddeev dilogarithm) and $\mathrm{Li}_2^q$ (Rogers dilogarithm) asymptotic regulators that appear in the framework's volume-conjecture and substrate-evaluation routes are **specific saddle-point regimes of the AJ-conjecture machinery** $\hat{A}_K \cdot J_N(K; q) = 0$. The identification is algebraic over $\mathbb{Z}[q^{\pm 1}]$ on both sides; the difference between $\Phi_q$ and $\mathrm{Li}_2^q$ contexts is the choice of archimedean saddle (real vs root-of-unity).*

## Statement

Let $K$ be a hyperbolic knot complement and $J_N(K; q) \in \mathbb{Z}[q^{\pm 1}]$ its N-colored Jones polynomial. The AJ Conjecture (Garoufalidis 2004) asserts the existence of a non-trivial q-difference operator $\hat{A}_K \in \mathcal{A}_q$ such that:

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) \;=\; 0$$

where $\hat{M}f(M) := M\cdot f(M)$ and $\hat{L}f(M) := f(qM)$, with $\hat{L}\hat{M} = q\hat{M}\hat{L}$.

The Kashaev-Murakami-Murakami Volume Conjecture for hyperbolic $K$:

$$\lim_{N \to \infty} \frac{2\pi}{N} \log |J_N(K; e^{2\pi i / N})| \;=\; \mathrm{Vol}(K)$$

is governed in the asymptotic by the geometric component of the classical A-polynomial $A_K(L, M)$ (Garoufalidis-Lê 2015; Hikami 2003).

**The framework's identification:** the dilogarithm regulators that appear in the substrate-evaluation chain — $\Phi_q$ (Faddeev, used in the Pre-Archimedean derivation) and $\mathrm{Li}_2^q$ (Rogers, used in the categorical Schur-Weyl path) — are exactly:

- $\Phi_q$ = saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q = e^{2\pi i / N}$ (root-of-unity asymptotic)
- $\mathrm{Li}_2^q$ = saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q \in (0, 1)$ (real asymptotic, via Stokes)

The two regimes are related by the modular S-transform $q \leftrightarrow \tilde{q} = e^{2\pi i / \tau}$ ([`conj:modular-s-transform-q-q-tilde`](modular-s-transform-q-q-tilde.md), D14 in the duality tracker).

## Why this matters

The framework's [`canonical-derivation-cheat-sheet.md`](../../../docs/canonical-derivation-cheat-sheet.md) currently distinguishes $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically — using one or the other depending on which gives the cleaner expression for a given derivation. Per the AJ identification, both are the **same algebraic object** ($\hat{A}_K$) viewed through different archimedean lenses. Wiring this explicitly:

1. **Unifies the cheat-sheet's context-sorting** into a single algebraic statement.
2. **Provides the categorical-derivation target** for the rescoped Path B closure question from PR [#1231](https://github.com/litlfred/qou/pull/1231) §11: "why does the Markov-trace closed form have the coefficients it does?"
3. **Pre-Archimedean**: the AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$ (no $\mathbb{R}$ or $\mathbb{C}$ needed); the framework's Pre-Archimedean / Archimedean split passes through this algebraic gate.

## Lean structure

[`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a **conditional proposition** under §3b-cond:

- Class `QuantumAPolynomial K` axiomatizes the AJ conjecture (existence of $\hat{A}_K$)
- Class `PhiQRegulator K` axiomatizes the Faddeev dilog regime
- Class `Li2QRegulator K` axiomatizes the Rogers dilog regime
- Theorem `phi_q_eq_aj_saddle_root_of_unity`: given `[QuantumAPolynomial K] [PhiQRegulator K]`, $\Phi_q$ equals the AJ saddle at $q = e^{2\pi i / N}$
- Theorem `li2_q_eq_aj_saddle_real`: given `[QuantumAPolynomial K] [Li2QRegulator K]`, $\mathrm{Li}_2^q$ equals the AJ saddle at real $q$

Both theorems are **fully verified by Lean** modulo the three class instances. The classes encode literature statements (AJ conjecture, dilog identities); the framework's contribution is the IDENTIFICATION at the algebraic-over-$\mathbb{Z}[q^{\pm 1}]$ level.

## Conditional dependencies

**Conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)** because the full identification requires:

1. AJ conjecture proved for $K$ (proved for many: 2-bridge knots, twist knots, most Rolfsen-table knots; status for 𝓑_3 specifically needs literature check — Hikami / Habiro)
2. The Faddeev / Rogers identifications used in the framework match the literature's exactly (not just up to convention)

For 𝓑_3 specifically, the algebraic side is in literature (Champanerkar-Kofman-Mullen 2008 for classical A-polynomial; Hikami for related quantum work). What's open: explicit verification that the framework's $\Phi_q$ / $\mathrm{Li}_2^q$ choices align with the AJ machinery's saddles.

**Cross-reference:** [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §9 (AJ conjecture crosses archimedean wall) for full background.
