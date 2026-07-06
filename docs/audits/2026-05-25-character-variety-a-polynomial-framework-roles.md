# Character variety + A-polynomial in the QOU framework chain — 2026-05-25

**Trigger:** Author question following H_3/H_{3A} bug audit: "where do the Character Variety and the A-polynomial play a role? in relation to archimedean functor, dilog, Φ_q, eigen/generation functions, etc."

**Status:** Structural-role audit. Identifies wiring gaps for follow-up.

## §1. The three objects

| Object | Definition | Dimension |
|---|---|---|
| **Character variety** $X(K)$ | $\mathrm{Hom}(\pi_1(S^3 \setminus K), SL_2(\mathbb{C})) // SL_2$ | typically 2-complex-dim for knots |
| **A-polynomial** $A_K(L, M)$ | classical projection of $X(K)$ to cusp coordinates $(L, M)$ = (longitude eigenvalue, meridian eigenvalue) | 1-complex-dim curve |
| **Quantum A-polynomial** $\hat{A}_K(\hat{L}, \hat{M}; q)$ | q-difference operator annihilating the colored Jones tower | algebraic in q |

For the Borromean rings 𝓑_3 specifically:
- $X(\mathcal{B}_3)$ is known via Champanerkar-Kofman-Mullen (2008)
- $A_{\mathcal{B}_3}$ is computable from the Wirtinger presentation
- $\hat{A}_{\mathcal{B}_3}$ is implicit in the colored Jones recurrence

## §2. Framework roles — three points in the canonical chain

### Top of chain: character variety ↔ Mostow-Prasad selection

Mostow-Prasad rigidity says: for finite-volume hyperbolic 3-manifolds, the discrete-faithful representation $\rho: \pi_1(S^3 \setminus K) \to PSL_2(\mathbb{C})$ is **unique up to conjugation**. This means:

$$\rho \in X(K)$$

is a SINGLE distinguished point on the **geometric component** of $X(K)$ — the irreducible component containing the discrete-faithful repn. The substrate q_0 in the framework's algebra is the algebraic parameter compatible with this point.

**Framework wiring:** implicit. The substrate q_0 = 1.1097 (from CAL-2 / m_μ/m_e) is selected to match the geometric component of $X(\mathcal{B}_3)$, but the character variety is NOT explicitly computed in production.

### Middle of chain: A-polynomial ↔ Φ_q / Li_2^q (dilog) recurrence

The **AJ conjecture** (Garoufalidis):

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) = 0$$

where $J_N(K; q)$ is the N-colored Jones polynomial. The classical limit $q \to 1$ gives the A-polynomial.

The **Volume Conjecture** (Kashaev-Murakami-Murakami):

$$\lim_{N \to \infty} \frac{2\pi}{N} \log |J_N(K; e^{2\pi i / N})| = \mathrm{Vol}(K)$$

for hyperbolic K. The asymptotic is governed by:

$$J_N(K; e^{2\pi i / N}) \sim e^{N \cdot \mathrm{Li}_2(L_*) / (2\pi i)} \cdot (\text{corrections})$$

where $L_*$ is the "preferred" longitude eigenvalue from the geometric component.

**This is where Φ_q (Faddeev) and $\mathrm{Li}_2^q$ (Rogers) live in the framework.** The cheat sheet's distinction between them is the distinction between two different asymptotic regimes of $J_N$, both controlled by the A-polynomial.

**Framework wiring:** Φ_q is present in `_deprecated/thimble/` work + Pre-Archimedean derivation chain content blocks. The explicit A-polynomial / AJ-conjecture machinery is NOT wired to production.

### Bottom of chain: eigenfunctions of $\hat{A}_K$ ↔ Wedderburn Markov-trace

$\hat{A}_K$ is a q-difference operator on $\hat{L}$ and $\hat{M}$ (which satisfy $\hat{L}\hat{M} = q\hat{M}\hat{L}$). Its **eigenfunctions** are (regularized versions of) the colored Jones polynomials. Equivalently:

$$\mathrm{tr}_M^{(N)}(\beta_K) = J_N(K; q)$$

(with appropriate normalization). So the framework's Wedderburn sum:

$$\mathrm{tr}_M(\beta_K) = \sum_{\lambda \vdash n} y_\lambda \cdot \chi^\lambda(\beta_K)$$

IS exactly the eigenfunction-expansion side of the AJ conjecture for the level-N (with n related to N) colored Jones.

**Generating function**:
$$G_K(x; q) := \sum_{N \ge 0} J_N(K; q) \cdot x^N$$

For hyperbolic K, $G_K$ has Stokes-phenomenon structure (multiple saddle-points correspond to different irreducible components of $X(K)$), with the geometric component contributing the dominant exponential growth.

**Framework wiring:** $J_N$ via Markov trace is wired (`alpha_k_jones_markov_h3.py` + the H_4 atlas just landed). Generating function $G_K$ and explicit Stokes analysis are NOT wired.

## §3. Wiring status table

