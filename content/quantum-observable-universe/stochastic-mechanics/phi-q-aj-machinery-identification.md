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

## Significance

The framework's [`canonical-derivation-cheat-sheet.md`](../../../docs/canonical-derivation-cheat-sheet.md) currently distinguishes $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically — using one or the other depending on which gives the cleaner expression for a given derivation. Per the AJ identification, both are the **same algebraic object** ($\hat{A}_K$) viewed through different archimedean lenses. Wiring this explicitly:

1. **Unifies the cheat-sheet's context-sorting** into a single algebraic statement.
2. **Provides the categorical-derivation target** for the rescoped Path B closure question from PR [#1231](https://github.com/litlfred/qou/pull/1231) §11: "why does the Markov-trace closed form have the coefficients it does?"
3. **Pre-Archimedean**: the AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$ (no $\mathbb{R}$ or $\mathbb{C}$ needed); the framework's Pre-Archimedean / Archimedean split passes through this algebraic gate.

## Lean structure

[`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a **conditional proposition** under §3b-cond, split explicitly into a provable backbone and conjectural class inputs.

**Proved unconditionally (sorry-free):**

- `qWeyl_commutation` — the q-Weyl relation $\hat{L}\hat{M} = q\hat{M}\hat{L}$ on the function model $\hat{M}f(m) = m \cdot f(m)$, $\hat{L}f(m) = f(qm)$.
- `Annihilates.add_smul` — the solution space of a homogeneous q-difference operator is closed under linear combinations (superposition).
- `saddle_regimes_disjoint` — the two archimedean regimes are genuinely distinct: a real $q \in (0,1)$ satisfies $q^N \neq 1$, so no parameter lies in both regimes.

**Conjectural class inputs (no instances fabricated):**

- Class `QuantumAPolynomial F K` carries the AJ conjecture's content: the operator $\hat{A}_K$ (order, coefficients, homogeneity), the colored Jones tower, the annihilation $\hat{A}_K \cdot J_N = 0$, and non-triviality.
- Class `PhiQRegulator F K` carries the Faddeev identification: the $\Phi_q$-generated saddle tower is annihilated by the same $\hat{A}_K$ in the root-of-unity regime ($q^N = 1$, $q \neq 1$).
- Class `Li2QRegulator K` carries the Rogers identification: the $\mathrm{Li}_2^q$-generated saddle tower is annihilated by the same $\hat{A}_K$ in the real regime $q \in (0,1)$ (stated over $\mathbb{R}$, the archimedean side of the wall).

**Derived conditional theorems** (they compose class fields through the proved superposition lemma — they do not project a conclusion-typed field):

- `phi_q_eq_aj_saddle_root_of_unity`: at every root-of-unity parameter, the Jones tower and the $\Phi_q$ saddle tower lie in the *same* solution space of $\hat{A}_K$ — every linear combination is annihilated.
- `li2_q_eq_aj_saddle_real`: the same at real $q \in (0,1)$ for $\mathrm{Li}_2^q$.
- `phi_q_li2_q_unified_via_aj`: the two lenses on the one algebraic object $\hat{A}_K$ are genuinely different — the regimes are disjoint (unconditional).

The classes encode literature statements (AJ conjecture, dilog-saddle identifications); the framework's contribution is the IDENTIFICATION at the algebraic-over-$\mathbb{Z}[q^{\pm 1}]$ level. The analytic half of the saddle-point statement (asymptotic growth extraction) remains part of the open class inputs.

## Conditional dependencies

**Conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)** because the full identification requires:

1. AJ conjecture proved for $K$ (proved for many: 2-bridge knots, twist knots, most Rolfsen-table knots; status for 𝓑_3 specifically needs literature check — Hikami / Habiro)
2. The Faddeev / Rogers identifications used in the framework match the literature's exactly (not just up to convention)

For 𝓑_3 specifically, the algebraic side is in literature (Champanerkar 2003 for classical A-polynomials and Bloch invariants of hyperbolic 3-manifolds; Hikami for related quantum work). What's open: explicit verification that the framework's $\Phi_q$ / $\mathrm{Li}_2^q$ choices align with the AJ machinery's saddles.

**Cross-reference:** [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §9 (AJ conjecture crosses archimedean wall) for full background.

**Archimedean specialisation (§7c).** The $\Phi_q$ / $A_J$ regulator identities are stated over real $q$ with the archimedean ordering $0 < q < 1$; this real-analytic regime is the archimedean side of the substrate wall for the generic quantum-$A$-polynomial machinery, acknowledged here.