| Object | What | Wiring |
|---|---|---|
| $X(\mathcal{B}_3)$ | character variety of Borromean | ⏳ implicit in q_0 substrate; not explicitly computed |
| Mostow-Prasad uniqueness | geometric-component selection | ⏳ implicit, cited in audits |
| $A_{\mathcal{B}_3}(L, M)$ | classical A-polynomial | ❌ not computed; published in literature (Champanerkar) |
| $\hat{A}_{\mathcal{B}_3}$ | quantum A-polynomial / q-difference recurrence | ❌ not wired; AJ conjecture machinery absent |
| $\Phi_q$ Faddeev dilog | asymptotic regulator | ⏳ in `_deprecated/thimble/`, content blocks |
| $\mathrm{Li}_2^q$ Rogers dilog | asymptotic regulator | ⏳ partially present |
| $J_N(K; q)$ colored Jones | level-N Markov trace | ✅ wired (`alpha_k_jones_markov_h{3,4}.py`) |
| $G_K(x; q)$ generating function | Stokes scaffolding for J_N tower | ❌ not wired; research-grade |
| Eigenfunctions of $\hat{A}_K$ | = colored Jones with regularization | ❌ via Stokes-phenomenon analysis |

## §4. Connection to the framework's existing dualities

From the duality tracker (PR [#1139](https://github.com/litlfred/qou/pull/1139)):

- **D17 DIM master Pentagon** — Ding-Iohara-Miki master Pentagon specialises to Macdonald / Pachner / Bloch. The A-polynomial machinery sits at this level: $\hat{A}_K$ is built from quantum dilog primitives that compose via DIM.
- **D19 quantum-Langlands dual** — $H_n(q) \leftrightarrow H_n(q^{-1})$. The A-polynomial has a natural Langlands-dual structure via the (L, M) → (M, L) involution.

So A-polynomial wiring lives in the **D17 / D19 ⏳ scaffold** tier of the duality tracker — research-grade open, but tractable for 𝓑_3 specifically because:
- The classical A_{𝓑_3} is in the literature
- The colored Jones tower for 𝓑_3 is computable via Markov trace
- The AJ conjecture is PROVEN for many classes including the Borromean

## §5. What this enables for the framework

If A-polynomial machinery is wired:

1. **Direct check of Volume Conjecture for 𝓑_3** — asymptotic of $J_N$ at $q = e^{2\pi i / N}$ should give $\mathrm{Vol}(\mathcal{B}_3) = 8G$.
2. **Φ_q / Li_2^q context-sorting becomes derivable** rather than empirical — each is a specific saddle-point contribution governed by an A-polynomial component.
3. **The Markov-trace closed form** $(4 + h^2 − 3h^4 − h^6)/(h^2 + 4)$ becomes a CONSEQUENCE of the quantum A-polynomial recurrence, not a Jones-polynomial fact computed independently. This is the categorical derivation Path B (Tier 2 in the workplan) was looking for.

## §6. Tractable next steps

1. **Compute classical $A_{\mathcal{B}_3}$ from Wirtinger presentation** (in-session feasible, sympy) — gives explicit polynomial.
2. **Verify $A_{\mathcal{B}_3}$ matches Champanerkar 2008 / Cooper-Culler-Gillet-Long-Shalen reference**.
3. **Identify geometric component of $X(\mathcal{B}_3)$** via the discrete-faithful repn → eigenvalues of meridians.
4. **Map substrate q_0 to a specific (L, M) point** on the A-polynomial curve.
5. **Set up the quantum recurrence** $\hat{A}_{\mathcal{B}_3} \cdot J_N = 0$ as a Lean-verifiable q-difference identity (research-grade; ties to D17/D19).

## §7. Cross-references

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §Φ_q vs Li_2^q context-sorting
- [`docs/audits/2026-05-24-crystal-yekutieli-correspondence-chain.md`](2026-05-24-crystal-yekutieli-correspondence-chain.md) §11 (Mostow-Prasad)
- [`docs/duality-tracker.md`](../duality-tracker.md) D17 (DIM master Pentagon), D19 (quantum-Langlands)
- [`computations/alpha/alpha_k_jones_markov_h3.py`](../../computations/alpha/alpha_k_jones_markov_h3.py) — colored Jones via Markov
- [`computations/alpha/alpha_k_jones_markov_h4.py`](../../computations/alpha/alpha_k_jones_markov_h4.py) — H_4 extension (this PR)

## §8. Honest verdict

**The A-polynomial is the framework's most important missing primitive.** It's the natural categorical-derivation anchor for everything from $\Phi_q$ asymptotics to the Volume Conjecture to the Markov-trace closed form. Wiring it would:

- Convert several "empirical" identifications in the cheat sheet to derived statements
- Provide the Lean-formalization target for the rescoped Path B closure question (PR #1231 §11)
- Unlock the Stokes-phenomenon analysis that distinguishes Φ_q from Li_2^q contexts structurally

Cost estimate: classical A_{𝓑_3} computation is in-session feasible; full quantum recurrence + AJ conjecture verification is research-grade (~2-4 weeks).
